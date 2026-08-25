#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <random>
#include <chrono>
#include <thread>
#include <future>
#include <numeric>
#include <algorithm>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <deque>
#include <set>
#include <map>
#include <span>
#include <concepts>
#include <ranges>

// ============================================================================
// CONSTANTS & CANONICAL PRIORS
// ============================================================================
constexpr double DEFAULT_MU_0 = 0.3989422804014327;     // 1 / sqrt(2 * pi)
constexpr double DEFAULT_LAMBDA_0 = 1.718281828459045;   // e - 1
constexpr int DEFAULT_NODES = 100;
constexpr int DEFAULT_RUNS = 100;
constexpr int DEFAULT_MAX_STEPS = 1500;

// ============================================================================
// COMPACT SPARSE DIRECTED GRAPH (C++20 - ZERO EXCESS RAM)
// ============================================================================
struct TargetEdge {
    int target;
    int H;
    auto operator<=>(const TargetEdge&) const = default;
};

struct Cycle3 {
    int u;
    int v;
    int w;
    auto operator<=>(const Cycle3&) const = default;
};

class DiGraph {
public:
    int n;
    std::vector<std::vector<TargetEdge>> succ;
    std::vector<std::vector<TargetEdge>> pred;

    explicit DiGraph(int num_nodes = 0) : n(num_nodes) {
        init(num_nodes);
    }

    void init(int num_nodes) {
        n = num_nodes;
        succ.assign(n, {});
        pred.assign(n, {});
    }

    inline bool has_edge(int u, int v) const {
        if (u < 0 || u >= n || v < 0 || v >= n) return false;
        for (const auto& e : succ[u]) {
            if (e.target == v) return true;
        }
        return false;
    }

    inline int get_H(int u, int v) const {
        if (u < 0 || u >= n || v < 0 || v >= n) return 0;
        for (const auto& e : succ[u]) {
            if (e.target == v) return e.H;
        }
        return 0;
    }

    void add_edge(int u, int v, int timestamp) {
        if (u < 0 || u >= n || v < 0 || v >= n) return;
        for (auto& e : succ[u]) {
            if (e.target == v) {
                e.H = timestamp;
                for (auto& pe : pred[v]) {
                    if (pe.target == u) {
                        pe.H = timestamp;
                        return;
                    }
                }
                return;
            }
        }
        succ[u].push_back({v, timestamp});
        pred[v].push_back({u, timestamp});
    }

    void remove_edge(int u, int v) {
        if (u < 0 || u >= n || v < 0 || v >= n) return;
        for (size_t i = 0; i < succ[u].size(); ++i) {
            if (succ[u][i].target == v) {
                succ[u].erase(succ[u].begin() + i);
                break;
            }
        }
        for (size_t i = 0; i < pred[v].size(); ++i) {
            if (pred[v][i].target == u) {
                pred[v].erase(pred[v].begin() + i);
                break;
            }
        }
    }

    int max_in_height(int u) const {
        int max_h = 0;
        for (const auto& pe : pred[u]) {
            if (pe.H > max_h) {
                max_h = pe.H;
            }
        }
        return max_h;
    }
};

// ============================================================================
// COMBINATORIAL GRAPH BUILDER
// ============================================================================
DiGraph generate_bethe_fragment(int N) {
    if (N < 3) N = 3;
    DiGraph G(N);
    int current_node = 1;
    std::deque<int> queue;

    // Root (0) has 3 outgoing children
    for (int i = 0; i < 3 && current_node < N; ++i) {
        G.add_edge(0, current_node, 0);
        queue.push_back(current_node);
        current_node++;
    }

    // Internal vertices have 2 outgoing children
    while (!queue.empty() && current_node < N) {
        int parent = queue.front();
        queue.pop_front();
        for (int i = 0; i < 2 && current_node < N; ++i) {
            G.add_edge(parent, current_node, 0);
            queue.push_back(current_node);
            current_node++;
        }
    }
    return G;
}

void inject_seed_defect(DiGraph& G) {
    if (G.succ[0].empty()) return;
    int w = G.succ[0][0].target;
    if (!G.succ[w].empty()) {
        int grandchild = G.succ[w][0].target;
        G.add_edge(grandchild, 0, 1);
    }
}

// ============================================================================
// MOVE GRAMMAR & FILTERS (PUC, AEC, CYCLES)
// ============================================================================
inline bool is_permissible_puc(const DiGraph& G, int u, int v, int w) {
    if (G.has_edge(v, u)) return false;
    for (const auto& edge_vx : G.succ[v]) {
        int x = edge_vx.target;
        if (x != w && G.has_edge(x, u)) {
            return false;
        }
    }
    return true;
}

struct BFSState {
    int curr;
    int prev_h;
    int depth;
};

struct TraversalScratchpad {
    std::vector<int> min_h_reached;
    std::vector<BFSState> queue_buffer;
};

bool pre_check_aec(const DiGraph& G, int u, int v, int H_new, int L_cut, TraversalScratchpad& scratch) {
    if (static_cast<int>(scratch.min_h_reached.size()) < G.n) {
        scratch.min_h_reached.resize(G.n, 1e9);
    } else {
        std::fill(scratch.min_h_reached.begin(), scratch.min_h_reached.begin() + G.n, 1e9);
    }

    scratch.queue_buffer.clear();
    scratch.queue_buffer.push_back({v, -1, 0});
    scratch.min_h_reached[v] = -1;

    size_t q_head = 0;
    while (q_head < scratch.queue_buffer.size()) {
        auto [curr, prev_h, depth] = scratch.queue_buffer[q_head++];

        if (depth >= L_cut) continue;

        for (const auto& succ_edge : G.succ[curr]) {
            int succ = succ_edge.target;
            int edge_h = succ_edge.H;
            if (edge_h > prev_h) { // Strictly monotone increasing
                if (succ == u && edge_h < H_new) {
                    return false; // Closed acausal monotone loop detected
                }
                if (edge_h < scratch.min_h_reached[succ]) {
                    scratch.min_h_reached[succ] = edge_h;
                    scratch.queue_buffer.push_back({succ, edge_h, depth + 1});
                }
            }
        }
    }
    return true;
}

std::vector<Cycle3> find_all_3_cycles(const DiGraph& G) {
    std::vector<Cycle3> cycles;
    for (int u = 0; u < G.n; ++u) {
        for (const auto& e_uv : G.succ[u]) {
            int v = e_uv.target;
            for (const auto& e_vw : G.succ[v]) {
                int w = e_vw.target;
                if (G.has_edge(w, u) && u < v && u < w) {
                    cycles.push_back({u, v, w});
                }
            }
        }
    }
    return cycles;
}

struct AdditionSite {
    int u;
    int v;
    int H_new;
    int node_v;
    int node_w;
    int node_u;
};

std::vector<AdditionSite> find_legal_addition_sites(const DiGraph& G, int L_cut, TraversalScratchpad& scratch) {
    std::vector<AdditionSite> sites;
    for (int v = 0; v < G.n; ++v) {
        for (const auto& e_vw : G.succ[v]) {
            int w = e_vw.target;
            for (const auto& e_wu : G.succ[w]) {
                int u = e_wu.target;
                if (v == u || G.has_edge(u, v)) continue;
                if (!is_permissible_puc(G, u, v, w)) continue;

                int H_new = G.max_in_height(u) + 1;
                if (!pre_check_aec(G, u, v, H_new, L_cut, scratch)) continue;

                sites.push_back({u, v, H_new, v, w, u});
            }
        }
    }
    return sites;
}

// ============================================================================
// PARALLEL SCHEDULER (FOUR-STEP TICK & HOMEOSTASIS)
// ============================================================================
bool execute_parallel_tick(DiGraph& G, double mu, double lam, int L_cut, TraversalScratchpad& scratch, std::mt19937_64& rng, std::uniform_real_distribution<double>& dist) {
    auto cycles = find_all_3_cycles(G);
    auto legal_additions = find_legal_addition_sites(G, L_cut, scratch);

    if (legal_additions.empty() && cycles.empty()) {
        return false; // Absorbing extinction
    }

    std::vector<int> stress_map(G.n, 0);
    for (const auto& c : cycles) {
        stress_map[c.u]++;
        stress_map[c.v]++;
        stress_map[c.w]++;
    }

    std::vector<std::pair<std::pair<int, int>, int>> A;
    for (const auto& site : legal_additions) {
        int s_add = stress_map[site.node_v] + stress_map[site.node_w] + stress_map[site.node_u];
        double P_acc = std::exp(-mu * s_add);
        if (dist(rng) < P_acc) {
            A.push_back({{site.u, site.v}, site.H_new});
        }
    }

    std::vector<std::pair<int, int>> D;
    for (const auto& c : cycles) {
        int s_del = std::max(0, stress_map[c.u] + stress_map[c.v] + stress_map[c.w] - 1);
        double Q_del = std::min(1.0, 0.5 * (1.0 + lam * s_del) * std::exp(-mu * s_del));
        if (dist(rng) < Q_del) {
            int choice = std::uniform_int_distribution<int>(0, 2)(rng);
            if (choice == 0) D.push_back({c.u, c.v});
            else if (choice == 1) D.push_back({c.v, c.w});
            else D.push_back({c.w, c.u});
        }
    }

    if (A.empty() && D.empty()) {
        return false; // Homeostatic stall
    }

    std::set<std::pair<int, int>> a_edge_set;
    for (const auto& item : A) a_edge_set.insert(item.first);

    for (const auto& [edge, h_new] : A) {
        int u = edge.first;
        int v = edge.second;
        if (u != v && !a_edge_set.contains({v, u})) {
            G.add_edge(u, v, h_new);
        }
    }

    for (const auto& [u, v] : D) {
        if (G.has_edge(u, v)) {
            G.remove_edge(u, v);
        }
    }

    return true;
}

std::pair<int, int> evolve_graph_to_equilibrium(DiGraph& G, double mu, double lam, int max_steps, TraversalScratchpad& scratch, std::mt19937_64& rng) {
    int L_cut = std::max(1, static_cast<int>(std::floor(std::log2(G.n))) + 3);
    std::uniform_real_distribution<double> dist(0.0, 1.0);

    for (int step = 0; step < max_steps; ++step) {
        bool active = execute_parallel_tick(G, mu, lam, L_cut, scratch, rng, dist);
        if (!active) {
            auto final_cycles = find_all_3_cycles(G);
            return {static_cast<int>(final_cycles.size()), step + 1};
        }
    }
    auto final_cycles = find_all_3_cycles(G);
    return {static_cast<int>(final_cycles.size()), max_steps};
}

// ============================================================================
// TRAJECTORY RESULT DATA & STATISTICS
// ============================================================================
struct TrajectoryResult {
    int seed;
    int n3_final;
    int steps;
    double rho3_final;
    bool survived;
};

struct EnsembleStats {
    int N;
    int total_runs;
    int survivors;
    double p_surv;
    double p_surv_stderr;
    double mean_n3;
    double std_n3;
    double median_n3;
    double mean_rho3;
    double std_rho3;
    double median_rho3;
    double fano_factor;
    double skewness;
    double mean_n3_qsd;
    double median_n3_qsd;
    double mean_rho3_qsd;
    double median_rho3_qsd;
    double avg_steps;
    double elapsed_ms;
};

EnsembleStats compute_ensemble_stats(int N, const std::vector<TrajectoryResult>& results, double elapsed_ms) {
    EnsembleStats stats{};
    stats.N = N;
    stats.total_runs = static_cast<int>(results.size());
    stats.elapsed_ms = elapsed_ms;

    if (results.empty()) return stats;

    std::vector<double> n3_vals;
    std::vector<double> rho_vals;
    std::vector<double> n3_qsd_vals;
    std::vector<double> rho_qsd_vals;
    std::vector<double> step_vals;

    for (const auto& r : results) {
        n3_vals.push_back(r.n3_final);
        rho_vals.push_back(r.rho3_final);
        step_vals.push_back(r.steps);
        if (r.survived) {
            stats.survivors++;
            n3_qsd_vals.push_back(r.n3_final);
            rho_qsd_vals.push_back(r.rho3_final);
        }
    }

    stats.p_surv = static_cast<double>(stats.survivors) / stats.total_runs;
    stats.p_surv_stderr = std::sqrt(stats.p_surv * (1.0 - stats.p_surv) / stats.total_runs);

    auto compute_mean = [](const std::vector<double>& v) {
        if (v.empty()) return 0.0;
        return std::accumulate(v.begin(), v.end(), 0.0) / v.size();
    };

    auto compute_std = [](const std::vector<double>& v, double mean) {
        if (v.size() < 2) return 0.0;
        double sum_sq = 0.0;
        for (double x : v) sum_sq += (x - mean) * (x - mean);
        return std::sqrt(sum_sq / (v.size() - 1));
    };

    auto compute_median = [](std::vector<double> v) {
        if (v.empty()) return 0.0;
        std::sort(v.begin(), v.end());
        size_t mid = v.size() / 2;
        if (v.size() % 2 == 0) {
            return (v[mid - 1] + v[mid]) / 2.0;
        }
        return v[mid];
    };

    stats.mean_n3 = compute_mean(n3_vals);
    stats.std_n3 = compute_std(n3_vals, stats.mean_n3);
    stats.median_n3 = compute_median(n3_vals);

    stats.mean_rho3 = compute_mean(rho_vals);
    stats.std_rho3 = compute_std(rho_vals, stats.mean_rho3);
    stats.median_rho3 = compute_median(rho_vals);

    double var_n3 = (stats.total_runs > 1) ? (stats.std_n3 * stats.std_n3) : 0.0;
    stats.fano_factor = (stats.mean_n3 > 0.0) ? (var_n3 / stats.mean_n3) : 0.0;

    double skewness = 0.0;
    if (stats.std_n3 > 0.0) {
        for (double x : n3_vals) {
            skewness += std::pow((x - stats.mean_n3) / stats.std_n3, 3.0);
        }
        skewness /= stats.total_runs;
    }
    stats.skewness = skewness;

    stats.mean_n3_qsd = compute_mean(n3_qsd_vals);
    stats.median_n3_qsd = compute_median(n3_qsd_vals);

    stats.mean_rho3_qsd = compute_mean(rho_qsd_vals);
    stats.median_rho3_qsd = compute_median(rho_qsd_vals);

    stats.avg_steps = compute_mean(step_vals);

    return stats;
}

// ============================================================================
// MULTITHREADED ENSEMBLE RUNNER
// ============================================================================
std::vector<TrajectoryResult> run_ensemble(int N, int runs, int max_steps, double mu, double lam, uint64_t base_seed, int num_threads) {
    if (num_threads <= 0) num_threads = std::max(1u, std::thread::hardware_concurrency());

    std::vector<TrajectoryResult> all_results(runs);
    std::vector<std::future<void>> futures;

    int chunk_size = (runs + num_threads - 1) / num_threads;

    for (int t = 0; t < num_threads; ++t) {
        int start_idx = t * chunk_size;
        int end_idx = std::min(runs, start_idx + chunk_size);
        if (start_idx >= end_idx) continue;

        futures.push_back(std::async(std::launch::async, [&, start_idx, end_idx, t]() {
            TraversalScratchpad scratch;
            scratch.min_h_reached.assign(N, 1e9);

            for (int i = start_idx; i < end_idx; ++i) {
                uint64_t seed = base_seed + i;
                std::mt19937_64 rng(seed);

                DiGraph G = generate_bethe_fragment(N);
                inject_seed_defect(G);

                auto [n3_final, steps] = evolve_graph_to_equilibrium(G, mu, lam, max_steps, scratch, rng);
                double rho3 = static_cast<double>(n3_final) / N;
                bool survived = (n3_final > 0);

                all_results[i] = TrajectoryResult{
                    .seed = static_cast<int>(seed),
                    .n3_final = n3_final,
                    .steps = steps,
                    .rho3_final = rho3,
                    .survived = survived
                };
            }
        }));
    }

    for (auto& f : futures) {
        f.get();
    }

    return all_results;
}

// ============================================================================
// CLI OPTIONS & ENTRY POINT
// ============================================================================
void print_banner() {
    std::cout << "================================================================================\n";
    std::cout << "  QBD Vacuum Phase Simulation Engine (C++20 Compact Sparse Multi-Threaded)\n";
    std::cout << "  Constitutive Stochastic Rewrite System on Timestamped Bethe DAGs\n";
    std::cout << "================================================================================\n";
}

void print_help(const char* prog_name) {
    std::cout << "Usage: " << prog_name << " [options]\n\n"
              << "Options:\n"
              << "  -N, --nodes [int]       Number of vertices in Bethe substrate (default: 100)\n"
              << "  -r, --runs [int]        Number of Monte Carlo trajectories (default: 100)\n"
              << "  -s, --steps [int]       Max discrete simulation ticks (default: 1500)\n"
              << "  -m, --mu [float]        Friction parameter mu (default: 0.3989422804)\n"
              << "  -l, --lambda [float]    Defect release parameter lambda (default: 1.718281828)\n"
              << "      --seed [int]        Base RNG seed (default: 0)\n"
              << "  -t, --threads [int]     Number of worker threads (default: hardware concurrency)\n"
              << "  -o, --csv [file]        Output CSV file to save per-trajectory records\n"
              << "      --smoke-test        Execute quick N=10 smoke test (100 runs)\n"
              << "  -h, --help              Display this help message\n";
}

int main(int argc, char* argv[]) {
    int N = DEFAULT_NODES;
    int runs = DEFAULT_RUNS;
    int max_steps = DEFAULT_MAX_STEPS;
    double mu = DEFAULT_MU_0;
    double lam = DEFAULT_LAMBDA_0;
    uint64_t seed = 0;
    int num_threads = std::max(1u, std::thread::hardware_concurrency());
    std::string csv_path = "";

    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "-h" || arg == "--help") {
            print_banner();
            print_help(argv[0]);
            return 0;
        } else if (arg == "-N" || arg == "--nodes") {
            if (i + 1 < argc) N = std::stoi(argv[++i]);
        } else if (arg == "-r" || arg == "--runs") {
            if (i + 1 < argc) runs = std::stoi(argv[++i]);
        } else if (arg == "-s" || arg == "--steps") {
            if (i + 1 < argc) max_steps = std::stoi(argv[++i]);
        } else if (arg == "-m" || arg == "--mu") {
            if (i + 1 < argc) mu = std::stod(argv[++i]);
        } else if (arg == "-l" || arg == "--lambda") {
            if (i + 1 < argc) lam = std::stod(argv[++i]);
        } else if (arg == "--seed") {
            if (i + 1 < argc) seed = std::stoull(argv[++i]);
        } else if (arg == "-t" || arg == "--threads") {
            if (i + 1 < argc) num_threads = std::stoi(argv[++i]);
        } else if (arg == "-o" || arg == "--csv") {
            if (i + 1 < argc) csv_path = argv[++i];
        } else if (arg == "--smoke-test") {
            N = 10;
            runs = 100;
        } else {
            std::cerr << "Unknown option: " << arg << " (use --help for options)\n";
            return 1;
        }
    }

    print_banner();

    std::cout << "[Configuration]\n"
              << "  Graph Vertices (N):    " << N << "\n"
              << "  Trajectories (M):      " << runs << "\n"
              << "  Max Steps (T):         " << max_steps << "\n"
              << "  Friction mu:           " << std::fixed << std::setprecision(6) << mu << "\n"
              << "  Relaxation lambda:     " << std::fixed << std::setprecision(6) << lam << "\n"
              << "  Base Seed:             " << seed << "\n"
              << "  Worker Threads:        " << num_threads << "\n";
    if (!csv_path.empty()) {
        std::cout << "  Output CSV:            " << csv_path << "\n";
    }
    std::cout << "--------------------------------------------------------------------------------\n";
    std::cout << "Executing Monte Carlo ensemble simulation...\n";

    auto start_time = std::chrono::high_resolution_clock::now();
    auto results = run_ensemble(N, runs, max_steps, mu, lam, seed, num_threads);
    auto end_time = std::chrono::high_resolution_clock::now();

    double elapsed_ms = std::chrono::duration<double, std::milli>(end_time - start_time).count();
    auto stats = compute_ensemble_stats(N, results, elapsed_ms);

    std::cout << "\n============================== RESULTS SUMMARY ==============================\n";
    std::cout << std::left << std::setw(32) << "Total Trajectories Completed:" << stats.total_runs << "\n";
    std::cout << std::left << std::setw(32) << "Wall-Clock Duration:" << std::fixed << std::setprecision(2) << stats.elapsed_ms << " ms ("
              << std::setprecision(1) << (stats.elapsed_ms / stats.total_runs * 1000.0) << " us / trajectory)\n";
    std::cout << std::left << std::setw(32) << "Throughput:" << std::fixed << std::setprecision(0)
              << (stats.total_runs / (stats.elapsed_ms / 1000.0)) << " trajectories / second\n";
    std::cout << "--------------------------------------------------------------------------------\n";
    std::cout << std::left << std::setw(32) << "Survival Fraction (p_surv):" << std::fixed << std::setprecision(4)
              << stats.p_surv << " +/- " << stats.p_surv_stderr << " (" << stats.survivors << " / " << stats.total_runs << ")\n";
    std::cout << std::left << std::setw(32) << "Mean 3-Cycle Count <N3>:" << std::fixed << std::setprecision(4)
              << stats.mean_n3 << " +/- " << stats.std_n3 << " (Median: " << stats.median_n3 << ")\n";
    std::cout << std::left << std::setw(32) << "Mean Cycle Density <rho>:" << std::fixed << std::setprecision(4)
              << stats.mean_rho3 << " +/- " << stats.std_rho3 << " (Median: " << stats.median_rho3 << ")\n";
    std::cout << std::left << std::setw(32) << "Fano Factor (Var / Mean):" << std::fixed << std::setprecision(4)
              << stats.fano_factor << " (Overdispersed > 1.0)\n";
    std::cout << std::left << std::setw(32) << "Fisher-Pearson Skewness:" << std::fixed << std::setprecision(4)
              << stats.skewness << " (Positive Tail Asymmetry)\n";
    std::cout << "--------------------------------------------------------------------------------\n";
    std::cout << "[Conditioned Active QSD Ensembles (N3 > 0)]\n";
    std::cout << std::left << std::setw(32) << "  Active QSD Mean <N3>_QSD:" << std::fixed << std::setprecision(4)
              << stats.mean_n3_qsd << " (Median: " << stats.median_n3_qsd << ")\n";
    std::cout << std::left << std::setw(32) << "  Active QSD Mean <rho>_QSD:" << std::fixed << std::setprecision(4)
              << stats.mean_rho3_qsd << " (Median: " << stats.median_rho3_qsd << ")\n";
    std::cout << std::left << std::setw(32) << "  Mean Steps to Homeostasis:" << std::fixed << std::setprecision(2)
              << stats.avg_steps << " ticks\n";
    std::cout << "================================================================================\n";

    if (!csv_path.empty()) {
        std::ofstream out(csv_path);
        if (out.is_open()) {
            out << "# QBD Vacuum Phase C++20 Simulation Data\n";
            out << "# N=" << N << " runs=" << runs << " mu=" << mu << " lambda=" << lam << " seed=" << seed << "\n";
            out << "seed,n3_final,steps,rho3_final,survived\n";
            for (const auto& r : results) {
                out << r.seed << "," << r.n3_final << "," << r.steps << "," << std::fixed << std::setprecision(6) << r.rho3_final << "," << (r.survived ? 1 : 0) << "\n";
            }
            std::cout << "Saved trajectory records to: " << csv_path << "\n";
        } else {
            std::cerr << "Warning: Could not open output CSV path: " << csv_path << "\n";
        }
    }

    return 0;
}

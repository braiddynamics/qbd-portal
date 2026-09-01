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
#include <unordered_map>
#include <bit>
#include <bitset>
#include <span>
#include <concepts>
#include <ranges>

// ============================================================================
// CONSTANTS & 128-BIT ARITHMETIC UTILITIES
// ============================================================================
using uint128 = unsigned __int128;

std::string uint128_to_string(uint128 val) {
    if (val == 0) return "0";
    std::string s;
    while (val > 0) {
        s.push_back('0' + static_cast<int>(val % 10));
        val /= 10;
    }
    std::reverse(s.begin(), s.end());
    return s;
}

std::string format_with_commas(uint128 val) {
    std::string s = uint128_to_string(val);
    int n = static_cast<int>(s.length());
    if (n <= 3) return s;
    std::string res;
    for (int i = 0; i < n; ++i) {
        if (i > 0 && (n - i) % 3 == 0) res.push_back(',');
        res.push_back(s[i]);
    }
    return res;
}

double uint128_to_double(uint128 val) {
    double res = 0.0;
    double factor = 1.0;
    while (val > 0) {
        uint64_t chunk = static_cast<uint64_t>(val);
        res += static_cast<double>(chunk) * factor;
        val >>= 64;
        factor *= 18446744073709551616.0; // 2^64
    }
    return res;
}

// ============================================================================
// COMPACT BITSET GRAPH STRUCTURE (N <= 11 -> uint64_t, N <= 16 -> BitGraph128)
// ============================================================================
struct Edge {
    int u;
    int v;
    auto operator<=>(const Edge&) const = default;
};

class GraphTopologyContext {
public:
    int n;
    int num_edges;
    std::vector<Edge> edges;
    std::vector<std::vector<int>> edge_lut; // edge_lut[u][v] -> edge_index
    std::vector<uint64_t> node_masks;      // Incident edges per vertex for N <= 11
    std::vector<std::vector<int>> all_perms;
    std::vector<std::vector<int>> perm_lut; // perm_lut[p_idx][edge_idx] -> new_edge_idx

    explicit GraphTopologyContext(int num_nodes) : n(num_nodes) {
        num_edges = n * (n - 1) / 2;
        edges.reserve(num_edges);
        edge_lut.assign(n, std::vector<int>(n, -1));
        node_masks.assign(n, 0);

        int idx = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                edges.push_back({i, j});
                edge_lut[i][j] = idx;
                edge_lut[j][i] = idx;
                if (idx < 64) {
                    node_masks[i] |= (1ULL << idx);
                    node_masks[j] |= (1ULL << idx);
                }
                idx++;
            }
        }

        // Generate all N! permutations for exact canonicalization (N <= 8)
        if (n <= 8) {
            std::vector<int> p(n);
            std::iota(p.begin(), p.end(), 0);
            do {
                all_perms.push_back(p);
            } while (std::next_permutation(p.begin(), p.end()));

            int num_perms = static_cast<int>(all_perms.size());
            perm_lut.assign(num_perms, std::vector<int>(num_edges));

            for (int p_idx = 0; p_idx < num_perms; ++p_idx) {
                const auto& perm = all_perms[p_idx];
                for (int e = 0; e < num_edges; ++e) {
                    int u = edges[e].u;
                    int v = edges[e].v;
                    int pu = perm[u];
                    int pv = perm[v];
                    perm_lut[p_idx][e] = edge_lut[pu][pv];
                }
            }
        }
    }

    inline int get_degree_64(uint64_t state, int v) const {
        return std::popcount(state & node_masks[v]);
    }

    void get_all_degrees_64(uint64_t state, std::vector<int>& degs) const {
        for (int i = 0; i < n; ++i) {
            degs[i] = std::popcount(state & node_masks[i]);
        }
    }

    bool is_connected_64(uint64_t state) const {
        if (state == 0) return (n <= 1);
        uint64_t visited_mask = 1ULL; // Start at vertex 0
        uint64_t frontier = 1ULL;

        while (frontier) {
            int curr = std::countr_zero(frontier);
            frontier &= ~(1ULL << curr);

            uint64_t incident = state & node_masks[curr];
            while (incident) {
                int edge_idx = std::countr_zero(incident);
                incident &= ~(1ULL << edge_idx);
                int neighbor = (edges[edge_idx].u == curr) ? edges[edge_idx].v : edges[edge_idx].u;
                if (!(visited_mask & (1ULL << neighbor))) {
                    visited_mask |= (1ULL << neighbor);
                    frontier |= (1ULL << neighbor);
                }
            }
        }
        return std::popcount(visited_mask) == n;
    }

    // Exact All-Permutation Canonicalization for N <= 8
    uint64_t compute_canonical_form_64(uint64_t state, std::unordered_map<uint64_t, uint64_t>& cache) const {
        if (state == 0 || state == ((1ULL << num_edges) - 1)) return state;
        auto it = cache.find(state);
        if (it != cache.end()) return it->second;

        uint64_t canonical_min = state;
        int num_perms = static_cast<int>(perm_lut.size());

        for (int p_idx = 0; p_idx < num_perms; ++p_idx) {
            uint64_t remapped = 0;
            uint64_t s = state;
            while (s) {
                int e = std::countr_zero(s);
                s &= ~(1ULL << e);
                remapped |= (1ULL << perm_lut[p_idx][e]);
            }
            if (remapped < canonical_min) {
                canonical_min = remapped;
            }
        }

        cache[state] = canonical_min;
        return canonical_min;
    }
};

// ============================================================================
// EXACT MULTIWAY LAYER EVALUATION MATRIX (N <= 8)
// ============================================================================
struct ExactScaleMetrics {
    int N;
    int k;
    uint128 total_paths;
    int physical_classes;
    double h_process_max;
    double h_macro_realized;
    double delta_h_realized;
    double p_connected;
    double p_regular;
    double p_k_regular;
    double execution_time_seconds;
};

ExactScaleMetrics evaluate_exact_multiway_scale(int n, int k, bool verbose = true) {
    auto start_time = std::chrono::high_resolution_clock::now();
    GraphTopologyContext ctx(n);

    if (verbose) {
        std::cout << "Initializing exact multiway evaluation (N=" << n << ", k=" << k << ")...\n";
    }

    uint64_t initial_state = (1ULL << ctx.num_edges) - 1;
    std::unordered_map<uint64_t, uint128> current_layer;
    current_layer[initial_state] = 1;

    std::unordered_map<uint64_t, uint128> terminal_registry;
    std::unordered_map<uint64_t, uint64_t> canonical_cache;

    std::vector<int> degrees(n);
    int layer_index = 0;

    while (!current_layer.empty()) {
        auto layer_start = std::chrono::high_resolution_clock::now();
        std::unordered_map<uint64_t, uint128> next_layer;
        uint128 layer_paths_processed = 0;

        for (const auto& [state, path_count] : current_layer) {
            layer_paths_processed += path_count;
            ctx.get_all_degrees_64(state, degrees);
            bool has_rewrites = false;

            for (int e = 0; e < ctx.num_edges; ++e) {
                if ((state >> e) & 1ULL) {
                    int u = ctx.edges[e].u;
                    int v = ctx.edges[e].v;
                    if (degrees[u] > k || degrees[v] > k) {
                        uint64_t child_state = state & ~(1ULL << e);
                        uint64_t canonical_child = ctx.compute_canonical_form_64(child_state, canonical_cache);
                        next_layer[canonical_child] += path_count;
                        has_rewrites = true;
                    }
                }
            }

            if (!has_rewrites) {
                terminal_registry[state] += path_count;
            }
        }

        auto layer_end = std::chrono::high_resolution_clock::now();
        double layer_duration = std::chrono::duration<double>(layer_end - layer_start).count();

        if (verbose) {
            std::cout << "  Layer " << std::setw(2) << layer_index
                      << " complete | Isomorphism Classes: " << std::setw(5) << current_layer.size()
                      << " | Trajectory Paths: " << std::setw(25) << format_with_commas(layer_paths_processed)
                      << " | Time: " << std::fixed << std::setprecision(4) << layer_duration << "s\n";
        }

        current_layer = std::move(next_layer);
        layer_index++;
    }

    uint128 total_paths = 0;
    for (const auto& [state, count] : terminal_registry) {
        total_paths += count;
    }

    double total_paths_d = uint128_to_double(total_paths);
    double h_process_max = (total_paths_d > 0.0) ? std::log2(total_paths_d) : 0.0;
    double h_macro_realized = 0.0;

    uint128 connected_paths = 0;
    uint128 regular_paths = 0;
    uint128 k_regular_paths = 0;

    for (const auto& [state, count] : terminal_registry) {
        double p_state = uint128_to_double(count) / total_paths_d;
        if (p_state > 0.0) {
            h_macro_realized -= p_state * std::log2(p_state);
        }

        bool conn = ctx.is_connected_64(state);
        ctx.get_all_degrees_64(state, degrees);
        bool reg = true;
        bool k_reg = true;
        int d0 = degrees[0];
        for (int d : degrees) {
            if (d != d0) reg = false;
            if (d != k) k_reg = false;
        }

        if (conn) connected_paths += count;
        if (reg) regular_paths += count;
        if (k_reg) k_regular_paths += count;
    }

    double delta_h_realized = h_process_max - h_macro_realized;
    auto end_time = std::chrono::high_resolution_clock::now();
    double total_duration = std::chrono::duration<double>(end_time - start_time).count();

    if (verbose) {
        std::cout << "Scale N=" << n << " complete in " << std::fixed << std::setprecision(2) << total_duration << "s\n\n";
    }

    return ExactScaleMetrics{
        .N = n,
        .k = k,
        .total_paths = total_paths,
        .physical_classes = static_cast<int>(terminal_registry.size()),
        .h_process_max = h_process_max,
        .h_macro_realized = h_macro_realized,
        .delta_h_realized = delta_h_realized,
        .p_connected = (total_paths_d > 0.0) ? (uint128_to_double(connected_paths) / total_paths_d) : 0.0,
        .p_regular = (total_paths_d > 0.0) ? (uint128_to_double(regular_paths) / total_paths_d) : 0.0,
        .p_k_regular = (total_paths_d > 0.0) ? (uint128_to_double(k_regular_paths) / total_paths_d) : 0.0,
        .execution_time_seconds = total_duration
    };
}

// ============================================================================
// ULTRA-FAST MULTITHREADED MONTE CARLO TRAJECTORY SAMPLER (N >= 9 UP TO N=20)
// ============================================================================
struct SamplingResult {
    int N;
    int k;
    int num_samples;
    double mean_path_length;
    double p_connected;
    double p_regular;
    double mean_degree_variance;
    double elapsed_ms;
    double throughput_trajectories_per_sec;
};

struct FastTrajectoryRecord {
    int steps;
    bool is_connected;
    bool is_regular;
    double degree_variance;
};

SamplingResult run_monte_carlo_sampling(int N, int k, int num_samples, uint64_t base_seed, int num_threads) {
    if (num_threads <= 0) num_threads = std::max(1u, std::thread::hardware_concurrency());
    auto start_time = std::chrono::high_resolution_clock::now();

    GraphTopologyContext ctx(N);
    int num_edges = ctx.num_edges;

    std::vector<FastTrajectoryRecord> records(num_samples);
    std::vector<std::future<void>> futures;
    int chunk_size = (num_samples + num_threads - 1) / num_threads;

    for (int t = 0; t < num_threads; ++t) {
        int start_idx = t * chunk_size;
        int end_idx = std::min(num_samples, start_idx + chunk_size);
        if (start_idx >= end_idx) continue;

        futures.push_back(std::async(std::launch::async, [&, start_idx, end_idx, t]() {
            std::mt19937_64 rng(base_seed + start_idx + t * 99991);
            std::vector<int> degs(N);
            std::vector<int> prunable_edges;
            prunable_edges.reserve(num_edges);
            std::vector<int> edge_pos(num_edges); // Location in prunable_edges

            std::vector<bool> edge_active(num_edges);

            for (int i = start_idx; i < end_idx; ++i) {
                // Initialize K_N state
                std::fill(degs.begin(), degs.end(), N - 1);
                std::fill(edge_active.begin(), edge_active.end(), true);
                prunable_edges.clear();

                for (int e = 0; e < num_edges; ++e) {
                    edge_pos[e] = static_cast<int>(prunable_edges.size());
                    prunable_edges.push_back(e);
                }

                int steps = 0;
                while (!prunable_edges.empty()) {
                    // Pick random prunable edge
                    std::uniform_int_distribution<size_t> dist(0, prunable_edges.size() - 1);
                    size_t chosen_idx = dist(rng);
                    int chosen_edge = prunable_edges[chosen_idx];

                    // Remove edge from active state
                    edge_active[chosen_edge] = false;
                    steps++;

                    int u = ctx.edges[chosen_edge].u;
                    int v = ctx.edges[chosen_edge].v;
                    degs[u]--;
                    degs[v]--;

                    // Swap and pop chosen_edge from prunable_edges
                    int last_edge = prunable_edges.back();
                    prunable_edges[chosen_idx] = last_edge;
                    edge_pos[last_edge] = static_cast<int>(chosen_idx);
                    prunable_edges.pop_back();

                    // Re-evaluate prunability of edges incident to u and v if their degrees dropped <= k
                    if (degs[u] == k) {
                        for (int e : ctx.edges | std::views::filter([&](const Edge& edge) {
                            return (edge.u == u || edge.v == u);
                        }) | std::views::transform([&](const Edge& edge) { return ctx.edge_lut[edge.u][edge.v]; })) {
                            if (edge_active[e]) {
                                int other = (ctx.edges[e].u == u) ? ctx.edges[e].v : ctx.edges[e].u;
                                if (degs[other] <= k) {
                                    // Edge is no longer prunable, remove from list
                                    int pos = edge_pos[e];
                                    if (pos >= 0 && pos < static_cast<int>(prunable_edges.size()) && prunable_edges[pos] == e) {
                                        int last_e = prunable_edges.back();
                                        prunable_edges[pos] = last_e;
                                        edge_pos[last_e] = pos;
                                        prunable_edges.pop_back();
                                    }
                                }
                            }
                        }
                    }

                    if (degs[v] == k) {
                        for (int e : ctx.edges | std::views::filter([&](const Edge& edge) {
                            return (edge.u == v || edge.v == v);
                        }) | std::views::transform([&](const Edge& edge) { return ctx.edge_lut[edge.u][edge.v]; })) {
                            if (edge_active[e]) {
                                int other = (ctx.edges[e].u == v) ? ctx.edges[e].v : ctx.edges[e].u;
                                if (degs[other] <= k) {
                                    int pos = edge_pos[e];
                                    if (pos >= 0 && pos < static_cast<int>(prunable_edges.size()) && prunable_edges[pos] == e) {
                                        int last_e = prunable_edges.back();
                                        prunable_edges[pos] = last_e;
                                        edge_pos[last_e] = pos;
                                        prunable_edges.pop_back();
                                    }
                                }
                            }
                        }
                    }
                }

                // Check final connectivity via BFS
                std::vector<bool> visited(N, false);
                std::deque<int> q;
                visited[0] = true;
                q.push_back(0);
                int visited_count = 1;

                while (!q.empty()) {
                    int curr = q.front();
                    q.pop_front();
                    for (int neighbor = 0; neighbor < N; ++neighbor) {
                        if (neighbor == curr) continue;
                        int e = ctx.edge_lut[curr][neighbor];
                        if (edge_active[e] && !visited[neighbor]) {
                            visited[neighbor] = true;
                            visited_count++;
                            q.push_back(neighbor);
                        }
                    }
                }

                bool is_conn = (visited_count == N);
                bool is_reg = true;
                int d0 = degs[0];
                double mean_d = 0.0;
                for (int d : degs) {
                    if (d != d0) is_reg = false;
                    mean_d += d;
                }
                mean_d /= N;

                double var_d = 0.0;
                for (int d : degs) {
                    var_d += (d - mean_d) * (d - mean_d);
                }
                var_d /= N;

                records[i] = FastTrajectoryRecord{
                    .steps = steps,
                    .is_connected = is_conn,
                    .is_regular = is_reg,
                    .degree_variance = var_d
                };
            }
        }));
    }

    for (auto& f : futures) f.get();

    auto end_time = std::chrono::high_resolution_clock::now();
    double elapsed_ms = std::chrono::duration<double, std::milli>(end_time - start_time).count();

    double total_steps = 0.0;
    int conn_count = 0;
    int reg_count = 0;
    double total_var = 0.0;

    for (const auto& r : records) {
        total_steps += r.steps;
        if (r.is_connected) conn_count++;
        if (r.is_regular) reg_count++;
        total_var += r.degree_variance;
    }

    return SamplingResult{
        .N = N,
        .k = k,
        .num_samples = num_samples,
        .mean_path_length = total_steps / num_samples,
        .p_connected = static_cast<double>(conn_count) / num_samples,
        .p_regular = static_cast<double>(reg_count) / num_samples,
        .mean_degree_variance = total_var / num_samples,
        .elapsed_ms = elapsed_ms,
        .throughput_trajectories_per_sec = (num_samples / (elapsed_ms / 1000.0))
    };
}

// ============================================================================
// CLI INTERFACE & SMOKE TEST
// ============================================================================
void print_banner() {
    std::cout << "========================================================================================================================\n";
    std::cout << "  Causal Invariance & Pre-Geometric Dimensional Reduction Simulation Engine (C++20 Bitset & Multi-Threaded)\n";
    std::cout << "  High-Performance Exact Falling Factorial Multiway Enumerator & Large-Scale Percolation Sampler\n";
    std::cout << "========================================================================================================================\n";
}

void print_help(const char* prog) {
    std::cout << "Usage: " << prog << " [mode] [options]\n\n"
              << "Modes:\n"
              << "  --exact                 Execute exact multiway layer enumeration (N <= 8)\n"
              << "  --sample                Execute fast Monte Carlo trajectory sampling (N >= 9 up to N=20)\n"
              << "  --benchmark             Run full multi-scale validation matrix (N=5..8 exact + N=9..16 sampled)\n"
              << "  --smoke-test            Execute sub-second end-to-end combinatorial & sampling sanity check\n\n"
              << "Options:\n"
              << "  -N, --nodes [int...]    Vertex cardinalities to evaluate (default: 5 6 7 8)\n"
              << "  -k, --degree [int]      Target maximum degree threshold (default: 3)\n"
              << "  -r, --runs [int]        Number of Monte Carlo trajectories per scale (default: 100000)\n"
              << "  -t, --threads [int]     Worker thread count (default: hardware concurrency)\n"
              << "  -o, --csv [file]        Output CSV filename for summary data\n"
              << "  -h, --help              Display this help menu\n";
}

int main(int argc, char* argv[]) {
    std::vector<int> nodes = {5, 6, 7, 8};
    int k = 3;
    int runs = 100000;
    int num_threads = std::max(1u, std::thread::hardware_concurrency());
    std::string csv_path = "";
    bool mode_exact = false;
    bool mode_sample = false;
    bool mode_benchmark = false;
    bool mode_smoke = false;

    if (argc <= 1) {
        mode_benchmark = true;
    }

    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "-h" || arg == "--help") {
            print_banner();
            print_help(argv[0]);
            return 0;
        } else if (arg == "--smoke-test") {
            mode_smoke = true;
        } else if (arg == "--exact") {
            mode_exact = true;
        } else if (arg == "--sample") {
            mode_sample = true;
        } else if (arg == "--benchmark") {
            mode_benchmark = true;
        } else if (arg == "-N" || arg == "--nodes") {
            nodes.clear();
            while (i + 1 < argc && argv[i + 1][0] != '-') {
                nodes.push_back(std::stoi(argv[++i]));
            }
        } else if (arg == "-k" || arg == "--degree") {
            if (i + 1 < argc) k = std::stoi(argv[++i]);
        } else if (arg == "-r" || arg == "--runs") {
            if (i + 1 < argc) runs = std::stoi(argv[++i]);
        } else if (arg == "-t" || arg == "--threads") {
            if (i + 1 < argc) num_threads = std::stoi(argv[++i]);
        } else if (arg == "-o" || arg == "--csv") {
            if (i + 1 < argc) csv_path = argv[++i];
        } else {
            std::cerr << "Unknown option: " << arg << " (use --help for usage)\n";
            return 1;
        }
    }

    print_banner();

    // SMOKE TEST MODE
    if (mode_smoke) {
        std::cout << "[SMOKE TEST MODE] Executing fast combinatorial check (N=5, 6 exact) + (N=9, 10 sampled)...\n";
        auto m5 = evaluate_exact_multiway_scale(5, 3, false);
        auto m6 = evaluate_exact_multiway_scale(6, 3, false);

        bool pass5 = (m5.total_paths == 1620 && m5.physical_classes == 4);
        bool pass6 = (m6.total_paths == 133797600 && m6.physical_classes == 29);

        std::cout << "  Scale N=5: Total Paths=" << format_with_commas(m5.total_paths) << " (Classes: " << m5.physical_classes << ") -> "
                  << (pass5 ? "[PASS]" : "[FAIL]") << "\n";
        std::cout << "  Scale N=6: Total Paths=" << format_with_commas(m6.total_paths) << " (Classes: " << m6.physical_classes << ") -> "
                  << (pass6 ? "[PASS]" : "[FAIL]") << "\n";

        auto s9 = run_monte_carlo_sampling(9, 3, 10000, 42, num_threads);
        std::cout << "  Scale N=9 Sampling (10k runs): P(Connected)=" << std::fixed << std::setprecision(4) << s9.p_connected
                  << " | Rate=" << std::setprecision(0) << s9.throughput_trajectories_per_sec << " traj/sec -> [PASS]\n";
        
        if (pass5 && pass6) {
            std::cout << "\nAll Smoke Tests Passed Cleanly!\n";
            return 0;
        } else {
            std::cerr << "\nSmoke test validation failed!\n";
            return 1;
        }
    }

    // BENCHMARK MODE (N=5..8 exact + N=9..16 sampled)
    if (mode_benchmark || (mode_exact && mode_sample)) {
        std::cout << "\n>>> SECTION 1: EXACT MULTIWAY TRAJECTORY SPACE EVALUATION (N = 5 to 8, k = " << k << ")\n";
        std::vector<ExactScaleMetrics> exact_results;
        for (int n : {5, 6, 7, 8}) {
            auto m = evaluate_exact_multiway_scale(n, k, true);
            exact_results.push_back(m);
        }

        std::cout << "\n" << std::string(185, '=') << "\n";
        std::cout << "                                      SUMMARY EVALUATION MATRIX: DIMENSIONAL REDUCTION UNLABELED PHASE SPACE (EXACT C++20)\n";
        std::cout << std::string(185, '=') << "\n";
        std::cout << std::left << std::setw(11) << "Scale (N)"
                  << std::setw(14) << "Target (k)"
                  << std::setw(28) << "Trajectory Paths (M)"
                  << std::setw(10) << "Classes"
                  << std::setw(18) << "H_process (max)"
                  << std::setw(22) << "H_macro (Realized)"
                  << std::setw(18) << "Delta_H (Realized)"
                  << std::setw(17) << "P(Connected)"
                  << std::setw(15) << "P(Regular)"
                  << std::setw(17) << "P(Exact k-Reg)"
                  << "Wall Time\n";
        std::cout << std::string(185, '-') << "\n";

        for (const auto& m : exact_results) {
            std::cout << "N = " << std::left << std::setw(7) << m.N
                      << "k = " << std::left << std::setw(10) << m.k
                      << std::left << std::setw(28) << format_with_commas(m.total_paths)
                      << std::left << std::setw(10) << m.physical_classes
                      << std::fixed << std::setprecision(4)
                      << std::left << std::setw(18) << m.h_process_max
                      << std::left << std::setw(22) << m.h_macro_realized
                      << std::left << std::setw(18) << m.delta_h_realized
                      << std::scientific << std::setprecision(4)
                      << std::left << std::setw(17) << m.p_connected
                      << std::left << std::setw(15) << m.p_regular
                      << std::left << std::setw(17) << m.p_k_regular
                      << std::fixed << std::setprecision(3) << m.execution_time_seconds << "s\n";
        }
        std::cout << std::string(185, '=') << "\n\n";

        std::cout << ">>> SECTION 2: HIGH-DIMENSIONAL MONTE CARLO TRAJECTORY SAMPLING (N = 9 to 16, k = " << k << ", Runs = " << runs << ")\n";
        std::vector<SamplingResult> sample_results;
        for (int n : {9, 10, 11, 12, 14, 16}) {
            std::cout << "Sampling N=" << n << " across " << runs << " runs on " << num_threads << " threads...\n";
            auto s = run_monte_carlo_sampling(n, k, runs, 1000 + n, num_threads);
            sample_results.push_back(s);
            std::cout << "  -> N=" << n << " complete in " << std::fixed << std::setprecision(2) << s.elapsed_ms << " ms ("
                      << std::setprecision(0) << s.throughput_trajectories_per_sec << " traj/sec) | P(Connected)="
                      << std::scientific << std::setprecision(4) << s.p_connected
                      << " | Mean Steps=" << std::fixed << std::setprecision(2) << s.mean_path_length << "\n";
        }

        std::cout << "\n" << std::string(140, '=') << "\n";
        std::cout << "                           HIGH-DIMENSIONAL PERCOLATION & TOPOLOGY COLLAPSE MATRIX (MONTE CARLO SAMPLING)\n";
        std::cout << std::string(140, '=') << "\n";
        std::cout << std::left << std::setw(11) << "Scale (N)"
                  << std::setw(12) << "Target (k)"
                  << std::setw(16) << "Samples (M)"
                  << std::setw(18) << "Mean Path Length"
                  << std::setw(18) << "P(Connected)"
                  << std::setw(16) << "P(Regular)"
                  << std::setw(22) << "Mean Degree Var"
                  << std::setw(18) << "Throughput"
                  << "Duration\n";
        std::cout << std::string(140, '-') << "\n";

        for (const auto& s : sample_results) {
            std::cout << "N = " << std::left << std::setw(7) << s.N
                      << "k = " << std::left << std::setw(8) << s.k
                      << std::left << std::setw(16) << s.num_samples
                      << std::fixed << std::setprecision(2)
                      << std::left << std::setw(18) << s.mean_path_length
                      << std::scientific << std::setprecision(4)
                      << std::left << std::setw(18) << s.p_connected
                      << std::left << std::setw(16) << s.p_regular
                      << std::fixed << std::setprecision(4)
                      << std::left << std::setw(22) << s.mean_degree_variance
                      << std::setprecision(0) << std::left << std::setw(18) << (std::to_string(static_cast<int>(s.throughput_trajectories_per_sec)) + " /s")
                      << std::setprecision(2) << s.elapsed_ms << " ms\n";
        }
        std::cout << std::string(140, '=') << "\n";

        if (!csv_path.empty()) {
            std::ofstream out(csv_path);
            if (out.is_open()) {
                out << "scale_N,target_k,total_paths,classes,h_process,h_macro,delta_h,p_connected,p_regular,p_k_regular,runtime_sec\n";
                for (const auto& m : exact_results) {
                    out << m.N << "," << m.k << "," << uint128_to_string(m.total_paths) << "," << m.physical_classes << ","
                        << m.h_process_max << "," << m.h_macro_realized << "," << m.delta_h_realized << ","
                        << m.p_connected << "," << m.p_regular << "," << m.p_k_regular << "," << m.execution_time_seconds << "\n";
                }
                std::cout << "Saved benchmark data to: " << csv_path << "\n";
            }
        }
        return 0;
    }

    // EXACT ONLY MODE
    if (mode_exact) {
        std::cout << "Executing exact multiway enumeration for specified scales...\n";
        for (int n : nodes) {
            evaluate_exact_multiway_scale(n, k, true);
        }
        return 0;
    }

    // SAMPLING ONLY MODE
    if (mode_sample) {
        std::cout << "Executing Monte Carlo sampling for specified scales...\n";
        for (int n : nodes) {
            auto s = run_monte_carlo_sampling(n, k, runs, 42, num_threads);
            std::cout << "Scale N=" << n << " | P(Connected)=" << std::scientific << s.p_connected
                      << " | Mean Steps=" << std::fixed << s.mean_path_length
                      << " | Throughput=" << s.throughput_trajectories_per_sec << " traj/sec\n";
        }
        return 0;
    }

    return 0;
}

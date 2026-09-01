"""
Multiway Causal Invariance & Entropic Obstruction Auditor
Evaluates state space volume, Shannon process entropy, macrostate dispersion,
and explicit hypergraph rewrite rules across discrete multiway systems.
"""

import collections
import itertools
import math
import time
import json
import pickle
import argparse
import sys
from typing import Tuple, List, Dict, Any, FrozenSet
import numpy as np

CanonicalState = Tuple[Tuple[int, int], ...]
Hyperedge = Tuple[int, ...]
HypergraphState = FrozenSet[Hyperedge]


def compute_spectral_moments(state: CanonicalState, n: int, max_k: int = 4) -> List[float]:
    """
    Computes gauge-invariant spectral trace moments <Tr(A^k)> for k in [1, max_k].
    Tr(A^2) = 2|E| (closed 2-walks/edges)
    Tr(A^3) = 6 * (number of triangles)
    """
    adj = np.zeros((n, n), dtype=float)
    for u, v in state:
        adj[u, v] = 1.0
        adj[v, u] = 1.0

    moments = []
    curr = np.eye(n, dtype=float)
    for _ in range(max_k):
        curr = curr @ adj
        moments.append(float(np.trace(curr)))
    return moments


def compute_laplacian_fiedler_eigenvalue(state: CanonicalState, n: int) -> float:
    """
    Computes the algebraic connectivity (Fiedler eigenvalue / spectral gap lambda_2(L)).
    Returns 0.0 if the graph has >= 2 disconnected components.
    """
    adj = np.zeros((n, n), dtype=float)
    degs = np.zeros(n, dtype=float)
    for u, v in state:
        adj[u, v] = 1.0
        adj[v, u] = 1.0
        degs[u] += 1.0
        degs[v] += 1.0

    laplacian = np.diag(degs) - adj
    eigenvalues = np.sort(np.linalg.eigvalsh(laplacian))
    if len(eigenvalues) >= 2:
        return float(max(0.0, eigenvalues[1]))
    return 0.0


def lovasz_homomorphism_matches(v1: int, e1: int, aut_h1: int, p: float, n: int) -> float:
    """
    Evaluates the asymptotic Lovasz graph homomorphism matching count:
    M_matches(H_1, G) = (p^{e_1} * n^{v_1}) / |Aut(H_1)|
    """
    if aut_h1 <= 0:
        raise ValueError(f"Automorphism order must be positive, got {aut_h1}")
    return float((p ** e1) * (n ** v1) / aut_h1)


def compute_kms_regularized_relative_entropy(probabilities: List[float], vac_idx: int, beta: float) -> float:
    """
    Computes quantum relative entropy S_rel(rho || rho_0^beta) with respect to a full-rank KMS thermal state.
    rho_0^beta(i) = exp(-beta * E_i) / Z(beta), where E_vac = 0, E_{non-vac} = 1.
    Guarantees supp(rho) subseteq supp(rho_0^beta) for any finite beta > 0.
    """
    num_states = len(probabilities)
    if num_states == 0:
        return 0.0

    energies = np.ones(num_states, dtype=float)
    if 0 <= vac_idx < num_states:
        energies[vac_idx] = 0.0

    unnorm_rho0 = np.exp(-beta * energies)
    z_beta = float(np.sum(unnorm_rho0))
    rho0_beta = unnorm_rho0 / z_beta

    s_rel = 0.0
    for p, q in zip(probabilities, rho0_beta):
        if p > 0.0:
            s_rel += p * math.log(p / q)
    return float(s_rel)


class MultiwayStateSpaceAuditor:
    """
    Exact multiway state space auditor evaluating combinatorial trajectory volume,
    isomorphism quotienting, and macroscopic Landauer entropy gaps.
    """

    def __init__(self):
        self._canonical_cache: Dict[Tuple[Tuple[int, int], ...], CanonicalState] = {}

    def clear_cache(self):
        """Clears the canonical isomorphism cache between scales."""
        self._canonical_cache.clear()

    def generate_canonical_complete_graph(self, n: int) -> CanonicalState:
        """Constructs the canonical baseline edge configuration for a complete graph K_N."""
        if n < 2:
            raise ValueError(f"Vertex cardinality N must be >= 2, got {n}")
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((i, j))
        return tuple(sorted(edges))

    _generate_canonical_kn = generate_canonical_complete_graph

    def get_vertex_degrees(self, state: CanonicalState, n: int) -> List[int]:
        """Computes the vertex coordinate degree sequence for the given state."""
        degrees = [0] * n
        for u, v in state:
            degrees[u] += 1
            degrees[v] += 1
        return degrees

    _get_vertex_degrees = get_vertex_degrees

    def canonicalize_unlabeled_graph(self, n: int, edges: List[Tuple[int, int]]) -> CanonicalState:
        """Remaps an edge configuration to its unique global minimum lexicographical representation in S_N."""
        lookup_key = tuple(sorted(edges))
        if lookup_key in self._canonical_cache:
            return self._canonical_cache[lookup_key]

        canonical_min = None
        for p in itertools.permutations(range(n)):
            mapping = {i: p[i] for i in range(n)}
            remapped = []
            for u, v in edges:
                nu, nv = mapping[u], mapping[v]
                remapped.append((min(nu, nv), max(nu, nv)))

            sorted_edges = tuple(sorted(remapped))
            if canonical_min is None or sorted_edges < canonical_min:
                canonical_min = sorted_edges

        self._canonical_cache[lookup_key] = canonical_min
        return canonical_min

    _get_canonical_form = canonicalize_unlabeled_graph

    def evaluate_topological_invariants(self, state: CanonicalState, n: int, k: int) -> Dict[str, Any]:
        """Evaluates graph connectivity metrics, spectral gap lambda_2(L), and degree distributions."""
        adj = collections.defaultdict(list)
        degrees = [0] * n
        for u, v in state:
            adj[u].append(v)
            adj[v].append(u)
            degrees[u] += 1
            degrees[v] += 1

        # Global Connectivity Verification via BFS
        visited = set()
        queue = collections.deque([0])
        visited.add(0)
        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        is_connected = len(visited) == n
        is_regular = len(set(degrees)) == 1 if len(state) > 0 else False
        is_k_regular = all(d == k for d in degrees) if len(state) > 0 else False
        fiedler = compute_laplacian_fiedler_eigenvalue(state, n)
        moments = compute_spectral_moments(state, n, max_k=4)

        return {
            "is_connected": is_connected,
            "is_regular": is_regular,
            "is_k_regular": is_k_regular,
            "degree_sequence": sorted(degrees, reverse=True),
            "fiedler_eigenvalue": fiedler,
            "spectral_moments": moments
        }

    _analyze_terminal_geometry = evaluate_topological_invariants

    def evaluate_exact_multiway_induction(self, n: int, k: int, silent: bool = False, top_k: int = 5, save_cache: bool = True) -> Dict[str, Any]:
        """Executes exact layer-by-layer multiway state space enumeration under a fixed degree threshold k."""
        if n < 2:
            raise ValueError(f"Vertex scale N must be >= 2, got {n}")
        if k < 0:
            raise ValueError(f"Target degree k must be non-negative, got {k}")

        if not silent:
            print(f"Initializing exact multiway state space evaluation (N={n}, k={k})...")
        start_time = time.perf_counter()

        initial_state = self.generate_canonical_complete_graph(n)
        current_layer: Dict[CanonicalState, int] = {initial_state: 1}
        terminal_registry: Dict[CanonicalState, int] = collections.defaultdict(int)

        layer_index = 0

        while current_layer:
            layer_start = time.perf_counter()
            next_layer: Dict[CanonicalState, int] = collections.defaultdict(int)
            layer_paths_processed = sum(current_layer.values())

            for state, path_count in current_layer.items():
                degrees = self.get_vertex_degrees(state, n)
                has_rewrites = False

                for edge in state:
                    u, v = edge
                    if degrees[u] > k or degrees[v] > k:
                        child_edges = [e for e in state if e != edge]
                        canonical_child = self.canonicalize_unlabeled_graph(n, child_edges)
                        next_layer[canonical_child] += path_count
                        has_rewrites = True

                if not has_rewrites:
                    terminal_registry[state] += path_count

            layer_end = time.perf_counter()

            if not silent:
                print(f"  Layer {layer_index:<2} complete | Isomorphism Classes: {len(current_layer):<5} | Trajectory Paths: {layer_paths_processed:<12,} | Time: {layer_end - layer_start:.4f}s")

            current_layer = next_layer
            layer_index += 1

        total_paths = sum(terminal_registry.values())
        h_process_max = 0.0
        h_macro_realized = 0.0
        delta_h_realized = 0.0

        if total_paths > 0:
            h_process_max = math.log2(total_paths)
            h_macro_realized = -sum((count / total_paths) * math.log2(count / total_paths)
                                    for count in terminal_registry.values() if count > 0)
            delta_h_realized = h_process_max - h_macro_realized

        connected_paths = 0
        regular_paths = 0
        k_regular_paths = 0
        class_metrics = []

        for state, path_count in terminal_registry.items():
            geo = self.evaluate_topological_invariants(state, n, k)
            if geo["is_connected"]:
                connected_paths += path_count
            if geo["is_regular"]:
                regular_paths += path_count
            if geo["is_k_regular"]:
                k_regular_paths += path_count

            class_metrics.append({
                "state": [[u, v] for u, v in state],
                "path_count": path_count,
                "probability": path_count / total_paths if total_paths > 0 else 0.0,
                "degree_sequence": geo["degree_sequence"]
            })

        class_metrics.sort(key=lambda x: x["path_count"], reverse=True)

        if save_cache:
            output_filename = f"distribution_N{n}_k{k}.json"
            try:
                with open(output_filename, "w") as f:
                    json.dump(class_metrics, f, indent=4)
            except IOError as e:
                if not silent:
                    print(f"Warning: Failed to export distribution JSON: {e}")

            cache_filename = f"cache_N{n}_k{k}.pkl"
            try:
                with open(cache_filename, "wb") as f:
                    pickle.dump(self._canonical_cache, f)
            except IOError as e:
                if not silent:
                    print(f"Warning: Failed to export cache PKL: {e}")

        total_duration = time.perf_counter() - start_time
        if not silent:
            print(f"Scale N={n} complete in {total_duration:.2f}s\n")

        return {
            "total_paths": total_paths,
            "physical_classes": len(terminal_registry),
            "h_process_max": h_process_max,
            "h_macro_realized": h_macro_realized,
            "delta_h_realized": delta_h_realized,
            "p_connected": connected_paths / total_paths if total_paths > 0 else 0.0,
            "p_regular": regular_paths / total_paths if total_paths > 0 else 0.0,
            "p_k_regular": k_regular_paths / total_paths if total_paths > 0 else 0.0,
            "top_k_classes": class_metrics[:top_k],
            "all_classes": class_metrics,
            "execution_time_seconds": total_duration
        }

    evaluate_scale = evaluate_exact_multiway_induction

    def sample_monte_carlo_percolation(self, n: int, k: int, num_samples: int = 1000, seed: int = 42) -> Dict[str, Any]:
        """
        Fast Monte Carlo trajectory sampler for deep scales (N >= 9) where exhaustive DP is intractable.
        Samples random pruning paths from K_N to terminal states under degree threshold k.
        """
        import random
        rng = random.Random(seed)

        initial_state = list(self.generate_canonical_complete_graph(n))
        terminal_lengths = []
        connected_count = 0
        regular_count = 0
        degree_variance_sum = 0.0

        for _ in range(num_samples):
            current_edges = list(initial_state)
            steps = 0
            while True:
                degs = [0] * n
                for u, v in current_edges:
                    degs[u] += 1
                    degs[v] += 1
                prunable = [e for e in current_edges if degs[e[0]] > k or degs[e[1]] > k]
                if not prunable:
                    break
                chosen_edge = rng.choice(prunable)
                current_edges.remove(chosen_edge)
                steps += 1

            terminal_lengths.append(steps)
            canonical_terminal = tuple(sorted(current_edges))
            geo = self.evaluate_topological_invariants(canonical_terminal, n, k)
            if geo["is_connected"]:
                connected_count += 1
            if geo["is_regular"]:
                regular_count += 1

            degs = [0] * n
            for u, v in current_edges:
                degs[u] += 1
                degs[v] += 1
            mean_deg = sum(degs) / n
            var_deg = sum((d - mean_deg) ** 2 for d in degs) / n
            degree_variance_sum += var_deg

        return {
            "n": n,
            "k": k,
            "num_samples": num_samples,
            "mean_path_length": sum(terminal_lengths) / num_samples if num_samples > 0 else 0.0,
            "min_path_length": min(terminal_lengths) if terminal_lengths else 0,
            "max_path_length": max(terminal_lengths) if terminal_lengths else 0,
            "p_connected_sampled": connected_count / num_samples if num_samples > 0 else 0.0,
            "p_regular_sampled": regular_count / num_samples if num_samples > 0 else 0.0,
            "mean_degree_variance": degree_variance_sum / num_samples if num_samples > 0 else 0.0
        }

    sample_trajectory_statistics = sample_monte_carlo_percolation


# Alias for backwards compatibility
PreGeometricMultiwayAuditor = MultiwayStateSpaceAuditor


class ExplicitHypergraphRuleAuditor:
    """Auditor for explicit local Wolfram hypergraph substitution rules (2-in 4-out, 2-in 1-out, 2-in 2-out)."""

    def __init__(self):
        self._iso_cache: Dict[HypergraphState, HypergraphState] = {}

    def get_canonical_hypergraph(self, edges: HypergraphState) -> HypergraphState:
        """Quotients child hypergraphs by vertex permutations to eliminate redundant isomorphic states."""
        if edges in self._iso_cache:
            return self._iso_cache[edges]

        all_verts = sorted(set(v for e in edges for v in e))
        n = len(all_verts)
        vert_to_idx = {v: i for i, v in enumerate(all_verts)}
        norm_edges = tuple(sorted(tuple(sorted(vert_to_idx[v] for v in e)) for e in edges))

        canonical_min = None
        for p in itertools.permutations(range(n)):
            remapped = tuple(sorted(tuple(sorted(p[u] for u in e)) for e in norm_edges))
            if canonical_min is None or remapped < canonical_min:
                canonical_min = remapped

        res = frozenset(canonical_min)
        self._iso_cache[edges] = res
        return res

    def find_2in_matches(self, edges: HypergraphState) -> List[Tuple[Hyperedge, Hyperedge]]:
        """Finds all unique unordered pairs of edges sharing exactly one vertex (2-in rule match: {x,y} and {x,z})."""
        matches = []
        edge_list = sorted(list(edges))
        for i in range(len(edge_list)):
            for j in range(i + 1, len(edge_list)):
                e1, e2 = edge_list[i], edge_list[j]
                shared = set(e1) & set(e2)
                if len(shared) == 1:
                    matches.append((e1, e2))
        return matches

    def apply_2in_4out_rule(self, edges: HypergraphState, match: Tuple[Hyperedge, Hyperedge], new_vertex: int) -> HypergraphState:
        """Applies expansion rule {{x,y}, {x,z}} -> {{x,w}, {y,w}, {z,w}, {y,z}} where w is new_vertex."""
        e1, e2 = match
        x = list(set(e1) & set(e2))[0]
        y = list(set(e1) - {x})[0]
        z = list(set(e2) - {x})[0]
        w = new_vertex

        rem = set(edges) - {e1, e2}
        new_edges = {
            (min(x, w), max(x, w)),
            (min(y, w), max(y, w)),
            (min(z, w), max(z, w)),
            (min(y, z), max(y, z))
        }
        raw_child = frozenset(rem | new_edges)
        return self.get_canonical_hypergraph(raw_child)

    def apply_2in_1out_rule(self, edges: HypergraphState, match: Tuple[Hyperedge, Hyperedge]) -> HypergraphState:
        """Applies dimensional pruning contraction rule {{x,y}, {x,z}} -> {{y,z}} (reduces edge count by 1)."""
        e1, e2 = match
        x = list(set(e1) & set(e2))[0]
        y = list(set(e1) - {x})[0]
        z = list(set(e2) - {x})[0]

        rem = set(edges) - {e1, e2}
        new_edge = (min(y, z), max(y, z))
        raw_child = frozenset(rem | {new_edge})
        return self.get_canonical_hypergraph(raw_child)

    def find_2in_2out_swap_matches(self, edges: HypergraphState) -> List[Tuple[Hyperedge, Hyperedge]]:
        """Finds all unordered pairs of disjoint edges {u,v} and {w,z} with no shared vertices."""
        matches = []
        edge_list = sorted(list(edges))
        for i in range(len(edge_list)):
            for j in range(i + 1, len(edge_list)):
                e1, e2 = edge_list[i], edge_list[j]
                if not (set(e1) & set(e2)):
                    matches.append((e1, e2))
        return matches

    def apply_2in_2out_swap_rule(self, edges: HypergraphState, match: Tuple[Hyperedge, Hyperedge]) -> HypergraphState:
        """Applies degree-preserving topology swap {{u,v}, {w,z}} -> {{u,w}, {v,z}}."""
        e1, e2 = match
        u, v = e1
        w, z = e2

        rem = set(edges) - {e1, e2}
        new_edges = {
            (min(u, w), max(u, w)),
            (min(v, z), max(v, z))
        }
        raw_child = frozenset(rem | new_edges)
        return self.get_canonical_hypergraph(raw_child)

    def evaluate_multiway_branching(self, initial_edges: HypergraphState, steps: int = 2) -> Dict[str, Any]:
        """Calculates exact multiway branch count and distinct macrostates across asynchronous substitutions."""
        canonical_initial = self.get_canonical_hypergraph(initial_edges)
        current_layer: Dict[HypergraphState, int] = {canonical_initial: 1}
        next_free_vertex = max(max(e) for e in initial_edges) + 1 if initial_edges else 0

        branching_history = []

        for step in range(steps):
            next_layer: Dict[HypergraphState, int] = collections.defaultdict(int)
            total_matches_layer = 0

            for state, path_count in current_layer.items():
                matches = self.find_2in_matches(state)
                total_matches_layer += len(matches) * path_count
                for m in matches:
                    child = self.apply_2in_4out_rule(state, m, next_free_vertex + step)
                    next_layer[child] += path_count

            branching_history.append({
                "step": step,
                "input_states": len(current_layer),
                "total_branches": total_matches_layer,
                "distinct_child_states": len(next_layer)
            })
            current_layer = next_layer

        total_paths = sum(current_layer.values())
        h_process = math.log2(total_paths) if total_paths > 0 else 0.0

        return {
            "steps": steps,
            "branching_history": branching_history,
            "total_paths": total_paths,
            "distinct_macrostates": len(current_layer),
            "h_process": h_process
        }

    def evaluate_pruning_multiway(self, initial_edges: HypergraphState, steps: int = 2) -> Dict[str, Any]:
        """Calculates multiway branching under 2-in 1-out dimensional edge-pruning rule."""
        canonical_initial = self.get_canonical_hypergraph(initial_edges)
        current_layer: Dict[HypergraphState, int] = {canonical_initial: 1}

        branching_history = []
        for step in range(steps):
            next_layer: Dict[HypergraphState, int] = collections.defaultdict(int)
            total_matches_layer = 0

            for state, path_count in current_layer.items():
                matches = self.find_2in_matches(state)
                total_matches_layer += len(matches) * path_count
                for m in matches:
                    child = self.apply_2in_1out_rule(state, m)
                    next_layer[child] += path_count

            branching_history.append({
                "step": step,
                "input_states": len(current_layer),
                "total_branches": total_matches_layer,
                "distinct_child_states": len(next_layer)
            })
            current_layer = next_layer

        total_paths = sum(current_layer.values())
        h_process = math.log2(total_paths) if total_paths > 0 else 0.0

        return {
            "steps": steps,
            "branching_history": branching_history,
            "total_paths": total_paths,
            "distinct_macrostates": len(current_layer),
            "h_process": h_process
        }


# Alias for backwards compatibility
HypergraphRewriteAuditor = ExplicitHypergraphRuleAuditor


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multiway Causal Invariance & Entropic Obstruction Auditor")
    parser.add_argument("-n", "--nodes", type=int, nargs="+", default=[5, 6, 7, 8],
                        help="List of vertex scales (N) to evaluate sequentially.")
    parser.add_argument("-k", "--target-degree", type=int, default=3,
                        help="Maximum vertex coordinate configuration constraint threshold (default: 3)")
    parser.add_argument("--top-k", type=int, default=5,
                        help="Number of top dominant physical macrostate topologies to evaluate (default: 5)")
    parser.add_argument("--danger-zone", action="store_true",
                        help="Required flag to authorize scale configurations where N > 8")

    args = parser.parse_args()

    if any(n > 8 for n in args.nodes) and not args.danger_zone:
        print("\n[ERROR] Requested scale exceeds vertex cardinality N=8.")
        print("Authorizing verification runs past this boundary requires the flag: --danger-zone")
        sys.exit(1)

    runner = MultiwayStateSpaceAuditor()
    results = []

    print("-" * 90)
    print("Multiway Causal Invariance Auditor: Dimensional Reduction Phase Space Solver")
    print("-" * 90)

    for node_scale in args.nodes:
        runner.clear_cache()
        metrics = runner.evaluate_exact_multiway_induction(node_scale, args.target_degree, silent=False, top_k=args.top_k)
        results.append((node_scale, args.target_degree, metrics))

    print("\n" + "=" * 185)
    print("                                      SUMMARY EVALUATION MATRIX: DIMENSIONAL REDUCTION UNLABELED PHASE SPACE")
    print("=" * 185)
    print(f"{'Scale (N)':<11}{'Target (k)':<14}{'Trajectory Paths (M)':<24}{'Classes':<10}{'H_process (max)':<18}{'H_macro (Realized)':<22}{'Delta_H (Realized)':<18}{'P(Connected)':<17}{'P(Regular)':<15}{'P(Exact k-Reg)'}")
    print("-" * 185)
    for n, k, m in results:
        print(f"N = {n:<7}"
              f"k = {str(k):<10}"
              f"{m['total_paths']:<24,}"
              f"{m['physical_classes']:<10}"
              f"{m['h_process_max']:<18.4f}"
              f"{m['h_macro_realized']:<22.4f}"
              f"{m['delta_h_realized']:<18.4f}"
              f"{m['p_connected']:<17.4e}"
              f"{m['p_regular']:<15.4e}"
              f"{m['p_k_regular']:<17.4e}")
    print("=" * 185)

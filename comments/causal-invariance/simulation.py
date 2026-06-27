import collections
import itertools
import math
import time
import json
import pickle
import argparse
import sys
from typing import Tuple, List, Dict, Any

CanonicalState = Tuple[Tuple[int, int], ...]

class PreGeometricMultiwayAuditor:
    def __init__(self):
        # Universal cache persists across all layers within a scale to maintain O(1) lookups
        self._canonical_cache: Dict[Tuple[Tuple[int, int], ...], CanonicalState] = {}

    def clear_cache(self):
        """Clear cache between scales (canonical forms are N-dependent)."""
        self._canonical_cache.clear()

    def _generate_canonical_kn(self, n: int) -> CanonicalState:
        """Constructs the canonical baseline configuration for a complete graph K_N."""
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((i, j))
        return tuple(sorted(edges))

    def _get_vertex_degrees(self, state: CanonicalState, n: int) -> List[int]:
        """Computes the vertex coordinate degree sequence for the given state."""
        degrees = [0] * n
        for u, v in state:
            degrees[u] += 1
            degrees[v] += 1
        return degrees

    def _get_canonical_form(self, n: int, edges: List[Tuple[int, int]]) -> CanonicalState:
        """Remaps an edge configuration to its unique lexicographical minimum form via memoized permutation search."""
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

    def _analyze_terminal_geometry(self, state: CanonicalState, n: int, k: int) -> Dict[str, Any]:
        """Evaluates graph connectivity metrics and local degree sequence distributions."""
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
        
        return {
            "is_connected": is_connected,
            "is_regular": is_regular,
            "is_k_regular": is_k_regular,
            "degree_sequence": sorted(degrees, reverse=True)
        }

    def evaluate_scale(self, n: int, k: int, silent: bool = False, top_k: int = 5, save_cache: bool = True) -> Dict[str, Any]:
        """Executes a layer-by-layer multiway state space enumeration under a fixed degree threshold."""
        if not silent:
            print(f"Initializing multiway state space evaluation (N={n}, k={k})...")
        start_time = time.perf_counter()
        
        initial_state = self._generate_canonical_kn(n)
        current_layer: Dict[CanonicalState, int] = {initial_state: 1}
        terminal_registry: Dict[CanonicalState, int] = collections.defaultdict(int)
        
        layer_index = 0
        
        while current_layer:
            layer_start = time.perf_counter()
            next_layer: Dict[CanonicalState, int] = collections.defaultdict(int)
            layer_paths_processed = sum(current_layer.values())
            
            for state, path_count in current_layer.items():
                degrees = self._get_vertex_degrees(state, n)
                has_rewrites = False
                
                for edge in state:
                    u, v = edge
                    if degrees[u] > k or degrees[v] > k:
                        child_edges = [e for e in state if e != edge]
                        canonical_child = self._get_canonical_form(n, child_edges)
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
            geo = self._analyze_terminal_geometry(state, n, k)
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
        
        output_filename = f"distribution_N{n}_k{k}.json"
        with open(output_filename, "w") as f:
            json.dump(class_metrics, f, indent=4)

        if save_cache:
            cache_filename = f"cache_N{n}_k{k}.pkl"
            with open(cache_filename, "wb") as f:
                pickle.dump(self._canonical_cache, f)

        total_duration = time.perf_counter() - start_time
        if not silent:
            print(f"Scale N={n} complete in {total_duration:.2f}s (Configuration data exported to {output_filename})\n")
                
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
            "execution_time_seconds": total_duration
        }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Discrete Hypergraph Evolution & Multiway Trajectory Auditor")
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

    runner = PreGeometricMultiwayAuditor()
    results = []
    
    print("-" * 90)
    print("Discrete Hypergraph Evolution Matrix: Multiway Trajectory Space Simulation Engine")
    print("-" * 90)
    
    for node_scale in args.nodes:
        runner.clear_cache()
        metrics = runner.evaluate_scale(node_scale, args.target_degree, silent=False, top_k=args.top_k)
        results.append((node_scale, args.target_degree, metrics))
        
    print("\n" + "=" * 185)
    print("                                      SUMMARY EVALUATION MATRIX: DIMENSIONAL REDUCTION UNLABELED PHASE SPACE")
    print("=" * 185)
    print(f"{'Scale (N)':<11}{'Target (k)':<14}{'Trajectory Paths (M)':<24}{'Classes':<10}{'H_process (max)':<18}{'H_macro (Realized)':<22}{'ΔH (Realized)':<18}{'P(Connected)':<17}{'P(Regular)':<15}{'P(Exact k-Reg)'}")
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

    print("\n--- MACROSTATE DISTRIBUTION ANALYSIS: TOPOLOGICAL CONFIGURATION PROFILES ---")
    for n, k, m in results:
        print(f"\nScale N={n}, k={k} | Distribution Profile across Dominant Isomorphism Classes:")
        for idx, item in enumerate(m['top_k_classes']):
            print(f"  Rank {idx+1}: Representation={item['probability']*100:.2f}% | Degree Sequence={item['degree_sequence']}")

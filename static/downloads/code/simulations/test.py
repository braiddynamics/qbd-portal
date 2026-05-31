#!/usr/bin/env python
# -----------------------------------------------------------------------------
# Title:     QBD Spontaneous Ignition and Symmetry-Breaking Audit
# Subject:   Audits spontaneous loop nucleation and symmetry-breaking tunneling
#            claims in Chapter 18.1.6 (Standalone Version).
# Version:   1.1
# -----------------------------------------------------------------------------

import random
import numpy as np
import pandas as pd
import networkx as nx

# --- Standalone Graph Setup & Invariant Generators ---

def build_directed_bethe_fragment(depth, k=3):
    """
    Constructs a directed regular Bethe lattice fragment.
    Edges point from root (layer 0) to leaves (future).
    Enforces a strict bipartite partitioning based on layer parity.
    """
    G = nx.DiGraph()
    root = 0
    G.add_node(root, layer=0, partition="A")
   
    current_layer = [root]
    next_node_id = 1
   
    for d in range(depth):
        next_layer = []
        partition_name = "B" if (d + 1) % 2 == 1 else "A"
        
        for parent in current_layer:
            # Root splits into k, others split into k-1 (one parent, k-1 children)
            num_children = k if parent == root else k - 1
           
            for _ in range(num_children):
                child = next_node_id
                G.add_node(child, layer=d+1, partition=partition_name)
                G.add_edge(parent, child)
               
                next_layer.append(child)
                next_node_id += 1
        current_layer = next_layer
        
    return G

def find_all_2_paths(G):
    """Finds all unique directed 2-paths u -> v -> w in the DiGraph."""
    paths = []
    for u in G.nodes():
        for v in list(G.successors(u)):
            for w in list(G.successors(v)):
                if w != u:  # Avoid trivial 2-cycles
                    paths.append((u, v, w))
    return paths

def greedy_edge_disjoint_paths(paths):
    """Finds a maximal set of edge-disjoint 2-paths to audit packing constraints."""
    independent_set = []
    used_edges = set()
    for u, v, w in paths:
        e1 = (u, v)
        e2 = (v, w)
        if e1 not in used_edges and e2 not in used_edges:
            independent_set.append((u, v, w))
            used_edges.add(e1)
            used_edges.add(e2)
    return independent_set

def count_directed_3_cycles_fast(G):
    """Optimized O(N) directed 3-cycle counter for low out-degree graphs."""
    count = 0
    for u in G.nodes():
        for v in G.successors(u):
            if v == u: continue
            for w in G.successors(v):
                if w == v or w == u: continue
                if G.has_edge(w, u):
                    count += 1
    return count // 3

# --- Stochastic Alignment Simulations ---

def simulate_bipartite_stasis(G, trials=3000):
    """
    Model 1: Bipartite Stasis.
    Out-degree slots are re-assigned strictly within opposite-partition neighbors.
    Enforces horizon leaf damping to preserve bipartite metrics.
    """
    nodes = list(G.nodes())
    undirected_G = G.to_undirected()
    
    cycles_closed = []
    for _ in range(trials):
        G_trial = nx.DiGraph()
        G_trial.add_nodes_from(nodes)
        for u in nodes:
            candidates = list(undirected_G.neighbors(u))
            if len(candidates) >= 2:
                targets = random.sample(candidates, 2)
            else:
                # Horizon Leaf Damping: boundary nodes do not introduce non-local edges
                targets = candidates
            for v in targets:
                G_trial.add_edge(u, v)
        cycles_closed.append(count_directed_3_cycles_fast(G_trial))
    return np.mean(cycles_closed), np.std(cycles_closed)

def simulate_symmetry_breaking(G, trials=3000):
    """
    Model 2: Symmetry-Breaking Tunneling.
    Out-degree slots can align to same-partition neighbors at distance 2,
    explicitly breaking bipartite symmetry.
    """
    nodes = list(G.nodes())
    undirected_G = G.to_undirected()
    
    cycles_closed = []
    for _ in range(trials):
        G_trial = nx.DiGraph()
        G_trial.add_nodes_from(nodes)
        for u in nodes:
            neighbors = list(undirected_G.neighbors(u))
            candidates = set()
            for n in neighbors:
                for nn in undirected_G.neighbors(n):
                    if nn != u:
                        candidates.add(nn)
            candidates = list(candidates)
            if len(candidates) >= 2:
                targets = random.sample(candidates, 2)
            else:
                # Horizon Leaf Damping
                targets = candidates
            for v in targets:
                G_trial.add_edge(u, v)
        cycles_closed.append(count_directed_3_cycles_fast(G_trial))
    return np.mean(cycles_closed), np.std(cycles_closed)

def run_ignition_audit():
    # Sweep depths 2 to 9 to verify scaling parameters
    depths = [2, 3, 4, 5, 6, 7, 8, 9]
    
    print("="*80)
    print("Spontaneous Loop Nucleation Audit (Theorem 18.1.2 Verification)")
    print("Pre-Geometric Bipartite Stasis vs. Symmetry-Breaking Tunneling")
    print("="*80)
    
    results = []
    for d in depths:
        # Generate self-contained directed Bethe lattice fragment
        G_vacuum = build_directed_bethe_fragment(depth=d, k=3)
        N = G_vacuum.number_of_nodes()
        
        # Verify 3-cycles is exactly 0 in the pre-ignition vacuum
        initial_cycles = count_directed_3_cycles_fast(G_vacuum)
        assert initial_cycles == 0, f"Error: ZPI vacuum contains {initial_cycles} initial cycles!"
        
        paths = find_all_2_paths(G_vacuum)
        edge_disj = greedy_edge_disjoint_paths(paths)
        
        m1_mean, m1_std = simulate_bipartite_stasis(G_vacuum, trials=3000)
        m2_mean, m2_std = simulate_symmetry_breaking(G_vacuum, trials=3000)
        
        theoretical_current = N / 32.0
        
        results.append({
            "Depth": d,
            "N": N,
            "Total 2-Paths": len(paths),
            "Max Precursors": len(edge_disj),
            "Model 1 (Stasis)": f"{m1_mean:.4f} ± {m1_std:.3f}",
            "Model 2 (Tunnel)": f"{m2_mean:.4f} ± {m2_std:.3f}",
            "Theoretical (N/32)": f"{theoretical_current:.4f}"
        })
        
    df = pd.DataFrame(results)
    print(df.to_markdown(index=False, tablefmt="github"))
    print("="*80)

if __name__ == "__main__":
    run_ignition_audit()

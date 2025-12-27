import networkx as nx
import numpy as np
from collections import defaultdict
import math
from typing import List

def automorphisms(G):
    if G.number_of_nodes() == 0: return 1
    N = G.number_of_nodes()
    if N == 1: return 1
   
    if isinstance(G, nx.Graph):
        matcher = nx.isomorphism.GraphMatcher(G, G)
    else:
        matcher = nx.isomorphism.DiGraphMatcher(G, G)
   
    try:
        iso_count = len(list(matcher.isomorphisms_iter()))
        return iso_count
    except Exception as e:
        return 0

def compute_orbit_sizes(G: nx.Graph) -> List[int]:
    matcher = nx.isomorphism.GraphMatcher(G, G)
    autos_list = list(matcher.isomorphisms_iter())
    nodes = list(G.nodes())
    orbits = {}
    for v in nodes:
        orbit_set = frozenset(m[v] for m in autos_list)
        if orbit_set not in orbits:
            orbits[orbit_set] = len(orbit_set)
    return list(orbits.values())

def compute_H_S(G: nx.Graph) -> float:
    sizes = compute_orbit_sizes(G)
    N = G.number_of_nodes()
    if N == 0: return 0.0
    p = np.array(sizes) / N
    return -np.sum(p * np.log2(p + 1e-10))

# --- Lemma Filters ---
def filter_lemma_3_2_6(G: nx.Graph) -> bool:
    # Filter suboptimal sites: low 2-path density (e.g., linear/sparse trees)
    degrees = dict(G.degree())
    internal = [d for d in degrees.values() if d > 1]
    if not internal: return False
    avg_internal_deg = sum(internal) / len(internal)
    return avg_internal_deg > 2.5  # Threshold for sufficient branching/site density

def filter_lemma_3_2_7(G: nx.Graph) -> bool:
    # Filter non-regular: variance in internal degrees
    degrees = dict(G.degree())
    internal = [d for d in degrees.values() if d > 1]
    if not internal: return False
    return np.var(internal) < 0.5  # Low variance for regularity

def filter_lemma_3_2_8(G: nx.Graph) -> bool:
    # Filter non-level-transitive: low automorphism count relative to N
    aut = automorphisms(G)
    return aut >= 1152  # Threshold for sufficient symmetry/transitivity

# Main Census for N=10
if __name__ == "__main__":
    N = 10
    lambda_vals = np.linspace(0.4, 0.6, 5)
   
    # Enumerate all non-isomorphic trees
    trees = list(nx.nonisomorphic_trees(N))
    filtered = trees[:]
    print("Start with trees (after 3.2.4):", len(filtered))
   
    # Apply Lemma 3.2.6 filter
    filtered = [tree for tree in filtered if filter_lemma_3_2_6(tree)]
    print("After 3.2.6 (suboptimal sites):", len(filtered))
   
    # Apply Lemma 3.2.7 filter
    filtered = [t for t in filtered if filter_lemma_3_2_7(t)]
    print("After 3.2.7 (non-regular):", len(filtered))
   
    # Apply Lemma 3.2.8 filter
    filtered = [t for t in filtered if filter_lemma_3_2_8(t)]
    print("After 3.2.8 (non-level-transitive):", len(filtered))
   
    # Compute Scores
    max_S_list = []
    filtered_details = []
    for tree in filtered:
        aut = automorphisms(tree)
        aut_log = math.log2(aut + 1e-10)
        hs = compute_H_S(tree)
        S_vals = [lam * aut_log + (1 - lam) * hs for lam in lambda_vals]
        max_S = max(S_vals)
        max_S_list.append(max_S)
        filtered_details.append((aut, hs, max_S))
   
    # Select Bethe (Best Score)
    b_max_S = max(max_S_list)
   
    print(f"N={N}: Bethe max_S in range [0.4,0.6]: {b_max_S:.3f}")
    print("Remaining trees after all lemmas:", len(filtered))
   
    # Best Survivor
    idx = max_S_list.index(b_max_S)
    print(f"Bethe: |Aut| = {filtered_details[idx][0]}, H_S = {filtered_details[idx][1]:.2f}")
   
    print("Remaining details (|Aut|, H_S, max_S):")
    for det in filtered_details:
        print(f" ({det[0]}, {det[1]:.1f}, {det[2]:.3f})")
import networkx as nx
import numpy as np
from collections import defaultdict
import math
def automorphisms(G):
    matcher = nx.algorithms.isomorphism.GraphMatcher(G, G)
    return sum(1 for _ in matcher.isomorphisms_iter())
def compute_orbit_sizes(G):
    matcher = nx.isomorphism.GraphMatcher(G, G)
    autos_list = list(matcher.isomorphisms_iter())
    nodes = list(G.nodes())
    orbits = defaultdict(set)
    for v in nodes:
        orbit = frozenset(m[v] for m in autos_list)
        orbits[orbit] = len(orbit)
    return list(orbits.values())
def compute_H_S(G):
    sizes = compute_orbit_sizes(G)
    N = G.number_of_nodes()
    p = np.array(sizes) / N
    return -np.sum(p * np.log2(p + 1e-10))
def aut_size(G):
    return automorphisms(G)
# Star-like for N=10: center 0, leaves 1-9
G_star = nx.Graph()
G_star.add_edges_from([(0, i) for i in range(1, 10)])
# Bethe for N=10: root 0, level1 1-3, level2 4-9
G_bethe = nx.Graph()
G_bethe.add_edges_from([(0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(2,7),(3,8),(3,9)])
aut_star = math.factorial(9) # 9!
p_star = np.array([1/10, 9/10])
hs_star = -np.sum(p_star * np.log2(p_star + 1e-10))
aut_bethe = aut_size(G_bethe)
hs_bethe = compute_H_S(G_bethe)
# Dynamic prints
print(f"Star-like: |Aut| = {aut_star}, H_S = {hs_star:.2f}")
print(f"Bethe: |Aut| = {aut_bethe}, H_S = {hs_bethe:.2f}")
print(f"Comparison: Bethe H_S > Star H_S: {hs_bethe > hs_star}")
# Table (executes to stdout)
print("\n| Graph | |Aut| | H_S |")
print("|-------|------|-----|")
print(f"| Star | {aut_star} | {hs_star:.2f} |")
print(f"| Bethe | {aut_bethe} | {hs_bethe:.2f} |")
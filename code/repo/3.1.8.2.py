import networkx as nx
import math
# Two disconnected directed trees (each a star with 3 leaves)
G_disc = nx.DiGraph()
G_disc.add_edges_from([(0,1),(0,2),(0,3),(4,5),(4,6),(4,7)]) # N=8
# Equivalent connected graph: merge by adding one bridging edge
G_conn = nx.DiGraph(G_disc)
G_conn.add_edge(3,4)
# Automorphism counts (using NetworkX isomorphism matcher)
def aut_count(G):
    matcher = nx.algorithms.isomorphism.DiGraphMatcher(G, G)
    return sum(1 for _ in matcher.isomorphisms_iter())
print("Disconnected |Aut|:", aut_count(G_disc)) # 72 (3! × 3! × 2)
print("Connected |Aut|:", aut_count(G_conn)) # dramatically smaller
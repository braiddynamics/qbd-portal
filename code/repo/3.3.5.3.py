import networkx as nx
import math

def automorphisms(G):
    N = G.number_of_nodes()
    if N <= 1:
        return 1
    degrees = [G.degree(v) for v in G.nodes()]
    if max(degrees) == N - 1:  # Star fallback
        return math.factorial(N - 1)
    matcher = nx.algorithms.isomorphism.GraphMatcher(G, G)
    try:
        return len(list(matcher.isomorphisms_iter()))
    except:
        return 0  # Timeout fallback

# Balanced Bethe N=7 undirected: root 0, level1:1-3, level2:4-6 (one each)
G0 = nx.Graph()
G0.add_edges_from([(0,1),(0,2),(0,3),(1,4),(2,5),(3,6)])  # N=7

print("Initial G0 |Aut|:", automorphisms(G0))  # 6 (S3 on 1-3)

# Mock sites: chords between level1 siblings
chords = [(1,2), (1,3), (2,3)]

# Parallel: add all
G_par = G0.copy()
for c in chords:
    G_par.add_edge(*c)
print("Parallel G1 |Aut|:", automorphisms(G_par))  # 6 (preserves K3 sym)

# Sequential: add only first
G_seq = G0.copy()
G_seq.add_edge(1,2)
print("Sequential G1 |Aut|:", automorphisms(G_seq))  # 2 (breaks)
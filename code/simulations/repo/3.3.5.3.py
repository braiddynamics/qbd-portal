import networkx as nx
import math

def get_automorphism_count(G):
    """Calculates the size of the automorphism group."""
    matcher = nx.isomorphism.GraphMatcher(G, G)
    try:
        return len(list(matcher.isomorphisms_iter()))
    except:
        return 0

# 1. Setup: Balanced Bethe Fragment (N=7)
# Structure: Root(0) -> Level1{1,2,3} -> Level2{4,5,6}
# Symmetries: Permutation of branches {1,4}, {2,5}, {3,6} => S3 Group
G0 = nx.Graph()
G0.add_edges_from([(0,1), (0,2), (0,3), (1,4), (2,5), (3,6)])

print(f"{'State':<20} | {'|Aut|':<10} | {'Symmetry Status'}")
print("-" * 65)

aut_0 = get_automorphism_count(G0)
print(f"{'Initial Vacuum':<20} | {aut_0:<10} | Perfect Symmetry (S3)")

# 2. Define Compliant Sites (Chords between Level 1 siblings)
# Potential edges: (1,2), (2,3), (1,3)
sites = [(1,2), (2,3), (1,3)]

# 3. Scenario A: Sequential Update (Random Choice)
# Scheduler picks site (1,2) arbitrarily.
G_seq = G0.copy()
G_seq.add_edge(*sites[0])
aut_seq = get_automorphism_count(G_seq)
status_seq = "BROKEN" if aut_seq < aut_0 else "PRESERVED"
print(f"{'Sequential Update':<20} | {aut_seq:<10} | {status_seq} (Distinguishes Branch 3)")

# 4. Scenario B: Parallel Update (All Sites)
# Scheduler executes all compliant updates simultaneously.
G_par = G0.copy()
G_par.add_edges_from(sites)
aut_par = get_automorphism_count(G_par)
status_par = "BROKEN" if aut_par < aut_0 else "PRESERVED"
print(f"{'Parallel Update':<20} | {aut_par:<10} | {status_par} (Equivariant)")
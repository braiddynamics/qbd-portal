import networkx as nx
from networkx.algorithms.isomorphism import DiGraphMatcher

def count_automorphisms(G):
    """Calculates the cardinality of the automorphism group Aut(G)."""
    matcher = DiGraphMatcher(G, G)
    return sum(1 for _ in matcher.isomorphisms_iter())

# 1. Disconnected Configuration
# Two separate stars: 0->{1,2,3} and 4->{5,6,7}
G_disc = nx.DiGraph()
G_disc.add_edges_from([(0,1), (0,2), (0,3)])
G_disc.add_edges_from([(4,5), (4,6), (4,7)])

# 2. Connected Configuration
# Bridge the roots: 3->4
G_conn = nx.DiGraph(G_disc)
G_conn.add_edge(3, 4)

# --- Execution ---
aut_disc = count_automorphisms(G_disc)
aut_conn = count_automorphisms(G_conn)
ratio = aut_disc / aut_conn

print(f"{'Metric':<20} | {'Disconnected':<15} | {'Connected':<15}")
print("-" * 55)
print(f"{'|Aut(G)|':<20} | {aut_disc:<15} | {aut_conn:<15}")
print("-" * 55)
print(f"Symmetry Reduction Factor: {ratio:.1f}x")
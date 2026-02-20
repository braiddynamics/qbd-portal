import networkx as nx
import numpy as np
from collections import defaultdict
import math

def calculate_orbit_entropy(G):
    """
    Computes the Shannon entropy of the automorphism orbit distribution.
    Higher entropy -> More uniform/indistinguishable vertices.
    """
    matcher = nx.isomorphism.GraphMatcher(G, G)
    autos = list(matcher.isomorphisms_iter())
    N = G.number_of_nodes()
    
    # Identify orbits
    node_orbits = defaultdict(set)
    processed = set()
    
    orbits = []
    for v in G.nodes():
        if v in processed: continue
        
        # Find all nodes u such that f(v) = u for some automorphism f
        orbit_members = {mapping[v] for mapping in autos}
        orbits.append(len(orbit_members))
        processed.update(orbit_members)
        
    # Calculate Entropy
    # P(Orbit) = Size(Orbit) / N
    probs = np.array(orbits) / N
    entropy = -np.sum(probs * np.log2(probs))
    
    return len(autos), entropy

# 1. Star Graph (N=10)
G_star = nx.star_graph(9) # Center 0, 9 leaves

# 2. Bethe Fragment (N=10)
# Root 0 -> 1,2,3; 1->4,5; 2->6,7; 3->8,9
G_bethe = nx.Graph()
G_bethe.add_edges_from([(0,1), (0,2), (0,3)])
G_bethe.add_edges_from([(1,4), (1,5), (2,6), (2,7), (3,8), (3,9)])

# --- Execution ---
aut_star, hs_star = calculate_orbit_entropy(G_star)
aut_bethe, hs_bethe = calculate_orbit_entropy(G_bethe)

print(f"{'Structure':<15} | {'|Aut|':<10} | {'Orbit Entropy':<15}")
print("-" * 45)
print(f"{'Star (Irreg)':<15} | {aut_star:<10} | {hs_star:.4f}")
print(f"{'Bethe (Reg)':<15} | {aut_bethe:<10} | {hs_bethe:.4f}")
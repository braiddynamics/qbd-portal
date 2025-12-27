import networkx as nx
import csv
import os
import numpy as np
from math import log
def generate_bethe_fragment(depth=5, b=3):
    if depth < 1 or b < 3:
        raise ValueError("Depth must be at least 1 and coordination number b must be at least 3.")
   
    G = nx.Graph()
    node_id = 0
    root = node_id
    node_id += 1
    G.add_node(root)
   
    levels = [[root]]
   
    for d in range(depth):
        next_level = []
        for parent in levels[-1]:
            # Root has b children; others have b-1 (since 1 edge goes up)
            num_children = b if parent == root else b - 1
            for _ in range(num_children):
                child = node_id
                node_id += 1
                G.add_node(child)
                G.add_edge(parent, child)
                next_level.append(child)
       
        if not next_level:
            break
        levels.append(next_level)
   
    total_nodes = G.number_of_nodes()
    if total_nodes == 0:
        return G, {}
       
    regular_nodes = sum(1 for v in G if G.degree(v) == b)
    regularity_fraction = regular_nodes / total_nodes
    analytical_fraction = 1.0 / (b - 1)
   
    metrics = {
        'depth': depth,
        'b': b,
        'nodes': total_nodes,
        'edges': G.number_of_edges(),
        'girth': float('inf'),
        'frac_b_regular': float(regularity_fraction),
        'frac_b_regular_analytical': float(analytical_fraction)
    }
    return G, metrics
def main():
    print("Quantum Braid Dynamics: Bethe Fragment Scaling Analysis (v1.0)")
    print("=" * 70)
   
    configs_to_test = []
    # Test k=3 for depths 3 to 15
    for depth in range(3, 16):
        configs_to_test.append({'depth': depth, 'b': 3})
    # Test k=4,5,6 for depth 5
    for b in [4, 5, 6]:
        configs_to_test.append({'depth': 5, 'b': b})
       
    print(f"{'Depth':<6} {'Coord.(b)':<10} {'Nodes':<10} {'Girth':<8} {'b-Regular%':<12} {'Theoretical Limit'}")
    print("-" * 70)
   
    for config in configs_to_test:
        _, metrics = generate_bethe_fragment(depth=config['depth'], b=config['b'])
        d = metrics['depth']
        b = metrics['b']
        n = metrics['nodes']
        g = "inf"
        frac = metrics['frac_b_regular']
        limit = metrics['frac_b_regular_analytical']
       
        print(f"{d:<6} {b:<10} {n:<10} {g:<8} {frac:<12.3%} {limit:.3%}")
if __name__ == "__main__":
    main()
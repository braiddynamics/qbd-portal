# §18.1.9 — Bipartite Parity Phase Transition

import numpy as np
import pandas as pd
import networkx as nx

def build_directed_bethe_fragment(depth=4, k=3):
    G = nx.DiGraph()
    root = 0
    G.add_node(root, layer=0, partition="A")
    
    current_layer = [root]
    next_node_id = 1
    
    for d in range(depth):
        next_layer = []
        partition_name = "B" if (d + 1) % 2 == 1 else "A"
        for parent in current_layer:
            num_children = k if parent == root else k - 1
            for _ in range(num_children):
                child = next_node_id
                G.add_node(child, layer=d+1, partition=partition_name)
                G.add_edge(parent, child)
                next_layer.append(child)
                next_node_id += 1
        current_layer = next_layer
    return G

def simulate_symmetry_breaking_sweep():
    """§18.1.9: sweep tunneling beta; track bipartite parity Phi and loop density under stasis vs breaking."""
    np.random.seed(42)
    results = []
    
    # Generate trivalent Bethe tree substrate
    G_base = build_directed_bethe_fragment(depth=5, k=3)
    N = G_base.number_of_nodes()
    
    # Count initial partitions
    partitions_base = nx.get_node_attributes(G_base, "partition")
    nodes_A = [n for n, p in partitions_base.items() if p == "A"]
    nodes_B = [n for n, p in partitions_base.items() if p == "B"]
    
    # Sweep beta
    beta_vals = np.linspace(0.0, 1.0, 11)
    
    for beta in beta_vals:
        # Run multiple trials and average
        trials = 100
        trial_parities = []
        trial_cycles = []
        
        for _ in range(trials):
            G_trial = nx.DiGraph()
            G_trial.add_nodes_from(G_base.nodes(data=True))
            
            # Align out-degree slots for each node
            for u in G_base.nodes():
                # Get neighbors in undirected base graph
                undirected_G = G_base.to_undirected()
                neighbors = list(undirected_G.neighbors(u))
                
                # Check tunneling choice
                if np.random.random() >= beta:
                    # Stasis: align strictly to opposite partition neighbors
                    targets = neighbors
                else:
                    # Tunneling: align to same-partition neighbor-of-neighbors
                    candidates = set()
                    for n in neighbors:
                        for nn in undirected_G.neighbors(n):
                            if nn != u:
                                candidates.add(nn)
                    targets = list(candidates)
                    
                # Direct outgoing slots (up to 2 edges)
                if len(targets) >= 2:
                    selected = np.random.choice(targets, 2, replace=False)
                else:
                    selected = targets
                    
                for v in selected:
                    G_trial.add_edge(u, v)
                    
            # Count 3-cycles in the trial graph
            # Fast cycle counter
            count = 0
            for u_node in G_trial.nodes():
                for v_node in G_trial.successors(u_node):
                    if v_node == u_node: continue
                    for w_node in G_trial.successors(v_node):
                        if w_node == v_node or w_node == u_node: continue
                        if G_trial.has_edge(w_node, u_node):
                            count += 1
            cycles = count // 3
            
            # Reconstruct partitions on the new trial graph
            # If the trial graph remains bipartite, it admits a perfect partition.
            # Otherwise, some same-partition edges exist.
            # Measure the fraction of edges that connect same-partition nodes.
            same_part_edges = 0
            total_edges = G_trial.number_of_edges()
            
            for u_edge, v_edge in G_trial.edges():
                part_u = partitions_base[u_edge]
                part_v = partitions_base[v_edge]
                if part_u == part_v:
                    same_part_edges += 1
                    
            same_part_fraction = same_part_edges / total_edges if total_edges > 0 else 0.0
            
            trial_parities.append(same_part_fraction)
            trial_cycles.append(cycles)
            
        mean_parity = np.mean(trial_parities)
        mean_cycles = np.mean(trial_cycles)
        
        # State classification
        if mean_cycles == 0:
            state = "Pre-Geometric Stasis"
        elif mean_parity < 0.2:
            state = "Igniting Plasma"
        else:
            state = "Crystallized Geometry"
            
        results.append({
            "Coupling (β)": f"{beta:.2f}",
            "Tunneling Prob": f"{beta * 100:.0f}%",
            "Parity Violation (Φ)": f"{mean_parity:.4f}",
            "3-Cycles Closed": f"{mean_cycles:.2f}",
            "Phase State": state
        })
        
    return results

def run_transition():
    print("-" * 72)
    print("§18.1.9 Bipartite Parity Phase Transition")
    print("Sweeping Tunneling Coupling and Tracking Bipartite Parity Violations")
    print("-" * 72)
    
    results = simulate_symmetry_breaking_sweep()
    df = pd.DataFrame(results)
    print(df.to_markdown(index=False, tablefmt="github"))
    print("-" * 72)

if __name__ == "__main__":
    run_transition()

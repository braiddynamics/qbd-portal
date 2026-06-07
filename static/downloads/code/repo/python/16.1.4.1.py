import networkx as nx
import numpy as np
from scipy.optimize import curve_fit

def verify_ryu_takayanagi_scaling():
    """
    Simulation 16.1.4.1: Discrete Ryu-Takayanagi Verification.

    This routine constructs a Tensor Network model of Hyperbolic Space (AdS_3)
    using a MERA-like graph structure (Binary Tree + Lateral Disentanglers).
    It calculates the Entanglement Entropy of a boundary region L via the
    Min-Cut of the bulk graph and verifies the holographic scaling law:
    S(L) ~ c/3 * log(L).
    """

    # -------------------------------------------------------------------------
    # 1. Bulk Geometry Construction (MERA / AdS Discretization)
    # -------------------------------------------------------------------------
    # We construct a balanced binary tree representing the renormalization flow.
    # Depth 7 yields 2^7 = 128 boundary sites (UV cutoff).
    depth = 7  
    G = nx.balanced_tree(r=2, h=depth)

    # Helper to map depth levels to specific node lists
    nodes_at_depth = {}
    curr_node_idx = 0
    for d in range(depth + 1):
        count = 2**d
        nodes_at_depth[d] = list(range(curr_node_idx, curr_node_idx + count))
        curr_node_idx += count

    # Add Lateral "Disentangler" Edges
    # In MERA, these represent local unitaries removing short-range entanglement.
    # Geometrically, they create the tessellation of the hyperbolic plane.
    for d in range(1, depth + 1):
        nodes = nodes_at_depth[d]
        for i in range(len(nodes) - 1):
            u, v = nodes[i], nodes[i+1]
            # Capacity = 1.0 (Unit Bit of Entanglement)
            G.add_edge(u, v, capacity=1.0)

    # Ensure vertical edges also have unitary capacity
    for u, v in G.edges():
        if 'capacity' not in G[u][v]:
            G[u][v]['capacity'] = 1.0

    # Define Boundary Layer (The Leaves)
    boundary_nodes = nodes_at_depth[depth]

    # Add Super-Source and Super-Sink for Max-Flow/Min-Cut calculation
    G.add_node("SOURCE")
    G.add_node("SINK")

    # -------------------------------------------------------------------------
    # 2. Holographic Entropy Calculation
    # -------------------------------------------------------------------------
    # We test regions of increasing size L to observe entropy scaling.
    region_sizes = [2, 4, 8, 16, 32, 64]
    entropies = []

    print(f"{'Boundary Region (L)':<20} | {'Min-Cut / Entropy (S)':<22} | {'Scaling Ratio S/log2(L)'}")
    print("-" * 70)

    for L in region_sizes:
        # Define Region A (Source) and Region B (Sink)
        region_A = boundary_nodes[:L]
        region_B = boundary_nodes[L:]

        # Connect Boundary to Super-Nodes with infinite capacity
        # This forces the cut to occur within the bulk geometry.
        source_edges = [("SOURCE", n) for n in region_A]
        sink_edges = [("SINK", n) for n in region_B]

        G.add_edges_from(source_edges, capacity=1e9)
        G.add_edges_from(sink_edges, capacity=1e9)

        # Compute Min-Cut (Ryu-Takayanagi Formula: S_A = Area_min)
        cut_value, _ = nx.minimum_cut(G, "SOURCE", "SINK")
        entropies.append(cut_value)

        # Analyze Logarithmic Scaling
        log_L = np.log2(L)
        ratio = cut_value / log_L if L > 1 else 0.0

        print(f"{L:<20} | {cut_value:<22.4f} | {ratio:.4f}")

        # Cleanup for next iteration
        G.remove_edges_from(source_edges)
        G.remove_edges_from(sink_edges)

    # -------------------------------------------------------------------------
    # 3. Scaling Fit Analysis
    # -------------------------------------------------------------------------
    def log_scaling_law(x, c_eff, const):
        return c_eff * np.log2(x) + const

    try:
        popt, _ = curve_fit(log_scaling_law, region_sizes, entropies)
        c_effective = popt[0]
        offset = popt[1]

        print("-" * 70)
        print(f"Fit Model: S(L) = c_eff * log2(L) + k")
        print(f"Effective Central Charge (c_eff): {c_effective:.4f}")
        print(f"Geometric Offset (k):             {offset:.4f}")

    except Exception as e:
        print(f"Curve fitting failed: {e}")

if __name__ == "__main__":
    verify_ryu_takayanagi_scaling()

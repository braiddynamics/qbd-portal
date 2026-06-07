import networkx as nx
import numpy as np

def verify_distance_gap():
    """
    Simulation 15.1.6.1: Bi-Metric Distance Gap Verification.
    
    This routine verifies the divergence between the emergent manifold metric (d_geo)
    and the intrinsic graph metric (d_topo) in the presence of a non-local 
    entanglement bridge.
    """
    
    # -------------------------------------------------------------------------
    # System Initialization
    # -------------------------------------------------------------------------
    # We model the emergent manifold M as a 1D compact cycle (Ring) of size N.
    # An entanglement bridge is introduced between antipodal nodes (0, N/2).
    manifold_sizes = [10, 50, 100, 500, 1000]

    # Header Output
    print(f"{'Manifold Size (N)':<20} | {'d_topo (Bridge)':<18} | {'d_geo (Bulk)':<18} | {'Gap Ratio'}")
    print("-" * 75)

    for N in manifold_sizes:
        # 1. Manifold Construction (Bulk Geometry)
        # Generate cycle graph C_N representing the discretized bulk metric.
        G = nx.cycle_graph(N)
        
        # Define antipodal points (Subsystems A and B)
        node_A = 0
        node_B = N // 2
        
        # 2. Geometric Metric Calculation (d_geo)
        # Calculate geodesic distance constrained to the bulk manifold topology.
        # This represents the path integral contribution from the semiclassical metric.
        d_geo = nx.shortest_path_length(G, source=node_A, target=node_B)
        
        # 3. Topological Bridge Injection
        # Introduce a singular edge (u, v) representing the shared stabilizer generator K.
        # This edge bypasses the bulk coordinate chart.
        G.add_edge(node_A, node_B, type='stabilizer_bridge')
        
        # 4. Topological Metric Calculation (d_topo)
        # Calculate the information latency on the full causal graph G.
        d_topo = nx.shortest_path_length(G, source=node_A, target=node_B)
        
        # 5. Divergence Analysis
        # Compute the ratio of geometric separation to topological adjacency.
        ratio = d_geo / d_topo if d_topo > 0 else 0
        
        print(f"{N:<20} | {d_topo:<18} | {d_geo:<18} | {ratio:.1f}")

if __name__ == "__main__":
    verify_distance_gap()

import networkx as nx
import numpy as np

def verify_geodesic_emergence():
    print("--- INTEGRATION TEST: Geodesic Motion & Equivalence Principle ---")
    
    # 1. CONSTRUCT SPACETIME GRAPH (1+1D)
    # Dimensions: Time T=0 to T=20, Space X=0 to X=10
    G = nx.DiGraph()
    T_steps = 21
    X_width = 11
    
    # Define Gravity Well: "Slow" time (high density) in the center (x=5)
    # We assign "weights" to edges. Weight = Proper Time.
    # In vacuum (edges), weight = 1.0.
    # In gravity well, we add extra nodes/weight effectively making the path "longer" (more proper time).
    # Heuristic: Lapse N is low, so Proper Time (1/N) is high.
    
    def get_proper_time_weight(x):
        # Gaussian potential well at x=5
        dist = abs(x - 5)
        # Closer to mass = Higher Proper Time density (Gravitational Time Dilation)
        return 1.0 + 2.0 * np.exp(-dist**2 / 2.0)

    # Build Lattice
    for t in range(T_steps - 1):
        for x in range(X_width):
            u = (t, x)
            
            # Allow movement to x-1, x, x+1 (Light cones)
            for dx in [-1, 0, 1]:
                next_x = x + dx
                if 0 <= next_x < X_width:
                    v = (t + 1, next_x)
                    
                    # Edge Weight = Proper Time accumulated
                    # We average the proper time potential of start and end x
                    weight = (get_proper_time_weight(x) + get_proper_time_weight(next_x)) / 2.0
                    
                    # We negate weight because algorithms usually find SHORTEST path.
                    # We want LONGEST path (Maximal Proper Time).
                    # Bellman-Ford or negating weights works for DAGs.
                    G.add_edge(u, v, weight=-weight)

    # 2. VERIFY ACYCLICITY (Global Hyperbolicity)
    if not nx.is_directed_acyclic_graph(G):
        print("FAIL: Graph contains cycles (CTCs). Physics broken.")
        return
    else:
        print("PASS: Graph is Acyclic (Globally Hyperbolic).")

    # 3. COMPUTE GEODESIC (Path of Stationary Phase)
    # Particle starts at (0, 2) and ends at (20, 2).
    # Straight line path is x=2 -> x=2.
    # Geodesic should curve towards x=5 (the gravity well) to maximize proper time.
    start_node = (0, 2)
    end_node = (20, 2)
    
    # Use shortest path on negative weights = Longest Path (Max Proper Time)
    path = nx.shortest_path(G, source=start_node, target=end_node, weight='weight')
    
    # Extract trajectory
    trajectory = [p[1] for p in path]
    
    # 4. ANALYZE DEVIATION
    # Does it bend toward the mass (x=5)?
    max_deflection = max(trajectory)
    print(f"Start X: {trajectory[0]}")
    print(f"End X:   {trajectory[-1]}")
    print(f"Max X (Apex): {max_deflection}")
    print(f"Trajectory: {trajectory}")
    
    if max_deflection > 2:
        print("PASS: Geodesic Deviation Detected.")
        print("      Particle accelerated toward high-curvature region (Gravity).")
    else:
        print("FAIL: Particle followed Euclidean straight line. No Gravity detected.")

if __name__ == "__main__":
    verify_geodesic_emergence()

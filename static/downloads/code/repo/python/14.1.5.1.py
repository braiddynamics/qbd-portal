import networkx as nx
import numpy as np
from scipy.ndimage import gaussian_filter

def verify_time_foliation_integration():
    np.random.seed(42)
    print("--- Layered DAG ordering and inverse-depth smoothing ---")

    # 1. SETUP: 1+1D Spacetime Graph
    G = nx.DiGraph()
    width = 20
    steps = 30

    for t in range(steps):
        for x in range(width):
            u = (t, x)

            # The central columns have a higher chance of a two-edge route.
            density_prob = 0.8 if 8 <= x <= 12 else 0.1

            # Forward edges
            for dx in [-1, 0, 1]:
                nx_next = x + dx
                if 0 <= nx_next < width:
                    v = (t + 1, nx_next)
                    G.add_edge(u, v)

            # Add a route of length two to the next layer.
            if np.random.rand() < density_prob:
                m = f"delay_{t}_{x}_{np.random.randint(1000)}"
                G.add_edge(u, m)
                G.add_edge(m, (t+1, x)) # Reconnect to same spatial coord

    # 2. VERIFY: Global Monotonicity
    try:
        # Calculate Logical Depth (Longest Path) for every node
        depths = {}
        for n in nx.topological_sort(G):
            preds = list(G.predecessors(n))
            if not preds:
                depths[n] = 0.0
            else:
                depths[n] = max(depths[p] for p in preds) + 1.0

        print("PASS: Longest-path depth orders the synthetic DAG.")

    except nx.NetworkXUnfeasible:
        print("FAIL: The synthetic graph contains a directed cycle.")
        return

    # 3. Measure inverse depth increments between coordinate layers.

    raw_inverse_depth = np.zeros(width)
    samples = 0

    for t in range(steps - 1):
        for x in range(width):
            u = (t, x)
            v = (t + 1, x)

            if u in depths and v in depths:
                depth_increment = depths[v] - depths[u]

                inverse_depth = 1.0 / depth_increment
                raw_inverse_depth[x] += inverse_depth
        samples += 1

    # Average over time
    raw_inverse_depth /= samples

    # Add synthetic noise to test the filter.
    raw_inverse_depth += np.random.normal(0, 0.1, size=width)

    # Apply Smoothing
    smooth_inverse_depth = gaussian_filter(raw_inverse_depth, sigma=2.0)

    # Calculate Roughness (Sum of squared second derivatives)
    # Use diff twice to get Laplacian-like measure of "jaggedness"
    roughness_raw = np.sum(np.diff(raw_inverse_depth, 2)**2)
    roughness_smooth = np.sum(np.diff(smooth_inverse_depth, 2)**2)

    print(f"Roughness (Raw):      {roughness_raw:.4f}")
    print(f"Roughness (Smoothed): {roughness_smooth:.4f}")

    if roughness_smooth < roughness_raw * 0.2:
        print("PASS: Smoothing reduces inverse-depth roughness.")
    else:
        print("FAIL: Roughness reduction criterion not met.")

if __name__ == "__main__":
    verify_time_foliation_integration()

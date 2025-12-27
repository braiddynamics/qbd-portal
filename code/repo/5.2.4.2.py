import networkx as nx
import numpy as np
import random
from scipy.optimize import curve_fit

# 1. Deterministic Initialization
random.seed(42)
np.random.seed(42)

def count_open_paths(G):
    """
    Counts u -> v -> w ONLY if edge u-w does NOT exist.
    This filters out internal triangle paths to isolate the interaction term.
    """
    paths = 0
    nodes = list(G.nodes())
    for v in nodes:
        neighbors = list(G.neighbors(v))
        k = len(neighbors)
        if k < 2: continue
        
        # Check all neighbor pairs
        for i in range(k):
            for j in range(i + 1, k):
                u, w = neighbors[i], neighbors[j]
                
                # CRITICAL: Only count if the loop is NOT closed
                if not G.has_edge(u, w):
                    paths += 1
    return paths

# 2. Simulation Parameters
N = 1000
runs = 20
max_cycles = 150  

all_densities = []
all_paths = []

for _ in range(runs):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    
    current_densities = []
    current_paths = []
    
    for c in range(1, max_cycles + 1):
        triad = random.sample(range(N), 3)
        nx.add_cycle(G, triad)
        
        # Record Metrics
        if c > 10: # Ensure sufficient density for interaction
            rho = c / N
            path_density = count_open_paths(G) / N
            
            current_densities.append(rho)
            current_paths.append(path_density)
        
    all_densities.append(current_densities)
    all_paths.append(current_paths)

# 3. Aggregation and Fitting
mean_rho = np.mean(all_densities, axis=0)
mean_paths = np.mean(all_paths, axis=0)

def power_law(x, a, b):
    return a * (x**b)

popt, _ = curve_fit(power_law, mean_rho, mean_paths)
amplitude, exponent = popt

print(f"Sample Size (N): {N} | Runs: {runs}")
print(f"Measured Scaling Exponent: {exponent:.4f}")
print(f"Theoretical Expectation:   2.0000")
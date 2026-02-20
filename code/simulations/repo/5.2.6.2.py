import networkx as nx
import numpy as np
import random
from scipy.optimize import curve_fit

# Set seeds for reproducibility
random.seed(42)
np.random.seed(42)

def measure_deletion_flux(N, max_density_cycles=100):
    densities = []
    flux_rates = [] 
    
    # Simulation Rule: P_delete = P_base * (1 + lambda * local_density)
    lambda_sim = 0.5  # Catalytic coefficient (example value)
    
    for cycles in range(10, max_density_cycles, 5):
        # Create Graph
        G = nx.Graph()
        G.add_nodes_from(range(N))
        for _ in range(cycles):
            triad = random.sample(range(N), 3)
            nx.add_cycle(G, triad)
            
        rho = cycles / N
        
        # Measure Deletion Flux
        deleted_count = 0
        edges = list(G.edges())
        if not edges:
            continue
        
        for u, v in edges:
            # Local Stress Metric (Average Degree in Neighborhood)
            k_local = (G.degree[u] + G.degree[v]) / 4.0 
            p_base = 0.05
            p_stress = p_base * (lambda_sim * k_local)
            
            if random.random() < (p_base + p_stress):
                deleted_count += 1
        
        # Normalized Flux = Deleted / Total Edges
        normalized_flux = deleted_count / len(edges) 
        
        densities.append(rho)
        flux_rates.append(normalized_flux)
        
    return densities, flux_rates

# Simulation parameters
N = 500
densities, normalized_rates = measure_deletion_flux(N, max_density_cycles=500)

# Fit to linear model: Rate = A + B * rho
def linear_fit(x, a, b):
    return a + b * x

popt, pcov = curve_fit(linear_fit, densities, normalized_rates)
intercept, slope = popt
std_err_intercept, std_err_slope = np.sqrt(np.diag(pcov))

# Formatted console output
print(f"Base Rate (Intercept): {intercept:.4f} ± {std_err_intercept:.4f}")
print(f"Catalytic Coeff (Slope): {slope:.4f} ± {std_err_slope:.4f}")
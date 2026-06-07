import numpy as np
import networkx as nx
from scipy.optimize import curve_fit
from itertools import product
from scipy.sparse.linalg import expm_multiply
from scipy.sparse import eye, diags

def toy_4d_grid(N):
    k = int(round(N**(1/4)))
    if k**4 != N:
        raise ValueError("N must be k^4")
    dim = [k] * 4
    G = nx.grid_graph(dim=dim, periodic=True)
    mapping = {tuple(idx): i for i, idx in enumerate(product(range(k), repeat=4))}
    G = nx.relabel_nodes(G, mapping)
    return G

def graph_heat_kernel_trace(G, t, ell0):
    """
    Computes p_t(x,x) for a single node (trace/N due to symmetry).
    Uses unnormalized Laplacian L = D - A scaled by 1/ell0^2.
    """
    A = nx.adjacency_matrix(G).astype(float)
    degrees = np.array(A.sum(axis=1)).flatten()
    L = diags(degrees) - A
    
    # Scale time by metric factor
    # Heat equation: du/dt = -L u. 
    # If spatial dx = ell0, then L_physical ~ L_graph / ell0^2
    # So we compute exp(- t * L_graph / ell0^2)
    
    scaled_t = t / (ell0**2)
    
    N = G.number_of_nodes()
    # Compute action of exp(-tL) on basis vector e_0
    v0 = np.zeros(N); v0[0] = 1.0
    pt_x = expm_multiply(-scaled_t * L, v0)
    
    return pt_x[0]

print("--- Heat Kernel Asymptotics Verification ---")
print("Target Slope (d/2): -2.00")
print(f"{'N':<8} | {'ell_0':<8} | {'Slope':<10} | {'Eff. Dim':<10} | {'R^2':<10}")
print("-" * 60)

for N in [81, 256, 625]: # k=3, 4, 5
    G = toy_4d_grid(N)
    k = int(round(N**(1/4)))
    ell0 = 1.0/k
    
    # Probe times: small enough to be local, large enough to diffuse
    # range 0.01 to 0.1 in physical units
    times = np.logspace(-2.5, -1.0, 10) 
    
    probs = [graph_heat_kernel_trace(G, t, ell0) for t in times]
    
    # Fit power law p(t) ~ t^(-d/2) -> log p = (-d/2) log t + C
    log_t = np.log(times)
    log_p = np.log(probs)
    
    slope, intercept = np.polyfit(log_t, log_p, 1)
    
    # R^2
    residuals = log_p - (slope*log_t + intercept)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((log_p - np.mean(log_p))**2)
    r2 = 1 - (ss_res / ss_tot)
    
    d_eff = -2 * slope
    
    print(f"{N:<8} | {ell0:<8.4f} | {slope:<10.3f} | {d_eff:<10.2f} | {r2:<10.4f}")

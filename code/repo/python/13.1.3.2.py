import numpy as np
import networkx as nx
from scipy.sparse.linalg import eigsh
from scipy.sparse import diags
from itertools import product

def toy_4d_grid(N):
    """
    Constructs a periodic 4D grid graph (Torus) with N nodes.
    Ensures Ahlfors 4-regularity by construction.
    """
    k = int(round(N**(1/4)))
    if k**4 != N:
        raise ValueError(f"N={N} is not a perfect 4th power.")
    
    dim = [k] * 4
    G = nx.grid_graph(dim=dim, periodic=True)
    
    # Flatten node labels for matrix operations
    mapping = {tuple(idx): i for i, idx in enumerate(product(range(k), repeat=4))}
    G = nx.relabel_nodes(G, mapping)
    return G, 1.0/k  # Graph and fundamental scale ell_0

def compute_fiedler_value(G, ell0):
    """
    Computes the first non-zero eigenvalue of the Rescaled Laplacian.
    L_tilde = (1/ell0^2) * (D - A) [Unnormalized form matches grid geometry]
    """
    A = nx.adjacency_matrix(G).astype(float)
    degrees = np.array(A.sum(axis=1)).flatten()
    
    # Construct Unnormalized Laplacian L = D - A
    # We use unnormalized because on a regular grid D is constant (2d),
    # matching the standard finite difference Laplacian.
    L_unnorm = diags(degrees) - A
    
    # Apply Metric Scaling: 1 / ell_0^2
    factor = 1.0 / (ell0**2)
    L_scaled = factor * L_unnorm
    
    # Solve for k=6 smallest magnitude eigenvalues
    # Shift-invert mode would be faster, but SM with sort is robust here.
    try:
        vals = eigsh(L_scaled, k=6, which='SM', return_eigenvectors=False)
        vals = np.sort(vals)
        
        # Filter numerical zeros (machine precision)
        non_zeros = vals[vals > 1e-5]
        
        if len(non_zeros) > 0:
            return non_zeros[0] # The Fiedler value
        else:
            return 0.0
    except Exception as e:
        return np.nan

print("--- Spectral Convergence Verification (4D Torus) ---")
print("Target Continuum Eigenvalue: (2*pi)^2 ≈ 39.4784")
print(f"{'N':<8} | {'ell_0':<8} | {'Lambda_1':<10} | {'Theory':<10} | {'Error %':<10}")
print("-" * 60)

target = (2 * np.pi)**2 

for k in [4, 6, 8, 10]:
    N = k**4
    G, ell0 = toy_4d_grid(N)
    lam = compute_fiedler_value(G, ell0)
    err = abs(lam - target) / target * 100
    print(f"{N:<8} | {ell0:<8.4f} | {lam:<10.4f} | {target:<10.4f} | {err:<10.2f}")

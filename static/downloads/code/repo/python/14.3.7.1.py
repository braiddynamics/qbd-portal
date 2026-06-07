import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import inv

def verify_cluster_decomposition_integration():
    print("\n--- INTEGRATION TEST: Cluster Decomposition (Correlation Decay) ---")
    
    # 1. SETUP: spatial Graph (1D Chain for simplicity)
    # We simulate a massive scalar field on a discrete spatial slice.
    # The propagator G(x,y) is the inverse of the massive Laplacian (-D + m^2).
    L = 50
    m_mass = 0.5
    
    # Construct Discrete Laplacian (1D)
    # D_ij = 2 if i=j, -1 if |i-j|=1
    diag = 2.0 * np.ones(L)
    off_diag = -1.0 * np.ones(L-1)
    # Add mass term
    diag += m_mass**2
    
    matrix = sp.diags([diag, off_diag, off_diag], [0, 1, -1], format='csc')
    
    # 2. COMPUTE: Propagator (Correlation Function <phi(x)phi(y)>)
    # In Euclidean path integral, G = (Laplacian + m^2)^-1
    propagator = inv(matrix).toarray()
    
    # 3. VERIFY: Exponential Decay
    # We measure correlation from center (L/2) to edge
    center = L // 2
    correlations = propagator[center, center:]
    distances = np.arange(len(correlations))
    
    # Fit to C * exp(-x / xi)
    # Take log of correlations (ignoring small noise floor)
    valid_idx = correlations > 1e-5
    y_data = np.log(correlations[valid_idx])
    x_data = distances[valid_idx]
    
    # Linear regression on log plot
    slope, intercept = np.polyfit(x_data, y_data, 1)
    correlation_length = -1.0 / slope
    
    print(f"Mass Parameter: {m_mass}")
    print(f"Measured Correlation Length: {correlation_length:.4f}")
    
    # Check theoretical expectation: xi ~ 1/m (approx)
    # For discrete, xi = -1/ln(roots)... roughly 1/m for small m.
    
    print(f"Correlation at x=0:  {correlations[0]:.4f}")
    print(f"Correlation at x=10: {correlations[10]:.6f}")
    
    if correlations[10] < correlations[0] * 0.1:
        print("PASS: Correlations decay with distance (Cluster Decomposition).")
        print("      System supports local massive particles.")
    else:
        print("FAIL: Long-range correlations persist (Non-local/Gapless).")

if __name__ == "__main__":
    verify_cluster_decomposition_integration()

import numpy as np

def generate_bipartite_ladder_topology():
    """
    Constructs the adjacency matrix for a connected, bipartite ladder network.
    Perfect bipartite partitioning: V1 = {0, 2, 4} and V2 = {1, 3, 5}.
    """
    n = 6
    A = np.zeros((n, n), dtype=float)
    bipartite_edges = [
        (0, 1), (1, 2),  # Top leg
        (3, 4), (4, 5),  # Bottom leg
        (0, 3), (1, 4), (2, 5)  # Transverse rungs
    ]
    for u, v in bipartite_edges:
        A[u, v] = 1.0
        A[v, u] = 1.0
    return A

def analyze_adjacency_spectrum(A):
    """Isolates the principal and subdominant roots of the topology."""
    eigvals, eigvecs = np.linalg.eigh(A)
    principal_idx = np.argmax(eigvals)
    lambda_0 = eigvals[principal_idx]
    psi_0 = eigvecs[:, principal_idx]
    
    # Robust phase alignment resilient to floating-point numerical noise
    if psi_0[np.argmax(np.abs(psi_0))] < 0:
        psi_0 = -psi_0
        
    print("=== TOPOLOGICAL SPECTRAL ANALYSIS ===")
    print(f"Principal Eigenvalue (lambda_0)  : {lambda_0:.4f}")
    print(f"Subdominant Eigenvalue (-lambda_0): {eigvals[0]:.4f}")
    print(f"Perfect Spectral Symmetry Around 0: {np.allclose(np.sort(eigvals), -np.sort(eigvals)[::-1])}\n")
    return lambda_0, psi_0

def derive_merw_transition_kernel(A, lambda_0, psi_0):
    """Executes similarity transformation to build the MERW Markov operator (Vectorized)."""
    # Vectorized calculation: P_ij = (A_ij / lambda_0) * (psi_j / psi_i)
    P = (A / lambda_0) * (psi_0[np.newaxis, :] / psi_0[:, np.newaxis])
            
    eigvals_P = np.linalg.eigvals(P)
    print("=== TRANSLATED RANDOM WALK OPERATOR ===")
    print(f"Spectrum of Markov Operator P     : {np.round(np.sort(eigvals_P), 4)}")
    print(f"Sub-principal Eigenvalue (-1) Present: {np.any(np.isclose(eigvals_P, -1.0))}\n")
    return P

def execute_markov_trajectory_simulation(P, psi_0, timesteps=100):
    """Tracks state vector propagation over time to record the limit cycle."""
    n = P.shape[0]
    V1 = [0, 2, 4]
    
    pi_t = np.zeros(n, dtype=float)
    pi_t[0] = 1.0  # Localized point-mass initialization at Node 0 (in V1)
    
    print("=== DISCRETE-TIME POWER ITERATION SYSTEM ===")
    print(f"Initial Distribution state vector pi(0): {pi_t}")
    
    for t in range(1, timesteps + 1):
        pi_t = pi_t @ P
        if t == (timesteps - 1):
            print(f"Asymptotic Vector Profile pi({t}) [Odd Boundary] : {np.round(pi_t, 4)}")
        elif t == timesteps:
            print(f"Asymptotic Vector Profile pi({t}) [Even Boundary]: {np.round(pi_t, 4)}")
            
    # Calculate the theoretical limit cycle for even t (mass is 2*psi^2 on V1, 0 on V2)
    theoretical_even = np.zeros(n)
    theoretical_even[V1] = 2 * (psi_0[V1] ** 2)
    
    print("-" * 50)
    print(f"Theoretical Stationary Target (psi_0^2)  : {np.round(psi_0 ** 2, 4)}")
    print(f"Theoretical Limit Cycle (Even t)         : {np.round(theoretical_even, 4)}")
    
    # Demonstrate the "Aperiodic Modification" (Lazy Walk) mentioned in the paper's conclusion
    P_lazy = 0.5 * np.eye(n) + 0.5 * P
    pi_lazy = np.zeros(n)
    pi_lazy[0] = 1.0
    for _ in range(timesteps):
        pi_lazy = pi_lazy @ P_lazy
        
    print("\n=== LAZY WALK (APERIODIC MODIFICATION) ===")
    print(f"Lazy Walk Asymptotic Profile pi({timesteps}) : {np.round(pi_lazy, 4)}")
    print(f"Convergence to psi_0^2 recovered!          : {np.allclose(pi_lazy, psi_0**2, atol=1e-3)}")

if __name__ == "__main__":
    A = generate_bipartite_ladder_topology()
    l_0, p_0 = analyze_adjacency_spectrum(A)
    P_kernel = derive_merw_transition_kernel(A, l_0, p_0)
    execute_markov_trajectory_simulation(P_kernel, p_0)

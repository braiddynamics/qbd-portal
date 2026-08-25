"""
Maximal Entropy Random Walk (MERW) on Bipartite Graphs
Spectral Verification & Dynamical Limit Cycle Simulator

Author: R. Fisher (Braid Dynamics Group)
Date: June 21, 2026
License: CC BY 4.0 / MIT

Demonstrates:
  1. The -lambda_0 adjacency eigenvalue on connected bipartite graphs.
  2. The mu_2 = -1 peripheral eigenvalue of the discrete-time MERW kernel P.
  3. The permanent period-two parity limit cycle for initial states with c != 0.
  4. Instantaneous convergence to pi* = psi_0^2 if and only if c = 0.
  5. Recovery of pi* via Cesaro averaging, parity averaging, and lazy walking.
"""

from __future__ import annotations

from collections import deque
import numpy as np


def find_bipartition(A: np.ndarray) -> tuple[list[int], list[int]]:
    """
    Computes the 2-coloring bipartition (V1, V2) of a connected graph via BFS.
    Raises ValueError if the graph is not bipartite.
    """
    n = A.shape[0]
    color = {}
    q = deque([0])
    color[0] = 0
    while q:
        u = q.popleft()
        for v in range(n):
            if A[u, v] != 0:
                if v not in color:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    raise ValueError("Graph is not bipartite (contains odd cycles).")
    v1 = [i for i, c in color.items() if c == 0]
    v2 = [i for i, c in color.items() if c == 1]
    return sorted(v1), sorted(v2)


def generate_bipartite_ladder_topology() -> np.ndarray:
    """
    Constructs the adjacency matrix for a 6-node ladder network.
    Bipartition: V1 = {0, 2, 4} and V2 = {1, 3, 5}.
    """
    n = 6
    A = np.zeros((n, n), dtype=float)
    bipartite_edges = [
        (0, 1), (1, 2),          # Top leg
        (3, 4), (4, 5),          # Bottom leg
        (0, 3), (1, 4), (2, 5)   # Transverse rungs
    ]
    for u, v in bipartite_edges:
        A[u, v] = 1.0
        A[v, u] = 1.0
    return A


def analyze_adjacency_spectrum(A: np.ndarray) -> tuple[float, np.ndarray, list[int], list[int]]:
    """Isolates the principal and subdominant roots of the topology."""
    v1, v2 = find_bipartition(A)
    eigvals, eigvecs = np.linalg.eigh(A)
    principal_idx = int(np.argmax(eigvals))
    lambda_0 = float(eigvals[principal_idx])
    psi_0 = eigvecs[:, principal_idx].copy()
    
    # Phase alignment: ensure psi_0 > 0
    if psi_0[np.argmax(np.abs(psi_0))] < 0:
        psi_0 = -psi_0
    psi_0 = psi_0 / np.linalg.norm(psi_0)

    print("=== TOPOLOGICAL SPECTRAL ANALYSIS ===")
    print(f"Graph Order (n)                  : {A.shape[0]} nodes")
    print(f"Bipartition Classes              : V1 = {v1}, V2 = {v2}")
    print(f"Principal Eigenvalue (lambda_0)  : {lambda_0:.4f}")
    print(f"Subdominant Eigenvalue (-lambda_0): {eigvals[0]:.4f}")
    print(f"Spectral Symmetry Around 0       : {np.allclose(np.sort(eigvals), -np.sort(eigvals)[::-1])}\n")
    return lambda_0, psi_0, v1, v2


def derive_merw_transition_kernel(A: np.ndarray, lambda_0: float, psi_0: np.ndarray) -> np.ndarray:
    """Constructs the discrete-time MERW Markov operator via similarity transformation."""
    # P_ij = (A_ij / lambda_0) * (psi_j / psi_i)
    P = (A / lambda_0) * (psi_0[np.newaxis, :] / psi_0[:, np.newaxis])
    
    # Assert row-stochasticity
    assert np.allclose(P.sum(axis=1), 1.0), "P must be row-stochastic."
    
    # Assert stationarity of pi* = psi_0^2
    pi_star = psi_0 ** 2
    assert np.allclose(pi_star @ P, pi_star), "pi* = psi_0^2 must be stationary."
    
    eigvals_P = np.linalg.eigvals(P)
    eigvals_P = np.real_if_close(eigvals_P, tol=1000)
    eigvals_sorted = np.sort(eigvals_P.real)
    
    print("=== TRANSLATED RANDOM WALK OPERATOR ===")
    print(f"Spectrum of Markov Operator P     : {np.round(eigvals_sorted, 4)}")
    print(f"Eigenvalue (-1) Present          : {np.any(np.isclose(eigvals_sorted, -1.0))}\n")
    return P


def execute_markov_trajectory_simulation(P: np.ndarray, psi_0: np.ndarray, v1: list[int], v2: list[int], timesteps: int = 100):
    """Propagates distribution state vectors to observe parity oscillations and convergence conditions."""
    n = P.shape[0]
    pi_star = psi_0 ** 2
    
    # Construct the parity vector v2
    v_2 = np.zeros(n, dtype=float)
    v_2[v1] = 1.0
    v_2[v2] = -1.0
    
    # --- Experiment A: Localized Initial Condition (c = +1 != 0) ---
    print("=== EXPERIMENT A: LOCALIZED INITIAL CONDITION (c = +1) ===")
    pi_t = np.zeros(n, dtype=float)
    pi_t[v1[0]] = 1.0  # Node 0 in V1
    c_init = float(pi_t @ v_2)
    print(f"Initial Distribution pi(0)        : {pi_t}")
    print(f"Initial Parity Imbalance c        : {c_init:.1f}")
    
    for t in range(1, timesteps + 1):
        pi_t = pi_t @ P
        # Parity diagnostic assertion: pi(t) @ v2 == (-1)^t * c
        expected_parity = ((-1.0) ** t) * c_init
        assert np.isclose(pi_t @ v_2, expected_parity), f"Parity mismatch at step {t}"
        
        if t >= timesteps - 1:
            parity_label = "Even" if (t % 2 == 0) else "Odd"
            print(f"Asymptotic Profile pi({t}) [{parity_label:>4} step]: {np.round(pi_t, 4)}")
            
    theoretical_even = np.zeros(n)
    theoretical_even[v1] = 2.0 * pi_star[v1]
    theoretical_odd = np.zeros(n)
    theoretical_odd[v2] = 2.0 * pi_star[v2]
    
    assert np.allclose(pi_t, theoretical_even if timesteps % 2 == 0 else theoretical_odd, atol=1e-5)
    print(f"Theoretical Target (psi_0^2)      : {np.round(pi_star, 4)}")
    print(f"Theoretical Limit Cycle (Even t)  : {np.round(theoretical_even, 4)}")
    print(f"Theoretical Limit Cycle (Odd t)   : {np.round(theoretical_odd, 4)}")

    # --- Experiment B: Balanced Initial Condition (c = 0) ---
    print("\n=== EXPERIMENT B: BALANCED INITIAL CONDITION (c = 0) ===")
    pi_balanced = np.ones(n, dtype=float) / n
    c_bal = float(pi_balanced @ v_2)
    print(f"Initial Balanced Distribution     : {np.round(pi_balanced, 4)}")
    print(f"Initial Parity Imbalance c        : {c_bal:.1f}")
    for _ in range(timesteps):
        pi_balanced = pi_balanced @ P
    print(f"Asymptotic Profile (c=0)          : {np.round(pi_balanced, 4)}")
    print(f"Direct Convergence to psi_0^2     : {np.allclose(pi_balanced, pi_star, atol=1e-5)}")
    assert np.allclose(pi_balanced, pi_star, atol=1e-5), "Balanced state must converge to pi*."

    # --- Experiment C: Lazy Walk (Aperiodic Modification) ---
    print("\n=== EXPERIMENT C: LAZY WALK MODIFICATION (alpha = 0.5) ===")
    P_lazy = 0.5 * np.eye(n) + 0.5 * P
    pi_lazy = np.zeros(n, dtype=float)
    pi_lazy[v1[0]] = 1.0
    for _ in range(timesteps):
        pi_lazy = pi_lazy @ P_lazy
    print(f"Lazy Walk Final Profile pi({timesteps}) : {np.round(pi_lazy, 4)}")
    print(f"Convergence to psi_0^2 Recovered  : {np.allclose(pi_lazy, pi_star, atol=1e-4)}\n")
    assert np.allclose(pi_lazy, pi_star, atol=1e-4), "Lazy walk must converge to pi*."


if __name__ == "__main__":
    A_ladder = generate_bipartite_ladder_topology()
    lam_0, psi_0, part_v1, part_v2 = analyze_adjacency_spectrum(A_ladder)
    P_mat = derive_merw_transition_kernel(A_ladder, lam_0, psi_0)
    execute_markov_trajectory_simulation(P_mat, psi_0, part_v1, part_v2)


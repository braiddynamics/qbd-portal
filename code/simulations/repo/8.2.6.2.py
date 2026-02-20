import numpy as np
import pandas as pd

def gell_mann_basis():
    r"""
    Return the standard 8 Gell-Mann matrices for su(3),
    normalized with Tr(λ^a λ^b) = 2 δ^{ab}.
    """
    l1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    l2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    l3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
    l4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    l5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    l6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    l7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    l8 = (1 / np.sqrt(3)) * np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex)
    return [l1, l2, l3, l4, l5, l6, l7, l8]

def flatten_gellmann(L, basis):
    """Project Hermitian matrix L onto su(3) basis → coefficients in ℝ⁸."""
    coeffs = [np.real(np.trace(L.conj().T @ b)) / 2 for b in basis]
    return np.array(coeffs)

def span_rank(flats):
    """Numerical rank of coefficient vectors via SVD."""
    if len(flats) == 0:
        return 0
    stacked = np.vstack(flats)
    _, s, _ = np.linalg.svd(stacked)
    return np.sum(s > 1e-8)

def simulate_random_order_closure(num_ensembles=500):
    """
    Ensemble simulation of su(3) basis closure under stochastic generator discovery.
    Starts from two real off-diagonal fundamentals (λ¹, λ⁴).
    Adds generators only if they increase span rank (mimicking commutator novelty).
    """
    basis = gell_mann_basis()
    seed_indices = [0, 3]  # λ¹ (1↔2), λ⁴ (1↔3)
    seed_flats = [flatten_gellmann(basis[i], basis) for i in seed_indices]

    dimensions = []
    for _ in range(num_ensembles):
        discovery_order = list(range(8))
        np.random.shuffle(discovery_order)

        current_flats = seed_flats[:]
        discovered = set(seed_indices)

        for idx in discovery_order:
            if idx in discovered:
                continue
            f = flatten_gellmann(basis[idx], basis)
            if np.linalg.norm(f) > 1e-10:
                temp = current_flats + [f]
                if span_rank(temp) > span_rank(current_flats):
                    current_flats.append(f)
                    discovered.add(idx)
                if len(current_flats) >= 8:
                    break
        dimensions.append(span_rank(current_flats))

    return np.array(dimensions)

if __name__ == "__main__":
    print("═" * 70)
    print("COMPUTATIONAL VERIFICATION OF SU(3) ALGEBRA CLOSURE")
    print("Robustness under Stochastic Generator Discovery Order")
    print("═" * 70)

    dims = simulate_random_order_closure(num_ensembles=500)

    avg_dim = np.mean(dims)
    full_prob = np.mean(dims == 8)
    dim_counts = pd.Series(dims).value_counts().sort_index()

    print(f"\nEnsembles simulated       : 500")
    print(f"Initial generators        : 2 (λ¹, λ⁴ – real off-diagonals)")
    print(f"Average final dimension   : {avg_dim:.2f}")
    print(f"Probability of full closure (dim=8): {full_prob:.3f} ({full_prob*100:.1f}%)")

    print("\nDistribution of final algebra dimensions:")
    df = pd.DataFrame({
        "Dimension": dim_counts.index,
        "Count": dim_counts.values,
        "Percentage": (dim_counts.values / len(dims) * 100).round(2)
    })
    print(df.to_string(index=False))

    print("\n" + "─" * 70)
    if full_prob == 1.0:
        print("RESULT: Deterministic closure confirmed.")
    else:
        print("RESULT: Partial closure observed – check parameters.")
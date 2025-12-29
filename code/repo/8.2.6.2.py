import numpy as np

def gell_mann_basis():
    r"""
    Return the standard 8 Gell-Mann matrices for su(3), normalized with Tr(lambda^a lambda^b) = 2 delta^{ab}.
    These form the basis for the Lie algebra.
    """
    # lambda1
    l1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    # lambda2
    l2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    # lambda3
    l3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
    # lambda4
    l4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    # lambda5
    l5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    # lambda6
    l6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    # lambda7
    l7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    # lambda8
    l8 = (1 / np.sqrt(3)) * np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex)
    return [l1, l2, l3, l4, l5, l6, l7, l8]

def flatten_gellmann(L, basis):
    r"""
    Project the Hermitian matrix L onto the su(3) basis to get coefficients vector in R^8.
    Uses inner product <A,B> = Re Tr(A^\dagger B) / 2 for normalization Tr(lambda^a lambda^b) = 2 delta.
    """
    coeffs = [np.real(np.trace(L.conj().T @ b)) / 2 for b in basis]
    return np.array(coeffs)

def span_rank(flats):
    r"""
    Compute the numerical rank of the stacked coefficient vectors using SVD.
    Returns the dimension of the span in the 8D su(3) space.
    """
    if len(flats) == 0:
        return 0
    stacked = np.vstack(flats)
    _, s, _ = np.linalg.svd(stacked)
    return np.sum(s > 1e-8)  # Threshold for numerical stability

def simulate_random_order_closure(num_ensembles=100):
    r"""
    Simulate ensemble of 'braid rewrites' by randomly ordering the discovery of su(3) generators
    starting from 2 fundamentals (l1, l4 - real off-diagonals typical of initial swaps).
    Add generators if they increase the span rank, mimicking commutator generation.
    Returns average final dimension and probability of full closure (dim=8).
    """
    basis_mats = gell_mann_basis()
    # Start with real off-diagonal fundamentals: index 0=l1 (12), 3=l4 (13)
    seed_indices = [0, 3]
    seed_mats = [basis_mats[i] for i in seed_indices]
    results = []
    for ensemble in range(num_ensembles):
        # Shuffle the order in which 'new' generators are 'discovered' (simulating random commutators)
        discovery_order = list(range(8))
        np.random.shuffle(discovery_order)
        current_flats = [flatten_gellmann(H, basis_mats) for H in seed_mats]
        discovered = set(seed_indices)
        for idx in discovery_order:
            if idx in discovered:
                continue
            H = basis_mats[idx]
            f = flatten_gellmann(H, basis_mats)
            if np.linalg.norm(f) > 1e-10:  # Non-zero
                temp_flats = current_flats + [f]
                if span_rank(temp_flats) > span_rank(current_flats):
                    current_flats.append(f)
                    discovered.add(idx)
                if len(current_flats) >= 8:
                    break
        dim = span_rank(current_flats)
        results.append(dim)
    avg_dim = np.mean(results)
    full_prob = np.mean(np.array(results) == 8)
    return avg_dim, full_prob, results

# Run the simulation
if __name__ == "__main__":
    avg, prob, results = simulate_random_order_closure(num_ensembles=100)
    print(f"Average span dimension across ensembles: {avg:.1f}")
    print(f"Probability of full closure (dim=8): {prob:.3f}")
    print(f"Final dimensions sample: {results[:10]}")  # First 10 for inspection
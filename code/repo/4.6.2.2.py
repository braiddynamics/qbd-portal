import numpy as np

# Scenario:
# Branch 1 (G1): Add C->A (Cost: 1.0)
# Branch 2 (G2): Add D->B (Cost: 1.0)
# Branch 3 (G3): Both Adds + Del C->D (Cost: 1.0 * 1.0 * 0.5 = 0.5)

def born_product(n_add, n_del, P_add=1.0, P_del=0.5):
    """Calculates raw thermodynamic weight of a transition path."""
    return (P_add ** n_add) * (P_del ** n_del)

# 1. Calculate Raw Weights (assuming chi=1 for vacuum)
W_G1 = born_product(n_add=1, n_del=0)
W_G2 = born_product(n_add=1, n_del=0)
W_G3 = born_product(n_add=2, n_del=1) # Note: Multi-event path

# 2. Normalize over the ensemble of valid outcomes
total_weight = W_G1 + W_G2 + W_G3
P_G1 = W_G1 / total_weight
P_G3 = W_G3 / total_weight

# 3. Verify the 1/2 Ratio
expected_ratio = 0.5
ratio = P_G3 / P_G1

assert np.isclose(P_G1, 1.0/2.5), "G1 norm mismatch"
assert np.isclose(P_G3, 0.5/2.5), "G3 norm mismatch"

print(f"Raw Weights: G1={W_G1}, G3={W_G3}")
print(f"Norm Probs:  G1={P_G1:.3f}, G3={P_G3:.3f}")
print(f"Ratio P(G3)/P(G1): {ratio:.2f} (Target: {expected_ratio})")
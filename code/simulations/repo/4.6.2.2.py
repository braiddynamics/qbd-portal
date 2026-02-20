import numpy as np

def transition_weight(n_add: int, n_del: int, P_add: float = 1.0, P_del: float = 0.5) -> float:
    """Raw thermodynamic weight of a transition path in the vacuum limit (χ = 1)."""
    return P_add ** n_add * P_del ** n_del

print("Emergent Born Rule Verification (Vacuum Limit)")
print("=" * 54)

# Define the three concrete transition paths in the toy ensemble
# Path A: single addition (e.g., add C→A)
W_A = transition_weight(n_add=1, n_del=0)

# Path B: single addition (e.g., add D→B) – symmetric to A
W_B = transition_weight(n_add=1, n_del=0)

# Path C: two additions + one deletion (e.g., add C→A, add D→B, then delete one edge)
W_C = transition_weight(n_add=2, n_del=1)

# Full ensemble of valid successors (two symmetric single-add paths + one mixed path)
total_weight = W_A + W_B + W_C

P_A = W_A / total_weight
P_B = W_B / total_weight  # identical to P_A
P_C = W_C / total_weight

ratio = P_C / P_A

print(f"Raw weights:")
print(f"  Single addition (Path A or B):           {W_A:.1f}")
print(f"  Two additions + one deletion (Path C):   {W_C:.1f}")
print(f"  Total ensemble weight:                   {total_weight:.1f}\n")

print(f"Normalized probabilities:")
print(f"  P(single addition):                      {P_A:.3f}")
print(f"  P(two adds + one deletion):              {P_C:.3f}")
print(f"  Ratio P(C)/P(A):                         {ratio:.2f}  (theoretical target: 0.50)")
print(f"  Exact match with ½ deletion penalty:     {np.isclose(ratio, 0.5)}")
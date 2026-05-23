import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

def h_balanced(alpha):
    """
    Computes allocation entropy h(α) for balanced degrees (d=1).
    Returns -inf at boundaries to enforce strict (0,1) domain.
    """
    if alpha <= 1e-9 or alpha >= (1 - 1e-9):
        return -np.inf
    beta = (1.0 - alpha) / 2.0
    return -alpha * np.log(alpha) - 2 * beta * np.log(beta)

def h_prime_analytical(alpha):
    """
    Computes the exact first derivative h'(α) = log(β/α).
    """
    beta = (1.0 - alpha) / 2.0
    return np.log(beta / alpha)

def h_double_prime_analytical(alpha):
    """
    Computes the exact second derivative h''(α).
    """
    return -1.0 / (1.0 - alpha) - 1.0 / alpha

def h_unbalanced(alpha, d_plus=1.0, d_minus=1.0):
    """
    Computes total entropy for unbalanced neighborhood sizes.
    """
    if alpha <= 1e-9 or alpha >= (1 - 1e-9):
        return -np.inf
    beta = (1.0 - alpha) / 2.0
    term_self = -alpha * np.log(alpha)
    term_future = -beta * np.log(beta / d_plus)
    term_past = -beta * np.log(beta / d_minus)
    return term_self + term_future + term_past

# 1. Optimization for Balanced Case
res = minimize_scalar(lambda a: -h_balanced(a), 
                      bounds=(0.01, 0.99), 
                      method='bounded', 
                      options={'xatol': 1e-12})
max_alpha = res.x
max_entropy = -res.fun

# 2. Derivative Checks at Theoretical Critical Point
alpha_theory = 1.0/3.0
val_h_prime = h_prime_analytical(alpha_theory)
val_h_double_prime = h_double_prime_analytical(alpha_theory)

# Check against Machine Epsilon to prove 0.0
machine_epsilon = np.finfo(float).eps
is_zero_within_precision = abs(val_h_prime) <= machine_epsilon

# 3. Sensitivity Check
res_sparse = minimize_scalar(lambda a: -h_unbalanced(a, d_plus=1.0, d_minus=0.087), 
                             bounds=(0.01, 0.99), 
                             method='bounded',
                             options={'xatol': 1e-12})
max_alpha_sparse = res_sparse.x

# --- Console Output ---
print(f"--- Balanced Case (d=1) ---")
print(f"Numerical Max α:    {max_alpha:.8f}")
print(f"Max Entropy h(α):   {max_entropy:.8f} (Theoretical log(3) ≈ 1.0986)")
print(f"h'(1/3) Residual:   {val_h_prime:.4e}")
print(f"  > Valid Zero?     {is_zero_within_precision} (Residual <= Machine Epsilon {machine_epsilon:.2e})")
print(f"h''(1/3):           {val_h_double_prime:.4f} (Expected: -4.5)")
print(f"\n--- Unbalanced Sensitivity ---")
print(f"Sparse Max α (d-=0.087): {max_alpha_sparse:.4f}")

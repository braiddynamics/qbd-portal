import numpy as np
from scipy.optimize import brentq

# --- 1. PRECISE PHYSICAL CONSTANTS ---
# Λ: Vacuum Permittivity (Lemma 5.2.3)
LAMBDA_VAC = 0.0156

# μ: Friction Coefficient (Theorem 4.4.6 - Gaussian Normalization)
MU = 1.0 / np.sqrt(2 * np.pi)  # ≈ 0.3989

# λ_cat: Catalysis Coefficient (Theorem 4.4.5 - Entropic Release)
LAMBDA_CAT = np.e - 1          # ≈ 1.7182

def master_equation(rho):
    """
    The Fundamental Equation of Geometrogenesis:
    dρ/dt = J_in(ρ) - J_out(ρ)
    
    J_in  = (Λ + 9ρ²) * exp(-6μρ)
    J_out = 0.5ρ + 3λ_catρ²
    """
    if rho < 0: return LAMBDA_VAC
    
    # Creation Flux: Autocatalysis dampened by Gaussian Friction
    # The factor 6μ arises from the coordination number (Z=6) in 2D packing.
    creation = (LAMBDA_VAC + 9 * rho**2) * np.exp(-6 * MU * rho)
    
    # Deletion Flux: Linear Decay + Entropic Catalysis
    deletion = 0.5 * rho + 3 * LAMBDA_CAT * rho**2
    
    return creation - deletion

# --- 2. SOLVER (Vacuum State) ---
# We verify the existence of the stable vacuum foam.
try:
    rho_star = brentq(master_equation, 0.001, 0.1)
except ValueError:
    rho_star = 0.0
    print("WARNING: System Unstable (Auto-Ignition)")

# --- 3. STABILITY & FLUX ANALYSIS ---
# Calculate components at the exact equilibrium
J_in = (LAMBDA_VAC + 9 * rho_star**2) * np.exp(-6 * MU * rho_star)
J_out = 0.5 * rho_star + 3 * LAMBDA_CAT * rho_star**2

# Analytical Jacobian for Stability Verification
# d/dρ (Creation - Deletion)
d_creation = (18 * rho_star - 6 * MU * (LAMBDA_VAC + 9 * rho_star**2)) * np.exp(-6 * MU * rho_star)
d_deletion = 0.5 + 6 * LAMBDA_CAT * rho_star
jacobian = d_creation - d_deletion

# --- 4. OUTPUT ---
print(f"--- QBD MASTER EQUATION VERIFICATION ---")
print(f"CONSTANTS: Λ={LAMBDA_VAC} | μ=1/√2π | λ_cat=e-1")
print("-" * 40)
print(f"Equilibrium State (ρ*): {rho_star:.6f}")
print("-" * 40)
print(f"Flux Balance Check:")
print(f"  Creation (J_in):      {J_in:.6f}")
print(f"  Deletion (J_out):     {J_out:.6f}")
print(f"  Net Residual:         {master_equation(rho_star):.2e}")
print("-" * 40)
print(f"Stability Analysis:")
print(f"  Gradient (J):         {jacobian:.4f}")
print(f"  Status:               {'STABLE (Attractor)' if jacobian < 0 else 'UNSTABLE'}")
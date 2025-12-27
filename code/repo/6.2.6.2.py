import numpy as np
import pandas as pd

def simulate_entropic_exclusion():
    """
    Calculates the relative abundance of higher-order braids (n > 3)
    based on the Boltzmann suppression of their topological complexity.
    """
    
    # 1. Physical Constants
    # T_vac = ln(2) approx 0.693. This is the critical temperature derived in Ch 5.
    T_VAC = np.log(2) 
    
    # 2. Define Candidates (Ribbon Counts)
    # We analyze n=3 (Standard Model) vs n=4..8 (Exotics)
    n_values = np.array([3, 4, 5, 6, 7, 8])
    
    # 3. Define Complexity Cost Function C(n)
    # The Minimal Generation Principle asserts that C scales with n.
    # We assume the most charitable case for exotics: Linear Scaling C = n.
    # (If scaling is quadratic, suppression is even stronger).
    complexity = n_values.astype(float)
    
    # 4. Calculate Boltzmann Weights
    # P(n) ~ exp(-Complexity / T_vac)
    weights = np.exp(-complexity / T_VAC)
    
    # 5. Normalize Relative to the Ground State (n=3)
    base_weight = weights[0] 
    relative_abundance = weights / base_weight
    
    # 6. Inverse Ratio (Suppression Factor)
    suppression_factor = 1.0 / relative_abundance

    # --- Output Data ---
    df = pd.DataFrame({
        'Ribbons (n)': n_values,
        'Relative Abundance': relative_abundance,
        'Suppression (1 in X)': suppression_factor
    })
    
    print("--- ENTROPIC EXCLUSION SWEEP ---")
    print(f"Vacuum Temperature: {T_VAC:.4f} (ln 2)")
    print("\nResults:")
    print(df.to_string(index=False))

if __name__ == "__main__":
    simulate_entropic_exclusion()
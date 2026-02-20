import numpy as np
import pandas as pd

def simulate_entropic_exclusion():
    """
    Computes thermodynamic suppression of higher-order braids (n > 3)
    relative to tripartite ground state (n=3).
    
    Continuous Boltzmann model: ΔC = 1 nat per ribbon, T = ln 2.
    """
    print("═" * 70)
    print("ENTROPIC SUPPRESSION OF EXOTIC BRAIDS")
    print("Boltzmann Weights vs. Ribbon Count (n)")
    print("═" * 70)
    
    T_vac = np.log(2)                                 # ≈ 0.693147
    suppression_per_ribbon = np.exp(-1 / T_vac)        # ≈ 0.236928
    
    n_values = np.arange(3, 9)
    relative = suppression_per_ribbon ** (n_values - 3)
    suppression_factor = 1 / relative
    
    df = pd.DataFrame({
        'Ribbon count (n)'      : n_values,
        'Relative probability'  : [f"{r:.6f}" for r in relative],
        'Suppression factor'    : [f"{s:.1f}" for s in suppression_factor]
    })
    
    print(f"\nVacuum temperature T = ln 2 ≈ {T_vac:.6f}")
    print(f"Cost per ribbon ΔC = 1 nat")
    print(f"Suppression per ribbon ≈ {suppression_per_ribbon:.6f}")
    print("\nResults (normalized to n=3):")
    print(df.to_string(index=False))

if __name__ == "__main__":
    simulate_entropic_exclusion()
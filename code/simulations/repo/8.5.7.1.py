import math

def verify_gauge_coupling_consistency():
    print("--- QBD Gauge Coupling (g) Consistency Check ---")
    
    # 1. Fundamental Constants (Derived in Ch 4, 5, 8)
    
    # Topological Energy Scale (Alpha_topo)
    # Source: §4.4.2 (Bit-Nat Equivalence / 4 Dimensions)
    # Value: ln(2) / 4
    ALPHA_TOPO = math.log(2) / 4 
    
    # Local State Space Multiplier (M)
    # Source: §8.5.6 (Lemma: su2_local_dof_counting)
    # Derivation: 3 (Cycle Orientations) * 2 (Doublet States) + 1 (Spin Stabilizer)
    M_SU2 = 7 
    
    # Equilibrium Equilibrium Vacuum Density (Rho*)
    # Source: §5.3 (Parameter Sweep Results)
    # Mean density of the Region of Physical Viability (RPV)
    RHO_MEAN = 0.0290 
    
    # Ensemble Scatter (Standard Deviation)
    # Source: §5.3 (Fluctuations across 100 runs)
    # This represents the natural variance of the vacuum.
    RHO_SIGMA = 0.0050 

    # ---------------------------------------------------------
    # 2. Experimental Benchmark
    # Source: Particle Data Group (PDG)
    G_EXP_PDG = 0.6530

    # ---------------------------------------------------------
    # 3. Calculation Function
    # Formula: g = sqrt( 4 * pi * alpha * M * rho )
    def calculate_g(rho_val):
        prefactor = 4 * math.pi
        return math.sqrt(prefactor * ALPHA_TOPO * M_SU2 * rho_val)

    # ---------------------------------------------------------
    # 4. Perform Verification
    
    g_predicted_mean = calculate_g(RHO_MEAN)
    
    # Calculate bounds based on vacuum fluctuations (+/- 1 sigma)
    g_lower_bound = calculate_g(RHO_MEAN - RHO_SIGMA)
    g_upper_bound = calculate_g(RHO_MEAN + RHO_SIGMA)
    
    # Calculate relative error of the mean
    rel_error = abs(g_predicted_mean - G_EXP_PDG) / G_EXP_PDG * 100

    # ---------------------------------------------------------
    # 5. Output Results
    
    print(f"{'METRIC':<25} | {'VALUE':<10} | {'NOTES':<20}")
    print("-" * 65)
    print(f"{'Alpha_topo':<25} | {ALPHA_TOPO:.4f}     | {'ln(2)/4'}")
    print(f"{'Multiplier (M)':<25} | {M_SU2}          | {'SU(2) DoF'}")
    print(f"{'Equilibrium Density (rho)':<25} | {RHO_MEAN:.4f}     | {'+/- 0.0050'}")
    print("-" * 65)
    print(f"{'Predicted g (Mean)':<25} | {g_predicted_mean:.4f}     | {'Source: Thm 8.5.1'}")
    print(f"{'Experimental g (PDG)':<25} | {G_EXP_PDG:.4f}     | {'Benchmark'}")
    print(f"{'Relative Error':<25} | {rel_error:.2f}%      | {'< 2% Target'}")
    print("-" * 65)
    print(f"{'Vacuum Confidence Interval (1-sigma)':<35}")
    print(f"Lower Bound (rho - sigma): g = {g_lower_bound:.4f}")
    print(f"Upper Bound (rho + sigma): g = {g_upper_bound:.4f}")
    
    # Check if experiment is within theory bounds
    is_consistent = g_lower_bound <= G_EXP_PDG <= g_upper_bound
    
    print("-" * 65)
    if is_consistent:
        print("PASS: Experimental value falls within the natural vacuum fluctuation range.")
    else:
        print("FAIL: Experimental value lies outside the 1-sigma fluctuation range.")

if __name__ == "__main__":
    verify_gauge_coupling_consistency()
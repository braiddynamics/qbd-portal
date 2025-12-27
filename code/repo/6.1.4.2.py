import numpy as np

def simulate_cluster_decay():
    """
    Simulates the time-evolution of local particle clusters under 
    the rigorous Fundamental Equation of Geometrogenesis.
    
    Dynamical Law: dρ/dt = (Λ + 9ρ²)*exp(-6μρ) - (0.5ρ + 3λρ²)
    """
    
    print("--- SIMULATION: DECAY OF THE UNKNOT ---")
    
    # --- 1. PRECISE PHYSICAL CONSTANTS (Ch 5) ---
    LAMBDA_VAC = 0.0156               # Vacuum Permittivity
    MU         = 1.0 / np.sqrt(2 * np.pi)  # Friction ≈ 0.3989
    LAMBDA_CAT = np.e - 1             # Catalysis ≈ 1.7183
    
    # Vacuum Equilibrium (Fixed Point)
    RHO_STAR   = 0.037               # Approx solution from Ch 5
    
    # Simulation Settings
    # Increased duration to ensure convergence from high density
    TICKS = 600
    DT    = 0.1
    
    # --- 2. INITIAL CONDITIONS ---
    # Start as a high-density fluctuation (High Stress)
    initial_rho = 0.50
    
    time = np.arange(0, TICKS * DT, DT)
    rho_trivial = np.zeros_like(time)
    rho_knotted = np.zeros_like(time)
    
    rho_trivial[0] = initial_rho
    rho_knotted[0] = initial_rho
    
    # --- 3. DYNAMICS ENGINE ---
    
    def get_fluxes(rho):
        """Calculates J_in and J_out based on the Master Equation."""
        # Creation: Autocatalysis dampened by Gaussian Friction
        j_in = (LAMBDA_VAC + 9 * rho**2) * np.exp(-6 * MU * rho)
        
        # Deletion: Linear Decay + Quadratic Catalytic Stress
        j_out = 0.5 * rho + 3 * LAMBDA_CAT * rho**2
        
        return j_in, j_out

    # Knot Core Density (Mass of the Particle)
    # The density below which the knot cannot be untied locally.
    RHO_CORE = 0.082

    for i in range(1, len(time)):
        
        # --- A. Trivial Cluster (Unprotected) ---
        r_t = rho_trivial[i-1]
        jin_t, jout_t = get_fluxes(r_t)
        
        # Trivial clusters feel the full force of deletion
        d_rho_t = jin_t - jout_t
        
        # Update (prevent going below vacuum floor)
        rho_trivial[i] = max(RHO_STAR, r_t + d_rho_t * DT)
        
        
        # --- B. Prime Knot (Protected) ---
        r_k = rho_knotted[i-1]
        jin_k, jout_k = get_fluxes(r_k)
        
        # Topological Barrier Logic:
        # If density > Core, the "fuzz" evaporates normally.
        # If density <= Core, the Knot Barrier activates (Deletion -> 0).
        if r_k <= RHO_CORE:
            jout_k = 0.0  # The Lock
            
        d_rho_k = jin_k - jout_k
        
        # Update (prevent going below vacuum floor)
        rho_knotted[i] = max(RHO_STAR, r_k + d_rho_k * DT)

    # --- 4. OUTPUT RESULTS ---
    print(f"Physical Parameters: Λ={LAMBDA_VAC} | μ={MU:.4f} | λ={LAMBDA_CAT:.4f}")
    print(f"Initial Density:     {initial_rho:.2f}")
    print("-" * 40)
    print(f"Final Trivial Density: {rho_trivial[-1]:.4f} (Vacuum State)")
    print(f"Final Knotted Density: {rho_knotted[-1]:.4f} (Stable Particle)")
    print("-" * 40)
    
    # Verification of Flux at Initial State
    j_in_0, j_out_0 = get_fluxes(initial_rho)
    print(f"Initial Flux Balance (ρ={initial_rho}):")
    print(f"  J_in:  {j_in_0:.3f}")
    print(f"  J_out: {j_out_0:.3f}")
    print(f"  Net:   {j_in_0 - j_out_0:.3f} (Strong Decay)")

if __name__ == "__main__":
    simulate_cluster_decay()
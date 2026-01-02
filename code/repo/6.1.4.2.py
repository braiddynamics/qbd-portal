import numpy as np

def simulate_cluster_decay():
    """
    Simulates the thermodynamic fate of a high-density excitation under the
    Fundamental Equation of Geometrogenesis.
    
    Compares:
    - Trivial (reducible) cluster: Fully exposed to deletion flux.
    - Prime knot: Protected by topological barrier below core density.
    
    Demonstrates architectural stability of non-trivial topology.
    """
    
    print("═" * 60)
    print("SIMULATION: TOPOLOGICAL STABILITY OF PARTICLES")
    print("Trivial Cluster vs. Prime Knot under Vacuum Deletion Flux")
    print("═" * 60)
    
    # ── Physical Constants (Derived in Chapter 5) ─────────────────────
    Λ_vac     = 0.0156                          # Vacuum Permittivity
    μ         = 1.0 / np.sqrt(2 * np.pi)        # Friction Coefficient ≈ 0.398942
    λ_cat     = np.e - 1                        # Catalysis Coefficient ≈ 1.718282
    
    ρ_star    = 0.0370                          # Equilibrium vacuum density
    ρ_core    = 0.0820                          # Knot core threshold (topological lock)
    
    # ── Simulation Parameters ────────────────────────────────────────
    initial_ρ = 0.50                            # High-stress fluctuation
    dt        = 0.10                            # Time step
    n_steps   = 600                             # Total steps (ensures convergence)
    
    time = np.arange(0, n_steps * dt, dt)
    
    # ── State Initialization ─────────────────────────────────────────
    ρ_trivial = np.zeros_like(time)
    ρ_knotted = np.zeros_like(time)
    
    ρ_trivial[0] = initial_ρ
    ρ_knotted[0] = initial_ρ
    
    # ── Flux Calculation Helper ──────────────────────────────────────
    def fluxes(ρ):
        j_in  = (Λ_vac + 9 * ρ**2) * np.exp(-6 * μ * ρ)
        j_out = 0.5 * ρ + 3 * λ_cat * ρ**2
        return j_in, j_out
    
    # ── Time Evolution Loop ──────────────────────────────────────────
    for i in range(1, len(time)):
        # Trivial cluster: Full exposure
        j_in_t, j_out_t = fluxes(ρ_trivial[i-1])
        dρ_t = j_in_t - j_out_t
        ρ_trivial[i] = max(ρ_star, ρ_trivial[i-1] + dρ_t * dt)
        
        # Prime knot: Deletion suppressed below core
        j_in_k, j_out_k = fluxes(ρ_knotted[i-1])
        if ρ_knotted[i-1] <= ρ_core:
            j_out_k = 0.0  # Topological barrier activates
        dρ_k = j_in_k - j_out_k
        ρ_knotted[i] = max(ρ_star, ρ_knotted[i-1] + dρ_k * dt)
    
    # ── Results Output ───────────────────────────────────────────────
    print(f"\nPhysical Parameters:")
    print(f"  Vacuum Drive (Λ)      : {Λ_vac:.4f}")
    print(f"  Friction (μ)          : {μ:.6f}")
    print(f"  Catalysis (λ_cat)     : {λ_cat:.6f}")
    print(f"  Equilibrium Density   : {ρ_star:.4f}")
    print(f"  Knot Core Threshold   : {ρ_core:.4f}")
    print(f"\nInitial Local Density   : {initial_ρ:.2f}")
    print("-" * 60)
    print(f"Final States after {n_steps} steps:")
    print(f"  Trivial Cluster       : {ρ_trivial[-1]:.6f} → Vacuum Equilibrium")
    print(f"  Prime Knot            : {ρ_knotted[-1]:.6f} → Stable Particle")
    print("-" * 60)
    
    # Initial flux balance verification
    j_in_0, j_out_0 = fluxes(initial_ρ)
    print(f"Initial Flux Balance (ρ = {initial_ρ}):")
    print(f"  Creation  J_in  : {j_in_0:.4f}")
    print(f"  Deletion  J_out : {j_out_0:.4f}")
    print(f"  Net Rate dρ/dt  : {j_in_0 - j_out_0:+.4f} (Strong Decay)")
if __name__ == "__main__":
    simulate_cluster_decay()
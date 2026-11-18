import numpy as np

def simulate_cluster_decay():
    """
    Simulates the thermodynamic fate of a high-density excitation under the
    Fundamental Equation of Geometrogenesis.
    
    Compares:
    - Trivial (reducible) cluster: Fully exposed to deletion flux.
    - Prime knot: Continuous barrier suppression of deletion at and below core density.
    
    Demonstrates convergence of the knotted cluster to an analytic zero.
    """
    
    print("SIMULATION: TOPOLOGICAL STABILITY OF PARTICLES")
    print("Trivial Cluster vs. Prime Knot under Vacuum Deletion Flux")
    print("=" * 60)
    
    # ── Physical Constants (Derived in Chapter 5) ─────────────────────
    Λ_vac     = 2.0 ** (-6)                     # Vacuum Permittivity = 0.015625
    μ         = 1.0 / np.sqrt(2 * np.pi)        # Friction Coefficient ≈ 0.398942
    λ_cat     = np.e - 1                        # Catalysis Coefficient ≈ 1.718282
    
    ρ_star    = 0.037061                        # Equilibrium vacuum density
    ρ_core    = 0.082000                        # Knot core threshold (topological lock)
    δ_core    = 0.010000                        # Continuous barrier transition width
    
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
    
    # ── Flux Calculation Helpers ─────────────────────────────────────
    def fluxes(ρ):
        j_in  = (Λ_vac + 9 * ρ**2) * np.exp(-6 * μ * ρ)
        j_out = 0.5 * ρ + 3 * λ_cat * ρ**2
        return j_in, j_out
    
    def barrier_suppression(ρ):
        # Continuous core-protection ramp: 0 for ρ <= ρ_core, rising to 1 over width δ_core
        return float(np.clip((ρ - ρ_core) / δ_core, 0.0, 1.0))
    
    # Locate analytic fixed points of F(ρ) and F_knot(ρ) = J_in(ρ) - s(ρ) * J_out(ρ)
    lo_t, hi_t = 0.0, 0.10
    for _ in range(80):
        mid = 0.5 * (lo_t + hi_t)
        j_in_m, j_out_m = fluxes(mid)
        if j_in_m - j_out_m > 0.0:
            lo_t = mid
        else:
            hi_t = mid
    ρ_trivial_star = 0.5 * (lo_t + hi_t)
    
    lo_k, hi_k = ρ_core, ρ_core + δ_core
    for _ in range(80):
        mid = 0.5 * (lo_k + hi_k)
        j_in_m, j_out_m = fluxes(mid)
        if j_in_m - barrier_suppression(mid) * j_out_m > 0.0:
            lo_k = mid
        else:
            hi_k = mid
    ρ_knot_star = 0.5 * (lo_k + hi_k)
    
    # ── Time Evolution Loop ──────────────────────────────────────────
    for i in range(1, len(time)):
        # Trivial cluster: Full exposure
        j_in_t, j_out_t = fluxes(ρ_trivial[i-1])
        dρ_t = j_in_t - j_out_t
        ρ_trivial[i] = max(ρ_star, ρ_trivial[i-1] + dρ_t * dt)
        
        # Prime knot: Continuous barrier suppression of deletion
        j_in_k, j_out_k = fluxes(ρ_knotted[i-1])
        s_k = barrier_suppression(ρ_knotted[i-1])
        dρ_k = j_in_k - s_k * j_out_k
        ρ_knotted[i] = max(ρ_star, ρ_knotted[i-1] + dρ_k * dt)
    
    # ── Results Output ───────────────────────────────────────────────
    print(f"\nPhysical Parameters:")
    print(f"  Vacuum Drive (Λ)      : {Λ_vac:.6f}")
    print(f"  Friction (μ)          : {μ:.6f}")
    print(f"  Catalysis (λ_cat)     : {λ_cat:.6f}")
    print(f"  Equilibrium Density   : {ρ_trivial_star:.6f}")
    print(f"  Knot Core Threshold   : {ρ_core:.6f}")
    print(f"  Barrier Width (δ)     : {δ_core:.6f}")
    print(f"  Knotted Analytic Zero : {ρ_knot_star:.6f}")
    print(f"\nInitial Local Density   : {initial_ρ:.2f}")
    print("-" * 60)
    print(f"Final States after {n_steps} steps:")
    print(f"  Trivial Cluster       : {ρ_trivial[-1]:.6f} (|Δρ| = {abs(ρ_trivial[-1] - ρ_trivial[-2]):.2e})")
    print(f"  Prime Knot            : {ρ_knotted[-1]:.6f} (|Δρ| = {abs(ρ_knotted[-1] - ρ_knotted[-2]):.2e})")
    print("-" * 60)
    
    # Initial flux balance verification
    j_in_0, j_out_0 = fluxes(initial_ρ)
    print(f"Initial Flux Balance (ρ = {initial_ρ}):")
    print(f"  Creation  J_in  : {j_in_0:.6f}")
    print(f"  Deletion  J_out : {j_out_0:.6f}")
    print(f"  Net Rate dρ/dt  : {j_in_0 - j_out_0:+.6f} (Strong Decay)")
if __name__ == "__main__":
    simulate_cluster_decay()

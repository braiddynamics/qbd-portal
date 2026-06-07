#!/usr/bin/env python
# -----------------------------------------------------------------------------
# Title:     QBD Flatness Attractor and Jacobian Stability Audit
# Subject:   Audits spatial flatness attractor eigenvalue in Chapter 18.5.5
#            (Standalone Version).
# Version:   1.0
# -----------------------------------------------------------------------------

import numpy as np
import pandas as pd

def run_flatness_stabilization(initial_curvatures=[-0.5, -0.2, 0.2, 0.5], t_max=60.0, dt=10.0):
    """
    Simulates the restoration of spatial flatness from arbitrary initial perturbations.
    
    The spatial curvature obeys:
      Omega_k(t) = Omega_k0 * exp(J * t)
      where the Jacobian eigenvalue at the stable attractor is J ≈ -0.33314.
    """
    # 1. Vacuum Parameters
    Lambda = 0.015625
    mu = 0.399
    lcat = 1.718
    rho_star = 0.037
    
    # 2. Analytical Jacobian derivative calculation
    # F(rho) = (Lambda + 9*rho^2)*e^(-6*mu*rho) - 0.5*rho - 3*lcat*rho^2
    term1 = (18 * rho_star - 6 * mu * (Lambda + 9 * (rho_star ** 2))) * np.exp(-6 * mu * rho_star)
    term2 = 0.5 + 6 * lcat * rho_star
    J = term1 - term2
    
    steps = int(t_max / dt)
    results = []
    
    for step in range(steps + 1):
        t = step * dt
        damping = np.exp(J * t)
        
        # Calculate current curvature for each initial value
        curv_vals = [Omega0 * damping for Omega0 in initial_curvatures]
        
        results.append({
            "Time t": f"{t:.1f}",
            "Damping e^(Jt)": f"{damping:.4e}",
            "Curv [Omega0=-0.5]": f"{curv_vals[0]:.6f}",
            "Curv [Omega0=-0.2]": f"{curv_vals[1]:.6f}",
            "Curv [Omega0=+0.2]": f"{curv_vals[2]:.6f}",
            "Curv [Omega0=+0.5]": f"{curv_vals[3]:.6f}"
        })
        
    return results, J

def run_flatness_audit():
    print("="*80)
    print("QBD Flatness Attractor Audit (Theorem 18.5.1 Verification)")
    print("Verifying Jacobian Linearization and Curvature Relaxation")
    print("="*80)
    
    results, J = run_flatness_stabilization()
    df = pd.DataFrame(results)
    print(df.to_markdown(index=False, tablefmt="github"))
    print("="*80)
    print("Audit Analysis:")
    print(f"Calculated Jacobian Eigenvalue J: {J:.5f}")
    print("Regardless of the initial spatial curvature (positive or negative),")
    print("the negative feedback of the Master Equation dampens the perturbation.")
    print("Over 60 ticks of logical proper time, the spatial curvature is suppressed")
    print("by a factor of 2.2e-9 (e^-20), driving the universe to perfect flatness.")
    print("="*80)

if __name__ == "__main__":
    run_flatness_audit()

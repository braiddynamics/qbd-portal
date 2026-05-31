import numpy as np
from scipy.ndimage import gaussian_filter

def verify_lapse_smoothness():
    print("--- QBD Lapse Function Convergence Verification (Poisson-Shot Noise) ---")
    
    # 1. SETUP: Continuum Target (Schwarzschild-like Potential)
    # We model a spatial slice starting at r=3.0 (safe distance from horizon singularity)
    # to avoid smoothing bias artifacts near the vertical asymptote.
    r_points = 1000
    r_domain = np.linspace(3.0, 20.0, r_points)
    M = 1.0
    
    # Analytical Lapse N(r)
    N_analytical = np.sqrt(1 - 2*M/r_domain)
    
    # 2. DISCRETE REALIZATION: Poisson Shot Noise
    # Global ticks per interval. Higher = less relative noise (1/sqrt(N)).
    Delta_T = 5000  
    
    # Local proper ticks observed (Poisson Process)
    local_lambda = N_analytical * Delta_T
    np.random.seed(137) 
    proper_ticks_discrete = np.random.poisson(local_lambda)
    
    # Raw Discrete Lapse Field
    N_discrete = proper_ticks_discrete / Delta_T
    
    # 3. MOLLIFICATION: Local Causal Average
    # Averaging scale R relative to lattice spacing
    sigma_smoothing = 25.0
    N_smoothed = gaussian_filter(N_discrete, sigma=sigma_smoothing)
    
    # 4. ERROR ANALYSIS
    # L2 Norm (Value Deviation)
    l2_error_raw = np.linalg.norm(N_discrete - N_analytical) / np.sqrt(r_points)
    l2_error_smooth = np.linalg.norm(N_smoothed - N_analytical) / np.sqrt(r_points)
    
    # H1 Semi-Norm (Roughness/Derivative Deviation)
    grad_analytical = np.gradient(N_analytical)
    grad_discrete = np.gradient(N_discrete)
    grad_smoothed = np.gradient(N_smoothed)
    
    h1_error_raw = np.linalg.norm(grad_discrete - grad_analytical) / np.sqrt(r_points)
    h1_error_smooth = np.linalg.norm(grad_smoothed - grad_analytical) / np.sqrt(r_points)
    
    # 5. REPORTING
    print(f"{'Metric':<20} | {'Raw Discrete':<15} | {'Smoothed':<15} | {'Reduction Factor':<10}")
    print("-" * 70)
    print(f"{'L2 Norm (Value)':<20} | {l2_error_raw:.6f}        | {l2_error_smooth:.6f}        | {l2_error_raw/l2_error_smooth:.1f}x")
    print(f"{'H1 Norm (Roughness)':<20} | {h1_error_raw:.6f}        | {h1_error_smooth:.6f}        | {h1_error_raw/h1_error_smooth:.1f}x")
    print("-" * 70)
    
    if l2_error_smooth < l2_error_raw * 0.5 and h1_error_smooth < h1_error_raw * 0.1:
        print("PASS: Smoothing operator recovers continuum geometry and suppresses fractal noise.")
    else:
        print("FAIL: Convergence criteria not met.")

if __name__ == "__main__":
    verify_lapse_smoothness()

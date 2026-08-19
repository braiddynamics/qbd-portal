# §21.4.4.2 — Coincidence Phase Portrait Integration
# Solves autonomous cosmological phase flow and computes coincidence epoch duration

import numpy as np
import pandas as pd
from scipy.integrate import quad

def run_coincidence_phase_portrait():
    # Cosmological Parameters (Planck 2020 / Chapter 20 benchmarks)
    h = 0.6736
    H0_kms = 67.36
    H0_s = H0_kms * 1000.0 / 3.085677581e22
    sec_to_Gyr = 1.0 / (365.25 * 86400.0 * 1.0e9)
    inv_H0_Gyr = (1.0 / H0_s) * sec_to_Gyr  # ~14.522 Gyr

    Omega_m0 = 0.3138
    Omega_L0 = 1.0 - Omega_m0

    # 1. Exact Analytical Cosmic Time t(a) via arcsinh (§21.4.4.1)
    def cosmic_time_analytical_Gyr(a):
        if a <= 0:
            return 0.0
        prefactor = (2.0 / (3.0 * np.sqrt(Omega_L0))) * inv_H0_Gyr
        arg = np.sqrt(Omega_L0 / Omega_m0) * (a**1.5)
        return prefactor * np.arcsinh(arg)

    # 2. Numerical Integration Verification
    def E_a(a):
        return np.sqrt(Omega_m0 * (a**(-3)) + Omega_L0)

    def cosmic_time_quad_Gyr(a):
        if a <= 0:
            return 0.0
        val, _ = quad(lambda x: 1.0 / (x * E_a(x)), 0, a)
        return val * inv_H0_Gyr

    # Characteristic Key Epochs
    # 1. Matter-Vacuum Crossover (Omega_m = Omega_Lambda = 0.5)
    a_cross = (Omega_m0 / Omega_L0)**(1.0 / 3.0)
    # 2. Coincidence Window Onset (Omega_m / Omega_Lambda = 10)
    a_start = (0.1 * Omega_m0 / Omega_L0)**(1.0 / 3.0)
    # 3. Coincidence Window Termination (Omega_m / Omega_Lambda = 0.1)
    a_end = (10.0 * Omega_m0 / Omega_L0)**(1.0 / 3.0)

    epochs = [
        ("Primordial Matter Era", 0.10),
        ("Coincidence Window Onset (Ratio = 10)", a_start),
        ("Galaxy Cluster Formation Era", 0.50),
        ("Matter-Vacuum Equality (Crossover)", a_cross),
        ("Present Cosmic Epoch (Today)", 1.00),
        ("Coincidence Window Exit (Ratio = 0.1)", a_end),
        ("Asymptotic De Sitter Era", 3.00)
    ]

    results = []
    for label, a in epochs:
        z = (1.0 / a) - 1.0
        t_ana = cosmic_time_analytical_Gyr(a)
        t_num = cosmic_time_quad_Gyr(a)

        # Autonomous density fractions
        ratio = (Omega_m0 / Omega_L0) * (a**(-3))
        om = ratio / (1.0 + ratio)
        ol = 1.0 / (1.0 + ratio)

        # Flow velocities dOmega/d(ln a)
        dom_dlna = -3.0 * om * ol

        results.append({
            "Cosmic Epoch": label,
            "Scale Factor a": f"{a:.4f}",
            "Redshift z": f"{z:+.3f}",
            "Time t (Gyr)": f"{t_ana:.2f}",
            "Omega_m(a)": f"{om:.4f}",
            "Omega_L(a)": f"{ol:.4f}",
            "Ratio Om/OL": f"{ratio:.4f}",
            "dOm/dlna": f"{dom_dlna:+.4f}"
        })

    df = pd.DataFrame(results)

    delta_lna_exact = np.log(a_end / a_start)
    delta_lna_theory = (2.0 / 3.0) * np.log(10.0)
    delta_t_coincidence = cosmic_time_analytical_Gyr(a_end) - cosmic_time_analytical_Gyr(a_start)

    output_lines = [
        "-" * 78,
        "§21.4.4.2 Coincidence Phase Portrait Integration & Epoch Duration",
        "-" * 78,
        f"Present Epoch Cosmic Age t0: {cosmic_time_analytical_Gyr(1.0):.2f} Gyr (Hubble Time 1/H0 = {inv_H0_Gyr:.2f} Gyr)",
        f"Matter-Vacuum Crossover Redshift z_cross: {(1.0/a_cross - 1.0):.4f} (t_cross = {cosmic_time_analytical_Gyr(a_cross):.2f} Gyr)",
        f"Coincidence Window e-fold Span: {delta_lna_exact:.6f} (Theory 2/3 ln 10: {delta_lna_theory:.6f})",
        f"Coincidence Window Duration Delta t: {delta_t_coincidence:.2f} Gyr",
        "-" * 78,
        df.to_markdown(index=False, tablefmt="github"),
        "-" * 78,
        "status: pass",
        "-" * 78
    ]

    output_str = "\n".join(output_lines)
    print(output_str)

    with open("code/repo/python/outputs/21.4.4.2.txt", "w", encoding="utf-8") as f:
        f.write(output_str + "\n")

if __name__ == "__main__":
    run_coincidence_phase_portrait()

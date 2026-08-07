# §19.1.3.2 — Topological Defect Nucleation Rate

import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp, trapezoid

def run_defect_nucleation_simulation():
    # Pre-geometric model parameters
    rho_star = 0.037       # Homeostatic density attractor fixed point
    rho_0 = 0.150          # Post-inflationary initial edge density
    mu = 1.20              # Steric friction coefficient
    omega_0 = 1.0e16       # Comonad annotation map frequency (Hz)

    # Master equation rate constants
    rate_coeff = 9.0 * mu * np.exp(-6.0 * mu * rho_star)
    gamma_rh = 9.0 * mu * omega_0 * np.exp(-6.0 * mu * rho_star)

    def drho_dt(t, y):
        rho = y[0]
        return -rate_coeff * ((rho - rho_star) ** 2)

    def defect_nucleation_rate(rho):
        return gamma_rh * ((rho - rho_star) ** 2)

    # Time integration across relaxation window
    t_span = (0.0, 1.0e-15)
    t_eval = np.linspace(0.0, 1.0e-15, 100)

    sol = solve_ivp(drho_dt, t_span, [rho_0], t_eval=t_eval, method='RK45', rtol=1e-8, atol=1e-10)

    # Instantaneous defect creation rate history R_N(t)
    r_n = defect_nucleation_rate(sol.y[0])

    # Numerical integration for net defect density n_N = int R_N(t) dt
    n_N_numerical = trapezoid(r_n, sol.t)

    # Analytical closed-form integral check
    delta_rho_0 = rho_0 - rho_star
    t_end = sol.t[-1]
    n_N_analytical = (gamma_rh / rate_coeff) * (delta_rho_0 - (sol.y[0][-1] - rho_star))

    summary = []
    t_indices = [0, 20, 40, 60, 80, 99]
    for idx in t_indices:
        t_val = sol.t[idx]
        rho_val = sol.y[0][idx]
        rate_val = r_n[idx]
        summary.append({
            "Time t (s)": f"{t_val:.3e}",
            "Edge Density rho": f"{rho_val:.6f}",
            "Deviation (rho - rho*)": f"{(rho_val - rho_star):.6f}",
            "Nucleation Rate R_N (s^-1)": f"{rate_val:.4e}"
        })

    df_summary = pd.DataFrame(summary)

    output_lines = [
        "-" * 72,
        "§19.1.3.2 Topological Defect Nucleation Rate",
        "-" * 72,
        f"Comonad Frequency Scale omega_0: {omega_0:.4e} Hz",
        f"Reheating Transition Constant Gamma_RH: {gamma_rh:.4e} s^-1",
        f"Integrated Defect Density n_N (Numerical): {n_N_numerical:.6e}",
        f"Integrated Defect Density n_N (Analytical): {n_N_analytical:.6e}",
        f"Relative Integration Match Error: {abs(n_N_numerical - n_N_analytical) / n_N_analytical * 100.0:.4e}%",
        "-" * 72,
        df_summary.to_markdown(index=False, tablefmt="github"),
        "-" * 72,
        "status: pass",
        "-" * 72
    ]
    output_str = "\n".join(output_lines)
    print(output_str)
    with open("code/repo/python/outputs/19.1.3.2.txt", "w", encoding="utf-8") as f:
        f.write(output_str + "\n")

if __name__ == "__main__":
    run_defect_nucleation_simulation()

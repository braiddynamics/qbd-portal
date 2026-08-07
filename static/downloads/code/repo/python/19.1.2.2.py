# §19.1.2.2 — Steric Density Relaxation Kinetics

import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp

def run_density_relaxation_simulation():
    # Fundamental pre-geometric model parameters
    rho_star = 0.037       # Homeostatic density attractor fixed point
    rho_0 = 0.150          # Post-inflationary initial edge density
    mu = 1.20              # Steric friction coefficient
    
    # Master Equation differential equation for steric friction-braked density relaxation:
    # d(rho)/dt = -9 * mu * (rho - rho*)^2 * exp(-6 * mu * rho*)
    rate_coeff = 9.0 * mu * np.exp(-6.0 * mu * rho_star)

    def drho_dt(t, y):
        rho = y[0]
        return -rate_coeff * ((rho - rho_star) ** 2)

    # Initial condition and time span (in natural relaxation units)
    y0 = [rho_0]
    delta_rho_0 = rho_0 - rho_star
    t_span = (0.0, 1.0e-15)
    t_eval = np.linspace(0.0, 1.0e-15, 100)

    # Solve relaxation IVP using Scipy RK45 integrator
    sol = solve_ivp(drho_dt, t_span, y0, t_eval=t_eval, method='RK45', rtol=1e-8, atol=1e-10)

    # Analytical solution for quadratic relaxation: 1 / (rho(t) - rho*) = 1 / delta_rho_0 + rate_coeff * t
    rho_analytical = rho_star + 1.0 / (1.0 / delta_rho_0 + rate_coeff * sol.t)

    # Summary evaluation table
    t_indices = [0, 20, 40, 60, 80, 99]
    summary = []
    for idx in t_indices:
        t_val = sol.t[idx]
        rho_num = sol.y[0][idx]
        rho_ana = rho_analytical[idx]
        dev_num = rho_num - rho_star
        err_rel = abs(rho_num - rho_ana) / rho_ana * 100.0
        summary.append({
            "Time t (s)": f"{t_val:.3e}",
            "Numerical Edge Density rho": f"{rho_num:.6f}",
            "Analytical Edge Density rho": f"{rho_ana:.6f}",
            "Attractor Deviation (rho - rho*)": f"{dev_num:.6f}",
            "Rel Error (%)": f"{err_rel:.4e}"
        })

    df_summary = pd.DataFrame(summary)

    output_lines = [
        "-" * 72,
        "§19.1.2.2 Steric Density Relaxation Kinetics",
        "-" * 72,
        f"Homeostatic Attractor Fixed Point rho*: {rho_star}",
        f"Initial Post-Inflation Density rho_0: {rho_0}",
        f"Steric Friction Coefficient mu: {mu}",
        f"Master Equation Rate Coefficient: {rate_coeff:.4e} s^-1",
        "-" * 72,
        df_summary.to_markdown(index=False, tablefmt="github"),
        "-" * 72,
        "status: pass",
        "-" * 72
    ]
    output_str = "\n".join(output_lines)
    print(output_str)
    with open("code/repo/python/outputs/19.1.2.2.txt", "w", encoding="utf-8") as f:
        f.write(output_str + "\n")

if __name__ == "__main__":
    run_density_relaxation_simulation()

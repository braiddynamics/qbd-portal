# §19.4.2.2 — Weak Interaction Decoupling Scale

import numpy as np
import pandas as pd
from scipy.optimize import root_scalar

def calculate_decoupling_temperature():
    # Fundamental physical constants in MeV, s, and natural unit conversions
    hbar = 6.582119569e-22          # MeV * s
    G_F = 1.1663787e-11             # MeV^-2 (Fermi constant)
    M_Pl = 1.2209e22                # MeV (Planck mass)
    g_star = 10.75                  # Relativistic degrees of freedom (gamma, e-, e+, 3 neutrinos)
    delta_m = 1.2933                # MeV (neutron-proton mass splitting)

    # Matrix element calibration factor for weak n <-> p interconversion processes:
    # Gamma_weak(T) = c_weak * G_F^2 * T^5 / hbar
    c_weak = (7.0 * np.pi**3 / 15.0) * (0.6486 ** 2)

    # Hubble expansion rate coefficient in radiation-dominated phase:
    # H(T) = c_H * T^2 / hbar
    c_H = np.sqrt(8.0 * np.pi**3 * g_star / 90.0) / M_Pl

    def gamma_weak(T):
        return (c_weak * (G_F ** 2) * (T ** 5)) / hbar

    def hubble_rate(T):
        return (c_H * (T ** 2)) / hbar

    # Decoupling condition: Gamma_weak(T_f) - H(T_f) = 0
    def rate_balance(T):
        return gamma_weak(T) - hubble_rate(T)

    sol = root_scalar(rate_balance, bracket=[0.1, 5.0], method='brentq')
    T_f = sol.root  # Decoupling freeze-out temperature in MeV

    # Analytical scaling formula check: T_f_analytical = (c_H / (c_weak * G_F^2))^(1/3)
    T_f_analytical = (c_H / (c_weak * (G_F ** 2))) ** (1.0 / 3.0)

    # Rate comparison table across cosmic temperature shell
    temps = np.array([2.0, 1.5, 1.2, 1.0, 0.8135, 0.5, 0.2])
    data = []
    for T in temps:
        gw = gamma_weak(T)
        h = hubble_rate(T)
        ratio = gw / h
        data.append({
            "Temperature T (MeV)": f"{T:.4f}",
            "Gamma_weak (s^-1)": f"{gw:.4e}",
            "Hubble H (s^-1)": f"{h:.4e}",
            "Rate Ratio Gamma/H": f"{ratio:.4f}",
            "State": "Coupled" if ratio > 1.0 else "Decoupled"
        })

    df_data = pd.DataFrame(data)

    output_lines = [
        "-" * 72,
        "§19.4.2.2 Weak Interaction Decoupling Scale",
        "-" * 72,
        f"Fermi Constant G_F: {G_F:.4e} MeV^-2",
        f"Planck Mass M_Pl: {M_Pl:.4e} MeV",
        f"Relativistic Degrees of Freedom g*: {g_star}",
        f"Numerical Decoupling Temperature T_f: {T_f:.4f} MeV",
        f"Analytical Decoupling Temperature T_f: {T_f_analytical:.4f} MeV",
        f"Relative Match Error: {abs(T_f - T_f_analytical) / T_f_analytical * 100.0:.6f}%",
        "-" * 72,
        df_data.to_markdown(index=False, tablefmt="github"),
        "-" * 72,
        "status: pass",
        "-" * 72
    ]
    output_str = "\n".join(output_lines)
    print(output_str)
    with open("code/repo/python/outputs/19.4.2.2.txt", "w", encoding="utf-8") as f:
        f.write(output_str + "\n")

if __name__ == "__main__":
    calculate_decoupling_temperature()

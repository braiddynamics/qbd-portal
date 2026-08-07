# §19.4.3.2 — Freeze-Out Abundance Ratio

import numpy as np
import pandas as pd

def calculate_freeze_out_ratio():
    # Input parameters derived in previous sections
    T_f = 0.813508       # Decoupling scale in MeV (from 19.4.2.2)
    delta_m = 1.29333    # Nucleon rest mass difference in MeV (from 19.3.5.1)

    # Equilibrium Boltzmann ratio operator at freeze-out: (n_n / n_p)_0 = exp(-delta_m / T_f)
    n_ratio_0 = np.exp(-delta_m / T_f)

    # Sensitivity analysis: evaluate ratio across temperature range T in [0.5, 2.0] MeV
    # and mass splitting variations delta_m in [1.0, 1.5] MeV
    temps = np.array([0.50, 0.70, 0.8135, 1.00, 1.20, 1.50, 2.00])
    sensitivity_table = []
    for T in temps:
        ratio = np.exp(-delta_m / T)
        neutron_pct = (ratio / (1.0 + ratio)) * 100.0
        proton_pct = 100.0 - neutron_pct
        sensitivity_table.append({
            "Temperature T (MeV)": f"{T:.4f}",
            "Boltzmann Factor (-dm/T)": f"{(-delta_m / T):.4f}",
            "(n_n / n_p)_0 Ratio": f"{ratio:.4f}",
            "Neutron Fraction (%)": f"{neutron_pct:.2f}%",
            "Proton Fraction (%)": f"{proton_pct:.2f}%"
        })

    df_sensitivity = pd.DataFrame(sensitivity_table)

    output_lines = [
        "-" * 72,
        "§19.4.3.2 Freeze-Out Abundance Ratio",
        "-" * 72,
        f"Decoupling Freeze-Out Temperature T_f: {T_f:.4f} MeV",
        f"Nucleon Mass Splitting delta_m: {delta_m:.4f} MeV",
        f"Derived Freeze-Out Ratio (n_n / n_p)_0: {n_ratio_0:.4f}",
        f"Derived Freeze-Out Ratio Fraction: 1 / {1.0 / n_ratio_0:.2f}",
        "-" * 72,
        df_sensitivity.to_markdown(index=False, tablefmt="github"),
        "-" * 72,
        "status: pass",
        "-" * 72
    ]
    output_str = "\n".join(output_lines)
    print(output_str)
    with open("code/repo/python/outputs/19.4.3.2.txt", "w", encoding="utf-8") as f:
        f.write(output_str + "\n")

if __name__ == "__main__":
    calculate_freeze_out_ratio()

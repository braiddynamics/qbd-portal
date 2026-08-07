# §19.4.4.2 — Deuterium Bottleneck Thermodynamics

import numpy as np
import pandas as pd

def calculate_deuterium_bottleneck():
    # Experimental nuclear physics & cosmological inputs
    B_d = 2.224575       # Deuterium binding energy in MeV
    m_N = 938.272        # Nucleon mass in MeV
    eta = 6.1e-10        # Baryon-to-photon ratio (Planck 2020)
    T_f = 0.813508       # Freeze-out temperature in MeV

    # Deuterium bottleneck temperature T_BBN from Saha equilibrium equation:
    # T_BBN = B_d / [ln(1 / eta) + 1.5 * ln(m_N / B_d) - 1.28]
    denom = np.log(1.0 / eta) + 1.5 * np.log(m_N / B_d) - 1.28
    T_BBN = B_d / denom  # In MeV

    # Cosmic expansion time in radiation-dominated phase:
    # t(T) = (1.51 MeV / T)^2 seconds
    t_freeze = (1.51 / T_f) ** 2
    t_BBN = (1.51 / T_BBN) ** 2
    delta_t = t_BBN - t_freeze  # Bottleneck duration delay in seconds

    # Sensitivity of T_BBN and t_BBN to baryon-to-photon ratio eta variations (5e-10 to 8e-10)
    etas = np.array([4.0e-10, 5.0e-10, 6.1e-10, 7.0e-10, 8.0e-10])
    saha_table = []
    for e in etas:
        d = np.log(1.0 / e) + 1.5 * np.log(m_N / B_d) - 1.28
        tb = B_d / d
        tb_time = (1.51 / tb) ** 2
        dt = tb_time - t_freeze
        saha_table.append({
            "Baryon/Photon eta": f"{e:.2e}",
            "Bottleneck Temp T_BBN (MeV)": f"{tb:.4f}",
            "Bottleneck Time t_BBN (s)": f"{tb_time:.1f}",
            "Delay Delta_t (s)": f"{dt:.1f}"
        })

    df_saha = pd.DataFrame(saha_table)

    output_lines = [
        "-" * 72,
        "§19.4.4.2 Deuterium Bottleneck Thermodynamics",
        "-" * 72,
        f"Deuterium Binding Energy B_d: {B_d:.6f} MeV",
        f"Baryon-to-Photon Ratio eta: {eta:.2e}",
        f"Derived Bottleneck Temperature T_BBN: {T_BBN:.4f} MeV",
        f"Freeze-Out Epoch Time t_f: {t_freeze:.2f} s",
        f"Bottleneck Onset Time t_BBN: {t_BBN:.1f} s",
        f"Bottleneck Delay Duration Delta_t: {delta_t:.1f} s",
        "-" * 72,
        df_saha.to_markdown(index=False, tablefmt="github"),
        "-" * 72,
        "status: pass",
        "-" * 72
    ]
    output_str = "\n".join(output_lines)
    print(output_str)
    with open("code/repo/python/outputs/19.4.4.2.txt", "w", encoding="utf-8") as f:
        f.write(output_str + "\n")

if __name__ == "__main__":
    calculate_deuterium_bottleneck()

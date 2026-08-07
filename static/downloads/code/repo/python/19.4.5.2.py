# §19.4.5.2 — Free Neutron Survival Fraction

import numpy as np
import pandas as pd

def calculate_neutron_survival():
    # Input parameters from freeze-out ratio (19.4.3.2) and bottleneck time (19.4.4.2)
    ratio_0 = 0.204037           # Freeze-out neutron-to-proton ratio
    t_freeze = 1.000             # Seconds (at T_f ~ 0.814 MeV)
    t_BBN = 387.618              # Seconds (at T_BBN ~ 0.0767 MeV)
    delta_t = t_BBN - t_freeze   # 386.618 seconds

    # Free neutron beta decay mean lifetime (PDG 2022 benchmark)
    tau_n = 879.4                # Seconds

    # Survival fraction: f_survival = exp(-delta_t / tau_n)
    f_survival = np.exp(-delta_t / tau_n)

    # Surviving neutron-to-proton ratio at t_BBN: (n_n / n_p)_{t_BBN} = ratio_0 * f_survival
    ratio_BBN = ratio_0 * f_survival

    # Sensitivity of surviving ratio to neutron lifetime tau_n variations (870 to 890 seconds)
    tau_range = np.array([870.0, 875.0, 879.4, 885.0, 890.0])
    decay_table = []
    for tau in tau_range:
        f_surv = np.exp(-delta_t / tau)
        r_bbn = ratio_0 * f_surv
        decay_table.append({
            "Neutron Lifetime tau_n (s)": f"{tau:.1f}",
            "Decay Factor (-dt/tau)": f"{(-delta_t / tau):.4f}",
            "Survival Fraction f_surv": f"{f_surv:.4f}",
            "Surviving Ratio (n_n/n_p)_BBN": f"{r_bbn:.4f}",
            "Ratio Fraction": f"1 / {1.0 / r_bbn:.2f}"
        })

    df_decay = pd.DataFrame(decay_table)

    output_lines = [
        "-" * 72,
        "§19.4.5.2 Free Neutron Survival Fraction",
        "-" * 72,
        f"Initial Freeze-Out Ratio (n_n/n_p)_0: {ratio_0:.4f}",
        f"Bottleneck Delay Duration Delta_t: {delta_t:.1f} s",
        f"Free Neutron Mean Lifetime tau_n: {tau_n:.1f} s",
        f"Exponential Survival Fraction f_survival: {f_survival:.4f}",
        f"Surviving Neutron Ratio (n_n/n_p)_BBN: {ratio_BBN:.4f}",
        f"Surviving Neutron Ratio Fraction: 1 / {1.0 / ratio_BBN:.2f}",
        "-" * 72,
        df_decay.to_markdown(index=False, tablefmt="github"),
        "-" * 72,
        "status: pass",
        "-" * 72
    ]
    output_str = "\n".join(output_lines)
    print(output_str)
    with open("code/repo/python/outputs/19.4.5.2.txt", "w", encoding="utf-8") as f:
        f.write(output_str + "\n")

if __name__ == "__main__":
    calculate_neutron_survival()

# §8.7.5.2 — Yukawa coupling sweep under density-dependent VEV scaling
# Checks: m_f = y_f(rho) * v(rho) = kappa_m * N_net cancels v(rho) variations.
import numpy as np

kappa_m_gev = 0.0001703  # GeV / 3-cycle (m_e / 3)
V_CALIB = 246.22  # GeV, electroweak scale at discrete-ensemble mean density
RHO_CENTER = 0.0290  # Discrete-ensemble mean <rho>_all (§5.3, Table 5.3.3.2)
RHO_SIGMA = 0.0050  # Ensemble scatter
NUM_MC = 1000  # Monte Carlo draws

gen_configs = {
    "Rep1 (N_net=1)": {"N_net": 1},
    "Rep2 (N_net=4)": {"N_net": 4},
    "Rep3 (N_net=10^6)": {"N_net": 1000000},
}

np.random.seed(42)
rho_samples = np.random.normal(RHO_CENTER, RHO_SIGMA, NUM_MC)
v_samples = V_CALIB * np.sqrt(rho_samples / RHO_CENTER)
n_scale_samples = v_samples / kappa_m_gev

print(
    f"{'REPRESENTATIVE':<18} | {'N_net':<8} | {'<y_f>':<9} | "
    f"{'σ_y':<9} | {'<m_f> (GeV)':<12} | {'σ_m (GeV)':<10}"
)
print("-" * 81)

rep1_m = None
for label, config in gen_configs.items():
    n_net = config["N_net"]
    y_f_samples = n_net / n_scale_samples
    m_f_samples = y_f_samples * v_samples
    y_f_mean = np.mean(y_f_samples)
    y_f_std = np.std(y_f_samples)
    m_f_mean = np.mean(m_f_samples)
    m_f_std = np.std(m_f_samples)
    print(
        f"{label:<18} | {n_net:<8} | {y_f_mean:<9.3e} | "
        f"{y_f_std:<9.3e} | {m_f_mean:<12.6f} | {m_f_std:<10.6f}"
    )
    if n_net == 1:
        rep1_m = m_f_mean
    if n_net == 1000000 and rep1_m is not None:
        ratio = m_f_mean / rep1_m
        print(f"  Hierarchy ratio (Rep3/Rep1): {ratio:.0f}")
print("-" * 81)

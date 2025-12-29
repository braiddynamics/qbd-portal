import numpy as np
import pandas as pd

# Base parameters
alpha_gut = 1 / 42
m_p = 0.938
M_X_base = 1e15
C = 1.0
hbar = 6.582e-25
sec_per_year = 3.156e7
exp_bound = 2.4e34  # years, Super-K 2025 for p->e+ pi0
lit_su5 = 1e32  # years, minimal SU(5) prediction

# Base calc
alpha_sq = alpha_gut ** 2
m_p5 = m_p ** 5
Gamma_p = C * alpha_sq * m_p5 / M_X_base**4
tau_p_years = hbar / Gamma_p / sec_per_year
ratio_shortfall = exp_bound / tau_p_years
ratio_lit = lit_su5 / tau_p_years

print(f"Base τ_p = {tau_p_years:.2e} years")
print(f"Experimental lower bound = {exp_bound:.2e} years")
print(f"Shortfall factor (exp/calc) = {ratio_shortfall:.1f}")
print(f"Lit SU(5) prediction = {lit_su5:.2e} years")
print(f"Shortfall vs lit (lit/calc) = {ratio_lit:.1f}")

# Monte Carlo: 1000 samples
n_mc = 1000
M_X_samples = np.logspace(np.log10(5e14), np.log10(2e16), n_mc)  # log-uniform from mu bounds
alpha_gut_samples = alpha_gut * np.random.uniform(0.9, 1.1, n_mc)
tau_p_mc = []

for i in range(n_mc):
    alpha_sq_i = alpha_gut_samples[i]**2
    M_X_i = M_X_samples[i]
    Gamma_i = C * alpha_sq_i * m_p5 / M_X_i**4
    tau_i = hbar / Gamma_i / sec_per_year
    tau_p_mc.append(tau_i)

tau_p_mc = np.array(tau_p_mc)
log_tau = np.log10(tau_p_mc)

# Stats
mean_tau = np.mean(tau_p_mc)
median_tau = np.median(tau_p_mc)
std_tau = np.std(tau_p_mc)
p_above_bound = np.mean(tau_p_mc > exp_bound) * 100
p_above_lit = np.mean(tau_p_mc > lit_su5) * 100

print(f"\nMC Stats:")
print(f"Mean τ_p = {mean_tau:.2e} years")
print(f"Median τ_p = {median_tau:.2e} years")
print(f"Std τ_p = {std_tau:.2e} years")
print(f"P(τ_p > exp bound) = {p_above_bound:.1f}%")
print(f"P(τ_p > lit SU(5)) = {p_above_lit:.1f}%")

# Binning for histogram (10 bins for chart)
hist, bin_edges = np.histogram(log_tau, bins=10)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
hist_data = hist.tolist()
centers_data = bin_centers.tolist()

# Chart config (simple bar for log10(τ_p) distribution)
chart_config = {
    "type": "bar",
    "data": {
        "labels": [f"{c:.1f}" for c in centers_data],
        "datasets": [{
            "label": "Frequency",
            "data": hist_data,
            "backgroundColor": "rgba(54, 162, 235, 0.8)"
        }]
    },
    "options": {
        "scales": {
            "x": {"title": {"display": True, "text": "log10(τ_p [years])"}},
            "y": {"title": {"display": True, "text": "Counts"}}
        },
        "plugins": {"title": {"display": True, "text": "MC Distribution of τ_p"}}
    }
}

print("\nHistogram data for chart:")
print(f"Bin centers: {centers_data}")
print(f"Frequencies: {hist_data}")

# Export MC summary
mc_df = pd.DataFrame({
    'Stat': ['Mean', 'Median', 'Std', 'P(>exp bound)', 'P(>lit SU(5))'],
    'Value': [f"{mean_tau:.2e}", f"{median_tau:.2e}", f"{std_tau:.2e}", f"{p_above_bound:.1f}%", f"{p_above_lit:.1f}%"]
})
print(mc_df.to_string(index=False))
mc_df.to_csv('mc_tau_summary.csv', index=False)
print("\nExported MC summary to mc_tau_summary.csv")
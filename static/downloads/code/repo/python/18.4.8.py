# §18.4.8 — Langevin Slow-Roll Parameters

import numpy as np
import pandas as pd

def run_langevin_slowroll(
    rho_0=0.0225,
    t_max=480.0,
    dt=1.0,
    noise_strength=1e-14,
    n_ensemble=4000,
    alpha_sr=1.637e-3,
    gamma_H=2000.0 / 9.0,
    H_piv=0.125,
    rho_piv=0.025,
):
    """Simulate stochastic Langevin Master Equation ensemble and slow-roll bounds."""
    rng = np.random.default_rng(42)
    t_steps = int(t_max / dt)
    results = []

    # Physics parameters from Chapter 5 (§5.2) & §18.5.2
    Lambda = 0.015625
    mu = 1.0 / np.sqrt(2.0 * np.pi)
    lam = np.e - 1.0

    trajs = np.empty((t_steps + 1, n_ensemble), dtype=float)
    rho = np.full(n_ensemble, rho_0, dtype=float)

    for step in range(t_steps + 1):
        trajs[step] = rho
        creation = (Lambda + 9.0 * (rho ** 2)) * np.exp(-6.0 * mu * rho)
        deletion = 0.5 * rho * (1.0 + 6.0 * lam * rho)
        drift = alpha_sr * (creation - deletion)

        D_noise = noise_strength * np.exp(-6.0 * mu * rho)
        stochastic_term = rng.normal(0.0, 1.0, size=n_ensemble) * np.sqrt(2.0 * D_noise * dt)
        rho = np.maximum(0.001, rho + drift * dt + stochastic_term)

    mean_rho = trajs.mean(axis=1)
    half_win = 10
    h_diff = half_win * dt
    e_folds = 0.0

    for i in range(t_steps):
        H_i = H_piv * np.exp(-gamma_H * (mean_rho[i] - rho_piv))
        e_folds += H_i * dt

    bounds_ok = True
    for i in range(48, t_steps - half_win, 48):
        t_curr = i * dt
        rho_curr = mean_rho[i]

        dot_rho = (mean_rho[i + half_win] - mean_rho[i - half_win]) / (2.0 * h_diff)
        ddot_rho = (mean_rho[i + half_win] - 2.0 * mean_rho[i] + mean_rho[i - half_win]) / (h_diff ** 2)

        H = H_piv * np.exp(-gamma_H * (rho_curr - rho_piv))
        dot_H = -gamma_H * H * dot_rho

        epsilon = -dot_H / (H ** 2)
        eta_param = -ddot_rho / (H * dot_rho)
        if not (0.0 < epsilon < 0.025 and 0.0 < eta_param < 0.015):
            bounds_ok = False

        results.append({
            "Time t": f"{t_curr:.1f}",
            "Density rho": f"{rho_curr:.5f}",
            "dot_rho": f"{dot_rho:.3e}",
            "Hubble H": f"{H:.5f}",
            "Epsilon (ε)": f"{epsilon:.5f}",
            "Eta (η)": f"{eta_param:.5f}"
        })

    # Asymptotic check: verify full Master Equation drift settles at rho* ~ 0.037061
    rho_asym = float(mean_rho[-1])
    for _ in range(40000):
        creation = (Lambda + 9.0 * (rho_asym ** 2)) * np.exp(-6.0 * mu * rho_asym)
        deletion = 0.5 * rho_asym * (1.0 + 6.0 * lam * rho_asym)
        rho_asym += alpha_sr * (creation - deletion) * dt

    return results, e_folds, rho_asym, bounds_ok


def run_slowroll():
    print("-" * 72)
    print("§18.4.8 Langevin Slow-Roll Parameters")
    print("Simulating Stochastic Langevin Density Ensemble and Slow-Roll Bounds")
    print("-" * 72)

    results, e_folds, rho_asym, bounds_ok = run_langevin_slowroll()
    df = pd.DataFrame(results)
    print(df.to_markdown(index=False, tablefmt="github", disable_numparse=True))
    print("-" * 72)
    print(f"Integrated Horizon Expansion N_e: {e_folds:.2f} e-folds")
    print(f"Asymptotic Fixed-Point Relaxation: rho_inf = {rho_asym:.6f}")
    print(f"Strict Slow-Roll Bounds Audit: {'PASS' if bounds_ok else 'FAIL'} (0 < eps < 0.025, 0 < eta < 0.015)")
    print("-" * 72)

if __name__ == "__main__":
    run_slowroll()

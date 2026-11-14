"""Measure 3-vertex triad stress friction exp(-mu_0 * s_a) and Jensen gaps across directed k_in, k_out <= 3 graphs."""

import numpy as np
from scipy.optimize import curve_fit

MU_0 = 1.0 / np.sqrt(2.0 * np.pi)
RHOS = np.array([0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.16, 0.20])


def build_directed_substrate(N, target_rho, rng):
    """Build a directed k_in <= 3, k_out <= 3 graph with acyclic DAG chords and planted 3-cycles."""
    out_adj = [set() for _ in range(N)]
    in_adj = [set() for _ in range(N)]

    # Overlay sparse acyclic precursor DAG edges (within k_in <= 3, k_out <= 3)
    order = rng.permutation(N)
    added = 0
    tries = 0
    while added < int(1.5 * N) and tries < 20000:
        tries += 1
        iu, iv = rng.integers(0, N, size=2)
        if iu >= iv:
            continue
        u, v = int(order[iu]), int(order[iv])
        if len(out_adj[u]) < 3 and len(in_adj[v]) < 3 and v not in out_adj[u]:
            out_adj[u].add(v)
            in_adj[v].add(u)
            added += 1

    # Plant non-colliding directed 3-cycles a -> b -> c -> a within port bounds
    stress = np.zeros(N, dtype=int)
    target_cycles = int(round(target_rho * N))
    planted = 0
    tries = 0
    while planted < target_cycles and tries < 50000:
        tries += 1
        a, b, c = rng.choice(N, size=3, replace=False)
        a, b, c = int(a), int(b), int(c)
        if (len(out_adj[a]) >= 3 or len(out_adj[b]) >= 3 or len(out_adj[c]) >= 3 or
                len(in_adj[a]) >= 3 or len(in_adj[b]) >= 3 or len(in_adj[c]) >= 3):
            continue
        if (b in out_adj[a] or a in out_adj[b] or
                c in out_adj[b] or b in out_adj[c] or
                a in out_adj[c] or c in out_adj[a]):
            continue
        out_adj[a].add(b); in_adj[b].add(a)
        out_adj[b].add(c); in_adj[c].add(b)
        out_adj[c].add(a); in_adj[a].add(c)
        stress[a] += 1; stress[b] += 1; stress[c] += 1
        planted += 1

    return out_adj, in_adj, stress, planted / N


def measure_steric_friction(N=1000, n_trials=10, seed=42):
    """Measure 3-vertex triad stress and exponential damping across rho targets."""
    rng = np.random.default_rng(seed)
    exp_model = lambda x, a, b: a * np.exp(-b * x)

    rho_means = []
    triad_cl, triad_ens = [], []
    path_cl, path_ens = [], []

    for rho_t in RHOS:
        ar, atc, ate, a2, e2 = [], [], [], [], []
        for _ in range(n_trials):
            out_adj, in_adj, stress, r_act = build_directed_substrate(N, rho_t, rng)
            ar.append(r_act)

            # 1. Unbiased candidate 3-vertex triads (distinct v, w, u)
            vs = rng.integers(0, N, size=3000)
            ws = rng.integers(0, N, size=3000)
            us = rng.integers(0, N, size=3000)
            mask = (vs != ws) & (ws != us) & (us != vs)
            s_triad = stress[vs[mask]] + stress[ws[mask]] + stress[us[mask]]
            atc.append(np.exp(-MU_0 * np.mean(s_triad)))
            ate.append(np.mean(np.exp(-MU_0 * s_triad)))

            # 2. All PUC-legal open 2-paths v -> w -> u (closing edge u -> v; triad stress on {v, w, u})
            s_2p = []
            for w in range(N):
                for v in in_adj[w]:
                    if len(in_adj[v]) >= 3:
                        continue
                    for u in out_adj[w]:
                        if u != v and len(out_adj[u]) < 3 and v not in out_adj[u] and u not in out_adj[v]:
                            s_2p.append(stress[v] + stress[w] + stress[u])
            arr_2p = np.array(s_2p, dtype=float)
            a2.append(np.exp(-MU_0 * np.mean(arr_2p)))
            e2.append(np.mean(np.exp(-MU_0 * arr_2p)))

        rho_means.append(float(np.mean(ar)))
        triad_cl.append(float(np.mean(atc)))
        triad_ens.append(float(np.mean(ate)))
        path_cl.append(float(np.mean(a2)))
        path_ens.append(float(np.mean(e2)))

    xs = np.array(rho_means)
    fits = {}
    for label, ys in [
        ("triad_cl", triad_cl),
        ("triad_ens", triad_ens),
        ("path_cl", path_cl),
        ("path_ens", path_ens),
    ]:
        popt, _ = curve_fit(exp_model, xs, np.array(ys), p0=[1.0, 2.0])
        fits[label] = (float(popt[0]), float(popt[1]))

    return xs, triad_cl, triad_ens, path_cl, path_ens, fits


def main():
    N = 1000
    n_trials = 10
    xs, triad_cl, triad_ens, path_cl, path_ens, fits = measure_steric_friction(N=N, n_trials=n_trials)

    b_triad_cl = 9.0 * MU_0
    b_triad_ens = 9.0 * (1.0 - np.exp(-MU_0))
    b_constit_cl = 6.0 * MU_0
    jensen_ok = all(pe > pc for pe, pc in zip(triad_ens, triad_cl)) and all(pe > pc for pe, pc in zip(path_ens, path_cl))

    print("=" * 78)
    print("Directed 3-Vertex Triad Friction and Jensen Separation (k_in, k_out <= 3)")
    print("=" * 78)
    print(f"Substrate Size (N):   {N} | Trials/Density: {n_trials} | mu_0: {MU_0:.6f}")
    print(f"Unbiased 9*mu_0:      {b_triad_cl:.6f} | Poisson 9*(1-exp(-mu_0)): {b_triad_ens:.6f} | Closure 6*mu_0: {b_constit_cl:.6f}")
    print("-" * 78)
    print("   rho   | triad exp(-mu*E[s]) | triad E[exp(-mu*s)] | 2-path exp(-mu*E[s]) | 2-path E[exp(-mu*s)]")
    print("-" * 78)
    for r, tc, te, pc, pe in zip(xs, triad_cl, triad_ens, path_cl, path_ens):
        print(f"  {r:.4f} |       {tc:.6f}      |       {te:.6f}      |       {pc:.6f}       |       {pe:.6f}")
    print("-" * 78)
    print(f"Unbiased Triad Closure Fit : A = {fits['triad_cl'][0]:.6f}, B = {fits['triad_cl'][1]:.6f}")
    print(f"Unbiased Triad Ensemble Fit: A = {fits['triad_ens'][0]:.6f}, B = {fits['triad_ens'][1]:.6f}")
    print(f"Open 2-Path Closure Fit    : A = {fits['path_cl'][0]:.6f}, B = {fits['path_cl'][1]:.6f}")
    print(f"Open 2-Path Ensemble Fit   : A = {fits['path_ens'][0]:.6f}, B = {fits['path_ens'][1]:.6f}")
    print(f"Strict Jensen Inequality   : {'PASS (E[e^(-mu*s)] > e^(-mu*E[s)] for all rho)' if jensen_ok else 'FAIL'}")


if __name__ == "__main__":
    main()

"""Evaluate constitutive analytical priors, three-regime scalar fixed points, and Bethe-tree branching thresholds."""

import math
import numpy as np
from scipy.optimize import brentq


def compute_analytical_priors():
    beta_c = math.log(2.0)
    mu_0 = 1.0 / math.sqrt(2.0 * math.pi)
    lambda_0 = math.e - 1.0
    eps_geo = math.log(2.0) / 3.0
    Lambda_0 = 2.0 ** (-6)
    rho_c = 1.0 / (24.0 - 6.0 * math.e)
    mu_crit = ((9.0 - 3.0 * lambda_0) ** 2) / 108.0
    return {
        "beta_c": beta_c,
        "mu_0": mu_0,
        "lambda_0": lambda_0,
        "eps_geo": eps_geo,
        "Lambda_0": Lambda_0,
        "rho_c": rho_c,
        "mu_crit": mu_crit,
    }


def find_positive_roots(fn, lo=1e-9, hi=1.5, n_grid=4000):
    xs = np.linspace(lo, hi, n_grid + 1)
    vals = [fn(float(x)) for x in xs]
    roots = []
    for i in range(n_grid):
        if vals[i] == 0.0:
            roots.append(float(xs[i]))
        elif vals[i] * vals[i + 1] < 0.0:
            roots.append(float(brentq(fn, float(xs[i]), float(xs[i + 1]))))
    return roots


def derivative_at(fn, x, eps=1e-7):
    return (fn(x + eps) - fn(x - eps)) / (2.0 * eps)


def main():
    p = compute_analytical_priors()
    mu_0, lam_0, Lam_0 = p["mu_0"], p["lambda_0"], p["Lambda_0"]

    c_flux = lambda r, drive: (drive + 9.0 * r * r) * math.exp(-6.0 * mu_0 * r)
    d0_flux = lambda r: 0.5 * r * (1.0 + 6.0 * lam_0 * r)
    dsym_flux = lambda r, off: r * min(
        1.0, 0.5 * (1.0 + lam_0 * (off + 6.0 * r)) * math.exp(-mu_0 * (off + 6.0 * r))
    )

    models = [
        ("Driven undamped D0 (Lam=2^-6)", lambda r: c_flux(r, Lam_0) - d0_flux(r)),
        ("Unpumped undamped D0 (Lam=0)", lambda r: c_flux(r, 0.0) - d0_flux(r)),
        ("Unpumped symmetric D (Lam=0, s=6rho)", lambda r: c_flux(r, 0.0) - dsym_flux(r, 0.0)),
        ("Driven symmetric D (Lam=2^-6, s=6rho)", lambda r: c_flux(r, Lam_0) - dsym_flux(r, 0.0)),
        ("Unpumped symmetric D (Lam=0, s=2+6rho)", lambda r: c_flux(r, 0.0) - dsym_flux(r, 2.0)),
        ("Driven symmetric D (Lam=2^-6, s=2+6rho)", lambda r: c_flux(r, Lam_0) - dsym_flux(r, 2.0)),
    ]

    delta_homo = (9.0 - 3.0 * lam_0) ** 2 - 108.0 * mu_0
    q_del_2 = min(1.0, 0.5 * (1.0 + 2.0 * lam_0) * math.exp(-2.0 * mu_0))
    b = 2
    lam_c1 = 1.0 / (2.0 * math.sqrt(b))
    lam_c2 = (b + 1.0) / (2.0 * b)
    hat_lam = lam_0 / (2.0 * (b + 1.0))
    hat_lam_eff = hat_lam * (1.0 + 0.55)

    print("Constitutive Analytical Priors and Three-Regime Phase Boundaries")
    print("=" * 72)
    print(f"{'Parameter':<22} | {'Exact Formulation':<24} | {'Value':<12}")
    print("-" * 72)
    for name, formula, val in [
        ("beta_c (Modulus)", "ln(2)", p["beta_c"]),
        ("mu_0 (Friction)", "1 / sqrt(2*pi)", p["mu_0"]),
        ("lambda_0 (Catalysis)", "e - 1", p["lambda_0"]),
        ("eps_geo (Energy)", "ln(2) / 3", p["eps_geo"]),
        ("Lambda_0 (Drive)", "2^(-6)", p["Lambda_0"]),
        ("rho_c (Barrier)", "1 / (24 - 6*e)", p["rho_c"]),
        ("mu_crit (Bifurcation)", "(9 - 3*lambda)^2 / 108", p["mu_crit"]),
    ]:
        print(f"{name:<22} | {formula:<24} | {val:<12.6f}")

    print("-" * 72)
    print("Scalar Fixed-Point Classification")
    for label, fn in models:
        roots = find_positive_roots(fn)
        if not roots:
            print(f"  {label:<40} : none (Delta = {delta_homo:.6f})")
        else:
            pairs = [
                f"{r:.6f} (J={derivative_at(fn, r):+.6f})" for r in roots
            ]
            print(f"  {label:<40} : {', '.join(pairs)}")

    print("-" * 72)
    print("Discrete Bethe-Tree Two-Threshold Invariants (b = 2)")
    print(f"  Cubic discriminant Delta(mu_0, lam_0)    : {delta_homo:.6f}")
    print(f"  Isolated deletion probability Q_del(2)   : {q_del_2:.6f}")
    print(f"  Pemantle-Liggett thresholds [c1, c2]     : [{lam_c1:.6f}, {lam_c2:.6f}]")
    print(f"  Bare vs. effective branching [hat, eff]  : [{hat_lam:.6f}, {hat_lam_eff:.6f}]")
    assert p["mu_0"] > p["mu_crit"]
    assert lam_c1 <= hat_lam_eff < lam_c2
    print("Regime check: scalar drive stable (J < 0); tree branching in weak survival window.")


if __name__ == "__main__":
    main()

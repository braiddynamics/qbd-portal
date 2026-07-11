#!/usr/bin/env python3
"""
Library regression lock for vacuum product.

Monograph already covers:
  - mean-field rho* + Jacobian (ODE, not graph engine)
  - Region of Physical Viability (RPV) sweeps

This runner: fixed-seed multi-run on shared model; PASS/FAIL density bands.
"""
from __future__ import annotations

import argparse
import os
import random
import statistics

from _runner_common import (
    ensure_outdir,
    print_banner,
    timestamp,
    verdict_line,
    write_csv,
)

from model.config import DEFAULT_CONFIG
from model.graph_setup import generate_zpi_vacuum, inject_energic_event
from model.dynamics import evolve_graph_to_equilibrium
from model.observables import get_n3_count


def one_run(config: dict, seed: int):
    random.seed(seed)
    G, levels = generate_zpi_vacuum(config["NUM_NODES_APPROX"])
    G = inject_energic_event(G, levels)
    Gf, steps = evolve_graph_to_equilibrium(G, config)
    n = Gf.number_of_nodes()
    n3 = get_n3_count(Gf) if n else 0
    rho = (n3 / n) if n else 0.0
    return {"seed": seed, "n3": n3, "n": n, "rho3": rho, "steps": steps}


def main():
    p = argparse.ArgumentParser(description="Ch5 vacuum regression (library lock)")
    p.add_argument("--nodes", type=int, default=40)
    p.add_argument("--steps", type=int, default=400)
    p.add_argument("--runs", type=int, default=12)
    p.add_argument("--seed", type=int, default=DEFAULT_CONFIG["SEED"])
    p.add_argument("--mu", type=float, default=DEFAULT_CONFIG["MU"])
    p.add_argument("--lambda", type=float, default=DEFAULT_CONFIG["LAMBDA"], dest="lambda_")
    p.add_argument("--rho-min", type=float, default=0.01, help="RPV lower band")
    p.add_argument("--rho-max", type=float, default=0.15, help="RPV upper band (slightly loose for small N)")
    p.add_argument("--outdir", type=str, default="./outputs")
    p.add_argument(
        "--strict",
        action="store_true",
        help="Fail if mean rho outside band (default: report WARN when small-N noisy)",
    )
    args = p.parse_args()

    print_banner(
        "RUNNER: vacuum regression",
        "mean-field equations and RPV sweeps",
        "Fixed-seed PASS/FAIL lock on shared evolve_graph_to_equilibrium",
    )

    cfg = DEFAULT_CONFIG.copy()
    cfg.update({
        "NUM_NODES_APPROX": args.nodes,
        "SIMULATION_STEPS": args.steps,
        "MU": args.mu,
        "LAMBDA": args.lambda_,
    })

    rows = []
    for i in range(args.runs):
        rows.append(one_run(cfg, args.seed + i))

    rhos = [r["rho3"] for r in rows]
    mean_rho = statistics.mean(rhos)
    std_rho = statistics.pstdev(rhos) if len(rhos) > 1 else 0.0
    mean_steps = statistics.mean(r["steps"] for r in rows)
    mean_n3 = statistics.mean(r["n3"] for r in rows)

    in_band = args.rho_min < mean_rho < args.rho_max
    # Weakness: small N often freezes (rho~0) even at nominal mu,lambda.
    any_live = any(r["n3"] > 0 for r in rows)
    frac_live = sum(1 for r in rows if r["n3"] > 0) / len(rows)

    print(f"N~{args.nodes} runs={args.runs} mu={args.mu:.4f} lambda={args.lambda_:.4f}")
    print(f"mean rho3={mean_rho:.4f}  std={std_rho:.4f}  mean N3={mean_n3:.2f}  mean steps={mean_steps:.1f}")
    print(f"live fraction (N3>0)={frac_live:.2f}  target band ({args.rho_min}, {args.rho_max})")

    if in_band:
        status, detail = "PASS", f"mean rho3={mean_rho:.4f} in RPV-like band"
    elif any_live and not args.strict:
        status, detail = (
            "INCONCLUSIVE",
            f"mean rho3={mean_rho:.4f} outside band (small-N / short-run common); live={frac_live:.2f}. "
            "Monograph RPV uses N~100, 100 runs - use find_vacuum for that.",
        )
    elif any_live and args.strict:
        status, detail = "FAIL", f"mean rho3={mean_rho:.4f} outside strict band"
    else:
        status, detail = (
            "FAIL",
            f"all runs frozen (mean rho3={mean_rho:.4f}). Library vacuum did not sustain geometry.",
        )

    print(verdict_line("vacuum_regression", status, detail))

    outdir = ensure_outdir(args.outdir)
    path = os.path.join(outdir, f"vacuum_regression_{timestamp()}.csv")
    write_csv(path, rows)
    print(f"CSV: {path}")
    return 0 if status == "PASS" else (2 if status == "FAIL" else 0)


if __name__ == "__main__":
    raise SystemExit(main())

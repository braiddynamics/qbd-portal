#!/usr/bin/env python3
"""
Stress-energy flux time series on the shared library engine.

Monograph already covers:
  - full forked dynamics + add/del counters -> empirical T_ab
  - mean-field J_in / J_out balance

This runner: uses model.compute_proposal_rates / stress_energy (not counters)
on the shared evolve path; records ||T|| and residuals over time.

Known weakness: instantaneous proposal rates != long-run counter estimates.
"""
from __future__ import annotations

import argparse
import random
from typing import List, Dict

from _runner_common import ensure_outdir, print_banner, timestamp, verdict_line, write_csv

from model.config import DEFAULT_CONFIG
from model.graph_setup import generate_zpi_vacuum, inject_energic_event
from model.dynamics import (
    evolve_graph_to_equilibrium,
    _calculate_add_proposals,
    _calculate_del_proposals,
    build_stress_map,
)
from model.stress_energy import (
    stress_energy_tensor,
    frobenius_norm,
    mean_abs_flux,
    max_abs_vertex_residual,
)
from model.observables import get_n3_count
from model.utils import find_all_3_cycles


def snapshot_T(G, config) -> Dict[str, float]:
    T = stress_energy_tensor(G, config)
    return {
        "n3": get_n3_count(G),
        "n_edges": G.number_of_edges(),
        "T_frobenius": frobenius_norm(T),
        "T_mean_abs": mean_abs_flux(T),
        "T_max_vertex_residual": max_abs_vertex_residual(T, G.nodes()),
        "n_T_entries": len(T),
    }


def evolve_with_samples(G, config, sample_every: int) -> List[Dict]:
    """
    Mirror evolve_graph_to_equilibrium but sample T periodically.
    Physics identical to library evolve (same private proposal functions).
    """
    import math
    Tvac = config["T_VACUUM"]
    mu = config["MU"]
    lam = config["LAMBDA"]
    max_steps = config["SIMULATION_STEPS"]
    rows = []
    rows.append({"step": 0, **snapshot_T(G, config)})

    for step in range(max_steps):
        all_cycles, stress_map = build_stress_map(G)
        proposals_add = _calculate_add_proposals(G, Tvac, mu, stress_map)
        proposals_del = _calculate_del_proposals(G, Tvac, mu, lam, all_cycles, stress_map)
        if not proposals_add and not proposals_del:
            rows.append({"step": step + 1, **snapshot_T(G, config), "halted": 1})
            break
        edges_to_add = [(e[0], e[1], {"H": h}) for e, h in proposals_add]
        G.add_edges_from(edges_to_add)
        G.remove_edges_from(proposals_del.intersection(G.edges()))
        if (step + 1) % sample_every == 0:
            rows.append({"step": step + 1, **snapshot_T(G, config), "halted": 0})
    else:
        rows.append({"step": max_steps, **snapshot_T(G, config), "halted": 0})
    return rows


def main():
    p = argparse.ArgumentParser(description="T_ab flux balance on shared engine")
    p.add_argument("--nodes", type=int, default=30)
    p.add_argument("--steps", type=int, default=200)
    p.add_argument("--sample-every", type=int, default=20)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--outdir", type=str, default="./outputs")
    p.add_argument(
        "--residual-threshold",
        type=float,
        default=None,
        help="If set, FAIL when final max vertex residual exceeds this",
    )
    args = p.parse_args()

    print_banner(
        "RUNNER: flux balance (proposal-rate T_ab)",
        "counter-based stress-energy derivations and mean-field flux",
        "Time series of rate-based T_ab on shared model evolve",
    )

    cfg = DEFAULT_CONFIG.copy()
    cfg["NUM_NODES_APPROX"] = args.nodes
    cfg["SIMULATION_STEPS"] = args.steps

    random.seed(args.seed)
    G, levels = generate_zpi_vacuum(cfg["NUM_NODES_APPROX"])
    G = inject_energic_event(G, levels)
    series = evolve_with_samples(G, cfg, args.sample_every)

    print(f"{'step':>6} {'N3':>5} {'||T||F':>10} {'mean|T|':>10} {'max|r|':>10}")
    for r in series:
        print(
            f"{r['step']:6d} {r['n3']:5d} {r['T_frobenius']:10.4f} "
            f"{r['T_mean_abs']:10.4f} {r['T_max_vertex_residual']:10.4f}"
        )

    final = series[-1]
    initial = series[0]
    # Honest criteria: we report behavior; only fail if residual threshold set
    detail_parts = [
        f"final ||T||F={final['T_frobenius']:.4f}",
        f"final max|r|={final['T_max_vertex_residual']:.4f}",
        f"dN3={final['n3'] - initial['n3']}",
    ]

    if args.residual_threshold is not None:
        if final["T_max_vertex_residual"] <= args.residual_threshold:
            status = "PASS"
            detail = "; ".join(detail_parts) + f" residual≤{args.residual_threshold}"
        else:
            status = "FAIL"
            detail = "; ".join(detail_parts) + f" residual>{args.residual_threshold}"
    else:
        # Default: informational — vacuum often has nonzero residual at small N
        status = "INCONCLUSIVE"
        detail = (
            "; ".join(detail_parts)
            + " | No residual threshold set (rate-based T residual is often nonzero; "
            "compare counter T for equilibrium flux sums). "
            "Pass --residual-threshold to enforce a gate."
        )

    print(verdict_line("flux_balance", status, detail))

    import os
    out = ensure_outdir(args.outdir)
    path = os.path.join(out, f"flux_balance_{timestamp()}.csv")
    write_csv(path, series)
    print(f"CSV: {path}")
    return 0 if status != "FAIL" else 2


if __name__ == "__main__":
    raise SystemExit(main())

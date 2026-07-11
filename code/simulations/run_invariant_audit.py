#!/usr/bin/env python3
"""
Invariant audit during library evolution.

Monograph already covers:
  - Standalone PUC/AEC checks
  - Stabilizer algebra / syndrome tables (not on live evolve)
  - Unit tests for pre_check_aec / is_permissible

This runner: after evolve (and optionally mid-run snapshots), verify hard
graph invariants on the *shared* engine output.
"""
from __future__ import annotations

import argparse
import random
from typing import Dict, List, Tuple

from _runner_common import ensure_outdir, print_banner, timestamp, verdict_line, write_csv

from model.config import DEFAULT_CONFIG
from model.graph_setup import generate_zpi_vacuum, inject_energic_event
from model.dynamics import evolve_graph_to_equilibrium
from model.stabilizers import (
    hard_2cycle_projectors_satisfied,
    hard_projectors_satisfied,
    count_unsupported_chords,
)
from model.utils import find_all_3_cycles
from model.observables import get_n3_count


def audit_graph(G) -> Dict[str, object]:
    issues: List[str] = []
    # Hard: no 2-cycles
    two_ok = hard_2cycle_projectors_satisfied(G)
    if not two_ok:
        issues.append("2-cycle present")

    # Timestamps present on all edges
    missing_H = 0
    for u, v, data in G.edges(data=True):
        if "H" not in data:
            missing_H += 1
    if missing_H:
        issues.append(f"missing_H={missing_H}")

    # 3-cycle count consistency
    n3 = get_n3_count(G)
    n3_util = len(find_all_3_cycles(G))
    if n3 != n3_util:
        issues.append(f"n3_mismatch {n3}!={n3_util}")

    # Diagnostic (not critical): post-hoc "unsupported chord" count.
    # Micro-rule adds are always 2-path local; densification makes residual
    # locality ambiguous (see stabilizers.hard_locality_projectors_satisfied).
    unsupported = count_unsupported_chords(G)
    hard_ok = hard_projectors_satisfied(G)

    return {
        "two_cycle_ok": two_ok,
        "hard_ok": hard_ok,
        "unsupported_chords": unsupported,
        "missing_H": missing_H,
        "n3": n3,
        "n_nodes": G.number_of_nodes(),
        "n_edges": G.number_of_edges(),
        "issues": ";".join(issues) if issues else "",
        "ok_critical": two_ok and missing_H == 0 and n3 == n3_util,
    }


def main():
    p = argparse.ArgumentParser(description="Invariant audit on library evolve")
    p.add_argument("--nodes", type=int, default=40)
    p.add_argument("--steps", type=int, default=300)
    p.add_argument("--runs", type=int, default=8)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--outdir", type=str, default="./outputs")
    p.add_argument(
        "--require-locality",
        action="store_true",
        help="Also fail if locality hard-projector proxy fails (can be strict)",
    )
    args = p.parse_args()

    print_banner(
        "RUNNER: invariant audit",
        "PUC/AEC scripts, algebraic QECC, and unit tests",
        "Post-evolve hard invariants on shared model graphs",
    )

    cfg = DEFAULT_CONFIG.copy()
    cfg["NUM_NODES_APPROX"] = args.nodes
    cfg["SIMULATION_STEPS"] = args.steps

    rows = []
    critical_fails = 0
    locality_fails = 0

    for i in range(args.runs):
        random.seed(args.seed + i)
        G, levels = generate_zpi_vacuum(cfg["NUM_NODES_APPROX"])
        G = inject_energic_event(G, levels)
        Gf, steps = evolve_graph_to_equilibrium(G, cfg)
        a = audit_graph(Gf)
        a["seed"] = args.seed + i
        a["steps"] = steps
        rows.append(a)
        if not a["ok_critical"]:
            critical_fails += 1
        if not a["hard_ok"]:
            locality_fails += 1

    mean_unsup = sum(r["unsupported_chords"] for r in rows) / max(len(rows), 1)
    print(
        f"runs={args.runs} critical_fails={critical_fails} "
        f"strict_locality_fails={locality_fails} mean_unsupported_chords={mean_unsup:.1f}"
    )
    for r in rows:
        print(
            f"  seed={r['seed']} n3={r['n3']} two_ok={r['two_cycle_ok']} "
            f"unsupported_chords={r['unsupported_chords']} issues={r['issues'] or '-'}"
        )

    if critical_fails == 0 and (not args.require_locality or locality_fails == 0):
        status = "PASS"
        detail = (
            f"critical invariants OK (2-cycle/H/N3). "
            f"Post-hoc unsupported_chords mean={mean_unsup:.1f} "
            f"(diagnostic only: residual locality != insertion locality; "
            f"micro-rule still only proposes 2-path closes)."
        )
        if args.require_locality and locality_fails == 0:
            detail += " strict locality also OK."
    elif critical_fails == 0 and args.require_locality and locality_fails > 0:
        status, detail = (
            "FAIL",
            f"strict post-hoc locality failed {locality_fails}/{args.runs} "
            f"under --require-locality (mean unsupported_chords={mean_unsup:.1f}). "
            "This often fails after densification even when adds were local — known gap.",
        )
    else:
        status, detail = "FAIL", f"critical invariant failures: {critical_fails}/{args.runs}"

    print(verdict_line("invariant_audit", status, detail))

    out = ensure_outdir(args.outdir)
    import os
    path = os.path.join(out, f"invariant_audit_{timestamp()}.csv")
    # flatten issues for csv
    csv_rows = [{k: v for k, v in r.items()} for r in rows]
    write_csv(path, csv_rows)
    print(f"CSV: {path}")
    return 0 if status == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())

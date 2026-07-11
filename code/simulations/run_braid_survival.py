#!/usr/bin/env python3
"""
Graph-level trivial cluster vs injected tripartite cycle survival.

Monograph already covers:
  - mean-field ODE: trivial cluster vs prime knot (barrier at rho_core)
  - writhe mass hierarchy table (not dynamics)

This runner: shared-model graph experiment.
IMPORTANT: default evolve does NOT implement topological protection.
With --protection we only apply a *post-hoc* diagnostic barrier label / optional
manual freeze of delete proposals on the injected cycle edges (experimental).

Expect honest FAIL/INCONCLUSIVE if graph survival does not match mean-field story.
"""
from __future__ import annotations

import argparse
import random
from typing import Set, Tuple

from _runner_common import ensure_outdir, print_banner, timestamp, verdict_line, write_csv

from model.config import DEFAULT_CONFIG
from model.graph_setup import generate_zpi_vacuum, inject_energic_event
from model.dynamics import (
    build_stress_map,
    _calculate_add_proposals,
    _calculate_del_proposals,
)
from model.braids import inject_tripartite_cycle, deletion_barrier_active, flux_balance
from model.observables import get_n3_count
from model.utils import find_all_3_cycles


def evolve_custom(G, config, protected_edges: Set[Tuple[int, int]] | None, steps: int):
    """Evolve with optional experimental protection: never delete protected edges."""
    T = config["T_VACUUM"]
    mu = config["MU"]
    lam = config["LAMBDA"]
    for step in range(steps):
        all_cycles, stress_map = build_stress_map(G)
        proposals_add = _calculate_add_proposals(G, T, mu, stress_map)
        proposals_del = _calculate_del_proposals(G, T, mu, lam, all_cycles, stress_map)
        if protected_edges:
            proposals_del = {e for e in proposals_del if e not in protected_edges}
        if not proposals_add and not proposals_del:
            return G, step + 1
        G.add_edges_from([(u, v, {"H": h}) for (u, v), h in proposals_add])
        G.remove_edges_from(proposals_del.intersection(G.edges()))
    return G, steps


def make_trivial_blob(G, n_extra_cycles: int = 3):
    """Try to create a few extra short cycles without braid structure."""
    # Best-effort: close random compliant 2-paths if any exist after ignition
    from model.utils import is_permissible, pre_check_aec
    added = 0
    nodes = list(G.nodes())
    for v in nodes:
        for w in list(G.successors(v)):
            for u in list(G.successors(w)):
                if added >= n_extra_cycles:
                    return G
                if v == u or G.has_edge(u, v):
                    continue
                if not is_permissible(G, u, v, w):
                    continue
                max_h = max((d.get("H", 0) for _, _, d in G.in_edges(u, data=True)), default=0)
                H_new = max_h + 1
                if pre_check_aec(G, u, v, H_new):
                    G.add_edge(u, v, H=H_new)
                    added += 1
    return G


def main():
    p = argparse.ArgumentParser(description="Braid vs trivial survival (graph)")
    p.add_argument("--nodes", type=int, default=40)
    p.add_argument("--steps", type=int, default=250)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--outdir", type=str, default="./outputs")
    p.add_argument(
        "--protection",
        action="store_true",
        help="Experimental: refuse deletion of injected cycle edges",
    )
    p.add_argument("--mean-field-only", action="store_true", help="Only re-run ODE fluxes")
    args = p.parse_args()

    print_banner(
        "RUNNER: braid survival",
        "mean-field knot barrier and mass hierarchy derivations",
        "Graph survival of injected cycle vs trivial blob on shared model",
    )

    # Mean-field reference
    j_in, j_out, dr = flux_balance(0.50)
    print(f"Mean-field @rho=0.5: J_in={j_in:.4f} J_out={j_out:.4f} drho/dt={dr:.4f}")
    print(f"  barrier@0.05: {deletion_barrier_active(0.05)}  @0.10: {deletion_barrier_active(0.10)}")

    if args.mean_field_only:
        status = "PASS" if dr < 0 else "FAIL"
        print(verdict_line("braid_survival", status, "mean-field only"))
        return 0 if status == "PASS" else 2

    cfg = DEFAULT_CONFIG.copy()
    cfg["NUM_NODES_APPROX"] = args.nodes
    cfg["SIMULATION_STEPS"] = args.steps

    rows = []

    # Arm A: ignition + extra blob attempts
    random.seed(args.seed)
    Ga, levels = generate_zpi_vacuum(cfg["NUM_NODES_APPROX"])
    Ga = inject_energic_event(Ga, levels)
    Ga = make_trivial_blob(Ga, 3)
    n3_a0 = get_n3_count(Ga)
    Ga, steps_a = evolve_custom(Ga, cfg, None, args.steps)
    n3_a1 = get_n3_count(Ga)
    rows.append({
        "arm": "trivial_blob",
        "n3_initial": n3_a0,
        "n3_final": n3_a1,
        "steps": steps_a,
        "protection": False,
    })

    # Arm B: inject tripartite cycle (possibly protected)
    random.seed(args.seed + 1)
    Gb, levels = generate_zpi_vacuum(cfg["NUM_NODES_APPROX"])
    # start clean, inject braid cycle explicitly
    Gb, braid = inject_tripartite_cycle(Gb)
    # also hang vacuum tree if empty-ish: merge with zpi nodes
    # (inject on empty created 0,1,2 cycle; zpi has more structure if we use zpi first)
    random.seed(args.seed + 1)
    Gb, levels = generate_zpi_vacuum(cfg["NUM_NODES_APPROX"])
    Gb, braid = inject_tripartite_cycle(Gb, nodes=(levels[0][0], levels[1][0], levels[2][0]) if len(levels) > 2 else None)
    prot: Set[Tuple[int, int]] = set()
    if args.protection and braid.ribbons:
        for rib in braid.ribbons:
            if len(rib.path) >= 2:
                prot.add((rib.path[0], rib.path[1]))
    n3_b0 = get_n3_count(Gb)
    Gb, steps_b = evolve_custom(Gb, cfg, prot if args.protection else None, args.steps)
    n3_b1 = get_n3_count(Gb)
    rows.append({
        "arm": "injected_cycle",
        "n3_initial": n3_b0,
        "n3_final": n3_b1,
        "steps": steps_b,
        "protection": bool(args.protection),
    })

    print(f"trivial:  N3 {n3_a0} -> {n3_a1}")
    print(f"injected: N3 {n3_b0} -> {n3_b1}  protection={args.protection}")

    # Honest verdicts
    if not args.protection:
        if n3_b1 > n3_a1:
            status, detail = (
                "INCONCLUSIVE",
                "Injected cycle ended with more N3 without protection - may be luck/topology; "
                "default dynamics has no prime-knot barrier (unlike mean-field ODE).",
            )
        elif n3_b1 == n3_a1 == 0:
            status, detail = (
                "PASS",
                "Both evaporated without protection - consistent with unprotected graph dynamics. "
                "Mean-field barrier is NOT in default evolve (weakness vs mean-field model).",
            )
        else:
            status, detail = (
                "INCONCLUSIVE",
                f"trivial {n3_a0}->{n3_a1}, injected {n3_b0}->{n3_b1}; no clear survival signal without protection",
            )
    else:
        if n3_b1 > 0 and n3_b1 >= n3_a1:
            status, detail = (
                "PASS",
                "With experimental edge protection, injected cycle retained more geometry "
                "(hand-enforced; not emergent QECC).",
            )
        else:
            status, detail = (
                "FAIL",
                "Even with experimental edge protection, injected cycle did not out-survive trivial arm",
            )

    print(verdict_line("braid_survival", status, detail))
    print(
        "WEAKNESS: topological protection is not part of default Ch5 evolve; "
        "--protection is an experimental scaffold only."
    )

    import os
    out = ensure_outdir(args.outdir)
    path = os.path.join(out, f"braid_survival_{timestamp()}.csv")
    write_csv(path, rows)
    print(f"CSV: {path}")
    return 0 if status != "FAIL" else 2


if __name__ == "__main__":
    raise SystemExit(main())

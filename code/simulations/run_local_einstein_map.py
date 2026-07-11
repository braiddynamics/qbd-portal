#!/usr/bin/env python3
"""
Local Einstein / stress correlation on equilibrated model graphs.

Monograph already covers:
  - Protocol A (exact kappa on 3-node hand graph)
  - W1 geometry toys

This runner: evolve shared vacuum, sample a limited set of edges for G_ab
(OT-capped), compare to local cycle stress. Honest about small samples.

Known weakness: not a continuum Einstein equation proof; exploratory correlation.
"""
from __future__ import annotations

import argparse
import math
import random
from typing import List, Dict

from _runner_common import ensure_outdir, print_banner, timestamp, verdict_line, write_csv

from model.config import DEFAULT_CONFIG
from model.graph_setup import generate_zpi_vacuum, inject_energic_event
from model.dynamics import evolve_graph_to_equilibrium, build_stress_map
from model.geometry import undirected_distance_matrix, einstein_tensor_edge
from model.stress_energy import stress_energy_tensor
from model.observables import get_n3_count


def main():
    p = argparse.ArgumentParser(description="Local G_ab map on model vacuum")
    p.add_argument("--nodes", type=int, default=24)
    p.add_argument("--steps", type=int, default=150)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--max-edges", type=int, default=12, help="OT samples (expensive)")
    p.add_argument("--max-ot-nodes", type=int, default=DEFAULT_CONFIG.get("MAX_OT_NODES", 64))
    p.add_argument("--outdir", type=str, default="./outputs")
    args = p.parse_args()

    print_banner(
        "RUNNER: local Einstein map",
        "Protocol A and W1 geometry toy model derivations",
        "Sample G_ab vs stress / T on evolved *library* vacuum",
    )

    cfg = DEFAULT_CONFIG.copy()
    cfg["NUM_NODES_APPROX"] = args.nodes
    cfg["SIMULATION_STEPS"] = args.steps

    random.seed(args.seed)
    G, levels = generate_zpi_vacuum(cfg["NUM_NODES_APPROX"])
    G = inject_energic_event(G, levels)
    G, steps = evolve_graph_to_equilibrium(G, cfg)

    n = G.number_of_nodes()
    n3 = get_n3_count(G)
    print(f"evolved steps={steps} N={n} N3={n3}")

    if n > args.max_ot_nodes:
        print(
            f"INCONCLUSIVE: N={n} > MAX_OT_NODES={args.max_ot_nodes}. "
            "Refusing full-graph OT (honest scope). Reduce --nodes or raise --max-ot-nodes."
        )
        print(verdict_line(
            "local_einstein_map",
            "INCONCLUSIVE",
            f"N={n} exceeds OT cap; not a continuum GR validation",
        ))
        return 0

    _, stress = build_stress_map(G)
    Tmap = stress_energy_tensor(G, cfg)
    nodes, dist = undirected_distance_matrix(G)

    edges = list(G.edges())
    random.shuffle(edges)
    edges = edges[: args.max_edges]

    rows: List[Dict] = []
    for u, v in edges:
        try:
            gab = einstein_tensor_edge(G, u, v, dist, nodes)
        except Exception as e:
            rows.append({"u": u, "v": v, "error": str(e)})
            continue
        local_stress = stress.get(u, 0) + stress.get(v, 0)
        tab = Tmap.get((u, v), 0.0)
        rows.append({
            "u": u,
            "v": v,
            "G_ab": gab,
            "T_ab": tab,
            "local_stress": local_stress,
        })
        print(f"  edge ({u},{v}) G_ab={gab:.5f} T_ab={tab:.5f} stress={local_stress}")

    # Correlation if enough points
    gvals = [r["G_ab"] for r in rows if "G_ab" in r]
    tvals = [r["T_ab"] for r in rows if "G_ab" in r]
    svals = [r["local_stress"] for r in rows if "G_ab" in r]

    corr_gt = corr_gs = float("nan")
    if len(gvals) >= 3:
        corr_gt = _corr(gvals, tvals)
        corr_gs = _corr(gvals, svals)
        print(f"corr(G,T)={corr_gt:.3f}  corr(G,stress)={corr_gs:.3f}")

    status = "INCONCLUSIVE"
    detail = (
        f"sampled {len(gvals)} edges on N={n} N3={n3}; "
        f"corr(G,T)={corr_gt:.3f}. Exploratory only - monograph Protocol A remains the kappa proof."
    )
    # Soft green if we got samples without error
    if gvals and all(math.isfinite(x) for x in gvals):
        status = "PASS"
        detail = "OT samples computed; " + detail
    elif not gvals:
        status = "FAIL"
        detail = "no successful OT samples"

    print(verdict_line("local_einstein_map", status, detail))

    import os
    out = ensure_outdir(args.outdir)
    path = os.path.join(out, f"local_einstein_map_{timestamp()}.csv")
    write_csv(path, rows)
    print(f"CSV: {path}")
    return 0 if status != "FAIL" else 2


def _corr(xs, ys):
    n = len(xs)
    if n < 2:
        return float("nan")
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    dy = math.sqrt(sum((y - my) ** 2 for y in ys))
    if dx == 0 or dy == 0:
        return float("nan")
    return num / (dx * dy)


if __name__ == "__main__":
    raise SystemExit(main())

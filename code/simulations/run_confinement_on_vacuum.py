#!/usr/bin/env python3
"""
Confinement-style path-cost scaling on an evolved vacuum graph.

Monograph already covers:
  - linear V(L)=sigma*L on unit-weight 2D grid (sigma~1 by construction)

This runner: evolve library vacuum, take undirected residual, sample pairs at
graph distance L, measure shortest-path length vs L, fit sigma.

Known weakness: if vacuum is tree-like, paths are unique and "tension" is
combinatorial distance - not a QCD flux tube. Report INCONCLUSIVE if poor fit.
"""
from __future__ import annotations

import argparse
import math
import random
from collections import defaultdict
from typing import Dict, List, Tuple

import networkx as nx
import numpy as np

from _runner_common import ensure_outdir, print_banner, timestamp, verdict_line, write_csv

from model.config import DEFAULT_CONFIG
from model.graph_setup import generate_zpi_vacuum, inject_energic_event
from model.dynamics import evolve_graph_to_equilibrium
from model.observables import get_n3_count
from model.worldsheets import confinement_potential


def sample_distance_energy(U: nx.Graph, max_pairs_per_L: int = 20, max_L: int = 12):
    """For each distance L, sample pairs and record geodesic length (energy proxy)."""
    nodes = list(U.nodes())
    by_L: Dict[int, List[float]] = defaultdict(list)

    # Precompute distances from a sample of sources
    sources = random.sample(nodes, min(30, len(nodes)))
    for s in sources:
        lengths = nx.single_source_shortest_path_length(U, s, cutoff=max_L)
        bucket: Dict[int, List] = defaultdict(list)
        for t, d in lengths.items():
            if d >= 2:
                bucket[d].append(t)
        for L, targets in bucket.items():
            random.shuffle(targets)
            for t in targets[:max_pairs_per_L]:
                # unit weights ⇒ energy == distance
                by_L[L].append(float(L))

    separations = sorted(by_L.keys())
    mean_E = [float(np.mean(by_L[L])) for L in separations]
    return separations, mean_E, by_L


def main():
    p = argparse.ArgumentParser(description="Confinement proxy on vacuum graph")
    p.add_argument("--nodes", type=int, default=50)
    p.add_argument("--steps", type=int, default=200)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--outdir", type=str, default="./outputs")
    p.add_argument(
        "--also-grid",
        action="store_true",
        help="Also re-run unit-grid confinement (same as grid model / worldsheets)",
    )
    args = p.parse_args()

    print_banner(
        "RUNNER: confinement on vacuum",
        "unit-grid linear V(r) confinement potential",
        "Shortest-path scaling on evolved *library* vacuum undirected graph",
    )

    if args.also_grid:
        grid = confinement_potential([2, 4, 6, 8, 10])
        print(f"Grid reference: sigma={grid['sigma']:.4f} R^2={grid['r2']:.4f} (expect sigma~1)")

    cfg = DEFAULT_CONFIG.copy()
    cfg["NUM_NODES_APPROX"] = args.nodes
    cfg["SIMULATION_STEPS"] = args.steps

    random.seed(args.seed)
    G, levels = generate_zpi_vacuum(cfg["NUM_NODES_APPROX"])
    G = inject_energic_event(G, levels)
    G, steps = evolve_graph_to_equilibrium(G, cfg)
    n3 = get_n3_count(G)
    U = G.to_undirected()
    print(f"vacuum: steps={steps} N={U.number_of_nodes()} E={U.number_of_edges()} N3={n3}")

    if U.number_of_edges() == 0:
        print(verdict_line("confinement_vacuum", "FAIL", "empty undirected graph"))
        return 2

    seps, energies, _ = sample_distance_energy(U)
    if len(seps) < 3:
        print(verdict_line(
            "confinement_vacuum",
            "INCONCLUSIVE",
            "insufficient distance diversity (graph too small or fragmented)",
        ))
        return 0

    x = np.asarray(seps, dtype=float)
    y = np.asarray(energies, dtype=float)
    A = np.column_stack([x, np.ones_like(x)])
    coef, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
    sigma, intercept = float(coef[0]), float(coef[1])
    pred = sigma * x + intercept
    ss_res = float(np.sum((y - pred) ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0

    print(f"fit V ~ sigma*L+c: sigma={sigma:.4f} c={intercept:.4f} R^2={r2:.4f}")
    print("NOTE: unit edge weights => geodesic energy == L, so sigma->1 if sampling is clean.")
    print("This does NOT by itself prove QCD flux tubes (weakness vs full string claim).")

    rows = [{"L": int(L), "E_mean": float(E)} for L, E in zip(seps, energies)]
    rows.append({"L": -1, "E_mean": sigma, "note": "sigma_fit"})
    rows.append({"L": -2, "E_mean": r2, "note": "r2"})

    # Honest: PASS only if linear with σ near 1; else INCONCLUSIVE
    if r2 > 0.95 and abs(sigma - 1.0) < 0.15:
        status, detail = (
            "PASS",
            f"linear geodesic scaling sigma={sigma:.3f} R^2={r2:.3f} (combinatorial; see weakness note)",
        )
    else:
        status, detail = (
            "INCONCLUSIVE",
            f"sigma={sigma:.3f} R^2={r2:.3f} - not a clean linear tube signal on this vacuum",
        )

    print(verdict_line("confinement_vacuum", status, detail))

    import os
    out = ensure_outdir(args.outdir)
    path = os.path.join(out, f"confinement_vacuum_{timestamp()}.csv")
    write_csv(path, rows)
    print(f"CSV: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

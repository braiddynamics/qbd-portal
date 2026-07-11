#!/usr/bin/env python3
"""
Protocol A via model.geometry + optional library-graph smoke.

Monograph already covers:
  - Protocol A exact + Protocol B synthetic regression (standalone)
  - W1 / K on 3-node chain

This runner: re-run Protocol A through the *shared* geometry module (integration
check). Optional --on-vacuum samples one edge Einstein tensor on a model vacuum.
"""
from __future__ import annotations

import argparse
import math
import random

from _runner_common import ensure_outdir, print_banner, timestamp, verdict_line, write_csv

from model.config import DEFAULT_CONFIG
from model.geometry import protocol_a_coupling, affine_field_regression, einstein_tensor_edge
from model.graph_setup import generate_zpi_vacuum, inject_energic_event
from model.dynamics import evolve_graph_to_equilibrium


def main():
    p = argparse.ArgumentParser(description="Protocol A via model.geometry")
    p.add_argument("--outdir", type=str, default="./outputs")
    p.add_argument("--skip-protocol-b", action="store_true")
    p.add_argument(
        "--on-vacuum",
        action="store_true",
        help="Also compute G_ab on one edge of a small evolved vacuum (smoke only)",
    )
    p.add_argument("--nodes", type=int, default=25)
    p.add_argument("--steps", type=int, default=100)
    p.add_argument("--seed", type=int, default=42)
    args = p.parse_args()

    print_banner(
        "RUNNER: Protocol A (library geometry)",
        "Protocol A/B and W1 toy model derivations",
        "Same kappa check through model.geometry (+ optional vacuum smoke)",
    )

    a = protocol_a_coupling()
    print(
        f"Protocol A: G_vac={a['G_vac']:.6f} G_act={a['G_act']:.6f} "
        f"kappa={a['kappa']:.6f} target={a['kappa_target']:.6f}"
    )
    ok_a = math.isclose(a["kappa"], 1.0 / 3.0, abs_tol=1e-6)

    rows = [{"test": "protocol_a", **a, "pass": ok_a}]

    ok_b = True
    if not args.skip_protocol_b:
        b = affine_field_regression(a["G_vac"], n_samples=1500, seed=args.seed)
        ok_b = b["r2"] > 0.99 and abs(b["slope"] - 1.0 / 3.0) / (1.0 / 3.0) < 0.05
        print(
            f"Protocol B (synthetic): slope={b['slope']:.6f} intercept={b['intercept']:.6f} "
            f"R²={b['r2']:.6f}"
        )
        print(
            "  NOTE: Protocol B recovers kappa embedded in synthetic data - method check only."
        )
        rows.append({"test": "protocol_b_synthetic", **b, "pass": ok_b})

    vac_note = ""
    if args.on_vacuum:
        random.seed(args.seed)
        cfg = DEFAULT_CONFIG.copy()
        cfg["NUM_NODES_APPROX"] = args.nodes
        cfg["SIMULATION_STEPS"] = args.steps
        G, levels = generate_zpi_vacuum(cfg["NUM_NODES_APPROX"])
        G = inject_energic_event(G, levels)
        G, _ = evolve_graph_to_equilibrium(G, cfg)
        # pick first edge
        edges = list(G.edges())
        if edges:
            u, v = edges[0]
            try:
                gab = einstein_tensor_edge(G, u, v)
                vac_note = f"sample G_ab({u},{v})={gab:.6f} on evolved vacuum (smoke, not κ proof)"
                print(vac_note)
                rows.append({
                    "test": "vacuum_edge_smoke",
                    "u": u,
                    "v": v,
                    "G_ab": gab,
                    "pass": True,
                })
            except Exception as e:
                vac_note = f"vacuum OT failed: {e}"
                print(vac_note)
                rows.append({"test": "vacuum_edge_smoke", "pass": False, "error": str(e)})

    if ok_a and ok_b:
        status, detail = "PASS", "Protocol A kappa=1/3 via model.geometry" + (
            "; B synthetic OK" if not args.skip_protocol_b else ""
        )
    elif ok_a:
        status, detail = "FAIL", "Protocol A OK but synthetic B failed"
    else:
        status, detail = "FAIL", f"Protocol A kappa={a['kappa']} != 1/3"

    print(verdict_line("protocol_a_live", status, detail))
    if vac_note:
        print(f"  vacuum smoke: {vac_note}")

    import os
    out = ensure_outdir(args.outdir)
    path = os.path.join(out, f"protocol_a_live_{timestamp()}.csv")
    write_csv(path, rows)
    print(f"CSV: {path}")
    return 0 if status == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())

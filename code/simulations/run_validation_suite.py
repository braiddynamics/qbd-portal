#!/usr/bin/env python3
"""
Orchestrate library validation runners.

Executes all verification tests for the QBD shared library modules.
Exit code: 0 if no FAIL; 1 if any FAIL.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# (script, default extra args, notes)
RUNNERS = [
    ("run_vacuum_regression.py", [], "Ch5 library lock"),
    ("run_invariant_audit.py", [], "hard invariants post-evolve"),
    ("run_flux_balance.py", [], "rate-based T_ab time series"),
    ("run_protocol_a_live.py", [], "geometry Protocol A integration"),
    ("run_local_einstein_map.py", ["--nodes", "20", "--max-edges", "8"], "local G map"),
    ("run_braid_survival.py", [], "graph survival (honest)"),
    ("run_confinement_on_vacuum.py", ["--nodes", "40"], "vacuum geodesic scaling"),
]


def main():
    p = argparse.ArgumentParser(description="Run all library validation runners")
    p.add_argument("--outdir", type=str, default=os.path.join(HERE, "..", "outputs"))
    p.add_argument("--quick", action="store_true", help="Even smaller defaults via env-ish flags")
    p.add_argument("--only", type=str, nargs="*", help="Substring filter on script names")
    args = p.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    results = []

    print("=" * 78)
    print("QBD LIBRARY VALIDATION SUITE")
    print("Monograph standalone scripts are NOT executed here (by design).")
    print("See agent-readme.md for simulations monograph coverage cross-map.")
    print("=" * 78)

    for script, extra, note in RUNNERS:
        if args.only and not any(s in script for s in args.only):
            continue
        path = os.path.join(HERE, script)
        cmd = [sys.executable, path, "--outdir", args.outdir] + extra
        if args.quick and script == "run_vacuum_regression.py":
            cmd += ["--nodes", "25", "--steps", "150", "--runs", "6"]
        if args.quick and script == "run_flux_balance.py":
            cmd += ["--nodes", "20", "--steps", "80", "--sample-every", "20"]
        print("\n" + "#" * 78)
        print(f">>> {script}  ({note})")
        print("#" * 78)
        proc = subprocess.run(cmd, cwd=HERE)
        # Child uses 2 for FAIL, 0 for PASS/INCONCLUSIVE
        status = "FAIL" if proc.returncode == 2 else ("OK" if proc.returncode == 0 else f"exit={proc.returncode}")
        results.append((script, status, proc.returncode))

    print("\n" + "=" * 78)
    print("SUITE SUMMARY")
    print("=" * 78)
    fails = 0
    for script, status, code in results:
        print(f"  {status:12} {script}")
        if code == 2:
            fails += 1
    print("-" * 78)
    print(f"Failures (FAIL verdict): {fails}/{len(results)}")
    print("INCONCLUSIVE is allowed — it surfaces weaknesses rather than hiding them.")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())

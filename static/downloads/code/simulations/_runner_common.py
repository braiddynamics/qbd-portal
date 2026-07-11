"""Shared helpers for library test runners."""
from __future__ import annotations

import csv
import os
import sys
import time
from typing import Any, Dict, List, Optional

# Ensure code/ is on path when launched from simulations/
_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)


def ensure_outdir(path: str) -> str:
    os.makedirs(path, exist_ok=True)
    return path


def timestamp() -> str:
    return time.strftime("%Y%m%d-%H%M%S")


def write_csv(path: str, rows: List[Dict[str, Any]], fieldnames: Optional[List[str]] = None) -> None:
    if not rows:
        with open(path, "w", newline="", encoding="utf-8") as f:
            f.write("# empty results\n")
        return
    fields = fieldnames or list(rows[0].keys())
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def verdict_line(name: str, status: str, detail: str) -> str:
    return f"[{status:12}] {name}: {detail}"


def print_banner(title: str, covered: str, gap: str) -> None:
    print("=" * 78)
    print(title)
    print("-" * 78)
    print(f"Monograph coverage (already exists): {covered}")
    print(f"Library gap this runner targets:     {gap}")
    print("=" * 78)

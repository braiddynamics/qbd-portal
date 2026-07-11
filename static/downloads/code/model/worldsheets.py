# /model/worldsheets.py
"""
String / worldsheet limit helpers.

Provides Nambu-Goto discrete area proxies, linear confinement potential
checks on grid graphs, and left/right critical-dimension mode counting.
"""
from __future__ import annotations

from typing import Dict, Hashable, Iterable, List, Optional, Sequence, Tuple

import networkx as nx
import numpy as np


def shortest_path_energy(
    G: nx.Graph,
    source: Hashable,
    sink: Hashable,
    weight: str = "weight",
) -> float:
    """Minimal action between defects (Nambu–Goto discrete proxy)."""
    return float(nx.shortest_path_length(G, source, sink, weight=weight))


def confinement_potential(
    separations: Optional[Sequence[int]] = None,
    grid_padding: int = 10,
) -> Dict[str, object]:
    """
    Linear confinement check on a weighted 2D grid vacuum.

    V(L) ≈ σ L + V0 with σ ≈ 1 for unit edge weights (flux-tube tension).
    """
    if separations is None:
        separations = [2, 4, 6, 8, 10, 12, 14, 20, 30]

    energies: List[float] = []
    for L in separations:
        grid_size = int(L) + grid_padding
        G = nx.grid_2d_graph(grid_size, grid_size)
        for u, v in G.edges():
            G[u][v]["weight"] = 1.0
        source = (grid_size // 2, 2)
        sink = (grid_size // 2, 2 + int(L))
        energies.append(shortest_path_energy(G, source, sink, weight="weight"))

    x = np.asarray(separations, dtype=float)
    y = np.asarray(energies, dtype=float)
    # Linear least squares: y = sigma * x + c
    A = np.column_stack([x, np.ones_like(x)])
    coef, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
    sigma, intercept = float(coef[0]), float(coef[1])
    pred = sigma * x + intercept
    ss_res = float(np.sum((y - pred) ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0

    return {
        "separations": list(separations),
        "energies": energies,
        "sigma": sigma,
        "intercept": intercept,
        "r2": r2,
    }


def worldsheet_area_from_edge_counts(active_updates_per_tick: Sequence[int]) -> int:
    """
    Discrete worldsheet area ≈ total active rewrite events along a braid history.
    """
    return int(sum(int(x) for x in active_updates_per_tick))


def causal_tube_nodes(
    snapshots: Sequence[nx.DiGraph],
    core_nodes: Iterable[Hashable],
) -> set:
    """
    Union of core defect nodes across history snapshots (tube skeleton).
    """
    core = set(core_nodes)
    tube = set()
    for G in snapshots:
        for n in core:
            if n in G:
                tube.add(n)
                tube.update(G.successors(n))
                tube.update(G.predecessors(n))
    return tube


def heterotic_mode_count(
    dim_octonion: int = 8,
    n_strands_L: int = 3,
    n_strands_R: int = 1,
) -> Dict[str, float]:
    """
    Critical dimension / ZPE algebra for heterotic left/right sectors.

    Left:  3 × 8 + 2 = 26 bosonic
    Right: 1 × 8 + 2 = 10 super
    """
    D_trans_L = n_strands_L * dim_octonion
    D_total_L = D_trans_L + 2
    D_trans_R = n_strands_R * dim_octonion
    D_total_R = D_trans_R + 2

    E_vac_L = D_trans_L * (-1.0 / 24.0)
    E_vac_R = D_trans_R * (-1.0 / 24.0) + D_trans_R * (1.0 / 24.0)

    return {
        "D_transverse_L": float(D_trans_L),
        "D_total_L": float(D_total_L),
        "D_transverse_R": float(D_trans_R),
        "D_total_R": float(D_total_R),
        "target_D_L": 26.0,
        "target_D_R": 10.0,
        "anomaly_L": float(D_total_L - 26),
        "anomaly_R": float(D_total_R - 10),
        "E_vac_L": float(E_vac_L),
        "E_vac_R": float(E_vac_R),
        "algebra_closed": (D_total_L == 26 and D_total_R == 10 and abs(E_vac_R) < 1e-12),
    }


def t_duality_mass_squared(n: int, w: int, R: float) -> float:
    """
    Closed-string spectral term M^2 = (n/R)^2 + (w R)^2 (unit α' conventions).
    """
    if R <= 0:
        raise ValueError("R must be positive")
    return (n / R) ** 2 + (w * R) ** 2


def t_duality_spectrum_invariant(n: int, w: int, R: float) -> bool:
    """
    T-duality: spectrum at R with (n,w) matches spectrum at 1/R with (w,n).
    """
    m1 = t_duality_mass_squared(n, w, R)
    m2 = t_duality_mass_squared(w, n, 1.0 / R)
    return abs(m1 - m2) < 1e-10

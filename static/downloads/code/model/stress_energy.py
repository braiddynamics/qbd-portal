# /model/stress_energy.py
"""
Discrete stress-energy tensor T_ab from micro-rule proposal rates.

Calculates edge stress-energy T_ab = P_add(a,b) - P_del(a,b) and vertex
residuals to analyze local conservation laws.
"""
from __future__ import annotations

from typing import Dict, Tuple, Iterable

import networkx as nx
import numpy as np

from model.dynamics import compute_proposal_rates

Edge = Tuple[int, int]
RateMap = Dict[Edge, float]
TensorMap = Dict[Edge, float]


def stress_energy_tensor(G: nx.DiGraph, config: dict) -> TensorMap:
    """
    Build the discrete stress-energy map T_ab for the current graph.

    For each directed pair that participates in either an add or delete
    rate, T_ab = P_add - P_del. Reverse orientations are not filled here;
    use antisymmetrize_tensor if a skew flow matrix is required.
    """
    p_add, p_del = compute_proposal_rates(G, config)
    keys = set(p_add.keys()) | set(p_del.keys())
    return {
        e: p_add.get(e, 0.0) - p_del.get(e, 0.0)
        for e in keys
    }


def antisymmetrize_tensor(T: TensorMap) -> TensorMap:
    """
    Enforce T_ba = -T_ab as a directed flow matrix.

    Only material edges (those already present with nonzero T_ab) generate
    reverse algebraic counterparts when the reverse key is absent.
    """
    out: TensorMap = dict(T)
    for (a, b), val in list(T.items()):
        rev = (b, a)
        if rev not in out:
            out[rev] = -val
        # If both exist, leave measured values; caller may validate skew.
    return out


def vertex_flux_residuals(T: TensorMap, nodes: Iterable[int]) -> Dict[int, float]:
    """
    Local flux residual r(v) = sum_b T_vb + sum_a T_av.

    At homeostatic equilibrium the continuum limit expects near-zero
    residuals (discrete continuity / Bianchi proxy).
    """
    residuals = {int(v): 0.0 for v in nodes}
    for (a, b), val in T.items():
        if a in residuals:
            residuals[a] += val
        if b in residuals:
            residuals[b] += val
    return residuals


def frobenius_norm(T: TensorMap) -> float:
    """||T||_F = sqrt(sum T_ab^2)."""
    if not T:
        return 0.0
    return float(np.sqrt(sum(v * v for v in T.values())))


def mean_abs_flux(T: TensorMap) -> float:
    """Mean absolute entry of T (0 if empty)."""
    if not T:
        return 0.0
    return float(np.mean([abs(v) for v in T.values()]))


def max_abs_vertex_residual(T: TensorMap, nodes: Iterable[int]) -> float:
    """max_v |r(v)| over the vertex flux residuals."""
    residuals = vertex_flux_residuals(T, nodes)
    if not residuals:
        return 0.0
    return float(max(abs(r) for r in residuals.values()))

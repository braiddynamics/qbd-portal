# /model/geometry.py
"""
Discrete geometry: lazy causal measures, Wasserstein-1, Einstein tensor.

G_ab = (1/2) * K_ab with K_ab = 1 - W_1(mu_a, mu_b).
Protocol A: exact coupling kappa = dG/dT = 1/3 on the 3-node toy model.
"""
from __future__ import annotations

from typing import Dict, Hashable, Mapping, Optional, Tuple, List

import math
import networkx as nx
import numpy as np
from scipy.optimize import linprog


def lazy_mu(
    u: Hashable,
    G: nx.DiGraph,
    alpha: float = 1.0 / 3.0,
    beta: float = 1.0 / 3.0,
) -> Dict[Hashable, float]:
    """
    Lazy causal measure mu_u.

    Distributes probability mass over past, present, and future with
    re-absorption at vacuum boundaries (empty in/out-neighborhoods).
    """
    N_plus = list(G.successors(u))
    N_minus = list(G.predecessors(u))
    n_plus = len(N_plus)
    n_minus = len(N_minus)

    mu: Dict[Hashable, float] = {u: alpha}

    if n_plus == 0:
        mu[u] = mu.get(u, 0.0) + beta
    else:
        share = beta / n_plus
        for w in N_plus:
            mu[w] = mu.get(w, 0.0) + share

    if n_minus == 0:
        mu[u] = mu.get(u, 0.0) + beta
    else:
        share = beta / n_minus
        for w in N_minus:
            mu[w] = mu.get(w, 0.0) + share

    return mu


def undirected_distance_matrix(G: nx.DiGraph) -> Tuple[List[Hashable], np.ndarray]:
    """
    Shortest-path distance matrix on the underlying undirected graph.
    Unreachable pairs receive a large finite penalty (graph diameter bound).
    """
    nodes = list(G.nodes())
    n = len(nodes)
    if n == 0:
        return nodes, np.zeros((0, 0))

    U = G.to_undirected()
    dist = np.zeros((n, n), dtype=float)
    # Diameter-scale penalty for disconnected components.
    penalty = max(n, 1)

    for i, a in enumerate(nodes):
        lengths = nx.single_source_shortest_path_length(U, a)
        for j, b in enumerate(nodes):
            dist[i, j] = float(lengths.get(b, penalty))
    return nodes, dist


def wasserstein1(
    mu1: Mapping[Hashable, float],
    mu2: Mapping[Hashable, float],
    dist_matrix: np.ndarray,
    nodes: List[Hashable],
) -> float:
    """
    Exact 1-Wasserstein transport cost via linear programming.

    Marginals are taken on the ordered `nodes` list; missing mass entries
    default to 0. Requires total mass equality (lazy measures conserve mass).
    """
    n = len(nodes)
    if n == 0:
        return 0.0

    c = dist_matrix.reshape(-1)
    A_eq = np.zeros((2 * n, n * n))
    b_eq = np.zeros(2 * n)

    for i in range(n):
        for j in range(n):
            A_eq[i, i * n + j] = 1.0
        b_eq[i] = float(mu1.get(nodes[i], 0.0))

    for j in range(n):
        for i in range(n):
            A_eq[n + j, i * n + j] = 1.0
        b_eq[n + j] = float(mu2.get(nodes[j], 0.0))

    # Numerical mass fix: renormalize tiny drift.
    m1, m2 = b_eq[:n].sum(), b_eq[n:].sum()
    if m1 <= 0 or m2 <= 0:
        return 0.0
    if not math.isclose(m1, m2, rel_tol=1e-9, abs_tol=1e-12):
        b_eq[n:] *= m1 / m2

    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=(0, None), method="highs")
    if not res.success:
        raise RuntimeError(f"W1 transport failed: {res.message}")
    return float(res.fun)


def discrete_curvature(
    G: nx.DiGraph,
    u: Hashable,
    v: Hashable,
    dist_matrix: Optional[np.ndarray] = None,
    nodes: Optional[List[Hashable]] = None,
    alpha: float = 1.0 / 3.0,
    beta: float = 1.0 / 3.0,
) -> float:
    """
    K(u,v) = 1 - W_1(μ_u, μ_v).
    """
    if nodes is None or dist_matrix is None:
        nodes, dist_matrix = undirected_distance_matrix(G)
    mu_u = lazy_mu(u, G, alpha=alpha, beta=beta)
    mu_v = lazy_mu(v, G, alpha=alpha, beta=beta)
    w1 = wasserstein1(mu_u, mu_v, dist_matrix, nodes)
    return 1.0 - w1


def einstein_tensor_edge(
    G: nx.DiGraph,
    u: Hashable,
    v: Hashable,
    dist_matrix: Optional[np.ndarray] = None,
    nodes: Optional[List[Hashable]] = None,
    alpha: float = 1.0 / 3.0,
    beta: float = 1.0 / 3.0,
) -> float:
    """
    Discrete Einstein tensor on edge (u,v): G_ab = (1/2) K_ab.
    """
    K = discrete_curvature(G, u, v, dist_matrix, nodes, alpha, beta)
    return 0.5 * K


def protocol_a_coupling(
    alpha: float = 1.0 / 3.0,
    beta: float = 1.0 / 3.0,
) -> Dict[str, float]:
    """
    Protocol A: 3-node chain vs closed cycle.

    Vacuum G0: 0->1->2. Active G1: 0->1->2->0 with dT = 1.
    Returns measured kappa = dG / dT and intermediate curvatures.
    Target: kappa = 1/3.
    """
    # Fixed background metric as in the monograph verification suite.
    nodes = [0, 1, 2]
    d_mat = np.array(
        [
            [0.0, 1.0, 2.0],
            [1.0, 0.0, 1.0],
            [2.0, 1.0, 0.0],
        ],
        dtype=float,
    )

    G0 = nx.DiGraph([(0, 1), (1, 2)])
    G1 = nx.DiGraph([(0, 1), (1, 2), (2, 0)])

    G_vac = einstein_tensor_edge(G0, 0, 1, d_mat, nodes, alpha, beta)
    G_act = einstein_tensor_edge(G1, 0, 1, d_mat, nodes, alpha, beta)
    delta_G = G_act - G_vac
    delta_T = 1.0
    kappa = delta_G / delta_T

    return {
        "G_vac": G_vac,
        "G_act": G_act,
        "delta_G": delta_G,
        "delta_T": delta_T,
        "kappa": kappa,
        "kappa_target": 1.0 / 3.0,
    }


def affine_field_regression(
    G_vac: float,
    n_samples: int = 1000,
    lambda_vac: float = 0.015625,
    kappa_theory: float = 1.0 / 3.0,
    seed: int = 42,
) -> Dict[str, float]:
    """
    Protocol B: synthetic affine regression G = kappa T + G_vac under vacuum noise.
    """
    rng = np.random.default_rng(seed)
    T_signal = rng.exponential(scale=1.0, size=n_samples)
    T_noise = rng.normal(0.0, np.sqrt(lambda_vac), n_samples)
    T_data = T_signal + T_noise
    G_noise = rng.normal(0.0, lambda_vac, n_samples)
    G_data = kappa_theory * T_data + G_vac + G_noise

    # Simple least-squares: G ~ a T + b
    A = np.column_stack([T_data, np.ones_like(T_data)])
    coef, _, _, _ = np.linalg.lstsq(A, G_data, rcond=None)
    slope, intercept = float(coef[0]), float(coef[1])
    pred = slope * T_data + intercept
    ss_res = float(np.sum((G_data - pred) ** 2))
    ss_tot = float(np.sum((G_data - np.mean(G_data)) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0

    return {
        "slope": slope,
        "intercept": intercept,
        "r2": r2,
        "kappa_theory": kappa_theory,
        "G_vac_theory": G_vac,
        "lambda_vac": lambda_vac,
    }

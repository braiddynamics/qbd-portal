# tests/test_geometry.py
import math
import os
import sys

import networkx as nx
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from model.geometry import (
    lazy_mu,
    undirected_distance_matrix,
    wasserstein1,
    discrete_curvature,
    einstein_tensor_edge,
    protocol_a_coupling,
    affine_field_regression,
)


def test_lazy_mu_mass_conservation_interior():
    G = nx.DiGraph([(0, 1), (1, 2)])
    mu = lazy_mu(1, G)
    assert math.isclose(sum(mu.values()), 1.0, abs_tol=1e-12)


def test_lazy_mu_boundary_reabsorption():
    G = nx.DiGraph([(0, 1), (1, 2)])
    mu0 = lazy_mu(0, G)  # no past
    assert math.isclose(sum(mu0.values()), 1.0, abs_tol=1e-12)
    # Past β reabsorbed into self at root
    assert mu0[0] >= 1.0 / 3.0


def test_protocol_a_kappa_is_one_third():
    result = protocol_a_coupling()
    assert math.isclose(result["kappa"], 1.0 / 3.0, abs_tol=1e-6), result
    assert math.isclose(result["kappa_target"], 1.0 / 3.0)


def test_einstein_tensor_is_half_curvature():
    G = nx.DiGraph([(0, 1), (1, 2)])
    nodes, d = undirected_distance_matrix(G)
    K = discrete_curvature(G, 0, 1, d, nodes)
    Gab = einstein_tensor_edge(G, 0, 1, d, nodes)
    assert math.isclose(Gab, 0.5 * K, abs_tol=1e-12)


def test_wasserstein_chain_matches_script():
    """Reproduce §11.2.7.2 toy: W1 ≈ 2/3, K ≈ 1/3 on A–B of 0→1→2."""
    G = nx.DiGraph([(0, 1), (1, 2)])
    nodes = [0, 1, 2]
    dist = np_array = __import__("numpy").array(
        [[0, 1, 2], [1, 0, 1], [2, 1, 0]], dtype=float
    )
    mu_A = lazy_mu(0, G)
    mu_B = lazy_mu(1, G)
    w1 = wasserstein1(mu_A, mu_B, dist, nodes)
    assert math.isclose(w1, 2.0 / 3.0, abs_tol=1e-6)


def test_affine_regression_recovers_kappa():
    proto = protocol_a_coupling()
    reg = affine_field_regression(proto["G_vac"], n_samples=2000, seed=0)
    assert reg["r2"] > 0.99
    assert abs(reg["slope"] - (1.0 / 3.0)) / (1.0 / 3.0) < 0.05

# tests/test_stress_energy.py
import math
import os
import sys

import networkx as nx
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from model.config import DEFAULT_CONFIG
from model.dynamics import compute_proposal_rates, build_stress_map
from model.stress_energy import (
    stress_energy_tensor,
    antisymmetrize_tensor,
    vertex_flux_residuals,
    frobenius_norm,
    mean_abs_flux,
    max_abs_vertex_residual,
)


@pytest.fixture
def basic_config():
    cfg = DEFAULT_CONFIG.copy()
    cfg["MU"] = 0.0
    cfg["LAMBDA"] = 0.0
    cfg["T_VACUUM"] = math.log(2)
    return cfg


def test_compute_proposal_rates_on_open_2path(basic_config):
    """Compliant 2-path with μ=0 has P_add = 1 on the closing edge."""
    G = nx.DiGraph([(0, 1, {"H": 0}), (1, 2, {"H": 0})])
    p_add, p_del = compute_proposal_rates(G, basic_config)
    assert (2, 0) in p_add
    assert math.isclose(p_add[(2, 0)], 1.0)
    assert p_del == {} or all(v >= 0 for v in p_del.values())


def test_compute_del_rates_on_cycle(basic_config):
    """Isolated 3-cycle with μ=λ=0: Q_del = 1/2 shared over 3 edges."""
    G = nx.DiGraph([
        (0, 1, {"H": 1}),
        (1, 2, {"H": 2}),
        (2, 0, {"H": 3}),
    ])
    p_add, p_del = compute_proposal_rates(G, basic_config)
    # Each edge gets Q/3 = 0.5/3
    assert len(p_del) == 3
    for e, rate in p_del.items():
        assert math.isclose(rate, 0.5 / 3.0, rel_tol=1e-9)


def test_stress_energy_add_minus_del(basic_config):
    G = nx.DiGraph([(0, 1, {"H": 0}), (1, 2, {"H": 0})])
    T = stress_energy_tensor(G, basic_config)
    assert (2, 0) in T
    assert math.isclose(T[(2, 0)], 1.0)


def test_antisymmetrize_adds_reverse():
    T = {(0, 1): 0.5}
    skew = antisymmetrize_tensor(T)
    assert skew[(0, 1)] == 0.5
    assert skew[(1, 0)] == -0.5


def test_vertex_flux_and_norms(basic_config):
    G = nx.DiGraph([(0, 1, {"H": 0}), (1, 2, {"H": 0})])
    T = stress_energy_tensor(G, basic_config)
    residuals = vertex_flux_residuals(T, G.nodes())
    assert set(residuals.keys()) == set(G.nodes())
    assert frobenius_norm(T) >= 0.0
    assert mean_abs_flux(T) >= 0.0
    assert max_abs_vertex_residual(T, G.nodes()) >= 0.0


def test_build_stress_map_counts_cycles():
    G = nx.DiGraph([(0, 1), (1, 2), (2, 0)])
    cycles, stress = build_stress_map(G)
    assert len(cycles) == 1
    assert stress[0] == 1 and stress[1] == 1 and stress[2] == 1

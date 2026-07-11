# tests/test_worldsheets.py
import os
import sys

import networkx as nx
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from model.worldsheets import (
    confinement_potential,
    worldsheet_area_from_edge_counts,
    causal_tube_nodes,
    heterotic_mode_count,
    t_duality_mass_squared,
    t_duality_spectrum_invariant,
)


def test_confinement_is_linear_unit_tension():
    result = confinement_potential(separations=[2, 4, 6, 8, 10])
    assert abs(result["sigma"] - 1.0) < 1e-9
    assert result["r2"] > 0.999


def test_worldsheet_area_sums_updates():
    assert worldsheet_area_from_edge_counts([1, 2, 3, 0]) == 6


def test_causal_tube_nodes_union():
    G0 = nx.DiGraph([(0, 1), (1, 2)])
    G1 = nx.DiGraph([(0, 1), (1, 2), (2, 3)])
    tube = causal_tube_nodes([G0, G1], core_nodes=[1])
    assert 1 in tube
    assert 0 in tube or 2 in tube


def test_heterotic_algebra_closed():
    h = heterotic_mode_count()
    assert h["D_total_L"] == 26
    assert h["D_total_R"] == 10
    assert h["anomaly_L"] == 0
    assert h["anomaly_R"] == 0
    assert abs(h["E_vac_R"]) < 1e-12
    assert h["algebra_closed"] is True
    assert abs(h["E_vac_L"] - (-1.0)) < 1e-12


def test_t_duality_invariance():
    R = 1.5
    assert t_duality_spectrum_invariant(2, 3, R)
    m1 = t_duality_mass_squared(2, 3, R)
    m2 = t_duality_mass_squared(3, 2, 1.0 / R)
    assert abs(m1 - m2) < 1e-10


def test_t_duality_rejects_nonpositive_radius():
    with pytest.raises(ValueError):
        t_duality_mass_squared(1, 1, 0.0)

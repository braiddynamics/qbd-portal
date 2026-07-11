# tests/test_braids.py
import os
import sys

import networkx as nx
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from model.braids import (
    lepton_config,
    d_type_config,
    u_type_config,
    net_complexity,
    topological_mass,
    mass_hierarchy_table,
    inject_tripartite_cycle,
    deletion_barrier_active,
    flux_balance,
    su2_local_dof_count,
    STANDARD_MODEL_WRITHE,
    KAPPA_M_DEFAULT,
)
from model.utils import find_all_3_cycles


def test_electron_net_complexity_is_three():
    cfg = lepton_config(1, "Electron")
    assert net_complexity(cfg) == 3.0
    assert abs(topological_mass(cfg) - 0.511) < 1e-9


def test_family_complexity_formulas():
    assert net_complexity(lepton_config(2)) == 3 * 4
    assert net_complexity(d_type_config(3)) == 9
    assert net_complexity(u_type_config(4)) == 2 * 16 - 4


def test_mass_hierarchy_table_has_nine_fermions():
    rows = mass_hierarchy_table()
    assert len(rows) == 9
    names = {r["name"] for r in rows}
    assert "Electron" in names and "Top" in names
    # Electron exact by construction
    e = next(r for r in rows if r["name"] == "Electron")
    assert e["delta_pct"] < 1e-6


def test_sm_writhe_dict_complete():
    assert set(STANDARD_MODEL_WRITHE.keys()) == {
        "Electron", "Muon", "Tau",
        "Down", "Strange", "Bottom",
        "Up", "Charm", "Top",
    }


def test_inject_tripartite_cycle_creates_one_3cycle():
    G = nx.DiGraph()
    G, braid = inject_tripartite_cycle(G)
    cycles = find_all_3_cycles(G)
    assert len(cycles) == 1
    assert braid.config.family == "lepton"
    assert net_complexity(braid.config) == 3.0


def test_deletion_barrier_threshold():
    assert deletion_barrier_active(0.05, rho_core=0.082) is True
    assert deletion_barrier_active(0.10, rho_core=0.082) is False


def test_flux_balance_high_density_decays():
    j_in, j_out, dr = flux_balance(0.50)
    assert j_out > j_in
    assert dr < 0


def test_su2_local_dof_is_seven():
    assert su2_local_dof_count() == 7


def test_kappa_m_anchor():
    assert abs(KAPPA_M_DEFAULT - 0.511 / 3.0) < 1e-12

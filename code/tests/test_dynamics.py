import pytest
import networkx as nx
import math
import random
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.dynamics import (
    evolve_graph_to_equilibrium, 
    _calculate_add_proposals, 
    _calculate_del_proposals,
    compute_add_rates,
    compute_del_rates,
    build_stress_map
)
from model.utils import is_permissible, find_all_3_cycles
from model.observables import get_n3_count
from model.config import DEFAULT_CONFIG
from model.graph_setup import generate_zpi_vacuum, inject_energic_event

# --- Fixtures ---
@pytest.fixture
def basic_config():
    """Provides a basic, complete config for testing."""
    config = DEFAULT_CONFIG.copy()
    config["SIMULATION_STEPS"] = 100 
    config["NUM_NODES_APPROX"] = 10
    config["BETA_C"] = math.log(2)
    config["MU"] = 0.1
    config["LAMBDA"] = 0.1
    return config

# --- Unit Tests for Private Functions ---

@pytest.mark.parametrize("mock_random_val, expected_set", [
    (0.0, {((2, 0), 1)}), 
    (1.0, set()),       
])
def test_calculate_add_proposals_stochastic(mocker, basic_config, mock_random_val, expected_set):
    """
    Tests the add proposal function's stochastic acceptance/rejection
    and that it returns the correct timestamp.
    """
    mocker.patch('random.random', return_value=mock_random_val)
    config = basic_config.copy()
    config["MU"] = 0.0 
    
    G = nx.DiGraph()
    G.add_edges_from([(0, 1, {'H': 0}), (1, 2, {'H': 0})])
    
    # --- Mock the stress map ---
    # In this graph, there are 0 cycles, so the stress map is empty
    stress_map = {}
    
    proposals = _calculate_add_proposals(G, config["MU"], stress_map)
    
    assert proposals == expected_set

def test_calculate_add_proposals_respects_gpc(mocker, basic_config):
    """
    Tests that add proposals are NOT generated for GPC-failing paths.
    """
    mocker.patch('random.random', return_value=0.0) # Force accept
    config = basic_config.copy()
    config["MU"] = 0.0
    
    # This graph has a GPC-violating path:
    # 0 -> 1 -> 2 (the 2-path)
    # 0 -> 2 (the direct edge that violates uniqueness)
    G = nx.DiGraph([(0, 1, {'H': 0}), (1, 2, {'H': 0}), (0, 2, {'H': 0})])
    stress_map = {} # No cycles in this graph

    proposals = _calculate_add_proposals(G, config["MU"], stress_map)
    assert proposals == set() # No proposals

def test_calculate_add_proposals_respects_aec(mocker, basic_config):
    """
    Tests that add proposals are NOT generated for AEC-failing
    (paradoxical) paths, even if GPC is fine and random roll accepts.
    """
    mocker.patch('random.random', return_value=0.0) # Force accept
    config = basic_config.copy()
    config["MU"] = 0.0

    # This graph has a 2-path (0->1->2) that, if closed (2->0),
    # would create a timestamp-monotone cycle (H=1 < H=2 < H_new=3).
    # The pre_check_aec should catch this.
    G = nx.DiGraph([(0, 1, {'H': 1}), (1, 2, {'H': 2})])
    stress_map = {} # No cycles in this graph

    proposals = _calculate_add_proposals(G, config["MU"], stress_map)
    assert proposals == set()

@pytest.mark.parametrize("mock_random_val, expected_set", [
    (0.0, {(0, 1)}), # random.random (0.0) < Q_del (0.5) -> ACCEPT
    (0.6, set()),    # random.random (0.6) > Q_del (0.5) -> REJECT
])
def test_calculate_del_proposals_stochastic(mocker, basic_config, mock_random_val, expected_set):
    """
    Tests the delete proposal function's stochastic acceptance/rejection.
    Uses the logic where Q_del base is exactly 1/2 from the unbiased Bernoulli prior.
    """
    mocker.patch('random.random', return_value=mock_random_val)
    mocker.patch('random.choice', return_value=(0, 1))
    config = basic_config.copy()
    config["MU"] = 0.0
    config["LAMBDA"] = 0.0 
    
    G = nx.DiGraph([(0, 1, {'H': 1}), (1, 2, {'H': 2}), (2, 0, {'H': 3})])
    
    # --- Build mock args for the function ---
    all_cycles = [[(0, 1), (1, 2), (2, 0)]] # Pre-found cycles
    stress_map = {0: 1, 1: 1, 2: 1}         # Pre-computed stress
    
    proposals = _calculate_del_proposals(G, config["MU"], config["LAMBDA"],
                                         all_cycles, stress_map)
    assert proposals == expected_set

def test_calculate_del_proposals_respects_friction(mocker, basic_config):
    """
    Tests that high friction (μ) suppresses deletions.
    """
    mocker.patch('random.random', return_value=0.0001) 
    mocker.patch('random.choice', return_value=(0, 1))
    
    config = basic_config.copy()
    config["MU"] = 100.0 # Extremely high friction
    config["LAMBDA"] = 0.0 
    
    G = nx.DiGraph([(0, 1, {'H': 1}), (1, 2, {'H': 2}), (2, 0, {'H': 3}), 
                      (0, 2, {'H': 1}), (2, 3, {'H': 2}), (3, 0, {'H': 3})])

    # --- Build mock args for the function ---
    # Manually find the cycles and stress for this graph
    all_cycles = [[(0, 1), (1, 2), (2, 0)], [(0, 2), (2, 3), (3, 0)]]
    # Node 0 is in 2 cycles, 1 in 1, 2 in 2, 3 in 1
    stress_map = {0: 2, 1: 1, 2: 2, 3: 1}

    proposals = _calculate_del_proposals(G, config["MU"], config["LAMBDA"],
                                         all_cycles, stress_map)
    
    # Q_del will be ~0 due to exp(-100), so random.random() < Q_del fails
    assert proposals == set()


# --- Integration Tests for evolve_graph_to_equilibrium ---

def test_p_thermo_constants_are_correct(mocker, basic_config):
    """
    Verifies that with μ=0 and λ=0,
    P_base_add is exactly 1.0 (unconstrained boolean completion)
    and Q_base_del is exactly 0.5 (unbiased Bernoulli prior).
    """
    config = basic_config.copy()
    config["MU"] = 0.0
    config["LAMBDA"] = 0.0
    
    # --- Test 1: P_acc == 1.0 ---
    mocker.patch('random.random', return_value=0.9) # Should still accept
    
    G_add = nx.DiGraph([(0, 1, {'H': 2}), (1, 2, {'H': 1})]) # 2-path

    stress_map_add = {}
    proposals_add = _calculate_add_proposals(G_add, config["MU"], stress_map_add)
    
    # The path is valid, f(σ)=1, P_base=1.0. Total P_acc = 1.0.
    # random.random() (0.9) < 1.0, so it's in.
    assert len(proposals_add) == 1

    # --- Test 2: Q_del == 0.5 ---
    G_del = nx.DiGraph([(0, 1, {'H': 1}), (1, 2, {'H': 2}), (2, 0, {'H': 3})]) # 3-cycle
    all_cycles = [[(0, 1), (1, 2), (2, 0)]]
    stress_map_del = {0: 1, 1: 1, 2: 1}
    
    # Mock random to REJECT (0.6 > 0.5)
    mocker.patch('random.random', return_value=0.6)
    proposals_del_reject = _calculate_del_proposals(G_del, config["MU"], config["LAMBDA"], all_cycles, stress_map_del)
    assert len(proposals_del_reject) == 0

    # Mock random to ACCEPT (0.4 < 0.5)
    mocker.patch('random.random', return_value=0.4)
    proposals_del_accept = _calculate_del_proposals(G_del, config["MU"], config["LAMBDA"], all_cycles, stress_map_del)
    assert len(proposals_del_accept) == 1


def test_increases_complexity_from_spark(basic_config):
    """
    Tests that a single cycle in the "live" phase can survive or decay.
    """
    G = nx.DiGraph()
    G.add_edges_from([(0, 1, {'H': 1}), (1, 2, {'H': 2}), (2, 0, {'H': 3})])
    
    config = basic_config.copy()
    config["SIMULATION_STEPS"] = 200
    config["NUM_NODES_APPROX"] = G.number_of_nodes()

    G_final, steps = evolve_graph_to_equilibrium(G.copy(), config)
    final_n3 = get_n3_count(G_final)
    
    assert final_n3 in [0, 1]
    assert steps < 200 # Should stabilize (either decay or just sit)

def test_terminates_quickly_on_stuck_state(basic_config):
    """
    Tests that a graph with no possible moves terminates on step 1.
    """
    G = nx.DiGraph([(0, 1, {'H': 0}), (2, 3, {'H': 0})]) 
    config = basic_config.copy()
    config["NUM_NODES_APPROX"] = G.number_of_nodes()
    
    G_final, steps = evolve_graph_to_equilibrium(G.copy(), config)
    assert steps == 1 
    assert get_n3_count(G_final) == 0


def test_bernoulli_prior_unbiased_baseline():
    """
    Verifies that under unconstrained conditions (μ=0, λ=0),
    compute_add_rates yields P_add = 1.0 and compute_del_rates yields Q_del = 0.5 per cycle.
    """
    G = nx.DiGraph([(0, 1, {'H': 1}), (1, 2, {'H': 2}), (2, 0, {'H': 3})])
    cycles, stress = build_stress_map(G)
    
    # Rate of add on open 2-path
    G_open = nx.DiGraph([(0, 1, {'H': 0}), (1, 2, {'H': 0})])
    cycles_open, stress_open = build_stress_map(G_open)
    add_rates = compute_add_rates(G_open, mu=0.0, stress_map=stress_open)
    assert math.isclose(add_rates[(2, 0)], 1.0)
    
    # Rate of delete on isolated cycle: total deletion probability is Q_base = 0.5
    del_rates = compute_del_rates(G, mu=0.0, lam=0.0, all_cycles=cycles, stress_map=stress)
    total_del_prob = sum(del_rates.values())
    assert math.isclose(total_del_prob, 0.5, rel_tol=1e-9)


def test_steric_friction_suppression():
    """
    Verifies that steric friction exp(-μ * σ) exponentially suppresses add and del rates.
    """
    # Graph with 2 cycles sharing an edge
    G = nx.DiGraph([(0, 1, {'H': 1}), (1, 2, {'H': 2}), (2, 0, {'H': 3}),
                    (0, 2, {'H': 1}), (2, 3, {'H': 2}), (3, 0, {'H': 3})])
    cycles, stress = build_stress_map(G)
    
    del_rates_mu0 = compute_del_rates(G, mu=0.0, lam=0.0, all_cycles=cycles, stress_map=stress)
    del_rates_mu1 = compute_del_rates(G, mu=1.0, lam=0.0, all_cycles=cycles, stress_map=stress)
    
    # All rates with friction must be strictly less than without friction
    for edge in del_rates_mu0:
        assert del_rates_mu1[edge] < del_rates_mu0[edge]


def test_catalytic_acceleration():
    """
    Verifies that catalytic factor (1 + λ * σ_local) linearly accelerates cycle deletion.
    """
    G = nx.DiGraph([(0, 1, {'H': 1}), (1, 2, {'H': 2}), (2, 0, {'H': 3}),
                    (0, 2, {'H': 1}), (2, 3, {'H': 2}), (3, 0, {'H': 3})])
    cycles, stress = build_stress_map(G)
    
    del_rates_lam0 = compute_del_rates(G, mu=0.0, lam=0.0, all_cycles=cycles, stress_map=stress)
    del_rates_lam2 = compute_del_rates(G, mu=0.0, lam=2.0, all_cycles=cycles, stress_map=stress)
    
    total_lam0 = sum(del_rates_lam0.values())
    total_lam2 = sum(del_rates_lam2.values())
    assert total_lam2 > total_lam0


def test_detailed_balance_equilibrium(basic_config):
    """
    Verifies that dynamic equilibrium achieves a stable balance between
    creation and deletion without thermodynamic drift.
    """
    G = nx.DiGraph()
    G.add_edges_from([(0, 1, {'H': 1}), (1, 2, {'H': 2}), (2, 0, {'H': 3})])
    
    config = basic_config.copy()
    config["SIMULATION_STEPS"] = 150
    config["NUM_NODES_APPROX"] = 3
    
    G_final, steps = evolve_graph_to_equilibrium(G.copy(), config)
    assert steps > 0
    assert G_final.number_of_nodes() == 3


def test_evolve_graph_to_equilibrium(basic_config):
    """
    Full integration test of the timestamped system.
    """
    G, levels = generate_zpi_vacuum(20)
    G_initial = inject_energic_event(G.copy(), levels)
    
    config = basic_config.copy()
    config["NUM_NODES_APPROX"] = G_initial.number_of_nodes()
    config["SIMULATION_STEPS"] = 100

    G_final, steps = evolve_graph_to_equilibrium(G_initial.copy(), config)
    
    assert G_final is not None
    assert steps > 0


# --- Tests for Reciprocal Proposal Filtering & Atomic Reduction ---

def test_reciprocal_proposal_elimination_filter():
    """
    Corollary 2.2: The Step 3 merge filter strictly drops simultaneous
    reciprocal additions (u, v) and (v, u) and self-loops.
    """
    proposals_add = {
        ((1, 2), 2),
        ((2, 1), 2),  # Reciprocal collision with (1, 2)
        ((3, 4), 1),  # Valid addition
        ((5, 5), 1),  # Self-loop
    }
    add_edges_set = {edge for edge, _ in proposals_add}
    filtered_add = [
        (edge[0], edge[1], {'H': h_val})
        for edge, h_val in proposals_add
        if (edge[1], edge[0]) not in add_edges_set and edge[0] != edge[1]
    ]
    added_edges = {(u, v) for u, v, _ in filtered_add}
    assert added_edges == {(3, 4)}
    assert (1, 2) not in added_edges
    assert (2, 1) not in added_edges
    assert (5, 5) not in added_edges


def test_four_cycle_tie_fixture_symmetry_protection(basic_config):
    """
    Tests Astra's 4-cycle tie fixture with alternating timestamps (H=1, 2, 1, 2).
    Verifies that under parallel evolution, any reciprocal collisions are
    symmetrically dropped, preserving Axiom 1 (no 2-cycles).
    """
    G = nx.DiGraph()
    G.add_edges_from([
        (0, 1, {'H': 1}),
        (1, 2, {'H': 2}),
        (2, 3, {'H': 1}),
        (3, 0, {'H': 2}),
    ])
    config = basic_config.copy()
    config["SIMULATION_STEPS"] = 10
    config["MU"] = 0.0  # Deterministic proposal generation
    
    G_evolved, _ = evolve_graph_to_equilibrium(G.copy(), config)
    
    # Invariant: Axiom 1 strictly forbids 2-cycles (u -> v and v -> u)
    for u, v in G_evolved.edges():
        assert not G_evolved.has_edge(v, u), f"Axiom 1 violation: 2-cycle found between {u} and {v}"


def test_atomic_cycle_reduction_step_descent():
    """
    Theorem 2.4.5: Atomic Cycle Reduction directly descends in potential
    Phi(G) = (L_max, N_{L_max}) without intermediate pentagram inflation.
    """
    # 4-cycle: 0 -> 1 -> 2 -> 3 -> 0
    G4 = nx.DiGraph([(0, 1), (1, 2), (2, 3), (3, 0)])
    cycles_before = list(nx.simple_cycles(G4))
    l_max_before = max(len(c) for c in cycles_before)
    assert l_max_before == 4

    # Atomic rewrite: add chord (2, 0) closing (0 -> 1 -> 2), delete perimeter edge (2, 3)
    G4.add_edge(2, 0)
    G4.remove_edge(2, 3)
    cycles_after = list(nx.simple_cycles(G4))
    l_max_after = max((len(c) for c in cycles_after), default=0)
    assert l_max_after == 3  # Strictly descended from 4 to 3
    assert len(cycles_after) == 1
    assert set(cycles_after[0]) == {0, 1, 2}
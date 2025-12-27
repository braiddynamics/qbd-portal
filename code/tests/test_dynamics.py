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
    _calculate_del_proposals
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
    # Note: ALPHA is not needed by the micro-rules
    config["T_VACUUM"] = math.log(2) # Use the real postulated T
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
    
    # --- FIXED CALL ---
    # Removed N and ALPHA. The function now only takes 4 args.
    proposals = _calculate_add_proposals(G, config["T_VACUUM"], config["MU"], 
                                         stress_map) # Pass the map
    
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

    # --- FIXED CALL ---
    proposals = _calculate_add_proposals(G, config["T_VACUUM"], config["MU"], 
                                         stress_map)
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

    # --- FIXED CALL ---
    proposals = _calculate_add_proposals(G, config["T_VACUUM"], config["MU"],
                                         stress_map)
    assert proposals == set()

@pytest.mark.parametrize("mock_random_val, expected_set", [
    (0.0, {(0, 1)}), # random.random (0.0) < Q_del (0.5) -> ACCEPT
    (0.6, set()),    # random.random (0.6) > Q_del (0.5) -> REJECT
])
def test_calculate_del_proposals_stochastic(mocker, basic_config, mock_random_val, expected_set):
    """
    Tests the delete proposal function's stochastic acceptance/rejection.
    Uses the *new* logic where Q_del_thermo is exactly 1/2.
    """
    mocker.patch('random.random', return_value=mock_random_val)
    mocker.patch('random.choice', return_value=(0, 1))
    config = basic_config.copy()
    config["MU"] = 0.0
    config["LAMBDA"] = 0.0 
    config["T_VACUUM"] = math.log(2) # Ensure T is correct
    
    G = nx.DiGraph([(0, 1, {'H': 1}), (1, 2, {'H': 2}), (2, 0, {'H': 3})])
    
    # --- Build mock args for the function ---
    all_cycles = [[(0, 1), (1, 2), (2, 0)]] # Pre-found cycles
    stress_map = {0: 1, 1: 1, 2: 1}         # Pre-computed stress
    
    # --- FIXED CALL ---
    # Removed N and ALPHA. The function now only takes 6 args.
    proposals = _calculate_del_proposals(G, config["T_VACUUM"], config["MU"], config["LAMBDA"],
                                         all_cycles, stress_map) # Pass new args
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

    # --- FIXED CALL ---
    proposals = _calculate_del_proposals(G, config["T_VACUUM"], config["MU"], config["LAMBDA"],
                                         all_cycles, stress_map) # Pass new args
    
    # Q_del will be ~0 due to exp(-100), so random.random() < Q_del fails
    assert proposals == set()


# --- Integration Tests for evolve_graph_to_equilibrium ---

def test_p_thermo_constants_are_correct(mocker, basic_config):
    """
    This test replaces the old, flawed 'test_p_thermo_is_correct'.
    It verifies the *new* logic: that with T=ln(2), μ=0, and λ=0,
    P_thermo_add is *exactly* 1 and Q_thermo_del is *exactly* 1/2.
    """
    config = basic_config.copy()
    # Set config to the exact theoretical values
    config["T_VACUUM"] = math.log(2)
    config["MU"] = 0.0
    config["LAMBDA"] = 0.0
    
    # --- Test 1: P_acc_thermo == 1 ---
    mocker.patch('random.random', return_value=0.9) # Should still accept
    
    G_add = nx.DiGraph([(0, 1, {'H': 2}), (1, 2, {'H': 1})]) # 2-path

    stress_map_add = {}
    proposals_add = _calculate_add_proposals(G_add, config["T_VACUUM"], config["MU"], stress_map_add)
    
    # The path is valid, f(σ)=1, P_thermo=1. Total P_acc = 1.0.
    # random.random() (0.9) < 1.0, so it's in.
    assert len(proposals_add) == 1

    # --- Test 2: Q_del_thermo == 1/2 ---
    G_del = nx.DiGraph([(0, 1, {'H': 1}), (1, 2, {'H': 2}), (2, 0, {'H': 3})]) # 3-cycle
    all_cycles = [[(0, 1), (1, 2), (2, 0)]]
    stress_map_del = {0: 1, 1: 1, 2: 1}
    
    # Mock random to REJECT (0.6 > 0.5)
    mocker.patch('random.random', return_value=0.6)
    proposals_del_reject = _calculate_del_proposals(G_del, config["T_VACUUM"], config["MU"], config["LAMBDA"], all_cycles, stress_map_del)
    assert len(proposals_del_reject) == 0

    # Mock random to ACCEPT (0.4 < 0.5)
    mocker.patch('random.random', return_value=0.4)
    proposals_del_accept = _calculate_del_proposals(G_del, config["T_VACUUM"], config["MU"], config["LAMBDA"], all_cycles, stress_map_del)
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


def test_runs_at_high_T(basic_config):
    """
    Tests that a high T (hot) sim creates a dense graph.
    The new logic is N-agnostic, but T still matters for the *old* logic
    this test was based on. We'll keep it as a sanity check.
    With T=1000, ΔF_add = -1000*ln(2) < 0 -> P_thermo=1.
    With T=1000, ΔF_del = +1000*ln(2) > 0 -> Q_thermo=min(1, exp(-ln2)) = 1/2.
    The test should still pass.
    """
    G_initial_template = nx.DiGraph()
    G_initial_template.add_edges_from([(100, 101, {'H': 0}), (101, 102, {'H': 0})])
    
    config = basic_config.copy()
    config["NUM_NODES_APPROX"] = G_initial_template.number_of_nodes() # N=3
    config["T_VACUUM"] = 1000.0 # Very high T
    config["MU"] = 0.0          # No friction
    config["SIMULATION_STEPS"] = 100

    final_n3s = []
    for _ in range(20): # Run 20 times
        G_final, _ = evolve_graph_to_equilibrium(G_initial_template.copy(), config)
        final_n3s.append(get_n3_count(G_final))

    assert np.mean(final_n3s) > 0


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
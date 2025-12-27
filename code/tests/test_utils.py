import pytest
import networkx as nx
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.utils import (
    find_all_3_cycles, 
    is_permissible, 
    _is_path_monotone,
    pre_check_aec
)

# --- Tests for find_all_3_cycles ---
@pytest.mark.parametrize("edges, expected_count", [
    ([(0,1), (1,2), (2,0)], 1), # Standard 3-cycle
    ([(0,1), (1,2), (2,0), (0,2)], 1), # 3-cycle + transitive edge
    ([(0,1), (1,2), (2,3), (3,0)], 0), # 4-cycle
    ([(0,1), (1,0)], 0), # 2-cycle
    ([], 0), # Empty
    ([(0,1), (1,2), (2,0), (3,4), (4,5), (5,3)], 2), # Two disjoint 3-cycles
])
def test_find_all_3_cycles(edges, expected_count):
    """
    Tests the find_all_3_cycles function in the utils module.
    """
    G = nx.DiGraph()
    G.add_edges_from(edges)
    cycles = find_all_3_cycles(G)
    assert len(cycles) == expected_count

# --- Tests for GPC (is_permissible) ---
@pytest.mark.parametrize("edges, u, v, w, expected, test_id", [
    ([(0, 1), (1, 2)], 2, 0, 1, True, "Valid 2-path"),
    ([(0, 1), (1, 2), (0, 2)], 2, 0, 1, False, "Fails GPC (direct edge)"),
    ([(0, 1), (1, 2), (0, 3), (3, 2)], 2, 0, 1, False, "Fails GPC (alt 2-path)"),
    ([(0, 1), (1, 2), (0, 3), (3, 4), (4, 2)], 2, 0, 1, True, "Valid (alt 3-path is ok)"),
])
def test_is_permissible(edges, u, v, w, expected, test_id):
    """
    Tests the Principle of Unique Causality (PUC) implementation.
    """
    G = nx.DiGraph(edges)
    assert is_permissible(G, u, v, w) == expected

# --- Tests for Timestamp Logic (Axiom 3) ---

@pytest.mark.parametrize("edges_with_h, path, expected", [
    ([('A', 'B', {'H': 1}), ('B', 'C', {'H': 2})], ['A', 'B', 'C'], True),
    ([('A', 'B', {'H': 1}), ('B', 'C', {'H': 1})], ['A', 'B', 'C'], False),
    ([('A', 'B', {'H': 2}), ('B', 'C', {'H': 1})], ['A', 'B', 'C'], False),
    ([('A', 'B', {'H': 1})], ['A', 'B'], True),
    ([('A', 'B', {'H': 1}), ('B', 'C', {'H': 5}), ('C', 'D', {'H': 10})], ['A', 'B', 'C', 'D'], True),
    ([('A', 'B', {'H': 1}), ('B', 'C', {'H': 5}), ('C', 'D', {'H': 4})], ['A', 'B', 'C', 'D'], False),
])
def test_is_path_monotone(edges_with_h, path, expected):
    """
    Tests the _is_path_monotone helper function.
    """
    G = nx.DiGraph()
    G.add_edges_from(edges_with_h)
    assert _is_path_monotone(G, path) == expected

def test_pre_check_aec_safe():
    """
    Tests that pre_check_aec returns True (SAFE) for a non-monotone path.
    (See Monograph §1.13.2)
    """
    # Path (0 -> 1 -> 2) is NOT monotone (H=2 > H=1)
    G = nx.DiGraph()
    G.add_edges_from([(0, 1, {'H': 2}), (1, 2, {'H': 1})])
    
    # Proposing (2, 0) with H=3 is safe, as the cycle is not fully monotone
    assert pre_check_aec(G, u=2, v=0, H_new=3) == True

def test_pre_check_aec_paradox():
    """
    Tests that pre_check_aec returns False (PARADOX) for a monotone path.
    """
    # Path (0 -> 1 -> 2) IS monotone (H=1 < H=2)
    G = nx.DiGraph()
    G.add_edges_from([(0, 1, {'H': 1}), (1, 2, {'H': 2})])
    
    # Proposing (2, 0) with H=3 would complete the monotone cycle
    # (H(1,2) < H_new is 2 < 3, which is True)
    assert pre_check_aec(G, u=2, v=0, H_new=3) == False

def test_pre_check_aec_paradox_saved_by_timestamp():
    """
    Tests that a topologically monotone path is still SAFE if the
    new edge's timestamp is too low.
    """
    # Path (0 -> 1 -> 2) IS monotone (H=3 < H=4)
    G = nx.DiGraph()
    G.add_edges_from([(0, 1, {'H': 3}), (1, 2, {'H': 4})])
    
    # Proposing (2, 0) with H_new=2.
    # The check H(1,2) < H_new fails (4 < 2 is False).
    # Therefore, the cycle is NOT monotone.
    assert pre_check_aec(G, u=2, v=0, H_new=2) == True

def test_pre_check_aec_no_path():
    """
    Tests that pre_check_aec returns True (SAFE) if no return path exists.
    """
    G = nx.DiGraph()
    G.add_edges_from([(0, 1, {'H': 1}), (2, 3, {'H': 1})])
    
    # Proposing (1, 2) with H=2.
    # There is no path from 2 back to 1, so it's safe.
    assert pre_check_aec(G, u=1, v=2, H_new=2) == True
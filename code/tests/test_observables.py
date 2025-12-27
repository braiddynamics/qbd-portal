# tests/test_observables.py
import pytest
import networkx as nx
from model.observables import get_n3_count, get_graph_density
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.mark.parametrize("graph_dict, expected_n3, description", [
    ({}, 0, "Empty graph"),
    ({0: [1], 1: [2]}, 0, "Line graph with no cycle"),
    ({0: [1], 1: [2], 2: [0]}, 1, "Single perfect 3-cycle"),
    ({0: [1], 1: [2], 2: [0], 3:[4], 4:[5], 5:[3]}, 2, "Two disjoint 3-cycles"),
    ({0: [1, 2], 1: [3]}, 0, "Acyclic DAG"),
    ({0: [1], 1: [0]}, 0, "A 2-cycle should not be counted as a 3-cycle"),
    ({0: [1], 1: [2], 2: [3], 3: [0]}, 0, "A 4-cycle should not be counted as a 3-cycle")
])
def test_get_n3_count(graph_dict, expected_n3, description):
    G = nx.DiGraph(graph_dict)
    assert get_n3_count(G) == expected_n3, description

def test_get_graph_density():
    G = nx.DiGraph([(0,1), (1,2), (2,0)])
    assert get_graph_density(G) == 1.0, "3 edges / 3 nodes = 1.0"
    assert get_graph_density(nx.DiGraph()) == 0.0, "Empty graph"
# tests/test_qecc.py
import pytest
import networkx as nx
from model.qecc import measure_local_geometric_stress
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.mark.parametrize("edges, base_nodes, expected_stress, description", [
    (
        [(0,1), (1,2), (2,0)], 
        {0,1,2}, 
        1, 
        "A single 3-cycle, base={0,1,2}. Finds itself."
    ),
    (
        [(0,1), (1,2), (2,0), (3,4), (4,5), (5,3)], 
        {0,1,2}, 
        1, 
        "Two disjoint cycles, base={0,1,2}. Finds 1."
    ),
    (
        # Two overlapping 3-cycles: (0,1,2) and (0,2,3)
        [(0,1), (1,2), (2,0), (0,2), (2,3), (3,0)],
        {0,1,2}, # Base nodes for the first cycle
        2, # Finds (0,1,2) and (0,2,3)
        "Two overlapping cycles, finds both"
    ),
     (
        # Same graph
        [(0,1), (1,2), (2,0), (0,2), (2,3), (3,0)],
        {0,2,3}, # Base nodes for the second cycle
        2, # Finds (0,1,2) and (0,2,3)
        "Two overlapping cycles, finds both (from other side)"
    ),
    (
        [(0,1), (1,2)], 
        {0,1,2}, 
        0, 
        "A 2-path, finds 0 cycles"
    ),
])
def test_measure_local_geometric_stress(edges, base_nodes, expected_stress, description):
    """
    Tests the corrected measure_local_geometric_stress function
    with 1-hop neighborhood logic.
    """
    G = nx.DiGraph()
    G.add_edges_from(edges)
    stress = measure_local_geometric_stress(G, base_nodes)
    assert stress == expected_stress, description
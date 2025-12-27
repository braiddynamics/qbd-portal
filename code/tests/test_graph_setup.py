import pytest
import networkx as nx
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.graph_setup import generate_zpi_vacuum, inject_energic_event

# --- Tests for ZPI Vacuum ---
@pytest.mark.parametrize("n", [10, 50, 100])
def test_generate_zpi_vacuum_structure_and_timestamps(n):
    """
    Tests that the ZPI vacuum is a valid DAG and all
    initial edges have the correct vacuum timestamp (H=0).
    """
    G, levels = generate_zpi_vacuum(n)
    
    # --- Structure Assertions ---
    assert isinstance(G, nx.DiGraph)
    assert G.number_of_nodes() <= n
    assert nx.is_directed_acyclic_graph(G), "Vacuum must be DAG"
    assert len(levels) >= 2, "At least root and children"
    assert levels[0] == [0], "Root is 0"
    
    # --- Timestamp Assertion ---
    # Check that *every* edge in the vacuum has H=0
    for u, v, data in G.edges(data=True):
        assert data.get('H') == 0, f"Vacuum edge ({u},{v}) has wrong timestamp"

def test_generate_zpi_vacuum_small():
    """Tests the node count guard rail."""
    with pytest.raises(ValueError):
        generate_zpi_vacuum(2) # too small

# --- Tests for Ignition Event ---
@pytest.mark.parametrize("n", [10, 50])
def test_inject_energic_event_creates_cycle_and_timestamp(n):
    """
    Tests that the "ignition" event creates a 3-cycle
    and that the new edge has the first non-zero timestamp (H=1).
    """
    G, levels = generate_zpi_vacuum(n)
    G_orig_edges = G.number_of_edges()
    
    G_injected = inject_energic_event(G.copy(), levels) 
    
    # --- Structure Assertions ---
    assert not nx.is_directed_acyclic_graph(G_injected), "Should have cycle"
    cycles = list(nx.simple_cycles(G_injected))
    assert any(len(c) == 3 for c in cycles), "At least one 3-cycle"
    assert G_injected.number_of_edges() == G_orig_edges + 1, "Added one edge"

    # --- Timestamp Assertion ---
    # Find the new edge (u, v) and check its timestamp
    v = levels[0][0]  # root
    u = levels[2][0]  # first grandchild
    
    assert G_injected.has_edge(u, v), "Ignition edge (u, v) was not created"
    assert G_injected.edges[u, v].get('H') == 1, "Ignition edge has wrong timestamp"

def test_inject_energic_event_small_graph_fallback():
    """
    Tests the fallback case for tiny graphs (N < 4) and
    checks that all fallback edges have H=1.
    """
    G, levels = generate_zpi_vacuum(3)
    G_injected = inject_energic_event(G, levels)
    
    # --- Structure Assertions ---
    assert G_injected.number_of_nodes() == 3
    assert G_injected.number_of_edges() == 3, "Full 3-cycle"
    assert len(list(nx.simple_cycles(G_injected))) > 0, "Has cycles"

    # --- Timestamp Assertion ---
    for u, v, data in G_injected.edges(data=True):
        assert data.get('H') == 1, f"Fallback edge ({u},{v}) has wrong timestamp"
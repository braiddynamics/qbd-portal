# /model/qecc.py
import networkx as nx
from typing import Set
from model.utils import find_all_3_cycles

def measure_local_geometric_stress(G: nx.DiGraph, node_set: Set[int]) -> int:
    """
    Measures the local syndrome (σ) of a subgraph, defined
    as the "geometric stress."

    This is the core "Awareness" function of the
    evolution operator. It implements the "check operator"
    from the QECC formalism.

    The "stress" is the count of all 3-cycles (excitations, σ = -1)
    that are in contact with the input `node_set`. This count is
    then fed into the syndrome-response function f(σ)
    to calculate the thermodynamic friction (μ) and catalysis (λ)
    that govern P_acc and Q_del.

    The "awareness" is localized by first creating a 1-hop
    subgraph around the node_set to optimize the cycle search.

    Args:
        G: The full causal graph.
        node_set: The set of nodes at the center of the
                  measurement (e.g., the 3 nodes of a 2-path
                  or a 3-cycle).

    Returns:
        An integer count of all 3-cycles touching the `node_set`.
    """
    if not node_set:
        return 0
    
    # 1. Define the local "awareness patch":
    #    the node_set plus all 1-hop neighbors (predecessors/successors).
    #    This ensures any cycle "touching" the set is included.
    awareness_nodes = set(node_set)
    for node in node_set:
        # G.predecessors() and G.successors() are efficient lookups
        awareness_nodes.update(G.predecessors(node))
        awareness_nodes.update(G.successors(node))

    # 2. Create a localized subgraph based on this patch.
    #    This is a critical optimization, preventing a full-graph
    #    cycle search for every local measurement.
    subgraph = G.subgraph(awareness_nodes)
    
    # 3. Find all 3-cycles *only within this local subgraph*
    all_cycles = find_all_3_cycles(subgraph)

    # 4. Filter the local cycles to find the true stress count
    stress_count = 0
    for cycle_edges in all_cycles:
        cycle_nodes = {v for e in cycle_edges for v in e}
        # A cycle contributes to the stress *if* it touches
        # any of the *original* nodes in the input set.
        if not cycle_nodes.isdisjoint(node_set):
            stress_count += 1
            
    return stress_count
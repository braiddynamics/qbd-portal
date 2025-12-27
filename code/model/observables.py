# /model/observables.py


import networkx as nx
import numpy as np
from model.utils import find_all_3_cycles

def get_n3_count(G: nx.DiGraph) -> int:
    """
    Measures the total population of 3-cycles (N_3) in the graph.

    This observable quantifies the total amount of geometric information
    in the universe, as the 3-cycle is the fundamental "quantum of
    geometry".

    N_3 is the primary macroscopic variable in the Master Equation
    and its density (ρ_3 = N_3 / N) determines the equilibrium state.

    Args:
        G: The causal graph.

    Returns:
        The integer count of all unique 3-cycles.
    """
    # This function relies on a simple, robust cycle-finding utility.
    return len(find_all_3_cycles(G))

def get_graph_density(G: nx.DiGraph) -> float:
    """
    Calculates the average degree of the graph (<k> = |E| / N).

    This observable serves as a computationally cheap proxy for the
    3-cycle density (ρ_3). In a saturated, sparse graph, the two
    are proven to be linearly related by:
    
    <k> ≈ 6 * ρ_3
    
    This value is used to track the "crowding"
    or "stress" that informs the thermodynamic suppression function f(σ).

    Args:
        G: The causal graph.

    Returns:
        The average number of edges per node.
    """
    n = G.number_of_nodes()
    if n == 0:
        return 0.0
    
    # <k> = Total Edges / Total Nodes
    return G.number_of_edges() / n

    # Append to qbd_model/observables.py

from model.utils import is_permissible, pre_check_aec

def measure_compliant_site_count(G: nx.DiGraph) -> int:
    """
    Counts the total number of topologically compliant 2-paths (v->w->u)
    that satisfy PUC and AEC, serving as valid candidates for edge addition.
    
    This is the numerator 'N_sites' in the Mean Field equation.
    """
    count = 0
    # Iterate exactly as the Universal Constructor does
    for v in G.nodes():
        for w in list(G.successors(v)):
            for u in list(G.successors(w)):
                # Basic graph constraints
                if v == u or G.has_edge(u, v):
                    continue
                
                # Axiom 2: PUC Check
                if not is_permissible(G, u, v, w):
                    continue
                
                # Calculate H_new for AEC check
                in_edges = G.in_edges(u, data=True)
                max_h_in = max((data.get('H', 0) for _, _, data in in_edges), default=0)
                H_new = max_h_in + 1
                
                # Axiom 3: AEC Pre-check
                if pre_check_aec(G, u, v, H_new):
                    count += 1
    return count
# /model/utils.py
import networkx as nx
import math

def find_all_3_cycles(G: nx.DiGraph):
    """
    Finds all unique 3-cycles in the causal graph.
    """
    cycles = set()
    for u in G.nodes():
        for v in list(G.successors(u)):
            for w in list(G.successors(v)):
                if G.has_edge(w, u):
                    cycle_edges = frozenset([(u,v), (v,w), (w,u)])
                    cycles.add(cycle_edges)
    
    return [list(cycle) for cycle in cycles]

def is_permissible(G: nx.DiGraph, u, v, w) -> bool:
    """
    Verifies the PUC.

    """
    if G.has_edge(v, u):
        return False
    for x in G.successors(v):
        if x != w and G.has_edge(x, u):
            return False
    return True

# --- TIMESTAMP FUNCTIONS ---

def _is_path_monotone(G: nx.DiGraph, path: list) -> bool:
    """
    Helper for pre_check_aec. Checks if a path is timestamp-monotone.
    A path (v, w, ..., z) is monotone if H(v,w) < H(w,...) < ... < H(...,z).
    """
    if len(path) < 2:
        return True # A single node or empty path is not a paradox
        
    for i in range(len(path) - 2): # Iterate up to the second-to-last node
        u, v = path[i], path[i+1]
        w = path[i+2]
        
        # Get timestamps. Default to 0 if (somehow) missing.
        h1 = G.edges[u, v].get('H', 0)
        h2 = G.edges[v, w].get('H', 0)
        
        if not h1 < h2:
            return False # Path is not strictly increasing
            
    return True

def pre_check_aec(G: nx.DiGraph, u: int, v: int, H_new: int) -> bool:
    """
    Pre-checks a proposed edge for Acyclic Effective Causality

    INCLUDES an O(log N) cutoff for performance (Local BFS Bounds). This prevents an
    exponential-time search for long-range, non-physical paradoxes.
    """
    
    # --- Cutoff ---
    # We only check for *local* paradoxes. A log(N) depth is a
    # generous "local" neighborhood.
    N = G.number_of_nodes()
    if N > 1:
        # +3 is a safety buffer. Minimum cutoff of 3.
        cutoff = int(math.log(N)) + 3 
    else:
        cutoff = 1

    # 1. Temporarily add the edge
    G.add_edge(u, v, H=H_new)
    
    try:
        # 2. Search for any path from v back to u, *using the cutoff*
        for path in nx.all_simple_paths(G, source=v, target=u, cutoff=cutoff):
            # path is [v, node1, node2, ..., u]
            
            # 3. Check if the *full cycle path* is monotone.
            if len(path) > 1:
                is_existing_path_monotone = _is_path_monotone(G, path)
                
                if is_existing_path_monotone:
                    last_node_in_path = path[-2]
                    H_last_leg = G.edges[last_node_in_path, u].get('H', 0)
                    
                    if H_last_leg < H_new:
                        # 4. Paradox found!
                        return False # REJECT
    
    finally:
        # 5. ALWAYS remove the temporary edge
        G.remove_edge(u, v)
        
    # 6. No monotone paths found.
    return True # ACCEPT
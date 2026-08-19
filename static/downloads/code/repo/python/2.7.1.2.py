import networkx as nx
import math
from collections import deque

# ==============================================================================
# TIER 1: DEFINITIONAL REFERENCE SPECIFICATION (Semantic Mapping)
# ==============================================================================

def is_path_monotone(G: nx.DiGraph, path: list) -> bool:
    """
    Verifies if a path sequence exhibits strictly increasing creation timestamps:
    H(p_i, p_{i+1}) < H(p_{i+1}, p_{i+2}) for all intermediate nodes.
    """
    for i in range(len(path) - 2):
        h1 = G.edges[path[i], path[i+1]]['H']
        h2 = G.edges[path[i+1], path[i+2]]['H']
        if not (h1 < h2):
            return False  # Monotonicity broken: not an effective causal channel
    return True

def pre_check_aec_reference(G: nx.DiGraph, u: int, v: int, H_new: int) -> bool:
    """
    Reference specification: Directly enforces the 4 physical constraints
    of Acyclic Effective Causality (Axiom 3) via path verification.
    """
    # 1. Local Search Horizon (R ~ log N)
    N = G.number_of_nodes()
    cutoff = int(math.log2(N)) + 3 if N > 1 else 1
    
    # 2. Tentative State Construction
    G.add_edge(u, v, H=H_new)
    
    try:
        # 3. Reverse Path Search (v -> ... -> u)
        for path in nx.all_simple_paths(G, v, u, cutoff=cutoff):
            # Constraint A: Mediation (length >= 2)
            if len(path) >= 2:
                # Constraint B: Timestamp Monotonicity
                if is_path_monotone(G, path):
                    # Constraint C: Closure Consistency
                    last_leg_H = G.edges[path[-2], u]['H']
                    if last_leg_H < H_new:
                        return False  # Causal paradox detected: reject update
    finally:
        # 4. State Rollback (preserves substrate state)
        G.remove_edge(u, v)
        
    return True  # Causal hygiene satisfied

# ==============================================================================
# TIER 2: CONSTRUCTOR OPERATIONAL ENGINE (Real-Time Polynomial Execution)
# ==============================================================================

def pre_check_aec(G: nx.DiGraph, u: int, v: int, H_new: int) -> bool:
    """
    Operational execution engine: Evaluates the exact same decision predicate
    via monotonic forward BFS, pruning non-causal branches dynamically in O(V + E).
    """
    N = G.number_of_nodes()
    L_cut = int(math.floor(math.log2(N))) + 3 if N > 1 else 1
    queue = deque([(v, -1, 0)])  # (current_vertex, last_leg_H, depth)
    visited = set([(v, -1)])
    
    while queue:
        curr, last_h, depth = queue.popleft()
        if depth >= L_cut:
            continue
        for succ in G.successors(curr):
            edge_h = G.edges[curr, succ].get('H', 0)
            if edge_h <= last_h:
                continue  # Dynamic monotonicity filter
            if succ == u and edge_h < H_new:
                return False  # Loop closure intercepted
            state = (succ, edge_h)
            if state not in visited:
                visited.add(state)
                queue.append((succ, edge_h, depth + 1))
                
    return True  # Valid addition

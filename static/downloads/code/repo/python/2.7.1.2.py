def pre_check_aec(G, u, v, H_new):
    """
    Verifies that adding edge (u, v) at time H_new does not close a 
    monotonically increasing causal loop.
    """
    # 1. Define Local Search Horizon
    # The cutoff scales logarithmically (R ~ log N) to approximate global 
    # consistency within the thermodynamic limit of the local patch.
    N = G.number_of_nodes()
    cutoff = int(log(N)) + 3 if N > 1 else 1
    
    # 2. Tentative State Construction
    # Temporarily add the proposed edge to check its transitive effects.
    G.add_edge(u, v, H=H_new)
    
    try:
        # 3. Reverse Path Search (v -> ... -> u)
        # Search for any existing path that could complete a cycle back to u.
        for path in all_simple_paths(G, v, u, cutoff=cutoff):
            
            # Constraint A: Mediation
            # The path must involve at least 2 edges to constitute effective influence.
            if len(path) >= 2:
                
                # Constraint B: Monotonicity
                # The path must possess strictly increasing timestamps.
                if is_path_monotone(G, path):
                    
                    # Constraint C: Closure Consistency
                    # The return path must connect causally to the new edge.
                    last_leg_H = G.edges[path[-2], u]['H']
                    
                    if last_leg_H < H_new:
                        return False  # PARADOX DETECTED: Reject Update
    finally:
        # 4. State Rollback
        # Ensure the graph remains unmodified regardless of the outcome.
        G.remove_edge(u, v)
    
    return True  # No paradox found within horizon: Accept Update

def is_path_monotone(G, path):
    """
    Verifies if a path sequence exhibits strictly increasing timestamps.
    H(p_i, p_{i+1}) < H(p_{i+1}, p_{i+2})
    """
    for i in range(len(path)-2):
        h1 = G.edges[path[i], path[i+1]]['H']
        h2 = G.edges[path[i+1], path[i+2]]['H']
        if not (h1 < h2):
            return False # Timestamp break found, path is not causal.
    return True

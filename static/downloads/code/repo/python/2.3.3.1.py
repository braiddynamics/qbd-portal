def is_permissible(G, v, w, u):  
    """
    Checks if adding edge (u,v) to close the 2-path v->w->u is valid.
    Constraint: No other path of length <= 2 may exist between v and u.
    """
    # 1. Check for Direct Path (Length 1)
    if G.has_edge(v, u):         
        return False  # Forbidden: Cloning a direct link

    # 2. Check for Alternative 2-Paths (Length 2)
    # Scan neighbors of v to see if any connect to u (other than w)
    for x in G.successors(v):    
        if x != w and G.has_edge(x, u):
            return False  # Forbidden: Cloning an existing 2-path

    # 3. Path is Unique
    return True

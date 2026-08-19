def is_permissible(G: nx.DiGraph, v: int, w: int, u: int) -> bool:
    """
    Checks if adding edge (u, v) to close candidate 2-path v -> w -> u satisfies PUC.
    Constraint: No direct edge (v, u) and no alternative 2-path v -> x -> u (x != w).
    """
    # 1. Check for Direct Path (Length 1)
    if G.has_edge(v, u):
        # Forbidden: Cloning a direct link
        return False

    # 2. Check for Alternative 2-Paths (Length 2)
    # Scan neighbors of v to see if any connect to u (other than w)
    for x in G.successors(v):
        if x != w and G.has_edge(x, u):
            # Forbidden: Cloning an existing 2-path
            return False

    # 3. Path is Unique
    return True

import networkx as nx
import pandas as pd

def create_directed_cycle(k):
    """Creates a simple directed k-cycle."""
    G = nx.DiGraph()
    nodes = list(range(k))
    for i in range(k):
        G.add_edge(nodes[i], nodes[(i + 1) % k])
    return G

def max_cycle_length(G):
    """Finds the length of the longest simple cycle in the graph."""
    try:
        cycles = list(nx.simple_cycles(G))
        if not cycles:
            return 0
        return max(len(c) for c in cycles)
    except nx.NetworkXNoCycle:
        return 0

def find_compliant_2_paths(G):
    """Finds all PUC-compliant 2-paths (v -> w -> u)."""
    paths = []
    for v in G.nodes():
        for w in G.successors(v):
            for u in G.successors(w):
                if u == v: continue
                # PUC Check 1: No direct path v->u
                if G.has_edge(v, u):
                    continue
                # PUC Check 2: No alternative 2-path v->x->u with x != w
                other_paths = 0
                for x in G.successors(v):
                    if x != w and G.has_edge(x, u):
                        other_paths += 1
                # PUC Check 3: The closing chord u->v does not already exist
                if other_paths == 0 and not G.has_edge(u, v):
                    paths.append((v, w, u))
    return paths

def add_all_chords(G):
    """
    Phase 1: Add all PUC-compliant chords in parallel.
    Returns the number of additions.
    """
    ops = 0
    paths_to_add = find_compliant_2_paths(G)
    for v, w, u in paths_to_add:
        G.add_edge(u, v)
        ops += 1
    return ops

def delete_to_break_large_cycles(G):
    """
    Phase 2: Sequentially remove edges from large cycles
    until max L <= 3.
    Returns the number of deletions.
    """
    ops = 0
    current_max_len = max_cycle_length(G)
    while current_max_len > 3:
        cycle_found = None
        for cycle in nx.simple_cycles(G):
            if len(cycle) > 3:
                cycle_found = cycle
                break

        if cycle_found:
            # Delete the first edge of this cycle
            edge_to_remove = (cycle_found[0], cycle_found[1])
            if G.has_edge(*edge_to_remove):
                G.remove_edge(*edge_to_remove)
                ops += 1
            current_max_len = max_cycle_length(G)  # Re-check
        else:
            break

    return ops

def total_reduction_steps(k):
    """
    Calculates the total steps to reduce a k-cycle using the
    two-phase (add-all, then-delete) algorithm.
    """
    if k <= 3:
        return 0, 0

    G = create_directed_cycle(k)
    # Phase 1: Add all k chords (in simple k-cycle, all compliant)
    add_ops = add_all_chords(G)
    # Phase 2: Delete until max L <= 3
    del_ops = delete_to_break_large_cycles(G)
    return add_ops, del_ops

# --- Main execution ---
results = []
for k in range(4, 13):
    adds, dels = total_reduction_steps(k)
    results.append({
        "Cycle Length (k)": k,
        "Add Operations (Phase 1)": adds,
        "Delete Operations (Phase 2)": dels,
        "Total Reduction Steps": adds + dels
    })

# Format and print the results as a Markdown table
df = pd.DataFrame(results)
print(df.to_markdown(index=False, floatfmt=".0f"))
import sys
import math
import random
import numpy as np
import networkx as nx

# Ensure UTF-8 output across standard environments
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Deterministic initialization
random.seed(42)
np.random.seed(42)

def generate_bethe_fragment(N):
    """
    Generates a regular rooted Bethe tree DAG of size N.
    Root has out-degree 3; subsequent internal nodes have in-degree 1, out-degree 2.
    """
    if N < 3:
        raise ValueError("N must be at least 3")
    G = nx.DiGraph()
    root = 0
    G.add_node(root, depth=0)
    levels = [[root]]
    node_id = 1

    while G.number_of_nodes() < N:
        next_level = []
        if not levels[-1]:
            break
        current_depth = len(levels)
        for parent in levels[-1]:
            children = 3 if parent == root else 2
            for _ in range(children):
                if G.number_of_nodes() >= N:
                    break
                G.add_node(node_id, depth=current_depth)
                G.add_edge(parent, node_id, H=0)
                next_level.append(node_id)
                node_id += 1
        if not next_level:
            break
        levels.append(next_level)

    return G, levels

def inject_seed_defect(G, levels):
    """Injects a single symmetry-breaking 3-cycle defect at the root (H=1)."""
    if len(levels) >= 3 and levels[2]:
        root = levels[0][0]
        v = levels[1][0]
        w = levels[2][0]
        if not G.has_edge(w, root):
            G.add_edge(w, root, H=1)
    return G

def find_all_3_cycles(G):
    """Identifies all directed 3-cycles in G."""
    cycles = set()
    for u in G.nodes():
        for v in G.successors(u):
            for w in G.successors(v):
                if G.has_edge(w, u):
                    canonical = tuple(sorted([u, v, w]))
                    cycles.add(canonical)
    return list(cycles)

def execute_scheduler_tick(G, mu, lam):
    """
    Executes one discrete tick under scheduler operator U.
    Step 1: Awareness | Step 2: Proposals | Step 3: Merge | Step 4: Deletion
    """
    G_next = G.copy()
    cycles = find_all_3_cycles(G)

    stress_map = {n: 0 for n in G.nodes()}
    for u, v, w in cycles:
        stress_map[u] += 1
        stress_map[v] += 1
        stress_map[w] += 1

    candidate_additions = []
    for u in G.nodes():
        for w in G.successors(u):
            for v in G.successors(w):
                if u != v and not G.has_edge(v, u) and not G.has_edge(u, v):
                    s_add = stress_map[u] + stress_map[w] + stress_map[v]
                    p_acc = np.exp(-mu * s_add)
                    candidate_additions.append((v, u, p_acc))

    candidate_deletions = []
    for cycle in cycles:
        cycle_nodes = list(cycle)
        s_del = max(0, sum(stress_map[x] for x in cycle_nodes) - 1)
        q_del = min(1.0, 0.5 * (1.0 + lam * s_del) * np.exp(-mu * s_del))
        u, v, w = cycle
        edges = [(u, v), (v, w), (w, u)] if G.has_edge(u, v) and G.has_edge(v, w) and G.has_edge(w, u) else []
        if edges:
            chosen = random.choice(edges)
            candidate_deletions.append((chosen[0], chosen[1], q_del))

    accepted_adds = [chord for chord in candidate_additions if random.random() < chord[2]]
    accepted_dels = [edge for edge in candidate_deletions if random.random() < edge[2]]

    for v, u, _ in accepted_adds:
        preds = list(G_next.predecessors(v))
        max_h = max([G_next.edges[p, v].get('H', 0) for p in preds] + [0])
        G_next.add_edge(v, u, H=max_h + 1)

    for u, v, _ in accepted_dels:
        if G_next.has_edge(u, v):
            G_next.remove_edge(u, v)

    return G_next


def finite_depth_profile(vertices=100, trials=100, max_ticks=30):
    mu = 1 / np.sqrt(2 * np.pi)
    lam = np.e - 1
    baseline, _ = generate_bethe_fragment(N=vertices)
    depth = nx.get_node_attributes(baseline, "depth")
    changes = [depth[v] - depth[u] for v in baseline for w in baseline[v] for u in baseline[w]]
    assert changes and all(change == -2 for change in changes)
    print(f"Original outward two-path returns checked: {len(changes)}")

    survival = 0
    profile = {d: 0 for d in range(7)}
    for _ in range(trials):
        graph, levels = generate_bethe_fragment(N=vertices)
        graph = inject_seed_defect(graph, levels)
        for _ in range(max_ticks):
            if not find_all_3_cycles(graph):
                break
            graph = execute_scheduler_tick(graph, mu=mu, lam=lam)
        cycles = find_all_3_cycles(graph)
        survival += bool(cycles)
        for cycle in cycles:
            d = min(graph.nodes[v]["depth"] for v in cycle)
            if d in profile:
                profile[d] += 1

    print(f"Active fraction at the sampled stopping rule: {survival / trials:.4f}")
    for depth, count in profile.items():
        print(f"Depth {depth}: {count} final sampled triangles")


if __name__ == "__main__":
    finite_depth_profile()

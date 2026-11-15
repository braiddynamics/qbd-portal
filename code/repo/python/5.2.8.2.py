import sys
import collections
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
    """Identifies all unique directed 3-cycles (u -> v -> w -> u) in G."""
    cycles = []
    for u in G.nodes():
        for v in G.successors(u):
            if v <= u:
                continue
            for w in G.successors(v):
                if w > u and G.has_edge(w, u):
                    cycles.append((u, v, w))
    return cycles

def is_permissible_puc(G, u, v, w):
    """Enforces Parent-Uniqueness Condition PUC(G; u, v, w) for 2-path v -> w -> u."""
    if G.has_edge(v, u):
        return False
    for x in G.successors(v):
        if x != w and G.has_edge(x, u):
            return False
    return True

def pre_check_aec(G, u, v, H_new):
    """Bounded-horizon Acyclicity Evaluation Check (L_cut = floor(log2 N) + 3)."""
    N = G.number_of_nodes()
    L_cut = max(1, int(math.floor(math.log2(N))) + 3) if N > 1 else 1
    queue = collections.deque([(v, -1, 0)])
    min_h = {v: -1}
    while queue:
        curr, prev_h, depth = queue.popleft()
        if depth >= L_cut:
            continue
        for succ in G.successors(curr):
            edge_h = G[curr][succ].get('H', 0)
            if edge_h > prev_h:
                if succ == u and edge_h < H_new:
                    return False
                if edge_h < min_h.get(succ, 10**9):
                    min_h[succ] = edge_h
                    queue.append((succ, edge_h, depth + 1))
    return True

def execute_scheduler_tick(G, mu, lam):
    """
    Executes one discrete tick under scheduler operator U.
    Step 1: Awareness | Step 2: Proposals | Step 3: Reciprocal Filter & Merge | Step 4: Deletion
    """
    G_next = G.copy()
    cycles = find_all_3_cycles(G)

    stress_map = {n: 0 for n in G.nodes()}
    for u, v, w in cycles:
        stress_map[u] += 1
        stress_map[v] += 1
        stress_map[w] += 1

    legal_additions = []
    for v in G.nodes():
        for w in G.successors(v):
            for u in G.successors(w):
                if v == u or G.has_edge(u, v):
                    continue
                if not is_permissible_puc(G, u, v, w):
                    continue
                h_new = max((G.edges[p, u].get('H', 0) for p in G.predecessors(u)), default=0) + 1
                if not pre_check_aec(G, u, v, h_new):
                    continue
                legal_additions.append(((u, v), h_new, (v, w, u)))

    accepted_adds = []
    for (u, v), h_new, (nv, nw, nu) in legal_additions:
        s_add = stress_map[nv] + stress_map[nw] + stress_map[nu]
        p_acc = np.exp(-mu * s_add)
        if random.random() < p_acc:
            accepted_adds.append(((u, v), h_new))

    accepted_dels = []
    for u, v, w in cycles:
        s_del = max(0, stress_map[u] + stress_map[v] + stress_map[w] - 1)
        q_del = min(1.0, 0.5 * (1.0 + lam * s_del) * np.exp(-mu * s_del))
        if random.random() < q_del:
            chosen = random.choice([(u, v), (v, w), (w, u)])
            accepted_dels.append(chosen)

    add_edges = {edge for edge, _ in accepted_adds}
    filtered_adds = [
        ((u, v), h_new)
        for (u, v), h_new in accepted_adds
        if u != v and (v, u) not in add_edges
    ]
    for (u, v), h_new in filtered_adds:
        G_next.add_edge(u, v, H=h_new)

    for u, v in accepted_dels:
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

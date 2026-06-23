import numpy as np
import networkx as nx
import random
import math
from collections import defaultdict
from typing import Set, Tuple, List, Dict
# Utils
def find_all_3_cycles(G: nx.DiGraph):
    cycles = set()
    for u in G.nodes():
        for v in list(G.successors(u)):
            for w in list(G.successors(v)):
                if G.has_edge(w, u):
                    cycle_edges = frozenset([(u,v), (v,w), (w,u)])
                    cycles.add(cycle_edges)
    return [list(cycle) for cycle in cycles]
def is_permissible(G: nx.DiGraph, u, v, w) -> bool:
    for x in G.successors(u):
        if G.has_edge(x, v):
            return False
    return True
def _is_path_monotone(G: nx.DiGraph, path: list) -> bool:
    if len(path) < 2:
        return True
    for i in range(len(path) - 2):
        u, v = path[i], path[i+1]
        w = path[i+2]
        h1 = G.edges[u, v].get('H', 0)
        h2 = G.edges[v, w].get('H', 0)
        if not h1 < h2:
            return False
    return True
def pre_check_aec(G: nx.DiGraph, u: int, v: int, H_new: int) -> bool:
    N = G.number_of_nodes()
    cutoff = int(math.log(N)) + 3 if N > 1 else 1
    G.add_edge(u, v, H=H_new)
    try:
        for path in nx.all_simple_paths(G, source=v, target=u, cutoff=cutoff):
            if len(path) > 1:
                if _is_path_monotone(G, path):
                    last_node_in_path = path[-2]
                    H_last_leg = G.edges[last_node_in_path, u].get('H', 0)
                    if H_last_leg < H_new:
                        return False
    finally:
        G.remove_edge(u, v)
    return True
# QECC (unused directly, but for completeness)
def measure_local_geometric_stress(G: nx.DiGraph, node_set: Set[int]) -> int:
    if not node_set:
        return 0
    awareness_nodes = set(node_set)
    for node in node_set:
        awareness_nodes.update(G.predecessors(node))
        awareness_nodes.update(G.successors(node))
    subgraph = G.subgraph(awareness_nodes)
    all_cycles = find_all_3_cycles(subgraph)
    stress_count = 0
    for cycle_edges in all_cycles:
        cycle_nodes = {vv for e in cycle_edges for vv in e}
        if not cycle_nodes.isdisjoint(node_set):
            stress_count += 1
    return stress_count
# Graph setup
def generate_zpi_vacuum(num_nodes_approx: int) -> Tuple[nx.DiGraph, List[List[int]]]:
    if num_nodes_approx < 3:
        raise ValueError("num_nodes_approx must be at least 3 for a valid vacuum")
    G = nx.DiGraph()
    root = 0
    G.add_node(root)
    levels = [[root]]
    node_id = 1
    while G.number_of_nodes() < num_nodes_approx:
        next_level = []
        if not levels[-1]:
            break
        for parent in levels[-1]:
            children = 3 if parent == root else 2
            for _ in range(children):
                if G.number_of_nodes() >= num_nodes_approx:
                    break
                G.add_node(node_id)
                G.add_edge(parent, node_id, H=0)
                next_level.append(node_id)
                node_id += 1
        if not next_level:
            break
        levels.append(next_level)
    return G, levels
def inject_energic_event(G: nx.DiGraph, levels: list) -> nx.DiGraph:
    if len(levels) < 3 or (len(levels) >= 3 and not levels[2]):
        G_fallback = nx.DiGraph()
        G_fallback.add_edges_from([(0, 1, {'H': 1}),
                                  (1, 2, {'H': 1}),
                                  (2, 0, {'H': 1})])
        return G_fallback
    v = levels[0][0]
    w = levels[1][0]
    u = levels[2][0]
    G.add_edge(u, v, H=1)
    return G
# Config
config = {
    "T_VACUUM": math.log(2),
    "MU": 0.40,
    "LAMBDA": 1.7,
    "NUM_NODES_APPROX": 5,
    "SIMULATION_STEPS": 200,
}
# Dynamics helpers
def _calculate_add_proposals(G: nx.DiGraph, T: float, mu: float, stress_map: Dict[int, int]) -> Set[Tuple[Tuple[int, int], int]]:
    proposals_add: Set[Tuple[Tuple[int, int], int]] = set()
    DELTA_S_ADD = math.log(2.0)
    DELTA_F_ADD = -T * DELTA_S_ADD
    P_THERMO_ADD = 1.0
    for v in G.nodes():
        for w in list(G.successors(v)):
            for u in list(G.successors(w)):
                if v == u or G.has_edge(u, v):
                    continue
                if not is_permissible(G, u, v, w):
                    continue
                in_edges = G.in_edges(u, data=True)
                max_h_in = max((data.get('H', 0) for _, _, data in in_edges), default=0)
                H_new = max_h_in + 1
                proposed_edge = (u, v)
                if not pre_check_aec(G, u, v, H_new):
                    continue
                base_neighborhood = {v, w, u}
                stress_count = 0
                for node in base_neighborhood:
                    stress_count += stress_map.get(node, 0)
                f_friction = math.exp(-mu * stress_count)
                P_acc = f_friction * P_THERMO_ADD
                if random.random() < P_acc:
                    proposals_add.add(((u, v), H_new))
    return proposals_add
def _calculate_del_proposals(G: nx.DiGraph, T: float, mu: float, lam: float, all_cycles: List[list], stress_map: Dict[int, int]) -> Set[Tuple[int, int]]:
    proposals_del = set()
    DELTA_S_DEL = -math.log(2.0)
    DELTA_F_DEL = -T * DELTA_S_DEL
    Q_THERMO_DEL = 0.5
    for cycle_edges in all_cycles:
        base_nodes = {vv for e in cycle_edges for vv in e}
        stress_count = 0
        for node in base_nodes:
            stress_count += stress_map.get(node, 0)
        local_stress = max(0, stress_count - 1)
        f_friction = math.exp(-mu * local_stress)
        f_catalysis_del = (1.0 + lam * local_stress)
        Q_del_raw = f_friction * f_catalysis_del * Q_THERMO_DEL
        Q_del = min(1.0, Q_del_raw)
        if random.random() < Q_del:
            edge = random.choice(list(cycle_edges))
            proposals_del.add(edge)
    return proposals_del
# Modified evolve
def modified_evolve(G: nx.DiGraph, config: dict, add_counter: defaultdict, del_counter: defaultdict):
    T = config["T_VACUUM"]
    mu = config["MU"]
    lam = config["LAMBDA"]
    max_steps = config["SIMULATION_STEPS"]
    for step in range(max_steps):
        all_cycles = find_all_3_cycles(G)
        stress_map: Dict[int, int] = {}
        for cycle_edges in all_cycles:
            cycle_nodes = {vv for e in cycle_edges for vv in e}
            for node in cycle_nodes:
                stress_map[node] = stress_map.get(node, 0) + 1
        proposals_add = _calculate_add_proposals(G, T, mu, stress_map)
        proposals_del = _calculate_del_proposals(G, T, mu, lam, all_cycles, stress_map)
        # Count
        for (u,v), h in proposals_add:
            add_counter[(u,v)] += 1
        for e in proposals_del:
            del_counter[e] += 1
        # Apply
        edges_to_add = [(u, v, {'H': h}) for (u,v), h in proposals_add]
        G.add_edges_from(edges_to_add)
        existing_dels = proposals_del.intersection(G.edges())
        G.remove_edges_from(existing_dels)
    return G
# Run
random.seed(42) # For repro
G, levels = generate_zpi_vacuum(config["NUM_NODES_APPROX"])
G = inject_energic_event(G, levels)
add_c = defaultdict(int)
del_c = defaultdict(int)
G_final = modified_evolve(G, config, add_c, del_c)
N = G.number_of_nodes()
steps = config["SIMULATION_STEPS"]
T = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        if i != j:
            T[i, j] = (add_c[(i, j)] - del_c[(i, j)]) / steps
out_sums = np.sum(T, axis=1)
in_sums = np.sum(T, axis=0)
total_sums = out_sums + in_sums
print('T_ab matrix (rows: from a, cols: to b):')
print(np.round(T, 4))
print('\nOutgoing sums ∑_b T_ab:', np.round(out_sums, 4))
print('Incoming sums ∑_b T_ba:', np.round(in_sums, 4))
print('Total flux sums:', np.round(total_sums, 4))
print('Max |out|:', np.max(np.abs(out_sums)))
print('Max |in|:', np.max(np.abs(in_sums)))
print('Max |total|:', np.max(np.abs(total_sums)))
print('Equil: Total edges at end:', G.number_of_edges())

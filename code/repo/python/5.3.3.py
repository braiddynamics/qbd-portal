"""Simulate the four-step parallel Bethe-tree rewrite scheduler under homeostatic stopping across the friction corridor."""

import collections
from concurrent.futures import ProcessPoolExecutor
import math
import random


def generate_bethe_fragment(n):
    succ = [set() for _ in range(n)]
    pred = [{} for _ in range(n)]
    frontier = [0]
    node_id = 1
    while node_id < n and frontier:
        next_level = []
        for parent in frontier:
            children = 3 if parent == 0 else 2
            for _ in range(children):
                if node_id >= n:
                    break
                succ[parent].add(node_id)
                pred[node_id][parent] = 0
                next_level.append(node_id)
                node_id += 1
        frontier = next_level
    return succ, pred


def inject_seed_defect(succ, pred):
    first_child = min(succ[0])
    grandchild = min(succ[first_child])
    succ[grandchild].add(0)
    pred[0][grandchild] = 1


def find_all_3_cycles(succ):
    cycles = []
    for u, s_u in enumerate(succ):
        for v in sorted(s_u):
            if v <= u:
                continue
            for w in sorted(succ[v]):
                if w > u and u in succ[w]:
                    cycles.append((u, v, w))
    return cycles


def is_permissible_puc(succ, u, v, w):
    if u in succ[v]:
        return False
    for x in succ[v]:
        if x != w and u in succ[x]:
            return False
    return True


def pre_check_aec(succ, pred, u, v, h_new, l_cut):
    q = collections.deque([(v, -1, 0)])
    min_h = {v: -1}
    while q:
        curr, prev_h, depth = q.popleft()
        if depth >= l_cut:
            continue
        for nxt in succ[curr]:
            eh = pred[nxt][curr]
            if eh > prev_h:
                if nxt == u and eh < h_new:
                    return False
                if eh < min_h.get(nxt, 10**9):
                    min_h[nxt] = eh
                    q.append((nxt, eh, depth + 1))
    return True


def execute_parallel_tick(succ, pred, mu, lam, l_cut, rng):
    cycles = find_all_3_cycles(succ)
    legal_adds = []
    for v, s_v in enumerate(succ):
        for w in sorted(s_v):
            for u in sorted(succ[w]):
                if v == u or v in succ[u]:
                    continue
                if not is_permissible_puc(succ, u, v, w):
                    continue
                h_new = max(pred[u].values(), default=0) + 1
                if not pre_check_aec(succ, pred, u, v, h_new, l_cut):
                    continue
                legal_adds.append((u, v, h_new, v, w, u))

    if not legal_adds and not cycles:
        return False, 0

    stress = [0] * len(succ)
    for u, v, w in cycles:
        stress[u] += 1
        stress[v] += 1
        stress[w] += 1

    adds = []
    for u, v, h_new, nv, nw, nu in legal_adds:
        s_add = stress[nv] + stress[nw] + stress[nu]
        if rng.random() < math.exp(-mu * s_add):
            adds.append((u, v, h_new))

    dels = []
    for u, v, w in cycles:
        s_del = max(0, stress[u] + stress[v] + stress[w] - 1)
        q_del = min(1.0, 0.5 * (1.0 + lam * s_del) * math.exp(-mu * s_del))
        if rng.random() < q_del:
            edge = ((u, v), (v, w), (w, u))[rng.randrange(3)]
            dels.append(edge)

    add_pairs = {(u, v) for u, v, _ in adds}
    retained = [(u, v, h) for u, v, h in adds if u != v and (v, u) not in add_pairs]

    for u, v, h_new in retained:
        succ[u].add(v)
        pred[v][u] = h_new
    for u, v in dels:
        if v in succ[u]:
            succ[u].remove(v)
            del pred[v][u]

    return True, len(retained) + len(dels)


def run_trajectory(args):
    seed, n, mu, lam, max_ticks = args
    rng = random.Random(seed)
    succ, pred = generate_bethe_fragment(n)
    inject_seed_defect(succ, pred)
    l_cut = max(1, int(math.floor(math.log2(n))) + 3)

    steps = 0
    for tick in range(1, max_ticks + 1):
        steps = tick
        active, changed = execute_parallel_tick(succ, pred, mu, lam, l_cut, rng)
        if not active or changed == 0:
            break
    return len(find_all_3_cycles(succ)), steps


def evaluate_point(pool, mu, lam, n=100, trials=100, max_ticks=100, seed_base=1000):
    tasks = [(seed_base + i, n, mu, lam, max_ticks) for i in range(trials)]
    results = list(pool.map(run_trajectory, tasks))
    n3_list = [r[0] for r in results]
    dur_list = [r[1] for r in results]
    surv = [c for c in n3_list if c > 0]
    p_surv = len(surv) / trials
    rho_all = sum(n3_list) / (trials * n)
    n3_qsd = sum(surv) / len(surv) if surv else 0.0
    rho_qsd = n3_qsd / n
    mean_dur = sum(dur_list) / trials
    return p_surv, rho_all, rho_qsd, n3_qsd, mean_dur


def main():
    mu_0 = 1.0 / math.sqrt(2.0 * math.pi)
    lam_0 = math.e - 1.0
    n_nodes = 100
    max_ticks = 100
    mu_grid = [
        ("0.2000 (Extinction)", 0.20, 60, 1000),
        ("0.3000 (Subcritical)", 0.30, 60, 2000),
        ("0.3500 (Lower Edge)", 0.35, 60, 3000),
        ("0.3989 (mu_0 Design)", mu_0, 100, 0),
        ("0.4500 (Viable Core)", 0.45, 60, 4000),
        ("0.5500 (Upper Edge)", 0.55, 60, 5000),
        ("0.6500 (Jammed)", 0.65, 60, 6000),
    ]

    print("Discrete Four-Step Parallel Scheduler Corridor Sweep (tau_homeo, K=1)")
    print("=" * 78)
    print(f"Substrate: Bethe Fragment (N={n_nodes}, b=2) | lambda_0={lam_0:.6f} | T_max={max_ticks}")
    print("-" * 78)
    print(f"{'Friction mu':<21} | {'Trials':>6} | {'p_surv':>6} | {'<rho>_all':>9} | {'<rho>_QSD':>9} | {'<N3>_QSD':>8} | {'<tau>':>5}")
    print("-" * 78)

    with ProcessPoolExecutor() as pool:
        for label, mu_val, trials, seed_base in mu_grid:
            p_surv, rho_all, rho_qsd, n3_qsd, mean_dur = evaluate_point(
                pool, mu_val, lam_0, n=n_nodes, trials=trials, max_ticks=max_ticks, seed_base=seed_base
            )
            print(
                f"{label:<21} | {trials:>6d} | {p_surv:6.4f} | {rho_all:9.6f} | "
                f"{rho_qsd:9.6f} | {n3_qsd:8.2f} | {mean_dur:5.1f}"
            )


if __name__ == "__main__":
    main()

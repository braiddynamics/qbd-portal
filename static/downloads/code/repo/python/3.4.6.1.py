# §3.4.6.1 — Simulated Ignition Trajectories
# Checks: First-tick burst ignition probability and barrier crossing across finite N

import math
import networkx as nx
import pandas as pd


def generate_bethe_fragment(N: int = 100) -> nx.DiGraph:
    """Construct an outward-directed regular Bethe fragment with k_deg = 3."""
    G = nx.DiGraph()
    G.add_node(0)
    current_node = 1
    queue = []

    # Root has 3 outgoing children
    for _ in range(3):
        if current_node < N:
            G.add_node(current_node)
            G.add_edge(0, current_node, H=0)
            queue.append(current_node)
            current_node += 1

    # Internal vertices have 2 outgoing children
    while queue and current_node < N:
        parent = queue.pop(0)
        for _ in range(2):
            if current_node < N:
                G.add_node(current_node)
                G.add_edge(parent, current_node, H=0)
                queue.append(current_node)
                current_node += 1

    return G


def inject_seed_defect(G: nx.DiGraph) -> nx.DiGraph:
    """Inject a single directed 3-cycle connecting grandchild to root with H=1."""
    children = list(G.successors(0))
    if children:
        w = children[0]
        grandchildren = list(G.successors(w))
        if grandchildren:
            G.add_edge(grandchildren[0], 0, H=1)
    return G


def find_all_3_cycles(G: nx.DiGraph) -> list:
    """Identify all directed 3-cycles in the graph."""
    cycles = []
    for u in G.nodes():
        for v in G.successors(u):
            for w in G.successors(v):
                if G.has_edge(w, u) and u < v and u < w:
                    cycles.append([(u, v), (v, w), (w, u)])
    return cycles


def find_legal_addition_sites(G: nx.DiGraph) -> list:
    """Identify candidate 2-paths satisfying the Parent-Uniqueness Condition."""
    sites = []
    for v in G.nodes():
        for w in list(G.successors(v)):
            for u in list(G.successors(w)):
                if v == u or G.has_edge(u, v):
                    continue
                # Parent-Uniqueness Condition (PUC) check
                puc = True
                for x in G.successors(v):
                    if x != w and G.has_edge(x, u):
                        puc = False
                        break
                if not puc:
                    continue
                sites.append((v, w, u))
    return sites


def run_ignition_census() -> pd.DataFrame:
    """Evaluate first-tick ignition probability and burst density across system sizes."""
    mu_0 = 1.0 / math.sqrt(2.0 * math.pi)
    lambda_0 = math.e - 1.0
    rho_c = 1.0 / (2.0 * (9.0 - 3.0 * lambda_0))

    results = []
    for N in [50, 100, 200, 500, 1000]:
        G = generate_bethe_fragment(N)
        G = inject_seed_defect(G)

        legal_sites = find_legal_addition_sites(G)
        root_sites = [s for s in legal_sites if s[0] == 0]

        # Tree-supported sites have zero addition stress: P_acc(0) = 1.0
        p_acc_0 = math.exp(-mu_0 * 0.0)
        p_ign = 1.0 - (1.0 - p_acc_0) ** len(root_sites) if root_sites else 1.0

        # Execute parallel additions on tick 1
        for (v, w, u) in legal_sites:
            G.add_edge(u, v, H=1)

        n3_t1 = len(find_all_3_cycles(G))
        rho_t1 = n3_t1 / float(N)

        results.append({
            "Vertices (N)": N,
            "Root 2-Paths (M_1)": len(root_sites),
            "Total 2-Paths": len(legal_sites),
            "P_acc(0)": f"{p_acc_0:.4f}",
            "P(Ignition)": f"{p_ign:.4f}",
            "Burst Density rho(t=1)": f"{rho_t1:.4f}",
            "Barrier rho_c": f"{rho_c:.4f}",
            "Jump Ratio (rho/rho_c)": f"{rho_t1/rho_c:.2f}x"
        })

    return pd.DataFrame(results)


if __name__ == "__main__":
    df = run_ignition_census()
    print(df.to_markdown(index=False))

def _calculate_add_proposals(G: nx.DiGraph, T: float, mu: float, stress_map: Dict[int, int]) -> Set[Tuple[Tuple[int, int], int]]:
    proposals_add = set()
    P_THERMO_ADD = 1.0 # Exact from T=ln2
    for v in G.nodes():
        for w in G.successors(v):
            for u in G.successors(w):
                if v == u or G.has_edge(u, v): continue
                if not is_permissible(G, u, v, w): continue # PUC
                max_h_in = max((data.get('H', 0) for _, _, data in G.in_edges(u)), default=0)
                H_new = max_h_in + 1
                proposed_edge = (u, v)
                if not pre_check_aec(G, u, v, H_new): continue # AEC
                base_neighborhood = {v, w, u}
                stress_count = sum(stress_map.get(node, 0) for node in base_neighborhood)
                f_friction = math.exp(-mu * stress_count)
                P_acc = f_friction * P_THERMO_ADD
                if random.random() < P_acc: proposals_add.add(((u, v), H_new))
    return proposals_add

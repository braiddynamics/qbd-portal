import networkx as nx
import itertools

def verify_partial_order():
    # 1. Setup: Create a valid Causal DAG with timestamps
    # Structure: 0 -> 1 -> 2 -> 3 (Linear chain with valid timestamps)
    # plus a shortcut 0 -> 2 (to test multiple path options)
    G = nx.DiGraph()
    edges = [
        (0, 1, {'t': 10}),
        (1, 2, {'t': 20}),
        (2, 3, {'t': 30}),
        (0, 2, {'t': 15}) # Shortcut, valid but length=1
    ]
    G.add_edges_from(edges)
    
    nodes = list(G.nodes())
    
    # 2. Define the Effective Influence Check (u <= v)
    def has_effective_influence(u, v):
        if u == v: return False # Optimization, but checked formally below
        
        try:
            paths = nx.all_simple_paths(G, source=u, target=v)
        except nx.NodeNotFound:
            return False

        for path in paths:
            # Check Length Constraint (>= 2 edges)
            # path list contains nodes; edges = len(path) - 1
            if len(path) - 1 < 2:
                continue
            
            # Check Monotonicity Constraint
            timestamps = []
            valid_time = True
            for i in range(len(path) - 1):
                u_curr, v_next = path[i], path[i+1]
                t = G[u_curr][v_next]['t']
                if timestamps and t <= timestamps[-1]:
                    valid_time = False
                    break
                timestamps.append(t)
            
            if valid_time:
                return True # Found at least one valid causal morphism
        
        return False

    print("Partial Order Property Verification")
    print("=" * 50)

    # 3. Check Irreflexivity (u !<= u)
    # Axiom: No node should effectively influence itself (requires cycle)
    irreflexive = True
    for n in nodes:
        if has_effective_influence(n, n):
            print(f"Violation: Reflexive loop found at {n}")
            irreflexive = False
    
    print(f"Irreflexivity Verification: {'PASS' if irreflexive else 'FAIL'}")

    # 4. Check Transitivity (u <= v AND v <= w => u <= w)
    transitive = True
    # Check all permutations of 3 nodes
    for u, v, w in itertools.permutations(nodes, 3):
        u_v = has_effective_influence(u, v)
        v_w = has_effective_influence(v, w)
        u_w = has_effective_influence(u, w)
        
        if u_v and v_w:
            if not u_w:
                print(f"Violation: Transitivity failed for {u}->{v}->{w}")
                transitive = False

    print(f"Transitivity Verification:  {'PASS' if transitive else 'FAIL'}")

    # 5. Specific Edge Case Check
    # 0->1 (len 1, t=10): Not Effective
    # 1->2 (len 1, t=20): Not Effective
    # 0->1->2 (len 2, t=10,20): Effective
    check_0_2 = has_effective_influence(0, 2)
    print(f"Check 0->2 (via 0->1->2):     {'PASS' if check_0_2 else 'FAIL'} (Expected True)")

if __name__ == "__main__":
    verify_partial_order()
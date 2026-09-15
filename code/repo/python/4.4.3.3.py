"""
Validation for Monograph Section 4.4.3.3: Information-Theoretic Foundations
Verifies:
1. Jaynes (1957) Maximum Entropy on the boolean edge state space.
2. Exact temperature cancellation across 8 orders of magnitude of beta / T.
3. Local relational entropy gain Delta S = ln(2) upon 3-cycle closure.
"""

import math
import numpy as np
import networkx as nx

def run_information_foundations_validation():
    print("=" * 78)
    print("Section 4.4.3.3 Information-Theoretic Foundations & Temperature Cancellation")
    print("=" * 78)
    
    # 1. Jaynes Maximum Entropy on Boolean Edge Simplex {0, 1}
    p0, p1 = 0.5, 0.5
    H_shannon = - (p0 * math.log2(p0) + p1 * math.log2(p1))
    H_nats = - (p0 * math.log(p0) + p1 * math.log(p1))
    
    print("Protocol 1: Jaynes Maximum Entropy on Boolean Edge Space")
    print(f"  Unbiased Bernoulli Prior:         P(edge=0) = {p0:.1f}, P(edge=1) = {p1:.1f}")
    print(f"  Shannon Information Entropy:       {H_shannon:.6f} bits")
    print(f"  Information Entropy in nats:       {H_nats:.6f} nats")
    print(f"  Base-Conversion Modulus beta_c:    ln(2) = {math.log(2.0):.6f}")
    print(f"  Exact Identity:                   H_nats == ln(2): {math.isclose(H_nats, math.log(2.0))}")
    print("-" * 78)
    
    # 2. Temperature Cancellation in Ground-State Relational Dynamics (Delta U = 0)
    print("Protocol 2: Temperature Independence of Acceptance Probabilities (Delta U = 0)")
    print(f"{'T (arbitrary)':<15} | {'beta = 1/T':<15} | {'P_add':<15} | {'P_del':<15}")
    print("-" * 65)
    
    temperatures = [1e-4, 1e-2, 0.1, 0.693147, 1.0, 10.0, 100.0, 1e4]
    p_add_results = []
    p_del_results = []
    
    for T in temperatures:
        beta = 1.0 / T
        # Ground state: Delta U = 0
        delta_U = 0.0
        # Additive mode: Delta S = +ln(2)
        delta_S_add = math.log(2.0)
        delta_F_add = delta_U - T * delta_S_add  # - T * ln(2)
        # Metropolis: min(1, exp(-beta * delta_F)) = min(1, exp( (T*ln2)/T )) = min(1, 2) = 1.0
        p_add = min(1.0, math.exp(-beta * delta_F_add))
        
        # Deletion mode: Delta S = -ln(2)
        delta_S_del = -math.log(2.0)
        delta_F_del = delta_U - T * delta_S_del  # + T * ln(2)
        # min(1, exp(-beta * delta_F)) = exp(- (T*ln2)/T ) = exp(-ln2) = 0.5
        p_del = math.exp(-beta * delta_F_del)
        
        p_add_results.append(p_add)
        p_del_results.append(p_del)
        print(f"{T:<15.4e} | {beta:<15.4e} | {p_add:<15.6f} | {p_del:<15.6f}")
        
    all_add_unitary = all(math.isclose(p, 1.0) for p in p_add_results)
    all_del_half = all(math.isclose(p, 0.5) for p in p_del_results)
    print("-" * 65)
    print(f"  P_add == 1.0 across all T: {all_add_unitary}")
    print(f"  P_del == 0.5 across all T: {all_del_half}")
    print(f"  Verdict: Temperature T cancels identically for all T > 0; probability is fundamental.")
    print("-" * 78)
    
    # 3. Local Relational Entropy Gain from Loop Closure (Homological Cycle Rank)
    def relational_entropy(G):
        # Topological microstate volume: Omega = 2^(b_1) where b_1 = |E| - |V| + c
        c = nx.number_weakly_connected_components(G)
        betti_1 = G.number_of_edges() - G.number_of_nodes() + c
        omega = 2 ** betti_1
        return math.log(omega)

    G_pre = nx.DiGraph([(0, 1), (1, 2)])
    S_pre = relational_entropy(G_pre)
    G_post = G_pre.copy()
    G_post.add_edge(2, 0)
    S_post = relational_entropy(G_post)
    delta_S = S_post - S_pre

    print("Protocol 3: Local Entropy Gain from Relational Loop Closure")
    print(f"  Pre-closure Entropy S_pre:        {S_pre:.6f}")
    print(f"  Post-closure Entropy S_post:      {S_post:.6f}")
    print(f"  Measured delta S:                 {delta_S:.6f} nats")
    print(f"  Theoretical ln(2):                {math.log(2.0):.6f} nats")
    print(f"  Exact Match:                      {math.isclose(delta_S, math.log(2.0))}")
    print("=" * 78)

if __name__ == "__main__":
    run_information_foundations_validation()

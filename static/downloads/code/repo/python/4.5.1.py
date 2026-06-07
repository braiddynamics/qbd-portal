def R(annotated_graph, T, mu, lambda_cat):
    """
    Takes an annotated graph T(G) = (G, \sigma) and returns a
    probability distribution over successor graphs \mathbb{P}(G_t+1).
    Constants T, mu, lambda_cat derived in the **thermodynamic parameters section** [(§4.4)](/monograph/rules/dynamics/4.4/#4.4).
    """
    # --- 1. SCAN & FILTER (The "Brakes") ---
    # Find all PUC-compliant 2-paths (for Addition) and 3-cycles (for Deletion)
    compliant_2_paths = _find_compliant_sites(G)
    existing_3_cycles = _find_all_3_cycles(G)
    
    add_proposals = []
    del_proposals = []
    
    # --- 2. VALIDATE & CALCULATE PROBABILITIES (Engine + Friction) ---
    
    # A) Process all ADD proposals (Generative Drive)
    for (v, w, u) in compliant_2_paths:
        proposed_edge = (u, v)
        
        # A.1) The AEC Pre-Check (Axiom 3 "Brake")
        # Deterministically reject paradoxes before probability calculation
        if not pre_check_aec(G, proposed_edge):
            continue 
            
        # A.2) The Thermodynamic "Engine"
        # Base probability is 1.0 (Barrierless Creation at Criticality)
        P_thermo_add = 1.0
        
        # A.3) The "Friction" (Modulation by Local Stress)
        stress = measure_local_stress(G, {v, w, u})
        f_friction = exp(-mu * stress)
        
        # The full probability for this single event
        P_acc = f_friction * P_thermo_add
        
        # Assign Monotonic Timestamp
        H_new = 1 + max([H[e] for e in G.in_edges(u)] or [0])
        add_proposals.append( (proposed_edge, H_new, P_acc) )

    # B) Process all DELETE proposals (Entropic Balance)
    for cycle in existing_3_cycles:
        # B.1) The Thermodynamic "Engine"
        # Base probability is 0.5 (Entropic Penalty of Erasure)
        P_del_thermo = 0.5
        
        # B.2) The "Catalysis" (Modulation by Tension)
        # Stress *excluding* this cycle's own contribution
        stress = measure_local_stress(G, cycle.nodes) - 1
        f_catalysis = (1 + lambda_cat * max(0, stress))
        
        # The full probability for this single event
        P_del = min(1.0, f_catalysis * P_del_thermo)
        del_proposals.append( (cycle, P_del) )

    # --- 3. RETURN THE PROBABILITY DISTRIBUTION ---
    # The output is the ensemble of weighted proposals.
    # The realization (sampling/collapse) occurs in the **Evolution Operator U** [(§4.6)](/monograph/rules/dynamics/4.6/#4.6).
    return (add_proposals, del_proposals)

# /model/dynamics.py
import random
import math
from typing import Set, Tuple, List, Dict
import networkx as nx
from model.qecc import measure_local_geometric_stress
from model.utils import (
    find_all_3_cycles,
    is_permissible,
    pre_check_aec
)
from model.observables import get_n3_count

# --- PRIVATE HELPER FUNCTIONS (The "Physics" Logic of R) ---

def _calculate_add_proposals(G: nx.DiGraph, T: float, mu: float,
                             stress_map: Dict[int, int] # Pass in the cache
                             ) -> Set[Tuple[Tuple[int, int], int]]:
    """
    Calculates all stochastic 3-cycle creation proposals for this tick.

    
    This function is N-agnostic and α-agnostic, implementing the "micro-rule".
    It computes P_acc_thermo = 1 *exactly*.
    """
    proposals_add: Set[Tuple[Tuple[int, int], int]] = set()
    
    # Pre-calculate the exact, constant thermodynamic values
    # These are universal constants of the micro-rule.
    DELTA_S_ADD = math.log(2.0)
    DELTA_F_ADD = -T * DELTA_S_ADD  # ΔF = -(ln2)^2
    
    # P_thermo = min(1.0, exp(-ΔF_add / T))
    # P_thermo = min(1.0, exp( (T*ln2) / T ))
    # P_thermo = min(1.0, exp(ln2)) = min(1.0, 2.0) = 1.0
    P_THERMO_ADD = 1.0

    for v in G.nodes():
        for w in list(G.successors(v)):
            for u in list(G.successors(w)):
                if v == u or G.has_edge(u, v):
                    continue
                if not is_permissible(G, u, v, w): # PUC check
                    continue

                in_edges = G.in_edges(u, data=True)
                max_h_in = max((data.get('H', 0) for _, _, data in in_edges), default=0)
                H_new = max_h_in + 1
                
                proposed_edge = (u, v)
                if not pre_check_aec(G, u, v, H_new): # AEC pre-check
                    continue

                # --- Awareness: Use Stress Map Cache ---
                base_neighborhood = {v, w, u}
                stress_count = 0
                for node in base_neighborhood:
                    stress_count += stress_map.get(node, 0)
                # --- END AWARENESS ---

                # --- Calculate Acceptance Probability ---
                # f(σ) is the computational friction from PUC/AEC
                f_friction = math.exp(-mu * stress_count)
                
                # P_acc = f(σ) * P_acc_thermo
                # P_acc_thermo is *exactly* 1.
                P_acc = f_friction * P_THERMO_ADD

                if random.random() < P_acc:
                    proposals_add.add(((u, v), H_new))
                    
    return proposals_add

def _calculate_del_proposals(G: nx.DiGraph, T: float, mu: float, lam: float,
                             all_cycles: List[list],    # Pass in all cycles
                             stress_map: Dict[int, int] # Pass in the cache
                             ) -> Set[Tuple[int, int]]:
    """
    Calculates all stochastic 3-cycle deletion proposals for this tick.
    This function is N-agnostic and α-agnostic, implementing the "micro-rule".
    It computes Q_del_thermo = 1/2 *exactly*.
    """
    proposals_del = set()

    # Pre-calculate the constant thermodynamic values
    DELTA_S_DEL = -math.log(2.0)
    DELTA_F_DEL = -T * DELTA_S_DEL  # ΔF = +(ln2)^2
    
    # Q_thermo = min(1.0, exp(-ΔF_del / T))
    # Q_thermo = min(1.0, exp( -(T*ln2) / T ))
    # Q_thermo = min(1.0, exp(-ln2)) = min(1.0, 0.5) = 0.5
    Q_THERMO_DEL = 0.5

    for cycle_edges in all_cycles:
        base_nodes = {v for e in cycle_edges for v in e}

        # --- Awareness: Use Stress Map Cache ---
        stress_count = 0
        for node in base_nodes:
            stress_count += stress_map.get(node, 0)
        # --- END AWARENESS ---

        # The "local stress" for catalysis/friction excludes the
        # cycle's *own* contribution to the stress count.
        local_stress = max(0, stress_count - 1)
        
        # --- Calculate Deletion Probability ---
        f_friction = math.exp(-mu * local_stress)
        f_catalysis_del = (1.0 + lam * local_stress) # Catalysis from other cycles
        
        # Q_del = f(σ) * Q_del_thermo
        # Q_del_thermo is *exactly* 1/2.
        Q_del_raw = f_friction * f_catalysis_del * Q_THERMO_DEL
        Q_del = min(1.0, Q_del_raw) # Cap probability at 1.0

        if random.random() < Q_del:
            edge = random.choice(list(cycle_edges))
            proposals_del.add(edge)
            
    return proposals_del


# --- Rate-based stress-energy measurements ---

def build_stress_map(G: nx.DiGraph) -> Tuple[List[list], Dict[int, int]]:
    """
    Build the awareness stress cache used by the micro-rule R.

    Returns:
        (all_cycles, stress_map) where stress_map[node] is the number of
        3-cycles incident on that node.
    """
    all_cycles = find_all_3_cycles(G)
    stress_map: Dict[int, int] = {}
    for cycle_edges in all_cycles:
        cycle_nodes = {v for e in cycle_edges for v in e}
        for node in cycle_nodes:
            stress_map[node] = stress_map.get(node, 0) + 1
    return all_cycles, stress_map


def compute_add_rates(G: nx.DiGraph, T: float, mu: float,
                      stress_map: Dict[int, int]
                      ) -> Dict[Tuple[int, int], float]:
    """
    Deterministic add-acceptance probabilities for compliant 2-paths.

    Mirrors the micro-rule in _calculate_add_proposals but returns
    P_acc for each candidate edge (u, v) instead of Bernoulli samples.
    N-agnostic and α-agnostic. Does not mutate G.
    """
    rates: Dict[Tuple[int, int], float] = {}
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

                if not pre_check_aec(G, u, v, H_new):
                    continue

                base_neighborhood = {v, w, u}
                stress_count = sum(stress_map.get(node, 0) for node in base_neighborhood)
                f_friction = math.exp(-mu * stress_count)
                P_acc = f_friction * P_THERMO_ADD
                # Multiple 2-paths may close the same edge; keep max weight.
                rates[(u, v)] = max(rates.get((u, v), 0.0), P_acc)

    return rates


def compute_del_rates(G: nx.DiGraph, T: float, mu: float, lam: float,
                      all_cycles: List[list],
                      stress_map: Dict[int, int]
                      ) -> Dict[Tuple[int, int], float]:
    """
    Deterministic deletion probabilities attributed to edges in 3-cycles.

    Mirrors the micro-rule in _calculate_del_proposals. When a cycle is
    selected for deletion, one of its three edges is chosen uniformly;
    the per-edge rate therefore receives Q_del / 3 from each parent cycle.
    Does not mutate G.
    """
    rates: Dict[Tuple[int, int], float] = {}
    Q_THERMO_DEL = 0.5

    for cycle_edges in all_cycles:
        base_nodes = {v for e in cycle_edges for v in e}
        stress_count = sum(stress_map.get(node, 0) for node in base_nodes)
        local_stress = max(0, stress_count - 1)

        f_friction = math.exp(-mu * local_stress)
        f_catalysis_del = (1.0 + lam * local_stress)
        Q_del = min(1.0, f_friction * f_catalysis_del * Q_THERMO_DEL)

        edge_list = list(cycle_edges)
        if not edge_list:
            continue
        share = Q_del / len(edge_list)
        for edge in edge_list:
            # Normalize frozenset-style cycle members to ordered tuples.
            if isinstance(edge, tuple) and len(edge) == 2:
                e = edge
            else:
                e = tuple(edge)
            rates[e] = rates.get(e, 0.0) + share

    return rates


def compute_proposal_rates(G: nx.DiGraph, config: dict
                           ) -> Tuple[Dict[Tuple[int, int], float],
                                      Dict[Tuple[int, int], float]]:
    """
    Compute (P_add, P_del) maps for the current graph snapshot.

    Public entry point for stress-energy tensor construction. Leaves the
    stochastic evolve path untouched.
    """
    T = config["T_VACUUM"]
    mu = config["MU"]
    lam = config["LAMBDA"]
    all_cycles, stress_map = build_stress_map(G)
    p_add = compute_add_rates(G, T, mu, stress_map)
    p_del = compute_del_rates(G, T, mu, lam, all_cycles, stress_map)
    return p_add, p_del


# --- PUBLIC EVOLUTION FUNCTION (The "Scheduler" / Operator E) ---

def evolve_graph_to_equilibrium(G: nx.DiGraph, config: dict):
    """
    Runs the qbd simulation to approach a homeostatic equilibrium.
    (Implements the Evolution Operator E)
    
    This function is the "Macro" loop. It sets up the parameters
    and calls the "Micro" rules (_calculate_add/del_proposals).
    
    Crucially, it *does not* pass 'N' or 'alpha' to the micro-rules,
    as they are N-agnostic and α-agnostic.
    """
    N = G.number_of_nodes()
    if N == 0:
        return G, 0

    # Load foundational constants for the local micro-rules
    T = config["T_VACUUM"]  # T = ln(2)
    mu = config["MU"]
    lam = config["LAMBDA"]
    max_steps = config["SIMULATION_STEPS"]
    
    # NOTE: 'alpha' is *not* loaded here because it is not used
    # by the local rewrite rule R. It is a macroscopic descriptive
    # constant for post-simulation analysis.

    for step in range(max_steps):
        
        # --- Build Stress Map (Optimization) ---
        # 1. Find all cycles ONCE (Awareness)
        all_cycles = find_all_3_cycles(G)
        
        # 2. Build the stress cache for this step
        stress_map: Dict[int, int] = {} 
        for cycle_edges in all_cycles:
            cycle_nodes = {v for e in cycle_edges for v in e}
            for node in cycle_nodes:
                stress_map[node] = stress_map.get(node, 0) + 1
        # --- END OPTIMIZATION ---

        # --- AWARENESS & STOCHASTIC ACTION ---
        # Call the N-agnostic, α-agnostic micro-rules.
        proposals_add = _calculate_add_proposals(G, T, mu, stress_map)
        proposals_del = _calculate_del_proposals(G, T, mu, lam, all_cycles, stress_map)

        # --- EQUILIBRIUM CHECK ---
        if not proposals_add and not proposals_del:
            return G, step + 1  # System is stable

        # --- COLLAPSE ---
        edges_to_add = [(edge[0], edge[1], {'H': h_val}) 
                          for edge, h_val in proposals_add]
        G.add_edges_from(edges_to_add)
        
        # Ensure we only remove edges that still exist
        G.remove_edges_from(proposals_del.intersection(G.edges()))
        
    return G, max_steps
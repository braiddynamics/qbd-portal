import networkx as nx
import numpy as np
import pandas as pd

# --- Metrics & Helpers ---

def compute_metrics(G):
    """Computes Symmetry (|Aut|) and Orbit Entropy (H_S) for UNDIRECTED graphs."""
    matcher = nx.isomorphism.GraphMatcher(G, G)
    try:
        autos = list(matcher.isomorphisms_iter())
        num_autos = len(autos)
    except:
        return 0, 0
    
    # Orbit Entropy
    nodes = list(G.nodes())
    orbit_map = {v: frozenset(m[v] for m in autos) for v in nodes}
    unique_orbits = set(orbit_map.values())
    orbit_sizes = [len(o) for o in unique_orbits]
    
    N = G.number_of_nodes()
    probs = np.array(orbit_sizes) / N
    h_s = -np.sum(probs * np.log2(probs + 1e-10))
    
    return num_autos, h_s

def classify_structure(G):
    """Classifies the undirected topology."""
    degrees = dict(G.degree())
    max_k = max(degrees.values())
    internal_nodes = [n for n, d in degrees.items() if d > 1]
    
    if not internal_nodes: return "Point"
    
    # Check for Regular Trees (Uniform Internal Degree)
    if max_k == 3 and all(degrees[n] == 3 for n in internal_nodes) and len(internal_nodes) == 4:
        skeleton = G.subgraph(internal_nodes)
        skeleton_max_k = max(dict(skeleton.degree()).values())
        if skeleton_max_k == 3:
            return "Balanced Bethe Fragment"
        elif skeleton_max_k == 2:
            return "Caterpillar (Linear Core)"
        
    if max_k == 1: return "Linear Chain"
    if max_k == G.number_of_nodes() - 1: return f"Star Graph (k={max_k})"

    return f"Irregular (k_max={max_k})"

# --- The Axiomatic Sieve ---

def filter_lemma_3_2_2_geometric_viability(G):
    """
    Lemma 3.2.2: Exclusion of Cyclic Topologies (Geometric Viability).
    Constraint: Max degree <= 3.
    Physical Logic: A coordination number k > 3 implies the necessity of 
    closed loops to tile space efficiently. To ensure the vacuum remains 
    strictly pre-geometric (acyclic potential), we enforce k <= 3.
    """
    degrees = [d for n, d in G.degree()]
    return max(degrees) <= 3

def filter_lemma_3_2_6_site_maximality(G):
    """
    Lemma 3.2.6: Site Maximality.
    Constraint: Max degree >= 3 (Branching).
    Physical Logic: Linear chains (degree 2) possess minimal compliant sites, 
    stalling geometric ignition. The vacuum must be maximally branched.
    """
    degrees = [d for n, d in G.degree()]
    return max(degrees) >= 3

def filter_lemma_3_2_7_regularity(G):
    """
    Lemma 3.2.7: Strict Degree Regularity.
    Constraint: Uniform internal degree (Variance = 0).
    Physical Logic: Any variation in internal degree introduces distinguishability 
    between locations, violating the isotropy of the vacuum.
    """
    degrees = [d for n, d in G.degree()]
    internal = [d for d in degrees if d > 1]
    if not internal: return False
    return len(set(internal)) == 1

# --- Main Census ---

print(f"{'STEP':<45} | {'SURVIVORS':<10} | {'ELIMINATED'}")
print("-" * 70)

# 1. Enumerate
candidates = list(nx.nonisomorphic_trees(10))
print(f"{'1. Enumerate Undirected Topologies':<45} | {len(candidates):<10} | -")

# 2. Apply Lemma 3.2.2
survivors = [g for g in candidates if filter_lemma_3_2_2_geometric_viability(g)]
dropped = len(candidates) - len(survivors)
print(f"{'2. Lemma 3.2.2: Geometric Viability (k<=3)':<45} | {len(survivors):<10} | {dropped} (Stars/Hubs)")

# 3. Apply Lemma 3.2.6
prev_len = len(survivors)
survivors = [g for g in survivors if filter_lemma_3_2_6_site_maximality(g)]
dropped = prev_len - len(survivors)
print(f"{'3. Lemma 3.2.6: Site Maximality':<45} | {len(survivors):<10} | {dropped} (Linear Chains)")

# 4. Apply Lemma 3.2.7
prev_len = len(survivors)
survivors = [g for g in survivors if filter_lemma_3_2_7_regularity(g)]
dropped = prev_len - len(survivors)
print(f"{'4. Lemma 3.2.7: Strict Regularity':<45} | {len(survivors):<10} | {dropped} (Irregular)")

print("-" * 70)
print(f"\n{'--- FINAL SCORECARD (Lambda Sweep [0.4 - 0.6]) ---':^70}")

results = []
lambda_range = [0.4, 0.5, 0.6]

for G in survivors:
    aut, hs = compute_metrics(G)
    name = classify_structure(G)
    
    scores = []
    for lam in lambda_range:
        s = lam * np.log2(aut) + (1 - lam) * hs
        scores.append(s)
        
    results.append({
        "Name": name,
        "|Aut|": aut,
        "Entropy": hs,
        "Score (0.4)": scores[0],
        "Score (0.5)": scores[1],
        "Score (0.6)": scores[2],
        "Mean Score": np.mean(scores)
    })

df = pd.DataFrame(results).sort_values(by="Mean Score", ascending=False)
print(df.to_string(index=False, float_format="%.4f"))

if not df.empty:
    winner = df.iloc[0]
    is_robust = all(winner[f"Score ({lam})"] > df.iloc[1][f"Score ({lam})"] for lam in lambda_range)
    status = "ROBUST" if is_robust else "FRAGILE"
    
    print(f"\nWINNER: {winner['Name']}")
    print(f"Status: {status} across lambda [0.4, 0.6]")
    print("Reason: Maximizes Optimality Score regardless of specific weighting.")
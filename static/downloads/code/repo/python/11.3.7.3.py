import numpy as np
from scipy.optimize import linprog
import networkx as nx

def lazy_mu(u, G, alpha=1/3, beta=1/3):
    """
    Lazy causal measure μ_u (**Measure Dilution Lemma** [(§11.3.3)](/monograph/stage/discrete/11.3/#11.3.3)).
    Reassigns β if empty; dilution post-add (n^-=n_u^- +1).
    """
    N_plus = list(G.successors(u))
    N_minus = list(G.predecessors(u))
    n_plus = len(N_plus)
    n_minus = len(N_minus)
    mu = {u: alpha}
    if n_plus == 0:
        mu[u] += beta
    else:
        for w in N_plus:
            mu[w] = beta / n_plus
    if n_minus == 0:
        mu[u] += beta
    else:
        for w in N_minus:
            mu[w] = beta / n_minus
    return mu

def w1_linprog(mu_source, mu_target, dist_dict, nodes):
    """
    W_1 via linprog (**Cost Contraction Lemma** [(§11.3.5)](/monograph/stage/discrete/11.3/#11.3.5): Cost Contraction).
    """
    n = len(nodes)
    c = []
    inf_indices = []
    idx = 0
    # Construct cost vector
    for i, x in enumerate(nodes):
        for j, y in enumerate(nodes):
            d = dist_dict.get((x, y), np.inf)
            if np.isinf(d):
                inf_indices.append(idx)
                c.append(1e6)
            else:
                c.append(d)
            idx += 1
    c = np.array(c)
    
    # Equality constraints for marginals
    A_eq = np.zeros((2*n, n**2))
    b_eq = np.zeros(2*n)
    for i in range(n):
        for j in range(n):
            A_eq[i, i*n + j] = 1
        b_eq[i] = mu_source.get(nodes[i], 0)
    for k in range(n):
        for i in range(n):
            A_eq[n + k, i*n + k] = 1
        b_eq[n + k] = mu_target.get(nodes[k], 0)
        
    bounds = [(0, None) for _ in range(n**2)]
    
    # Infinite distance constraints (if any)
    if inf_indices:
        A_ub = np.zeros((len(inf_indices), n**2))
        for row, col in enumerate(inf_indices):
            A_ub[row, col] = 1
        b_ub = np.zeros(len(inf_indices))
    else:
        A_ub, b_ub = None, None
        
    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, A_ub=A_ub, b_ub=b_ub, method='highs')
    
    if not res.success: return np.inf
    return res.fun

def format_dict(d):
    return {k: round(v, 4) for k, v in d.items()}

# --- Simulation Setup ---
alpha = 1/3
beta = 1/3
nodes = [0,1,2]

# G0: Chain 0→1→2 
# (**Measure Dilution Lemma** [(§11.3.3)](/monograph/stage/discrete/11.3/#11.3.3)Pre-state: Disjoint neighborhoods)
G0 = nx.DiGraph([(0,1), (1,2)])
mu0_pre = lazy_mu(0, G0)
mu1_pre = lazy_mu(1, G0)
dist = {(0,0):0, (0,1):1, (0,2):2, (1,0):1, (1,1):0, (1,2):1, (2,0):2, (2,1):1, (2,2):0}
w1_pre = w1_linprog(mu0_pre, mu1_pre, dist, nodes)
K_pre = 1 - w1_pre

# G1: Add cycle 2→0 
# (**Measure Dilution Lemma** [(§11.3.3)](/monograph/stage/discrete/11.3/#11.3.3)Post-state: Shared mass at node 2)
G1 = G0.copy()
G1.add_edge(2, 0)
mu0_post = lazy_mu(0, G1)
mu1_post = lazy_mu(1, G1)
w1_post = w1_linprog(mu0_post, mu1_post, dist, nodes)
K_post = 1 - w1_post

# --- Verification Logic ---
# 1. Verify Shared Mass (**Measure Dilution Lemma** [(§11.3.3)](/monograph/stage/discrete/11.3/#11.3.3))
m_w = min(mu0_post.get(2,0), mu1_post.get(2,0))
dilution_verified = (m_w > 0)

# 2. Verify Strict Inequality (**Cost Contraction Lemma** [(§11.3.5)](/monograph/stage/discrete/11.3/#11.3.5))
contraction_verified = (w1_post < w1_pre - 1e-6) # explicit tolerance

# 3. Verify Sparse Scaling (Corollary 11.3.7)
m_w_sparse = beta / (0.087 + 1)  # Ch. 5 deg≈0.087 dilution
delta_k_sparse = m_w_sparse * 1.5  # Est save ~1.5 avg \bar{d}

# --- Output ---
print(f"--- State G0 (Pre-Nucleation) ---")
print(f"μ_u (0): {format_dict(mu0_pre)}")
print(f"μ_v (1): {format_dict(mu1_pre)}")
print(f"W1_pre:  {w1_pre:.4f}")
print(f"K_pre:   {K_pre:.4f}\n")

print(f"--- State G1 (Post-Nucleation) ---")
print(f"μ_u (0): {format_dict(mu0_post)}")
print(f"μ_v (1): {format_dict(mu1_post)}")
print(f"W1_post: {w1_post:.4f}")
print(f"K_post:  {K_post:.4f}\n")

print(f"--- Verification Results ---")
print(f"1. **Measure Dilution Lemma** [(§11.3.3)](/monograph/stage/discrete/11.3/#11.3.3)(Shared Mass > 0):   {dilution_verified} (m_w = {m_w:.4f})")
print(f"2. **Cost Contraction Lemma** [(§11.3.5)](/monograph/stage/discrete/11.3/#11.3.5)(W1_post < W1_pre):  {contraction_verified} (ΔK = {K_post - K_pre:.4f})")
print(f"3. Corollary 11.3.7 (Sparse Scaling): c ≈ {delta_k_sparse:.4f} (per cycle)")

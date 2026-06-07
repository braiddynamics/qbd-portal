import numpy as np
from scipy.optimize import linprog
import networkx as nx

def lazy_mu_dynamic(u, G, alpha=1.0/3.0, beta=1.0/3.0):
    """
    Computes μ_u dynamically based on graph topology.
    Implements the Re-absorption Logic (**Measure Validity Lemma** [(§11.2.4)](/monograph/stage/discrete/11.2/#11.2.4)).
    """
    N_plus = list(G.successors(u))
    N_minus = list(G.predecessors(u))
    n_plus = len(N_plus)
    n_minus = len(N_minus)
    
    # Initialize dictionary
    mu = {n: 0.0 for n in G.nodes()}
    
    # Self-mass (Present)
    mu[u] += alpha
    
    # Future mass
    if n_plus == 0:
        mu[u] += beta
    else:
        for v in N_plus:
            mu[v] += beta / n_plus
            
    # Past mass
    if n_minus == 0:
        mu[u] += beta
    else:
        for v in N_minus:
            mu[v] += beta / n_minus
            
    return mu

def w1_solve(mu1, mu2, dist_matrix, nodes):
    """
    Solves Optimal Transport problem given two measure dicts and distance matrix.
    Returns the transport cost.
    """
    n = len(nodes)
    c = dist_matrix.flatten()
    
    # Equality constraints (Marginals)
    A_eq = np.zeros((2*n, n*n))
    b_eq = np.zeros(2*n)
    
    # Source constraints
    for i in range(n):
        for j in range(n):
            A_eq[i, i*n + j] = 1
        b_eq[i] = mu1[nodes[i]]
        
    # Target constraints
    for j in range(n):
        for i in range(n):
            A_eq[n+j, i*n + j] = 1
        b_eq[n+j] = mu2[nodes[j]]
        
    bounds = [(0, None) for _ in range(n*n)]
    
    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
    return res.fun

def format_dict(d):
    return {k: float(f"{v:.4f}") for k, v in d.items()}

# --- Setup ---
G = nx.DiGraph()
G.add_edges_from([(0,1), (1,2)]) # 0=A, 1=B, 2=C
nodes = [0, 1, 2]

# Compute Measures
mu_A = lazy_mu_dynamic(0, G)
mu_B = lazy_mu_dynamic(1, G)

# Compute Distance Matrix (Undirected Shortest Path)
# d(A,B)=1, d(B,C)=1, d(A,C)=2
dist_matrix = np.array([
    [0, 1, 2],
    [1, 0, 1],
    [2, 1, 0]
], dtype=float)

# Solve
w1_val = w1_solve(mu_A, mu_B, dist_matrix, nodes)
K_val = 1 - w1_val

# Verify Excess Mass (Proof Step IV)
# Excess = mu_A - mu_B. Positive means "Source has extra", Negative means "Target needs mass".
excess = {n: mu_A[n] - mu_B[n] for n in nodes}

# --- Output ---
print(f"Measure A (Origin): {format_dict(mu_A)}")
print(f"Measure B (Center): {format_dict(mu_B)}")
print(f"Excess Mass (A-B):  {format_dict(excess)}")
print(f"Transport Cost W1:  {w1_val:.4f}")
print(f"Curvature K(A,B):   {K_val:.4f}")

# Verification Logic
transport_verified = np.isclose(w1_val, 2.0/3.0)
print(f"Verification Pass:  {transport_verified}")

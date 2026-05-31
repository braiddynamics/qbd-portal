import numpy as np
from scipy.optimize import linprog

def w1_linprog(mu_source, mu_target, dist_dict, nodes):
    """
    Computes W_1 via Linear Programming (Min Cost Flow).
    - dist_dict: Must represent SHORTEST PATH distances (metric).
    - Returns np.inf if the transport problem is infeasible.
    """
    n = len(nodes)
    c = []
    inf_indices = []
    idx = 0
    
    # 1. Construct Cost Vector
    # If distance is infinite, we assign a finite proxy but restrict flow to 0 later.
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
    
    # 2. Equality Constraints (Marginals)
    A_eq = np.zeros((2*n, n**2))
    b_eq = np.zeros(2*n)
    
    # Check mass conservation
    s_sum = sum(mu_source.values())
    t_sum = sum(mu_target.values())
    if not np.isclose(s_sum, t_sum):
        # Normalization to prevent numerical infeasibility
        mu_source = {k: v/s_sum for k,v in mu_source.items()}
        mu_target = {k: v/t_sum for k,v in mu_target.items()}

    # Source constraints
    for i in range(n):
        for j in range(n):
            A_eq[i, i*n + j] = 1
        b_eq[i] = mu_source.get(nodes[i], 0)
        
    # Target constraints
    for k in range(n):
        for i in range(n):
            A_eq[n + k, i*n + k] = 1
        b_eq[n + k] = mu_target.get(nodes[k], 0)
        
    # 3. Bounds: Forbid flow on infinite edges
    bounds = []
    for k in range(n**2):
        if k in inf_indices:
            bounds.append((0, 0)) # Constrain invalid paths to zero flow
        else:
            bounds.append((0, None))
    
    # 4. Solve
    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
    
    if not res.success:
        return np.inf
        
    return res.fun

# --- Setup ---
nodes = [0, 1, 2]
# Use exact fractions to ensure Sum(A) == Sum(B)
mu_A = {0: 2.0/3.0, 1: 1.0/3.0, 2: 0.0}       # Past-heavy (Source)
mu_B = {0: 1.0/3.0, 1: 1.0/3.0, 2: 1.0/3.0}   # Balanced (Target)

# --- Metrics (Geodesic Distances) ---
# Undirected: All connected. d(0,2) = 2.
d_undir = {
    (0,0):0, (0,1):1, (0,2):2, 
    (1,0):1, (1,1):0, (1,2):1, 
    (2,0):2, (2,1):1, (2,2):0
}

# Directed: Forward finite, Reverse infinite.
d_dir = {
    (0,0):0, (0,1):1, (0,2):2,       # 0->2 is valid path
    (1,0):np.inf, (1,1):0, (1,2):1,  # 1->0 impossible
    (2,0):np.inf, (2,1):np.inf, (2,2):0
}

# --- Computations ---
val_undir = w1_linprog(mu_A, mu_B, d_undir, nodes)
val_dir_fwd = w1_linprog(mu_A, mu_B, d_dir, nodes)   # A -> B
val_dir_rev = w1_linprog(mu_B, mu_A, d_dir, nodes)   # B -> A

# --- Output ---
print(f"Undirected W1 (A -> B):   {val_undir:.4f}")
print(f"Directed Fwd W1 (A -> B): {val_dir_fwd:.4f}")
print(f"Directed Rev W1 (B -> A): {val_dir_rev}")

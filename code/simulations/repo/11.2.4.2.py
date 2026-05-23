import numpy as np
import networkx as nx

def lazy_mu(u, G, alpha=1/3, beta=1/3):
    """
    Compute lazy causal measure μ_u for vertex u.
    Handles empty neighborhoods via mass reassignment (Laziness).
    """
    N_plus = list(G.successors(u))
    N_minus = list(G.predecessors(u))
    n_plus = len(N_plus)
    n_minus = len(N_minus)
    
    # Initial allocation to Present
    mu = {u: alpha}
    
    # Future Allocation
    if n_plus == 0:
        mu[u] += beta  # Reabsorb
    else:
        for w in N_plus:
            mu[w] = beta / n_plus
            
    # Past Allocation
    if n_minus == 0:
        mu[u] += beta  # Reabsorb
    else:
        for w in N_minus:
            mu[w] = beta / n_minus
            
    return mu, sum(mu.values())

def print_case(name, mu, total):
    # Format for clean console output
    formatted_mu = {k: round(v, 4) for k, v in mu.items()}
    print(f"Case: {name}")
    print(f"  Map: {formatted_mu}")
    print(f"  Sum: {total:.4f}\n")

# --- Simulation Setup ---

# 1. Standard Chain: 0 -> 1 -> 2
G_chain = nx.DiGraph()
G_chain.add_edges_from([(0,1), (1,2)])

# Case 1: Balanced (u=1, has both past and future)
mu1, sum1 = lazy_mu(1, G_chain)
print_case("Balanced Topology (u=1)", mu1, sum1)

# Case 2: Empty Past (u=0, has future but no past)
mu0, sum0 = lazy_mu(0, G_chain)
print_case("Empty Past (u=0)", mu0, sum0)

# 2. Reverse Chain: 0 <- 1 <- 2 (to simulate empty future at u=2)
G_rev = nx.DiGraph()
G_rev.add_edges_from([(1,0), (2,1)])

# Case 3: Empty Future (u=2, has past but no future)
mu2, sum2 = lazy_mu(2, G_rev)
print_case("Empty Future (u=2)", mu2, sum2)

# 3. Isolated Node
G_iso = nx.DiGraph()
G_iso.add_node(99)

# Case 4: Isolated Singularity
mu_iso, sum_iso = lazy_mu(99, G_iso)
print_case("Isolated Singularity (u=99)", mu_iso, sum_iso)

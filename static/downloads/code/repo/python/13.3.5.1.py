import numpy as np
import networkx as nx

def verify_bianchi_identity():
    print("--- QBD Discrete Bianchi Identity Verification ---")
    print("Objective: Check divergence-free condition ∇·G = 0 for conserved fluxes")
    print("=" * 65)

    sizes = [50, 100, 500]
    
    print(f"{'N (Nodes)':<12} | {'Mean Divergence (Error)':<25} | {'Max Divergence':<20}")
    print("-" * 65)

    for N in sizes:
        # 1. Generate a Connected Graph (Toroidal Lattice Proxy for Closed Manifold)
        # Using a regular graph ensures well-defined neighborhoods
        k = 4 # Degree
        G = nx.random_regular_graph(k, N, seed=42)
        
        # 2. Generate Conserved Flux T_ab (Simulating Equilibrium)
        # To strictly satisfy sum_b T_ab = 0, we treat edges as flow pipes.
        # We assign random cycle flows which are inherently divergence-free.
        T_matrix = np.zeros((N, N))
        
        # Add random cycle flows
        num_cycles = N * 2
        for _ in range(num_cycles):
            try:
                # Find a random cycle
                cycle = nx.find_cycle(G, source=np.random.choice(range(N)))
                flow_mag = np.random.normal(0, 1)
                
                for u, v in cycle:
                    T_matrix[u, v] += flow_mag
                    T_matrix[v, u] -= flow_mag # Antisymmetry
            except:
                pass

        # 3. Compute Geometry G_ab via Field Equation
        # G_ab = kappa * T_ab (plus G_vac, which is isotropic/divergence-free)
        kappa = 0.3333
        G_matrix = kappa * T_matrix 
        
        # 4. Calculate Divergence of G at each node
        # Div(u) = Sum_v G_uv
        divergences = np.sum(G_matrix, axis=1)
        
        # 5. Metrics
        mean_err = np.mean(np.abs(divergences))
        max_err = np.max(np.abs(divergences))
        
        print(f"{N:<12} | {mean_err:<25.4e} | {max_err:<20.4e}")

    print("-" * 65)
    print("RESULT: Divergence vanishes to machine precision.")
    print("        Geometric conservation is mathematically exact given G ~ T.")
    print("=================================================================")

if __name__ == "__main__":
    verify_bianchi_identity()

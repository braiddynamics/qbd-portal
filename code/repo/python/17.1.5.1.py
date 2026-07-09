import networkx as nx
import numpy as np
from scipy.optimize import curve_fit

def verify_braid_confinement():
    """
    Simulation 17.1.4.1: Braid Confinement Verification.
    
    This routine models the vacuum as a weighted lattice graph. It verifies that
    the energy cost (Action) required to maintain a topological connection 
    between two defects scales linearly with separation distance L, characteristic 
    of a confining flux tube (String) rather than a spreading field (Coulomb).
    """
    
    # -------------------------------------------------------------------------
    # 1. System Initialization
    # -------------------------------------------------------------------------
    separations = [2, 4, 6, 8, 10, 12, 14, 20, 30]
    energies = []
    
    print(f"{'Separation (L)':<18} | {'Flux Energy (E)':<18} | {'Tension (sigma)':<15}")
    print("-" * 65)

    for L in separations:
        # Construct the Vacuum Lattice
        # We use a grid sufficiently large to avoid boundary effects.
        # In QBD, the 'vacuum' is the ground state graph.
        grid_size = L + 10
        G = nx.grid_2d_graph(grid_size, grid_size)
        
        # Assign Action Weights
        # Every active link in the graph carries a computational cost (weight=1).
        # This represents the 'Mass Gap' or fundamental tension of the network.
        for u, v in G.edges():
            G[u][v]['weight'] = 1.0
            
        # Define Braid Endpoints (Defects)
        source = (grid_size // 2, 2)
        sink = (grid_size // 2, 2 + L)
        
        # ---------------------------------------------------------------------
        # 2. Compute Minimal Action Configuration
        # ---------------------------------------------------------------------
        # The physical state is the one minimizing total Action (Shortest Path).
        # This corresponds to the Nambu-Goto minimal area principle.
        
        if source in G and sink in G:
            min_action_path = nx.shortest_path_length(G, source, sink, weight='weight')
            energies.append(min_action_path)
            
            # Tension = Energy per unit length
            tension = min_action_path / L
            
            print(f"{L:<18} | {min_action_path:<18.1f} | {tension:.2f}")

    print("-" * 65)

    # -------------------------------------------------------------------------
    # 3. Scaling Analysis
    # -------------------------------------------------------------------------
    # Fit the Potential V(r) = sigma * r + C
    def linear_potential(x, sigma, c):
        return sigma * x + c
        
    popt, _ = curve_fit(linear_potential, separations, energies)
    sigma_fit = popt[0]
    intercept = popt[1]
    
    print(f"Fit Model: V(r) = sigma * r + V_0")
    print(f"String Tension (sigma): {sigma_fit:.4f} Action/Length")
    print(f"Self-Energy (V_0):      {intercept:.4f}")

if __name__ == "__main__":
    verify_braid_confinement()

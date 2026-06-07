import networkx as nx
import numpy as np

def calculate_wormhole_growth():
    """
    Simulation 15.3.5.1: Wormhole Length vs. Braid Complexity.
    
    This routine verifies the linear relationship between the computational 
    complexity (C) of the unitary circuit generating the state and the 
    geodesic length (L) of the resulting topological throat (Einstein-Rosen Bridge).
    This simulates the 'Complexity = Volume' conjecture.
    """
    
    # -------------------------------------------------------------------------
    # System Initialization
    # -------------------------------------------------------------------------
    # We test varying degrees of circuit complexity C (gate count).
    # Each gate represents a scrambling operation that lengthens the interior geometry.
    complexity_steps = [0, 5, 10, 20, 50, 100]
    
    print(f"{'Braid Complexity (C)':<22} | {'Throat Length (L)':<20} | {'Growth Rate (dL/dC)'}")
    print("-" * 65)

    for C in complexity_steps:
        # 1. Initialize the TFD State (Shortest Path)
        # The base state is a maximally entangled Bell pair: d_topo(Alice, Bob) = 1.
        G = nx.Graph()
        G.add_edge("Alice", "Bob")
        
        # 2. Apply Unitary Evolution (Complexity Growth)
        # We model time evolution U(t) as the sequential insertion of gates.
        # Graphically, a unitary operation on the channel subdivides the edge:
        # (u, v) -> (u, gate, v). This adds topological volume.
        for i in range(C):
            # Locate the current geodesic path through the throat
            path = nx.shortest_path(G, "Alice", "Bob")
            
            # Target the midpoint of the bridge for operation
            u = path[len(path)//2 - 1] 
            v = path[len(path)//2]     
            
            # Apply the gate (Subdivision Rule)
            if G.has_edge(u, v):
                G.remove_edge(u, v)
                
            gate_node = f"Gate_{i}"
            G.add_node(gate_node, type="unitary_op")
            G.add_edge(u, gate_node)
            G.add_edge(gate_node, v)

        # 3. Metric Evaluation
        # Calculate the new geodesic distance through the wormhole.
        throat_length = nx.shortest_path_length(G, "Alice", "Bob")
        
        # 4. Scaling Analysis
        # Calculate the rate of geometric expansion per unit of complexity.
        # Baseline length is 1, so growth is (L - 1).
        growth_rate = (throat_length - 1) / C if C > 0 else 0.0
        
        print(f"{C:<22} | {throat_length:<20} | {growth_rate:.2f}")

if __name__ == "__main__":
    calculate_wormhole_growth()

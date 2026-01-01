import networkx as nx
import numpy as np
import pandas as pd

def boundary_fraction(N: int):
    """Compute fraction of edges crossing block boundaries in a 2D toroidal lattice."""
    side = int(np.sqrt(N))
    if side * side != N:
        raise ValueError("N must be a perfect square for a square toroidal grid.")
    
    # Create toroidal 2D grid graph
    G = nx.grid_2d_graph(side, side, periodic=True)
    # Relabel nodes to linear indices 0..N-1
    mapping = {(i, j): i * side + j for i in range(side) for j in range(side)}
    G = nx.relabel_nodes(G, mapping)
    
    total_edges = G.number_of_edges()
    
    # Block size ≈ side // 4 (mimics correlation volume)
    block_side = max(2, side // 4)
    blocks_per_side = side // block_side
    
    boundary_edges = 0
    
    # Iterate over all edges and count those crossing block boundaries
    for u, v in G.edges():
        # Block coordinates of u and v
        block_u = (u // side // block_side, (u % side) // block_side)
        block_v = (v // side // block_side, (v % side) // block_side)
        
        if block_u != block_v:
            boundary_edges += 1
    
    # Each edge counted once (undirected graph)
    fraction = boundary_edges / total_edges if total_edges > 0 else 0.0
    
    # Relative correction term (as in original)
    rel_correction = np.sqrt(N) * np.log(total_edges + 1) / (N * np.log(2) + 1e-10)
    
    return {
        'N': N,
        'Boundary Edge Fraction': fraction,
        'Relative Correction': rel_correction
    }

# Perfect-square lattice sizes
sizes = [100, 400, 900, 1600, 2500, 3600, 4900, 6400, 8100, 10000]
results = [boundary_fraction(N) for N in sizes]

df = pd.DataFrame(results)

print("Subextensive Boundary Terms in 2D Toroidal Lattice")
print("=" * 54)
print(df.round(4).to_markdown(index=False, tablefmt="github"))
import networkx as nx
import numpy as np
import pandas as pd

def simulate_boundary_correction(N, d=2):
    """
    Simulates N-site 2D lattice, partitions into blocks of size ~sqrt(N)/4,
    counts fraction of edges crossing block boundaries.
    """
    if d != 2: raise ValueError("Toy model implemented for d=2")
    side = int(np.sqrt(N))
    if side**2 != N: N = side**2
    
    # Generate Toroidal Grid (representing uniform local connectivity)
    G = nx.grid_2d_graph(side, side, periodic=True) 
    G = nx.relabel_nodes(G, {(i,j): i*side + j for i in range(side) for j in range(side)})
    total_edges = G.number_of_edges()
    
    # Partition: Block size set to mimic correlation length xi
    block_size = max(2, side // 4) 
    num_blocks_row = side // block_size
    if num_blocks_row < 2: num_blocks_row = 2
    
    boundary_edges = 0
    
    for i in range(num_blocks_row):
        for j in range(num_blocks_row):
            block_start_row = i * block_size
            block_start_col = j * block_size
            
            block_nodes = []
            for row in range(block_start_row, min(block_start_row + block_size, side)):
                for col in range(block_start_col, min(block_start_col + block_size, side)):
                    node = row * side + col
                    block_nodes.append(node)
            
            for node in block_nodes:
                row_node = node // side
                col_node = node % side
                block_i_node = row_node // block_size
                block_j_node = col_node // block_size
                
                for nbr in G.neighbors(node):
                    row_nbr = nbr // side
                    col_nbr = nbr % side
                    block_i_nbr = row_nbr // block_size
                    block_j_nbr = col_nbr // block_size
                    
                    if (block_i_node, block_j_node) != (block_i_nbr, block_j_nbr):
                        boundary_edges += 1 
                        
    boundary_edges //= 2
    
    fraction = boundary_edges / total_edges if total_edges > 0 else 0
    rel_correction = np.sqrt(N) * np.log(total_edges + 1) / (N * np.log(2) + 1e-10) 
    
    return {
        'N': N, 
        'fraction': fraction, 
        'rel_correction': rel_correction
    }

Ns = [100, 400, 900, 1600, 2500, 3600, 4900, 6400, 8100, 10000]
results = [simulate_boundary_correction(n) for n in Ns]
df = pd.DataFrame(results)
print(df[['N', 'fraction', 'rel_correction']].round(4))
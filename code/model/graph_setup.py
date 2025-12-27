# /model/graph_setup.py
import networkx as nx

def generate_zpi_vacuum(num_nodes_approx: int):
    """
    Generates the Zero-Point Information (ZPI) vacuum as a Bethe fragment.

    Args:
        num_nodes_approx: The target number of nodes (N) for the graph.

    Returns:
        A tuple (G, levels) where G is the nx.DiGraph and levels
        is a list of lists containing the nodes at each depth.
    """
    if num_nodes_approx < 3:
        raise ValueError("num_nodes_approx must be at least 3 for a valid vacuum")
    
    # The causal graph, G
    G = nx.DiGraph()
    root = 0
    G.add_node(root)
    
    levels = [[root]]  # Used to track nodes by depth
    node_id = 1
    
    # Grow the tree until it reaches the target approximate size (N)
    while G.number_of_nodes() < num_nodes_approx:
        next_level = []
        if not levels[-1]: # Break if the last level had no nodes
            break
            
        for parent in levels[-1]:
            # Branching factor (k): 3 for root, 2 for all other internal nodes.
            children = 3 if parent == root else 2
            
            for _ in range(children):
                if G.number_of_nodes() >= num_nodes_approx:
                    break
                
                G.add_node(node_id)
                
                # --- TIMESTAMP LOGIC ---
                # Add the edge with the vacuum timestamp H=0
                G.add_edge(parent, node_id, H=0)
                # --- END ---
                
                next_level.append(node_id)
                node_id += 1
                
        if not next_level:
            break
        levels.append(next_level)
        
    return G, levels

def inject_energic_event(G: nx.DiGraph, levels: list):
    """
    Implements the "Ignition of Geometrogenesis".

    This function performs the single, non-perturbative "tunneling" event
    that breaks the vacuum's symmetry by adding one edge to create the
    universe's first 3-cycle. This "spark" is assigned the first
    non-zero timestamp, H=1.

    Args:
        G: The ZPI vacuum graph.
        levels: The node-depth list from generate_zpi_vacuum.

    Returns:
        The modified graph G, now containing one 3-cycle.
    """
    
    if len(levels) < 3 or (len(levels) >= 3 and not levels[2]):
        # Fallback: Graph is too small. Manually return a 3-cycle.
        G_fallback = nx.DiGraph()
        G_fallback.add_edges_from([(0, 1, {'H': 1}), 
                                  (1, 2, {'H': 1}), 
                                  (2, 0, {'H': 1})])
        return G_fallback

    # Find the vertices for the first 2-path:
    v = levels[0][0]  # v = The root
    w = levels[1][0]  # w = The root's first child
    u = levels[2][0]  # u = The first grandchild
    
    # --- TIMESTAMP LOGIC ---
    # Add the symmetry-breaking, "closing" edge (u, v)
    # with timestamp H=1, representing the first "tick" of
    # geometrogenesis.
    G.add_edge(u, v, H=1)
    # --- END ---
    
    return G
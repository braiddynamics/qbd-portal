import networkx as nx

def build_bethe_fragment(depth, k):
    """
    Constructs a directed Bethe lattice fragment.
    Edges point from root (past) to leaves (future).
    """
    G = nx.DiGraph()
    root = 0
    G.add_node(root, layer=0)
   
    current_layer = [root]
    next_node_id = 1
   
    for d in range(depth):
        next_layer = []
        for parent in current_layer:
            # Root splits into k; others split into k-1 (one parent, k-1 children)
            num_children = k if parent == root else k - 1
           
            for _ in range(num_children):
                child = next_node_id
                G.add_node(child, layer=d+1)
                G.add_edge(parent, child)
               
                next_layer.append(child)
                next_node_id += 1
        current_layer = next_layer
    return G

# --- Execution ---
G_vacuum = build_bethe_fragment(depth=2, k=3)

# Topological Checks
is_dag = nx.is_directed_acyclic_graph(G_vacuum)
node_count = G_vacuum.number_of_nodes()
edge_count = G_vacuum.number_of_edges()

# Tree Property Check: E = V - 1 for connected components
is_tree_sparsity = (edge_count == node_count - 1)

print(f"Graph Structure: {node_count} nodes, {edge_count} edges")
print(f"Is Directed Acyclic Graph (DAG): {is_dag}")
print(f"Sparsity Check (E=V-1): {is_tree_sparsity}")
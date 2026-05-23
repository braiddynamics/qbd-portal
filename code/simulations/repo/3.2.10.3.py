import networkx as nx
import pandas as pd

def bethe_fragment_metrics(depth: int, b: int) -> dict:
    """Generate finite regular Bethe fragment and compute key metrics."""
    if depth < 1 or b < 3:
        raise ValueError("Depth ≥ 1 and coordination b ≥ 3 required.")
    
    G = nx.Graph()
    node_id = 0
    root = node_id
    node_id += 1
    G.add_node(root)
    
    current_level = [root]
    
    for _ in range(depth):
        next_level = []
        for parent in current_level:
            children = b if parent == root else (b - 1)
            for _ in range(children):
                child = node_id
                node_id += 1
                G.add_node(child)
                G.add_edge(parent, child)
                next_level.append(child)
        if not next_level:
            break
        current_level = next_level
    
    total_nodes = G.number_of_nodes()
    regular_nodes = sum(1 for v in G if G.degree(v) == b)
    regularity_frac = regular_nodes / total_nodes if total_nodes > 0 else 0.0
    theoretical_frac = 1.0 / (b - 1)
    
    return {
        'Depth': depth,
        'Coordination (b)': b,
        'Nodes': total_nodes,
        'b-Regular Fraction': f'{regularity_frac:.4%}',
        'Theoretical Limit': f'{theoretical_frac:.4%}'
    }

# Test configurations
configs = (
    [{'depth': d, 'b': 3} for d in range(3, 16)] +   # b=3, depth 3–15
    [{'depth': 5, 'b': b} for b in [4, 5, 6]]       # depth=5, b=4,5,6
)

results = [bethe_fragment_metrics(**cfg) for cfg in configs]
df = pd.DataFrame(results)

print("Bethe Fragment Regularity Scaling")
print("=" * 50)
print(df.to_markdown(index=False, tablefmt="github"))

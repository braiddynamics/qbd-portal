import networkx as nx


def select(graph, priorities):
    return {a for a in graph if all(priorities[a] > priorities[b] for b in graph[a])}


conflicts = nx.Graph([(0, 1), (1, 2)])
weights = {0: 2, 1: 1, 2: 3}
selected = select(conflicts, weights)
assert selected == {0, 2}
assert all(not {a, b} <= selected for a, b in conflicts.edges)
labels = {0: "right", 1: "middle", 2: "left"}
relabeled = nx.relabel_nodes(conflicts, labels)
relabeled_weights = {labels[a]: weight for a, weight in weights.items()}
assert select(relabeled, relabeled_weights) == {labels[a] for a in selected}

tie = nx.Graph([(0, 1)])
selected_tie = select(tie, {0: 1, 1: 1})
assert selected_tie == set()
assert all(select(tie, {0: 1, 1: 1}) <= {a} for a in tie)
print(f"Independent selection: {sorted(selected)}")
print(f"Relabeled selection: {sorted(select(relabeled, relabeled_weights))}")
print(f"Equal-priority pair: {len(selected_tie)} retained")

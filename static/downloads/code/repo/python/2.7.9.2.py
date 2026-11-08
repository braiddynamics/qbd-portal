import networkx as nx


def mediated_relation(graph):
    relation = nx.DiGraph()
    relation.add_nodes_from(graph)
    for start in graph:
        for end in graph:
            if start == end:
                continue
            for path in nx.all_simple_paths(graph, start, end):
                heights = [graph[a][b]["height"] for a, b in zip(path, path[1:])]
                if len(heights) >= 2 and all(a < b for a, b in zip(heights, heights[1:])):
                    relation.add_edge(start, end)
                    break
    return relation


def timestamped(edges):
    graph = nx.DiGraph()
    graph.add_weighted_edges_from(edges, weight="height")
    return graph


from itertools import combinations


old = timestamped([(0, 1, 0), (0, 2, 0), (1, 3, 0), (1, 4, 0),
                   (2, 5, 0), (2, 6, 0), (3, 7, 0)])
depth = nx.single_source_shortest_path_length(old, 0)
chords = [(u, v, 1) for v in old for w in old[v] for u in old[w]]
count = 0
for size in range(len(chords) + 1):
    for batch in combinations(chords, size):
        graph = old.copy()
        graph.add_weighted_edges_from(batch, weight="height")
        relation = mediated_relation(graph)
        assert all(depth[b] == depth[a] - 1 for a, b in relation.edges)
        assert nx.is_directed_acyclic_graph(relation)
        count += 1
print(f"Outward-tree batches checked: {count}")

cycle = timestamped((i, (i + 1) % 6, 0) for i in range(6))
cycle.add_weighted_edges_from((((i + 2) % 6, i, 1) for i in range(6)), weight="height")
relation = mediated_relation(cycle)
assert set(relation.edges) == {(i, (i - 1) % 6) for i in range(6)}
assert not nx.is_directed_acyclic_graph(relation)
print(f"Six-cycle mediated pairs: {sorted(relation.edges)}")

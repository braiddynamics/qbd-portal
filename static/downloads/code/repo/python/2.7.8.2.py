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


old = timestamped([("v", "w", 0), ("w", "u", 0), ("u", "x", 0),
                   ("v", "z", 0), ("z", "x", 1)])
chords = [("u", "v", 1), ("x", "w", 2)]
assert nx.is_directed_acyclic_graph(mediated_relation(old))
for _, target, height in chords:
    assert all(height >= data["height"] for _, _, data in old.out_edges(target, data=True))
merged = old.copy()
merged.add_weighted_edges_from(chords, weight="height")
final = merged.copy()
final.remove_edge("z", "x")
for name, graph, expected in [("merge", merged, ["v", "w"]), ("final", final, [])]:
    closure = nx.transitive_closure(mediated_relation(graph))
    diagonal = [target for target in ("v", "w") if closure.has_edge(target, target)]
    assert diagonal == expected
    assert nx.is_directed_acyclic_graph(mediated_relation(graph)) == (not diagonal)
    print(f"{name} target diagonals: {diagonal}")

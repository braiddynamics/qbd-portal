import networkx as nx


def relations(graph):
    relation = nx.DiGraph()
    relation.add_nodes_from(graph)
    for a in graph:
        for b in graph:
            if a == b:
                continue
            if any(len(path) >= 3 and increasing(graph, path)
                   for path in nx.all_simple_paths(graph, a, b)):
                relation.add_edge(a, b)
    return relation


def increasing(graph, path):
    heights = [graph[a][b]["height"] for a, b in zip(path, path[1:])]
    return all(left < right for left, right in zip(heights, heights[1:]))


def evaluate(edges, v, w, u):
    graph = nx.DiGraph()
    graph.add_weighted_edges_from(edges, weight="height")
    height = 1 + max(data["height"] for _, _, data in graph.in_edges(u, data=True))
    middle = {z for z in graph[v] if z not in {v, u} and graph.has_edge(z, u)}
    geometric = (len({v, w, u}) == 3 and middle == {w}
                 and not graph.has_edge(v, u) and not graph.has_edge(u, v))
    reverse_ok = not any(
        len(path) >= 3 and increasing(graph, path)
        and graph[path[-2]][u]["height"] < height
        for path in nx.all_simple_paths(graph, v, u, cutoff=5)
    )
    graph.add_edge(u, v, height=height)
    directed = all(a != b and not graph.has_edge(b, a) for a, b in graph.edges)
    return directed, geometric, reverse_ok, nx.is_directed_acyclic_graph(relations(graph))


fixtures = [
    ([(0, 1, 0), (1, 2, 0), (2, 3, 0)], 0, 1, 3),
    ([(0, 1, 0), (1, 2, 0), (3, 3, 0)], 0, 1, 2),
    ([("A", "Z", 1), ("Z", "D", 2), ("D", "C", 3),
      ("C", "Z", 4), ("Z", "B", 5)], "A", "Z", "B"),
]
expected = [(True, False, True, True), (False, True, True, True),
            (True, True, False, False)]
for index, (fixture, target) in enumerate(zip(fixtures, expected), 1):
    actual = evaluate(*fixture)
    assert actual == target
    print(f"Proposal {index}: {actual}")

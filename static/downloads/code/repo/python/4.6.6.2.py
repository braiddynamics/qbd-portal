from math import e, exp, log2, pi, sqrt

import networkx as nx


def candidates(graph):
    result = set()
    cutoff = int(log2(len(graph))) + 3
    for v in graph:
        for w in graph[v]:
            for u in graph[w]:
                if len({v, w, u}) < 3 or graph.has_edge(v, u) or graph.has_edge(u, v):
                    continue
                if any(z != w and graph.has_edge(z, u) for z in graph[v]):
                    continue
                height = 1 + max(data["height"] for _, _, data in graph.in_edges(u, data=True))
                blocked = False
                for path in nx.all_simple_paths(graph, v, u, cutoff=cutoff):
                    heights = [graph[a][b]["height"] for a, b in zip(path, path[1:])]
                    if (len(heights) >= 2 and heights[-1] < height
                            and all(a < b for a, b in zip(heights, heights[1:]))):
                        blocked = True
                        break
                if not blocked:
                    result.add((u, v))
    return result


for name, edges, count, expected in [
    ("four-cycle", [(0, 1, 0), (1, 2, 0), (2, 3, 0), (3, 0, 0)], 4, True),
    ("two-path", [(0, 1, 0), (1, 2, 0)], 1, False),
    ("triangle", [(0, 1, 0), (1, 2, 0), (2, 0, 1)], 0, False),
]:
    graph = nx.DiGraph()
    graph.add_weighted_edges_from(edges, weight="height")
    eligible = candidates(graph)
    assert len(eligible) == count
    retained = {(u, v) for u, v in eligible if (v, u) not in eligible}
    triangles = [cycle for cycle in nx.simple_cycles(graph) if len(cycle) == 3]
    positive_deletion = bool(triangles)
    if positive_deletion:
        q = min(1, (1 + 2 * (e - 1)) * exp(-2 / sqrt(2 * pi)) / 2)
        assert q > 0
    quiescent = not positive_deletion and not retained
    assert quiescent == expected
    print(f"{name}: {len(eligible)} eligible, quiescent={quiescent}")

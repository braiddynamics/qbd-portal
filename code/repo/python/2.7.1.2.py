from math import log2

import networkx as nx


def pre_check_aec(graph, source, target, candidate_height):
    """Check a bounded reverse witness for an absent return chord."""
    cutoff = int(log2(len(graph))) + 3 if len(graph) > 1 else 1
    for path in nx.all_simple_paths(graph, target, source, cutoff=cutoff):
        heights = [graph[a][b]["H"] for a, b in zip(path, path[1:])]
        if (len(heights) >= 2 and heights[-1] < candidate_height
                and all(a < b for a, b in zip(heights, heights[1:]))):
            return False
    return True


snapshot = nx.DiGraph()
snapshot.add_weighted_edges_from([(0, 1, 0), (1, 2, 0)], weight="H")
assert pre_check_aec(snapshot, 2, 0, 1)
snapshot[1][2]["H"] = 1
assert not pre_check_aec(snapshot, 2, 0, 2)
print("Equal-height path admitted; strictly increasing reverse witness rejected.")

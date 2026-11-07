from collections import Counter
from itertools import permutations


def triangles(edges):
    vertices = sorted({vertex for edge in edges for vertex in edge})
    return {
        ((a, b), (b, c), (c, a))
        for a, b, c in permutations(vertices, 3)
        if a == min(a, b, c) and {(a, b), (b, c), (c, a)} <= edges
    }


old = {(0, 1), (0, 3), (0, 4), (1, 3), (1, 4), (1, 5),
       (2, 0), (2, 1), (2, 3), (4, 3), (5, 4)}
batch = {(3, 5), (5, 0), (5, 2)}
merged = triangles(old | batch)
supporting = {face for face in merged if len(set(face) & batch) <= 1}
support_counts = Counter(edge for face in supporting for edge in face)
full_counts = Counter(edge for face in merged for edge in face)
assert max(support_counts.values()) <= 2
assert full_counts[(3, 5)] == 3
assert any(len(set(face) & batch) >= 2 for face in merged)
print(f"Edge (3, 5): {support_counts[(3, 5)]} supporting, {full_counts[(3, 5)]} full")

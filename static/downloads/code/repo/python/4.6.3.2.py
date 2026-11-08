from fractions import Fraction as F
from itertools import product

def graph_kernel(edges, additions, triangles):
    # Rate parameters are supplied to audit the finite sampling law.
    factors = []
    for edge, p in additions:
        factors.append([(None, 1-p), (edge, p)])
    for cycle, q in triangles:
        factors.append([(None, 1-q)] + [(edge, q/3) for edge in cycle])
    law = {}
    count = {}
    for outcome in product(*factors):
        weight = F(1)
        for _, probability in outcome:
            weight *= probability
        if weight == 0:
            continue
        accepted = {edge for edge, _ in outcome[:len(additions)] if edge is not None}
        filtered = {edge for edge in accepted if edge[::-1] not in accepted and edge[0] != edge[1]}
        deleted = {edge for edge, _ in outcome[len(additions):] if edge is not None}
        successor = frozenset((set(edges) | filtered) - deleted)
        law[successor] = law.get(successor, F(0)) + weight
        count[successor] = count.get(successor, 0) + 1
    assert sum(law.values()) == 1
    return law, count

triangle = ((0,1),(1,2),(2,0))
law, _ = graph_kernel(triangle, [], [(triangle,F(3,5))])
specific = frozenset(set(triangle)-{(0,1)})
assert law[specific] == F(1,5)
print('Isolated triangle: total mass = 1; specified-edge deletion =', law[specific])

other = ((0,1),(1,3),(3,0))
edges = set(triangle) | set(other)
law, preimages = graph_kernel(edges, [], [(triangle,F(3,5)),(other,F(1,2))])
shared = frozenset(edges-{(0,1)})
assert preimages[shared] == 3
print('Shared triangles: total mass = 1; shared-edge-only preimages =', preimages[shared])

# Abstract reciprocal merge fixture: this checks merging, not proposal admission.
law, preimages = graph_kernel([], [((0,1),F(1,3)),((1,0),F(2,5))], [])
assert preimages[frozenset()] == 2
print('Reciprocal merge fixture: total mass = 1; unchanged-state preimages =', preimages[frozenset()])

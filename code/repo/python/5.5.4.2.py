from fractions import Fraction
from itertools import product


first = ((0, 1), (1, 2), (2, 0))
second = ((0, 1), (1, 3), (3, 0))
vertex = 0
delta = 3
q = Fraction(3, 5)


def choices(triangle):
    return [(None, 1 - q)] + [(edge, q / 3) for edge in triangle]


selections = Fraction(0)
distinct = Fraction(0)
for (edge_a, weight_a), (edge_b, weight_b) in product(choices(first), choices(second)):
    incident = [edge for edge in (edge_a, edge_b) if edge is not None and vertex in edge]
    assert len(incident) <= (delta - 1) * len(set(incident))
    selections += weight_a * weight_b * len(incident)
    distinct += weight_a * weight_b * len(set(incident))
lower = 2 * q * 2 / (3 * (delta - 1))
assert distinct >= lower and selections > distinct
print(f"Selection expectation: {selections}")
print(f"Distinct deletion expectation: {distinct}")
print(f"Multiplicity-corrected lower bound: {lower}")

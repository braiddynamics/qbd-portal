from fractions import Fraction
from itertools import product


p = Fraction(2, 5)
q = Fraction(3, 4)
seed = {"seed_leg_a", "seed_leg_b", "chord"}
first = {"branch_a", "addition_a", "chord"}
second = {"branch_b", "addition_b", "chord"}
deletions = [(None, 1 - q)] + [(edge, q / 3) for edge in sorted(seed)]
total = Fraction(0)
survival = Fraction(0)
for accept_first, accept_second in product((False, True), repeat=2):
    additions = (p if accept_first else 1 - p) * (p if accept_second else 1 - p)
    edges = seed | {"branch_a", "branch_b"}
    if accept_first:
        edges.add("addition_a")
    if accept_second:
        edges.add("addition_b")
    for edge, weight in deletions:
        final = edges - {edge}
        total += additions * weight
        if any(face <= final for face in (seed, first, second)):
            survival += additions * weight
assert total == 1
assert survival == 1 - q + 2 * q / 3 * (2 * p - p * p)
print(f"Exact seed-sector survival: {survival}")

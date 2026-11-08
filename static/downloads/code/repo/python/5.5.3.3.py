from fractions import Fraction
from itertools import product


def count_law(probabilities):
    distribution = [Fraction(0)] * (len(probabilities) + 1)
    for outcome in product((0, 1), repeat=len(probabilities)):
        weight = Fraction(1)
        for success, probability in zip(outcome, probabilities):
            weight *= probability if success else 1 - probability
        distribution[sum(outcome)] += weight
    assert sum(distribution) == 1
    return distribution


probabilities = [Fraction(1, 5), Fraction(2, 5), Fraction(3, 5)]
actual = count_law(probabilities)
envelope = count_law([max(probabilities)] * len(probabilities))
for threshold in range(1, len(probabilities) + 1):
    tail = sum(actual[threshold:])
    upper = sum(envelope[threshold:])
    assert tail <= upper
    print(f"Threshold {threshold}: {tail} <= {upper}")

vertices = 100
for name, edges in [("initial", 99.0), ("sampled active", 108.2), ("sampled final", 100.2)]:
    print(f"{name}: mean degree {2 * edges / vertices:.4f}")

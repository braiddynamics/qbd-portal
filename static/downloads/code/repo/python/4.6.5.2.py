from itertools import product
from math import e, exp, isclose, pi, sqrt


mu, lam = 1 / sqrt(2 * pi), e - 1
p = exp(-2 * mu)
q = min(1, (1 + 2 * lam) * exp(-2 * mu) / 2)
old_triangle = {("a", "b"), ("b", "c"), ("c", "a")}
new_triangle = {("b", "c"), ("c", "d"), ("d", "b")}
old = old_triangle | {("c", "d")}
delete_choices = [(None, 1 - q)] + [(edge, q / 3) for edge in sorted(old_triangle)]
drift = 0.0
for (add, add_weight), (edge, del_weight) in product(
    [(False, 1 - p), (True, p)], delete_choices
):
    final = (old | ({("d", "b")} if add else set())) - {edge}
    change = int(old_triangle <= final) + int(new_triangle <= final) - 1
    drift += add_weight * del_weight * change

assert isclose(drift, p * (1 - q / 3) - q)
assert drift <= p - q < 0
print(f"Enumerated one-tick triangle drift: {drift:.8f}")
print(f"Site-summed upper bound: {p - q:.8f}")

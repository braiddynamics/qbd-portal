"""Exact real Lie closure of Gaussian-rational matrices; no numerical rank cutoff."""
from sympy import I, Matrix, zeros


def elementary(n, i, j):
    a = zeros(n)
    a[i, j] = 1
    return a


def adjacent_generators(n):
    if n < 2:
        raise ValueError("At least two coordinates are required")
    x = [I * (elementary(n, k, k+1) + elementary(n, k+1, k)) for k in range(n-1)]
    z = [I * (elementary(n, k, k) - elementary(n, k+1, k+1)) for k in range(n-1)]
    return x, z


def real_coordinates(matrix):
    # All entries here are Gaussian rationals, so this is exact over Q.
    return [component for value in matrix for component in value.as_real_imag()]


def lie_basis(generators):
    basis = []
    echelon = {}

    def insert(matrix):
        vector = real_coordinates(matrix)
        for pivot in sorted(echelon):
            coefficient = vector[pivot]
            if coefficient:
                vector = [a - coefficient * b for a, b in zip(vector, echelon[pivot])]
        pivot = next((i for i, value in enumerate(vector) if value), None)
        if pivot is None:
            return
        scale = vector[pivot]
        echelon[pivot] = [value / scale for value in vector]
        basis.append(matrix)

    for generator in generators:
        insert(generator)
    cursor = 0
    while cursor < len(basis):
        for earlier in range(cursor):
            a, b = basis[cursor], basis[earlier]
            insert(a * b - b * a)
        cursor += 1
    return basis

print("n | exchange directions | diagonal directions | real closure dimension")
for n in (3,):
    exchanges, diagonals = adjacent_generators(n)
    generators = exchanges + diagonals
    expected = n * n - 1
    basis = lie_basis(generators)
    assert len(basis) == expected
    assert all(a.conjugate().T == -a and a.trace() == 0 for a in basis)
    print(f"{n} | {len(exchanges)} | {len(generators)-len(exchanges)} | {len(basis)}")

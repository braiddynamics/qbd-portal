# §8.2.8.2 — Swap-only Lie closure dimensions and diagonal obstruction
# Checks: Lie_R{i X_k} = D so(n) D† has zero diagonal and dim n(n-1)/2.
from sympy import I, Matrix, diag, zeros


def swap_only_closure(n):
    exchanges = []
    for k in range(n - 1):
        mat = zeros(n)
        mat[k, k + 1] = mat[k + 1, k] = I
        exchanges.append(mat)

    basis, coord_rows = [], []

    def add_if_independent(mat):
        vec = [comp for val in mat for comp in val.as_real_imag()]
        if Matrix(coord_rows + [vec]).rank() > len(coord_rows):
            coord_rows.append(vec)
            basis.append(mat)

    for gen in exchanges:
        add_if_independent(gen)
    idx = 0
    while idx < len(basis):
        for prev in range(idx):
            add_if_independent(basis[idx] * basis[prev] - basis[prev] * basis[idx])
        idx += 1

    conj = diag(*[I**j for j in range(n)])
    for elem in basis:
        assert all(elem[j, j] == 0 for j in range(n))
        rotated = conj.H * elem * conj
        assert rotated.T == -rotated
        assert all(entry.is_real for entry in rotated)
    return len(exchanges), len(basis)


print("n | exchanges | closure_dim | zero_diagonal | conjugate_so(n)")
for n in (2, 3, 5):
    num_ex, dim = swap_only_closure(n)
    assert dim == n * (n - 1) // 2
    print(f"{n} | {num_ex:<9} | {dim:<11} | true          | true")

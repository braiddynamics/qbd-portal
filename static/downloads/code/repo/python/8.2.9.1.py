# §8.2.9.1 — Adjacent exchange-plus-diagonal Lie closure and depth bound
# Checks: Lie_R{i X_k, i Z_k} = su(n) with dim n^2 - 1 and bracket depth <= n - 1.
from sympy import I, Matrix, zeros


def su_closure_with_depth(n):
    seeds = []
    for k in range(n - 1):
        ex = zeros(n)
        ex[k, k + 1] = ex[k + 1, k] = I
        dz = zeros(n)
        dz[k, k] = I
        dz[k + 1, k + 1] = -I
        seeds.extend((ex, dz))

    basis, coord_rows, depths = [], [], []

    def try_add(mat, depth):
        vec = [comp for val in mat for comp in val.as_real_imag()]
        if Matrix(coord_rows + [vec]).rank() > len(coord_rows):
            coord_rows.append(vec)
            basis.append(mat)
            depths.append(depth)
            return True
        return False

    for s in seeds:
        try_add(s, 0)

    depth = 0
    while len(basis) < n * n - 1 and depth < n:
        snapshot = len(basis)
        for i in range(snapshot):
            for j in range(i):
                if depths[i] == depth or depths[j] == depth:
                    try_add(basis[i] * basis[j] - basis[j] * basis[i], 1 + max(depths[i], depths[j]))
        depth += 1

    assert all(m.H == -m and m.trace() == 0 for m in basis)
    return n - 1, n - 1, len(basis), max(depths)


print("n | exchanges | diagonals | su(n)_dim | max_depth")
for n in (2, 3, 5):
    nex, ndz, dim, max_d = su_closure_with_depth(n)
    assert dim == n * n - 1
    assert max_d <= n - 1
    print(f"{n} | {nex:<9} | {ndz:<9} | {dim:<9} | {max_d}")

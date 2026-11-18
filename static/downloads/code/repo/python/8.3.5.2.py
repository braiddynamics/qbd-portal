# §8.3.5.2 — Explicit 3x3 tripartite commutator construction and su(3) spanning
# Checks: nested brackets yield F12, F23, F13, S13, spanning su(3) with dim 8.
from sympy import I, Matrix, symbols, zeros


def E(i, j):
    mat = zeros(3)
    mat[i, j] = 1
    return mat


def real_row(mat):
    return [comp for val in mat for comp in val.as_real_imag()]


A1, A2 = I * (E(0, 1) + E(1, 0)), I * (E(1, 2) + E(2, 1))
C1, C2 = I * (E(0, 0) - E(1, 1)), I * (E(1, 1) - E(2, 2))
S12, S23 = A1, A2
F12 = (A1 * C1 - C1 * A1) / 2
F23 = (A2 * C2 - C2 * A2) / 2
F13 = F12 * F23 - F23 * F12
S13 = F12 * A2 - A2 * F12

full_basis = [F12, S12, F13, S13, F23, S23, C1, C2]
swap_only = [A1, A2, A1 * A2 - A2 * A1]
assert Matrix([real_row(m) for m in full_basis]).rank() == 8
assert Matrix([real_row(m) for m in swap_only]).rank() == 3
assert all(m.H == -m and m.trace() == 0 for m in full_basis)

x, y, a12, b12, a13, b13, a23, b23 = symbols("x y a12 b12 a13 b13 a23 b23", real=True)
M = Matrix([
    [I * x, a12 + I * b12, a13 + I * b13],
    [-a12 + I * b12, I * y, a23 + I * b23],
    [-a13 + I * b13, -a23 + I * b23, -I * (x + y)],
])
R = (
    a12 * F12 + b12 * S12 + a13 * F13 + b13 * S13
    + a23 * F23 + b23 * S23 + x * C1 + (x + y) * C2
)
assert (R - M).expand() == zeros(3)

print("basis_set       | real_dim | skew_hermitian | traceless | reconstruction_error")
print("swap_only       | 3        | true           | true      | incomplete")
print("tripartite_seed | 8        | true           | true      | 0")

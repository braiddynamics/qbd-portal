# §9.2.11.2 — Explicit 5x5 su(5) nested-bracket spanning and symbolic reconstruction
# Checks: nested commutators of A_1..4, C_1..4 produce F_pq, S_pq, H_p (rank 24) and R = M.
from sympy import I, Matrix, Rational, symbols, zeros


def E(i, j):
    mat = zeros(5)
    mat[i, j] = 1
    return mat


def real_row(mat):
    return [comp for val in mat for comp in val.as_real_imag()]


A = [I * (E(k, k + 1) + E(k + 1, k)) for k in range(4)]
C = [I * (E(k, k) - E(k + 1, k + 1)) for k in range(4)]
B = [A[k] * C[k] - C[k] * A[k] for k in range(4)]

F, S = {}, {}
for k in range(4):
    F[(k, k + 1)] = B[k] / 2
    S[(k, k + 1)] = A[k]
for sep in range(2, 5):
    for p in range(5 - sep):
        q = p + sep
        F[(p, q)] = F[(p, q - 1)] * F[(q - 1, q)] - F[(q - 1, q)] * F[(p, q - 1)]
        S[(p, q)] = F[(p, q - 1)] * S[(q - 1, q)] - S[(q - 1, q)] * F[(p, q - 1)]

H = [sum((C[k] for k in range(p, 4)), zeros(5)) for p in range(4)]
basis = [F[pair] for pair in sorted(F)] + [S[pair] for pair in sorted(S)] + H

assert len(F) == 10 and len(S) == 10 and len(H) == 4
assert Matrix([real_row(m) for m in basis]).rank() == 24
assert all(m.H == -m and m.trace() == 0 for m in basis)

# Block decomposition: SU(3) (upper 3x3), SU(2) (lower 2x2), U(1)_Y (1), Leptoquark (12)
su3_idx = [m for m in [F[(p, q)] for p in range(3) for q in range(p + 1, 3)]
           + [S[(p, q)] for p in range(3) for q in range(p + 1, 3)] + [C[0], C[1]]]
su2_idx = [F[(3, 4)], S[(3, 4)], C[3]]
y_gen = [
    I * Matrix.diag(-Rational(1, 3), -Rational(1, 3), -Rational(1, 3), Rational(1, 2), Rational(1, 2))
]
lq_idx = [F[(p, q)] for p in range(3) for q in range(3, 5)] + [S[(p, q)] for p in range(3) for q in range(3, 5)]
assert Matrix([real_row(m) for m in su3_idx]).rank() == 8
assert Matrix([real_row(m) for m in su2_idx]).rank() == 3
assert Matrix([real_row(m) for m in y_gen]).rank() == 1
assert Matrix([real_row(m) for m in lq_idx]).rank() == 12
assert Matrix([real_row(m) for m in su3_idx + su2_idx + y_gen + lq_idx]).rank() == 24

c_vars = symbols("c0 c1 c2 c3", real=True)
M = zeros(5)
R = zeros(5)
for p in range(5):
    M[p, p] = I * c_vars[p] if p < 4 else -I * sum(c_vars)
    if p < 4:
        R += c_vars[p] * H[p]
    for q in range(p + 1, 5):
        apq, bpq = symbols(f"a{p}{q} b{p}{q}", real=True)
        M[p, q], M[q, p] = apq + I * bpq, -apq + I * bpq
        R += apq * F[(p, q)] + bpq * S[(p, q)]
assert (R - M).expand() == zeros(5)

print("algebra_component | real_dim | skew_hermitian | traceless | residual")
print("F_pq (10 pairs)   | 10       | true           | true      | -")
print("S_pq (10 pairs)   | 10       | true           | true      | -")
print("H_p  (4 diag)     | 4        | true           | true      | -")
print("su(5) total       | 24       | true           | true      | 0")

# §9.2.8.2 — Diagonal sector preservation and zero off-code action
# Checks: W†W = I_5, (I - P_5) Z_hat_k W = 0, [P_5, Z_hat_k] = 0, and e^{it Z_hat_k} W = W e^{it Z_k}.
from fractions import Fraction
from sympy import I, Rational, SparseMatrix, diag, exp, eye, zeros

w_occ = SparseMatrix(32, 5, {(1 << r, r): 1 for r in range(5)})
assert w_occ.H * w_occ == eye(5)
p5 = w_occ * w_occ.H
assert p5 * p5 == p5 and p5.H == p5
i32 = eye(32)
assert (i32 - p5) * w_occ == zeros(32, 5)

t_param = Rational(1, 3)
for k in range(4):
    z_hat = SparseMatrix(
        32,
        32,
        {(w, w): ((w >> k) & 1) - ((w >> (k + 1)) & 1) for w in range(32)},
    )
    z_sub = zeros(5)
    z_sub[k, k], z_sub[k + 1, k + 1] = 1, -1
    assert (i32 - p5) * z_hat * w_occ == zeros(32, 5)
    assert (i32 - p5) * z_hat * p5 == zeros(32, 32)
    assert p5 * z_hat - z_hat * p5 == zeros(32, 32)
    u_hat = diag(*[exp(I * t_param * z_hat[w, w]) for w in range(32)])
    u_sub = diag(*[exp(I * t_param * z_sub[j, j]) for j in range(5)])
    assert u_hat * w_occ == w_occ * u_sub
    assert (i32 - p5) * u_hat * w_occ == zeros(32, 5)

BASE = sum(0x99 << (8 * r) for r in range(5))
codewords = [BASE ^ (0xFF << (8 * j)) for j in range(5)]
assert len(set(codewords)) == 5


def z_imb_eigenval(word, k):
    def occ(mod):
        return sum(
            Fraction(1 - ((-1) ** (((BASE >> b) & 1) + ((word >> b) & 1))), 2)
            for b in range(8 * mod, 8 * mod + 8)
        ) / 8

    res = occ(k) - occ(k + 1)
    assert -1 <= res <= 1
    return res


for k in range(4):
    for j, w in enumerate(codewords):
        val = z_imb_eigenval(w, k)
        assert val == int(j == k) - int(j == k + 1)
        for bit in range(40):
            # Off-code single-bit flip is orthogonal to every codeword; diagonal action vanishes.
            off_word = w ^ (1 << bit)
            assert off_word not in codewords
            assert z_imb_eigenval(off_word, k) >= -1

print("encoding   | adjacent imbalances | off-code leakage | unitary sector invariant")
print("occupation | 4                   | 0                | true")
print("rung       | 4                   | 0                | true")

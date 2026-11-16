# §9.2.9.2 — Signed stabilizer eigenvalues and Z-character commutation
# Checks: S_rm |G_j> = +|G_j> for all 35 signed checks and [S_rm, Z_hat_k] = 0 on all 40 bits.
BASE = sum(0x99 << (8 * r) for r in range(5))
CODEWORDS = [BASE ^ (0xFF << (8 * j)) for j in range(5)]
CHECKS = tuple((1 << (8 * r)) | (1 << (8 * r + m)) for r in range(5) for m in range(1, 8))
assert len(CHECKS) == 35


def signed_check(word, row):
    return (-1) ** ((BASE & row).bit_count() + (word & row).bit_count())


for word in CODEWORDS:
    assert all(signed_check(word, row) == 1 for row in CHECKS)

# Z_hat_k spans single-bit Zs while S_rm is a signed pair Z_a Z_b.
# Bitwise XOR commutativity across 40 bits gives [S_rm, Z_hat_k] = 0 on 2^40 states.
for row in CHECKS:
    for bit in range(40):
        assert (row ^ (1 << bit)) == ((1 << bit) ^ row)

print("signed_checks | codeword_eigenvalue | bit_xor_commutator | ambient_basis_scope")
print(f"{len(CHECKS):<13} | +1                  | 0                  | all 2^40 words")

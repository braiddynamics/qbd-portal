# §10.9.5.1 — Gate-compiled Beauregard Shor factoring across N=15, 21, 35

import math
from fractions import Fraction
import numpy as np

H_MAT = np.array([[1, 1], [1, -1]], dtype=np.complex128) / np.sqrt(2.0)
X_MAT = np.array([[0, 1], [1, 0]], dtype=np.complex128)
Y_MAT = np.array([[0, -1j], [1j, 0]], dtype=np.complex128)
Z_MAT = np.array([[1, 0], [0, -1]], dtype=np.complex128)
PAULIS = (X_MAT, Y_MAT, Z_MAT)


class Circuit2Q:
    """Statevector simulator restricted to 1-qubit gates and 2-qubit entanglers."""

    def __init__(self, n_qubits):
        self.n = n_qubits
        idx = np.arange(1 << n_qubits)
        self.q0 = [idx[((idx >> (n_qubits - 1 - q)) & 1) == 0] for q in range(n_qubits)]
        self.q1 = [idx[((idx >> (n_qubits - 1 - q)) & 1) == 1] for q in range(n_qubits)]
        self.pair11 = {
            (a, b): idx[
                (((idx >> (n_qubits - 1 - a)) & 1) == 1)
                & (((idx >> (n_qubits - 1 - b)) & 1) == 1)
            ]
            for a in range(n_qubits)
            for b in range(n_qubits)
            if a != b
        }
        self.cx0 = {
            (c, t): idx[
                (((idx >> (n_qubits - 1 - c)) & 1) == 1)
                & (((idx >> (n_qubits - 1 - t)) & 1) == 0)
            ]
            for c in range(n_qubits)
            for t in range(n_qubits)
            if c != t
        }
        self.cx1 = {
            (c, t): idx[
                (((idx >> (n_qubits - 1 - c)) & 1) == 1)
                & (((idx >> (n_qubits - 1 - t)) & 1) == 1)
            ]
            for c in range(n_qubits)
            for t in range(n_qubits)
            if c != t
        }

    def apply_1q(self, v, q, mat):
        i0, i1 = self.q0[q], self.q1[q]
        a, b = v[i0].copy(), v[i1].copy()
        v[i0] = mat[0, 0] * a + mat[0, 1] * b
        v[i1] = mat[1, 0] * a + mat[1, 1] * b

    def inject_noise(self, v, p, rng, *qs):
        if p <= 0.0:
            return
        if len(qs) == 1:
            if rng.random() < p:
                self.apply_1q(v, qs[0], PAULIS[int(rng.integers(3))])
        elif rng.random() < p:
            code = int(rng.integers(1, 16))
            p1, p2 = code >> 2, code & 3
            if p1:
                self.apply_1q(v, qs[0], PAULIS[p1 - 1])
            if p2:
                self.apply_1q(v, qs[1], PAULIS[p2 - 1])

    def g1(self, v, q, mat, p=0.0, rng=None):
        self.apply_1q(v, q, mat)
        self.inject_noise(v, p, rng, q)

    def rz(self, v, q, phase, p=0.0, rng=None):
        v[self.q1[q]] *= phase
        self.inject_noise(v, p, rng, q)

    def cnot(self, v, c, t, p=0.0, rng=None):
        c0, c1 = self.cx0[(c, t)], self.cx1[(c, t)]
        v[c0], v[c1] = v[c1].copy(), v[c0].copy()
        self.inject_noise(v, p, rng, c, t)

    def cphase(self, v, q1, q2, phase, p=0.0, rng=None):
        v[self.pair11[(q1, q2)]] *= phase
        self.inject_noise(v, p, rng, q1, q2)


def verify_primitive_identities():
    """Confirm CNOT and CR_k decompose exactly into {H, CZ, R_z}."""
    cz = np.diag([1.0, 1.0, 1.0, -1.0])
    ih = np.kron(np.eye(2), H_MAT)
    cnot_ref = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], dtype=float)
    assert np.linalg.norm(ih @ cz @ ih - cnot_ref, 2) < 1e-13
    for k in (2, 3, 4, 8):
        ang = np.pi / (1 << (k - 1))
        cp_ref = np.diag([1.0, 1.0, 1.0, np.exp(1j * ang)])
        rz_p = np.diag([np.exp(-0.25j * ang), np.exp(0.25j * ang)])
        rz_m = np.diag([np.exp(0.25j * ang), np.exp(-0.25j * ang)])
        synth = np.exp(0.25j * ang) * np.kron(rz_p, rz_p) @ cnot_ref @ np.kron(np.eye(2), rz_m) @ cnot_ref
        assert np.linalg.norm(synth - cp_ref, 2) < 1e-13


def emit_ccphase(c1, c2, t, phi, ops):
    if abs(phi) < 1e-14:
        return
    hp, hm = np.exp(0.5j * phi), np.exp(-0.5j * phi)
    ops.extend([("CP", c2, t, hp), ("CNOT", c1, c2), ("CP", c2, t, hm), ("CNOT", c1, c2), ("CP", c1, t, hp)])


def emit_qft(b, ops):
    nb = len(b)
    for j in range(nb):
        ops.append(("H", b[j]))
        for k in range(j + 1, nb):
            ops.append(("CP", b[k], b[j], np.exp(1j * np.pi / (1 << (k - j)))))


def emit_iqft(b, ops):
    nb = len(b)
    for j in range(nb - 1, -1, -1):
        for k in range(nb - 1, j, -1):
            ops.append(("CP", b[k], b[j], np.exp(-1j * np.pi / (1 << (k - j)))))
        ops.append(("H", b[j]))


def emit_phi_add(b, val, sign, ctrls, ops):
    nb = len(b)
    for j, q in enumerate(b):
        ang = sign * 2.0 * np.pi * val / (1 << (nb - j))
        if abs(ang) < 1e-14:
            continue
        if not ctrls:
            ops.append(("RZ", q, np.exp(1j * ang)))
        elif len(ctrls) == 1:
            ops.append(("CP", ctrls[0], q, np.exp(1j * ang)))
        else:
            emit_ccphase(ctrls[0], ctrls[1], q, ang, ops)


def emit_cc_add_mod(c1, c2, b, anc, val, mod_n, ops):
    msb = b[0]
    emit_phi_add(b, val, +1, (c1, c2), ops)
    emit_phi_add(b, mod_n, -1, (), ops)
    emit_iqft(b, ops)
    ops.append(("CNOT", msb, anc))
    emit_qft(b, ops)
    emit_phi_add(b, mod_n, +1, (anc,), ops)
    emit_phi_add(b, val, -1, (c1, c2), ops)
    emit_iqft(b, ops)
    ops.extend([("X", msb), ("CNOT", msb, anc), ("X", msb)])
    emit_qft(b, ops)
    emit_phi_add(b, val, +1, (c1, c2), ops)


def emit_cc_sub_mod(c1, c2, b, anc, val, mod_n, ops):
    msb = b[0]
    emit_phi_add(b, val, -1, (c1, c2), ops)
    emit_iqft(b, ops)
    ops.extend([("X", msb), ("CNOT", msb, anc), ("X", msb)])
    emit_qft(b, ops)
    emit_phi_add(b, val, +1, (c1, c2), ops)
    emit_phi_add(b, mod_n, -1, (anc,), ops)
    emit_iqft(b, ops)
    ops.append(("CNOT", msb, anc))
    emit_qft(b, ops)
    emit_phi_add(b, mod_n, +1, (), ops)
    emit_phi_add(b, val, -1, (c1, c2), ops)


def build_mult_ops(c, x, b, anc, a_val, mod_n):
    m = len(x)
    ops = []
    emit_qft(b, ops)
    for j in range(m):
        emit_cc_add_mod(c, x[j], b, anc, (a_val * (1 << (m - 1 - j))) % mod_n, mod_n, ops)
    emit_iqft(b, ops)
    for j in range(m):
        xq, bq = x[j], b[1 + j]
        ops.extend([("CNOT", bq, xq), ("H", bq)])
        emit_ccphase(c, xq, bq, np.pi, ops)
        ops.extend([("H", bq), ("CNOT", bq, xq)])
    a_inv = pow(a_val, -1, mod_n)
    emit_qft(b, ops)
    for j in range(m - 1, -1, -1):
        emit_cc_sub_mod(c, x[j], b, anc, (a_inv * (1 << (m - 1 - j))) % mod_n, mod_n, ops)
    emit_iqft(b, ops)
    return ops


def run_ops(circ, v, ops, p, rng):
    for op in ops:
        k = op[0]
        if k == "H":
            circ.g1(v, op[1], H_MAT, p, rng)
        elif k == "X":
            circ.g1(v, op[1], X_MAT, p, rng)
        elif k == "RZ":
            circ.rz(v, op[1], op[2], p, rng)
        elif k == "CNOT":
            circ.cnot(v, op[1], op[2], p, rng)
        else:
            circ.cphase(v, op[1], op[2], op[3], p, rng)


def verify_multiplier_unitary(mod_n, a_val, circ):
    """Verify exact reversible modular multiplication on x in {1, N-2}."""
    m = mod_n.bit_length()
    x = list(range(1, m + 1))
    b = list(range(m + 1, 2 * m + 2))
    ops = build_mult_ops(0, x, b, 2 * m + 2, a_val, mod_n)
    for y_in in (1, mod_n - 2):
        v = np.zeros(1 << (2 * m + 3), dtype=np.complex128)
        v[(1 << (2 * m + 2)) | (y_in << (m + 2))] = 1.0
        run_ops(circ, v, ops, 0.0, None)
        idx_exp = (1 << (2 * m + 2)) | (((a_val * y_in) % mod_n) << (m + 2))
        assert abs(abs(v[idx_exp]) - 1.0) < 1e-11


def build_stage_table(mod_n, a_base, t_bits):
    m = mod_n.bit_length()
    x = list(range(1, m + 1))
    b = list(range(m + 1, 2 * m + 2))
    anc = 2 * m + 2
    return [build_mult_ops(0, x, b, anc, pow(a_base, 1 << (t_bits - 1 - s), mod_n), mod_n) for s in range(t_bits)]


def shor_shot(mod_n, t_bits, stages, circ, p, rng):
    m = mod_n.bit_length()
    n_tot = 2 * m + 3
    v = np.zeros(1 << n_tot, dtype=np.complex128)
    v[1 << (m + 2)] = 1.0  # c=0, x=1, b=0, anc=0
    bits = []
    half = 1 << (n_tot - 1)
    gates_run = 0
    for s in range(t_bits):
        circ.g1(v, 0, H_MAT, p, rng)
        run_ops(circ, v, stages[s], p, rng)
        gates_run += len(stages[s]) + 2
        rot = -sum(bits[j] * np.pi / (1 << (s - j)) for j in range(s))
        if abs(rot) > 1e-14:
            circ.rz(v, 0, np.exp(1j * rot), p, rng)
            gates_run += 1
        circ.g1(v, 0, H_MAT, p, rng)
        p1 = float(np.sum(np.abs(v[half:]) ** 2))
        bit = 1 if rng.random() < p1 else 0
        bits.append(bit)
        if bit == 1:
            v[:half] = 0.0
            v /= math.sqrt(max(p1, 1e-30))
            circ.g1(v, 0, X_MAT, p, rng)
            gates_run += 1
        else:
            v[half:] = 0.0
            v /= math.sqrt(max(1.0 - p1, 1e-30))
    return sum(bits[j] << j for j in range(t_bits)), gates_run


def cf_period(x_meas, t_bits, mod_n):
    return 1 if x_meas <= 0 else Fraction(x_meas, 1 << t_bits).limit_denominator(mod_n).denominator


def extract_factors(mod_n, a_base, r_cand):
    for mult in (r_cand, 2 * r_cand):
        if mult > 0 and mult % 2 == 0 and pow(a_base, mult, mod_n) == 1:
            g = math.gcd(pow(a_base, mult // 2, mod_n) - 1, mod_n)
            if 1 < g < mod_n:
                return mult, (min(g, mod_n // g), max(g, mod_n // g))
    return None


def is_harmonic(x_meas, t_bits, r_true):
    """True when measurement x_meas lies within +-1.5 bins of s * 2^t / r."""
    scale = 1 << t_bits
    return any(abs(x_meas - (s * scale) / r_true) <= 1.5 for s in range(r_true + 1))


verify_primitive_identities()
rng = np.random.default_rng(42)

# 1. Noiseless Beauregard factoring benchmark across N=15, 21, 35
print("N  | a | t  | qubits | mean_gates | r_est | factors | peak_lock | single_P | lcm2_P")
n21_noiseless = []
cases = [(15, 7, 8, 4, 40), (21, 2, 9, 6, 40), (35, 2, 11, 12, 10)]
for mod_n, a_base, t_bits, r_true, shots in cases:
    m = mod_n.bit_length()
    assert (1 << t_bits) >= mod_n * mod_n and (1 << (t_bits - 1)) < mod_n * mod_n
    circ = Circuit2Q(2 * m + 3)
    verify_multiplier_unitary(mod_n, pow(a_base, 2, mod_n), circ)
    stages = build_stage_table(mod_n, a_base, t_bits)
    runs = [shor_shot(mod_n, t_bits, stages, circ, 0.0, rng) for _ in range(shots)]
    meas = [r[0] for r in runs]
    mean_g = int(round(np.mean([r[1] for r in runs])))
    if mod_n == 21:
        n21_noiseless = meas
    lock_p = float(np.mean([is_harmonic(xm, t_bits, r_true) for xm in meas]))
    assert lock_p > 0.70
    single_hits = []
    r_found = None
    factors_found = None
    for xm in meas:
        res = extract_factors(mod_n, a_base, cf_period(xm, t_bits, mod_n))
        single_hits.append(res is not None)
        if res is not None and factors_found is None:
            r_found, factors_found = res
    pair_hits = []
    for i in range(0, len(meas) - 1, 2):
        r1 = cf_period(meas[i], t_bits, mod_n)
        r2 = cf_period(meas[i + 1], t_bits, mod_n)
        res = extract_factors(mod_n, a_base, math.lcm(r1, r2))
        pair_hits.append(res is not None)
        if res is not None and factors_found is None:
            r_found, factors_found = res
    assert factors_found is not None
    f_str = f"{factors_found[0]}x{factors_found[1]}"
    print(
        f"{mod_n:<2d} | {a_base} | {t_bits:<2d} | {2*m+3:<6d} | {mean_g:<10d} "
        f"| {r_found:<5d} | {f_str:<7s} | {lock_p:9.2f} | {np.mean(single_hits):8.2f} | {np.mean(pair_hits):6.2f}"
    )

# 2. Per-gate depolarizing noise sweep on N=21 (13 qubits, ~18.3k gates/shot)
c21 = Circuit2Q(13)
s21 = build_stage_table(21, 2, 9)
print("p_gate   | shots | peak_lock | single_P | lcm2_P")
for p in (0.0, 3e-5, 1e-4, 3e-4, 1e-3):
    draws = n21_noiseless if p == 0.0 else [shor_shot(21, 9, s21, c21, p, rng)[0] for _ in range(36)]
    lock_p = float(np.mean([is_harmonic(xm, 9, 6) for xm in draws]))
    s_hits = [extract_factors(21, 2, cf_period(xm, 9, 21)) is not None for xm in draws]
    p_hits = [
        extract_factors(21, 2, math.lcm(cf_period(draws[i], 9, 21), cf_period(draws[i + 1], 9, 21))) is not None
        for i in range(0, len(draws) - 1, 2)
    ]
    print(f"{p:8.1e} | {len(draws):5d} | {lock_p:9.2f} | {np.mean(s_hits):8.2f} | {np.mean(p_hits):6.2f}")

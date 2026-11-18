# §10.9.4.1 — Solovay-Kitaev SU(2) refinement and SU(2^n) QSD synthesis

import numpy as np
import qutip as qt
import scipy.linalg as sl

H_MAT = 1j / np.sqrt(2) * np.array([[1, 1], [1, -1]], dtype=complex)
T_MAT = np.exp(-1j * np.pi / 8) * np.diag([1, np.exp(1j * np.pi / 4)])
GENS = (H_MAT, H_MAT.conj().T, T_MAT, T_MAT.conj().T)
INV = {0: 1, 1: 0, 2: 3, 3: 2}
PAULI = (
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
)


def su2_to_quat(u):
    """Map SU(2) matrix to unit quaternion (w, x, y, z) on S^3."""
    return np.array(
        [u[0, 0].real, -u[0, 1].imag, -u[0, 1].real, -u[0, 0].imag],
        dtype=float,
    )


def build_base_net(max_len=18):
    """Enumerate unique SU(2) gate words up to max_len using BFS."""
    seen = {tuple(np.round(su2_to_quat(np.eye(2)), 10)): ()}
    mats = [np.eye(2, dtype=complex)]
    quats = [np.array([1.0, 0.0, 0.0, 0.0])]
    frontier = [(mats[0], ())]
    for _ in range(max_len):
        nxt = []
        for u, w in frontier:
            for gi, g in enumerate(GENS):
                if w and w[-1] == INV[gi]:
                    continue
                u2 = g @ u
                q = su2_to_quat(u2)
                key = tuple(np.round(q, 10))
                if key not in seen:
                    w2 = w + (gi,)
                    seen[key] = w2
                    mats.append(u2)
                    quats.append(q)
                    nxt.append((u2, w2))
        frontier = nxt
    return np.array(quats), np.array(mats), list(seen.values())


QUATS, NET_MATS, NET_WORDS = build_base_net(18)


def gc_decompose(delta):
    """Balanced group commutator delta = V W V^dag W^dag in SU(2)."""
    q = su2_to_quat(delta)
    w0 = np.clip(q[0], -1.0, 1.0)
    vec = q[1:]
    vnorm = np.linalg.norm(vec)
    if vnorm < 1e-13:
        eye = np.eye(2, dtype=complex)
        return eye, eye
    n_hat = vec / vnorm
    s = ((1.0 - w0) / 2.0) ** 0.25
    c = np.sqrt(max(0.0, 1.0 - s * s))
    v0 = c * np.eye(2, dtype=complex) - 1j * s * PAULI[0]
    w0_m = c * np.eye(2, dtype=complex) - 1j * s * PAULI[1]
    q0 = su2_to_quat(v0 @ w0_m @ v0.conj().T @ w0_m.conj().T)
    m_hat = q0[1:] / np.linalg.norm(q0[1:])
    mid = m_hat + n_hat
    mid_n = np.linalg.norm(mid)
    if mid_n < 1e-12:
        orth = np.cross(m_hat, [1.0, 0.0, 0.0])
        if np.linalg.norm(orth) < 1e-6:
            orth = np.cross(m_hat, [0.0, 1.0, 0.0])
        axis = orth / np.linalg.norm(orth)
    else:
        axis = mid / mid_n
    rot = -1j * sum(axis[i] * PAULI[i] for i in range(3))
    return rot @ v0 @ rot.conj().T, rot @ w0_m @ rot.conj().T


def sk_compile(u, depth):
    """Recursive Dawson-Nielsen Solovay-Kitaev approximation in SU(2)."""
    if depth == 0:
        idx = int(np.argmax(QUATS @ su2_to_quat(u)))
        return NET_WORDS[idx], NET_MATS[idx]
    w_p, u_p = sk_compile(u, depth - 1)
    v, w = gc_decompose(u @ u_p.conj().T)
    w_v, v_a = sk_compile(v, depth - 1)
    w_w, w_a = sk_compile(w, depth - 1)
    inv_v = tuple(INV[g] for g in reversed(w_v))
    inv_w = tuple(INV[g] for g in reversed(w_w))
    word = w_p + inv_w + inv_v + w_w + w_v
    mat = v_a @ w_a @ v_a.conj().T @ w_a.conj().T @ u_p
    return word, mat


def walsh_hadamard(angles):
    """Compute normalized inverse Walsh-Hadamard transform of rotation angles."""
    phi = np.array(angles, dtype=float)
    m = len(phi)
    step = 1
    while step < m:
        for i in range(0, m, 2 * step):
            for j in range(step):
                a, b = phi[i + j], phi[i + j + step]
                phi[i + j], phi[i + j + step] = a + b, a - b
        step *= 2
    return phi / m


def emit_ucg(angles, pauli_idx, qubits, depth, ops):
    """Compile uniformly controlled SU(2) rotation into {H, T, CZ} ops."""
    target, ctrls = qubits[0], qubits[1:]
    k = len(ctrls)
    m = 1 << k
    phi = walsh_hadamard(angles)
    for s_idx in range(m):
        g = s_idx ^ (s_idx >> 1)
        ang = phi[g]
        if abs(ang) > 1e-13:
            rot = np.cos(ang / 2) * np.eye(2, dtype=complex) - 1j * np.sin(ang / 2) * PAULI[pauli_idx]
            word, _ = sk_compile(rot, depth)
            for gi in word:
                ops.append((gi, target))
        g_next = (s_idx + 1) ^ ((s_idx + 1) >> 1) if s_idx + 1 < m else 0
        diff = g ^ g_next
        bit = (diff & -diff).bit_length() - 1
        c_q = ctrls[k - 1 - bit]
        # CNOT = H_hat CZ H_hat^dag cancels extra scalar phases cleanly
        ops.extend([(0, target), ("CZ", c_q, target), (1, target)])


def demultiplex(a_blk, b_blk, qubits, depth, ops):
    """Factor block-diagonal diag(A, B) into sub-blocks and controlled R_z."""
    t_mat, v_mat = sl.schur(a_blk @ b_blk.conj().T, output="complex")
    lam = np.angle(np.diag(t_mat))
    d_diag = np.exp(0.5j * lam)
    w_mat = (d_diag.conj()[:, None]) * (v_mat.conj().T @ a_blk)
    qsd_compile(w_mat, qubits[1:], depth, ops)
    emit_ucg(-lam, 2, qubits, depth, ops)
    qsd_compile(v_mat, qubits[1:], depth, ops)


def qsd_compile(u, qubits, depth, ops):
    """Compile n-qubit unitary into primitive {H, H^dag, T, T^dag, CZ} ops."""
    if len(qubits) == 1:
        u_su2 = u / np.sqrt(np.linalg.det(u))
        word, _ = sk_compile(u_su2, depth)
        for gi in word:
            ops.append((gi, qubits[0]))
        return
    half = u.shape[0] // 2
    (u1, u2), theta, (v1h, v2h) = sl.cossin(u, p=half, q=half, separate=True)
    demultiplex(v1h, v2h, qubits, depth, ops)
    emit_ucg(2.0 * theta, 1, qubits, depth, ops)
    demultiplex(u1, u2, qubits, depth, ops)


def evaluate_ops(ops, n_qubits):
    """Multiply primitive gate list sequentially, contracting 1q runs."""
    dim = 1 << n_qubits
    total = np.eye(dim, dtype=complex)
    i2 = np.eye(2, dtype=complex)

    def embed1(mat, q):
        res = mat if q == 0 else i2
        for i in range(1, n_qubits):
            res = np.kron(res, mat if i == q else i2)
        return res

    def cz_mat(q1, q2):
        diag = np.ones(dim, dtype=complex)
        for b in range(dim):
            if ((b >> (n_qubits - 1 - q1)) & 1) and ((b >> (n_qubits - 1 - q2)) & 1):
                diag[b] = -1.0
        return np.diag(diag)

    run_q, run_mat = None, None
    for op in ops:
        if op[0] == "CZ":
            if run_q is not None:
                total = embed1(run_mat, run_q) @ total
                run_q = None
            total = cz_mat(op[1], op[2]) @ total
        else:
            gi, q = op
            if run_q == q:
                run_mat = GENS[gi] @ run_mat
            else:
                if run_q is not None:
                    total = embed1(run_mat, run_q) @ total
                run_q, run_mat = q, GENS[gi]
    if run_q is not None:
        total = embed1(run_mat, run_q) @ total
    return total


def eval_word_su2(word):
    """Reconstruct exact SU(2) product matrix from primitive indices."""
    mat = np.eye(2, dtype=complex)
    for gi in word:
        mat = GENS[gi] @ mat
    return mat


def proj_op_norm(target, approx):
    """Phase-aligned operator norm distance between two unitaries."""
    phi = np.angle(np.trace(target.conj().T @ approx))
    return float(np.linalg.norm(target - np.exp(-1j * phi) * approx, 2))


# 1. Single-qubit SU(2) Dawson-Nielsen refinement on seeded U_target
u_raw = qt.rand_unitary(2, seed=42).full()
u_su2_target = u_raw / np.sqrt(np.linalg.det(u_raw))

print(f"SU(2) base net size (L0 <= 18): {len(NET_MATS)}")
print("depth | gate_count | ||U - U_n||_op | word_check")
for d in range(6):
    w_d, u_d = sk_compile(u_su2_target, d)
    err_d = float(np.linalg.norm(u_su2_target - u_d, 2))
    w_chk = float(np.linalg.norm(u_d - eval_word_su2(w_d), 2))
    assert w_chk < 1e-12
    if d == 5:
        assert err_d < 1e-6
    print(f"{d:5d} | {len(w_d):10d} | {err_d:14.3e} | {w_chk:10.2e}")

# 2. Multi-qubit SU(2^n) compilation into {H, T, CZ} (QSD + SK depth 4)
rng = np.random.default_rng(42)
print("qubits | group  | CZ_gates | 1q_gates   | projective_error")
for nq in (1, 2, 3):
    dim = 1 << nq
    raw = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
    q_mat, r_mat = np.linalg.qr(raw)
    q_mat *= np.sign(np.diag(r_mat))
    u_nq = q_mat / (np.linalg.det(q_mat) ** (1.0 / dim))
    ops = []
    qsd_compile(u_nq, list(range(nq)), 4, ops)
    assert all(op[0] in (0, 1, 2, 3, "CZ") for op in ops)
    u_approx = evaluate_ops(ops, nq)
    err_nq = proj_op_norm(u_nq, u_approx)
    assert err_nq < 1e-3
    cz_count = sum(1 for op in ops if op[0] == "CZ")
    oneq_count = len(ops) - cz_count
    grp = f"SU({dim})"
    print(f"{nq:6d} | {grp:<6s} | {cz_count:8d} | {oneq_count:10d} | {err_nq:16.3e}")

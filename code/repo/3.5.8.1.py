import numpy as np
# Pauli matrices
I = np.eye(2)
Z = np.array([[1, 0], [0, -1]])
X = np.array([[0, 1], [1, 0]])
# 6-qubit space
dim = 64
# Tensor helper
def tensor_op(op, pos, n=6):
    ops = [I] * n
    ops[pos] = op
    result = ops[0]
    for o in ops[1:]:
        result = np.kron(result, o)
    return result
# General Π_pair: diag 1 for not both fwd/rev=1, 0 if both q_fwd and q_rev =1
def general_pi_pair(q_fwd, q_rev, dim=64):
    diag_vec = np.ones(dim)
    for i in range(dim):
        # Binary, q0 MSB index0 (bit5='1' for i&32), ..., q5 LSB index5 (bit0='1' for i&1)
        bin_str = f'{i:06b}' # bin_str[0]=MSB q0, bin_str[5]=LSB q5
        qf_bit = int(bin_str[q_fwd]) # bit pos = q_fwd (0=MSB)
        qr_bit = int(bin_str[q_rev])
        if qf_bit == 1 and qr_bit == 1:
            diag_vec[i] = 0
    return np.diag(diag_vec)
Pi_AB = general_pi_pair(0,1)
Pi_BC = general_pi_pair(2,3)
Pi_CA = general_pi_pair(4,5)
# K's (forwards)
K_AB = tensor_op(Z, 0)
K_BC = tensor_op(Z, 2)
K_CA = tensor_op(Z, 4)
# State vec
def get_state_vec(state_int, dim=64):
    vec = np.zeros(dim)
    vec[state_int] = 1.0
    return vec
# States: vac 0=000000; tension CA q4=1 (bit1 from LSB? MSB q0 bit5=32, ..., q4 bit1=2 → i=2 '000010')
# exc AB q0 bit5=32, BC q2 bit3=8, CA q4 bit1=2 =32+8+2=42 '101010'
# 2-cycle AB-BA q0 bit5=32 q1 bit4=16 =48 '110000'
states_to_test = [0, 2, 42, 48]
state_labels = {0: '000000 (vac)', 2: '000010 (tension CA)', 42: '101010 (exc fwd)', 48: '110000 (2-cycle AB-BA)'}
results = []
for s in states_to_test:
    vec = get_state_vec(s)
    label = state_labels[s]
    pi_ab_eig = np.dot(vec, Pi_AB @ vec)
    pi_bc_eig = np.dot(vec, Pi_BC @ vec)
    pi_ca_eig = np.dot(vec, Pi_CA @ vec)
    pi_all = pi_ab_eig * pi_bc_eig * pi_ca_eig
    k_ab = float(np.dot(vec, K_AB @ vec))
    k_bc = float(np.dot(vec, K_BC @ vec))
    k_ca = float(np.dot(vec, K_CA @ vec))
    syndrome = (k_ab, k_bc, k_ca)
    results.append({'State': label, 'Π_all': pi_all, 'Syndrome (K)': syndrome, 'In C?': 1 if np.isclose(pi_all, 1) else 0})
import pandas as pd
df = pd.DataFrame(results)
print(df.to_markdown(index=False))
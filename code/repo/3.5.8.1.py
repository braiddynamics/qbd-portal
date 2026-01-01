import numpy as np
import pandas as pd

# Pauli matrices
I = np.eye(2)
Z = np.array([[1.0, 0.0], [0.0, -1.0]])

def tensor_op(op, pos, n=6):
    """Tensor product of operator at position pos with identity elsewhere."""
    ops = [I] * n
    ops[pos] = op
    result = ops[0]
    for o in ops[1:]:
        result = np.kron(result, o)
    return result

# Hard constraint projectors: annihilate reciprocal edges (2-cycles)
def cycle_projector(q_fwd, q_rev):
    """Diagonal projector: 0 if both forward and reverse edges present."""
    diag = np.ones(64)
    for i in range(64):
        bin_str = f'{i:06b}'
        fwd = int(bin_str[q_fwd])
        rev = int(bin_str[q_rev])
        if fwd == 1 and rev == 1:
            diag[i] = 0.0
    return np.diag(diag)

Pi_AB = cycle_projector(0, 1)   # q_AB=0, q_BA=1
Pi_BC = cycle_projector(2, 3)   # q_BC=2, q_CB=3
Pi_CA = cycle_projector(4, 5)   # q_CA=4, q_AC=5

# Geometric check operators (forward edges only)
K_AB = tensor_op(Z, 0)
K_BC = tensor_op(Z, 2)
K_CA = tensor_op(Z, 4)

# Test states (binary index → 6-qubit state)
test_states = {
    0:  '000000 (Vacuum)',
    2:  '000010 (Tension: CA present)',
    42: '101010 (Excitation: forward 3-cycle)',
    48: '110000 (Invalid: AB↔BA 2-cycle)'
}

results = []
for idx, label in test_states.items():
    vec = np.zeros(64)
    vec[idx] = 1.0
    
    # Total projector eigenvalue
    pi_ab = vec @ Pi_AB @ vec
    pi_bc = vec @ Pi_BC @ vec
    pi_ca = vec @ Pi_CA @ vec
    pi_total = pi_ab * pi_bc * pi_ca
    
    # Syndrome eigenvalues
    k_ab = float(vec @ K_AB @ vec)
    k_bc = float(vec @ K_BC @ vec)
    k_ca = float(vec @ K_CA @ vec)
    
    results.append({
        'State': label,
        'Π_total': f'{pi_total:.1f}',
        'Syndrome (K_AB, K_BC, K_CA)': f'({k_ab:+.1f}, {k_bc:+.1f}, {k_ca:+.1f})',
        'In Codespace ℂ': 'Yes' if np.isclose(pi_total, 1.0) else 'No'
    })

df = pd.DataFrame(results)
print(df.to_markdown(index=False, tablefmt="github"))
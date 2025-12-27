import numpy as np
# Pauli Z
Z = np.array([[1, 0], [0, -1]])
# Z ⊗ Z ⊗ Z ⊗ Z
Z4 = np.kron(np.kron(np.kron(Z, Z), Z), Z)
basis_4 = np.eye(16)
print("State |qs>: Eigenvalue (Syndrome)")
for i in range(16):
    state = basis_4[:, i]
    ev = state.T @ Z4 @ state
    # Format state string
    state_str = bin(i)[2:].zfill(4)
    print(f"State |{state_str}>: {ev:.1f}")
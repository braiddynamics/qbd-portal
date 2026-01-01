import numpy as np
import pandas as pd

# Pauli-Z matrix
Z = np.array([[1.0, 0.0],
              [0.0, -1.0]])

# Stabilizer operator S = Z ⊗ Z ⊗ Z ⊗ Z (4-qubit parity check)
S = np.kron(np.kron(np.kron(Z, Z), Z), Z)

# Computational basis states (16 vectors in ℝ¹⁶)
basis_states = np.eye(16)

# Compute eigenvalues and collect results
results = []
for i in range(16):
    state = basis_states[:, i]
    eigenvalue = float(state.T @ S @ state)  # Exact eigenvalue: ±1.0
    
    binary = format(i, '04b')
    excitations = bin(i).count('1')
    parity = "Even" if excitations % 2 == 0 else "Odd"
    
    results.append({
        "State |ψ⟩": f"|{binary}⟩",
        "Excitations": excitations,
        "Parity": parity,
        "Eigenvalue λ": f"{eigenvalue:+.1f}"
    })

# Render as aligned Markdown table
df = pd.DataFrame(results)
print(df.to_markdown(index=False, tablefmt="github"))
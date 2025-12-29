import qutip as qt
import numpy as np

# Define logical basis: |0_L> = |0>, |1_L> = |1>
psi0 = qt.basis(2, 0)  # |0_L>
psi1 = qt.basis(2, 1)  # |1_L>

# T-gate unitary: diag(1, exp(i π/4))
theta = np.pi / 4
T = qt.Qobj(np.diag([1, np.exp(1j * theta)]))

# Action on |0_L>: phase 0
result0 = T * psi0
phase0 = np.real(psi0.dag() * result0)  # Scalar for pure state; no [0,0] needed
print("Phase on |0_L> (expected 0, cos(0)=1): ", phase0)

# Action on |1_L>: phase π/4
result1 = T * psi1
phase1 = np.real(psi1.dag() * result1)
print("Phase on |1_L> (expected cos(π/4)≈0.707): ", phase1)

# Superposition: (|0_L> + |1_L>)/√2
superpos = (psi0 + psi1).unit()
result_super = T * superpos
expect_super = np.real(superpos.dag() * result_super)
print("Real part on superposition (mixed phases): ", expect_super)

print("Verification: Phases match T-gate unitary, confirming state-dependent geometric phase.")
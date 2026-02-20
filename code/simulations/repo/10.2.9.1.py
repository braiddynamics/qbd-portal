import qutip as qt
import numpy as np

# Define Pauli matrices
I = qt.qeye(2)
X = qt.sigmax()
Z = qt.sigmaz()

# Assume a 6-qubit system for demonstration

# Case 1: Disjoint geometric stabilizers on qubits 0-2 and 3-5
S_geom1 = qt.tensor(Z, Z, Z, I, I, I)
S_geom2 = qt.tensor(I, I, I, Z, Z, Z)
comm1 = (S_geom1 * S_geom2 - S_geom2 * S_geom1).norm()
print("Disjoint geometric commutator norm: ", comm1)

# Case 2: Overlapping geometric on qubits 0-2 and 2-4 (share qubit 2)
S_geom_overlap1 = qt.tensor(Z, Z, Z, I, I, I)
S_geom_overlap2 = qt.tensor(I, I, Z, Z, Z, I)
comm2 = (S_geom_overlap1 * S_geom_overlap2 - S_geom_overlap2 * S_geom_overlap1).norm()
print("Overlapping geometric commutator norm: ", comm2)

# Case 3: Ribbon stabilizer on qubits 0-3: Z0 Z1 Z2 Z3, geom on 1,2,4 (even overlap on 1,2)
S_ribbon = qt.tensor(Z, Z, Z, Z, I, I)
S_geom_r = qt.tensor(I, Z, Z, I, Z, I)
comm3 = (S_ribbon * S_geom_r - S_geom_r * S_ribbon).norm()
print("Ribbon-geom commutator norm (even overlap): ", comm3)

# Case 4: Vertex X stabilizers, v1 incident to 0,1: X0 X1, v2 to 1,2: X1 X2
S_v1 = qt.tensor(X, X, I, I, I, I)
S_v2 = qt.tensor(I, X, X, I, I, I)
comm4 = (S_v1 * S_v2 - S_v2 * S_v1).norm()
print("Vertex X commutator norm: ", comm4)

# Case 5: Vertex X and geom Z with even overlap (share two edges: 0,1)
S_v_even = qt.tensor(X, X, I, I, I, I)
S_geom_even = qt.tensor(Z, Z, Z, Z, I, I)
comm5 = (S_v_even * S_geom_even - S_geom_even * S_v_even).norm()
print("Vertex-geom even overlap commutator norm: ", comm5)

# Odd overlap contrast (share one: qubit 0)
S_geom_odd = qt.tensor(Z, I, Z, I, I, I)
comm6 = (S_v_even * S_geom_odd - S_geom_odd * S_v_even).norm()
print("Odd overlap (should not commute): ", comm6)

print("Commutators near 0 confirm commutation where designed.")
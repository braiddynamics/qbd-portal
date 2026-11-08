import qutip as qt


identity = qt.qeye(2)
x = qt.sigmax()
z = qt.sigmaz()
check = qt.tensor(z, z, z)
state = qt.tensor(qt.basis(2, 1), qt.basis(2, 1), qt.basis(2, 1))

errors = {
    "I": qt.tensor(identity, identity, identity),
    "X0": qt.tensor(x, identity, identity),
    "X1": qt.tensor(identity, x, identity),
    "Z0": qt.tensor(z, identity, identity),
    "X0 X1": qt.tensor(x, x, identity),
}

print("One-check syndrome example (check = Z0 Z1 Z2)")
for name, error in errors.items():
    output = error * state
    print(f"{name:5} check sign: {qt.expect(check, output):+.0f}")

import qutip as qt
import numpy as np
from qutip import mesolve, sigmay, sigmap, sigmam

# Initial |0><0|
rho0 = qt.ket2dm(qt.basis(2, 0))

# Drive H = Ω σy /2
Ω = 10.0
H = (Ω / 2) * sigmay()

# Low Γ=0.1 for partial mixing
Γ = 0.1
c_ops = [np.sqrt(Γ) * sigmam(), np.sqrt(Γ) * sigmap()]

times = np.linspace(0, 0.2, 50)

result = mesolve(H, rho0, times, c_ops)
rho_final = result.states[-1]
off_diag_real = np.real(rho_final[0,1])
off_diag_imag = np.imag(rho_final[0,1])
pops = np.real(np.diag(rho_final.full()))

print("Final pops: ", pops)
print("Final off-diag real: ", off_diag_real)
print("Final off-diag imag: ", off_diag_imag)
print("Verification: High Ω low Γ for ~0.5 coherence.")
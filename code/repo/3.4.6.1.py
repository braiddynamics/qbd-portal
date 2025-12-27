import numpy as np

# Params: ε_geo=1, ΔS=ln(2)≈0.693
eps_geo = 1.0
delta_S = np.log(2)
T_high = 10 * eps_geo / delta_S  # High T
T_low = 0.5 * eps_geo / delta_S  # Half-crossover for P_acc≈0.5

def metropolis_acc(T, delta_U=eps_geo, delta_S=delta_S):
    delta_F = delta_U - T * delta_S
    return min(1, np.exp(-delta_F / T))

# Sim P_acc over 10^4 proposals
n_trials = 10000
P_acc_high = np.mean([metropolis_acc(T_high) for _ in range(n_trials)])
P_acc_low = np.mean([metropolis_acc(T_low) for _ in range(n_trials)])

# Poisson P_ign for N=1000
N = 1000
N_pot = N**2 / 2
lambda_high = N_pot * P_acc_high
lambda_low = N_pot * P_acc_low
P_ign_high = 1 - np.exp(-lambda_high)
P_ign_low = 1 - np.exp(-lambda_low)

print(f"High T: P_acc={P_acc_high:.3f}, P_ign={P_ign_high:.3f}")
print(f"Low T: P_acc={P_acc_low:.3f}, P_ign={P_ign_low:.3f}")
import numpy as np

def shannon_entropy(p):
    """Shannon entropy in bits, safely handling zero probabilities."""
    p = np.asarray(p)
    p = p[p > 0]                        # Remove zero entries to avoid log(0)
    if len(p) == 0:
        return 0.0
    return -np.sum(p * np.log2(p))

# Number of Monte Carlo trials for statistical precision
n_trials = 10_000

entropy_production = []

for _ in range(n_trials):
    # Provisional distribution: ~50% valid path A, ~25% valid path B, ~25% invalid path C
    # Small Gaussian noise simulates realistic branching fluctuations
    noise = np.random.normal(0, 0.005, 2)
    p_A = max(0.0, 0.50 + noise[0])
    p_B = max(0.0, 0.25 + noise[1])
    p_C = max(0.0, 1.0 - p_A - p_B)     # Ensure non-negative and sum = 1
    
    provisional = np.array([p_A, p_B, p_C])
    S_provisional = shannon_entropy(provisional)
    
    # Projection: discard invalid path C, renormalize valid paths
    valid_mass = p_A + p_B
    if valid_mass > 0:
        projected = np.array([p_A / valid_mass, p_B / valid_mass, 0.0])
    else:
        projected = np.array([1.0, 0.0, 0.0])  # Degenerate fallback
    
    # Sampling: collapse to single outcome → entropy = 0
    S_final = 0.0
    
    # Entropy production = information lost to the environment
    delta_S = S_provisional - S_final
    entropy_production.append(delta_S)

avg_delta = np.mean(entropy_production)
std_delta = np.std(entropy_production)

print("Irreversibility via Entropy Production in 𝒰")
print("=" * 48)
print(f"Monte Carlo trials:         {n_trials:,}")
print(f"Average ΔS per tick:        {avg_delta:.5f} bits")
print(f"Standard deviation:         {std_delta:.5f} bits")
print(f"Minimum observed ΔS:        {min(entropy_production):.5f} bits")
print(f"Strictly positive ΔS:       {avg_delta > 0}")
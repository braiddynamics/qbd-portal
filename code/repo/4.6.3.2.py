import numpy as np

def shannon_entropy(p):
    p = p[p > 0]
    return -np.sum(p * np.log2(p)) if len(p) > 0 else 0.0

# Multi-trial: Avg over 100 runs
n_trials = 100
losses = []

for _ in range(n_trials):
    # Provisional: 50% Valid Path A, 25% Valid Path B, 25% Invalid Path C (with noise)
    p_valid_A = 0.5 + np.random.normal(0, 0.01)
    p_invalid = 0.25
    p_valid_B = 1.0 - p_valid_A - p_invalid
    prov = np.array([p_valid_A, p_valid_B, p_invalid])
    
    S_prov = shannon_entropy(prov)
    
    # Projection: Discard C (index 2), renorm A and B
    valid_sum = prov[0] + prov[1]
    proj = np.array([prov[0]/valid_sum, prov[1]/valid_sum, 0.0])
    
    # Sampling: Collapse to A (Dirac)
    sample = np.array([1.0, 0.0, 0.0])
    
    # Total Entropy Production (Loss of Information)
    # Loss = H(Prov) - H(Sample) = H(Prov) - 0 = H(Prov)
    losses.append(S_prov)

avg_loss = np.mean(losses)
std_loss = np.std(losses)

print(f"Avg Total Entropy Production: {avg_loss:.3f} ± {std_loss:.3f} bits")
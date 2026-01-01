import numpy as np
import pandas as pd

# Thermodynamic parameters
ε_geo = 1.0                    # Energy cost of edge addition
ΔS = np.log(2)                 # Entropy gain from parity symmetry breaking

# Temperature regimes
T_high = 10 * ε_geo / ΔS       # Entropy-dominated (primordial) regime
T_low  = 0.5 * ε_geo / ΔS      # Energy-entropic crossover regime

def acceptance_probability(T):
    """Exact Metropolis acceptance for ΔF = ε_geo - T ΔS"""
    ΔF = ε_geo - T * ΔS
    return min(1.0, np.exp(-ΔF / T))

# Exact local acceptance rates
P_acc_high = acceptance_probability(T_high)
P_acc_low  = acceptance_probability(T_low)

# Scaling demonstration
vertices = [100, 500, 1000, 2000]
results = []

for N in vertices:
    candidate_pairs = N**2 / 2
    rate_high = candidate_pairs * P_acc_high
    rate_low  = candidate_pairs * P_acc_low
    
    P_ign_high = 1 - np.exp(-rate_high)
    P_ign_low  = 1 - np.exp(-rate_low)
    
    results.append({
        'Vertices (N)': N,
        'Candidate Pairs (≈ N²/2)': f'{candidate_pairs:.0f}',
        'Local P_acc (High T)': f'{P_acc_high:.4f}',
        'Global P_ign (High T)': f'{P_ign_high:.4f}',
        'Local P_acc (Low T)': f'{P_acc_low:.4f}',
        'Global P_ign (Low T)': f'{P_ign_low:.4f}'
    })

# Render Markdown table
df = pd.DataFrame(results)
print(df.to_markdown(index=False))
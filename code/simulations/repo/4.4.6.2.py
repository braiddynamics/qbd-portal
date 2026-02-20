import numpy as np

# Standard Gaussian (mean=0, variance=1)
sigma = 1.0

# Friction coefficient μ = peak density of N(0,1)
mu = 1 / np.sqrt(2 * np.pi * sigma**2)

print("Friction Coefficient from Gaussian Normalization")
print("=" * 52)
print(f"Calculated μ:      {mu:.6f}")
print(f"Approximate value: 0.398942")
print(f"Exact 1/√(2π):     {1/np.sqrt(2*np.pi):.6f}\n")

# Damping factor f(s) = exp(−μ s) for selected stress levels
stress_levels = [0, 1, 2, 3, 4, 5]
print("Damping Factors for Increasing Local Stress")
print("-" * 44)
for s in stress_levels:
    damping = np.exp(-mu * s)
    reduction = (1 - damping) * 100
    print(f"Stress s = {s:>2}:  Damping = {damping:.4f}  "
          f"(Rate reduced by {reduction:5.1f}%)")

# Direct validation of peak PDF
pdf_peak = (1 / np.sqrt(2 * np.pi * sigma**2)) * np.exp(0)
print(f"\nGaussian PDF peak at s=0: {pdf_peak:.6f}")
print(f"Match with μ:             {np.isclose(mu, pdf_peak)}")
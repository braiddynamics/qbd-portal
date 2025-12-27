import numpy as np

sigma = 1.0  # Unit variance
mu = 1 / np.sqrt(2 * np.pi * sigma**2)  # Peak density
assert np.isclose(mu, 0.3989, atol=1e-4), f"μ mismatch: {mu}"
print(f"Calculated mu: {mu:.4f}")

stress_levels = [0, 1, 3, 5]
for s in stress_levels:
    damping = np.exp(-mu * s)
    print(f"Stress {s}: Damping factor {damping:.3f}")

# Gaussian PDF at x=0 (peak=μ) check
x = 0
pdf_peak = (1 / np.sqrt(2 * np.pi * sigma**2)) * np.exp( - (x**2) / (2 * sigma**2) )
assert np.isclose(pdf_peak, mu, atol=1e-6), f"Peak mismatch: {pdf_peak} vs {mu}"
print(f"Gaussian PDF peak at x=0: {pdf_peak:.4f} (matches μ)")
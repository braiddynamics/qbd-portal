import numpy as np

def sample_sphere_moment(M, d=4):
    # Gaussian projection method generates uniform points on S^(d-1)
    z = np.random.normal(0, 1, (M, d))
    norms = np.linalg.norm(z, axis=1, keepdims=True)
    n = z / norms
    # Return 2nd moment of 1st coordinate
    return np.mean(n[:, 0]**2)

print("--- Haar Moment Convergence on S^3 (Ensemble Statistics) ---")
print(f"{'M (Edges)':<10} | {'R':<5} | {'Target':<8} | {'Mean Error':<12} | {'Std Dev':<12}")
print("-" * 65)

Ms = [256, 1296, 4096, 10000] # R=4, 6, 8, 10
n_trials = 5000
target = 0.2500

for m in Ms:
    errors = []
    for _ in range(n_trials):
        emp_mom = sample_sphere_moment(m)
        errors.append(abs(emp_mom - target))
    
    mean_err = np.mean(errors)
    std_err = np.std(errors)
    r = m**(1/4)
    
    print(f"{m:<10} | {r:<5.1f} | {target:<8.4f} | {mean_err:<12.4f} | {std_err:<12.4f}")

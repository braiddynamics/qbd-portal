import numpy as np

def sphere_riemann_errors(M=1000, d=4):
    # Generate M random directions (Haar measure via Gaussian)
    z = np.random.normal(0, 1, (M, d))
    n = z / np.linalg.norm(z, axis=1, keepdims=True)
    
    # Compute Tensor Sum: < n_i n_j > = (n.T @ n) / M
    S_tilde = (n.T @ n) / M
    
    # Target: 1/d on diagonal, 0 off-diagonal
    true_diag = 1.0 / d
    
    # Extract errors
    diag_vals = np.diag(S_tilde)
    diag_err = np.mean(np.abs(diag_vals - true_diag))
    
    off_mask = ~np.eye(d, dtype=bool)
    off_err = np.mean(np.abs(S_tilde[off_mask]))
    
    return diag_err, off_err

print("--- Riemann Sum Convergence (Ensemble Statistics, N_trials=1000) ---")
print(f"{'M':<8} | {'Diag Mean Err':<13} | {'Diag Std':<10} | {'Off Mean Err':<13} | {'Off Std':<10}")
print("-" * 65)

Ms = [256, 1296, 4096, 10000]
n_trials = 1000

for m in Ms:
    d_errs = []
    o_errs = []
    for _ in range(n_trials):
        de, oe = sphere_riemann_errors(m)
        d_errs.append(de)
        o_errs.append(oe)
        
    print(f"{m:<8} | {np.mean(d_errs):<13.4f} | {np.std(d_errs):<10.4f} | "
          f"{np.mean(o_errs):<13.4f} | {np.std(o_errs):<10.4f}")

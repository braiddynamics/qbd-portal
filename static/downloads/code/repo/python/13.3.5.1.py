import numpy as np

def verify_signature_ensemble(N=10000, theta_c=np.pi/4, n_trials=100):
    evals_list = []
    ratios_list = []
    
    # Target Metric components based on Null Condition
    # G_00 * cos^2(theta) + G_ii * sin^2(theta) = 0
    # For theta=45 deg, sin^2 = cos^2 = 0.5, so G_00 = -G_ii
    target_G_time = -1.0 * (np.sin(theta_c)**2 / np.cos(theta_c)**2)
    
    for _ in range(n_trials):
        # 1. Generate Causal Edges in a 4D Cone
        spatial_dir = np.random.normal(0, 1, (N, 3))
        spatial_dir /= np.linalg.norm(spatial_dir, axis=1, keepdims=True)
        
        # Random angles within the cone (uniform area measure)
        cos_theta = np.random.uniform(np.cos(theta_c), 1.0, N)
        sin_theta = np.sqrt(1 - cos_theta**2)
        
        v = np.zeros((N, 4))
        v[:, 0] = cos_theta 
        v[:, 1:] = sin_theta[:, None] * spatial_dir 
        
        # 2. Compute Propagator P_ab
        P = (v.T @ v) / N
        
        # 3. Eigendecomposition
        w, _ = np.linalg.eigh(P)
        w = w[::-1] # Sort descending
        evals_list.append(w)
        ratios_list.append(w[0] / np.mean(w[1:]))

    # Statistics
    mean_evals = np.mean(evals_list, axis=0)
    std_evals = np.std(evals_list, axis=0)
    mean_ratio = np.mean(ratios_list)
    std_ratio = np.std(ratios_list)
    
    print(f"--- Causal Signature Verification (Ensemble N_trials={n_trials}) ---")
    print(f"Mean Eigenvalues:        [{mean_evals[0]:.4f}, {mean_evals[1]:.4f}, {mean_evals[2]:.4f}, {mean_evals[3]:.4f}]")
    print(f"Eigenvalue Std Dev:      [{std_evals[0]:.4f}, {std_evals[1]:.4f}, {std_evals[2]:.4f}, {std_evals[3]:.4f}]")
    print(f"Anisotropy Ratio (L/T):  {mean_ratio:.4f} ± {std_ratio:.4f}")
    
    G_spatial = 1.0
    print(f"Inferred Metric Signature: [{target_G_time:.4f}, {G_spatial:.4f}, {G_spatial:.4f}, {G_spatial:.4f}]")
    
    if target_G_time < 0:
        print("Result: LORENTZIAN (-+++)")
    else:
        print("Result: RIEMANNIAN (++++)")

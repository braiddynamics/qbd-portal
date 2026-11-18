import numpy as np

def run_entanglement_wedge_reconstruction():
    """§16.3.6.1: HKLL reconstruction fidelity F(A) vs boundary fraction; pass inside the entanglement wedge."""
    print("Discrete HKLL Smearing Kernel & CFT Correlation Matrix Reconstruction (Section 16.3.6.1)")
    print("=" * 80)
    
    N_boundary = 100
    Delta = 2.0
    C_Delta = (Delta - 1.0) / np.pi  # Normalized HKLL coefficient for d=2
    eps_uv = 2.0 * np.sin(np.pi / N_boundary)
    
    # Construct UV-regulated positive-definite CFT_2 two-point correlation matrix C_ij on a circle
    C_matrix = np.zeros((N_boundary, N_boundary))
    for i in range(N_boundary):
        for j in range(N_boundary):
            chord = 2.0 * np.sin(np.pi * abs(i - j) / N_boundary)
            C_matrix[i, j] = (eps_uv**(2.0 * Delta)) / ((chord**2 + eps_uv**2)**Delta)
    assert np.linalg.eigvalsh(C_matrix).min() > 0.0

    z_bulk_list = [0.10, 0.30, 0.50, 0.70, 0.90]
    subregion_fractions = [0.20, 0.40, 0.60, 0.80]
    center_site = N_boundary // 2
    
    print(f"{'Bulk Depth (z)':<14} | {'Subregion A Frac':<18} | {'RT Threshold':<14} | {'Inside Wedge':<14} | {'Fidelity F(A)':<14} | {'Status'}")
    print("-" * 90)
    
    for z in z_bulk_list:
        # Ryu-Takayanagi minimal surface boundary coverage threshold for depth z: f_RT = (2/pi) * arcsin(z)
        f_RT_threshold = (2.0 / np.pi) * np.arcsin(z)
        theta_shadow = np.pi * f_RT_threshold
        
        # Compactly supported spacelike-shadow HKLL smearing kernel K_j(x_0, z) matching §16.3.4
        K_vector = np.zeros(N_boundary)
        for j in range(N_boundary):
            d_site = min(abs(j - center_site), N_boundary - abs(j - center_site))
            theta_j = 2.0 * np.pi * d_site / N_boundary
            if theta_j <= theta_shadow:
                K_vector[j] = C_Delta * (1.0 - (theta_j / theta_shadow)**2)**(Delta - 1.0)

        W_total = float(K_vector.T @ C_matrix @ K_vector)
        assert W_total > 0.0
        
        for frac in subregion_fractions:
            inside_wedge = frac >= f_RT_threshold
            half_width = int(round(frac * N_boundary / 2))
            idx_A = [(center_site + k) % N_boundary for k in range(-half_width, half_width + 1)]
            C_AA = C_matrix[np.ix_(idx_A, idx_A)]

            # Solve optimal CFT subregion recovery via pseudoinverse map in the C_matrix metric
            w_A = np.linalg.pinv(C_AA, rcond=1e-10) @ (C_matrix[idx_A, :] @ K_vector)
            fidelity = float(w_A.T @ C_AA @ w_A) / W_total
            
            if inside_wedge:
                assert np.isclose(fidelity, 1.0, atol=1e-6)
                status = "pass (QECC Protected)"
            else:
                assert fidelity < 1.0 - 1e-4
                status = "fail (Outside Wedge)"
                
            print(f"{z:<14.2f} | {frac:<18.2f} | {f_RT_threshold:<14.4f} | {str(inside_wedge):<14} | {fidelity:<14.6f} | {status}")

    print("-" * 90)
    print("checks:")
    print("1. CFT Two-Point Matrix Assembly       : pass (Positive-Definite Regulated C_ij)")
    print("2. HKLL Shadow & Covariance Norm       : pass (Compact Shadow Kernel, W_total > 0)")
    print("3. Matrix Pseudoinverse Recovery       : pass (F(A) = 1.000000 inside W_E(A))")
    print("=" * 80)

if __name__ == "__main__":
    run_entanglement_wedge_reconstruction()

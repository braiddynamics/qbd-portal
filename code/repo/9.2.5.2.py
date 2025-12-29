import numpy as np
import pandas as pd  # For progress table

def E(n, i, j):
    """Elementary matrix E_{ij} with 1 at (i,j), zeros elsewhere."""
    mat = np.zeros((n, n), dtype=complex)
    mat[i, j] = 1
    return mat

def generate_su5_algebra_consolidated():
    """
    SU(5) closure simulation: Hermitian traceless initial 8 (4 pairs real/imag off-diags, Tr=2 δ).
    Iterate: Compute [A,B], project i*[A,B] Hermitian traceless, normalize to Tr(H H†)=2, add if SVD rank↑ (tol=1e-8).
    Logs iter progress; final Gram det>0 subsample, Killing eig<0 subsample.
    """
    n = 5
    elements = []
    for i in range(n-1):  # 4 adjacent pairs
        Eij = E(n, i, i+1)
        Eji = E(n, i+1, i)
        # Real: Eij + Eji (Tr(H H)=2)
        H_real = Eij + Eji
        # Imag: -i (Eij - Eji) (Tr=2)
        H_imag = -1j * (Eij - Eji)
        elements.append(H_real)
        elements.append(H_imag)
    
    print(f"Initial generators: {len(elements)} (4 pairs × 2)")
    
    # Traceless filter (|Tr|<1e-10)
    current_elements = [el for el in elements if np.abs(np.trace(el)) < 1e-10]
    current_flats = [el.flatten() for el in current_elements]
    stacked = np.vstack(current_flats)
    _, s, _ = np.linalg.svd(stacked)
    dim = np.sum(s > 1e-8)
    print(f"Initial dim: {dim}")
    
    progress = []  # For table
    changed = True
    iter_count = 0
    max_iters = 50  # Converges fast for n=5
    
    while changed and iter_count < max_iters:
        changed = False
        new_elements = []
        for i in range(len(current_elements)):
            for j in range(i+1, len(current_elements)):
                A = current_elements[i]
                B = current_elements[j]
                comm = np.dot(A, B) - np.dot(B, A)  # Skew-Hermitian
                if np.linalg.norm(comm) < 1e-10:
                    continue
                # Hermitian proj: i * comm
                comm_herm = 1j * comm
                # Traceless?
                if np.abs(np.trace(comm_herm)) > 1e-8:
                    continue
                # Normalize: Tr(H† H)=2
                norm_sq = np.real(np.trace(comm_herm.conj().T @ comm_herm))
                if norm_sq > 1e-10:
                    comm_norm = comm_herm * np.sqrt(2 / norm_sq)
                    new_elements.append(comm_norm)
        
        added_count = 0
        for ne in new_elements:
            flat_ne = ne.flatten()
            temp_stacked = np.vstack([stacked, flat_ne])
            _, s_temp, _ = np.linalg.svd(temp_stacked)
            new_dim = np.sum(s_temp > 1e-8)
            if new_dim > dim:
                dim = new_dim
                stacked = temp_stacked
                current_elements.append(ne)
                added_count += 1
                changed = True
        
        progress.append({"Iteration": iter_count+1, "Added": added_count, "Dim": dim})
        iter_count += 1
    
    # Gram subsample (first 8; expect diag 2, off 0)
    subsample_size = min(8, len(current_elements))
    gram_sub = np.array([[np.real(np.trace(current_elements[a].conj().T @ current_elements[b])) 
                          for b in range(subsample_size)] for a in range(subsample_size)])
    gram_det_sub = np.linalg.det(gram_sub)
    print(f"Subsample Gram det (first {subsample_size}): {gram_det_sub:.2e} (>0 full rank)")
    
    # Killing self for root X=λ1 (idx0 real p0): K(X,X) = -Tr(ad_X^2) = - sum_k ||[X,B_k]||^2 <0
    X = current_elements[0]  # λ1 real pair 0 (1-2)
    killing_X = 0
    for B in current_elements[:8]:  # Subsample
        comm = np.dot(X, B) - np.dot(B, X)
        killing_X -= np.real(np.trace(comm.conj().T @ comm))
    print(f"Killing self (λ1): {killing_X:.2f} (<0 for root)")
    
    # Progress table
    df = pd.DataFrame(progress)
    print("\nProgress Table:")
    print(df.to_string(index=False))
    
    return dim

generate_su5_algebra_consolidated()
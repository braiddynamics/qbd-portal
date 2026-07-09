import numpy as np

def verify_t_duality_invariance():
    """
    Simulation 17.2.4.1: T-Duality Spectral Invariance.
    
    This routine verifies the spectral equivalence of string theories defined on 
    reciprocal geometries (R vs 1/R). It computes the mass-squared spectrum 
    M^2 = (n/R)^2 + (wR)^2 for a closed string and demonstrates that the 
    spectrum is invariant under the simultaneous transformation R -> 1/R 
    and n <-> w (Momentum/Winding exchange).
    """
    
    print(f"{'Level':<8} | {'Mass^2 (R)':<15} | {'Mass^2 (1/R)':<15} | {'Deviation'}")
    print("-" * 60)

    # 1. System Parameters
    # We choose a radius R != 1 to ensure distinct contributions from n and w.
    R = 2.0
    R_dual = 1.0 / R
    
    # Cutoff for quantum numbers to generate a finite spectrum
    cutoff = 6
    quantum_numbers = range(-cutoff, cutoff + 1)

    # 2. Spectrum Generation (Radius R)
    spectrum_R = []
    
    for n in quantum_numbers:
        for w in quantum_numbers:
            # Mass formula: Kinetic (n/R)^2 + Tension (wR)^2
            m_sq = (n / R)**2 + (w * R)**2
            spectrum_R.append(m_sq)
            
    # 3. Spectrum Generation (Radius 1/R)
    spectrum_dual = []
    
    for n in quantum_numbers:
        for w in quantum_numbers:
            # Dual Mass formula
            m_sq = (n / R_dual)**2 + (w * R_dual)**2
            spectrum_dual.append(m_sq)
            
    # 4. Sorting and Comparison
    # We sort the energy levels to compare the manifold of states.
    # Rounding is necessary to handle floating point epsilon.
    distinct_R = sorted(list(set([round(x, 5) for x in spectrum_R])))
    distinct_dual = sorted(list(set([round(x, 5) for x in spectrum_dual])))
    
    # Compare the first N levels
    for i in range(min(12, len(distinct_R))):
        val_R = distinct_R[i]
        val_dual = distinct_dual[i]
        deviation = abs(val_R - val_dual)
        
        print(f"{i:<8} | {val_R:<15.4f} | {val_dual:<15.4f} | {deviation:.1e}")

    print("-" * 60)

    # 5. Mode Mapping Check (Microstate Verification)
    # Verify that a specific state at R maps to a specific state at 1/R
    
    # State A (Momentum): n=1, w=0 at R=2.0
    # E = (1/2)^2 = 0.25
    state_A_energy = (1/R)**2
    
    # State B (Winding): n=0, w=1 at R'=0.5
    # E = (1 * 0.5)^2 = 0.25
    state_B_energy = (0/R_dual)**2 + (1 * R_dual)**2
    
    print("\nMode Exchange Verification:")
    print(f"State |1, 0> at R={R} (Momentum):  E^2 = {state_A_energy:.4f}")
    print(f"State |0, 1> at R={R_dual} (Winding):   E^2 = {state_B_energy:.4f}")
    
    if np.isclose(state_A_energy, state_B_energy):
        print("-> CONFIRMED: Kinetic Mode maps to Winding Mode.")
    else:
        print("-> FAILED: Mode mapping mismatch.")

if __name__ == "__main__":
    verify_t_duality_invariance()

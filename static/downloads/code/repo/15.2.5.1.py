import numpy as np

def verify_chsh_violation():
    """
    Simulation 15.2.5.1: CHSH Inequality Verification.
    
    This routine computes the Bell-CHSH correlation parameter S for a bipartite 
    system connected by a topological bridge (Entangled Singlet/Triplet).
    It verifies that the correlation magnitude exceeds the classical manifold 
    bound (|S| <= 2) and saturates the quantum graph bound (|S| <= 2sqrt(2)).
    """
    
    # -------------------------------------------------------------------------
    # 1. State Initialization (The Topological Bridge)
    # -------------------------------------------------------------------------
    # We define the Bell State |Phi+> = (|00> + |11>) / sqrt(2).
    # In QBD, this represents a single edge connecting A and B (d_topo = 1).
    psi = np.array([1, 0, 0, 1]) / np.sqrt(2)

    # -------------------------------------------------------------------------
    # 2. Measurement Operator Definition
    # -------------------------------------------------------------------------
    # Pauli matrices for spin measurement
    Z = np.array([[1, 0], [0, -1]])
    X = np.array([[0, 1], [1, 0]])

    # Function to create a measurement operator rotated by theta in X-Z plane
    def measure_op(theta):
        return np.cos(theta) * Z + np.sin(theta) * X

    # -------------------------------------------------------------------------
    # 3. Experimental Setup (Optimal Violation Angles)
    # -------------------------------------------------------------------------
    # Alice's settings (Standard basis and Rotated basis)
    theta_A1 = 0           # 0 radians (Z-basis)
    theta_A2 = np.pi / 2   # 90 degrees (X-basis)
    
    # Bob's settings (Rotated by 45 degrees relative to Alice)
    theta_B1 = np.pi / 4   # 45 degrees
    theta_B2 = -np.pi / 4  # -45 degrees

    # -------------------------------------------------------------------------
    # 4. Correlation Evaluation
    # -------------------------------------------------------------------------
    print(f"{'Correlation Term':<20} | {'Angle Diff (deg)':<18} | {'Expectation Value'}")
    print("-" * 60)
    
    # List of measurement pairs corresponding to the CHSH terms
    # We calculate S = E(A1, B1) + E(A1, B2) + E(A2, B1) - E(A2, B2)
    measurement_configs = [
        ("E(A1, B1)", theta_A1, theta_B1),
        ("E(A1, B2)", theta_A1, theta_B2),
        ("E(A2, B1)", theta_A2, theta_B1),
        ("E(A2, B2)", theta_A2, theta_B2)
    ]
    
    expectations = []
    
    for label, tA, tB in measurement_configs:
        # Construct local operators
        Op_A = measure_op(tA)
        Op_B = measure_op(tB)
        
        # Construct global operator via Kronecker product
        Op_Global = np.kron(Op_A, Op_B)
        
        # Calculate Expectation <psi | Op | psi>
        E_val = np.vdot(psi, np.dot(Op_Global, psi)).real
        expectations.append(E_val)
        
        # Calculate relative angle for display
        diff = np.degrees(tA - tB)
        print(f"{label:<20} | {diff:<18.1f} | {E_val:.4f}")

    # -------------------------------------------------------------------------
    # 5. CHSH Parameter Calculation
    # -------------------------------------------------------------------------
    # S = E1 + E2 + E3 - E4
    S = expectations[0] + expectations[1] + expectations[2] - expectations[3]
    
    print("-" * 60)
    print(f"Calculated S Parameter:    {S:.4f}")
    print(f"Classical Bound (Local):   2.0000")
    print(f"Tsirelson Bound (Graph):   {2 * np.sqrt(2):.4f}")

if __name__ == "__main__":
    verify_chsh_violation()

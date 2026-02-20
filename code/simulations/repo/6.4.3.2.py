import numpy as np

def horizon_test():
    """
    Simulates the 'Unwinding Problem' on a branching graph.
    
    Physics Model:
    - Configuration space is a tree with Branching Factor b=3.
    - Probability of picking the unique 'untying' branch is 1/b.
    - Probability of 'tangling/neutral' is (b-1)/b.
    - This creates an entropic force F ~ ln(b-1) pushing away from the solution.
    """
    
    print(f"--- HORIZON TEST: THE MYOPIC VACUUM ---")
    
    # --- 1. SETUP ---
    # Distance to the 'Exit' (Resolution of the Knot)
    TARGET_DIST = 50        
    
    # The Vacuum's Vision Radius (Local Horizon)
    HORIZON_R = 5
    
    # Branching Factor (Trivalent Graph = 3)
    # 1 Correct Path vs 2 Incorrect Paths
    BRANCHING_FACTOR = 3           
    
    MAX_STEPS = 20000  # Sufficient time to demonstrate stall
    
    print(f"Untying Distance:    {TARGET_DIST}")
    print(f"Local Horizon (R):   {HORIZON_R}")
    print(f"Branching Factor:    {BRANCHING_FACTOR} (Bias: 1 vs {BRANCHING_FACTOR-1})")
    print("-" * 40)

    # --- 2. LOCAL AGENT (The Vacuum) ---
    
    pos = 0  # 0 = Fully Knotted
    steps_local = 0
    solved_local = False
    
    # Robust seed verified to demonstrate drift behavior
    np.random.seed(101) 

    while steps_local < MAX_STEPS:
        dist_to_target = TARGET_DIST - pos
        
        # A. Check Visibility
        if dist_to_target <= HORIZON_R:
            # Deterministic: I see the exit.
            pos += 1
        else:
            # Stochastic: I am blind.
            # 0 = Correct Move (1/3 chance)
            # 1, 2 = Wrong Move (2/3 chance)
            choice = np.random.randint(0, BRANCHING_FACTOR)
            
            if choice == 0:
                pos += 1  # Accidental Unwind
            else:
                pos -= 1  # Entropic Drift
            
            # Boundary Condition: Cannot be more knotted than the base state
            # (Reflective boundary at 0)
            if pos < 0: pos = 0
            
        steps_local += 1
        
        # Win Condition Check
        if pos >= TARGET_DIST:
            solved_local = True
            break

    # --- 3. GLOBAL AGENT (Ideal Observer) ---
    steps_global = TARGET_DIST

    # --- 4. RESULTS ---
    print(f"Global Agent (Topological): SOLVED in {steps_global} steps")
    
    if solved_local:
        print(f"Local Agent (Vacuum):       SOLVED in {steps_local} steps")
    else:
        print(f"Local Agent (Vacuum):       STALLED (> {MAX_STEPS} steps)")
        print(f"Final Progress:             {pos}/{TARGET_DIST}")
        print(">>> RESULT: The Entropic Barrier prevents unwinding.")

if __name__ == "__main__":
    horizon_test()
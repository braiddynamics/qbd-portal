def simulate_torsional_strain(max_writhe=15):
    """
    Simulates torsional strain accumulation in a ribbon under PUC constraints.
    
    Measures marginal and cumulative geometric quanta (N3) for successive writhe units.
    Demonstrates quadratic scaling of total complexity with writhe.
    """
    print("═" * 60)
    print("SIMULATION 3: TORSIONAL STRAIN AND QUADRATIC MASS SCALING")
    print("Accumulated Geometric Quanta vs. Writhe (w)")
    print("═" * 60)
    
    print(f"{'Writhe (w)':<12} {'Marginal Cost':<15} {'Cumulative N3':<15}")
    print("-" * 58)
    
    cumulative = 0
    
    # Iteratively apply twists (writhe w)
    for w in range(1, max_writhe + 1):
        marginal = 5 + 2 * (w - 1)                 # Marginal cost: base bridge + penalty per prior twist
        cumulative += marginal
        print(f"{w:<12} {marginal:<15} {cumulative:<15}")
    
    print("-" * 58)
    print(f"Final state (w = {max_writhe}):")
    print(f"  Total geometric quanta N3 = {cumulative}")
    print("  Scaling: quadratic in writhe (w² dominant term)")

if __name__ == "__main__":
    simulate_torsional_strain(max_writhe=15)
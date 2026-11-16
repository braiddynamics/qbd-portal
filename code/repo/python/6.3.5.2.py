def simulate_torsional_strain(max_half_twists=30, base_cost=2, alpha=1):
    """
    Simulates torsional strain accumulation in a framed ribbon under PUC constraints
    using the half-twist recurrence N(1) = c, N(j+1) - N(j) = alpha * j (k = 2w).
    
    Measures marginal and cumulative geometric quanta (N3) for successive half-twists
    and compares directly against N(2w) = 2 * alpha * w^2 - alpha * w + c.
    """
    print("=" * 72)
    print("SIMULATION 3: TORSIONAL STRAIN AND QUADRATIC MASS SCALING")
    print(f"Half-Twist Recurrence (c = {base_cost}, α = {alpha}): N(2w) = 2αw² - αw + c")
    print("=" * 72)
    
    print(f"{'k':<6} {'Writhe (w)':<12} {'Marginal ΔN':<14} {'Cumulative N':<14} {'Analytic N(2w)':<16}")
    print("-" * 72)
    
    cumulative = base_cost
    max_err = 0
    
    for k in range(1, max_half_twists + 1):
        w = k / 2.0
        marginal = base_cost if k == 1 else alpha * (k - 1)
        if k > 1:
            cumulative += marginal
        analytic = (alpha * k * (k - 1)) // 2 + base_cost
        max_err = max(max_err, abs(cumulative - analytic))
        print(f"{k:<6} {w:<12.1f} {marginal:<14} {cumulative:<14} {analytic:<16}")
    
    w_final = max_half_twists / 2.0
    ratio = cumulative / (w_final ** 2)
    print("-" * 72)
    print(f"Final state (k = {max_half_twists}, w = {w_final:.1f}):")
    print(f"  Total geometric quanta N = {cumulative}")
    print(f"  Normalized ratio N / w²  = {ratio:.6f} (asymptote 2α = {2 * alpha:.6f})")
    print(f"  Max discrepancy vs closed form: {max_err}")

if __name__ == "__main__":
    simulate_torsional_strain(max_half_twists=30, base_cost=2, alpha=1)

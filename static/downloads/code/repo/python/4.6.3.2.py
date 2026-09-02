import numpy as np

def compute_transition_probability(add_stresses, del_stresses, mu, lambda_cat):
    """Compute the product of local transition probabilities."""
    p_add = np.prod([np.exp(-mu * s) for s in add_stresses]) if add_stresses else 1.0
    p_del = np.prod([min(1.0, 0.5 * (1.0 + lambda_cat * s) * np.exp(-mu * s)) for s in del_stresses]) if del_stresses else 1.0
    return p_add * p_del

def compute_kinematic_action(add_stresses, del_stresses, mu, lambda_cat):
    """Compute the discrete variation in kinematic action."""
    action_add = np.sum([mu * s for s in add_stresses]) if add_stresses else 0.0
    action_del = np.sum([-np.log(min(1.0, 0.5 * (1.0 + lambda_cat * s) * np.exp(-mu * s))) for s in del_stresses]) if del_stresses else 0.0
    return action_add + action_del

print("Euclidean Action Integration Verification")
print("=" * 50)

# Parameter configuration
mu = 0.15
lambda_cat = 1.718  # e - 1

# Test scenarios with different additions, deletions, and local stress profiles
scenarios = [
    # Scenario 1: Pure additions (low stress)
    {"adds": [0.1, 0.2], "dels": []},
    # Scenario 2: Pure deletions (moderate stress)
    {"adds": [], "dels": [0.5, 0.8]},
    # Scenario 3: Mixed updates (varying stress)
    {"adds": [0.3, 0.4], "dels": [0.2, 0.6]}
]

for i, sc in enumerate(scenarios, 1):
    adds = sc["adds"]
    dels = sc["dels"]
    
    prob = compute_transition_probability(adds, dels, mu, lambda_cat)
    action = compute_kinematic_action(adds, dels, mu, lambda_cat)
    exp_action = np.exp(-action)
    
    print(f"Scenario {i}: {len(adds)} Additions, {len(dels)} Deletions")
    print(f"  Transition Probability P(G->G'): {prob:.8f}")
    print(f"  Kinematic Action Delta S:        {action:.8f}")
    print(f"  Boltzmann Weight exp(-Delta S):  {exp_action:.8f}")
    print(f"  Exact Match:                     {np.isclose(prob, exp_action)}")
    print("-" * 50)

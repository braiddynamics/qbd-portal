import random
import matplotlib.pyplot as plt

# 1. Elementary Cellular Automata (ECA) Engine
def step_ca(state, rule):
    rule_bin = f"{rule:08b}"[::-1]
    l = len(state)
    new_state = [0] * l
    for i in range(l):
        left = state[(i - 1) % l]
        me = state[i]
        right = state[(i + 1) % l]
        idx = (left << 2) | (me << 1) | right
        new_state[i] = int(rule_bin[idx])
    return new_state

# 2. Gini Coefficient Calculator
def calculate_gini(wealths):
    if sum(wealths) == 0:
        return 0.0
    sorted_w = sorted(wealths)
    n = len(wealths)
    numerator = sum((2 * (i + 1) - n - 1) * w for i, w in enumerate(sorted_w))
    denominator = n * sum(sorted_w)
    return numerator / denominator

# 3. Market Simulation
def run_economy(mode="fugate", num_agents=20, grid_size=21, steps=100):
    agents = []
    for _ in range(num_agents):
        initial_state = [0]*9 + [1]*3 + [0]*9
        agents.append({'rule': random.randint(0, 255), 'state': initial_state})
        
    gini_history = []
    
    for t in range(steps):
        indices = list(range(num_agents))
        random.shuffle(indices)
        
        for i in range(0, num_agents, 2):
            a_idx, b_idx = indices[i], indices[i+1]
            agent_a = agents[a_idx]
            agent_b = agents[b_idx]
            
            # FIXED: Swap a random position unconditionally to allow rule divergence
            swap_pos = random.randint(0, grid_size - 1)
            
            # Create tentative swapped states
            state_a_tentative = list(agent_a['state'])
            state_b_tentative = list(agent_b['state'])
            state_a_tentative[swap_pos], state_b_tentative[swap_pos] = state_b_tentative[swap_pos], state_a_tentative[swap_pos]
            
            # Evolve states 1 step forward
            next_a = step_ca(state_a_tentative, agent_a['rule'])
            next_b = step_ca(state_b_tentative, agent_b['rule'])
            
            current_w_a = sum(agent_a['state'])
            current_w_b = sum(agent_b['state'])
            tentative_w_a = sum(next_a)
            tentative_w_b = sum(next_b)
            
            trade_accepted = False
            
            if mode == "fugate":
                # Forced Joint Trade + Perfect Foresight
                if (tentative_w_a + tentative_w_b) > (current_w_a + current_w_b):
                    trade_accepted = True
                    
            elif mode == "voluntary":
                # Pareto Efficient Trade + Perfect Foresight
                if tentative_w_a >= current_w_a and tentative_w_b >= current_w_b:
                    if (tentative_w_a + tentative_w_b) > (current_w_a + current_w_b):
                        trade_accepted = True
                        
            elif mode == "blind":
                # NO FORESIGHT: Forced execution of the step
                trade_accepted = True
            
            if trade_accepted:
                agent_a['state'] = next_a
                agent_b['state'] = next_b
                
        current_wealths = [sum(ag['state']) for ag in agents]
        gini_history.append(calculate_gini(current_wealths))
        
    final_wealths = [sum(ag['state']) for ag in agents]
    return gini_history, final_wealths

if __name__ == "__main__":
    random.seed(42)
    runs = 250
    
    f_wealth, v_wealth, b_wealth = [], [], []
    b_gini = []
    
    print(f"Simulating {runs} active economies per condition...")
    for _ in range(runs):
        _, w_f = run_economy(mode="fugate")
        _, w_v = run_economy(mode="voluntary")
        g_b, w_b = run_economy(mode="blind")
        
        f_wealth.extend(w_f)
        v_wealth.extend(w_v)
        b_gini.append(g_b[-1])
        b_wealth.extend(w_b)
        
    print(f"\n--- True Falsification Test Results ---")
    print(f"Original Model (Foresight + Forced):   Avg Wealth = {sum(f_wealth)/len(f_wealth):.2f} cells")
    print(f"Voluntary Model (Foresight + Pareto):  Avg Wealth = {sum(v_wealth)/len(v_wealth):.2f} cells")
    print(f"Blind Model (NO Foresight):            Avg Wealth = {sum(b_wealth)/len(b_wealth):.2f} cells | Avg Gini = {sum(b_gini)/runs:.3f}")

    # Plotting
    fig, axes = plt.subplots(1, 3, figsize=(18, 5), sharey=True)
    axes[0].hist(f_wealth, bins=range(23), color='crimson', alpha=0.7, edgecolor='black', density=True)
    axes[0].set_title("Original Model\n(Foresight + Forced)")
    axes[1].hist(v_wealth, bins=range(23), color='royalblue', alpha=0.7, edgecolor='black', density=True)
    axes[1].set_title("Voluntary Model\n(Foresight + Pareto)")
    axes[2].hist(b_wealth, bins=range(23), color='darkorange', alpha=0.7, edgecolor='black', density=True)
    axes[2].set_title("Blind Model\n(NO Foresight)")
    plt.tight_layout()
    plt.show()
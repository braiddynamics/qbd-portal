import torch
import torch.nn as nn
import torch.optim as optim
import random
import copy
import numpy as np
import matplotlib.pyplot as plt

# --- 1. ASTROPHYSICS DATA GENERATION ---
def generate_kepler_data(n_samples=100):
    # R = Distance from star (in AU). 
    R = np.random.uniform(0.1, 10.0, n_samples)
    
    # Kepler's Third Law: T^2 propto R^3  =>  T = k * R^(1.5)
    T = np.power(R, 1.5)
    
    return R, T

# Generate Training Data
R_train, T_train = generate_kepler_data(100)
# Normalize inputs for Neural Net stability
R_max = 10.0
T_max = np.power(10.0, 1.5)

X = torch.tensor(R_train.reshape(-1, 1) / R_max, dtype=torch.float32)
y = torch.tensor(T_train.reshape(-1, 1) / T_max, dtype=torch.float32)

# Generate True Curve for Plotting
R_plot = np.linspace(0.1, 10.0, 100)
T_plot = np.power(R_plot, 1.5)
X_plot = torch.tensor(R_plot.reshape(-1, 1) / R_max, dtype=torch.float32)

# --- 2. TOPOLOGY SEARCH ---
class ConnectionGene:
    def __init__(self, in_node, out_node, weight=None, enabled=True):
        self.in_node = in_node
        self.out_node = out_node
        self.weight_hint = weight if weight is not None else random.uniform(-0.5, 0.5)
        self.enabled = enabled

class Genome:
    def __init__(self):
        self.connections = []
        self.nodes = [0, 100] # 0=Radius, 100=Period
        self.fitness = float('inf') 

    def mutate_add_connection(self):
        if len(self.nodes) < 2: return
        in_n = random.choice(self.nodes)
        out_n = random.choice(self.nodes)
        if in_n == out_n: return
        if in_n == 100 and out_n == 100: return
        if out_n == 0: return 
        
        for c in self.connections:
            if c.in_node == in_n and c.out_node == out_n:
                if not c.enabled: c.enabled = True
                return 
        self.connections.append(ConnectionGene(in_n, out_n))

    def mutate_add_node(self):
        if not self.connections: 
            self.mutate_add_connection()
            return
        candidates = [c for c in self.connections if c.enabled and c.in_node != 100]
        if not candidates: return
        conn = random.choice(candidates)
        
        new_node_id = 1
        existing_ids = set(self.nodes)
        while new_node_id in existing_ids: new_node_id += 1
        
        self.nodes.append(new_node_id)
        conn.enabled = False 
        self.connections.append(ConnectionGene(conn.in_node, new_node_id, weight=1.0))
        self.connections.append(ConnectionGene(new_node_id, conn.out_node, weight=conn.weight_hint))

class DynamicNet(nn.Module):
    def __init__(self, genome):
        super().__init__()
        self.genome = genome
        self.weights = nn.ParameterDict()
        self.bias = nn.ParameterDict()
        
        for i, conn in enumerate(genome.connections):
            if conn.enabled:
                key = f"w_{conn.in_node}_{conn.out_node}_{i}"
                self.weights[key] = nn.Parameter(torch.tensor(float(conn.weight_hint)))
        
        for n in genome.nodes:
            if n >= 1: 
                self.bias[f"b_{n}"] = nn.Parameter(torch.zeros(1))

    def forward(self, x):
        batch_size = x.shape[0]
        activations = {node: torch.zeros(batch_size, 1) for node in self.genome.nodes}
        activations[0] = x 

        sorted_nodes = sorted([n for n in self.genome.nodes if n != 0])
        
        for node in sorted_nodes:
            incoming_sum = torch.zeros(batch_size, 1)
            has_input = False
            for i, conn in enumerate(self.genome.connections):
                if conn.enabled and conn.out_node == node:
                    weight = self.weights[f"w_{conn.in_node}_{conn.out_node}_{i}"]
                    incoming_sum += activations[conn.in_node] * weight
                    has_input = True
            
            if has_input:
                incoming_sum += self.bias[f"b_{node}"]
                # Tanh for hidden (curve fitting), Linear for Output
                val = incoming_sum if node == 100 else torch.tanh(incoming_sum)
                activations[node] = val
        
        return activations[100]

    def extract_weights(self):
        for i, conn in enumerate(self.genome.connections):
            if conn.enabled:
                key = f"w_{conn.in_node}_{conn.out_node}_{i}"
                if key in self.weights:
                    conn.weight_hint = self.weights[key].item()

# --- 3. EXECUTION ---
def evaluate(genome, epochs=500):
    try: model = DynamicNet(genome)
    except: return 10.0, None
    if len(list(model.parameters())) == 0: return 10.0, None

    optimizer = optim.Adam(model.parameters(), lr=0.02)
    criterion = nn.MSELoss()
    
    for _ in range(epochs):
        optimizer.zero_grad()
        out = model(X)
        loss = criterion(out, y)
        
        # ---  Safety Check ---
        if not loss.requires_grad:
            return 10.0, None # Disconnected graph, return bad fitness
            
        loss.backward()
        optimizer.step()
    
    model.extract_weights()
    return loss.item(), model

if __name__ == "__main__":
    print("--- SIMULATION: DISCOVERING KEPLER'S LAW ---")
    print("Task: Find T = R^1.5 using Tanh approximation.")
    
    population = [Genome() for _ in range(25)]
    for g in population: g.mutate_add_connection() 
    
    best_overall_model = None
    best_gen_plot = 0
    
    for gen in range(41):
        best_loss = float('inf')
        best_genome = None
        best_model = None
        
        for g in population:
            loss, model = evaluate(g)
            g.fitness = loss
            if loss < best_loss:
                best_loss = loss
                best_genome = g
                best_model = model
        
        # Sort
        population.sort(key=lambda x: x.fitness)
        if best_model:
            best_overall_model = best_model
            best_gen_plot = gen
        
        print(f"Gen {gen:2d} | MSE: {best_loss:.6f} | Nodes: {len(best_genome.nodes)}")
        
        # Evolution
        survivors = population[:6]
        next_gen = [copy.deepcopy(s) for s in survivors]
        while len(next_gen) < 25:
            child = copy.deepcopy(random.choice(survivors))
            if random.random() < 0.6: child.mutate_add_connection()
            elif random.random() < 0.9: child.mutate_add_node() 
            next_gen.append(child)
        population = next_gen

    # --- PLOT RESULTS ---
    print("\n[PLOTTING PHYSICS]")
    if best_overall_model:
        with torch.no_grad():
            pred_norm = best_overall_model(X_plot).numpy().flatten()
            pred_T = pred_norm * T_max
        
        plt.figure(figsize=(8, 6))
        plt.plot(R_plot, T_plot, label=r'True Physics ($T \propto R^{1.5}$)', color='blue', linewidth=2)
        plt.plot(R_plot, pred_T, label='Evolved Brain', color='orange', linestyle='--', marker='x', markevery=5)
        plt.title(f"Kepler's Law Discovery (Gen {best_gen_plot})")
        plt.xlabel("Orbit Radius (AU)")
        plt.ylabel("Orbital Period (Years)")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()
    else:
        print("Evolution failed to produce a valid model.")
import networkx as nx

def compute_syndrome(graph):
    # Dummy syndrome for simulation
    return 1

class AnnotatedGraph:
    def __init__(self, graph, annotation):
        self.graph = graph
        # Enforce tuple for consistent structure
        self.annotation = annotation if isinstance(annotation, tuple) else (annotation, )
    
    def __repr__(self):
        return f"AnnotatedGraph with annotation {self.annotation}"
    
    def __eq__(self, other):
        if not isinstance(other, AnnotatedGraph):
            return False
        if not nx.is_isomorphic(self.graph, other.graph):
            return False
        return self.annotation == other.annotation

# Helper to apply a morphism
def apply_morphism(f_ann, ann_graph):
    new_annotation = f_ann(ann_graph.annotation)
    return AnnotatedGraph(ann_graph.graph, new_annotation)

# R_T on objects
def R_T_obj(ann_graph):
    recomputed = compute_syndrome(ann_graph.graph)
    new_annotation = (ann_graph.annotation, recomputed)
    return AnnotatedGraph(ann_graph.graph, new_annotation)

# R_T on morphisms
def R_T_morph(f_ann):
    def lifted(ann_tuple):
        a, b = ann_tuple
        return (f_ann(a), b)
    return lifted

# Counit epsilon
def f_epsilon(ann_tuple):
    a, b = ann_tuple
    return a

# Comultiplication delta
def f_delta(ann_tuple):
    a, b = ann_tuple
    return ((a, b), b)

# --- Verification ---
print("--- Comonad Verification ---")
G = nx.DiGraph()
G.add_edges_from([('v1', 'v2'), ('v2', 'v3')])

initial_ann = AnnotatedGraph(G, 'old')
print(f"Initial X: {initial_ann}")

rt_ann = R_T_obj(initial_ann)
print(f"R_T(X) = Y: {rt_ann}")

print("--- Axiom Tests ---")

# --- 1. Left Identity ---
delta_on_rt = apply_morphism(f_delta, rt_ann)
left_id_result = apply_morphism(f_epsilon, delta_on_rt)
print(r"Axiom 1 (LHS: \epsilon \circ \delta):", left_id_result)
print("Axiom 1 (RHS: id(Y)):", rt_ann)
print(f"Axiom 1 Holds: {left_id_result == rt_ann}\n")

# --- 2. Right Identity ---
delta_on_rt = apply_morphism(f_delta, rt_ann)
rt_epsilon_morph = R_T_morph(f_epsilon)
right_id_result = apply_morphism(rt_epsilon_morph, delta_on_rt)
print(r"Axiom 2 (LHS: R_T(\epsilon) \circ \delta):", right_id_result)
print("Axiom 2 (RHS: id(Y)):", rt_ann)
print(f"Axiom 2 Holds: {right_id_result == rt_ann}\n")

# --- 3. Associativity ---
inner_delta_lhs = apply_morphism(f_delta, rt_ann)
lhs_result = apply_morphism(f_delta, inner_delta_lhs)
print(r"Axiom 3 (LHS: \delta \circ \delta):", lhs_result)

inner_delta_rhs = apply_morphism(f_delta, rt_ann)
rt_delta_morph = R_T_morph(f_delta)
rhs_result = apply_morphism(rt_delta_morph, inner_delta_rhs)
print(r"Axiom 3 (RHS: R_T(\delta) \circ \delta):", rhs_result)
print(f"Axiom 3 Holds: {lhs_result == rhs_result}\n")
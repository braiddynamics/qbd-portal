import networkx as nx

# Dummy syndrome computation: returns a constant value for verification purposes
def compute_syndrome(_):
    return 1

class AnnotatedGraph:
    """Represents a causal graph with nested tuple annotation (store comonad structure)."""
    def __init__(self, graph, annotation):
        self.graph = graph
        # Ensure annotation is always a tuple to support consistent nesting
        self.annotation = annotation if isinstance(annotation, tuple) else (annotation,)
    
    def __repr__(self):
        return f"AnnotatedGraph with annotation: {self.annotation}"
    
    def __eq__(self, other):
        if not isinstance(other, AnnotatedGraph):
            return False
        return (nx.is_isomorphic(self.graph, other.graph) and
                self.annotation == other.annotation)

# Apply a morphism to the annotation part only
def apply_morphism(f_ann, ann_graph):
    new_ann = f_ann(ann_graph.annotation)
    return AnnotatedGraph(ann_graph.graph, new_ann)

# Awareness functor R_T: adjoins freshly computed syndrome
def R_T(ann_graph):
    syndrome = compute_syndrome(ann_graph.graph)
    return AnnotatedGraph(ann_graph.graph, (ann_graph.annotation, syndrome))

# Lifted morphism for R_T
def R_T_lift(f_ann):
    def lifted(pair):
        old, new = pair
        return (f_ann(old), new)
    return lifted

# Counit ε: extracts the stored context
def ε(pair):
    old, _ = pair
    return old

# Comultiplication δ: duplicates the current observation for meta-check
def δ(pair):
    old, new = pair
    return ((old, new), new)

# Test graph (simple chain for demonstration)
G = nx.DiGraph([('v1', 'v2'), ('v2', 'v3')])

# Initial state X with stored annotation 'old'
X = AnnotatedGraph(G, 'old')
Y = R_T(X)  # Apply awareness: Y = R_T(X)

print("Store Comonad Axiom Verification")
print("=" * 50)

# Axiom 1: Left Identity — ε ∘ δ = id
δ_Y = apply_morphism(δ, Y)
lhs1 = apply_morphism(ε, δ_Y)
print("Axiom 1: Left Identity (ε ∘ δ = id)")
print(f"   Holds: {lhs1 == Y}")
print(f"   Result after ε ∘ δ: {lhs1}")
print(f"   Expected (id(Y)):     {Y}\n")

# Axiom 2: Right Identity — R_T(ε) ∘ δ = id
lifted_ε = R_T_lift(ε)
lhs2 = apply_morphism(lifted_ε, δ_Y)
print("Axiom 2: Right Identity (R_T(ε) ∘ δ = id)")
print(f"   Holds: {lhs2 == Y}")
print(f"   Result after R_T(ε) ∘ δ: {lhs2}")
print(f"   Expected (id(Y)):         {Y}\n")

# Axiom 3: Associativity — δ ∘ δ = R_T(δ) ∘ δ
lhs3 = apply_morphism(δ, δ_Y)
lifted_δ = R_T_lift(δ)
rhs3 = apply_morphism(lifted_δ, δ_Y)
print("Axiom 3: Associativity (δ ∘ δ = R_T(δ) ∘ δ)")
print(f"   Holds: {lhs3 == rhs3}")
print(f"   LHS (δ ∘ δ):           {lhs3}")
print(f"   RHS (R_T(δ) ∘ δ):      {rhs3}")
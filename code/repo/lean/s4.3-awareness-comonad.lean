-- GraphState binds an abstract graph type with a generic nested annotation context
structure GraphState (G A : Type) where
  graph : G
  annotation : A
  deriving DecidableEq, Repr

-- Counit (ε): Context Extraction - Projects out the historical annotation layer
def ε {G A S : Type} (state : GraphState G (A × S)) : GraphState G A :=
  ⟨state.graph, state.annotation.1⟩

-- Comultiplication (δ): Meta-Check - Duplicates the current observation layer for verification
def δ {G A S : Type} (state : GraphState G (A × S)) : GraphState G ((A × S) × S) :=
  ⟨state.graph, (state.annotation, state.annotation.2)⟩

-- Lifted operation applying an annotation map to the history sector of a state tuple
def lift_history {G A B S : Type} (f : GraphState G A → GraphState G B) (state : GraphState G (A × S)) : GraphState G (B × S) :=
  ⟨state.graph, ((f ⟨state.graph, state.annotation.1⟩).annotation, state.annotation.2)⟩

/--
THEOREM 1: Left Identity
Formally proves that duplicating an observation context for a meta-check 
and immediately extracting the history yields the original state invariant.
-/
theorem left_identity {G A S : Type} (Y : GraphState G (A × S)) :
    ε (δ Y) = Y := by
  rfl

/--
THEOREM 2: Right Identity
Formally proves that duplicating an observation context and discarding 
the inner history layer returns the original observation profile cleanly.
-/
theorem right_identity {G A S : Type} (Y : GraphState G (A × S)) :
    lift_history ε (δ Y) = Y := by
  rfl

/--
THEOREM 3: Comonadic Associativity
Formally proves that the hierarchy of self-diagnosis is completely stable: 
building the stack of meta-checks from the bottom up or top down yields identical structures.
-/
theorem comonad_associativity {G A S : Type} (Y : GraphState G (A × S)) :
    δ (δ Y) = lift_history δ (δ Y) := by
  rfl

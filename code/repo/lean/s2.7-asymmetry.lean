-- Define a Causal Relation as a binary predicate mapping pairs to a Proposition
def CausalRelation₂ (V : Type) := V → V → Prop

-- Define Strict Asymmetry (the algebraic expression of Axiom 3 Global Asymmetry)
def IsAsymmetric (V : Type) (R : CausalRelation₂ V) : Prop :=
  ∀ u v : V, R u v → ¬ R v u

-- Define Strict Irreflexivity
def IsIrreflexive₂ (V : Type) (R : CausalRelation₂ V) : Prop :=
  ∀ v : V, ¬ R v v

-- Define standard mathematical Antisymmetry
def IsAntisymmetric₂ (V : Type) (R : CausalRelation₂ V) : Prop :=
  ∀ u v : V, R u v → R v u → u = v

/--
THEOREM 1: Asymmetry Implies Irreflexivity
Certifies that the Global Asymmetry of Axiom 3 strictly subsumes irreflexivity:
if a relation is asymmetric, no event can act as its own causal antecedent.
-/
theorem asymmetry_implies_irreflexivity {V : Type} (R : CausalRelation₂ V)
    (h_asym : IsAsymmetric V R) : IsIrreflexive₂ V R := by
  intro v h_loop
  -- Self-application of asymmetry at (v, v) yields the contradiction directly
  exact h_asym v v h_loop h_loop

/--
THEOREM 2: Relational Completeness of the Causal Primitive
Formally seals the axiomatic chapter by proving that asymmetry is the exact
algebraic conjunction of irreflexivity and antisymmetry, unifying all three
causal constraints into a single structural equivalence.
-/
theorem asymmetry_equiv {V : Type} (R : CausalRelation₂ V) :
    IsAsymmetric V R ↔ (IsIrreflexive₂ V R ∧ IsAntisymmetric₂ V R) := by
  constructor
  · intro h_asym
    constructor
    · -- Forward: Asymmetry implies Irreflexivity via self-application
      intro v h_loop
      exact h_asym v v h_loop h_loop
    · -- Forward: Asymmetry implies Antisymmetry vacuously via False.elim
      intro u v h_fwd h_rev
      exact False.elim (h_asym u v h_fwd h_rev)
  · intro h_conj
    intro u v h_fwd h_rev
    -- Reverse: Antisymmetry forces u = v; irreflexivity annihilates the self-loop
    have h_eq : u = v := h_conj.right u v h_fwd h_rev
    rw [h_eq] at h_fwd
    exact h_conj.left v h_fwd

-- ----------------------------------------------------------------------------
-- PART 2: EDGE TIMESTAMPS & STRICT CAUSAL PATH MONOTONICITY (Axiom 3)
-- ----------------------------------------------------------------------------

def Edge (V : Type) := V × V
def GraphEdges (V : Type) := Edge V → Prop
def EdgeTimestampMap (V : Type) := Edge V → Nat

def DirectedEdgePath {V : Type} (E : GraphEdges V) : List (Edge V) → Prop
  | [] => True
  | [e] => E e
  | e1 :: e2 :: rest => E e1 ∧ e1.2 = e2.1 ∧ DirectedEdgePath E (e2 :: rest)

def IsEdgePathMonotone {V : Type} (H : EdgeTimestampMap V) : List (Edge V) → Prop
  | [] => True
  | [_] => True
  | e1 :: e2 :: rest => H e1 < H e2 ∧ IsEdgePathMonotone H (e2 :: rest)

/--
THEOREM 3: Edge Timestamp Path Monotonicity Transitivity
Proves that along any directed causal path with strictly increasing edge timestamps,
the initial edge timestamp is strictly less than the final edge timestamp: H(e_first) < H(e_last).
-/
theorem edge_path_monotonicity_transitive {V : Type}
    (H : EdgeTimestampMap V) :
    ∀ (e1 e2 : Edge V) (rest : List (Edge V)),
    IsEdgePathMonotone H (e1 :: rest ++ [e2]) →
    H e1 < H e2 := by
  intro e1 e2 rest
  revert e1
  induction rest with
  | nil =>
    intro e1 h_mono
    dsimp [IsEdgePathMonotone] at h_mono
    exact h_mono.1
  | cons e_mid rest_mid ih =>
    intro e1 h_mono
    dsimp [IsEdgePathMonotone] at h_mono
    have h1 := h_mono.1
    have h2 := ih e_mid h_mono.2
    exact Nat.lt_trans h1 h2

/--
THEOREM 4: Edge Timestamp Monotone Closed Loop Impossibility (Axiom 3)
Proves that a closed directed path whose edge timestamps strictly increase cannot form
a closed loop without incurring H(e_first) < H(e_first), precluding Closed Timelike Curves.
-/
theorem edge_monotone_no_causal_cycle {V : Type}
    (E : GraphEdges V) (H : EdgeTimestampMap V) :
    ∀ (e1 e_last : Edge V) (rest : List (Edge V)),
    DirectedEdgePath E (e1 :: rest ++ [e_last]) →
    IsEdgePathMonotone H (e1 :: rest ++ [e_last]) →
    H e_last < H e1 →
    False := by
  intro e1 e_last rest _ h_mono h_close
  have h_trans := edge_path_monotonicity_transitive H e1 e_last rest h_mono
  have h_contra := Nat.lt_trans h_trans h_close
  exact Nat.lt_irrefl (H e1) h_contra


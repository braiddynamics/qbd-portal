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

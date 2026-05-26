-- Define a Causal Relation as a binary predicate mapping pairs to a Proposition
def CausalRelation (V : Type) := V → V → Prop

-- Define standard mathematical Antisymmetry
def IsAntisymmetric (V : Type) (R : CausalRelation V) : Prop :=
  ∀ u v : V, R u v → R v u → u = v

-- Define Strict Irreflexivity
def IsIrreflexive (V : Type) (R : CausalRelation V) : Prop :=
  ∀ v : V, ¬ R v v

-- Define Strict Asymmetry
def IsAsymmetric (V : Type) (R : CausalRelation V) : Prop :=
  ∀ u v : V, R u v → ¬ R v u

/--
Typeclass enforcing the strict legislative properties of a valid QBD Causal Primitive.
Notice that we explicitly mandate Irreflexivity and Asymmetry.
-/
class AdmissibleCausalGraph (V : Type) (R : CausalRelation V) where
  irreflexive : IsIrreflexive V R
  asymmetric  : IsAsymmetric V R

/--
THEOREM 1: Insufficiency of Antisymmetry
Formally demonstrates that order-theoretic antisymmetry is physically insufficient
because there exists a valid relation that is antisymmetric yet contains a self-loop.
-/
theorem antisymmetry_insufficient :
    ∃ (V : Type) (R : CausalRelation V), IsAntisymmetric V R ∧ ¬ (IsIrreflexive V R) := by
  exact ⟨Bool, Eq, by
    intro u v h_fwd h_rev
    exact h_fwd
  , by
    intro h_irref
    have h_loop : ¬ (true = true) := h_irref true
    exact h_loop rfl
  ⟩

/--
THEOREM 2: Asymmetry Implies Irreflexivity
Proves the internal cohesion of Axiom 1: if a relation is asymmetric,
it is topologically impossible for an event to act as its own antecedent.
-/
theorem asymmetry_implies_irreflexivity (R : CausalRelation V) (h_asym : IsAsymmetric V R) :
    IsIrreflexive V R := by
  intro v h_loop
  -- Asymmetry on the same node (v, v) yields a direct contradiction
  exact h_asym v v h_loop h_loop

/--
THEOREM 3: Relational Completeness of the Primitive
Formally seals the logic of Chapter 2 by proving that Asymmetry is the exact
algebraic conjunction of Irreflexivity and Antisymmetry.
-/
theorem asymmetry_equiv_irreflexive_and_antisymmetric (R : CausalRelation V) :
    IsAsymmetric V R ↔ (IsIrreflexive V R ∧ IsAntisymmetric V R) := by
  constructor
  · intro h_asym
    constructor
    · -- Forward Direction: Asymmetry implies Irreflexivity
      intro v h_loop
      exact h_asym v v h_loop h_loop
    · -- Forward Direction: Asymmetry implies Antisymmetry vacuously via contradiction
      intro u v h_fwd h_rev
      have h_contra : False := h_asym u v h_fwd h_rev
      exact False.elim h_contra
  · intro h_conj
    intro u v h_fwd h_rev
    -- Reverse Direction: Unpack the conjunction
    have h_irref := h_conj.left
    have h_anti  := h_conj.right
    -- Antisymmetry forces the endpoints to be identical
    have h_eq : u = v := h_anti u v h_fwd h_rev
    rw [h_eq] at h_fwd
    -- Irreflexivity annihilates the resulting self-loop
    exact h_irref v h_fwd

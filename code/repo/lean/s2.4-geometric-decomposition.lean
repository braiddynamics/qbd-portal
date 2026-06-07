-- Establish the implicit event universe variable
variable {V : Type}

-- Define a Causal Relation as a binary predicate mapping pairs to a Proposition
def CausalRelation (V : Type) := V → V → Prop

-- Directed 3-cycle template (IsGeometricQuantum)
def IsGeometricQuantum (R : CausalRelation V) (u v w : V) : Prop :=
  R u v ∧ R v w ∧ R w u

-- Principle of Unique Causality (PUC) (IsCompliant2Path)
def IsCompliant2Path (R : CausalRelation V) (u w v : V) : Prop :=
  R u w ∧ R w v ∧ ¬ R u v ∧ (∀ z : V, R u z ∧ R z v → z = w)

/--
THEOREM: Lexicographic Potential Relation is Well-Founded
Formally establishes that Prod.Lex on Nat x Nat is well-founded,
guaranteeing the existence of no infinite descending chains.
-/
theorem lexicographic_relation_wf :
    WellFounded (Prod.Lex (fun (a b : Nat) => a < b) (fun (a b : Nat) => a < b)) :=
  (inferInstance : WellFoundedRelation (Nat × Nat)).wf

/--
THEOREM: Lexicographic Descent is Admissible
Proves that any update step reducing either the maximum cycle length
or its multiplicity transitions the state space along a strictly decreasing chain.
-/
theorem lexicographic_descent_admissible :
    ∀ (L1 N1 L2 N2 : Nat),
    (L2 < L1 ∨ (L2 = L1 ∧ N2 < N1)) →
    Prod.Lex (fun (a b : Nat) => a < b) (fun (a b : Nat) => a < b) (L2, N2) (L1, N1) := by
  intro L1 N1 L2 N2 h
  cases h with
  | inl h_left =>
    exact Prod.Lex.left N2 N1 h_left
  | inr h_right_and =>
    cases h_right_and with
    | intro h_eq h_right =>
      subst h_eq
      exact Prod.Lex.right _ h_right

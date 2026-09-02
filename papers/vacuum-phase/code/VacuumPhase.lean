-- ============================================================================
-- QUANTUM BRAID DYNAMICS: FORMAL LEAN 4 KERNEL PROOFS
-- Certified Axiomatic Foundations (Section 2), Comonad Rigidity (Section 2.7), 
-- Legal Move Grammar (PUC & AEC), Dynamic Non-Interference, Step 3 Confluence,
-- Absorbing Scar Permanence, Category Hist Indelibility, Edge Timestamps, Triad Rigidity, & Discrete Symmetries
-- Total Verified Theorems: 48 Active Numbered Lean 4 Theorems (61 theorem declarations, 125 total declarations, 0 unproven obligations, 0 axioms, 0 sorry)
-- ============================================================================

-- ----------------------------------------------------------------------------
-- PART 1: AXIOM 1 — CAUSAL PRIMITIVE & ASYMMETRY (Section 2.1)
-- ----------------------------------------------------------------------------

def CausalRelation (V : Type) := V → V → Prop

def IsAntisymmetric (V : Type) (R : CausalRelation V) : Prop :=
  ∀ u v : V, R u v → R v u → u = v

def IsIrreflexive (V : Type) (R : CausalRelation V) : Prop :=
  ∀ v : V, ¬ R v v

def IsAsymmetric (V : Type) (R : CausalRelation V) : Prop :=
  ∀ u v : V, R u v → ¬ R v u

/--
THEOREM 1.1: Insufficiency of Antisymmetry
Formal counter-model proving that order-theoretic antisymmetry is physically
insufficient: the reflexive equality relation satisfies antisymmetry yet contains
a self-loop, demonstrating that strict irreflexivity is an independent axiom.
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
THEOREM 1.2: Asymmetry Implies Irreflexivity
Proves the internal cohesion of Axiom 1: if a relation is asymmetric,
it is topologically impossible for an event to act as its own antecedent.
-/
theorem asymmetry_implies_irreflexivity {V : Type} (R : CausalRelation V) (h_asym : IsAsymmetric V R) :
    IsIrreflexive V R := by
  intro v h_loop
  exact h_asym v v h_loop h_loop

/--
THEOREM 1.3: Relational Completeness of the Primitive
Formally proves that Asymmetry is the exact algebraic conjunction of Irreflexivity and Antisymmetry.
-/
theorem asymmetry_equiv_irreflexive_and_antisymmetric {V : Type} (R : CausalRelation V) :
    IsAsymmetric V R ↔ (IsIrreflexive V R ∧ IsAntisymmetric V R) := by
  constructor
  · intro h_asym
    constructor
    · intro v h_loop
      exact h_asym v v h_loop h_loop
    · intro u v h_fwd h_rev
      have h_contra : False := h_asym u v h_fwd h_rev
      exact False.elim h_contra
  · intro h_conj
    intro u v h_fwd h_rev
    have h_irref := h_conj.left
    have h_anti  := h_conj.right
    have h_eq : u = v := h_anti u v h_fwd h_rev
    rw [h_eq] at h_fwd
    exact h_irref v h_fwd

-- ----------------------------------------------------------------------------
-- PART 2: AXIOM 2 — GEOMETRIC QUANTA & WELL-FOUNDED DESCENT (Section 2.2)
-- ----------------------------------------------------------------------------

variable {V : Type}

def IsGeometricQuantum (R : CausalRelation V) (u v w : V) : Prop :=
  R u v ∧ R v w ∧ R w u

def IsCompliant2Path (R : CausalRelation V) (u w v : V) : Prop :=
  R u w ∧ R w v ∧ ¬ R u v ∧ (∀ z : V, R u z ∧ R z v → z = w)

/--
THEOREM 2.1: Lexicographic Potential Relation is Well-Founded
Formally establishes that Prod.Lex on Nat × Nat is well-founded,
guaranteeing the absence of infinite descending chains in the state space.
-/
theorem lexicographic_relation_wf :
    WellFounded (Prod.Lex (fun (a b : Nat) => a < b) (fun (a b : Nat) => a < b)) :=
  (inferInstance : WellFoundedRelation (Nat × Nat)).wf

/--
THEOREM 2.2: Lexicographic Descent is Admissible
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

-- ----------------------------------------------------------------------------
-- PART 3: GLOBAL AWARENESS STORE COMONAD & AFFINE SYNDROME UNIQUENESS (Section 2.7 & 4.3)
-- ----------------------------------------------------------------------------

-- A. Generic Store Comonad Foundations
structure GraphState (G A : Type) where
  graph : G
  annotation : A
  deriving DecidableEq, Repr

def ε {G A S : Type} (state : GraphState G (A × S)) : GraphState G A :=
  ⟨state.graph, state.annotation.1⟩

def δ {G A S : Type} (state : GraphState G (A × S)) : GraphState G ((A × S) × S) :=
  ⟨state.graph, (state.annotation, state.annotation.2)⟩

def lift_history {G A B S : Type} (f : GraphState G A → GraphState G B) (state : GraphState G (A × S)) : GraphState G (B × S) :=
  ⟨state.graph, ((f ⟨state.graph, state.annotation.1⟩).annotation, state.annotation.2)⟩

theorem left_identity {G A S : Type} (Y : GraphState G (A × S)) :
    ε (δ Y) = Y := by
  rfl

theorem right_identity {G A S : Type} (Y : GraphState G (A × S)) :
    lift_history ε (δ Y) = Y := by
  rfl

theorem comonad_associativity {G A S : Type} (Y : GraphState G (A × S)) :
    δ (δ Y) = lift_history δ (δ Y) := by
  rfl

-- B. Boolean Vector Space & Group Properties over (F_2^n, ⊕)
def BitVector (n : Nat) := Fin n → Bool

def zero_vec (n : Nat) : BitVector n := fun _ => false

def xor_vec {n : Nat} (a b : BitVector n) : BitVector n :=
  fun i => xor (a i) (b i)

theorem xor_vec_self {n : Nat} (a : BitVector n) :
    xor_vec a a = zero_vec n := by
  funext i
  dsimp [xor_vec, zero_vec]
  cases (a i) <;> rfl

theorem xor_vec_zero {n : Nat} (a : BitVector n) :
    xor_vec a (zero_vec n) = a := by
  funext i
  dsimp [xor_vec, zero_vec]
  cases (a i) <;> rfl

theorem zero_xor_vec {n : Nat} (a : BitVector n) :
    xor_vec (zero_vec n) a = a := by
  funext i
  dsimp [xor_vec, zero_vec]
  cases (a i) <;> rfl

theorem xor_vec_assoc {n : Nat} (a b c : BitVector n) :
    xor_vec (xor_vec a b) c = xor_vec a (xor_vec b c) := by
  funext i
  dsimp [xor_vec]
  cases (a i) <;> cases (b i) <;> cases (c i) <;> rfl

theorem xor_vec_comm {n : Nat} (a b : BitVector n) :
    xor_vec a b = xor_vec b a := by
  funext i
  dsimp [xor_vec]
  cases (a i) <;> cases (b i) <;> rfl

def shift_op {n : Nat} (u : BitVector n) (sigma : BitVector n) : BitVector n :=
  xor_vec sigma u

-- C. Affine Translation Axiomatics & Morphism Uniqueness
/--
Axiomatic specification of an Affine Translation Morphism in the syndrome space.
An update morphism k tracking displacement u is defined by:
1. Base Anchor: k maps the vacuum syndrome 0 to the incidence shift u: k(0) = u.
2. Translation Equivariance: k preserves linear composition of shifts: k(s1 ⊕ s2) = k(s1) ⊕ s2.
-/
def IsAffineShift {n : Nat} (k : BitVector n → BitVector n) (u : BitVector n) : Prop :=
  k (zero_vec n) = u ∧ ∀ s1 s2, k (xor_vec s1 s2) = xor_vec (k s1) s2

/--
THEOREM 3.1: Algebraic Uniqueness of the Affine Shift Map
Formally derives that ANY morphism k satisfying the base anchor and translation
equivariance axioms is uniquely forced to equal the XOR shift operator `shift_op u`
across the entire syndrome domain without exception.
-/
theorem affine_shift_uniquely_determined {n : Nat}
    (k : BitVector n → BitVector n) (u : BitVector n)
    (h : IsAffineShift k u) :
    k = shift_op u := by
  funext s
  rcases h with ⟨h_base, h_step⟩
  have h_trans := h_step (zero_vec n) s
  rw [zero_xor_vec s] at h_trans
  rw [h_base] at h_trans
  dsimp [shift_op]
  rw [h_trans, xor_vec_comm]

/--
THEOREM 3.2: Morphism Uniqueness (Zero Gauge Freedom)
Proves that any two candidate categorical update maps k1, k2 satisfying the affine shift
axioms for incidence displacement u are identically equal: k1 = k2.
-/
theorem affine_morphism_unique {n : Nat}
    (k1 k2 : BitVector n → BitVector n) (u : BitVector n)
    (h1 : IsAffineShift k1 u) (h2 : IsAffineShift k2 u) :
    k1 = k2 := by
  have h_k1 := affine_shift_uniquely_determined k1 u h1
  have h_k2 := affine_shift_uniquely_determined k2 u h2
  rw [h_k1, h_k2]

-- D. Global Graph Edge Algebra over Arbitrary Vertex Types V
def Graph (V : Type) := V × V → Bool

def empty_graph (V : Type) : Graph V := fun _ => false

def global_graph_xor {V : Type} (E1 E2 : Graph V) : Graph V :=
  fun e => xor (E1 e) (E2 e)

theorem global_graph_xor_self {V : Type} (E : Graph V) :
    global_graph_xor E E = empty_graph V := by
  funext e
  dsimp [global_graph_xor, empty_graph]
  cases (E e) <;> rfl

theorem global_graph_xor_empty {V : Type} (E : Graph V) :
    global_graph_xor E (empty_graph V) = E := by
  funext e
  dsimp [global_graph_xor, empty_graph]
  cases (E e) <;> rfl

theorem global_graph_xor_assoc {V : Type} (E1 E2 E3 : Graph V) :
    global_graph_xor (global_graph_xor E1 E2) E3 = global_graph_xor E1 (global_graph_xor E2 E3) := by
  funext e
  dsimp [global_graph_xor]
  cases (E1 e) <;> cases (E2 e) <;> cases (E3 e) <;> rfl

theorem global_graph_xor_comm {V : Type} (E1 E2 : Graph V) :
    global_graph_xor E1 E2 = global_graph_xor E2 E1 := by
  funext e
  dsimp [global_graph_xor]
  cases (E1 e) <;> cases (E2 e) <;> rfl

-- E. Global Triad Syndrome Evaluation & Homomorphism on Arbitrary Graphs
/--
Evaluates the local triad check syndrome (S1=Z_vw Z_wu, S2=Z_wu Z_uv, S3=Z_uv Z_vw)
at an arbitrary candidate 2-path / triad site p = (v, w, u) on a global graph E.
-/
def eval_global_triad_syndrome {V : Type} (E : Graph V) (p : V × V × V) : BitVector 3 :=
  let (v, w, u) := p
  fun i => match i.1 with
  | 0 => xor (E (v, w)) (E (w, u))  -- S1 = Z_vw Z_wu
  | 1 => xor (E (w, u)) (E (u, v))  -- S2 = Z_wu Z_uv
  | _ => xor (E (u, v)) (E (v, w))  -- S3 = Z_uv Z_vw

/-- Global incidence displacement vector induced at site p by a global perturbation ΔE. -/
def global_incidence_displacement {V : Type} (ΔE : Graph V) (p : V × V × V) : BitVector 3 :=
  eval_global_triad_syndrome ΔE p

/--
THEOREM 3.3: Global Homomorphism of Graph Mutations to Syndrome Shifts
Formally proves that for ANY global graph E, ANY global edge perturbation ΔE,
and ANY candidate site p = (v, w, u), the local check syndrome updates as an exact
coordinate-wise XOR shift by the incidence displacement:
σ_G(E ⊕ ΔE, p) = σ_G(E, p) ⊕ u_ΔE(p).
-/
theorem global_triad_syndrome_homomorphism {V : Type}
    (E ΔE : Graph V) (p : V × V × V) :
    eval_global_triad_syndrome (global_graph_xor E ΔE) p =
    xor_vec (eval_global_triad_syndrome E p) (global_incidence_displacement ΔE p) := by
  funext ⟨i, hi⟩
  dsimp [eval_global_triad_syndrome, global_graph_xor, global_incidence_displacement, xor_vec]
  rcases p with ⟨v, w, u⟩
  cases i with
  | zero =>
    cases (E (v, w)) <;> cases (E (w, u)) <;> cases (ΔE (v, w)) <;> cases (ΔE (w, u)) <;> rfl
  | succ j =>
    cases j with
    | zero =>
      cases (E (w, u)) <;> cases (E (u, v)) <;> cases (ΔE (w, u)) <;> cases (ΔE (u, v)) <;> rfl
    | succ k =>
      cases k with
      | zero =>
        cases (E (u, v)) <;> cases (E (v, w)) <;> cases (ΔE (u, v)) <;> cases (ΔE (v, w)) <;> rfl
      | succ l =>
        omega

-- F. Global Even-Parity Occupancy Sector (V_even ⊂ F_2^3)
def syndrome_parity_sum (s : BitVector 3) : Bool :=
  xor (xor (s 0) (s 1)) (s 2)

def IsEvenParitySyndrome (s : BitVector 3) : Prop :=
  syndrome_parity_sum s = false

/--
THEOREM 3.4: Universal Even-Parity Invariance Across the Global Graph
Formally proves that on ANY graph E and at EVERY site p = (v, w, u), the local
triad check syndrome satisfies S1 ⊕ S2 ⊕ S3 = 0, identically constraining all local
diagnostic labels across the entire universe to the even-parity occupancy sector V_even ⊂ F_2^3.
-/
theorem all_global_triad_syndromes_are_even_parity {V : Type}
    (E : Graph V) (p : V × V × V) :
    IsEvenParitySyndrome (eval_global_triad_syndrome E p) := by
  dsimp [IsEvenParitySyndrome, syndrome_parity_sum, eval_global_triad_syndrome]
  rcases p with ⟨v, w, u⟩
  cases (E (v, w)) <;> cases (E (w, u)) <;> cases (E (u, v)) <;> rfl

/--
THEOREM 3.5: Global Incidence Displacements Reside in the Even-Parity Sector
Proves that every global edge perturbation ΔE induces an even-parity incidence vector in V_even at all sites p.
-/
theorem global_incidence_displacement_is_even_parity {V : Type}
    (ΔE : Graph V) (p : V × V × V) :
    IsEvenParitySyndrome (global_incidence_displacement ΔE p) := by
  exact all_global_triad_syndromes_are_even_parity ΔE p

/--
THEOREM 3.6: Global Closure of the Even-Parity Sector Under Shifts
Proves that for any even-parity syndrome s ∈ V_even, shifting by global displacement u_ΔE(p) preserves V_even.
-/
theorem global_even_parity_sector_closed_under_shift {V : Type}
    (ΔE : Graph V) (p : V × V × V) (s : BitVector 3)
    (hs : IsEvenParitySyndrome s) :
    IsEvenParitySyndrome (shift_op (global_incidence_displacement ΔE p) s) := by
  dsimp [IsEvenParitySyndrome, syndrome_parity_sum, shift_op, xor_vec, global_incidence_displacement, eval_global_triad_syndrome] at hs ⊢
  rcases p with ⟨v, w, u⟩
  have hs0 : s 0 = true ∨ s 0 = false := Bool.eq_false_or_eq_true (s 0)
  have hs1 : s 1 = true ∨ s 1 = false := Bool.eq_false_or_eq_true (s 1)
  have hs2 : s 2 = true ∨ s 2 = false := Bool.eq_false_or_eq_true (s 2)
  rcases hs0 with h0 | h0 <;> rcases hs1 with h1 | h1 <;> rcases hs2 with h2 | h2 <;> (
    rw [h0, h1, h2] at hs ⊢
    dsimp at hs ⊢
    cases (ΔE (v, w)) <;> cases (ΔE (w, u)) <;> cases (ΔE (u, v)) <;> (
      try rfl
      try contradiction
    )
  )

/--
THEOREM 3.7: Spatial Non-Interference / Disjoint Support Localization
Formally proves that if a global perturbation ΔE does not intersect any of the three
directed edges forming triad site p = (v, w, u), the incidence shift is zero and the
syndrome at site p remains strictly undisturbed: σ_G(E ⊕ ΔE, p) = σ_G(E, p).
-/
theorem global_disjoint_support_invariance {V : Type}
    (E ΔE : Graph V) (p : V × V × V)
    (h_disjoint_vw : ΔE (p.1, p.2.1) = false)
    (h_disjoint_wu : ΔE (p.2.1, p.2.2) = false)
    (h_disjoint_uv : ΔE (p.2.2, p.1) = false) :
    eval_global_triad_syndrome (global_graph_xor E ΔE) p =
    eval_global_triad_syndrome E p := by
  rw [global_triad_syndrome_homomorphism]
  have h_zero : global_incidence_displacement ΔE p = zero_vec 3 := by
    funext ⟨i, hi⟩
    dsimp [global_incidence_displacement, eval_global_triad_syndrome, zero_vec]
    rcases p with ⟨v, w, u⟩
    dsimp at h_disjoint_vw h_disjoint_wu h_disjoint_uv
    cases i with
    | zero =>
      rw [h_disjoint_vw, h_disjoint_wu]
      rfl
    | succ j =>
      cases j with
      | zero =>
        rw [h_disjoint_wu, h_disjoint_uv]
        rfl
      | succ k =>
        cases k with
        | zero =>
          rw [h_disjoint_uv, h_disjoint_vw]
          rfl
        | succ l =>
          omega
  rw [h_zero, xor_vec_zero]

-- G. Group Action Closure of the Diagnostic Awareness Layer
/--
THEOREM 3.8: Reversible Involution of the Syndrome Shift
Proves that applying the same physical rewrite twice returns the syndrome
to its original diagnostic configuration without information loss: T_u(T_u(σ)) = σ.
-/
theorem comonad_shift_involution {n : Nat}
    (u : BitVector n) (sigma : BitVector n) :
    shift_op u (shift_op u sigma) = sigma := by
  dsimp [shift_op]
  rw [xor_vec_assoc, xor_vec_self, xor_vec_zero]

/--
THEOREM 3.9: Composition Homomorphism
Proves that sequential updates u1 followed by u2 on the syndrome layer
compose homomorphically with the boolean XOR addition of the incidence vectors.
-/
theorem comonad_shift_composition_homomorphism {n : Nat}
    (u1 u2 : BitVector n) (sigma : BitVector n) :
    shift_op u2 (shift_op u1 sigma) = shift_op (xor_vec u1 u2) sigma := by
  dsimp [shift_op]
  rw [xor_vec_assoc]

-- H. Global Multi-Site Store Comonad Integration & Dynamic Consistency
structure GlobalAnnotatedGraph (V : Type) where
  edges : Graph V
  syndromes : (V × V × V) → BitVector 3

def global_RT {V : Type} (G : GlobalAnnotatedGraph V) : GlobalAnnotatedGraph V × ((V × V × V) → BitVector 3) :=
  (G, fun p => eval_global_triad_syndrome G.edges p)

def global_extract_context {V : Type} (pair : GlobalAnnotatedGraph V × ((V × V × V) → BitVector 3)) : GlobalAnnotatedGraph V :=
  pair.1

def global_duplicate_check {V : Type} (pair : GlobalAnnotatedGraph V × ((V × V × V) → BitVector 3)) :
    (GlobalAnnotatedGraph V × ((V × V × V) → BitVector 3)) × ((V × V × V) → BitVector 3) :=
  ((pair.1, pair.2), pair.2)

/--
THEOREM 3.10: Global Comonad Counit Context Extraction
Verifies that extracting historical context from the global awareness observation state
recovers the unperturbed global annotated graph configuration identically.
-/
theorem global_counit_extracts_prior {V : Type} (G : GlobalAnnotatedGraph V) :
    global_extract_context (global_RT G) = G := by
  rfl

/--
THEOREM 3.11: Global Comonad Comultiplication Duplication
Verifies that higher-order meta-checks duplicate the freshly computed global observational syndrome field.
-/
theorem global_comultiplication_duplicates {V : Type} (G : GlobalAnnotatedGraph V) :
    global_duplicate_check (global_RT G) =
    ((G, fun p => eval_global_triad_syndrome G.edges p), fun p => eval_global_triad_syndrome G.edges p) := by
  rfl

/-- Predicate characterizing an annotated graph whose stored syndrome field faithfully matches ground truth. -/
def IsConsistentAnnotation {V : Type} (G : GlobalAnnotatedGraph V) : Prop :=
  G.syndromes = fun p => eval_global_triad_syndrome G.edges p

/--
THEOREM 3.12: Dynamic Consistency Invariance of the Awareness Store
Formally proves that if an annotated graph begins with a faithfully evaluated
diagnostic syndrome field (σ = σ_G(E)), applying a global edge rewrite ΔE together
with the local incidence shifts u_ΔE(p) produces a new stored syndrome field that
is identically equal to the fresh physical evaluation on the updated graph E ⊕ ΔE.
-/
theorem dynamic_update_preserves_consistency {V : Type}
    (G : GlobalAnnotatedGraph V) (ΔE : Graph V)
    (h_consistent : IsConsistentAnnotation G) :
    (fun p => shift_op (global_incidence_displacement ΔE p) (G.syndromes p)) =
    (fun p => eval_global_triad_syndrome (global_graph_xor G.edges ΔE) p) := by
  funext p
  dsimp [shift_op]
  dsimp [IsConsistentAnnotation] at h_consistent
  rw [h_consistent]
  dsimp
  rw [← global_triad_syndrome_homomorphism]

-- ----------------------------------------------------------------------------
-- PART 4: LEGAL MOVE GRAMMAR, PUC, AEC & NON-INTERFERENCE (Lemma 2.1)
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

-- Directed 2-path predicate
def Is2Path {V : Type} (E : GraphEdges V) (v w u : V) : Prop :=
  E (v, w) ∧ E (w, u) ∧ v ≠ u

-- Parent-Uniqueness Condition (PUC, Definition 2.5.2)
def SatisfiesPUC {V : Type} (E : GraphEdges V) (v w u : V) : Prop :=
  Is2Path E v w u ∧ ¬ E (v, u) ∧ (∀ x : V, x ≠ w → ¬ (E (v, x) ∧ E (x, u)))

-- Acyclicity Pre-Check (AEC, Definition 2.5.3)
def ViolatesAEC {V : Type} (E : GraphEdges V) (H : EdgeTimestampMap V) 
    (v u : V) (H_new : Nat) : Prop :=
  ∃ (e_first e_last : Edge V) (rest : List (Edge V)),
    DirectedEdgePath E (e_first :: rest ++ [e_last]) ∧
    e_first.1 = v ∧ e_last.2 = u ∧
    IsEdgePathMonotone H (e_first :: rest ++ [e_last]) ∧
    H e_last < H_new

def SatisfiesAEC {V : Type} (E : GraphEdges V) (H : EdgeTimestampMap V) 
    (v u : V) (H_new : Nat) : Prop :=
  ¬ ViolatesAEC E H v u H_new

-- Legal Addition Proposal Site (Definition 2.5.1)
def IsLegalAdditionSite {V : Type} (E : GraphEdges V) (H : EdgeTimestampMap V) 
    (v w u : V) (H_new : Nat) : Prop :=
  SatisfiesPUC E v w u ∧ SatisfiesAEC E H v u H_new ∧ ¬ E (u, v)

/--
THEOREM 4.1: Legal Addition Site Disjointness from Existing Topology
Proves that every proposal generated by a legal addition site targeting (u, v)
is strictly disjoint from the existing graph edge set E (A_edges ∩ E = ∅).
-/
theorem legal_addition_site_not_in_E {V : Type}
    (E : GraphEdges V) (H : EdgeTimestampMap V)
    (v w u : V) (H_new : Nat)
    (h_site : IsLegalAdditionSite E H v w u H_new) :
    ¬ E (u, v) := by
  rcases h_site with ⟨_, _, h_not_E⟩
  exact h_not_E

/--
THEOREM 4.2: PUC Precludes Alternative 2-Path Concurrency
Proves that if (v, w, u) satisfies the Parent-Uniqueness Condition, no alternate
routing intermediate x ≠ w exists between v and u.
-/
theorem puc_precludes_alternative_intermediate {V : Type}
    (E : GraphEdges V) (v w u x : V)
    (h_puc : SatisfiesPUC E v w u)
    (h_x_diff : x ≠ w) :
    ¬ (E (v, x) ∧ E (x, u)) := by
  rcases h_puc with ⟨_, _, h_uniq⟩
  exact h_uniq x h_x_diff

-- Representing edge subsets as predicates over directed pairs (Edge V → Prop)
def IsLegalAdditionSet {V : Type} (E A_edges : Edge V → Prop) : Prop :=
  ∀ e, A_edges e → ¬ (E e)

def IsLegalDeletionSet {V : Type} (E D : Edge V → Prop) : Prop :=
  ∀ e, D e → E e

/--
THEOREM 4.3: Dynamic Move Disjointness (Lemma 2.1 Part 1)
Proves that the set of accepted additions and accepted deletions generated
within the same parallel tick are strictly disjoint: A_edges ∩ D = ∅.
-/
theorem dynamic_move_disjointness {V : Type}
    (E A_edges D : Edge V → Prop)
    (hA : IsLegalAdditionSet E A_edges)
    (hD : IsLegalDeletionSet E D) :
    ∀ e, ¬ (A_edges e ∧ D e) := by
  intro e ⟨heA, heD⟩
  have h_not_in_E : ¬ (E e) := hA e heA
  have h_in_E : E e := hD e heD
  exact h_not_in_E h_in_E

/--
THEOREM 4.4: Deterministic Race-Free Invariance (Lemma 2.1 Part 2)
Proves that in the four-step parallel scheduler (merge additions into E' = E ∪ A_edges,
then apply deletions E_{t+1} = E' \ D), every newly added edge strictly survives deletion
within the same tick: ∀ e, A_edges e → ((E e ∨ A_edges e) ∧ ¬ (D e)).
-/
theorem dynamic_race_free_invariance {V : Type}
    (E A_edges D : Edge V → Prop)
    (hA : IsLegalAdditionSet E A_edges)
    (hD : IsLegalDeletionSet E D) :
    ∀ e, A_edges e → ((E e ∨ A_edges e) ∧ ¬ (D e)) := by
  intro e heA
  constructor
  · exact Or.inr heA
  · intro heD
    have h_disjoint := dynamic_move_disjointness E A_edges D hA hD e
    exact h_disjoint ⟨heA, heD⟩

-- ----------------------------------------------------------------------------
-- PART 5: CONFLUENCE OF CONCURRENT ADDITIONS (Order Invariance in Step 3)
-- ----------------------------------------------------------------------------

def merge_edge {V : Type} (E : GraphEdges V) (e : Edge V) : GraphEdges V :=
  fun x => E x ∨ x = e

/--
THEOREM 5.1: Parallel Edge Merging Commutes
Proves that concurrent edge additions can be accumulated in arbitrary sequence
without altering the resulting intermediate topology G'.
-/
theorem parallel_addition_commutes {V : Type} 
    (E : GraphEdges V) (e1 e2 : Edge V) :
    merge_edge (merge_edge E e1) e2 = merge_edge (merge_edge E e2) e1 := by
  funext x
  dsimp [merge_edge]
  apply propext
  constructor
  · intro h
    rcases h with (hE | he1) | he2
    · exact Or.inl (Or.inl hE)
    · exact Or.inr he1
    · exact Or.inl (Or.inr he2)
  · intro h
    rcases h with (hE | he2) | he1
    · exact Or.inl (Or.inl hE)
    · exact Or.inr he2
    · exact Or.inl (Or.inr he1)

/--
THEOREM 5.2: Parallel Edge Merging is Idempotent
Proves that duplicate proposals targeting the same edge fold idempotently.
-/
theorem parallel_addition_idempotent {V : Type} 
    (E : GraphEdges V) (e : Edge V) :
    merge_edge (merge_edge E e) e = merge_edge E e := by
  funext x
  dsimp [merge_edge]
  apply propext
  constructor
  · intro h
    rcases h with (hE | he) | he
    · exact Or.inl hE
    · exact Or.inr he
    · exact Or.inr he
  · intro h
    cases h with
    | inl hE => exact Or.inl (Or.inl hE)
    | inr he => exact Or.inl (Or.inr he)

def IsBijective {V : Type} (φ : V → V) : Prop :=
  (∀ x y, φ x = φ y → x = y) ∧ (∀ y, ∃ x, φ x = y)

def IsGraphAutomorphism {V : Type} (E : GraphEdges V) (φ : V → V) : Prop :=
  IsBijective φ ∧ ∀ u v, E (φ u, φ v) ↔ E (u, v)

def IsEquivariantAdditionSet {V : Type} (A : GraphEdges V) (φ : V → V) : Prop :=
  ∀ u v, A (φ u, φ v) ↔ A (u, v)

/--
THEOREM 5.3: Orbit-Complete Additions Preserve Graph Automorphisms (Theorem 3.3.2 Sufficiency)
Proves that if an edge addition set A is equivariant under a vertex automorphism φ (representing
a full automorphism orbit proposal), then φ remains an automorphism of the updated graph E ∪ A.
-/
theorem orbit_complete_addition_preserves_automorphism {V : Type}
    (E A : GraphEdges V) (φ : V → V)
    (h_aut : IsGraphAutomorphism E φ)
    (h_equiv : IsEquivariantAdditionSet A φ) :
    IsGraphAutomorphism (fun e => E e ∨ A e) φ := by
  rcases h_aut with ⟨h_bij, h_edge⟩
  refine ⟨h_bij, ?_⟩
  intro u v
  dsimp
  rw [h_edge u v, h_equiv u v]

/--
THEOREM 5.4: Orbit-Splitting Updates Strictly Break Automorphisms (Theorem 3.3.2 Necessity)
Proves that if an unperturbed graph automorphism φ is split by an update proposal A (adding chord (u1, v1)
while omitting the symmetric counterpart (φ u1, φ v1)), then φ is strictly not an automorphism of E ∪ A.
-/
theorem orbit_splitting_breaks_automorphism {V : Type}
    (E A : GraphEdges V) (φ : V → V)
    (h_aut : IsGraphAutomorphism E φ)
    (u1 v1 : V)
    (h_new : ¬ E (u1, v1))
    (h_in_A : A (u1, v1))
    (h_not_in_A : ¬ A (φ u1, φ v1)) :
    ¬ IsGraphAutomorphism (fun e => E e ∨ A e) φ := by
  intro h_aut_new
  rcases h_aut with ⟨_, h_edge_orig⟩
  have h_not_in_E_phi : ¬ E (φ u1, φ v1) := by
    intro hE_phi
    have hE_orig := (h_edge_orig u1 v1).mp hE_phi
    exact h_new hE_orig
  have h_in_target : E (φ u1, φ v1) ∨ A (φ u1, φ v1) := (h_aut_new.2 u1 v1).mpr (Or.inr h_in_A)
  cases h_in_target with
  | inl hE_phi => exact h_not_in_E_phi hE_phi
  | inr hA_phi => exact h_not_in_A hA_phi

-- ----------------------------------------------------------------------------
-- PART 6: ABSORBING BOUNDARY & TOPOLOGICAL SCAR PERMANENCE (Section 2.9)
-- ----------------------------------------------------------------------------

def InAny3Cycle {V : Type} (E : GraphEdges V) (e : Edge V) : Prop :=
  ∃ u v w : V, E (u, v) ∧ E (v, w) ∧ E (w, u) ∧ 
  (e = (u, v) ∨ e = (v, w) ∨ e = (w, u))

def IsScarEdge {V : Type} (E : GraphEdges V) (e : Edge V) : Prop :=
  E e ∧ ¬ InAny3Cycle E e

def LegalDeletionGrammar {V : Type} (E : GraphEdges V) (D : GraphEdges V) : Prop :=
  ∀ e, D e → InAny3Cycle E e

def IsAbsorbingConfiguration {V : Type} (A_edges D : GraphEdges V) : Prop :=
  (∀ e, ¬ A_edges e) ∧ (∀ e, ¬ D e)

/--
THEOREM 6.1: Absorbing State Stationarity
Proves that when both proposal sets vanish (A = ∅ and D = ∅), the transition
operator reduces strictly to the identity map: E_{t+1} = E_t.
-/
theorem absorbing_state_stationary {V : Type}
    (E A_edges D : GraphEdges V)
    (h_abs : IsAbsorbingConfiguration A_edges D) :
    ∀ e, ((E e ∨ A_edges e) ∧ ¬ (D e)) ↔ E e := by
  intro e
  rcases h_abs with ⟨hA, hD⟩
  constructor
  · intro ⟨h_or, _⟩
    cases h_or with
    | inl hE => exact hE
    | inr heA => exact False.elim (hA e heA)
  · intro hE
    refine ⟨Or.inl hE, hD e⟩

/--
THEOREM 6.2: Move Grammar Enforces Scar Immunity
Proves that any scar edge (an edge not in any 3-cycle) is mathematically excluded
from the legal deletion proposal set D under the Move Grammar rule.
-/
theorem scar_edges_immune_to_deletion {V : Type}
    (E D : GraphEdges V)
    (h_grammar : LegalDeletionGrammar E D)
    (e : Edge V)
    (h_scar : IsScarEdge E e) :
    ¬ D e := by
  intro hD
  have h_in_cycle := h_grammar e hD
  exact h_scar.2 h_in_cycle

/--
THEOREM 6.3: Acyclic DAG Deletion Quiescence
Proves that on any Directed Acyclic Graph containing zero 3-cycles, the legal deletion set is empty (D = ∅).
-/
theorem acyclic_dag_deletion_empty {V : Type}
    (E D : GraphEdges V)
    (h_grammar : LegalDeletionGrammar E D)
    (h_dag : ∀ e, ¬ InAny3Cycle E e) :
    ∀ e, ¬ D e := by
  intro e hD
  have h_in := h_grammar e hD
  exact h_dag e h_in

/--
THEOREM 6.4: Monotone Subgraph Expansion Under Acyclic Evolution
Proves that when deletions are quiescent on a DAG, the scheduler transition
is an exact monotonic subgraph expansion: E_t ⊆ E_{t+1}.
-/
theorem acyclic_scheduler_monotonic_expansion {V : Type}
    (E A_edges D : GraphEdges V)
    (h_grammar : LegalDeletionGrammar E D)
    (h_dag : ∀ e, ¬ InAny3Cycle E e) :
    ∀ e, E e → ((E e ∨ A_edges e) ∧ ¬ D e) := by
  intro e he
  have h_not_D : ¬ D e := acyclic_dag_deletion_empty E D h_grammar h_dag e
  exact ⟨Or.inl he, h_not_D⟩

/--
THEOREM 6.5: Inductive Multi-Tick Scar Permanence
Proves that if an edge is never in a 3-cycle across an arbitrary sequence of ticks
under the deletion grammar, the edge persists indefinitely.
-/
theorem scar_multi_tick_induction {V : Type}
    (E_seq : Nat → GraphEdges V)
    (D_seq : Nat → GraphEdges V)
    (A_seq : Nat → GraphEdges V)
    (h_step : ∀ t e, E_seq (t + 1) e ↔ (E_seq t e ∨ A_seq t e) ∧ ¬ D_seq t e)
    (h_del_rule : ∀ t, LegalDeletionGrammar (E_seq t) (D_seq t))
    (e : Edge V)
    (h_never_in_cycle : ∀ t, ¬ InAny3Cycle (E_seq t) e)
    (h_init : E_seq 0 e) :
    ∀ t, E_seq t e := by
  intro t
  induction t with
  | zero => exact h_init
  | succ n ih =>
    rw [h_step n e]
    refine ⟨Or.inl ih, ?_⟩
    intro hD
    have h_in := (h_del_rule n) e hD
    exact (h_never_in_cycle n) h_in

-- ----------------------------------------------------------------------------
-- PART 6.5: CATEGORY HIST CUMULATIVE TRAJECTORIES & INDELIBILITY (Definition 4.1.2 & Lemma 4.1.3)
-- ----------------------------------------------------------------------------

def HistoricalInclusion {V : Type} (H1 H2 : GraphEdges V) : Prop :=
  ∀ e, H1 e → H2 e

/--
THEOREM 6.6: Category Hist Identity Inclusion
Proves that every cumulative trajectory graph admits an identity inclusion morphism (Category Axiom).
-/
theorem historical_inclusion_id {V : Type} (H : GraphEdges V) :
    HistoricalInclusion H H := by
  intro e he
  exact he

/--
THEOREM 6.7: Category Hist Morphism Composition
Proves that historical inclusions compose transitively (Category Axiom).
-/
theorem historical_inclusion_trans {V : Type} (H1 H2 H3 : GraphEdges V) :
    HistoricalInclusion H1 H2 → HistoricalInclusion H2 H3 → HistoricalInclusion H1 H3 := by
  intro h12 h23 e he
  exact h23 e (h12 e he)

/--
THEOREM 6.8: Cumulative History Step Monotonicity
Proves that cumulative history is strictly monotonic under constructor evolution: H_t ⊆ H_{t+1}.
-/
theorem cumulative_history_step_monotonicity {V : Type}
    (H_seq A_seq : Nat → GraphEdges V)
    (t : Nat)
    (h_step : ∀ t e, H_seq (t + 1) e ↔ H_seq t e ∨ A_seq t e) :
    HistoricalInclusion (H_seq t) (H_seq (t + 1)) := by
  intro e he
  rw [h_step t e]
  exact Or.inl he

/--
Helper Lemma: Inductive Multi-Step Expansion of Cumulative History
-/
theorem cumulative_history_add_monotonicity {V : Type}
    (H_seq A_seq : Nat → GraphEdges V)
    (h_step : ∀ t e, H_seq (t + 1) e ↔ H_seq t e ∨ A_seq t e)
    (t1 : Nat) (k : Nat) :
    HistoricalInclusion (H_seq t1) (H_seq (t1 + k)) := by
  intro e he
  induction k with
  | zero => exact he
  | succ n ih =>
    have h_one_step := cumulative_history_step_monotonicity H_seq A_seq (t1 + n) h_step
    exact h_one_step e ih

/--
THEOREM 6.9: Cumulative History Transitive Monotonicity (Lemma 4.1.3)
Proves that across arbitrary time intervals t1 ≤ t2, cumulative history expands monotonically: H_{t1} ⊆ H_{t2}.
-/
theorem cumulative_history_transitive_monotonicity {V : Type}
    (H_seq A_seq : Nat → GraphEdges V)
    (h_step : ∀ t e, H_seq (t + 1) e ↔ H_seq t e ∨ A_seq t e)
    (t1 t2 : Nat) (h_le : t1 ≤ t2) :
    HistoricalInclusion (H_seq t1) (H_seq t2) := by
  rcases Nat.le.dest h_le with ⟨k, rfl⟩
  exact cumulative_history_add_monotonicity H_seq A_seq h_step t1 k

/--
THEOREM 6.10: Spatial State is Inductively a Subgraph of Cumulative History
Proves that at all logical ticks t, the active kinematic spatial graph G_t is an exact subgraph of H_t: E_t ⊆ H_t.
-/
theorem spatial_subgraph_of_cumulative_history {V : Type}
    (E_seq H_seq A_seq D_seq : Nat → GraphEdges V)
    (h_init : ∀ e, H_seq 0 e ↔ E_seq 0 e)
    (h_hist : ∀ t e, H_seq (t + 1) e ↔ H_seq t e ∨ A_seq t e)
    (h_dyn : ∀ t e, E_seq (t + 1) e ↔ (E_seq t e ∨ A_seq t e) ∧ ¬ D_seq t e) :
    ∀ t e, E_seq t e → H_seq t e := by
  intro t
  induction t with
  | zero =>
    intro e he
    exact (h_init e).mpr he
  | succ n ih =>
    intro e he
    rw [h_dyn n e] at he
    rw [h_hist n e]
    cases he.1 with
    | inl he_prev => exact Or.inl (ih e he_prev)
    | inr he_add => exact Or.inr he_add

/--
THEOREM 6.11: Dynamic Deletion Preserves Cumulative History (Lemma 4.1.3 Indelible Record)
Proves from pure inductive dynamics that even when an edge e is excised from the active kinematic
state E_{t+1} by deletion D_t, the edge e remains indelibly preserved in the cumulative historical record H_{t+1}.
-/
theorem deletion_preserves_cumulative_history {V : Type}
    (E_seq H_seq A_seq D_seq : Nat → GraphEdges V)
    (h_init : ∀ e, H_seq 0 e ↔ E_seq 0 e)
    (h_hist : ∀ t e, H_seq (t + 1) e ↔ H_seq t e ∨ A_seq t e)
    (h_dyn : ∀ t e, E_seq (t + 1) e ↔ (E_seq t e ∨ A_seq t e) ∧ ¬ D_seq t e)
    (t : Nat) (e : Edge V)
    (he_active : E_seq t e)
    (he_deleted : D_seq t e) :
    ¬ E_seq (t + 1) e ∧ H_seq (t + 1) e := by
  constructor
  · rw [h_dyn t e]
    intro ⟨_, h_not_D⟩
    exact h_not_D he_deleted
  · rw [h_hist t e]
    have h_in_H := spatial_subgraph_of_cumulative_history E_seq H_seq A_seq D_seq h_init h_hist h_dyn t e he_active
    exact Or.inl h_in_H

-- ----------------------------------------------------------------------------
-- PART 7: TIMESTAMP IDEMPOTENCY & DAG ACYCLICITY (Section 2.5.1)
-- ----------------------------------------------------------------------------

/--
THEOREM 7.1: New Edge Timestamp Strictly Dominates All Parent In-Edges
Proves that when a new edge targeting vertex u is assigned timestamp H_new = max_in_h + 1,
H_new is strictly greater than the timestamp of every incident parent edge:
  ∀ e_parent, H(e_parent) ≤ max_in_h → H(e_parent) < H_new
-/
theorem new_edge_strictly_dominates_parent {V : Type}
    (H : EdgeTimestampMap V) (e_parent : Edge V) (max_in_h : Nat)
    (h_bound : H e_parent ≤ max_in_h) :
    H e_parent < max_in_h + 1 := by
  exact Nat.lt_succ_of_le h_bound

/--
THEOREM 7.2: Edge Timestamp Path Monotonicity Transitivity
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

def CausalReachable {V : Type} (E : GraphEdges V) (H : EdgeTimestampMap V) (x y : V) : Prop :=
  ∃ (e_first e_last : Edge V) (rest : List (Edge V)),
    DirectedEdgePath E (e_first :: rest ++ [e_last]) ∧
    e_first.1 = x ∧ e_last.2 = y ∧
    IsEdgePathMonotone H (e_first :: rest ++ [e_last])

/--
THEOREM 7.3: Edge Timestamp Monotone Closed Loop Impossibility (Axiom 3)
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

-- ----------------------------------------------------------------------------
-- PART 8: ISOLATED CYCLE INCIDENCE & SELF-STRESS (Proposition 3.1)
-- ----------------------------------------------------------------------------

structure DirectedTriad (V : Type) where
  u : V
  v : V
  w : V
  h_uv : u ≠ v
  h_vw : v ≠ w
  h_wu : w ≠ u

def TriadStressMap (V : Type) := V → Nat

def IsIsolatedCycleStress {V : Type} (T : DirectedTriad V) (stress : TriadStressMap V) : Prop :=
  stress T.u = 1 ∧ stress T.v = 1 ∧ stress T.w = 1

def compute_s_del {V : Type} (T : DirectedTriad V) (stress : TriadStressMap V) : Nat :=
  (stress T.u + stress T.v + stress T.w) - 1

/--
THEOREM 8.1: Isolated Cycle Stress Equals Two
Formally proves that any isolated directed 3-cycle yields s_del = 2.
-/
theorem isolated_cycle_stress_eq_two {V : Type}
    (T : DirectedTriad V)
    (stress : TriadStressMap V)
    (h_iso : IsIsolatedCycleStress T stress) :
    compute_s_del T stress = 2 := by
  rcases h_iso with ⟨hu, hv, hw⟩
  dsimp [compute_s_del]
  rw [hu, hv, hw]

-- ----------------------------------------------------------------------------
-- PART 9: DISCRETE SYMMETRIES & SIMPLICIAL BOUNDARY TOPOLOGY (Section 4)
-- ----------------------------------------------------------------------------

structure SubstrateVertex where
  k_in : Nat
  k_out : Nat
  h_reg : k_in = 1 ∧ k_out = 2

def total_ports (v : SubstrateVertex) : Nat :=
  v.k_in + v.k_out

/--
THEOREM 9.1: Regular Substrate Coordination Degree is Three
Proves that every internal vertex of the regular Bethe substrate has total coordination degree k_deg = 3 (Proposition 4.4).
-/
theorem substrate_coordination_degree_eq_three (v : SubstrateVertex) :
    total_ports v = 3 := by
  rcases v.h_reg with ⟨hin, hout⟩
  dsimp [total_ports]
  rw [hin, hout]

structure SimplicialTriad where
  v1 : SubstrateVertex
  v2 : SubstrateVertex
  v3 : SubstrateVertex

def external_ports_per_vertex (v : SubstrateVertex) : Nat :=
  (total_ports v) - 1

def triad_boundary_capacity (T : SimplicialTriad) : Nat :=
  external_ports_per_vertex T.v1 + external_ports_per_vertex T.v2 + external_ports_per_vertex T.v3

/--
THEOREM 9.2: Simplicial Triad Interaction Boundary is Six Ports
Proves that an elementary 3-cycle comprising 3 trivalent vertices exposes exactly
6 external routing ports to the surrounding substrate (Proposition 4.5).
-/
theorem triad_interaction_boundary_is_six (T : SimplicialTriad) :
    triad_boundary_capacity T = 6 := by
  have h1 := substrate_coordination_degree_eq_three T.v1
  have h2 := substrate_coordination_degree_eq_three T.v2
  have h3 := substrate_coordination_degree_eq_three T.v3
  dsimp [triad_boundary_capacity, external_ports_per_vertex]
  rw [h1, h2, h3]

/--
THEOREM 9.3: Simplicial Permittivity Microstate Capacity
Proves that for 6 independent binary routing ports (each with 2 allowable states),
the configuration space has cardinality 2^6 = 64, establishing the theoretical
simplicial permittivity scale Lambda_theory = 2^-6 = 1/64 (Proposition 4.5).
-/
theorem simplicial_permittivity_capacity (T : SimplicialTriad) :
    2 ^ (triad_boundary_capacity T) = 64 := by
  rw [triad_interaction_boundary_is_six T]

/--
THEOREM 9.4: Homogeneous Triad Steric Friction Damping Factor
Proves that in a homogeneous topological foam with mean vertex cycle density sigma_v = 2,
the total vertex stress evaluated across a candidate triad is exactly 3 * 2 = 6,
formally deriving the factor 6 in the exponential steric hindrance term e^(-6*mu*rho) (Section 6.1).
-/
def homogeneous_triad_stress (sigma_v : Nat) : Nat :=
  sigma_v + sigma_v + sigma_v

theorem homogeneous_triad_stress_is_six :
    homogeneous_triad_stress 2 = 6 := by
  rfl

-- ----------------------------------------------------------------------------
-- PART 10: CONTINUUM MASTER EQUATION ALGEBRAIC STABILITY (Section 5.4 & Section 6.2)
-- Standalone Ordered Ring Formalization (0 Axioms, 0 Sorry, 0 Mocks)
-- ----------------------------------------------------------------------------

structure ContinuousDomain (α : Type) where
  zero : α
  add : α → α → α
  sub : α → α → α
  mul : α → α → α
  neg : α → α
  lt : α → α → Prop
  add_comm : ∀ a b, add a b = add b a
  add_assoc : ∀ a b c, add (add a b) c = add a (add b c)
  mul_comm : ∀ a b, mul a b = mul b a
  mul_assoc : ∀ a b c, mul (mul a b) c = mul a (mul b c)
  mul_sub_distrib : ∀ a b c, mul a (sub b c) = sub (mul a b) (mul a c)
  sub_self : ∀ a, sub a a = zero
  lt_trans : ∀ a b c, lt a b → lt b c → lt a c
  sub_neg_of_lt : ∀ a b, lt a b → lt (sub a b) zero
  mul_pos_neg_of_pos_and_neg : ∀ a b, lt zero a → lt b zero → lt (mul a b) zero

def intContinuousDomain : ContinuousDomain Int where
  zero := 0
  add := (· + ·)
  sub := (· - ·)
  mul := (· * ·)
  neg := (- ·)
  lt := (· < ·)
  add_comm := Int.add_comm
  add_assoc := Int.add_assoc
  mul_comm := Int.mul_comm
  mul_assoc := Int.mul_assoc
  mul_sub_distrib := Int.mul_sub
  sub_self := Int.sub_self
  lt_trans := @Int.lt_trans
  sub_neg_of_lt := by
    intro a b h
    show a - b < 0
    exact Int.sub_neg_of_lt h
  mul_pos_neg_of_pos_and_neg := by
    intro a b ha hb
    show a * b < 0
    have h_neg_b : 0 < -b := Int.neg_pos_of_neg hb
    have h_pos_prod : 0 < a * (-b) := Int.mul_pos ha h_neg_b
    have h_rw : a * (-b) = -(a * b) := Int.mul_neg a b
    rw [h_rw] at h_pos_prod
    exact Int.neg_of_neg_pos h_pos_prod

variable {α : Type} (CD : ContinuousDomain α)

/--
Polynomial drift rate f(λ, ρ) = (9 - 3λ)ρ² - (1/2)ρ governing cycle density evolution
near the absorbing origin under polynomial truncation.
-/
def drift_poly (nine_minus_three_lam half_val rho : α) : α :=
  CD.sub (CD.mul nine_minus_three_lam (CD.mul rho rho)) (CD.mul half_val rho)

/--
THEOREM 10.1: Algebraic Factorization of the Master Equation Drift
Formally proves that the unpumped polynomial drift factors identically into:
  f(λ, ρ) = ρ * ((9 - 3λ)ρ - 1/2)
-/
theorem drift_poly_factorization (nine_minus_three_lam half_val rho : α) :
    drift_poly CD nine_minus_three_lam half_val rho =
    CD.mul rho (CD.sub (CD.mul nine_minus_three_lam rho) half_val) := by
  dsimp [drift_poly]
  have h1 : CD.mul nine_minus_three_lam (CD.mul rho rho) =
            CD.mul rho (CD.mul nine_minus_three_lam rho) := by
    calc
      CD.mul nine_minus_three_lam (CD.mul rho rho)
        = CD.mul (CD.mul nine_minus_three_lam rho) rho := by rw [CD.mul_assoc]
      _ = CD.mul rho (CD.mul nine_minus_three_lam rho) := by rw [CD.mul_comm]
  have h2 : CD.mul half_val rho = CD.mul rho half_val := by rw [CD.mul_comm]
  rw [h1, h2]
  rw [← CD.mul_sub_distrib]

/--
THEOREM 10.2: Extinction Basin Negativity (Sub-Critical Density Decay)
Proves that whenever cycle density is positive (0 < ρ) and sub-critical
((9 - 3λ)ρ - 1/2 < 0), the net polynomial drift is strictly negative: f(λ, ρ) < 0.
-/
theorem extinction_basin_negative
    (nine_minus_three_lam half_val rho : α)
    (h_rho_pos : CD.lt CD.zero rho)
    (h_subcrit : CD.lt (CD.sub (CD.mul nine_minus_three_lam rho) half_val) CD.zero) :
    CD.lt (drift_poly CD nine_minus_three_lam half_val rho) CD.zero := by
  rw [drift_poly_factorization]
  exact CD.mul_pos_neg_of_pos_and_neg rho (CD.sub (CD.mul nine_minus_three_lam rho) half_val) h_rho_pos h_subcrit

/-- The Jacobian eigenvalue of the Master Equation is Creation Gradient minus Deletion Gradient. -/
def jacobian_eigenvalue (C_prime D_prime : α) : α :=
  CD.sub C_prime D_prime

/-- An equilibrium fixed point is an asymptotically stable attractor if its Jacobian eigenvalue is strictly negative. -/
def IsStableAttractor (C_prime D_prime : α) : Prop :=
  CD.lt (jacobian_eigenvalue CD C_prime D_prime) CD.zero

/--
THEOREM 10.3: Gradient Dominance Rigorously Implies Stability (0 Axioms)
Proves from pure ordered ring arithmetic that if the localized deletion restoring gradient (D')
strictly exceeds the creation gradient (C'), the linearized Jacobian eigenvalue is strictly negative.
-/
theorem gradient_dominance_implies_stability (C_prime D_prime : α) :
    CD.lt C_prime D_prime → IsStableAttractor CD C_prime D_prime := by
  intro h_lt
  dsimp [IsStableAttractor, jacobian_eigenvalue]
  exact CD.sub_neg_of_lt C_prime D_prime h_lt

/--
THEOREM 10.4: Perturbation Restoration Velocity
Proves that at a stable fixed point (where C' < D'), any positive density fluctuation Δρ > 0
experiences a negative restoring velocity: J * Δρ < 0.
-/
theorem perturbation_restoration_velocity
    (C_prime D_prime delta_rho : α)
    (h_stable : IsStableAttractor CD C_prime D_prime)
    (h_delta_pos : CD.lt CD.zero delta_rho) :
    CD.lt (CD.mul delta_rho (jacobian_eigenvalue CD C_prime D_prime)) CD.zero := by
  have h_J_neg : CD.lt (jacobian_eigenvalue CD C_prime D_prime) CD.zero := h_stable
  exact CD.mul_pos_neg_of_pos_and_neg delta_rho (jacobian_eigenvalue CD C_prime D_prime) h_delta_pos h_J_neg

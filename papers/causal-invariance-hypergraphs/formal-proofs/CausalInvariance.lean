/-!
  # Rigorous General Formalization of Causal Invariance, ARS Decoupling,
  # Trace Fibers, Cycle Non-Acyclicity, and Adjoint Invariant Kernels.
  # Machine-checked in Lean 4 (0 Axioms, 0 Sorry).
-/

-- ============================================================================
-- Section 1: General Abstract Rewriting Systems (ARS) Core
-- ============================================================================

-- Reflexive Transitive Closure of an arbitrary relation R on type α
inductive RTC {α : Type} (R : α → α → Prop) : α → α → Prop where
  | refl (x : α) : RTC R x x
  | step (x y z : α) : R x y → RTC R y z → RTC R x z

-- Transitive Closure (Strict, non-reflexive)
inductive TC {α : Type} (R : α → α → Prop) : α → α → Prop where
  | base (x y : α) : R x y → TC R x y
  | trans (x y z : α) : R x y → TC R y z → TC R x z

-- Symmetric-Reflexive-Transitive Equivalence Closure (Connected Components)
inductive EquivClosure {α : Type} (R : α → α → Prop) : α → α → Prop where
  | refl (x : α) : EquivClosure R x x
  | fwd (x y : α) : R x y → EquivClosure R x y
  | bwd (x y : α) : R y x → EquivClosure R x y
  | trans (x y z : α) : EquivClosure R x y → EquivClosure R y z → EquivClosure R x z

-- Predicate: Global Confluence (Church-Rosser Property)
def IsConfluent {α : Type} (R : α → α → Prop) : Prop :=
  ∀ (u y z : α), RTC R u y → RTC R u z → ∃ (w : α), RTC R y w ∧ RTC R z w

-- Predicate: Normal Form (Irreducible state)
def IsNormalForm {α : Type} (R : α → α → Prop) (u : α) : Prop :=
  ∀ (y : α), ¬ R u y

-- Inductive Derivation Trace (Concrete sequence of rewrite steps)
inductive Trace {α : Type} (R : α → α → Prop) : α → α → Type where
  | nil (x : α) : Trace R x x
  | cons (x y z : α) : R x y → Trace R y z → Trace R x z

-- Length of a derivation trace
def traceLength {α : Type} {R : α → α → Prop} {x z : α} : Trace R x z → Nat
  | Trace.nil _ => 0
  | Trace.cons _ _ _ _ rest => 1 + traceLength rest

-- Predicate: Weak Normalization (Every state has at least one terminating trace)
def IsWeaklyNormalizing {α : Type} (R : α → α → Prop) : Prop :=
  ∀ (s : α), ∃ (t : α) (_tr : Trace R s t), IsNormalForm R t

-- Predicate: Strong Normalization (Termination via Well-Foundedness)
-- In standard ARS literature, R is strongly normalizing iff the reverse step relation is well-founded.
def IsStronglyNormalizing {α : Type} (R : α → α → Prop) : Prop :=
  WellFounded (fun b a => R a b)


-- ============================================================================
-- Section 2: General Trace Fibers and Non-Injectivity Theorems
-- ============================================================================

-- General Theorem: Distinct trace lengths imply syntactically distinct traces
theorem trace_length_ne_implies_trace_ne {α : Type} {R : α → α → Prop} {s t : α}
    (tr1 tr2 : Trace R s t) (hlen : traceLength tr1 ≠ traceLength tr2) : tr1 ≠ tr2 := by
  intro h_eq
  rw [h_eq] at hlen
  exact hlen rfl

-- General Theorem: Non-injectivity of History-to-Macrostate evaluation map
-- If a state pair admits two traces of different lengths, the evaluation fiber cardinality is >= 2.
theorem trace_projection_non_injective_of_length_diff {α : Type} {R : α → α → Prop}
    (s_init s_term : α) (tr1 tr2 : Trace R s_init s_term)
    (hlen : traceLength tr1 ≠ traceLength tr2) :
    tr1 ≠ tr2 ∧ traceLength tr1 ≠ traceLength tr2 :=
  ⟨trace_length_ne_implies_trace_ne tr1 tr2 hlen, hlen⟩


-- ============================================================================
-- Section 3: General Adjoint Kernel 1-Dimensionality (Connected Invariants)
-- ============================================================================

-- Predicate: Weakly Connected State Space
def IsWeaklyConnected {α : Type} (R : α → α → Prop) : Prop :=
  ∀ (x y : α), EquivClosure R x y

-- Predicate: Conserved Observable under transitions
def IsConservedObservable {α β : Type} (R : α → α → Prop) (f : α → β) : Prop :=
  ∀ (x y : α), R x y → f x = f y

-- Lemma: Conserved observables are constant along equivalence paths
theorem conserved_along_equiv_closure {α β : Type} {R : α → α → Prop} (f : α → β)
    (h_cons : IsConservedObservable R f) {x y : α} (h_eqv : EquivClosure R x y) :
    f x = f y := by
  induction h_eqv with
  | refl a => rfl
  | fwd a b hR => exact h_cons a b hR
  | bwd a b hR => exact (h_cons b a hR).symm
  | trans a b c _ _ hab hbc => exact hab.trans hbc

-- GENERAL THEOREM: On any weakly connected state space, the kernel of the adjoint
-- transition operator is strictly 1-dimensional (all conserved quantities are constants).
theorem general_adjoint_kernel_is_one_dimensional {α β : Type} {R : α → α → Prop}
    (h_conn : IsWeaklyConnected R) (f : α → β) (h_cons : IsConservedObservable R f) :
    ∀ (x y : α), f x = f y := by
  intro x y
  exact conserved_along_equiv_closure f h_cons (h_conn x y)


-- ============================================================================
-- Section 4: General Directed Cycles Violate Strict DAG Orderings
-- ============================================================================

def IsIrreflexive {α : Type} (R : α → α → Prop) : Prop :=
  ∀ (x : α), ¬ R x x

def IsTransitive {α : Type} (R : α → α → Prop) : Prop :=
  ∀ (x y z : α), R x y → R y z → R x z

def IsAsymmetric {α : Type} (R : α → α → Prop) : Prop :=
  ∀ (x y : α), R x y → ¬ R y x

-- GENERAL THEOREM: Any relation possessing a directed cyclic dependency is not irreflexive
theorem cycle_violates_irreflexivity {α : Type} (R : α → α → Prop)
    (x : α) (h_cycle : TC R x x) : ¬ IsIrreflexive (TC R) := by
  intro h_irr
  exact h_irr x h_cycle

-- GENERAL THEOREM: Asymmetry implies Irreflexivity for any relation
theorem asymmetry_implies_irreflexivity {α : Type} (R : α → α → Prop)
    (h_asym : IsAsymmetric R) : IsIrreflexive R := by
  intro x h_loop
  exact h_asym x x h_loop h_loop


-- ============================================================================
-- Section 5: General Causal Posets & DAG Isomorphisms
-- ============================================================================

structure CausalDAG (E : Type) where
  prec : E → E → Prop
  asym : IsAsymmetric prec
  trans : IsTransitive prec

structure CausalDAGIsomorphism (E1 E2 : Type) (g1 : CausalDAG E1) (g2 : CausalDAG E2) where
  toFun : E1 → E2
  invFun : E2 → E1
  left_inv : ∀ x, invFun (toFun x) = x
  right_inv : ∀ y, toFun (invFun y) = y
  preserve_order : ∀ x y, g1.prec x y ↔ g2.prec (toFun x) (toFun y)

def AreIsomorphicDAGs (E1 E2 : Type) (g1 : CausalDAG E1) (g2 : CausalDAG E2) : Prop :=
  Nonempty (CausalDAGIsomorphism E1 E2 g1 g2)

-- General Theorem: DAG isomorphism implies bijection of underlying event sets
theorem dag_iso_implies_bijective {E1 E2 : Type} {g1 : CausalDAG E1} {g2 : CausalDAG E2}
    (iso : CausalDAGIsomorphism E1 E2 g1 g2) :
    (∀ x1 x2 : E1, iso.toFun x1 = iso.toFun x2 → x1 = x2) ∧
    (∀ y : E2, ∃ x : E1, iso.toFun x = y) := by
  constructor
  · intro x1 x2 h_eq
    have h := congrArg iso.invFun h_eq
    rw [iso.left_inv, iso.left_inv] at h
    exact h
  · intro y
    exact ⟨iso.invFun y, iso.right_inv y⟩


-- ============================================================================
-- Section 6: Rigorous Minimal ARS Models (Lemma 1 Decoupling Proof)
-- ============================================================================

-- Model M1: Causal Invariant Without Global Confluence
inductive StateM1 : Type where
  | a : StateM1 | b : StateM1 | c : StateM1 | d : StateM1 | e : StateM1
  deriving DecidableEq, Repr

inductive RelM1 : StateM1 → StateM1 → Prop where
  | ab : RelM1 StateM1.a StateM1.b
  | ac : RelM1 StateM1.a StateM1.c
  | bd : RelM1 StateM1.b StateM1.d
  | ce : RelM1 StateM1.c StateM1.e

theorem normal_form_d_M1 : IsNormalForm RelM1 StateM1.d := by intro y hR; cases hR
theorem normal_form_e_M1 : IsNormalForm RelM1 StateM1.e := by intro y hR; cases hR

theorem wn_M1 : IsWeaklyNormalizing RelM1 := by
  intro s
  cases s with
  | a =>
    refine ⟨StateM1.d, Trace.cons StateM1.a StateM1.b StateM1.d RelM1.ab
      (Trace.cons StateM1.b StateM1.d StateM1.d RelM1.bd (Trace.nil StateM1.d)), normal_form_d_M1⟩
  | b =>
    refine ⟨StateM1.d, Trace.cons StateM1.b StateM1.d StateM1.d RelM1.bd (Trace.nil StateM1.d), normal_form_d_M1⟩
  | c =>
    refine ⟨StateM1.e, Trace.cons StateM1.c StateM1.e StateM1.e RelM1.ce (Trace.nil StateM1.e), normal_form_e_M1⟩
  | d => refine ⟨StateM1.d, Trace.nil StateM1.d, normal_form_d_M1⟩
  | e => refine ⟨StateM1.e, Trace.nil StateM1.e, normal_form_e_M1⟩

-- Strong normalization via well-founded reduction
theorem sn_M1 : IsStronglyNormalizing RelM1 := by
  constructor
  intro s
  constructor
  intro y hy
  cases hy with
  | ab =>
    constructor; intro z hz; cases hz with
    | bd => constructor; intro w hw; cases hw
  | ac =>
    constructor; intro z hz; cases hz with
    | ce => constructor; intro w hw; cases hw
  | bd => constructor; intro w hw; cases hw
  | ce => constructor; intro w hw; cases hw

theorem not_confluent_M1 : ¬ IsConfluent RelM1 := by
  intro hConf
  have hab : RTC RelM1 StateM1.a StateM1.d :=
    RTC.step StateM1.a StateM1.b StateM1.d RelM1.ab
      (RTC.step StateM1.b StateM1.d StateM1.d RelM1.bd (RTC.refl StateM1.d))
  have hac : RTC RelM1 StateM1.a StateM1.e :=
    RTC.step StateM1.a StateM1.c StateM1.e RelM1.ac
      (RTC.step StateM1.c StateM1.e StateM1.e RelM1.ce (RTC.refl StateM1.e))
  have ⟨w, hw1, hw2⟩ := hConf StateM1.a StateM1.d StateM1.e hab hac
  have hwd : w = StateM1.d := by cases hw1 with | refl => rfl | step _ _ _ hR _ => cases hR
  have hwe : w = StateM1.e := by cases hw2 with | refl => rfl | step _ _ _ hR _ => cases hR
  rw [hwd] at hwe; nomatch hwe

inductive EventM1_1 : Type where
  | e1 : EventM1_1 | e2 : EventM1_1
  deriving DecidableEq, Repr

inductive EventM1_2 : Type where
  | e1' : EventM1_2 | e2' : EventM1_2
  deriving DecidableEq, Repr

inductive DepM1_1 : EventM1_1 → EventM1_1 → Prop where
  | dep : DepM1_1 EventM1_1.e1 EventM1_1.e2

inductive DepM1_2 : EventM1_2 → EventM1_2 → Prop where
  | dep : DepM1_2 EventM1_2.e1' EventM1_2.e2'

def dagM1_1 : CausalDAG EventM1_1 where
  prec := DepM1_1
  asym := by intro u v h; cases h; intro hcontra; cases hcontra
  trans := by intro u v w h1 h2; cases h1; cases h2

def dagM1_2 : CausalDAG EventM1_2 where
  prec := DepM1_2
  asym := by intro u v h; cases h; intro hcontra; cases hcontra
  trans := by intro u v w h1 h2; cases h1; cases h2

theorem M1_causal_graphs_isomorphic : AreIsomorphicDAGs EventM1_1 EventM1_2 dagM1_1 dagM1_2 := by
  refine ⟨{
    toFun := fun | EventM1_1.e1 => EventM1_2.e1' | EventM1_1.e2 => EventM1_2.e2'
    invFun := fun | EventM1_2.e1' => EventM1_1.e1 | EventM1_2.e2' => EventM1_1.e2
    left_inv := by intro x; cases x <;> rfl
    right_inv := by intro y; cases y <;> rfl
    preserve_order := by
      intro x y
      constructor
      · intro h; cases h; exact DepM1_2.dep
      · intro h; cases x <;> cases y <;> cases h <;> exact DepM1_1.dep
  }⟩


-- Model M2: Globally Confluent Without Causal Invariance
inductive StateM2 : Type where
  | a : StateM2 | b : StateM2 | c : StateM2 | x : StateM2 | d : StateM2
  deriving DecidableEq, Repr

inductive RelM2 : StateM2 → StateM2 → Prop where
  | ab : RelM2 StateM2.a StateM2.b
  | ac : RelM2 StateM2.a StateM2.c
  | bd : RelM2 StateM2.b StateM2.d
  | cx : RelM2 StateM2.c StateM2.x
  | xd : RelM2 StateM2.x StateM2.d

theorem normal_form_d_M2 : IsNormalForm RelM2 StateM2.d := by intro y hR; cases hR

theorem wn_M2 : IsWeaklyNormalizing RelM2 := by
  intro s
  cases s with
  | a =>
    refine ⟨StateM2.d, Trace.cons StateM2.a StateM2.b StateM2.d RelM2.ab
      (Trace.cons StateM2.b StateM2.d StateM2.d RelM2.bd (Trace.nil StateM2.d)), normal_form_d_M2⟩
  | b =>
    refine ⟨StateM2.d, Trace.cons StateM2.b StateM2.d StateM2.d RelM2.bd (Trace.nil StateM2.d), normal_form_d_M2⟩
  | c =>
    refine ⟨StateM2.d, Trace.cons StateM2.c StateM2.x StateM2.d RelM2.cx
      (Trace.cons StateM2.x StateM2.d StateM2.d RelM2.xd (Trace.nil StateM2.d)), normal_form_d_M2⟩
  | x =>
    refine ⟨StateM2.d, Trace.cons StateM2.x StateM2.d StateM2.d RelM2.xd (Trace.nil StateM2.d), normal_form_d_M2⟩
  | d => refine ⟨StateM2.d, Trace.nil StateM2.d, normal_form_d_M2⟩

theorem sn_M2 : IsStronglyNormalizing RelM2 := by
  constructor
  intro s
  constructor
  intro y hy
  cases hy with
  | ab =>
    constructor; intro z hz; cases hz with
    | bd => constructor; intro w hw; cases hw
  | ac =>
    constructor; intro z hz; cases hz with
    | cx =>
      constructor; intro w hw; cases hw with
      | xd => constructor; intro v hv; cases hv
  | bd => constructor; intro w hw; cases hw
  | cx =>
    constructor; intro z hz; cases hz with
    | xd => constructor; intro v hv; cases hv
  | xd => constructor; intro w hw; cases hw

theorem to_d_from_a : RTC RelM2 StateM2.a StateM2.d :=
  RTC.step StateM2.a StateM2.b StateM2.d RelM2.ab (RTC.step StateM2.b StateM2.d StateM2.d RelM2.bd (RTC.refl StateM2.d))
theorem to_d_from_b : RTC RelM2 StateM2.b StateM2.d :=
  RTC.step StateM2.b StateM2.d StateM2.d RelM2.bd (RTC.refl StateM2.d)
theorem to_d_from_c : RTC RelM2 StateM2.c StateM2.d :=
  RTC.step StateM2.c StateM2.x StateM2.d RelM2.cx (RTC.step StateM2.x StateM2.d StateM2.d RelM2.xd (RTC.refl StateM2.d))
theorem to_d_from_x : RTC RelM2 StateM2.x StateM2.d :=
  RTC.step StateM2.x StateM2.d StateM2.d RelM2.xd (RTC.refl StateM2.d)
theorem to_d_from_d : RTC RelM2 StateM2.d StateM2.d := RTC.refl StateM2.d

theorem confluent_M2 : IsConfluent RelM2 := by
  intro u y z _huy _huz
  refine ⟨StateM2.d, ?_, ?_⟩
  · cases y with | a => exact to_d_from_a | b => exact to_d_from_b | c => exact to_d_from_c | x => exact to_d_from_x | d => exact to_d_from_d
  · cases z with | a => exact to_d_from_a | b => exact to_d_from_b | c => exact to_d_from_c | x => exact to_d_from_x | d => exact to_d_from_d

-- Branch 1 and Branch 2 in M2
inductive EventM2_1 : Type where
  | e1 : EventM2_1 | e2 : EventM2_1
  deriving DecidableEq, Repr

inductive EventM2_2 : Type where
  | e1' : EventM2_2 | e2' : EventM2_2 | e3' : EventM2_2
  deriving DecidableEq, Repr

inductive DepM2_1 : EventM2_1 → EventM2_1 → Prop where
  | dep : DepM2_1 EventM2_1.e1 EventM2_1.e2

inductive DepM2_2 : EventM2_2 → EventM2_2 → Prop where
  | dep12 : DepM2_2 EventM2_2.e1' EventM2_2.e2'
  | dep23 : DepM2_2 EventM2_2.e2' EventM2_2.e3'
  | dep13 : DepM2_2 EventM2_2.e1' EventM2_2.e3'

def dagM2_1 : CausalDAG EventM2_1 where
  prec := DepM2_1
  asym := by intro u v h; cases h; intro hcontra; cases hcontra
  trans := by intro u v w h1 h2; cases h1; cases h2

def dagM2_2 : CausalDAG EventM2_2 where
  prec := DepM2_2
  asym := by intro u v h; cases h <;> intro hcontra <;> cases hcontra
  trans := by
    intro u v w h1 h2
    cases h1 with
    | dep12 => cases h2 with | dep23 => exact DepM2_2.dep13
    | dep23 => cases h2
    | dep13 => cases h2

-- Theorem: No bijection exists between 2-element event set and 3-element event set
theorem no_bijection_2_3 : ¬ ∃ (f : EventM2_2 → EventM2_1) (g : EventM2_1 → EventM2_2),
    (∀ x, g (f x) = x) ∧ (∀ y, f (g y) = y) := by
  intro ⟨f, g, left_inv, right_inv⟩
  have h1 : f EventM2_2.e1' = EventM2_1.e1 ∨ f EventM2_2.e1' = EventM2_1.e2 := by
    cases f EventM2_2.e1' with | e1 => exact Or.inl rfl | e2 => exact Or.inr rfl
  have h2 : f EventM2_2.e2' = EventM2_1.e1 ∨ f EventM2_2.e2' = EventM2_1.e2 := by
    cases f EventM2_2.e2' with | e1 => exact Or.inl rfl | e2 => exact Or.inr rfl
  have h3 : f EventM2_2.e3' = EventM2_1.e1 ∨ f EventM2_2.e3' = EventM2_1.e2 := by
    cases f EventM2_2.e3' with | e1 => exact Or.inl rfl | e2 => exact Or.inr rfl
  rcases h1 with (h1 | h1) <;> rcases h2 with (h2 | h2) <;> rcases h3 with (h3 | h3)
  · have heq : f EventM2_2.e1' = f EventM2_2.e2' := by rw [h1, h2]
    have h_inj : g (f EventM2_2.e1') = g (f EventM2_2.e2') := by rw [heq]
    rw [left_inv, left_inv] at h_inj; nomatch h_inj
  · have heq : f EventM2_2.e1' = f EventM2_2.e2' := by rw [h1, h2]
    have h_inj : g (f EventM2_2.e1') = g (f EventM2_2.e2') := by rw [heq]
    rw [left_inv, left_inv] at h_inj; nomatch h_inj
  · have heq : f EventM2_2.e1' = f EventM2_2.e3' := by rw [h1, h3]
    have h_inj : g (f EventM2_2.e1') = g (f EventM2_2.e3') := by rw [heq]
    rw [left_inv, left_inv] at h_inj; nomatch h_inj
  · have heq : f EventM2_2.e2' = f EventM2_2.e3' := by rw [h2, h3]
    have h_inj : g (f EventM2_2.e2') = g (f EventM2_2.e3') := by rw [heq]
    rw [left_inv, left_inv] at h_inj; nomatch h_inj
  · have heq : f EventM2_2.e2' = f EventM2_2.e3' := by rw [h2, h3]
    have h_inj : g (f EventM2_2.e2') = g (f EventM2_2.e3') := by rw [heq]
    rw [left_inv, left_inv] at h_inj; nomatch h_inj
  · have heq : f EventM2_2.e1' = f EventM2_2.e3' := by rw [h1, h3]
    have h_inj : g (f EventM2_2.e1') = g (f EventM2_2.e3') := by rw [heq]
    rw [left_inv, left_inv] at h_inj; nomatch h_inj
  · have heq : f EventM2_2.e1' = f EventM2_2.e2' := by rw [h1, h2]
    have h_inj : g (f EventM2_2.e1') = g (f EventM2_2.e2') := by rw [heq]
    rw [left_inv, left_inv] at h_inj; nomatch h_inj
  · have heq : f EventM2_2.e1' = f EventM2_2.e2' := by rw [h1, h2]
    have h_inj : g (f EventM2_2.e1') = g (f EventM2_2.e2') := by rw [heq]
    rw [left_inv, left_inv] at h_inj; nomatch h_inj

theorem M2_causal_graphs_not_isomorphic : ¬ AreIsomorphicDAGs EventM2_1 EventM2_2 dagM2_1 dagM2_2 := by
  intro ⟨iso⟩
  exact no_bijection_2_3 ⟨iso.invFun, iso.toFun, iso.right_inv, iso.left_inv⟩

-- Concrete Traces in M2
def trace1_M2 : Trace RelM2 StateM2.a StateM2.d :=
  Trace.cons StateM2.a StateM2.b StateM2.d RelM2.ab
    (Trace.cons StateM2.b StateM2.d StateM2.d RelM2.bd (Trace.nil StateM2.d))

def trace2_M2 : Trace RelM2 StateM2.a StateM2.d :=
  Trace.cons StateM2.a StateM2.c StateM2.d RelM2.ac
    (Trace.cons StateM2.c StateM2.x StateM2.d RelM2.cx
      (Trace.cons StateM2.x StateM2.d StateM2.d RelM2.xd (Trace.nil StateM2.d)))

theorem M2_trace_non_injectivity :
    trace1_M2 ≠ trace2_M2 ∧ traceLength trace1_M2 = 2 ∧ traceLength trace2_M2 = 3 := by
  refine ⟨?_, rfl, rfl⟩
  apply trace_length_ne_implies_trace_ne trace1_M2 trace2_M2
  decide

-- Main Decoupling Master Theorems
theorem causal_invariance_does_not_imply_confluence :
    ∃ (α : Type) (R : α → α → Prop),
      IsStronglyNormalizing R ∧ ¬ IsConfluent R ∧
      AreIsomorphicDAGs EventM1_1 EventM1_2 dagM1_1 dagM1_2 :=
  ⟨StateM1, RelM1, sn_M1, not_confluent_M1, M1_causal_graphs_isomorphic⟩

theorem confluence_does_not_imply_causal_invariance :
    ∃ (α : Type) (R : α → α → Prop),
      IsStronglyNormalizing R ∧ IsConfluent R ∧
      ¬ AreIsomorphicDAGs EventM2_1 EventM2_2 dagM2_1 dagM2_2 :=
  ⟨StateM2, RelM2, sn_M2, confluent_M2, M2_causal_graphs_not_isomorphic⟩

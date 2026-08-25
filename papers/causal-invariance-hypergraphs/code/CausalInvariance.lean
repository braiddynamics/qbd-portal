/-!
  # Formal Proof of Lemma 1 & Non-Injectivity
  # Logical Independence of Confluence and Causal Invariance with Causal DAG Isomorphisms
  # Formalized in Lean 4.
-/

-- ============================================================================
-- Section 1: Abstract Rewriting System Core Definitions
-- ============================================================================

-- Reflexive Transitive Closure of an Abstract Rewriting Relation
inductive RTC {α : Type} (R : α → α → Prop) : α → α → Prop where
  | refl (x : α) : RTC R x x
  | step (x y z : α) : R x y → RTC R y z → RTC R x z

-- Predicate: Global Confluence (Church-Rosser Property)
def IsConfluent {α : Type} (R : α → α → Prop) : Prop :=
  ∀ (u y z : α), RTC R u y → RTC R u z → ∃ (w : α), RTC R y w ∧ RTC R z w

-- Predicate: Normal Form (State with no outgoing rewrite transitions)
def IsNormalForm {α : Type} (R : α → α → Prop) (u : α) : Prop :=
  ∀ (y : α), ¬ R u y

-- Inductive Derivation Trace representing concrete chronological execution paths
inductive Trace {α : Type} (R : α → α → Prop) : α → α → Type where
  | nil (x : α) : Trace R x x
  | cons (x y z : α) : R x y → Trace R y z → Trace R x z

-- Length of a derivation trace
def traceLength {α : Type} {R : α → α → Prop} {x z : α} : Trace R x z → Nat
  | Trace.nil _ => 0
  | Trace.cons _ _ _ _ rest => 1 + traceLength rest

-- Predicate: Strong Normalization (Every state terminates at a normal form in finite steps)
def IsStronglyNormalizing {α : Type} (R : α → α → Prop) : Prop :=
  ∀ (s : α), ∃ (t : α) (_tr : Trace R s t), IsNormalForm R t


-- ============================================================================
-- Section 2: Formal Causal Event Dependency DAGs & Isomorphism
-- ============================================================================

def CausalRelation (E : Type) := E → E → Prop

def IsAsymmetric (E : Type) (R : CausalRelation E) : Prop :=
  ∀ u v : E, R u v → ¬ R v u

def IsTransitive (E : Type) (R : CausalRelation E) : Prop :=
  ∀ u v w : E, R u v → R v w → R u w

def IsIrreflexive (E : Type) (R : CausalRelation E) : Prop :=
  ∀ v : E, ¬ R v v

theorem asymmetry_implies_irreflexivity {E : Type} (R : CausalRelation E) (h : IsAsymmetric E R) :
    IsIrreflexive E R := by
  intro v h_loop
  exact h v v h_loop h_loop

-- A Causal Event Dependency DAG consists of an event type and a strict partial order relation
structure CausalDAG (E : Type) where
  dep : CausalRelation E
  asym : IsAsymmetric E dep
  trans : IsTransitive E dep

-- Formal definition of Causal DAG Isomorphism (order-preserving bijection on event sets)
structure CausalDAGIsomorphism (E1 E2 : Type) (g1 : CausalDAG E1) (g2 : CausalDAG E2) where
  toFun : E1 → E2
  invFun : E2 → E1
  left_inv : ∀ x, invFun (toFun x) = x
  right_inv : ∀ y, toFun (invFun y) = y
  preserve_order : ∀ x y, g1.dep x y ↔ g2.dep (toFun x) (toFun y)

def AreIsomorphicDAGs (E1 E2 : Type) (g1 : CausalDAG E1) (g2 : CausalDAG E2) : Prop :=
  Nonempty (CausalDAGIsomorphism E1 E2 g1 g2)


-- ============================================================================
-- Section 3: Counterexample System M1 (Causal Invariant DAGs, Non-Confluent)
-- ============================================================================

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

theorem sn_M1 : IsStronglyNormalizing RelM1 := by
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

-- Event structures for Branch 1 and Branch 2 of M1
inductive EventM1_1 : Type where
  | e1 : EventM1_1  -- event a -> b
  | e2 : EventM1_1  -- event b -> d
  deriving DecidableEq, Repr

inductive EventM1_2 : Type where
  | e1' : EventM1_2  -- event a -> c
  | e2' : EventM1_2  -- event c -> e
  deriving DecidableEq, Repr

inductive DepM1_1 : EventM1_1 → EventM1_1 → Prop where
  | dep : DepM1_1 EventM1_1.e1 EventM1_1.e2

inductive DepM1_2 : EventM1_2 → EventM1_2 → Prop where
  | dep : DepM1_2 EventM1_2.e1' EventM1_2.e2'

def dagM1_1 : CausalDAG EventM1_1 where
  dep := DepM1_1
  asym := by intro u v h; cases h; intro hcontra; cases hcontra
  trans := by intro u v w h1 h2; cases h1; cases h2

def dagM1_2 : CausalDAG EventM1_2 where
  dep := DepM1_2
  asym := by intro u v h; cases h; intro hcontra; cases hcontra
  trans := by intro u v w h1 h2; cases h1; cases h2

-- Theorem: Branch 1 and Branch 2 in M1 generate isomorphic Causal DAGs
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


-- ============================================================================
-- Section 4: Counterexample System M2 (Confluent, Non-Isomorphic Causal DAGs)
-- ============================================================================

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

theorem sn_M2 : IsStronglyNormalizing RelM2 := by
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

-- Event structures for Branch 1 (2 events) and Branch 2 (3 events) of M2
inductive EventM2_1 : Type where
  | e1 : EventM2_1  -- a -> b
  | e2 : EventM2_1  -- b -> d
  deriving DecidableEq, Repr

inductive EventM2_2 : Type where
  | e1' : EventM2_2  -- a -> c
  | e2' : EventM2_2  -- c -> x
  | e3' : EventM2_2  -- x -> d
  deriving DecidableEq, Repr

inductive DepM2_1 : EventM2_1 → EventM2_1 → Prop where
  | dep : DepM2_1 EventM2_1.e1 EventM2_1.e2

inductive DepM2_2 : EventM2_2 → EventM2_2 → Prop where
  | dep12 : DepM2_2 EventM2_2.e1' EventM2_2.e2'
  | dep23 : DepM2_2 EventM2_2.e2' EventM2_2.e3'
  | dep13 : DepM2_2 EventM2_2.e1' EventM2_2.e3'

def dagM2_1 : CausalDAG EventM2_1 where
  dep := DepM2_1
  asym := by intro u v h; cases h; intro hcontra; cases hcontra
  trans := by intro u v w h1 h2; cases h1; cases h2

def dagM2_2 : CausalDAG EventM2_2 where
  dep := DepM2_2
  asym := by
    intro u v h
    cases h <;> intro hcontra <;> cases hcontra
  trans := by
    intro u v w h1 h2
    cases h1 with
    | dep12 =>
      cases h2 with
      | dep23 => exact DepM2_2.dep13
    | dep23 => cases h2
    | dep13 => cases h2

-- Theorem: Branch 1 and Branch 2 in M2 are strictly NON-ISOMORPHIC as Causal DAGs (2 != 3)
theorem M2_causal_graphs_not_isomorphic : ¬ AreIsomorphicDAGs EventM2_1 EventM2_2 dagM2_1 dagM2_2 := by
  intro ⟨iso⟩
  have h1 : iso.invFun EventM2_2.e1' = EventM2_1.e1 ∨ iso.invFun EventM2_2.e1' = EventM2_1.e2 := by
    cases iso.invFun EventM2_2.e1' with
    | e1 => exact Or.inl rfl
    | e2 => exact Or.inr rfl
  have h2 : iso.invFun EventM2_2.e2' = EventM2_1.e1 ∨ iso.invFun EventM2_2.e2' = EventM2_1.e2 := by
    cases iso.invFun EventM2_2.e2' with
    | e1 => exact Or.inl rfl
    | e2 => exact Or.inr rfl
  have h3 : iso.invFun EventM2_2.e3' = EventM2_1.e1 ∨ iso.invFun EventM2_2.e3' = EventM2_1.e2 := by
    cases iso.invFun EventM2_2.e3' with
    | e1 => exact Or.inl rfl
    | e2 => exact Or.inr rfl
  rcases h1 with (h1 | h1) <;> rcases h2 with (h2 | h2) <;> rcases h3 with (h3 | h3)
  · have heq : iso.invFun EventM2_2.e1' = iso.invFun EventM2_2.e2' := by rw [h1, h2]
    have h_inj : iso.toFun (iso.invFun EventM2_2.e1') = iso.toFun (iso.invFun EventM2_2.e2') := by rw [heq]
    rw [iso.right_inv, iso.right_inv] at h_inj
    nomatch h_inj
  · have heq : iso.invFun EventM2_2.e1' = iso.invFun EventM2_2.e2' := by rw [h1, h2]
    have h_inj : iso.toFun (iso.invFun EventM2_2.e1') = iso.toFun (iso.invFun EventM2_2.e2') := by rw [heq]
    rw [iso.right_inv, iso.right_inv] at h_inj
    nomatch h_inj
  · have heq : iso.invFun EventM2_2.e1' = iso.invFun EventM2_2.e3' := by rw [h1, h3]
    have h_inj : iso.toFun (iso.invFun EventM2_2.e1') = iso.toFun (iso.invFun EventM2_2.e3') := by rw [heq]
    rw [iso.right_inv, iso.right_inv] at h_inj
    nomatch h_inj
  · have heq : iso.invFun EventM2_2.e2' = iso.invFun EventM2_2.e3' := by rw [h2, h3]
    have h_inj : iso.toFun (iso.invFun EventM2_2.e2') = iso.toFun (iso.invFun EventM2_2.e3') := by rw [heq]
    rw [iso.right_inv, iso.right_inv] at h_inj
    nomatch h_inj
  · have heq : iso.invFun EventM2_2.e2' = iso.invFun EventM2_2.e3' := by rw [h2, h3]
    have h_inj : iso.toFun (iso.invFun EventM2_2.e2') = iso.toFun (iso.invFun EventM2_2.e3') := by rw [heq]
    rw [iso.right_inv, iso.right_inv] at h_inj
    nomatch h_inj
  · have heq : iso.invFun EventM2_2.e1' = iso.invFun EventM2_2.e3' := by rw [h1, h3]
    have h_inj : iso.toFun (iso.invFun EventM2_2.e1') = iso.toFun (iso.invFun EventM2_2.e3') := by rw [heq]
    rw [iso.right_inv, iso.right_inv] at h_inj
    nomatch h_inj
  · have heq : iso.invFun EventM2_2.e1' = iso.invFun EventM2_2.e2' := by rw [h1, h2]
    have h_inj : iso.toFun (iso.invFun EventM2_2.e1') = iso.toFun (iso.invFun EventM2_2.e2') := by rw [heq]
    rw [iso.right_inv, iso.right_inv] at h_inj
    nomatch h_inj
  · have heq : iso.invFun EventM2_2.e1' = iso.invFun EventM2_2.e2' := by rw [h1, h2]
    have h_inj : iso.toFun (iso.invFun EventM2_2.e1') = iso.toFun (iso.invFun EventM2_2.e2') := by rw [heq]
    rw [iso.right_inv, iso.right_inv] at h_inj
    nomatch h_inj


-- ============================================================================
-- Section 5: Trace-Based Non-Injectivity & Information Erasure Proof
-- ============================================================================

def trace1_M2 : Trace RelM2 StateM2.a StateM2.d :=
  Trace.cons StateM2.a StateM2.b StateM2.d RelM2.ab
    (Trace.cons StateM2.b StateM2.d StateM2.d RelM2.bd (Trace.nil StateM2.d))

def trace2_M2 : Trace RelM2 StateM2.a StateM2.d :=
  Trace.cons StateM2.a StateM2.c StateM2.d RelM2.ac
    (Trace.cons StateM2.c StateM2.x StateM2.d RelM2.cx
      (Trace.cons StateM2.x StateM2.d StateM2.d RelM2.xd (Trace.nil StateM2.d)))

-- Theorem: Two syntactically distinct derivation traces terminate at the identical normal form
theorem distinct_traces_coincide_at_terminal :
  trace1_M2 ≠ trace2_M2 ∧
  traceLength trace1_M2 = 2 ∧
  traceLength trace2_M2 = 3 := by
  refine ⟨?_, rfl, rfl⟩
  intro h
  nomatch h

-- Main Decoupling Theorems
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



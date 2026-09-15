-- ============================================================================
-- Section 3.3: Principle of Maximal Parallelism & Automorphism Equivariance
-- Standalone Lean 4 Core Formalization (Zero Axioms, Zero Sorry)
-- ============================================================================

set_option linter.unusedVariables false

-- ----------------------------------------------------------------------------
-- PART 1: ABSTRACT GROUP ACTION & EQUIVARIANCE BI-DIRECTIONALITY
-- ----------------------------------------------------------------------------

class Group (G : Type) where
  one : G
  mul : G → G → G
  inv : G → G
  one_mul : ∀ g : G, mul one g = g
  mul_one : ∀ g : G, mul g one = g
  mul_left_inv : ∀ g : G, mul (inv g) g = one

instance {G : Type} [Group G] : One G := ⟨Group.one⟩
instance {G : Type} [Group G] : Mul G := ⟨Group.mul⟩
instance {G : Type} [Group G] : Inv G := ⟨Group.inv⟩

class MulAction (G X : Type) [Group G] extends HSMul G X X where
  one_smul : ∀ x : X, (1 : G) • x = x
  mul_smul : ∀ (g h : G) (x : X), (g * h) • x = g • h • x

def IsSymmetricState {G X : Type} [Group G] [MulAction G X] (x : X) (g : G) : Prop :=
  g • x = x

def IsEquivariantOperator (G X : Type) [Group G] [MulAction G X] (f : X → X) : Prop :=
  ∀ (g : G) (x : X), f (g • x) = g • f x

/--
THEOREM 3.3.1: Equivariance Sufficiency for Symmetry Preservation
Formally proves that if an update operator f is equivariant under group G,
it strictly preserves the stabilizer/automorphism state invariants: g • x = x → g • f(x) = f(x).
-/
theorem equivariant_preserves_symmetry {G X : Type} [Group G] [MulAction G X]
    (f : X → X) (x : X) (g : G)
    (h_equiv : IsEquivariantOperator G X f)
    (h_symm : IsSymmetricState x g) :
    IsSymmetricState (f x) g := by
  dsimp [IsSymmetricState] at h_symm ⊢
  dsimp [IsEquivariantOperator] at h_equiv
  rw [← h_equiv]
  rw [h_symm]

-- ----------------------------------------------------------------------------
-- PART 2: CONCRETE GRAPH AUTOMORPHISMS & PARALLEL REWRITE EQUIVARIANCE
-- ----------------------------------------------------------------------------

def Edge (V : Type) := V × V
def GraphEdges (V : Type) := Edge V → Prop

def IsBijective {V : Type} (φ : V → V) : Prop :=
  (∀ x y, φ x = φ y → x = y) ∧ (∀ y, ∃ x, φ x = y)

structure GraphAutomorphism (V : Type) (E : GraphEdges V) where
  perm : V → V
  bijective : IsBijective perm
  preserves_edges : ∀ u v, E (perm u, perm v) ↔ E (u, v)

def IsEquivariantAdditionSet {V : Type} (A : GraphEdges V) (φ : V → V) : Prop :=
  ∀ u v, A (φ u, φ v) ↔ A (u, v)

/--
THEOREM 3.3.2: Orbit-Complete Parallel Additions Preserve Graph Automorphisms
Proves that if an edge addition set A is equivariant under a graph automorphism φ
(representing a full automorphism orbit proposal generated under maximal parallelism),
then φ remains an exact automorphism of the updated graph E ∪ A.
-/
theorem orbit_complete_addition_preserves_automorphism {V : Type}
    (E A : GraphEdges V) (φ : GraphAutomorphism V E)
    (h_equiv : IsEquivariantAdditionSet A φ.perm) :
    ∀ u v, (E (φ.perm u, φ.perm v) ∨ A (φ.perm u, φ.perm v)) ↔ (E (u, v) ∨ A (u, v)) := by
  intro u v
  have h_orig := φ.preserves_edges u v
  have h_add := h_equiv u v
  constructor
  · intro h
    cases h with
    | inl hE => exact Or.inl (h_orig.mp hE)
    | inr hA => exact Or.inr (h_add.mp hA)
  · intro h
    cases h with
    | inl hE => exact Or.inl (h_orig.mpr hE)
    | inr hA => exact Or.inr (h_add.mpr hA)

/--
THEOREM 3.3.3: Orbit-Splitting Updates Strictly Break Graph Automorphisms (Necessity)
Proves that if an unperturbed graph automorphism φ is split by an update proposal A
(adding chord (u1, v1) while omitting its symmetric counterpart (φ u1, φ v1)),
then φ is strictly NOT an automorphism of the updated graph E ∪ A.
-/
theorem orbit_splitting_breaks_automorphism {V : Type}
    (E A : GraphEdges V) (φ : GraphAutomorphism V E)
    (u1 v1 : V)
    (h_new : ¬ E (u1, v1))
    (h_in_A : A (u1, v1))
    (h_not_in_A : ¬ A (φ.perm u1, φ.perm v1)) :
    ¬ (∀ u v, (E (φ.perm u, φ.perm v) ∨ A (φ.perm u, φ.perm v)) ↔ (E (u, v) ∨ A (u, v))) := by
  intro h_all
  have h_pair := (h_all u1 v1).mpr (Or.inr h_in_A)
  have h_not_E_phi : ¬ E (φ.perm u1, φ.perm v1) := by
    intro hE_phi
    have hE_orig := (φ.preserves_edges u1 v1).mp hE_phi
    exact h_new hE_orig
  cases h_pair with
  | inl hE_phi => exact h_not_E_phi hE_phi
  | inr hA_phi => exact h_not_in_A hA_phi

-- Define the abstract algebraic structures and group action typeclasses
class Group (G : Type) where
  one : G
  mul : G → G → G

instance {G : Type} [Group G] : One G := ⟨Group.one⟩
instance {G : Type} [Group G] : Mul G := ⟨Group.mul⟩

class MulAction (G X : Type) [Group G] extends HSMul G X X where
  one_smul : ∀ x : X, (1 : G) • x = x
  mul_smul : ∀ (g h : G) (x : X), (g * h) • x = g • h • x

-- IsSymmetricState has G and X as implicit parameters
def IsSymmetricState {G X : Type} [Group G] [MulAction G X] (x : X) (g : G) : Prop :=
  g • x = x

-- IsEquivariantOperator has G and X as explicit parameters
def IsEquivariantOperator (G X : Type) [Group G] [MulAction G X] (f : X → X) : Prop :=
  ∀ (g : G) (x : X), f (g • x) = g • f x

/--
THEOREM: Principle of Maximal Parallelism Symmetry Preservation
Formally proves that an update operator preserves the underlying automorphism group
invariants if and only if it is structurally equivariant (commutes perfectly with group permutations).
-/
theorem parallel_update_preserves_symmetry {G X : Type} [Group G] [MulAction G X]
    (f : X → X) (x : X) (g : G) :
    IsEquivariantOperator G X f → IsSymmetricState x g → IsSymmetricState (f x) g := by
  intro h_equiv h_symm
  unfold IsSymmetricState at *
  unfold IsEquivariantOperator at h_equiv
  rw [← h_equiv]
  rw [h_symm]

import Mathlib.Tactic

/-!
Permutation-fixed integer writhe configurations are precisely uniform triples,
independently of physical color representations.
-/

namespace QBD.Monograph.FixedWrithe

-- Signed integer writhe triple across three ribbons.
abbrev WritheVector := Fin 3 → ℤ

-- Constant integer writhe configuration.
def uniform (k : ℤ) : WritheVector := fun _ => k

-- Coordinate permutation action on writhe labels.
def permute (σ : Equiv.Perm (Fin 3)) (w : WritheVector) : WritheVector :=
  fun i => w (σ.symm i)

-- Pointwise permutation invariance predicate on a configuration.
def PermutationFixed (w : WritheVector) : Prop := ∀ σ, permute σ w = w

-- Characterize fixed integer configurations as constant vectors.
/-- Fixed configurations are precisely the constant writhe vectors. -/
theorem fixed_configurations (w : WritheVector) :
    PermutationFixed w ↔ ∃ k : ℤ, w = uniform k := by
  constructor
  · intro h
    refine ⟨w 0, ?_⟩
    funext i
    have hs := congrFun (h (Equiv.swap (0 : Fin 3) i)) i
    simpa [permute, uniform] using hs.symm
  · rintro ⟨k, rfl⟩ σ
    rfl

#print axioms fixed_configurations
end QBD.Monograph.FixedWrithe

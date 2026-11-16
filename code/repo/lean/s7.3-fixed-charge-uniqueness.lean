import Mathlib.Tactic

/-!
A permutation-fixed integer writhe configuration is uniquely determined by its
rational electric charge value.
-/

namespace QBD.Monograph.ChargeUniqueness

-- Signed integer writhe triple across three ribbons.
abbrev WritheVector := Fin 3 → ℤ

-- Normalized rational electric charge sum over three ribbons.
def charge (w : WritheVector) : ℚ := (∑ i, (w i : ℚ)) / 3

-- Constant integer writhe configuration.
def uniform (k : ℤ) : WritheVector := fun _ => k

-- Coordinate permutation action on writhe labels.
def permute (σ : Equiv.Perm (Fin 3)) (w : WritheVector) : WritheVector :=
  fun i => w (σ.symm i)

-- Pointwise permutation invariance predicate on a configuration.
def PermutationFixed (w : WritheVector) : Prop := ∀ σ, permute σ w = w

-- Characterize fixed writhe configurations as uniform triples.
/-- Every permutation-fixed writhe vector is constant. -/
theorem fixed_iff_uniform (w : WritheVector) :
    PermutationFixed w ↔ ∃ k : ℤ, w = uniform k := by
  constructor
  · intro h
    refine ⟨w 0, ?_⟩
    funext i
    have hs := congrFun (h (Equiv.swap (0 : Fin 3) i)) i
    simpa [permute, uniform] using hs.symm
  · rintro ⟨k, rfl⟩ σ
    rfl

-- Compute the charge of a constant integer triple.
/-- A uniform triple (k, k, k) carries charge k. -/
theorem charge_uniform (k : ℤ) : charge (uniform k) = k := by
  norm_num [charge, uniform, Fin.sum_univ_succ]

-- Relate the fixed-configuration predicate to its specified integer charge.
/-- A fixed label of integer charge k is exactly the constant vector k. -/
theorem fixed_charge (w : WritheVector) (k : ℤ) :
    (PermutationFixed w ∧ charge w = k) ↔ w = uniform k := by
  constructor
  · rintro ⟨hfixed, hcharge⟩
    obtain ⟨a, rfl⟩ := (fixed_iff_uniform w).mp hfixed
    have heq : (a : ℚ) = (k : ℚ) := by simpa [charge_uniform] using hcharge
    have hak : a = k := by exact_mod_cast heq
    subst a
    rfl
  · intro h
    subst w
    exact ⟨(fixed_iff_uniform (uniform k)).mpr ⟨k, rfl⟩, charge_uniform k⟩

#print axioms fixed_charge
end QBD.Monograph.ChargeUniqueness

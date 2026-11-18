import Mathlib.Tactic

/-!
Under the explicit complexity cutoff C ≤ 3, permutation-fixed writhe labels are
restricted to uniform configurations carrying charges -1, 0, or 1.
-/

namespace QBD.Monograph.LowComplexity

-- Signed integer writhe triple across three ribbons.
abbrev WritheVector := Fin 3 → ℤ

-- Normalized rational electric charge sum over three ribbons.
def charge (w : WritheVector) : ℚ := (∑ i, (w i : ℚ)) / 3

-- Absolute-writhe complexity measure across three ribbons.
def complexity (w : WritheVector) : ℤ := ∑ i, |w i|

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

-- Compute the complexity of a constant integer triple.
/-- A uniform triple (k, k, k) has complexity 3 * |k|. -/
theorem complexity_uniform (k : ℤ) : complexity (uniform k) = 3 * |k| := by
  simp [complexity, uniform]

-- Keep the complexity cutoff visible as an explicit hypothesis.
/-- Fixed labels below the stated cutoff have the three selected charges. -/
theorem selected_charges (w : WritheVector) (hf : PermutationFixed w)
    (hc : complexity w ≤ 3) : charge w = -1 ∨ charge w = 0 ∨ charge w = 1 := by
  obtain ⟨k, rfl⟩ := (fixed_iff_uniform w).mp hf
  have hc' : 3 * |k| ≤ 3 := by simpa [complexity_uniform] using hc
  have ha : |k| ≤ 1 := by omega
  have bounds := abs_le.mp ha
  have hk : k = -1 ∨ k = 0 ∨ k = 1 := by omega
  rcases hk with hk | hk | hk <;> subst k <;> norm_num [charge_uniform]

#print axioms selected_charges
end QBD.Monograph.LowComplexity

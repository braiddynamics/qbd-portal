import Mathlib.Tactic
import Mathlib.Data.Complex.Basic
import Mathlib.LinearAlgebra.Matrix.Notation

/-!
Accepted charge definition on integer writhe labels. PermutationFixed is a
predicate on individual configurations, not the invariant subspace of the
quantum permutation representation and not a physical SU(3) classification.
The diagonal actions below are pointwise algebra on amplitudes; no Hilbert
operator domain or microscopic graph identification is asserted.
-/

namespace QBD.IntegerWritheCharge

abbrev WritheVector := Fin 3 → ℤ

def charge (w : WritheVector) : ℚ := (∑ i, (w i : ℚ)) / 3

def complexity (w : WritheVector) : ℤ := ∑ i, |w i|

def uniform (k : ℤ) : WritheVector := fun _ => k

def permute (σ : Equiv.Perm (Fin 3)) (w : WritheVector) : WritheVector :=
  fun i => w (σ.symm i)

def PermutationFixed (w : WritheVector) : Prop := ∀ σ, permute σ w = w

def electron : WritheVector := uniform (-1)
def asymmetric : WritheVector := ![-2, -1, 0]
def downLabel : WritheVector := ![-1, 0, 0]
def upLabel : WritheVector := ![1, 1, 0]

def parity (w : WritheVector) (i : Fin 3) : ℤ :=
  if w i % 2 = 0 then 1 else -1

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

theorem charge_uniform (k : ℤ) : charge (uniform k) = k := by
  norm_num [charge, uniform, Fin.sum_univ_succ]

theorem complexity_uniform (k : ℤ) : complexity (uniform k) = 3 * |k| := by
  simp [complexity, uniform]

theorem fixed_charge_iff_uniform (w : WritheVector) (k : ℤ) :
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

theorem unique_fixed_charge_minus_one (w : WritheVector)
    (hfixed : PermutationFixed w) (hcharge : charge w = -1) : w = electron := by
  exact (fixed_charge_iff_uniform w (-1)).mp ⟨hfixed, hcharge⟩

theorem charge_permute (σ : Equiv.Perm (Fin 3)) (w : WritheVector) :
    charge (permute σ w) = charge w := by
  unfold charge permute
  rw [Equiv.sum_comp σ.symm (fun i => (w i : ℚ))]

theorem neutral_label_charge : charge (uniform 0) = 0 := by norm_num [charge_uniform]
theorem down_label_charge : charge downLabel = -(1 / 3 : ℚ) := by
  norm_num [charge, downLabel, Fin.sum_univ_succ]
theorem up_label_charge : charge upLabel = (2 / 3 : ℚ) := by
  norm_num [charge, upLabel, Fin.sum_univ_succ]
theorem electron_charge : charge electron = -1 := by simp [electron, charge_uniform]
theorem asymmetric_charge : charge asymmetric = -1 := by
  norm_num [charge, asymmetric, Fin.sum_univ_succ]

theorem asymmetric_not_fixed : ¬PermutationFixed asymmetric := by
  intro h
  obtain ⟨k, hk⟩ := (fixed_iff_uniform asymmetric).mp h
  have hzero := congrFun hk 0
  have hone := congrFun hk 1
  norm_num [asymmetric, uniform] at hzero hone
  omega

theorem complexity_tie : complexity electron = 3 ∧ complexity asymmetric = 3 := by
  norm_num [complexity, electron, uniform, asymmetric, Fin.sum_univ_succ]

theorem not_fixed_of_distinct_entries (w : WritheVector) (i j : Fin 3)
    (hij : w i ≠ w j) : ¬PermutationFixed w := by
  intro h
  obtain ⟨k, hk⟩ := (fixed_iff_uniform w).mp h
  apply hij
  rw [hk]
  rfl

theorem down_label_not_fixed : ¬PermutationFixed downLabel := by
  apply not_fixed_of_distinct_entries downLabel 0 1
  norm_num [downLabel]

theorem up_label_not_fixed : ¬PermutationFixed upLabel := by
  apply not_fixed_of_distinct_entries upLabel 0 (Fin.succ (Fin.succ 0))
  decide

theorem low_complexity_fixed_charge (w : WritheVector)
    (hf : PermutationFixed w) (hc : complexity w ≤ 3) :
    charge w = -1 ∨ charge w = 0 ∨ charge w = 1 := by
  obtain ⟨k, rfl⟩ := (fixed_iff_uniform w).mp hf
  have hc' : 3 * |k| ≤ 3 := by simpa [complexity_uniform] using hc
  have ha : |k| ≤ 1 := by omega
  have bounds := abs_le.mp ha
  have hk : k = -1 ∨ k = 0 ∨ k = 1 := by omega
  rcases hk with hk | hk | hk <;> subst k <;> norm_num [charge_uniform]

theorem first_parity_distinguishes_labels : parity electron 0 ≠ parity asymmetric 0 := by
  norm_num [parity, electron, uniform, asymmetric]

theorem total_parity_same :
    (∏ i, parity electron i) = -1 ∧ (∏ i, parity asymmetric i) = -1 := by
  norm_num [parity, electron, uniform, asymmetric, Fin.prod_univ_succ]

theorem fixed_charge_support_unique (ψ : WritheVector → ℂ)
    (hsupport : ∀ w, ψ w ≠ 0 → PermutationFixed w ∧ charge w = -1)
    (w : WritheVector) (hne : w ≠ electron) : ψ w = 0 := by
  by_contra hnonzero
  obtain ⟨hf, hq⟩ := hsupport w hnonzero
  exact hne (unique_fixed_charge_minus_one w hf hq)

theorem asymmetric_injective : Function.Injective asymmetric := by
  intro i j hij
  fin_cases i <;> fin_cases j <;> norm_num [asymmetric] at *

theorem orbit_labels_injective : Function.Injective (fun σ => permute σ asymmetric) := by
  intro σ τ h
  have hinverse : σ.symm = τ.symm := by
    apply Equiv.ext
    intro i
    apply asymmetric_injective
    exact congrFun h i
  have hdouble := congrArg (fun e : Equiv.Perm (Fin 3) => e.symm) hinverse
  simpa using hdouble

theorem orbit_labels_not_fixed (σ : Equiv.Perm (Fin 3)) :
    ¬PermutationFixed (permute σ asymmetric) := by
  intro h
  obtain ⟨k, hk⟩ := (fixed_iff_uniform (permute σ asymmetric)).mp h
  have hzero := congrFun hk (σ 0)
  have hone := congrFun hk (σ 1)
  norm_num [permute, asymmetric, uniform] at hzero hone
  omega

abbrev OrbitAmplitudes := Equiv.Perm (Fin 3) → ℂ

def symmetricOrbitSum : OrbitAmplitudes := fun _ => 1

def permuteOrbitAmplitudes (σ : Equiv.Perm (Fin 3)) (ψ : OrbitAmplitudes) :
    OrbitAmplitudes := fun τ => ψ (σ.symm * τ)

theorem symmetric_orbit_sum_invariant (σ : Equiv.Perm (Fin 3)) :
    permuteOrbitAmplitudes σ symmetricOrbitSum = symmetricOrbitSum := by rfl

theorem symmetric_orbit_sum_nonzero : symmetricOrbitSum ≠ 0 := by
  intro h
  have he := congrFun h (1 : Equiv.Perm (Fin 3))
  norm_num [symmetricOrbitSum] at he

theorem all_orbit_labels_have_charge_minus_one (σ : Equiv.Perm (Fin 3)) :
    charge (permute σ asymmetric) = -1 := by
  rw [charge_permute, asymmetric_charge]

abbrev Amplitudes := WritheVector → ℂ

def writheAction (i : Fin 3) (ψ : Amplitudes) : Amplitudes :=
  fun w => (w i : ℂ) * ψ w

def chargeAction (ψ : Amplitudes) : Amplitudes :=
  fun w => (charge w : ℂ) * ψ w

theorem charge_action_is_normalized_writhe_sum (ψ : Amplitudes) (w : WritheVector) :
    chargeAction ψ w = (∑ i, writheAction i ψ w) / 3 := by
  simp [chargeAction, writheAction, charge, Fin.sum_univ_succ]
  ring

#print axioms fixed_iff_uniform
#print axioms fixed_charge_iff_uniform
#print axioms unique_fixed_charge_minus_one
#print axioms charge_permute
#print axioms asymmetric_not_fixed
#print axioms low_complexity_fixed_charge
#print axioms first_parity_distinguishes_labels
#print axioms fixed_charge_support_unique
#print axioms orbit_labels_injective
#print axioms orbit_labels_not_fixed
#print axioms symmetric_orbit_sum_invariant
#print axioms all_orbit_labels_have_charge_minus_one
#print axioms charge_action_is_normalized_writhe_sum

end QBD.IntegerWritheCharge

namespace QBD.Monograph.ChargeUniqueness
open QBD.IntegerWritheCharge

-- Relate the fixed-configuration predicate to its specified integer charge.
/-- A fixed label of integer charge k is exactly the constant vector k. -/
theorem fixed_charge (w : WritheVector) (k : ℤ) :
    (PermutationFixed w ∧ charge w = k) ↔ w = uniform k :=
  fixed_charge_iff_uniform w k

#print axioms fixed_charge
end QBD.Monograph.ChargeUniqueness

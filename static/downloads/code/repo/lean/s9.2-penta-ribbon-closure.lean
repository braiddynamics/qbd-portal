import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Algebra.Lie.Matrix
import Mathlib.Algebra.Lie.Subalgebra
import Mathlib.LinearAlgebra.Complex.Module
import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.LinearAlgebra.Matrix.Trace

attribute [local instance 100] LieRing.ofAssociativeRing

noncomputable section
set_option maxHeartbeats 4000000
set_option maxRecDepth 4000

namespace QBD.SU5Closure
abbrev M := Matrix (Fin 5) (Fin 5) ℂ

-- The compact real matrix Lie algebra, independently of its generators.
def su : LieSubalgebra ℝ M where
  carrier := {a | a.conjTranspose = -a ∧ a.trace = 0}
  zero_mem' := by simp
  add_mem' := by
    intro a b ha hb
    exact ⟨by simp [Matrix.conjTranspose_add, ha.1, hb.1, add_comm], by simp [Matrix.trace_add, ha.2, hb.2]⟩
  smul_mem' := by
    intro r a ha
    exact ⟨by simp [Matrix.conjTranspose_smul, ha.1], by simp [Matrix.trace_smul, ha.2]⟩
  lie_mem' := by
    intro a b ha hb
    constructor
    · change (a * b - b * a).conjTranspose = -(a * b - b * a)
      simp [Matrix.conjTranspose_sub, Matrix.conjTranspose_mul, ha.1, hb.1]
    · change (a * b - b * a).trace = 0
      rw [Matrix.trace_sub, Matrix.trace_mul_comm a b, sub_self]

def realSkew : LieSubalgebra ℝ M where
  carrier := {a | a.transpose = -a ∧ ∀ i j, (a i j).im = 0}
  zero_mem' := by simp
  add_mem' := by
    intro a b ha hb
    exact ⟨by simp [Matrix.transpose_add, ha.1, hb.1, add_comm], by simpa using fun i j => show ((a + b) i j).im = 0 by simp [ha.2, hb.2]⟩
  smul_mem' := by
    intro r a ha
    exact ⟨by simp [Matrix.transpose_smul, ha.1], by simpa using fun i j => show ((r • a) i j).im = 0 by simp [ha.2]⟩
  lie_mem' := by
    intro a b ha hb
    constructor
    · change (a * b - b * a).transpose = -(a * b - b * a)
      simp [Matrix.transpose_sub, Matrix.transpose_mul, ha.1, hb.1]
    · intro i j
      change ((a * b - b * a) i j).im = 0
      simp [Matrix.mul_apply, Complex.mul_im, ha.2, hb.2]

def phase (i : Fin 5) : ℂ := match i.val with
  | 0 => 1
  | 1 => Complex.I
  | 2 => -1
  | 3 => -Complex.I
  | _ => 1

def D : M := Matrix.diagonal phase

theorem D_unitary : D * D.conjTranspose = 1 ∧ D.conjTranspose * D = 1 := by
  constructor <;> ext i j <;> fin_cases i <;> fin_cases j <;>
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, D, phase, Matrix.mul_apply, Fin.sum_univ_succ, Matrix.diagonal_apply]

def conjugate (a : M) : M := D.conjTranspose * a * D

theorem conjugate_bracket (a b : M) :
    conjugate ⁅a,b⁆ = ⁅conjugate a, conjugate b⁆ := by
  change D.conjTranspose * (a*b-b*a) * D =
    (D.conjTranspose*a*D)*(D.conjTranspose*b*D) -
    (D.conjTranspose*b*D)*(D.conjTranspose*a*D)
  simp only [Matrix.mul_sub, Matrix.sub_mul]
  simp only [Matrix.mul_assoc, ← Matrix.mul_assoc D D.conjTranspose, D_unitary.1,
    Matrix.one_mul]

def twistedSo : LieSubalgebra ℝ M where
  carrier := {a | conjugate a ∈ realSkew}
  zero_mem' := by simp [conjugate]
  add_mem' := by
    intro a b ha hb
    simpa [conjugate, Matrix.mul_add, Matrix.add_mul] using realSkew.add_mem ha hb
  smul_mem' := by
    intro r a ha
    simpa [conjugate, Matrix.mul_smul, Matrix.smul_mul] using realSkew.smul_mem r ha
  lie_mem' := by
    intro a b ha hb
    change conjugate ⁅a,b⁆ ∈ realSkew
    rw [conjugate_bracket]
    exact realSkew.lie_mem ha hb


open scoped Matrix

def E (i j : Fin 5) : M := Matrix.single i j 1

@[simp] theorem E_apply (i j a b : Fin 5) :
    E i j a b = if i.val = a.val ∧ j.val = b.val then 1 else 0 := by
  simp only [E, Matrix.single_apply, Fin.ext_iff]

def F (i j : Fin 5) : M := E i j - E j i

def S (i j : Fin 5) : M := Complex.I • (E i j + E j i)

def H (i : Fin 5) : M := Complex.I • (E i i - E 4 4)

def A (k : Fin 4) : M := S k.castSucc k.succ

def C (k : Fin 4) : M := Complex.I • (E k.castSucc k.castSucc - E k.succ k.succ)

def four : LieSubalgebra ℝ M := LieSubalgebra.lieSpan ℝ M (Set.range A)

def eight : LieSubalgebra ℝ M := LieSubalgebra.lieSpan ℝ M (Set.range A ∪ Set.range C)

def basis24 : Fin 24 → M := fun t =>
  match t.val with
  | 0 => F 0 1
  | 1 => F 0 2
  | 2 => F 0 3
  | 3 => F 0 4
  | 4 => F 1 2
  | 5 => F 1 3
  | 6 => F 1 4
  | 7 => F 2 3
  | 8 => F 2 4
  | 9 => F 3 4
  | 10 => S 0 1
  | 11 => S 0 2
  | 12 => S 0 3
  | 13 => S 0 4
  | 14 => S 1 2
  | 15 => S 1 3
  | 16 => S 1 4
  | 17 => S 2 3
  | 18 => S 2 4
  | 19 => S 3 4
  | 20 => H 0
  | 21 => H 1
  | 22 => H 2
  | _ => H 3

def synth24 (v : Fin 24 → ℝ) : M := fun i j =>
  match i.val, j.val with
  | 0, 0 => (v 20 : ℂ) * Complex.I
  | 0, 1 => (v 0 : ℂ) + (v 10 : ℂ) * Complex.I
  | 0, 2 => (v 1 : ℂ) + (v 11 : ℂ) * Complex.I
  | 0, 3 => (v 2 : ℂ) + (v 12 : ℂ) * Complex.I
  | 0, 4 => (v 3 : ℂ) + (v 13 : ℂ) * Complex.I
  | 1, 0 => -(v 0 : ℂ) + (v 10 : ℂ) * Complex.I
  | 1, 1 => (v 21 : ℂ) * Complex.I
  | 1, 2 => (v 4 : ℂ) + (v 14 : ℂ) * Complex.I
  | 1, 3 => (v 5 : ℂ) + (v 15 : ℂ) * Complex.I
  | 1, 4 => (v 6 : ℂ) + (v 16 : ℂ) * Complex.I
  | 2, 0 => -(v 1 : ℂ) + (v 11 : ℂ) * Complex.I
  | 2, 1 => -(v 4 : ℂ) + (v 14 : ℂ) * Complex.I
  | 2, 2 => (v 22 : ℂ) * Complex.I
  | 2, 3 => (v 7 : ℂ) + (v 17 : ℂ) * Complex.I
  | 2, 4 => (v 8 : ℂ) + (v 18 : ℂ) * Complex.I
  | 3, 0 => -(v 2 : ℂ) + (v 12 : ℂ) * Complex.I
  | 3, 1 => -(v 5 : ℂ) + (v 15 : ℂ) * Complex.I
  | 3, 2 => -(v 7 : ℂ) + (v 17 : ℂ) * Complex.I
  | 3, 3 => (v 23 : ℂ) * Complex.I
  | 3, 4 => (v 9 : ℂ) + (v 19 : ℂ) * Complex.I
  | 4, 0 => -(v 3 : ℂ) + (v 13 : ℂ) * Complex.I
  | 4, 1 => -(v 6 : ℂ) + (v 16 : ℂ) * Complex.I
  | 4, 2 => -(v 8 : ℂ) + (v 18 : ℂ) * Complex.I
  | 4, 3 => -(v 9 : ℂ) + (v 19 : ℂ) * Complex.I
  | _, _ => -((v 20 : ℂ) + v 21 + v 22 + v 23) * Complex.I

def coord24 (m : M) : Fin 24 → ℝ := fun t =>
  match t.val with
  | 0 => (m 0 1).re
  | 1 => (m 0 2).re
  | 2 => (m 0 3).re
  | 3 => (m 0 4).re
  | 4 => (m 1 2).re
  | 5 => (m 1 3).re
  | 6 => (m 1 4).re
  | 7 => (m 2 3).re
  | 8 => (m 2 4).re
  | 9 => (m 3 4).re
  | 10 => (m 0 1).im
  | 11 => (m 0 2).im
  | 12 => (m 0 3).im
  | 13 => (m 0 4).im
  | 14 => (m 1 2).im
  | 15 => (m 1 3).im
  | 16 => (m 1 4).im
  | 17 => (m 2 3).im
  | 18 => (m 2 4).im
  | 19 => (m 3 4).im
  | 20 => (m 0 0).im
  | 21 => (m 1 1).im
  | 22 => (m 2 2).im
  | _ => (m 3 3).im

theorem coord24_synth24 (v : Fin 24 → ℝ) : coord24 (synth24 v) = v := by
  ext t
  fin_cases t <;>
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, coord24, synth24, basis24, F, S, H, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;> rfl

theorem synth24_reconstruct (m : M) (hm : m ∈ su) : synth24 (coord24 m) = m := by
  have hre (i j : Fin 5) : (m j i).re = -(m i j).re := by
    have h := congrArg Complex.re (congrFun (congrFun hm.1 i) j)
    simpa using h
  have him (i j : Fin 5) : (m j i).im = (m i j).im := by
    have h := congrArg Complex.im (congrFun (congrFun hm.1 i) j)
    simpa using neg_injective h
  have ht : (m 0 0).im + ((m 1 1).im + ((m 2 2).im + ((m 3 3).im + (m 4 4).im))) = 0 := by
    simpa [Matrix.trace, Matrix.diag, Fin.sum_univ_succ] using congrArg Complex.im hm.2
  ext i j
  fin_cases i <;> fin_cases j
  · change synth24 (coord24 m) 0 0 = m 0 0
    have hr := hre 0 0
    have hi := him 0 0
    have hd := hre 0 0
    have he := hre 0 0
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 0 1 = m 0 1
    have hr := hre 0 1
    have hi := him 0 1
    have hd := hre 0 0
    have he := hre 1 1
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 0 2 = m 0 2
    have hr := hre 0 2
    have hi := him 0 2
    have hd := hre 0 0
    have he := hre 2 2
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 0 3 = m 0 3
    have hr := hre 0 3
    have hi := him 0 3
    have hd := hre 0 0
    have he := hre 3 3
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 0 4 = m 0 4
    have hr := hre 0 4
    have hi := him 0 4
    have hd := hre 0 0
    have he := hre 4 4
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 1 0 = m 1 0
    have hr := hre 1 0
    have hi := him 1 0
    have hd := hre 1 1
    have he := hre 0 0
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 1 1 = m 1 1
    have hr := hre 1 1
    have hi := him 1 1
    have hd := hre 1 1
    have he := hre 1 1
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 1 2 = m 1 2
    have hr := hre 1 2
    have hi := him 1 2
    have hd := hre 1 1
    have he := hre 2 2
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 1 3 = m 1 3
    have hr := hre 1 3
    have hi := him 1 3
    have hd := hre 1 1
    have he := hre 3 3
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 1 4 = m 1 4
    have hr := hre 1 4
    have hi := him 1 4
    have hd := hre 1 1
    have he := hre 4 4
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 2 0 = m 2 0
    have hr := hre 2 0
    have hi := him 2 0
    have hd := hre 2 2
    have he := hre 0 0
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 2 1 = m 2 1
    have hr := hre 2 1
    have hi := him 2 1
    have hd := hre 2 2
    have he := hre 1 1
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 2 2 = m 2 2
    have hr := hre 2 2
    have hi := him 2 2
    have hd := hre 2 2
    have he := hre 2 2
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 2 3 = m 2 3
    have hr := hre 2 3
    have hi := him 2 3
    have hd := hre 2 2
    have he := hre 3 3
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 2 4 = m 2 4
    have hr := hre 2 4
    have hi := him 2 4
    have hd := hre 2 2
    have he := hre 4 4
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 3 0 = m 3 0
    have hr := hre 3 0
    have hi := him 3 0
    have hd := hre 3 3
    have he := hre 0 0
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 3 1 = m 3 1
    have hr := hre 3 1
    have hi := him 3 1
    have hd := hre 3 3
    have he := hre 1 1
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 3 2 = m 3 2
    have hr := hre 3 2
    have hi := him 3 2
    have hd := hre 3 3
    have he := hre 2 2
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 3 3 = m 3 3
    have hr := hre 3 3
    have hi := him 3 3
    have hd := hre 3 3
    have he := hre 3 3
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 3 4 = m 3 4
    have hr := hre 3 4
    have hi := him 3 4
    have hd := hre 3 3
    have he := hre 4 4
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 4 0 = m 4 0
    have hr := hre 4 0
    have hi := him 4 0
    have hd := hre 4 4
    have he := hre 0 0
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 4 1 = m 4 1
    have hr := hre 4 1
    have hi := him 4 1
    have hd := hre 4 4
    have he := hre 1 1
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 4 2 = m 4 2
    have hr := hre 4 2
    have hi := him 4 2
    have hd := hre 4 4
    have he := hre 2 2
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 4 3 = m 4 3
    have hr := hre 4 3
    have hi := him 4 3
    have hd := hre 4 4
    have he := hre 3 3
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 4 4 = m 4 4
    have hr := hre 4 4
    have hi := him 4 4
    have hd := hre 4 4
    have he := hre 4 4
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

-- Membership of the generators and explicit bracket-generated basis elements.
theorem A_mem_eight (k : Fin 4) : A k ∈ eight :=
  LieSubalgebra.subset_lieSpan (Or.inl (Set.mem_range_self k))

theorem C_mem_eight (k : Fin 4) : C k ∈ eight :=
  LieSubalgebra.subset_lieSpan (Or.inr (Set.mem_range_self k))

theorem S01_mem : S 0 1 ∈ eight := A_mem_eight 0

theorem F01_mem : F 0 1 ∈ eight := by
  have h : (1/2 : ℝ) • ⁅A 0, C 0⁆ = F 0 1 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.smul_mem _ (eight.lie_mem (A_mem_eight 0) (C_mem_eight 0))

theorem S12_mem : S 1 2 ∈ eight := A_mem_eight 1

theorem F12_mem : F 1 2 ∈ eight := by
  have h : (1/2 : ℝ) • ⁅A 1, C 1⁆ = F 1 2 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.smul_mem _ (eight.lie_mem (A_mem_eight 1) (C_mem_eight 1))

theorem S23_mem : S 2 3 ∈ eight := A_mem_eight 2

theorem F23_mem : F 2 3 ∈ eight := by
  have h : (1/2 : ℝ) • ⁅A 2, C 2⁆ = F 2 3 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.smul_mem _ (eight.lie_mem (A_mem_eight 2) (C_mem_eight 2))

theorem S34_mem : S 3 4 ∈ eight := A_mem_eight 3

theorem F34_mem : F 3 4 ∈ eight := by
  have h : (1/2 : ℝ) • ⁅A 3, C 3⁆ = F 3 4 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.smul_mem _ (eight.lie_mem (A_mem_eight 3) (C_mem_eight 3))

theorem F02_mem : F 0 2 ∈ eight := by
  have h : ⁅F 0 1, F 1 2⁆ = F 0 2 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F01_mem F12_mem

theorem S02_mem : S 0 2 ∈ eight := by
  have h : ⁅F 0 1, S 1 2⁆ = S 0 2 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F01_mem S12_mem

theorem F13_mem : F 1 3 ∈ eight := by
  have h : ⁅F 1 2, F 2 3⁆ = F 1 3 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F12_mem F23_mem

theorem S13_mem : S 1 3 ∈ eight := by
  have h : ⁅F 1 2, S 2 3⁆ = S 1 3 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F12_mem S23_mem

theorem F24_mem : F 2 4 ∈ eight := by
  have h : ⁅F 2 3, F 3 4⁆ = F 2 4 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F23_mem F34_mem

theorem S24_mem : S 2 4 ∈ eight := by
  have h : ⁅F 2 3, S 3 4⁆ = S 2 4 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F23_mem S34_mem

theorem F03_mem : F 0 3 ∈ eight := by
  have h : ⁅F 0 2, F 2 3⁆ = F 0 3 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F02_mem F23_mem

theorem S03_mem : S 0 3 ∈ eight := by
  have h : ⁅F 0 2, S 2 3⁆ = S 0 3 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F02_mem S23_mem

theorem F14_mem : F 1 4 ∈ eight := by
  have h : ⁅F 1 3, F 3 4⁆ = F 1 4 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F13_mem F34_mem

theorem S14_mem : S 1 4 ∈ eight := by
  have h : ⁅F 1 3, S 3 4⁆ = S 1 4 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F13_mem S34_mem

theorem F04_mem : F 0 4 ∈ eight := by
  have h : ⁅F 0 3, F 3 4⁆ = F 0 4 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F03_mem F34_mem

theorem S04_mem : S 0 4 ∈ eight := by
  have h : ⁅F 0 3, S 3 4⁆ = S 0 4 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F03_mem S34_mem

theorem H0_mem : H 0 ∈ eight := by
  have h : (1/2 : ℝ) • ⁅F 0 4, S 0 4⁆ = H 0 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.smul_mem _ (eight.lie_mem F04_mem S04_mem)

theorem H1_mem : H 1 ∈ eight := by
  have h : (1/2 : ℝ) • ⁅F 1 4, S 1 4⁆ = H 1 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.smul_mem _ (eight.lie_mem F14_mem S14_mem)

theorem H2_mem : H 2 ∈ eight := by
  have h : (1/2 : ℝ) • ⁅F 2 4, S 2 4⁆ = H 2 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.smul_mem _ (eight.lie_mem F24_mem S24_mem)

theorem H3_mem : H 3 ∈ eight := by
  have h : (1/2 : ℝ) • ⁅F 3 4, S 3 4⁆ = H 3 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.smul_mem _ (eight.lie_mem F34_mem S34_mem)

theorem basis24_mem (t : Fin 24) : basis24 t ∈ eight := by
  fin_cases t
  · exact F01_mem
  · exact F02_mem
  · exact F03_mem
  · exact F04_mem
  · exact F12_mem
  · exact F13_mem
  · exact F14_mem
  · exact F23_mem
  · exact F24_mem
  · exact F34_mem
  · exact S01_mem
  · exact S02_mem
  · exact S03_mem
  · exact S04_mem
  · exact S12_mem
  · exact S13_mem
  · exact S14_mem
  · exact S23_mem
  · exact S24_mem
  · exact S34_mem
  · exact H0_mem
  · exact H1_mem
  · exact H2_mem
  · exact H3_mem

theorem synth24_mem (v : Fin 24 → ℝ) : synth24 v ∈ eight := by
  have heq : (∑ t : Fin 24, v t • basis24 t) = synth24 v := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, basis24, F, S, H, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;> first
      | rfl
      | (change -v 20 + (-v 21 + (-v 22 + -v 23)) = -v 23 + (-v 22 + (-v 21 + -v 20)); ring)
  rw [← heq]
  exact eight.sum_mem fun t _ => eight.smul_mem _ (basis24_mem t)

theorem eight_le_su : eight ≤ su := by
  apply LieSubalgebra.lieSpan_le.mpr
  intro m hm
  rcases hm with ⟨k, rfl⟩ | ⟨k, rfl⟩
  all_goals
    constructor
    · ext i j
      fin_cases k <;> fin_cases i <;> fin_cases j <;> apply Complex.ext <;>
        norm_num [Fin.succ, Fin.ofNat, A, C, S, E_apply]
    · fin_cases k <;> apply Complex.ext <;>
        norm_num [Fin.succ, Fin.ofNat, A, C, S, E_apply, Matrix.trace, Fin.sum_univ_succ]

theorem eight_eq_su : eight = su := by
  apply le_antisymm eight_le_su
  intro m hm
  rw [← synth24_reconstruct m hm]
  exact synth24_mem _


def eightCoordinates : eight ≃ₗ[ℝ] (Fin 24 → ℝ) where
  toFun m := coord24 m.val
  invFun v := ⟨synth24 v, synth24_mem v⟩
  left_inv m := by
    apply Subtype.ext
    exact synth24_reconstruct m.val (eight_le_su m.property)
  right_inv := coord24_synth24
  map_add' a b := by
    ext t
    fin_cases t <;> simp [coord24]
  map_smul' r a := by
    ext t
    fin_cases t <;> simp [coord24]

theorem eight_dimension : Module.finrank ℝ eight = 24 := by
  simpa using eightCoordinates.finrank_eq

-- The ten path brackets of the original four symmetric generators.
def B (i j : Fin 5) : M :=
  Complex.I ^ (j.val-i.val) • E i j - (-Complex.I) ^ (j.val-i.val) • E j i

def basis10 : Fin 10 → M := fun t =>
  match t.val with
  | 0 => B 0 1
  | 1 => B 0 2
  | 2 => B 0 3
  | 3 => B 0 4
  | 4 => B 1 2
  | 5 => B 1 3
  | 6 => B 1 4
  | 7 => B 2 3
  | 8 => B 2 4
  | _ => B 3 4

def synth10 (v : Fin 10 → ℝ) : M := fun i j =>
  match i.val, j.val with
  | 0, 0 => 0
  | 0, 1 => (v 0 : ℂ) * (Complex.I)
  | 0, 2 => (v 1 : ℂ) * (-1)
  | 0, 3 => (v 2 : ℂ) * (-Complex.I)
  | 0, 4 => (v 3 : ℂ) * (1)
  | 1, 0 => (v 0 : ℂ) * (Complex.I)
  | 1, 1 => 0
  | 1, 2 => (v 4 : ℂ) * (Complex.I)
  | 1, 3 => (v 5 : ℂ) * (-1)
  | 1, 4 => (v 6 : ℂ) * (-Complex.I)
  | 2, 0 => (v 1 : ℂ) * (1)
  | 2, 1 => (v 4 : ℂ) * (Complex.I)
  | 2, 2 => 0
  | 2, 3 => (v 7 : ℂ) * (Complex.I)
  | 2, 4 => (v 8 : ℂ) * (-1)
  | 3, 0 => (v 2 : ℂ) * (-Complex.I)
  | 3, 1 => (v 5 : ℂ) * (1)
  | 3, 2 => (v 7 : ℂ) * (Complex.I)
  | 3, 3 => 0
  | 3, 4 => (v 9 : ℂ) * (Complex.I)
  | 4, 0 => (v 3 : ℂ) * (-1)
  | 4, 1 => (v 6 : ℂ) * (-Complex.I)
  | 4, 2 => (v 8 : ℂ) * (1)
  | 4, 3 => (v 9 : ℂ) * (Complex.I)
  | _, _ => 0

def coord10 (m : M) : Fin 10 → ℝ := fun t =>
  match t.val with
  | 0 => (m 0 1).im
  | 1 => -(m 0 2).re
  | 2 => -(m 0 3).im
  | 3 => (m 0 4).re
  | 4 => (m 1 2).im
  | 5 => -(m 1 3).re
  | 6 => -(m 1 4).im
  | 7 => (m 2 3).im
  | 8 => -(m 2 4).re
  | _ => (m 3 4).im

theorem coord10_synth10 (v : Fin 10 → ℝ) : coord10 (synth10 v) = v := by
  ext t
  fin_cases t <;>
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, coord10, synth10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;> rfl

theorem four_le_twistedSo : four ≤ twistedSo := by
  apply LieSubalgebra.lieSpan_le.mpr
  rintro m ⟨k,rfl⟩
  change (conjugate (A k)).transpose = -conjugate (A k) ∧
    ∀ i j, (conjugate (A k) i j).im = 0
  constructor
  · ext i j; fin_cases k <;> fin_cases i <;> fin_cases j <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, A, S, E_apply, Matrix.mul_apply, Matrix.diagonal_apply,
        Matrix.single_apply, Fin.sum_univ_succ]
  · intro i j; fin_cases k <;> fin_cases i <;> fin_cases j <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, A, S, E_apply, Matrix.mul_apply, Matrix.diagonal_apply,
        Matrix.single_apply, Fin.sum_univ_succ]

theorem synth10_reconstruct (m : M) (hm : m ∈ twistedSo) : synth10 (coord10 m) = m := by
  have hs (i j : Fin 5) : conjugate m j i = -conjugate m i j :=
    congrFun (congrFun hm.1 i) j
  have hz (i j : Fin 5) : (conjugate m i j).im = 0 := hm.2 i j
  ext i j
  fin_cases i <;> fin_cases j
  · change synth10 (coord10 m) 0 0 = m 0 0
    have hr := congrArg Complex.re (hs 0 0)
    have hi := congrArg Complex.im (hs 0 0)
    have hzi := hz 0 0
    have hzj := hz 0 0
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 0 1 = m 0 1
    have hr := congrArg Complex.re (hs 0 1)
    have hi := congrArg Complex.im (hs 0 1)
    have hzi := hz 0 1
    have hzj := hz 1 0
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 0 2 = m 0 2
    have hr := congrArg Complex.re (hs 0 2)
    have hi := congrArg Complex.im (hs 0 2)
    have hzi := hz 0 2
    have hzj := hz 2 0
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 0 3 = m 0 3
    have hr := congrArg Complex.re (hs 0 3)
    have hi := congrArg Complex.im (hs 0 3)
    have hzi := hz 0 3
    have hzj := hz 3 0
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 0 4 = m 0 4
    have hr := congrArg Complex.re (hs 0 4)
    have hi := congrArg Complex.im (hs 0 4)
    have hzi := hz 0 4
    have hzj := hz 4 0
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 1 0 = m 1 0
    have hr := congrArg Complex.re (hs 1 0)
    have hi := congrArg Complex.im (hs 1 0)
    have hzi := hz 1 0
    have hzj := hz 0 1
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 1 1 = m 1 1
    have hr := congrArg Complex.re (hs 1 1)
    have hi := congrArg Complex.im (hs 1 1)
    have hzi := hz 1 1
    have hzj := hz 1 1
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 1 2 = m 1 2
    have hr := congrArg Complex.re (hs 1 2)
    have hi := congrArg Complex.im (hs 1 2)
    have hzi := hz 1 2
    have hzj := hz 2 1
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 1 3 = m 1 3
    have hr := congrArg Complex.re (hs 1 3)
    have hi := congrArg Complex.im (hs 1 3)
    have hzi := hz 1 3
    have hzj := hz 3 1
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 1 4 = m 1 4
    have hr := congrArg Complex.re (hs 1 4)
    have hi := congrArg Complex.im (hs 1 4)
    have hzi := hz 1 4
    have hzj := hz 4 1
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 2 0 = m 2 0
    have hr := congrArg Complex.re (hs 2 0)
    have hi := congrArg Complex.im (hs 2 0)
    have hzi := hz 2 0
    have hzj := hz 0 2
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 2 1 = m 2 1
    have hr := congrArg Complex.re (hs 2 1)
    have hi := congrArg Complex.im (hs 2 1)
    have hzi := hz 2 1
    have hzj := hz 1 2
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 2 2 = m 2 2
    have hr := congrArg Complex.re (hs 2 2)
    have hi := congrArg Complex.im (hs 2 2)
    have hzi := hz 2 2
    have hzj := hz 2 2
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 2 3 = m 2 3
    have hr := congrArg Complex.re (hs 2 3)
    have hi := congrArg Complex.im (hs 2 3)
    have hzi := hz 2 3
    have hzj := hz 3 2
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 2 4 = m 2 4
    have hr := congrArg Complex.re (hs 2 4)
    have hi := congrArg Complex.im (hs 2 4)
    have hzi := hz 2 4
    have hzj := hz 4 2
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 3 0 = m 3 0
    have hr := congrArg Complex.re (hs 3 0)
    have hi := congrArg Complex.im (hs 3 0)
    have hzi := hz 3 0
    have hzj := hz 0 3
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 3 1 = m 3 1
    have hr := congrArg Complex.re (hs 3 1)
    have hi := congrArg Complex.im (hs 3 1)
    have hzi := hz 3 1
    have hzj := hz 1 3
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 3 2 = m 3 2
    have hr := congrArg Complex.re (hs 3 2)
    have hi := congrArg Complex.im (hs 3 2)
    have hzi := hz 3 2
    have hzj := hz 2 3
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 3 3 = m 3 3
    have hr := congrArg Complex.re (hs 3 3)
    have hi := congrArg Complex.im (hs 3 3)
    have hzi := hz 3 3
    have hzj := hz 3 3
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 3 4 = m 3 4
    have hr := congrArg Complex.re (hs 3 4)
    have hi := congrArg Complex.im (hs 3 4)
    have hzi := hz 3 4
    have hzj := hz 4 3
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 4 0 = m 4 0
    have hr := congrArg Complex.re (hs 4 0)
    have hi := congrArg Complex.im (hs 4 0)
    have hzi := hz 4 0
    have hzj := hz 0 4
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 4 1 = m 4 1
    have hr := congrArg Complex.re (hs 4 1)
    have hi := congrArg Complex.im (hs 4 1)
    have hzi := hz 4 1
    have hzj := hz 1 4
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 4 2 = m 4 2
    have hr := congrArg Complex.re (hs 4 2)
    have hi := congrArg Complex.im (hs 4 2)
    have hzi := hz 4 2
    have hzj := hz 2 4
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 4 3 = m 4 3
    have hr := congrArg Complex.re (hs 4 3)
    have hi := congrArg Complex.im (hs 4 3)
    have hzi := hz 4 3
    have hzj := hz 3 4
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 4 4 = m 4 4
    have hr := congrArg Complex.re (hs 4 4)
    have hi := congrArg Complex.im (hs 4 4)
    have hzi := hz 4 4
    have hzj := hz 4 4
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
theorem B01_mem : B 0 1 ∈ four := by
  have h : B 0 1 = A 0 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, B, A, S, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [h]
  exact LieSubalgebra.subset_lieSpan (Set.mem_range_self 0)

theorem B12_mem : B 1 2 ∈ four := by
  have h : B 1 2 = A 1 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, B, A, S, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [h]
  exact LieSubalgebra.subset_lieSpan (Set.mem_range_self 1)

theorem B23_mem : B 2 3 ∈ four := by
  have h : B 2 3 = A 2 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, B, A, S, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [h]
  exact LieSubalgebra.subset_lieSpan (Set.mem_range_self 2)

theorem B34_mem : B 3 4 ∈ four := by
  have h : B 3 4 = A 3 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, B, A, S, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [h]
  exact LieSubalgebra.subset_lieSpan (Set.mem_range_self 3)

theorem B02_mem : B 0 2 ∈ four := by
  have h : ⁅B 0 1, A 1⁆ = B 0 2 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, B, A, S, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact four.lie_mem B01_mem (LieSubalgebra.subset_lieSpan (Set.mem_range_self 1))

theorem B13_mem : B 1 3 ∈ four := by
  have h : ⁅B 1 2, A 2⁆ = B 1 3 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, B, A, S, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact four.lie_mem B12_mem (LieSubalgebra.subset_lieSpan (Set.mem_range_self 2))

theorem B24_mem : B 2 4 ∈ four := by
  have h : ⁅B 2 3, A 3⁆ = B 2 4 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, B, A, S, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact four.lie_mem B23_mem (LieSubalgebra.subset_lieSpan (Set.mem_range_self 3))

theorem B03_mem : B 0 3 ∈ four := by
  have h : ⁅B 0 2, A 2⁆ = B 0 3 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, B, A, S, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact four.lie_mem B02_mem (LieSubalgebra.subset_lieSpan (Set.mem_range_self 2))

theorem B14_mem : B 1 4 ∈ four := by
  have h : ⁅B 1 3, A 3⁆ = B 1 4 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, B, A, S, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact four.lie_mem B13_mem (LieSubalgebra.subset_lieSpan (Set.mem_range_self 3))

theorem B04_mem : B 0 4 ∈ four := by
  have h : ⁅B 0 3, A 3⁆ = B 0 4 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, B, A, S, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact four.lie_mem B03_mem (LieSubalgebra.subset_lieSpan (Set.mem_range_self 3))

theorem basis10_mem (t : Fin 10) : basis10 t ∈ four := by
  fin_cases t
  · exact B01_mem
  · exact B02_mem
  · exact B03_mem
  · exact B04_mem
  · exact B12_mem
  · exact B13_mem
  · exact B14_mem
  · exact B23_mem
  · exact B24_mem
  · exact B34_mem

theorem synth10_mem (v : Fin 10 → ℝ) : synth10 v ∈ four := by
  have heq : (∑ t : Fin 10, v t • basis10 t) = synth10 v := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, basis10, B, F, S, H, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;> first | rfl | ring
  rw [← heq]
  exact four.sum_mem fun t _ => four.smul_mem _ (basis10_mem t)

theorem four_eq_twistedSo : four = twistedSo := by
  apply le_antisymm four_le_twistedSo
  intro m hm
  rw [← synth10_reconstruct m hm]
  exact synth10_mem _

def fourCoordinates : four ≃ₗ[ℝ] (Fin 10 → ℝ) where
  toFun m := coord10 m.val
  invFun v := ⟨synth10 v, synth10_mem v⟩
  left_inv m := by
    apply Subtype.ext
    exact synth10_reconstruct m.val (four_le_twistedSo m.property)
  right_inv := coord10_synth10
  map_add' a b := by
    ext t
    fin_cases t <;> simp [coord10, add_comm]
  map_smul' r a := by
    ext t
    fin_cases t <;> simp [coord10, add_comm]

theorem four_dimension : Module.finrank ℝ four = 10 := by
  simpa using fourCoordinates.finrank_eq

/-- Uniform conjugation, with no alternating sign. -/
theorem conjugate_adjacent (k : Fin 4) :
    conjugate (A k) = -F k.castSucc k.succ := by
  ext i j
  fin_cases k <;> fin_cases i <;> fin_cases j <;> apply Complex.ext <;>
    norm_num [Fin.succ, pow_succ, Fin.ofNat, conjugate, D, phase, A, F, S, E_apply, Matrix.mul_apply,
      Matrix.diagonal_apply, Fin.sum_univ_succ]

/-- The missing quadrature is an actual real Lie bracket of admitted matrix directions. -/
theorem adjacent_commutator (k : Fin 4) :
    ⁅A k, C k⁆ = (2 : ℝ) • F k.castSucc k.succ := by
  ext i j
  fin_cases k <;> fin_cases i <;> fin_cases j <;> apply Complex.ext <;>
    norm_num [Fin.succ, pow_succ, Fin.ofNat, A, C, F, S, E_apply, LieRing.of_associative_ring_bracket,
      Matrix.mul_apply, Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im]

/-- Every element of the original closure has zero diagonal, in the original basis. -/
theorem four_zero_diagonal (m : M) (hm : m ∈ four) (i : Fin 5) : m i i = 0 := by
  have h := congrFun (congrFun (synth10_reconstruct m (four_le_twistedSo hm)) i) i
  fin_cases i <;> simpa [synth10] using h.symm

theorem original_dimension_24_false : Module.finrank ℝ four ≠ 24 := by
  rw [four_dimension]
  norm_num

#print axioms adjacent_commutator
#print axioms conjugate_adjacent
#print axioms four_zero_diagonal
#print axioms eight_eq_su
#print axioms eight_dimension
#print axioms four_eq_twistedSo
#print axioms four_dimension

end QBD.SU5Closure

namespace QBD.Monograph.PentaClosure
open QBD.SU5Closure

-- Compare the original and enlarged real matrix Lie spans.
/-- The original closure has dimension ten; the direct enlarged closure has dimension twenty-four. -/
theorem closure_dimensions : Module.finrank ℝ four = 10 ∧ Module.finrank ℝ eight = 24 :=
  ⟨four_dimension, eight_dimension⟩

-- Identify the target independently of a dimension count.
/-- The enlarged generated algebra is the traceless skew-Hermitian matrix algebra. -/
theorem full_target : eight = su := eight_eq_su

#print axioms closure_dimensions
#print axioms full_target
end QBD.Monograph.PentaClosure

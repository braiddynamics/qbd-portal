# Computational supplement

*Clifford Contractions and the First-Order Bosonic Action in Geometric Unity*

R. Fisher · Braid Dynamics Applied Research Group

November 17, 2026

DOI: [10.5281/zenodo.24325062](https://doi.org/10.5281/zenodo.24325062)

The text and figures in the note and companion documents are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The software and project configuration files, including the source listings below, are licensed under the [MIT License](https://opensource.org/license/mit). The [archive README](#source-readme-md) specifies the scope of these grants, and the full [CC BY 4.0](#source-license-cc-by-4-0-txt) and [MIT](#source-license-mit-txt) terms are reproduced below and included in the archive.

This Markdown document contains the complete verification code. Each named section contains one file, with a summary immediately above its source. The file index links directly to every listing.

The [Code Guide](fisher-geometric-unity-2026-11-17-code-guide.pdf) explains the mathematical coverage, describes every file, reports the benchmark results, and gives the commands for running the project. Its [Markdown source](fisher-geometric-unity-2026-11-17-code-guide.md) is also available. The [source archive](fisher-geometric-unity-2026-11-17-code.zip) contains the same files as individual files inside a directory named `gu-code`.

# File index {#file-index}

Select a filename to read its complete source.

## Main results and audit

| File | Purpose |
|:-----|:--------|
| [Theorem52.lean](#source-theorem52-lean) | Derives the first variation, stationarity criterion, and Einstein specialization under the stated boundary and separation hypotheses. |
| [WitnessW1.lean](#source-witnessw1-lean) | Constructs the exact nonzero torsion correction in the split Clifford algebra and checks the test blade and trace pairing. |
| [BianchiSymbol.lean](#source-bianchisymbol-lean) | Identifies closed first jets, realizes them by closed linear two-forms, and proves unique factorization through alternation. |
| [NoetherIdentity.lean](#source-noetheridentity-lean) | Proves finite gauge invariance, the dressing differential, and the paired and off-shell Noether identities under explicit hypotheses. |
| [D7RealTheorem.lean](#source-d7realtheorem-lean) | Assembles real Theorem 3.4, including the dimensions 200, 96, 56, and 48 and the closed-field Bianchi criterion. |
| [Audit.lean](#source-audit-lean) | Prints the axiom dependencies of the indexed mathematical results. |

## Complex exterior representations

| File | Purpose |
|:-----|:--------|
| [D7Counts.lean](#source-d7counts-lean) | Computes signed integer multiplicities and verifies the fifteen grade rows and channel totals. |
| [D7Classification.lean](#source-d7classification-lean) | Provides general decomposition, intertwiner-dimension, block decomposition, and real-to-complex comparison lemmas. |
| [D7Exterior.lean](#source-d7exterior-lean) | Defines the split complex orthogonal action and checks exterior weights, highest-weight candidates, and Weyl dimensions. |
| [D7Hodge.lean](#source-d7hodge-lean) | Constructs the equivariant Hodge involution on the middle exterior power and its signed eigenspaces. |
| [D7Irreducible.lean](#source-d7irreducible-lean) | Proves irreducibility of the non-middle exterior powers using signed coordinate actions. |
| [D7VectorTensor.lean](#source-d7vectortensor-lean) | Constructs alternation, trace, and their sections and splits the vector times two-form representation into three channels. |
| [D7Hook.lean](#source-d7hook-lean) | Proves irreducibility of the traceless hook representation. |
| [D7VectorGrades.lean](#source-d7vectorgrades-lean) | Constructs wedge and metric-contraction maps and their equivariant sections in all exterior degrees. |
| [D7MiddleTensor.lean](#source-d7middletensor-lean) | Constructs the two signed residual summands in the middle degree. |
| [D7MiddleIrreducible.lean](#source-d7middleirreducible-lean) | Proves irreducibility of the signed middle residual summands. |
| [D7TensorColumns.lean](#source-d7tensorcolumns-lean) | Organizes repeated-index and distinct-index tensor coordinates used in the kernel arguments. |
| [D7TensorRotations.lean](#source-d7tensorrotations-lean) | Calculates the plane rotations that connect the two tensor-coordinate families. |
| [D7GradeIrreducible.lean](#source-d7gradeirreducible-lean) | Proves irreducibility of the non-middle vector-exterior kernels. |
| [D7ComplementaryGrades.lean](#source-d7complementarygrades-lean) | Transports exterior representations and their tensor kernels between complementary degrees by Hodge duality. |
| [D7SignedDistinction.lean](#source-d7signeddistinction-lean) | Distinguishes the two signed middle constituents using a diagonal torus action. |

## Multiplicity counts and complex symbols

| File | Purpose |
|:-----|:--------|
| [D7TripleInvariants.lean](#source-d7tripleinvariants-lean) | Classifies invariant trilinear exterior forms and bounds the vector and alternating multiplicities. |
| [D7TripleMultiplicity.lean](#source-d7triplemultiplicity-lean) | Realizes the trilinear invariants and proves the vector and alternating totals of 56 and 96. |
| [D7QuadInvariants.lean](#source-d7quadinvariants-lean) | Classifies the invariant forms with a vector factor and three exterior factors. |
| [D7QuadMultiplicity.lean](#source-d7quadmultiplicity-lean) | Realizes the invariant four-factor forms needed for the unrestricted contraction count. |
| [D7Unrestricted.lean](#source-d7unrestricted-lean) | Identifies unrestricted intertwiners with invariant forms and proves the total dimension 200. |
| [D7Final.lean](#source-d7final-lean) | Assembles the complex symbol channels, the Bianchi factorization, the hook count, and the general action-span comparison. |
| [D7BianchiFields.lean](#source-d7bianchifields-lean) | Matches the complex tensor symbols to coordinate first jets and proves the closed-field criterion in every grade. |

## Real Spin and Clifford actions

| File | Purpose |
|:-----|:--------|
| [D7UnitaryRealForm.lean](#source-d7unitaryrealform-lean) | Models skew-adjoint coefficient matrices as a real form and identifies their complexification. |
| [D7SpinAction.lean](#source-d7spinaction-lean) | Defines the real Spin vector and Clifford conjugation actions and their exterior-algebra identification. |
| [D7CliffordMatrix.lean](#source-d7cliffordmatrix-lean) | Constructs the split Clifford algebra as matrices on the 128-dimensional exterior spinor module. |
| [D7CliffordAdjoint.lean](#source-d7cliffordadjoint-lean) | Identifies the matrix adjoint, checks Hermitian signature (64,64), and intertwines coefficient conjugation. |
| [D7SpinNullFrame.lean](#source-d7spinnullframe-lean) | Changes the real vector action into split null coordinates and maps its complexification into the orthogonal action. |
| [D7SpinRootLifts.lean](#source-d7spinrootlifts-lean) | Constructs real Spin lifts of the isotropic root transvections. |
| [D7SpinOrientation.lean](#source-d7spinorientation-lean) | Proves that the real Spin vector action has determinant one. |
| [D7RootInterpolation.lean](#source-d7rootinterpolation-lean) | Uses polynomial interpolation to place complex split-root tensor actions in the span of real Spin actions. |
| [D7RootGeneration.lean](#source-d7rootgeneration-lean) | Proves generation of the complex split special orthogonal action by split roots and extends the action-span result. |
| [D7RealComparison.lean](#source-d7realcomparison-lean) | Identifies the complexified real coefficient, form, and covector tensor actions with the complex exterior-grade actions. |
| [D7RealJets.lean](#source-d7realjets-lean) | Constructs real coordinate first jets, wedge and trace projections, and their equivariant sections. |
| [D7RealRanks.lean](#source-d7realranks-lean) | Transfers the complex intertwiner counts to the real operator and exterior-symbol spaces. |

## Program and project configuration

| File | Purpose |
|:-----|:--------|
| [GU-test.py](#source-gu-test-py) | Runs the six groups of computational and numerical checks reported in the benchmark tables. |
| [lakefile.toml](#source-lakefile-toml) | Declares the 39 Lean library targets and pins Mathlib to v4.33.1. |
| [lake-manifest.json](#source-lake-manifest-json) | Records the exact Mathlib and transitive dependency revisions for the portable project. |
| [lean-toolchain](#source-lean-toolchain) | Pins Lean to leanprover/lean4:v4.33.1. |

## Publication and license files

| File | Purpose |
|:-----|:--------|
| [README.md](#source-readme-md) | Records the publication DOI and citation, archive contents, and the scope of the text and software licenses. |
| [LICENSE-CC-BY-4.0.txt](#source-license-cc-by-4-0-txt) | Contains the full Creative Commons Attribution 4.0 International terms for the text and figures. |
| [LICENSE-MIT.txt](#source-license-mit-txt) | Contains the full MIT License and copyright notice for the software and project configuration files. |

# Source listings {#source-listings}

Each code block is a complete file under the filename in its heading.

## Theorem52.lean {#source-theorem52-lean}

Derives the first variation, stationarity criterion, and Einstein specialization under the stated boundary and separation hypotheses.

~~~lean
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.LinearAlgebra.BilinearMap
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# Geometric Unity: Theorem 5.2

The first variation of the action at fixed background, metric and dressing
(Eqs. (46)–(47) of the technical note).
Indexed coefficients take values in a real associative algebra. The
linear functional `trace` represents the integrated cyclic trace. The
Leibniz and parallelism hypotheses express the covariant product rule in
components. `BoundaryZero` is the integrated divergence identity for the
mixed terms involving the test field, supplied by Stokes' theorem in the
geometric setting.

The output uses raised components, so the sign of an orthonormal metric
enters the mass term through `g`. The fixed factor `i` of the commutator
channel is absorbed into its insertion `Q`. No topology or continuity
assumptions on the coefficient algebra are needed for the real derivative
along a line.

Checked with Lean 4.33.1 and Mathlib v4.33.1.
-/

namespace GeometricUnity.Theorem52

noncomputable section

open scoped BigOperators

variable {A : Type*} [Ring A] [Algebra ℝ A]
variable {ι : Type*} [Fintype ι]

abbrev OneForm (ι A : Type*) := ι → A
abbrev TwoForm (ι A : Type*) := ι → ι → A
abbrev Insertion (ι A : Type*) := ι → ι → ι → A
abbrev Bracket (A : Type*) [Ring A] [Algebra ℝ A] := A →ₗ[ℝ] A →ₗ[ℝ] A

def anti : Bracket A :=
  LinearMap.mk₂ ℝ (fun x y => x * y + y * x)
    (by intros; simp only [add_mul, mul_add]; abel)
    (by intros; simp [smul_add])
    (by intros; simp only [add_mul, mul_add]; abel)
    (by intros; simp [smul_add])

def comm : Bracket A :=
  LinearMap.mk₂ ℝ (fun x y => x * y - y * x)
    (by intros; simp only [add_mul, mul_add]; abel)
    (by intros; simp [smul_sub])
    (by intros; simp only [add_mul, mul_add]; abel)
    (by intros; simp [smul_sub])

theorem anti_apply (x y : A) : anti x y = x * y + y * x := rfl
theorem comm_apply (x y : A) : comm x y = x * y - y * x := rfl

structure Alternating (P : Insertion ι A) : Prop where
  swapBC (a b c : ι) : P a c b = -P a b c
  swapAC (a b c : ι) : P c b a = -P a b c

omit [Algebra ℝ A] [Fintype ι] in
private theorem Alternating.cycle {P : Insertion ι A} (h : Alternating P) (a b c : ι) :
    P c a b = P a b c := by
  rw [h.swapBC c b a, h.swapAC a b c, neg_neg]

omit [Algebra ℝ A] [Fintype ι] in
private theorem Alternating.cycle' {P : Insertion ι A} (h : Alternating P) (a b c : ι) :
    P b c a = P a b c :=
  (h.cycle c a b).trans (h.cycle a b c)

variable (trace : A →ₗ[ℝ] ℝ)

def Cyclic : Prop := ∀ x y : A, trace (x * y) = trace (y * x)

def sum3 {B : Type*} [AddCommMonoid B] (f : ι → ι → ι → B) : B :=
  ∑ a, ∑ b, ∑ c, f a b c

private theorem sum3_swapBC {B : Type*} [AddCommMonoid B] (f : ι → ι → ι → B) :
    sum3 (fun a b c => f a c b) = sum3 f := by
  unfold sum3
  exact Finset.sum_congr rfl (fun a _ => Finset.sum_comm)

private theorem sum3_cycle {B : Type*} [AddCommMonoid B] (f : ι → ι → ι → B) :
    sum3 (fun a b c => f c a b) = sum3 f := by
  unfold sum3
  calc
    (∑ a, ∑ b, ∑ c, f c a b) = ∑ a, ∑ c, ∑ b, f c a b :=
      Finset.sum_congr rfl (fun _ _ => Finset.sum_comm)
    _ = ∑ c, ∑ a, ∑ b, f c a b := Finset.sum_comm

private theorem sum3_cycle' {B : Type*} [AddCommMonoid B] (f : ι → ι → ι → B) :
    sum3 (fun a b c => f b c a) = sum3 f :=
  (sum3_cycle (fun a b c => f c a b)).trans (sum3_cycle f)

private theorem sum3_swapAC {B : Type*} [AddCommMonoid B] (f : ι → ι → ι → B) :
    sum3 (fun a b c => f c b a) = sum3 f :=
  (sum3_cycle (fun a b c => f a c b)).trans (sum3_swapBC f)

private theorem sum3_add (f h : ι → ι → ι → ℝ) :
    sum3 (fun a b c => f a b c + h a b c) = sum3 f + sum3 h := by
  simp [sum3, Finset.sum_add_distrib]

private theorem sum3_sub (f h : ι → ι → ι → ℝ) :
    sum3 (fun a b c => f a b c - h a b c) = sum3 f - sum3 h := by
  simp [sum3, Finset.sum_sub_distrib]

private theorem sum3_neg (f : ι → ι → ι → ℝ) :
    sum3 (fun a b c => -f a b c) = -sum3 f := by
  simp [sum3, Finset.sum_neg_distrib]

private theorem sum3_congr {f h : ι → ι → ι → ℝ}
    (heq : ∀ a b c, f a b c = h a b c) : sum3 f = sum3 h :=
  congrArg sum3 (funext fun a => funext fun b => funext fun c => heq a b c)

private theorem rotate (h : Cyclic trace) (x y z : A) :
    trace (x * (y * z)) = trace (y * (z * x)) := by
  rw [h x (y * z), mul_assoc]

private theorem trace_anti_swap (h : Cyclic trace) (x p y : A) :
    trace (x * anti p y) = trace (y * anti p x) := by
  simp only [anti_apply, mul_add, map_add]
  rw [rotate trace h x p y, rotate trace h p y x, rotate trace h x y p]
  abel

private theorem trace_comm_swap (h : Cyclic trace) (x p y : A) :
    trace (x * comm p y) = -trace (y * comm p x) := by
  simp only [comm_apply, mul_sub, map_sub]
  rw [rotate trace h x p y, rotate trace h p y x, rotate trace h x y p]
  abel

private theorem trace_comm_shift (h : Cyclic trace) (x p y : A) :
    trace (x * comm p y) = -trace (p * comm x y) := by
  simp only [comm_apply, mul_sub, map_sub]
  rw [rotate trace h x p y, rotate trace h x y p, rotate trace h y p x]
  abel

variable (D : ι → A →ₗ[ℝ] A)

def Leibniz : Prop := ∀ b x y, D b (x * y) = D b x * y + x * D b y
def Parallel (P : Insertion ι A) : Prop := ∀ a b c, D b (P a b c) = 0

/-- The integrated trace of the divergence of the indicated mixed product. -/
def BoundaryZero (B : Bracket A) (P : Insertion ι A) (X Y : OneForm ι A) : Prop :=
  sum3 (fun a b c => trace (D b (X a * B (P a b c) (Y c)))) = 0

def dB (T : OneForm ι A) : TwoForm ι A := fun b c => D b (T c) - D c (T b)

def wedgeSquare (T : OneForm ι A) : TwoForm ι A := fun b c => comm (T b) (T c)

/-- Bare contraction with the explicit factor of one half. -/
def theta (B : Bracket A) (P : Insertion ι A) (F : TwoForm ι A) : OneForm ι A :=
  fun a => (1 / 2 : ℝ) • ∑ b, ∑ c, B (P a b c) (F b c)

def pair (X Y : OneForm ι A) : ℝ := ∑ a, trace (X a * Y a)

def raise (g : ι → ℝ) (T : OneForm ι A) : OneForm ι A := fun a => g a • T a

def action (g : ι → ℝ) (P Q : Insertion ι A) (F : TwoForm ι A)
    (lam m : ℝ) (T : OneForm ι A) : ℝ :=
  let H := F + (1 / 2 : ℝ) • dB D T + lam • wedgeSquare T
  pair trace T (theta anti P H + theta comm Q H) + m * pair trace T (raise g T)

def correction (P : Insertion ι A) (lam : ℝ) (T : OneForm ι A) : OneForm ι A :=
  fun a => (-lam) • ∑ b, ∑ c, anti (T b) (comm (T c) (P a b c))

def euler (g : ι → ℝ) (P Q : Insertion ι A) (F : TwoForm ι A)
    (lam m : ℝ) (T : OneForm ι A) : OneForm ι A :=
  theta anti P (F + dB D T + (3 * lam) • wedgeSquare T) +
    theta comm Q F + (2 * m) • raise g T + correction P lam T

private def contraction (B : Bracket A) (P : Insertion ι A) (F : TwoForm ι A)
    (X : OneForm ι A) : ℝ :=
  sum3 fun a b c => trace (X a * B (P a b c) (F b c))

private def kinetic (B : Bracket A) (P : Insertion ι A) (X Y : OneForm ι A) : ℝ :=
  sum3 fun a b c => trace (X a * B (P a b c) (D b (Y c)))

private def cubic (B : Bracket A) (P : Insertion ι A) (X Y Z : OneForm ι A) : ℝ :=
  sum3 fun a b c => trace (X a * B (P a b c) (comm (Y b) (Z c)))

private def correctionTerm (P : Insertion ι A) (X T : OneForm ι A) : ℝ :=
  sum3 fun a b c => trace (X a * anti (T b) (comm (T c) (P a b c)))

private theorem pair_add_right (X Y Z : OneForm ι A) :
    pair trace X (Y + Z) = pair trace X Y + pair trace X Z := by
  simp [pair, Pi.add_apply, mul_add, Finset.sum_add_distrib]

private theorem pair_smul_right (r : ℝ) (X Y : OneForm ι A) :
    pair trace X (r • Y) = r * pair trace X Y := by
  simp [pair, Pi.smul_apply, Finset.mul_sum, smul_eq_mul]

private theorem pair_theta (B : Bracket A) (P : Insertion ι A) (F : TwoForm ι A)
    (X : OneForm ι A) : pair trace X (theta B P F) = (1 / 2) * contraction trace B P F X := by
  simp [pair, theta, contraction, sum3, Finset.mul_sum, map_sum, smul_eq_mul]

private theorem contraction_add (B : Bracket A) (P : Insertion ι A) (F H : TwoForm ι A)
    (X : OneForm ι A) :
    contraction trace B P (F + H) X = contraction trace B P F X + contraction trace B P H X := by
  simp [contraction, Pi.add_apply, mul_add, sum3_add]

private theorem contraction_smul (B : Bracket A) (P : Insertion ι A) (F : TwoForm ι A)
    (r : ℝ) (X : OneForm ι A) :
    contraction trace B P (r • F) X = r * contraction trace B P F X := by
  simp [contraction, sum3, Pi.smul_apply, Finset.mul_sum, smul_eq_mul]

private theorem contraction_dB (B : Bracket A) (P : Insertion ι A) (h : Alternating P)
    (X Y : OneForm ι A) : contraction trace B P (dB D Y) X = 2 * kinetic trace D B P X Y := by
  have swap : sum3 (fun a b c => trace (X a * B (P a b c) (D c (Y b)))) =
      -kinetic trace D B P X Y := by
    rw [← sum3_swapBC (fun a b c => trace (X a * B (P a b c) (D c (Y b))))]
    unfold kinetic
    rw [← sum3_neg]
    apply sum3_congr
    intro a b c
    rw [h.swapBC a b c, map_neg, LinearMap.neg_apply, mul_neg, map_neg]
  simp only [contraction, dB, map_sub, mul_sub, sum3_sub, swap]
  change kinetic trace D B P X Y - -kinetic trace D B P X Y = _
  ring

private theorem pair_correction (P : Insertion ι A) (lam : ℝ) (X T : OneForm ι A) :
    pair trace X (correction P lam T) = -lam * correctionTerm trace P X T := by
  simp [pair, correction, correctionTerm, sum3, Finset.mul_sum, map_sum,
    smul_eq_mul]

private theorem kinetic_swap (B : Bracket A) (P : Insertion ι A) (hp : Alternating P)
    (hD : Leibniz D) (hP : Parallel D P)
    (hbracket : ∀ b x y, D b (B x y) = B (D b x) y + B x (D b y))
    (s : ℝ) (hs : ∀ x p y, trace (x * B p y) = s * trace (y * B p x))
    (X Y : OneForm ι A) (hzero : BoundaryZero trace D B P X Y) :
    kinetic trace D B P X Y = s * kinetic trace D B P Y X := by
  let f := fun a b c => trace (D b (X a) * B (P a b c) (Y c))
  let k := fun a b c => trace (X a * B (P a b c) (D b (Y c)))
  have hprod (a b c : ι) :
      trace (D b (X a * B (P a b c) (Y c))) = f a b c + k a b c := by
    dsimp [f, k]
    rw [hD b, hbracket b, hP a b c, map_zero, LinearMap.zero_apply, zero_add, map_add]
  have hz : sum3 f + sum3 k = 0 := by
    rw [← sum3_add, ← sum3_congr hprod]
    exact hzero
  have ibp : sum3 k = -sum3 f := by
    linarith
  calc
    kinetic trace D B P X Y = -sum3 f := ibp
    _ = sum3 (fun a b c => s * trace (Y c * B (P c b a) (D b (X a)))) := by
      rw [← sum3_neg]
      apply sum3_congr
      intro a b c
      dsimp [f]
      rw [hs, hp.swapAC a b c, map_neg, LinearMap.neg_apply, mul_neg, map_neg, mul_neg]
    _ = _ := by rw [sum3_swapAC]; simp [kinetic, sum3, Finset.mul_sum]

private theorem kinetic_plus_symm (P : Insertion ι A) (hp : Alternating P)
    (hcyc : Cyclic trace) (hD : Leibniz D) (hP : Parallel D P)
    (X Y : OneForm ι A) (hzero : BoundaryZero trace D anti P X Y) :
    kinetic trace D anti P X Y = kinetic trace D anti P Y X := by
  have h := kinetic_swap trace D anti P hp hD hP
    (by intro b x y; simp only [anti_apply, map_add, hD b]; abel)
    1 (by intro x p y; rw [one_mul]; exact trace_anti_swap trace hcyc x p y) X Y hzero
  simpa using h

private theorem kinetic_minus_skew (Q : Insertion ι A) (hq : Alternating Q)
    (hcyc : Cyclic trace) (hD : Leibniz D) (hQ : Parallel D Q)
    (X Y : OneForm ι A) (hzero : BoundaryZero trace D comm Q X Y) :
    kinetic trace D comm Q X Y = -kinetic trace D comm Q Y X := by
  have h := kinetic_swap trace D comm Q hq hD hQ
    (by intro b x y; simp only [comm_apply, map_sub, hD b]; abel)
    (-1) (by intro x p y; rw [neg_one_mul]; exact trace_comm_swap trace hcyc x p y) X Y hzero
  simpa using h

private theorem cubic_minus_zero (Q : Insertion ι A) (hq : Alternating Q)
    (hcyc : Cyclic trace) (T : OneForm ι A) :
    cubic trace comm Q T T T = 0 := by
  let f := fun a b c => trace (Q a b c * comm (T a) (comm (T b) (T c)))
  have h1 : sum3 (fun a b c => trace (Q a b c * comm (T c) (comm (T a) (T b)))) =
      sum3 f := by
    calc
      _ = sum3 (fun a b c => f c a b) := by
        apply sum3_congr
        intro a b c
        dsimp [f]
        rw [hq.cycle a b c]
      _ = _ := sum3_cycle f
  have h2 : sum3 (fun a b c => trace (Q a b c * comm (T b) (comm (T c) (T a)))) =
      sum3 f := by
    calc
      _ = sum3 (fun a b c => f b c a) := by
        apply sum3_congr
        intro a b c
        dsimp [f]
        rw [hq.cycle' a b c]
      _ = _ := sum3_cycle' f
  have jacobi (x y z : A) : comm x (comm y z) + comm y (comm z x) + comm z (comm x y) = 0 := by
    simp only [comm_apply]
    noncomm_ring
  have hs : sum3 f + sum3 f + sum3 f = 0 := by
    -- Combine exactly one copy from each cyclic placement.
    calc
      _ = sum3 (fun a b c =>
        trace (Q a b c * (comm (T a) (comm (T b) (T c)) +
          comm (T b) (comm (T c) (T a)) + comm (T c) (comm (T a) (T b))))) := by
        simp only [mul_add, map_add, sum3_add]
        rw [h1, h2]
      _ = 0 := by simp [jacobi, sum3]
  calc
    cubic trace comm Q T T T = sum3 (fun a b c => -f a b c) := by
      apply sum3_congr
      intro a b c
      exact trace_comm_shift trace hcyc _ _ _
    _ = 0 := by rw [sum3_neg]; linarith

private theorem cubic_move (P : Insertion ι A) (hp : Alternating P)
    (hcyc : Cyclic trace) (T X : OneForm ι A) :
    cubic trace anti P T X T =
      sum3 (fun a b c => trace (X a * comm (T b) (anti (P a b c) (T c)))) := by
  calc
    _ = sum3 (fun a b c => trace (X b * comm (T c) (anti (P a b c) (T a)))) := by
      apply sum3_congr
      intro a b c
      rw [trace_anti_swap trace hcyc]
      simp only [comm_apply, sub_mul, map_sub, mul_assoc, mul_sub]
      rw [rotate trace hcyc (T c) (X b) (anti (P a b c) (T a))]
    _ = _ := by
      let f := fun a b c => trace (X a * comm (T b) (anti (P a b c) (T c)))
      calc
        _ = sum3 (fun a b c => f b c a) := by
          apply sum3_congr
          intro a b c
          dsimp [f]
          rw [hp.cycle' a b c]
        _ = _ := sum3_cycle' f

private theorem cubic_exchange (P : Insertion ι A) (hp : Alternating P) (X Y Z : OneForm ι A) :
    cubic trace anti P X Y Z = cubic trace anti P X Z Y := by
  unfold cubic
  rw [← sum3_swapBC (fun a b c => trace (X a * anti (P a b c) (comm (Z b) (Y c))))]
  apply sum3_congr
  intro a b c
  have flip : comm (Z c) (Y b) = -comm (Y b) (Z c) := by
    simp only [comm_apply]
    abel
  simp only [hp.swapBC a b c, flip, map_neg, LinearMap.neg_apply, neg_neg]

private theorem cubic_move_value (P : Insertion ι A) (hp : Alternating P)
    (hcyc : Cyclic trace) (T X : OneForm ι A) :
    cubic trace anti P T X T = cubic trace anti P X T T - correctionTerm trace P X T := by
  let r := fun a b c => trace (X a * comm (anti (T b) (T c)) (P a b c))
  have hr := sum3_swapBC r
  have hf : ∀ a b c, r a c b = -r a b c := by
    intro a b c
    change trace (X a * comm (anti (T c) (T b)) (P a c b)) = _
    rw [hp.swapBC a b c, map_neg, mul_neg, map_neg]
    simp only [r, anti_apply, add_comm (T c * T b) (T b * T c)]
  have hz : sum3 r = 0 := by
    have hneg : sum3 (fun a b c => r a c b) = -sum3 r :=
      (sum3_congr hf).trans (sum3_neg r)
    linarith
  have rearrange (b c p : A) :
      comm b (anti p c) = anti p (comm b c) - anti b (comm c p) + comm (anti b c) p := by
    simp only [comm_apply, anti_apply]
    noncomm_ring
  rw [cubic_move trace P hp hcyc T X]
  simp only [rearrange, mul_add, mul_sub, map_add, map_sub, sum3_add, sum3_sub]
  change cubic trace anti P X T T - correctionTerm trace P X T + sum3 r = _
  rw [hz, add_zero]

/-! The action on an affine line is a real scalar polynomial of degree at most
three. The following lemmas differentiate it without a topology on `A`. -/

private theorem polynomial_deriv (c₀ c₁ c₂ c₃ : ℝ) :
    HasDerivAt (fun t : ℝ => c₀ + t * c₁ + t ^ 2 * c₂ + t ^ 3 * c₃) c₁ 0 := by
  have h := (((hasDerivAt_const (0 : ℝ) c₀).fun_add
      ((hasDerivAt_id' (x := (0 : ℝ))).mul_const c₁)).fun_add
      ((hasDerivAt_pow 2 (0 : ℝ)).mul_const c₂)).fun_add
      ((hasDerivAt_pow 3 (0 : ℝ)).mul_const c₃)
  simpa using h

private theorem trace_line2 (x dx y dy : A) :
    HasDerivAt (fun t : ℝ => trace ((x + t • dx) * (y + t • dy)))
      (trace (dx * y) + trace (x * dy)) 0 := by
  have heq : (fun t : ℝ => trace ((x + t • dx) * (y + t • dy))) =
      fun t => trace (x * y) + t * (trace (dx * y) + trace (x * dy)) +
        t ^ 2 * trace (dx * dy) + t ^ 3 * 0 := by
    funext t
    simp only [add_mul, mul_add, smul_mul_assoc, mul_smul_comm,
      map_add, map_smul, smul_eq_mul]
    ring
  rw [heq]
  exact polynomial_deriv _ _ _ _

private theorem trace_line3 (B : Bracket A) (L : A →ₗ[ℝ] A) (x dx y dy z dz : A) :
    HasDerivAt (fun t : ℝ => trace ((x + t • dx) * L (B (y + t • dy) (z + t • dz))))
      (trace (dx * L (B y z)) + trace (x * L (B dy z)) + trace (x * L (B y dz))) 0 := by
  let f := fun x y z => trace (x * L (B y z))
  have heq : (fun t : ℝ => f (x + t • dx) (y + t • dy) (z + t • dz)) =
      fun t => f x y z + t * (f dx y z + f x dy z + f x y dz) +
        t ^ 2 * (f dx dy z + f dx y dz + f x dy dz) + t ^ 3 * f dx dy dz := by
    funext t
    simp only [f, map_add, map_smul, LinearMap.add_apply, LinearMap.smul_apply,
      smul_mul_assoc, mul_smul_comm, add_mul, mul_add, smul_eq_mul]
    ring
  change HasDerivAt (fun t : ℝ => f (x + t • dx) (y + t • dy) (z + t • dz)) _ _
  rw [heq]
  exact polynomial_deriv _ _ _ _

private theorem sum3_deriv {f : ι → ι → ι → ℝ → ℝ} {f' : ι → ι → ι → ℝ}
    (h : ∀ a b c, HasDerivAt (f a b c) (f' a b c) 0) :
    HasDerivAt (fun t => sum3 (fun a b c => f a b c t)) (sum3 f') 0 :=
  HasDerivAt.fun_sum fun a _ =>
    HasDerivAt.fun_sum fun b _ =>
      HasDerivAt.fun_sum fun c _ => h a b c

private theorem contraction_deriv (B : Bracket A) (P : Insertion ι A) (F : TwoForm ι A)
    (T X : OneForm ι A) :
    HasDerivAt (fun t : ℝ => contraction trace B P F (T + t • X))
      (contraction trace B P F X) 0 := by
  unfold contraction
  apply sum3_deriv
  intro a b c
  simpa only [Pi.add_apply, Pi.smul_apply, smul_zero, add_zero, mul_zero, map_zero] using
    trace_line2 trace (T a) (X a) (B (P a b c) (F b c)) 0

private theorem kinetic_deriv (B : Bracket A) (P : Insertion ι A) (T X : OneForm ι A) :
    HasDerivAt (fun t : ℝ => kinetic trace D B P (T + t • X) (T + t • X))
      (kinetic trace D B P X T + kinetic trace D B P T X) 0 := by
  unfold kinetic
  rw [← sum3_add]
  apply sum3_deriv
  intro a b c
  simpa only [Pi.add_apply, Pi.smul_apply, map_add, map_smul] using
    trace_line2 trace (T a) (X a) (B (P a b c) (D b (T c))) (B (P a b c) (D b (X c)))

private theorem cubic_deriv (B : Bracket A) (P : Insertion ι A) (T X : OneForm ι A) :
    HasDerivAt (fun t : ℝ => cubic trace B P (T + t • X) (T + t • X) (T + t • X))
      (cubic trace B P X T T + cubic trace B P T X T + cubic trace B P T T X) 0 := by
  unfold cubic
  rw [← sum3_add, ← sum3_add]
  apply sum3_deriv
  intro a b c
  exact trace_line3 trace comm (B (P a b c)) (T a) (X a) (T b) (X b) (T c) (X c)

private theorem mass_deriv (g : ι → ℝ) (hcyc : Cyclic trace) (T X : OneForm ι A) :
    HasDerivAt (fun t : ℝ => pair trace (T + t • X) (raise g (T + t • X)))
      (2 * pair trace X (raise g T)) 0 := by
  have h (a : ι) : HasDerivAt
      (fun t : ℝ => trace ((T + t • X) a * raise g (T + t • X) a))
      (2 * trace (X a * raise g T a)) 0 := by
    have hc : trace (T a * (g a • X a)) = trace (X a * (g a • T a)) := by
      simp only [mul_smul_comm, map_smul, hcyc (T a) (X a)]
    have hd := trace_line2 trace (T a) (X a) (g a • T a) (g a • X a)
    simpa only [raise, Pi.add_apply, Pi.smul_apply, smul_add, smul_comm (g a), hc, two_mul] using hd
  simpa only [pair, Finset.mul_sum] using HasDerivAt.fun_sum (fun a _ => h a)

private theorem action_reduced (g : ι → ℝ) (P Q : Insertion ι A) (F : TwoForm ι A)
    (hp : Alternating P) (hq : Alternating Q) (hcyc : Cyclic trace)
    (lam m : ℝ) (T : OneForm ι A) :
    action trace D g P Q F lam m T =
      (1 / 2) * (contraction trace anti P F T + contraction trace comm Q F T +
        kinetic trace D anti P T T + kinetic trace D comm Q T T) +
      (lam / 2) * cubic trace anti P T T T + m * pair trace T (raise g T) := by
  simp only [action, pair_add_right, pair_theta, contraction_add, contraction_smul,
    contraction_dB trace D anti P hp, contraction_dB trace D comm Q hq]
  change (1 / 2 : ℝ) *
      (contraction trace anti P F T + (1 / 2) * (2 * kinetic trace D anti P T T) +
        lam * cubic trace anti P T T T) +
    (1 / 2) * (contraction trace comm Q F T + (1 / 2) * (2 * kinetic trace D comm Q T T) +
        lam * cubic trace comm Q T T T) + m * pair trace T (raise g T) = _
  rw [cubic_minus_zero trace Q hq hcyc T]
  ring

/-- The real derivative in direction `α` is the trace pairing with the full
Euler expression, including the quadratic correction. -/
theorem theorem_5_2 (g : ι → ℝ) (P Q : Insertion ι A) (F : TwoForm ι A)
    (hp : Alternating P) (hq : Alternating Q) (hcyc : Cyclic trace) (hD : Leibniz D)
    (hP : Parallel D P) (hQ : Parallel D Q) (lam m : ℝ) (T α : OneForm ι A)
    (hbP : BoundaryZero trace D anti P T α) (hbQ : BoundaryZero trace D comm Q T α) :
    HasDerivAt (fun t : ℝ => action trace D g P Q F lam m (T + t • α))
      (pair trace α (euler D g P Q F lam m T)) 0 := by
  simp_rw [action_reduced trace D g P Q F hp hq hcyc lam m]
  have h :=
    ((((contraction_deriv trace anti P F T α).add
      (contraction_deriv trace comm Q F T α)).add
      (kinetic_deriv trace D anti P T α)).add
      (kinetic_deriv trace D comm Q T α)).const_mul (1 / 2)
  have hv := (h.add ((cubic_deriv trace anti P T α).const_mul (lam / 2))).add
    ((mass_deriv trace g hcyc T α).const_mul m)
  apply hv.congr_deriv
  rw [kinetic_plus_symm trace D P hp hcyc hD hP T α hbP,
    kinetic_minus_skew trace D Q hq hcyc hD hQ T α hbQ,
    cubic_exchange trace P hp T T α, cubic_move_value trace P hp hcyc T α]
  simp only [euler, pair_add_right, pair_theta, contraction_add, contraction_smul,
    contraction_dB trace D anti P hp, pair_smul_right, pair_correction]
  change _ = (1 / 2 : ℝ) *
    (contraction trace anti P F α + 2 * kinetic trace D anti P α T +
      (3 * lam) * cubic trace anti P α T T) +
    (1 / 2) * contraction trace comm Q F α + (2 * m) * pair trace α (raise g T) +
    (-lam) * correctionTerm trace P α T
  ring

/-- Stationarity is equivalent to vanishing of the Euler expression
if the trace pairing separates the coefficients against the test fields. -/
theorem stationary_iff (g : ι → ℝ) (P Q : Insertion ι A) (F : TwoForm ι A)
    (hp : Alternating P) (hq : Alternating Q) (hcyc : Cyclic trace) (hD : Leibniz D)
    (hP : Parallel D P) (hQ : Parallel D Q) (lam m : ℝ) (T : OneForm ι A)
    (admissible : OneForm ι A → Prop)
    (hbP : ∀ α, admissible α → BoundaryZero trace D anti P T α)
    (hbQ : ∀ α, admissible α → BoundaryZero trace D comm Q T α)
    (separates : ∀ E : OneForm ι A, (∀ α, admissible α → pair trace α E = 0) → E = 0) :
    (∀ α, admissible α → deriv (fun t : ℝ => action trace D g P Q F lam m (T + t • α)) 0 = 0) ↔
    euler D g P Q F lam m T = 0 := by
  have h (α) (hα : admissible α) :=
    (theorem_5_2 trace D g P Q F hp hq hcyc hD hP hQ lam m T α (hbP α hα) (hbQ α hα)).deriv
  constructor
  · intro hs
    apply separates
    intro α hα
    rw [← h α hα]
    exact hs α hα
  · intro heq α hα
    rw [h α hα]
    simp [heq, pair]

omit [Fintype ι] in
private theorem adjoint_comm (sharp : A →ₗ[ℝ] A)
    (hrev : ∀ x y, sharp (x * y) = sharp y * sharp x)
    (x p : A) (hx : sharp x = -x) (hp : sharp p = p) :
    sharp (comm x p) = comm x p := by
  simp only [comm_apply, map_sub, hrev, hx, hp, mul_neg, neg_mul]
  abel

/-- A skew-adjoint torsion and self-adjoint insertion give a skew-adjoint
correction. Here `sharp` is the coefficient adjoint on the real algebra. -/
theorem correction_skew (sharp : A →ₗ[ℝ] A)
    (hrev : ∀ x y, sharp (x * y) = sharp y * sharp x)
    (T : OneForm ι A) (P : Insertion ι A) (lam : ℝ)
    (hT : ∀ a, sharp (T a) = -T a) (hP : ∀ a b c, sharp (P a b c) = P a b c)
    (a : ι) : sharp (correction P lam T a) = -correction P lam T a := by
  have h (b c : ι) : sharp (anti (T b) (comm (T c) (P a b c))) =
      -anti (T b) (comm (T c) (P a b c)) := by
    have hc := adjoint_comm sharp hrev (T c) (P a b c) (hT c) (hP a b c)
    simp only [anti_apply, map_add, hrev, hT b, hc, mul_neg, neg_mul]
    abel
  simp only [correction, map_smul, map_sum, h, Finset.sum_neg_distrib, smul_neg]

/-- Local component formula for the background covariant derivative. -/
def covariant (d : ι → A →ₗ[ℝ] A) (B : OneForm ι A) : ι → A →ₗ[ℝ] A :=
  fun b => d b + comm (B b)

def curvature (d : ι → A →ₗ[ℝ] A) (B : OneForm ι A) : TwoForm ι A :=
  dB d B + wedgeSquare B

omit [Fintype ι] in
theorem curvature_shift (d : ι → A →ₗ[ℝ] A) (B T : OneForm ι A) :
    curvature d (B + T) = curvature d B + dB (covariant d B) T + wedgeSquare T := by
  funext a b
  simp only [curvature, dB, covariant, wedgeSquare, Pi.add_apply, LinearMap.add_apply,
    map_add, comm_apply]
  noncomm_ring

/-- At the Einstein couplings the first term is the contraction of the full
curvature, and the mass coefficient is `κ`. The correction persists. -/
theorem einstein_euler (d : ι → A →ₗ[ℝ] A) (g : ι → ℝ) (P : Insertion ι A)
    (B T : OneForm ι A) (κ : ℝ) :
    euler (covariant d B) g P 0 (curvature d B) (1 / 3) (κ / 2) T =
      theta anti P (curvature d (B + T)) + κ • raise g T + correction P (1 / 3) T := by
  rw [euler, curvature_shift]
  have h₁ : (3 * (1 / 3) : ℝ) = 1 := by norm_num
  have h₂ : 2 * (κ / 2) = κ := by ring
  simp only [h₁, h₂, one_smul]
  have hQ : theta comm (0 : Insertion ι A) (curvature d B) = 0 := by
    funext a
    simp [theta]
  rw [hQ, add_zero]

end

end GeometricUnity.Theorem52
~~~

[Return to file index](#file-index)

## WitnessW1.lean {#source-witnessw1-lean}

Constructs the exact nonzero torsion correction in the split Clifford algebra and checks the test blade and trace pairing.

~~~lean
import Mathlib.Algebra.CharP.Invertible
import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.CliffordAlgebra.Contraction
import Mathlib.LinearAlgebra.CliffordAlgebra.Conjugation
import Mathlib.Tactic.Module
import Mathlib.Tactic.NormNum

/-!
# Geometric Unity: Witness W1

Proposition 5.3, Eq. (57) of the technical note. The calculation takes place
in the real Clifford algebra of the actual split quadratic form on 14 axes.
The indices 0 through 6 have positive square and 7 through 13 have negative
square. The witness uses the first five positive generators.

Checked with Lean 4.33.1 and Mathlib v4.33.1.
-/

namespace GeometricUnity.WitnessW1

abbrev Index := Fin 14

def metricSign (i : Index) : ℝ := if i.val < 7 then 1 else -1

def splitForm : QuadraticForm ℝ (Index → ℝ) :=
  QuadraticMap.weightedSumSquares ℝ metricSign

abbrev Cl := CliffordAlgebra splitForm

noncomputable def basisVector (i : Index) : Index → ℝ := Pi.single i 1

noncomputable def gamma (i : Index) : Cl := CliffordAlgebra.ι splitForm (basisVector i)

theorem gamma_square (i : Index) : gamma i * gamma i = algebraMap ℝ Cl (metricSign i) := by
  rw [gamma, CliffordAlgebra.ι_sq_scalar]
  congr 1
  simp [splitForm, QuadraticMap.weightedSumSquares_apply, basisVector, Pi.single_apply]

theorem gamma_anticommute (i j : Index) (h : i ≠ j) :
    gamma i * gamma j = -(gamma j * gamma i) := by
  apply CliffordAlgebra.ι_mul_ι_comm_of_isOrtho
  rw [← QuadraticMap.isOrtho_polarBilin, QuadraticMap.polarBilin_apply_apply, QuadraticMap.polar]
  simp only [splitForm, QuadraticMap.weightedSumSquares_apply]
  rw [← Finset.sum_sub_distrib, ← Finset.sum_sub_distrib]
  apply Finset.sum_eq_zero
  intro k _
  by_cases ki : k = i
  · subst k
    simp [basisVector, h]
  by_cases kj : k = j
  · subst k
    simp [basisVector, h.symm]
  · simp [basisVector, ki, kj]

noncomputable def comm (X Y : Cl) : Cl := X * Y - Y * X
noncomputable def anti (X Y : Cl) : Cl := X * Y + Y * X

noncomputable def torsion (a : Index) : Cl :=
  if a = 1 then gamma 3 else if a = 2 then gamma 4 else 0

/-- The undressed insertion gamma_a{}^{bc}, including the two metric signs. -/
noncomputable def insertion (a b c : Index) : Cl :=
  if a = b ∨ a = c ∨ b = c then 0
  else (metricSign b * metricSign c) • (gamma a * gamma b * gamma c)

noncomputable def correction (a : Index) : Cl :=
  -(1 / 3 : ℝ) • (∑ b, ∑ c, anti (torsion b) (comm (torsion c) (insertion a b c)))

noncomputable def blade : Cl := gamma 0 * gamma 1 * gamma 2 * gamma 3 * gamma 4

private theorem swapDescending {i j : Index} (h : j < i) (x : Cl) :
    gamma i * (gamma j * x) = -(gamma j * (gamma i * x)) := by
  rw [← mul_assoc, gamma_anticommute i j (ne_of_gt h), neg_mul, mul_assoc]

private theorem swapLast {i j : Index} (h : j < i) :
    gamma i * gamma j = -(gamma j * gamma i) :=
  gamma_anticommute i j (ne_of_gt h)

private theorem cancelPositive {i : Index} (h : i.val < 7) (x : Cl) :
    gamma i * (gamma i * x) = x := by
  rw [← mul_assoc, gamma_square, metricSign, if_pos h, map_one, one_mul]

private theorem sum_supported {B : Type*} [AddCommMonoid B] (f : Index → B)
    (hf : ∀ i, i ≠ 1 → i ≠ 2 → f i = 0) :
    ∑ i, f i = f 1 + f 2 := by
  calc
    ∑ i, f i = ∑ i ∈ ({1, 2} : Finset Index), f i := by
      symm
      apply Finset.sum_subset (Finset.subset_univ _)
      intro i _ hi
      exact hf i (fun h => hi (by simp [h])) (fun h => hi (by simp [h]))
    _ = f 1 + f 2 := by simp

private theorem sum_correction (a : Index) :
    correction a =
      -(1 / 3 : ℝ) •
        (anti (gamma 3) (comm (gamma 4) (insertion a 1 2)) +
         anti (gamma 4) (comm (gamma 3) (insertion a 2 1))) := by
  unfold correction
  rw [sum_supported (fun b => ∑ c, anti (torsion b) (comm (torsion c) (insertion a b c)))]
  · simp_rw [sum_supported (fun c => anti (torsion 1) (comm (torsion c) (insertion a 1 c)))
        (by intro i hi hj; simp [torsion, hi, hj, comm, anti]),
      sum_supported (fun c => anti (torsion 2) (comm (torsion c) (insertion a 2 c)))
        (by intro i hi hj; simp [torsion, hi, hj, comm, anti])]
    simp [torsion, insertion, comm, anti]
  · intro i hi hj
    simp [torsion, hi, hj, anti]

private theorem insertion_012 : insertion 0 1 2 = gamma 0 * gamma 1 * gamma 2 := by
  rw [insertion, if_neg (by decide)]
  norm_num [metricSign]

private theorem insertion_021 : insertion 0 2 1 = -(gamma 0 * gamma 1 * gamma 2) := by
  rw [show insertion 0 2 1 = gamma 0 * gamma 2 * gamma 1 by
    rw [insertion, if_neg (by decide)]; norm_num [metricSign],
    mul_assoc, gamma_anticommute 2 1 (by decide), mul_neg, mul_assoc]

theorem blade_square : blade * blade = 1 := by
  -- Append a final unit so each adjacent interchange has the same form.
  rw [← mul_one (blade * blade)]
  simp (disch := decide) only [blade, mul_assoc, swapDescending, cancelPositive, mul_neg,
    neg_neg]

/-- On real blades the coefficient adjoint is grade involution followed by
reversion. The variation along this blade is skew-adjoint. -/
theorem blade_skew : CliffordAlgebra.reverse (CliffordAlgebra.involute blade) = -blade := by
  have hinv (i : Index) : CliffordAlgebra.involute (gamma i) = -gamma i :=
    CliffordAlgebra.involute_ι _
  have hrev (i : Index) : CliffordAlgebra.reverse (gamma i) = gamma i :=
    CliffordAlgebra.reverse_ι _
  simp (disch := decide) only [blade, map_mul, hinv, CliffordAlgebra.reverse.map_mul, map_neg, hrev,
    neg_mul, mul_neg, mul_assoc, swapDescending, swapLast, neg_neg]

theorem correction_value : correction 0 = (-8 / 3 : ℝ) • blade := by
  rw [sum_correction, insertion_012, insertion_021]
  -- Normalize the eight words using the Clifford anticommutation relations.
  simp (disch := decide) only [anti, comm, sub_eq_add_neg, neg_mul, mul_neg, add_mul,
    mul_add, mul_assoc, swapDescending, swapLast, neg_neg, blade]
  module

theorem correction_ne_zero : correction 0 ≠ 0 := by
  rw [correction_value]
  apply smul_ne_zero (by norm_num)
  intro h
  exact (one_ne_zero : (1 : Cl) ≠ 0) (by simpa [h] using blade_square.symm)

/-- With the 128-dimensional matrix trace normalization, this is the trace
pairing density obtained by setting alpha_0 = gamma^{01234}. -/
theorem pairing_density (trace : Cl →ₗ[ℝ] ℝ) (normalized : trace 1 = 128) :
    trace (blade * correction 0) = -1024 / 3 := by
  rw [correction_value, mul_smul_comm, blade_square, map_smul, normalized]
  norm_num

end GeometricUnity.WitnessW1
~~~

[Return to file index](#file-index)

## BianchiSymbol.lean {#source-bianchisymbol-lean}

Identifies closed first jets, realizes them by closed linear two-forms, and proves unique factorization through alternation.

~~~lean
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Module
import Mathlib.Tactic.NormNum

/-!
# Geometric Unity: the Bianchi symbol criterion

In coordinates, a first jet of a two-form is an array `J a b c`
skew in its last two indices. The exterior derivative of the two-form
has components given by the cyclic sum. Every jet in the kernel of
that sum is realized by a closed linear two-form. A linear symbol
vanishes on all such jets precisely when it factors uniquely through
the projection onto alternating tensors.
-/

namespace GeometricUnity.BianchiSymbol

noncomputable section

open scoped BigOperators

variable {ι E W : Type*}
variable [AddCommGroup E] [Module ℝ E] [AddCommGroup W] [Module ℝ W]

abbrev Coefficients (ι E : Type*) := ι → ι → ι → E

def skewJets (ι E : Type*) [AddCommGroup E] [Module ℝ E] :
    Submodule ℝ (Coefficients ι E) where
  carrier := {J | ∀ a b c, J a c b = -J a b c}
  zero_mem' := by intro a b c; simp
  add_mem' := by
    intro J K hJ hK a b c
    change J a c b + K a c b = -(J a b c + K a b c)
    rw [hJ a b c, hK a b c, neg_add]
  smul_mem' := by
    intro r J hJ a b c
    change r • J a c b = -(r • J a b c)
    rw [hJ a b c, smul_neg]

abbrev Jet (ι E : Type*) [AddCommGroup E] [Module ℝ E] := ↥(skewJets ι E)

/-- For a jet already skew in its last two indices, cyclic invariance
is equivalent to total alternation. -/
def alternatingJets (ι E : Type*) [AddCommGroup E] [Module ℝ E] :
    Submodule ℝ (Jet ι E) where
  carrier := {J | ∀ a b c, J.val c a b = J.val a b c}
  zero_mem' := by intro a b c; rfl
  add_mem' := by
    intro J K hJ hK a b c
    change J.val c a b + K.val c a b = J.val a b c + K.val a b c
    rw [hJ a b c, hK a b c]
  smul_mem' := by
    intro r J hJ a b c
    change r • J.val c a b = r • J.val a b c
    rw [hJ a b c]

abbrev ThreeForm (ι E : Type*) [AddCommGroup E] [Module ℝ E] :=
  ↥(alternatingJets ι E)

theorem ThreeForm.swapFirst (J : ThreeForm ι E) (a b c : ι) :
    J.val.val b a c = -J.val.val a b c := by
  rw [J.property a c b, J.val.property a b c]

def cyclicSum (J : Coefficients ι E) (a b c : ι) : E :=
  J a b c + J b c a + J c a b

def ClosedJet (J : Jet ι E) : Prop := ∀ a b c, cyclicSum J.val a b c = 0

private def cyclicAverage : Jet ι E →ₗ[ℝ] Jet ι E where
  toFun J := ⟨fun a b c => (1 / 3 : ℝ) • cyclicSum J.val a b c, by
    intro a b c
    change (1 / 3 : ℝ) • cyclicSum J.val a c b = -((1 / 3 : ℝ) • cyclicSum J.val a b c)
    unfold cyclicSum
    rw [J.property a b c, J.property c a b, J.property b c a, ← smul_neg]
    congr 1
    abel⟩
  map_add' J K := by
    apply Subtype.ext
    funext a b c
    change (1 / 3 : ℝ) • cyclicSum (J.val + K.val) a b c =
      (1 / 3 : ℝ) • cyclicSum J.val a b c + (1 / 3 : ℝ) • cyclicSum K.val a b c
    rw [← smul_add]
    congr 1
    simp only [cyclicSum, Pi.add_apply]
    abel
  map_smul' r J := by
    apply Subtype.ext
    funext a b c
    change (1 / 3 : ℝ) • cyclicSum (r • J.val) a b c =
      r • ((1 / 3 : ℝ) • cyclicSum J.val a b c)
    simp only [cyclicSum, Pi.smul_apply, ← smul_add]
    rw [smul_comm]

/-- Alternation is the mean of the three cyclic permutations on the
space of jets skew in their last two slots. -/
def alternation : Jet ι E →ₗ[ℝ] ThreeForm ι E :=
  cyclicAverage.codRestrict (alternatingJets ι E) (by
    intro J a b c
    change (1 / 3 : ℝ) • cyclicSum J.val c a b = (1 / 3 : ℝ) • cyclicSum J.val a b c
    congr 1
    unfold cyclicSum
    abel)

theorem alternation_apply (J : Jet ι E) (a b c : ι) :
    (alternation J).val.val a b c = (1 / 3 : ℝ) • cyclicSum J.val a b c := rfl

theorem alternation_retract (F : ThreeForm ι E) : alternation F.val = F := by
  apply Subtype.ext
  apply Subtype.ext
  funext a b c
  have second : F.val.val b c a = F.val.val a b c :=
    (F.property c a b).trans (F.property a b c)
  change (1 / 3 : ℝ) • cyclicSum F.val.val a b c = F.val.val a b c
  rw [cyclicSum, second, F.property a b c]
  module

theorem closed_iff_alternation_eq_zero (J : Jet ι E) : ClosedJet J ↔ alternation J = 0 := by
  constructor
  · intro h
    apply Subtype.ext
    apply Subtype.ext
    funext a b c
    change (1 / 3 : ℝ) • cyclicSum J.val a b c = 0
    rw [h a b c, smul_zero]
  · intro h a b c
    have hh : (1 / 3 : ℝ) • cyclicSum J.val a b c = 0 :=
      congrArg (fun T : ThreeForm ι E => T.val.val a b c) h
    exact (smul_eq_zero.mp hh).resolve_left (by norm_num)

def Compatible (M : Jet ι E →ₗ[ℝ] W) : Prop := ∀ J, ClosedJet J → M J = 0

def alternatingRestriction (M : Jet ι E →ₗ[ℝ] W) : ThreeForm ι E →ₗ[ℝ] W :=
  M.comp (alternatingJets ι E).subtype

theorem value_on_alternation (M : Jet ι E →ₗ[ℝ] W) (hM : Compatible M) (J : Jet ι E) :
    M J = M (alternation J).val := by
  have hker : alternation (J - (alternation J).val) = 0 := by
    rw [map_sub, alternation_retract, sub_self]
  have hz := hM _ ((closed_iff_alternation_eq_zero _).mpr hker)
  rw [map_sub] at hz
  exact sub_eq_zero.mp hz

/-- The Bianchi-compatible symbols are exactly the maps that factor
uniquely through alternation. The factor is restriction to three-forms. -/
theorem compatible_iff_unique_factor (M : Jet ι E →ₗ[ℝ] W) :
    Compatible M ↔ ∃! L : ThreeForm ι E →ₗ[ℝ] W, M = L.comp alternation := by
  constructor
  · intro hM
    refine ⟨alternatingRestriction M, LinearMap.ext (value_on_alternation M hM), ?_⟩
    intro L hL
    apply LinearMap.ext
    intro F
    have heq := LinearMap.congr_fun hL F.val
    rw [LinearMap.comp_apply, alternation_retract] at heq
    exact heq.symm
  · rintro ⟨L, hL, _⟩ J hJ
    rw [hL, LinearMap.comp_apply, (closed_iff_alternation_eq_zero J).mp hJ, map_zero]

/-- Restriction retains the intertwining identity for any action whose
action on three-forms is the restriction of its action on jets. -/
theorem alternatingRestriction_intertwines
    (M : Jet ι E →ₗ[ℝ] W) (S : Jet ι E →ₗ[ℝ] Jet ι E)
    (S₃ : ThreeForm ι E →ₗ[ℝ] ThreeForm ι E) (T : W →ₗ[ℝ] W)
    (hS : ∀ F, S F.val = (S₃ F).val) (hM : ∀ J, M (S J) = T (M J)) :
    ∀ F, alternatingRestriction M (S₃ F) = T (alternatingRestriction M F) := by
  intro F
  change M (S₃ F).val = T (M F.val)
  rw [← hS F, hM]

section Realization

variable [Fintype ι] [DecidableEq ι]

/-- A linear two-form with coefficients given by the prescribed first jet. -/
def linearField (J : Jet ι E) (x : ι → ℝ) (b c : ι) : E :=
  ∑ a, x a • J.val a b c

omit [DecidableEq ι] in
theorem linearField_skew (J : Jet ι E) (x : ι → ℝ) (b c : ι) :
    linearField J x c b = -linearField J x b c := by
  unfold linearField
  simp only [fun a => J.property a b c, smul_neg, Finset.sum_neg_distrib]

theorem linearField_line (J : Jet ι E) (x : ι → ℝ) (a b c : ι) (t : ℝ) :
    linearField J (x + t • Pi.single a 1) b c = linearField J x b c + t • J.val a b c := by
  simp [linearField, Pi.add_apply, Pi.smul_apply, Pi.single_apply, add_smul,
    mul_ite, ite_smul, Finset.sum_add_distrib]

end Realization

section CoordinateDerivative

variable {A : Type*} [NormedAddCommGroup A] [NormedSpace ℝ A]
variable [Fintype ι] [DecidableEq ι]

def coordinateDerivative (F : (ι → ℝ) → ι → ι → A) (x : ι → ℝ) (a b c : ι) : A :=
  deriv (fun t : ℝ => F (x + t • Pi.single a 1) b c) 0

def ClosedField (F : (ι → ℝ) → ι → ι → A) : Prop :=
  ∀ x a b c, cyclicSum (coordinateDerivative F x) a b c = 0

theorem hasPartial_linearField (J : Jet ι A) (x : ι → ℝ) (a b c : ι) :
    HasDerivAt (fun t : ℝ => linearField J (x + t • Pi.single a 1) b c) (J.val a b c) 0 := by
  simp_rw [linearField_line]
  apply (hasDerivAt_const_add_iff (linearField J x b c)).2
  simpa only [one_smul] using
    HasDerivAt.smul_const (hasDerivAt_id' (x := (0 : ℝ))) (J.val a b c)

theorem partial_linearField (J : Jet ι A) (x : ι → ℝ) (a b c : ι) :
    coordinateDerivative (linearField J) x a b c = J.val a b c :=
  (hasPartial_linearField J x a b c).deriv

/-- The realized form is closed at every coordinate point precisely
when the prescribed jet has vanishing cyclic sum. -/
theorem linearField_closed_iff (J : Jet ι A) : ClosedField (linearField J) ↔ ClosedJet J := by
  constructor
  · intro h a b c
    simpa only [cyclicSum, partial_linearField] using h 0 a b c
  · intro h x a b c
    simpa only [cyclicSum, partial_linearField] using h a b c

theorem closed_linear_realization (J : Jet ι A) (hJ : ClosedJet J) :
    ∃ F : (ι → ℝ) → ι → ι → A,
      (∀ x b c, F x c b = -F x b c) ∧ ClosedField F ∧
        ∀ x a b c, coordinateDerivative F x a b c = J.val a b c :=
  ⟨linearField J, linearField_skew J, (linearField_closed_iff J).mpr hJ, partial_linearField J⟩

/-- Taking coordinate derivatives preserves the skew symmetry of a two-form. -/
def firstJet (F : (ι → ℝ) → ι → ι → A)
    (hF : ∀ x b c, F x c b = -F x b c) (x : ι → ℝ) : Jet ι A :=
  ⟨coordinateDerivative F x, by
    intro a b c
    unfold coordinateDerivative
    have h : (fun t : ℝ => F (x + t • Pi.single a 1) c b) =
        fun t : ℝ => -F (x + t • Pi.single a 1) b c :=
      funext fun t => hF (x + t • Pi.single a 1) b c
    rw [h]
    exact deriv.neg (f := fun t : ℝ => F (x + t • Pi.single a 1) b c)⟩

/-- Testing on coordinatewise differentiable closed fields is equivalent
to testing on the closed jets. Linear fields suffice for the reverse direction. -/
theorem compatible_iff_closed_fields (M : Jet ι A →ₗ[ℝ] W) :
    Compatible M ↔
      ∀ (F : (ι → ℝ) → ι → ι → A) (hF : ∀ x b c, F x c b = -F x b c),
        (∀ x a b c,
          DifferentiableAt ℝ (fun t : ℝ => F (x + t • Pi.single a 1) b c) 0) →
          ClosedField F → ∀ x, M (firstJet F hF x) = 0 := by
  constructor
  · intro hM F hF _ hclosed x
    exact hM _ (hclosed x)
  · intro h J hJ
    have hz := h (linearField J) (linearField_skew J)
      (fun x a b c => (hasPartial_linearField J x a b c).differentiableAt)
      ((linearField_closed_iff J).mpr hJ) 0
    have heq : firstJet (linearField J) (linearField_skew J) 0 = J := by
      apply Subtype.ext
      funext a b c
      exact partial_linearField J 0 a b c
    rwa [heq] at hz

end CoordinateDerivative

end

end GeometricUnity.BianchiSymbol
~~~

[Return to file index](#file-index)

## NoetherIdentity.lean {#source-noetheridentity-lean}

Proves finite gauge invariance, the dressing differential, and the paired and off-shell Noether identities under explicit hypotheses.

~~~lean
import Theorem52
import Mathlib.Algebra.TrivSqZeroExt.Basic
import Mathlib.Algebra.Group.Action.Opposite
import Mathlib.Analysis.Calculus.Deriv.Linear

/-!
# Geometric Unity: the coupled Noether identity

The coordinate model uses commuting coefficient derivations, a real
associative algebra, and an integrated cyclic trace. The finite gauge
transformations act on units and on local connection coefficients.
The dressing differential is the tangent coefficient in the algebra
of dual numbers. The connection differential agrees with the real
directional derivative of Theorem 5.2. The final identity uses the
integrated boundary identity and separation by admissible gauge tests.
-/

namespace GeometricUnity.NoetherIdentity

open GeometricUnity.Theorem52
open scoped BigOperators

noncomputable section

variable {ι A C : Type*} [Ring A] [Algebra ℝ A] [Ring C] [Algebra ℝ C]

private def mapOne (f : A →ₐ[ℝ] C) (X : OneForm ι A) : OneForm ι C := fun a => f (X a)
private def mapTwo (f : A →ₐ[ℝ] C) (F : TwoForm ι A) : TwoForm ι C := fun a b => f (F a b)
private def mapInsertion (f : A →ₐ[ℝ] C) (P : Insertion ι A) : Insertion ι C :=
  fun a b c => f (P a b c)

private theorem map_dB (f : A →ₐ[ℝ] C) (d : ι → A →ₗ[ℝ] A) (δ : ι → C →ₗ[ℝ] C)
    (hf : ∀ a x, δ a (f x) = f (d a x)) (X : OneForm ι A) :
    dB δ (mapOne f X) = mapTwo f (dB d X) := by
  funext a b
  simp [dB, mapOne, mapTwo, hf]

private theorem map_wedgeSquare (f : A →ₐ[ℝ] C) (X : OneForm ι A) :
    wedgeSquare (mapOne f X) = mapTwo f (wedgeSquare X) := by
  funext a b
  simp [wedgeSquare, mapOne, mapTwo, comm_apply]

private theorem map_comm (f : A →ₐ[ℝ] C) (x y : A) :
    comm (f x) (f y) = f (comm x y) := by simp [comm_apply]

private theorem map_anti (f : A →ₐ[ℝ] C) (x y : A) :
    anti (f x) (f y) = f (anti x y) := by simp [anti_apply]

private theorem map_covariant (f : A →ₐ[ℝ] C) (d : ι → A →ₗ[ℝ] A)
    (δ : ι → C →ₗ[ℝ] C) (hf : ∀ a x, δ a (f x) = f (d a x)) (B : OneForm ι A)
    (a : ι) (x : A) :
    covariant δ (mapOne f B) a (f x) = f (covariant d B a x) := by
  simp [covariant, mapOne, hf, map_comm]

private theorem map_curvature (f : A →ₐ[ℝ] C) (d : ι → A →ₗ[ℝ] A)
    (δ : ι → C →ₗ[ℝ] C) (hf : ∀ a x, δ a (f x) = f (d a x)) (B : OneForm ι A) :
    curvature δ (mapOne f B) = mapTwo f (curvature d B) := by
  rw [curvature, map_dB f d δ hf, map_wedgeSquare]
  funext a b
  simp [curvature, mapTwo]

private theorem covariant_leibniz (d : ι → A →ₗ[ℝ] A) (hd : Leibniz d) (B : OneForm ι A) :
    Leibniz (covariant d B) := by
  intro a x y
  simp only [covariant, LinearMap.add_apply, comm_apply, hd a]
  noncomm_ring

private theorem derivation_one (d : ι → A →ₗ[ℝ] A) (hd : Leibniz d) (a : ι) :
    d a 1 = 0 := by
  have h := hd a 1 1
  simp only [one_mul, mul_one] at h
  exact left_eq_add.mp h

section Gauge

/-- Conjugation in the direction used in the note, `x ↦ h⁻¹ x h`. -/
def conjugate (h : Aˣ) : A →ₐ[ℝ] A where
  toFun x := ↑h⁻¹ * x * (h : A)
  map_zero' := by simp
  map_one' := by simp
  map_add' x y := by simp [mul_add, add_mul]
  map_mul' x y := by simp [mul_assoc, Units.mul_inv_cancel_left]
  commutes' r := by
    simp [Algebra.algebraMap_eq_smul_one]

theorem conjugate_apply (h : Aˣ) (x : A) :
    conjugate h x = ↑h⁻¹ * x * (h : A) := rfl

private theorem conjugate_comp (h k : Aˣ) (x : A) :
    conjugate k (conjugate h x) = conjugate (h * k) x := by
  simp [conjugate_apply, mul_inv_rev, mul_assoc]

private theorem conjugate_trace (trace : A →ₗ[ℝ] ℝ) (htrace : Cyclic trace) (h : Aˣ) :
    trace.comp (conjugate h).toLinearMap = trace := by
  apply LinearMap.ext
  intro x
  change trace (↑h⁻¹ * x * (h : A)) = trace x
  rw [htrace _ (h : A), ← mul_assoc, h.mul_inv, one_mul]

def gaugeTerm (d : ι → A →ₗ[ℝ] A) (h : Aˣ) : OneForm ι A :=
  fun a => ↑h⁻¹ * d a (h : A)

/-- Component transform of a connection, including its inhomogeneous term. -/
def gaugeConnection (d : ι → A →ₗ[ℝ] A) (h : Aˣ) (B : OneForm ι A) : OneForm ι A :=
  mapOne (conjugate h) B + gaugeTerm d h

theorem gaugeConnection_comp (d : ι → A →ₗ[ℝ] A) (hd : Leibniz d)
    (h k : Aˣ) (B : OneForm ι A) :
    gaugeConnection d k (gaugeConnection d h B) = gaugeConnection d (h * k) B := by
  have log_comp (a : ι) :
      gaugeTerm d (h * k) a = conjugate k (gaugeTerm d h a) + gaugeTerm d k a := by
    simp [gaugeTerm, conjugate_apply, mul_inv_rev, hd a, mul_add,
      mul_assoc, Units.inv_mul_cancel_left]
  funext a
  simp [gaugeConnection, mapOne, conjugate_comp, log_comp, add_assoc]

theorem gaugeConnection_one (d : ι → A →ₗ[ℝ] A) (hd : Leibniz d) (B : OneForm ι A) :
    gaugeConnection d 1 B = B := by
  funext a
  simp [gaugeConnection, gaugeTerm, mapOne, conjugate_apply, derivation_one d hd]

private theorem derivative_inv (d : ι → A →ₗ[ℝ] A) (hd : Leibniz d) (h : Aˣ) (a : ι) :
    d a (↑h⁻¹ : A) = -(↑h⁻¹ * d a (h : A) * ↑h⁻¹) := by
  have hz : d a (↑h⁻¹ : A) * ↑h + ↑h⁻¹ * d a (h : A) = 0 := by
    rw [← hd a, h.inv_mul, derivation_one d hd]
  have he := congrArg (fun x : A => x * (↑h⁻¹ : A)) hz
  rw [add_mul, h.mul_inv_cancel_right, zero_mul] at he
  exact eq_neg_of_add_eq_zero_left he

private theorem derivative_conjugate (d : ι → A →ₗ[ℝ] A) (hd : Leibniz d)
    (h : Aˣ) (a : ι) (x : A) :
    d a (conjugate h x) = conjugate h (d a x) +
      conjugate h x * gaugeTerm d h a - gaugeTerm d h a * conjugate h x := by
  simp only [conjugate_apply, gaugeTerm, hd a, derivative_inv d hd h a, add_mul, neg_mul]
  rw [show (↑h⁻¹ * x * (h : A)) * (↑h⁻¹ * d a (h : A)) =
    ↑h⁻¹ * x * d a (h : A) by simp [mul_assoc, Units.mul_inv_cancel_left]]
  noncomm_ring

/-- The conjugating derivative terms cancel the inhomogeneous connection term. -/
theorem covariant_gauge (d : ι → A →ₗ[ℝ] A) (hd : Leibniz d)
    (h : Aˣ) (B : OneForm ι A) (a : ι) (x : A) :
    covariant d (gaugeConnection d h B) a (conjugate h x) =
      conjugate h (covariant d B a x) := by
  simp only [covariant, LinearMap.add_apply, gaugeConnection, Pi.add_apply, mapOne,
    derivative_conjugate d hd h, map_add]
  rw [← map_comm (conjugate h) (B a) x]
  simp only [comm_apply]
  abel

def Commuting (d : ι → A →ₗ[ℝ] A) : Prop :=
  ∀ a b x, d a (d b x) = d b (d a x)

private theorem gaugeTerm_flat (d : ι → A →ₗ[ℝ] A) (hd : Leibniz d)
    (hc : Commuting d) (h : Aˣ) : curvature d (gaugeTerm d h) = 0 := by
  funext a b
  simp only [curvature, Pi.add_apply, Pi.zero_apply, dB, wedgeSquare, gaugeTerm, hd a, hd b,
    derivative_inv d hd h, comm_apply, neg_mul, hc a b (h : A)]
  noncomm_ring

theorem curvature_gauge (d : ι → A →ₗ[ℝ] A) (hd : Leibniz d)
    (hc : Commuting d) (h : Aˣ) (B : OneForm ι A) :
    curvature d (gaugeConnection d h B) = mapTwo (conjugate h) (curvature d B) := by
  have hcov (a : ι) (x : A) :
      covariant d (gaugeTerm d h) a (conjugate h x) = conjugate h (d a x) := by
    simpa [gaugeConnection, mapOne, covariant] using covariant_gauge d hd h 0 a x
  rw [gaugeConnection, add_comm, curvature_shift, gaugeTerm_flat d hd hc h, zero_add,
    map_dB (conjugate h) d (covariant d (gaugeTerm d h)) hcov, map_wedgeSquare]
  funext a b
  simp [curvature, mapTwo]

end Gauge

variable [Fintype ι]

section Action

private theorem map_theta (f : A →ₐ[ℝ] C)
    (B : Bracket A) (B' : Bracket C) (hf : ∀ x y, B' (f x) (f y) = f (B x y))
    (P : Insertion ι A) (F : TwoForm ι A) :
    theta B' (mapInsertion f P) (mapTwo f F) = mapOne f (theta B P F) := by
  funext a
  simp [theta, mapInsertion, mapTwo, mapOne, hf, map_sum]

private theorem pair_map (f : A →ₐ[ℝ] C) (trace : C →ₗ[ℝ] ℝ) (X Y : OneForm ι A) :
    pair trace (mapOne f X) (mapOne f Y) = pair (trace.comp f.toLinearMap) X Y := by
  simp [pair, mapOne]

private theorem action_map (f : A →ₐ[ℝ] C) (trace : C →ₗ[ℝ] ℝ)
    (d : ι → A →ₗ[ℝ] A) (δ : ι → C →ₗ[ℝ] C) (hf : ∀ a x, δ a (f x) = f (d a x))
    (g : ι → ℝ) (P Q : Insertion ι A) (F : TwoForm ι A) (lam m : ℝ) (X : OneForm ι A) :
    action trace δ g (mapInsertion f P) (mapInsertion f Q) (mapTwo f F) lam m (mapOne f X) =
      action (trace.comp f.toLinearMap) d g P Q F lam m X := by
  simp only [action, map_dB f d δ hf, map_wedgeSquare]
  have hin :
      mapTwo f F + (1 / 2 : ℝ) • mapTwo f (dB d X) + lam • mapTwo f (wedgeSquare X) =
        mapTwo f (F + (1 / 2 : ℝ) • dB d X + lam • wedgeSquare X) := by
    funext a b
    simp [mapTwo]
  rw [hin, map_theta f anti anti (map_anti f), map_theta f comm comm (map_comm f)]
  have hadd (U V : OneForm ι A) : mapOne f U + mapOne f V = mapOne f (U + V) := by
    funext a
    simp [mapOne]
  have hg : raise g (mapOne f X) = mapOne f (raise g X) := by
    funext a
    simp [raise, mapOne]
  rw [hadd, hg, pair_map, pair_map]

/-- The reference connection and Clifford insertions are dressed by the
same invertible coefficient. The connection `U` varies independently. -/
def dressedAction (trace : A →ₗ[ℝ] ℝ) (d : ι → A →ₗ[ℝ] A) (g : ι → ℝ)
    (P₀ Q₀ : Insertion ι A) (B₀ : OneForm ι A) (lam m : ℝ) (U : OneForm ι A) (ε : Aˣ) : ℝ :=
  let B := gaugeConnection d ε B₀
  action trace (covariant d B) g (mapInsertion (conjugate ε) P₀) (mapInsertion (conjugate ε) Q₀)
    (curvature d B) lam m (U - B)

/-- Finite simultaneous gauge invariance of the action of Theorem 5.2. -/
theorem dressedAction_gauge (trace : A →ₗ[ℝ] ℝ) (htrace : Cyclic trace)
    (d : ι → A →ₗ[ℝ] A) (hd : Leibniz d) (hc : Commuting d) (g : ι → ℝ)
    (P₀ Q₀ : Insertion ι A) (B₀ U : OneForm ι A) (lam m : ℝ) (ε h : Aˣ) :
    dressedAction trace d g P₀ Q₀ B₀ lam m (gaugeConnection d h U) (ε * h) =
      dressedAction trace d g P₀ Q₀ B₀ lam m U ε := by
  let B := gaugeConnection d ε B₀
  have hB : gaugeConnection d (ε * h) B₀ = gaugeConnection d h B :=
    (gaugeConnection_comp d hd ε h B₀).symm
  have ht : gaugeConnection d h U - gaugeConnection d h B = mapOne (conjugate h) (U - B) := by
    funext a
    simp only [gaugeConnection, Pi.sub_apply, Pi.add_apply, mapOne, map_sub]
    abel
  have hins (R : Insertion ι A) :
      mapInsertion (conjugate (ε * h)) R = mapInsertion (conjugate h) (mapInsertion (conjugate ε) R) := by
    funext a b c
    exact (conjugate_comp ε h (R a b c)).symm
  simp only [dressedAction, hB, ht, hins, curvature_gauge d hd hc h]
  rw [action_map (conjugate h) trace (covariant d B) (covariant d (gaugeConnection d h B))
    (covariant_gauge d hd h B), conjugate_trace trace htrace h]

private theorem dressedAction_compensate (trace : A →ₗ[ℝ] ℝ) (htrace : Cyclic trace)
    (d : ι → A →ₗ[ℝ] A) (hd : Leibniz d) (hc : Commuting d) (g : ι → ℝ)
    (P₀ Q₀ : Insertion ι A) (B₀ U : OneForm ι A) (lam m : ℝ) (ε h : Aˣ) :
    dressedAction trace d g P₀ Q₀ B₀ lam m U (ε * h) =
      dressedAction trace d g P₀ Q₀ B₀ lam m (gaugeConnection d h⁻¹ U) ε := by
  have hh := dressedAction_gauge trace htrace d hd hc g P₀ Q₀ B₀
    (gaugeConnection d h⁻¹ U) lam m ε h
  rwa [gaugeConnection_comp d hd h⁻¹ h U, inv_mul_cancel, gaugeConnection_one d hd] at hh

end Action

section Dual

open TrivSqZeroExt

private abbrev Dual (A : Type*) := TrivSqZeroExt A A

private abbrev constant : A →ₐ[ℝ] Dual A := TrivSqZeroExt.inlAlgHom ℝ A A

private def tangentOne (X : OneForm ι A) : OneForm ι (Dual A) := fun a => inr (X a)

omit [Algebra ℝ A] in
private theorem dual_product (x y : Dual A) : (x * y).snd = x.fst * y.snd + x.snd * y.fst := rfl

private def liftLinear (D : A →ₗ[ℝ] A) : Dual A →ₗ[ℝ] Dual A where
  toFun x := ⟨D x.fst, D x.snd⟩
  map_add' x y := by
    apply TrivSqZeroExt.ext
    · exact D.map_add x.fst y.fst
    · exact D.map_add x.snd y.snd
  map_smul' r x := by
    apply TrivSqZeroExt.ext
    · exact map_smul D r x.fst
    · exact map_smul D r x.snd

@[simp] private theorem lift_fst (D : A →ₗ[ℝ] A) (x : Dual A) :
    (liftLinear D x).fst = D x.fst := rfl

@[simp] private theorem lift_snd (D : A →ₗ[ℝ] A) (x : Dual A) :
    (liftLinear D x).snd = D x.snd := rfl

private theorem lift_constant (D : A →ₗ[ℝ] A) (x : A) :
    liftLinear D (constant x) = constant (D x) := by
  apply TrivSqZeroExt.ext <;> simp

omit [Fintype ι] in
private theorem liftLeibniz (D : ι → A →ₗ[ℝ] A) (hD : Leibniz D) :
    Leibniz (fun a => liftLinear (D a)) := by
  intro a x y
  apply TrivSqZeroExt.ext
  · simp only [lift_fst, fst_mul, fst_add, hD a]
  · simp only [dual_product, lift_fst, lift_snd, snd_add, map_add, hD a]
    abel

omit [Fintype ι] in
private theorem liftCommuting (D : ι → A →ₗ[ℝ] A) (hD : Commuting D) :
    Commuting (fun a => liftLinear (D a)) := by
  intro a b x
  apply TrivSqZeroExt.ext
  · exact hD a b x.fst
  · exact hD a b x.snd

private def tangentTrace (trace : A →ₗ[ℝ] ℝ) : Dual A →ₗ[ℝ] ℝ where
  toFun x := trace x.snd
  map_add' _ _ := by simp
  map_smul' _ _ := by simp

@[simp] private theorem tangentTrace_apply (trace : A →ₗ[ℝ] ℝ) (x : Dual A) :
    tangentTrace trace x = trace x.snd := rfl

private theorem tangentTrace_cyclic (trace : A →ₗ[ℝ] ℝ) (h : Cyclic trace) :
    Cyclic (tangentTrace trace) := by
  intro x y
  change trace (x * y).snd = trace (y * x).snd
  simp only [dual_product, map_add]
  rw [h x.fst y.snd, h x.snd y.fst, add_comm]

private def scaleTangent (r : ℝ) : Dual A →ₐ[ℝ] Dual A where
  toFun x := ⟨x.fst, r • x.snd⟩
  map_zero' := by ext <;> simp
  map_one' := by ext <;> simp
  map_add' x y := by
    apply TrivSqZeroExt.ext
    · rfl
    · exact smul_add r x.snd y.snd
  map_mul' x y := by
    apply TrivSqZeroExt.ext
    · rfl
    · change r • (x.fst * y.snd + x.snd * y.fst) = x.fst * (r • y.snd) + (r • x.snd) * y.fst
      simp [smul_add]
  commutes' _ := by
    ext <;> simp [algebraMap_eq_inl']

@[simp] private theorem scale_fst (r : ℝ) (x : Dual A) :
    (scaleTangent r x).fst = x.fst := rfl

@[simp] private theorem scale_snd (r : ℝ) (x : Dual A) :
    (scaleTangent r x).snd = r • x.snd := rfl

private theorem lift_scale (r : ℝ) (D : A →ₗ[ℝ] A) (x : Dual A) :
    liftLinear D (scaleTangent r x) = scaleTangent r (liftLinear D x) := by
  apply TrivSqZeroExt.ext
  · rfl
  · exact map_smul D r x.snd

private theorem scale_trace (r : ℝ) (trace : A →ₗ[ℝ] ℝ) :
    (tangentTrace trace).comp (scaleTangent r).toLinearMap = r • tangentTrace trace := by
  apply LinearMap.ext
  intro x
  exact map_smul trace r x.snd

private theorem action_trace_smul (r : ℝ) (trace : A →ₗ[ℝ] ℝ)
    (D : ι → A →ₗ[ℝ] A) (g : ι → ℝ) (P Q : Insertion ι A) (F : TwoForm ι A)
    (lam m : ℝ) (X : OneForm ι A) :
    action (r • trace) D g P Q F lam m X = r * action trace D g P Q F lam m X := by
  simp only [action, pair, LinearMap.smul_apply, smul_eq_mul, ← Finset.mul_sum]
  ring

private theorem euler_primal (D : ι → A →ₗ[ℝ] A) (g : ι → ℝ) (P Q : Insertion ι A)
    (F : TwoForm ι A) (lam m : ℝ) (X : OneForm ι A) (a : ι) :
    (euler (fun b => liftLinear (D b)) g (mapInsertion constant P) (mapInsertion constant Q)
      (mapTwo constant F) lam m (mapOne constant X) a).fst =
      euler D g P Q F lam m X a := by
  simp [euler, theta, correction, raise, dB, wedgeSquare, comm_apply, anti_apply,
    mapOne, mapTwo, mapInsertion, fst_sum]

private theorem action_tangent (trace : A →ₗ[ℝ] ℝ) (htrace : Cyclic trace)
    (D : ι → A →ₗ[ℝ] A) (D_leibniz : Leibniz D) (g : ι → ℝ) (P Q : Insertion ι A)
    (F : TwoForm ι A) (hp : Alternating P) (hq : Alternating Q)
    (hP : Parallel D P) (hQ : Parallel D Q) (lam m : ℝ) (X α : OneForm ι A)
    (hbP : BoundaryZero trace D anti P X α) (hbQ : BoundaryZero trace D comm Q X α) :
    action (tangentTrace trace) (fun a => liftLinear (D a)) g
        (mapInsertion constant P) (mapInsertion constant Q) (mapTwo constant F) lam m
        (mapOne constant X + tangentOne α) =
      pair trace α (euler D g P Q F lam m X) := by
  let D' a := liftLinear (D a)
  let P' := mapInsertion constant P
  let Q' := mapInsertion constant Q
  let F' := mapTwo constant F
  let X' := mapOne constant X
  let α' := tangentOne α
  let tr' := tangentTrace trace
  let I := action tr' D' g P' Q' F' lam m
  have hAlt (R : Insertion ι A) (hR : Alternating R) : Alternating (mapInsertion constant R) := by
    constructor
    · intro a b c; simp [mapInsertion, hR.swapBC a b c]
    · intro a b c; simp [mapInsertion, hR.swapAC a b c]
  have hPar (R : Insertion ι A) (hR : Parallel D R) : Parallel D' (mapInsertion constant R) := by
    intro a b c
    change liftLinear (D b) (constant (R a b c)) = 0
    rw [lift_constant, hR a b c, map_zero]
  have hbP' : BoundaryZero tr' D' anti P' X' α' := by
    simpa [BoundaryZero, sum3, tr', D', P', X', α', tangentTrace, mapInsertion,
      mapOne, tangentOne, anti_apply] using hbP
  have hbQ' : BoundaryZero tr' D' comm Q' X' α' := by
    simpa [BoundaryZero, sum3, tr', D', Q', X', α', tangentTrace, mapInsertion,
      mapOne, tangentOne, comm_apply] using hbQ
  have hd := theorem_5_2 tr' D' g P' Q' F' (hAlt P hp) (hAlt Q hq)
    (tangentTrace_cyclic trace htrace) (liftLeibniz D D_leibniz)
    (hPar P hP) (hPar Q hQ) lam m X' α' hbP' hbQ'
  have hline (t : ℝ) : I (X' + t • α') = t * I (X' + α') := by
    have h := action_map (scaleTangent t) tr' D' D' (fun a => lift_scale t (D a))
      g P' Q' F' lam m (X' + α')
    have hP' : mapInsertion (scaleTangent t) P' = P' := by
      funext a b c; apply TrivSqZeroExt.ext <;> simp [P', mapInsertion]
    have hQ' : mapInsertion (scaleTangent t) Q' = Q' := by
      funext a b c; apply TrivSqZeroExt.ext <;> simp [Q', mapInsertion]
    have hF' : mapTwo (scaleTangent t) F' = F' := by
      funext a b; apply TrivSqZeroExt.ext <;> simp [F', mapTwo]
    have hX' : mapOne (scaleTangent t) (X' + α') = X' + t • α' := by
      funext a; apply TrivSqZeroExt.ext <;> simp [X', α', mapOne, tangentOne]
    rw [hP', hQ', hF', hX', scale_trace, action_trace_smul] at h
    exact h
  have hpoly : (fun t : ℝ => I (X' + t • α')) = fun t => t * I (X' + α') := funext hline
  change HasDerivAt (fun t : ℝ => I (X' + t • α'))
    (pair tr' α' (euler D' g P' Q' F' lam m X')) 0 at hd
  rw [hpoly] at hd
  have hlinear : HasDerivAt (fun t : ℝ => t * I (X' + α')) (I (X' + α')) 0 := by
    simpa only [one_mul] using (hasDerivAt_id' (x := (0 : ℝ))).mul_const (I (X' + α'))
  change I (X' + α') = _
  rw [← hlinear.deriv, hd.deriv]
  simp only [pair, tr', α', tangentTrace_apply, tangentOne, dual_product,
    fst_inr, snd_inr, zero_mul, zero_add, D', P', Q', F', X', euler_primal D g P Q F lam m X]

end Dual

section DressingDifferential

open TrivSqZeroExt

omit [Fintype ι] in
private theorem map_gaugeConnection (f : A →ₐ[ℝ] C) (d : ι → A →ₗ[ℝ] A)
    (δ : ι → C →ₗ[ℝ] C) (hf : ∀ a x, δ a (f x) = f (d a x)) (ε : Aˣ) (B : OneForm ι A) :
    gaugeConnection δ (Units.map f.toMonoidHom ε) (mapOne f B) =
      mapOne f (gaugeConnection d ε B) := by
  funext a
  simp [gaugeConnection, gaugeTerm, conjugate_apply, mapOne, hf]

private def infinitesimalGauge (ζ : A) : (Dual A)ˣ where
  val := ⟨1, ζ⟩
  inv := ⟨1, -ζ⟩
  val_inv := by
    apply TrivSqZeroExt.ext
    · change (1 : A) * 1 = 1; simp
    · change (1 : A) * (-ζ) + ζ * 1 = 0; simp
  inv_val := by
    apply TrivSqZeroExt.ext
    · change (1 : A) * 1 = 1; simp
    · change (1 : A) * ζ + (-ζ) * 1 = 0; simp

omit [Algebra ℝ A] in
private theorem infinitesimalGauge_inv (ζ : A) :
    (infinitesimalGauge ζ)⁻¹ = infinitesimalGauge (-ζ) := by
  apply Units.ext
  rfl

omit [Algebra ℝ A] in
@[simp] private theorem infinitesimal_fst (ζ : A) :
    (↑(infinitesimalGauge ζ) : Dual A).fst = 1 := rfl

omit [Algebra ℝ A] in
@[simp] private theorem infinitesimal_snd (ζ : A) :
    (↑(infinitesimalGauge ζ) : Dual A).snd = ζ := rfl

omit [Fintype ι] in
/-- The coefficient of the infinitesimal connection transform is `D_U ζ`. -/
private theorem gaugeConnection_infinitesimal (d : ι → A →ₗ[ℝ] A) (hd : Leibniz d)
    (U : OneForm ι A) (ζ : A) :
    gaugeConnection (fun a => liftLinear (d a)) (infinitesimalGauge ζ) (mapOne constant U) =
      mapOne constant U + tangentOne (fun a => covariant d U a ζ) := by
  funext a
  apply TrivSqZeroExt.ext
  · simp [gaugeConnection, mapOne, gaugeTerm, conjugate_apply, infinitesimalGauge_inv,
      tangentOne, derivation_one d hd]
  · simp only [gaugeConnection, mapOne, gaugeTerm, conjugate_apply, infinitesimalGauge_inv,
      tangentOne, Pi.add_apply, snd_add, dual_product, fst_mul, infinitesimal_fst, infinitesimal_snd,
      inlAlgHom_apply, fst_inl, snd_inl, snd_inr, lift_fst, lift_snd, derivation_one d hd,
      covariant, LinearMap.add_apply, comm_apply, mul_one, one_mul, mul_zero,
      add_zero, zero_add, neg_mul]
    abel

omit [Fintype ι] in
private theorem lift_covariant (d : ι → A →ₗ[ℝ] A) (B : OneForm ι A) :
    covariant (fun a => liftLinear (d a)) (mapOne constant B) =
      fun a => liftLinear (covariant d B a) := by
  funext a
  apply LinearMap.ext
  intro x
  apply TrivSqZeroExt.ext <;> simp [covariant, mapOne, comm_apply]

/-- Right multiplication of the dressing by the infinitesimal gauge unit. -/
def dressingJet (ε : Aˣ) (ζ : A) : (TrivSqZeroExt A A)ˣ :=
  Units.map constant.toMonoidHom ε * infinitesimalGauge ζ

theorem dressingJet_snd (ε : Aˣ) (ζ : A) :
    (↑(dressingJet ε ζ) : TrivSqZeroExt A A).snd = (ε : A) * ζ := by
  change (ε : A) * ζ + 0 * 1 = (ε : A) * ζ
  rw [zero_mul, add_zero]

variable (trace : A →ₗ[ℝ] ℝ) (d : ι → A →ₗ[ℝ] A) (g : ι → ℝ)
variable (P₀ Q₀ : Insertion ι A) (B₀ : OneForm ι A) (lam m : ℝ)
variable (U : OneForm ι A) (ε : Aˣ)

/-- The raised connection Euler expression of Theorem 5.2 for the dressed action. -/
def dressedEuler : OneForm ι A :=
  let B := gaugeConnection d ε B₀
  euler (covariant d B) g (mapInsertion (conjugate ε) P₀) (mapInsertion (conjugate ε) Q₀)
    (curvature d B) lam m (U - B)

/-- First-order variation of the dressing at fixed connection. The lifted
dressing has constant coefficient `ε` and tangent coefficient `ε * ζ`. -/
def dressingDerivative (ζ : A) : ℝ :=
  dressedAction (tangentTrace trace) (fun a => liftLinear (d a)) g
    (mapInsertion constant P₀) (mapInsertion constant Q₀) (mapOne constant B₀) lam m
    (mapOne constant U) (dressingJet ε ζ)

/-- The two integrated boundary conditions needed to apply Theorem 5.2 in
the infinitesimal gauge direction. -/
def ConnectionBoundary (ζ : A) : Prop :=
  let B := gaugeConnection d ε B₀
  let α := fun a => covariant d U a ζ
  BoundaryZero trace (covariant d B) anti (mapInsertion (conjugate ε) P₀) (U - B) α ∧
    BoundaryZero trace (covariant d B) comm (mapInsertion (conjugate ε) Q₀) (U - B) α

private theorem lifted_dressedAction (α : OneForm ι A) :
    let B := gaugeConnection d ε B₀
    let P := mapInsertion (conjugate ε) P₀
    let Q := mapInsertion (conjugate ε) Q₀
    dressedAction (tangentTrace trace) (fun a => liftLinear (d a)) g
      (mapInsertion constant P₀) (mapInsertion constant Q₀) (mapOne constant B₀) lam m
      (mapOne constant U + tangentOne α) (Units.map constant.toMonoidHom ε) =
    action (tangentTrace trace) (fun a => liftLinear (covariant d B a)) g
      (mapInsertion constant P) (mapInsertion constant Q)
      (mapTwo constant (curvature d B)) lam m (mapOne constant (U - B) + tangentOne α) := by
  let B := gaugeConnection d ε B₀
  let f : A →ₐ[ℝ] Dual A := constant
  let d' : ι → Dual A →ₗ[ℝ] Dual A := fun a => liftLinear (d a)
  let ε' : (Dual A)ˣ := Units.map f.toMonoidHom ε
  have hD (a : ι) (x : A) : d' a (f x) = f (d a x) := lift_constant (d a) x
  have hB : gaugeConnection d' ε' (mapOne f B₀) = mapOne f B :=
    map_gaugeConnection f d d' hD ε B₀
  have hins (R : Insertion ι A) :
      mapInsertion (conjugate ε') (mapInsertion constant R) =
        mapInsertion constant (mapInsertion (conjugate ε) R) := by
    funext a b c
    simp [ε', f, mapInsertion, conjugate_apply]
  have hT : mapOne constant U + tangentOne α - mapOne constant B =
      mapOne constant (U - B) + tangentOne α := by
    funext a
    simp only [Pi.sub_apply, Pi.add_apply, mapOne, map_sub]
    abel
  change dressedAction (tangentTrace trace) d' g (mapInsertion constant P₀)
    (mapInsertion constant Q₀) (mapOne constant B₀) lam m (mapOne constant U + tangentOne α) ε' = _
  rw [dressedAction, hB, hins P₀, hins Q₀, hT, lift_covariant d B,
    map_curvature f d d' hD B]

/-- Finite invariance in the dual algebra moves the dressing variation
to a connection variation in the opposite gauge direction. -/
theorem dressingDerivative_eq_neg_pair (htrace : Cyclic trace) (hd : Leibniz d) (hc : Commuting d)
    (hp : Alternating P₀) (hq : Alternating Q₀)
    (hP : Parallel (covariant d B₀) P₀) (hQ : Parallel (covariant d B₀) Q₀)
    (ζ : A) (hb : ConnectionBoundary trace d P₀ Q₀ B₀ U ε ζ) :
    dressingDerivative trace d g P₀ Q₀ B₀ lam m U ε ζ =
      -pair trace (fun a => covariant d U a ζ) (dressedEuler d g P₀ Q₀ B₀ lam m U ε) := by
  let B := gaugeConnection d ε B₀
  let P := mapInsertion (conjugate ε) P₀
  let Q := mapInsertion (conjugate ε) Q₀
  let α := fun a => covariant d U a ζ
  let d' a := liftLinear (d a)
  have hdir : gaugeConnection d' (infinitesimalGauge ζ)⁻¹ (mapOne constant U) =
      mapOne constant U + tangentOne (-α) := by
    rw [infinitesimalGauge_inv, gaugeConnection_infinitesimal d hd U (-ζ)]
    have ha : (fun a => covariant d U a (-ζ)) = -α := by
      funext a
      exact map_neg (covariant d U a) ζ
    rw [ha]
  have hAlt (R : Insertion ι A) (hR : Alternating R) :
      Alternating (mapInsertion (conjugate ε) R) := by
    constructor
    · intro a b c; simp [mapInsertion, hR.swapBC a b c]
    · intro a b c; simp [mapInsertion, hR.swapAC a b c]
  have hPar (R : Insertion ι A) (hR : Parallel (covariant d B₀) R) :
      Parallel (covariant d B) (mapInsertion (conjugate ε) R) := by
    intro a b c
    simp [B, mapInsertion, covariant_gauge d hd, hR a b c]
  have hbP : BoundaryZero trace (covariant d B) anti P (U - B) (-α) := by
    simpa [BoundaryZero, sum3, Finset.sum_neg_distrib] using hb.1
  have hbQ : BoundaryZero trace (covariant d B) comm Q (U - B) (-α) := by
    simpa [BoundaryZero, sum3, Finset.sum_neg_distrib] using hb.2
  calc
    _ = dressedAction (tangentTrace trace) d' g (mapInsertion constant P₀)
        (mapInsertion constant Q₀) (mapOne constant B₀) lam m
        (gaugeConnection d' (infinitesimalGauge ζ)⁻¹ (mapOne constant U))
        (Units.map constant.toMonoidHom ε) :=
      dressedAction_compensate (tangentTrace trace) (tangentTrace_cyclic trace htrace)
        d' (liftLeibniz d hd) (liftCommuting d hc) g (mapInsertion constant P₀)
        (mapInsertion constant Q₀) (mapOne constant B₀) (mapOne constant U) lam m
        (Units.map constant.toMonoidHom ε) (infinitesimalGauge ζ)
    _ = dressedAction (tangentTrace trace) d' g (mapInsertion constant P₀)
        (mapInsertion constant Q₀) (mapOne constant B₀) lam m
        (mapOne constant U + tangentOne (-α)) (Units.map constant.toMonoidHom ε) :=
      congrArg (fun V => dressedAction (tangentTrace trace) d' g (mapInsertion constant P₀)
        (mapInsertion constant Q₀) (mapOne constant B₀) lam m V
        (Units.map constant.toMonoidHom ε)) hdir
    _ = action (tangentTrace trace) (fun a => liftLinear (covariant d B a)) g
        (mapInsertion constant P) (mapInsertion constant Q) (mapTwo constant (curvature d B)) lam m
        (mapOne constant (U - B) + tangentOne (-α)) :=
      lifted_dressedAction trace d g P₀ Q₀ B₀ lam m U ε (-α)
    _ = pair trace (-α) (dressedEuler d g P₀ Q₀ B₀ lam m U ε) :=
      action_tangent trace htrace (covariant d B) (covariant_leibniz d hd B) g P Q
        (curvature d B) (hAlt P₀ hp) (hAlt Q₀ hq) (hPar P₀ hP) (hPar Q₀ hQ)
        lam m (U - B) (-α) hbP hbQ
    _ = _ := by simp [pair, α, Finset.sum_neg_distrib]

end DressingDifferential

section Noether

def divergence (d : ι → A →ₗ[ℝ] A) (U E : OneForm ι A) : A :=
  ∑ a, covariant d U a (E a)

/-- The integrated divergence of the traced product is zero for
the admissible gauge test. -/
def GaugeBoundary (trace : A →ₗ[ℝ] ℝ) (d : ι → A →ₗ[ℝ] A) (U E : OneForm ι A) (ζ : A) : Prop :=
  (∑ a, trace (covariant d U a (ζ * E a))) = 0

/-- Cyclicity removes the connection commutator from the boundary term. -/
theorem gaugeBoundary_iff_ordinary (trace : A →ₗ[ℝ] ℝ) (htrace : Cyclic trace)
    (d : ι → A →ₗ[ℝ] A) (U E : OneForm ι A) (ζ : A) :
    GaugeBoundary trace d U E ζ ↔ (∑ a, trace (d a (ζ * E a))) = 0 := by
  have h : (∑ a, trace (covariant d U a (ζ * E a))) = ∑ a, trace (d a (ζ * E a)) := by
    apply Finset.sum_congr rfl
    intro a _
    simp only [covariant, LinearMap.add_apply, comm_apply, map_add, map_sub,
      htrace (U a) (ζ * E a), sub_self, add_zero]
  unfold GaugeBoundary
  rw [h]

theorem integrated_gauge_product (trace : A →ₗ[ℝ] ℝ) (d : ι → A →ₗ[ℝ] A) (hd : Leibniz d)
    (U E : OneForm ι A) (ζ : A) (hb : GaugeBoundary trace d U E ζ) :
    -pair trace (fun a => covariant d U a ζ) E = trace (ζ * divergence d U E) := by
  have h := covariant_leibniz d hd U
  unfold Leibniz at h
  unfold GaugeBoundary at hb
  simp only [h, map_add, Finset.sum_add_distrib] at hb
  simp only [pair, divergence, Finset.mul_sum, map_sum]
  linarith

variable (trace : A →ₗ[ℝ] ℝ) (d : ι → A →ₗ[ℝ] A) (g : ι → ℝ)
variable (P₀ Q₀ : Insertion ι A) (B₀ : OneForm ι A) (lam m : ℝ)
variable (U : OneForm ι A) (ε : Aˣ)

/-- The dressing differential is represented by the covariant divergence
of the full connection Euler expression. -/
theorem dressingDerivative_eq_divergence (htrace : Cyclic trace) (hd : Leibniz d) (hc : Commuting d)
    (hp : Alternating P₀) (hq : Alternating Q₀)
    (hP : Parallel (covariant d B₀) P₀) (hQ : Parallel (covariant d B₀) Q₀)
    (ζ : A) (hb : ConnectionBoundary trace d P₀ Q₀ B₀ U ε ζ)
    (hg : GaugeBoundary trace d U (dressedEuler d g P₀ Q₀ B₀ lam m U ε) ζ) :
    dressingDerivative trace d g P₀ Q₀ B₀ lam m U ε ζ =
      trace (ζ * divergence d U (dressedEuler d g P₀ Q₀ B₀ lam m U ε)) := by
  rw [dressingDerivative_eq_neg_pair trace d g P₀ Q₀ B₀ lam m U ε htrace hd hc hp hq hP hQ ζ hb]
  exact integrated_gauge_product trace d hd U _ ζ hg

/-- Theorem 6.1 in the coordinate model. Separation of the two Euler
representatives by admissible tests turns the paired identity into
the off-shell identity `Eε = D_U,a E_U^a`. -/
theorem theorem_6_1 (htrace : Cyclic trace) (hd : Leibniz d) (hc : Commuting d)
    (hp : Alternating P₀) (hq : Alternating Q₀)
    (hP : Parallel (covariant d B₀) P₀) (hQ : Parallel (covariant d B₀) Q₀)
    (admissible : A → Prop)
    (hb : ∀ ζ, admissible ζ → ConnectionBoundary trace d P₀ Q₀ B₀ U ε ζ)
    (hg : ∀ ζ, admissible ζ →
      GaugeBoundary trace d U (dressedEuler d g P₀ Q₀ B₀ lam m U ε) ζ)
    (separates : ∀ Z : A, (∀ ζ, admissible ζ → trace (ζ * Z) = 0) → Z = 0)
    (Eε : A) (hE : ∀ ζ, admissible ζ →
      dressingDerivative trace d g P₀ Q₀ B₀ lam m U ε ζ = trace (ζ * Eε)) :
    Eε = divergence d U (dressedEuler d g P₀ Q₀ B₀ lam m U ε) := by
  apply sub_eq_zero.mp
  apply separates
  intro ζ hζ
  rw [mul_sub, map_sub, ← hE ζ hζ,
    dressingDerivative_eq_divergence trace d g P₀ Q₀ B₀ lam m U ε htrace hd hc hp hq hP hQ
      ζ (hb ζ hζ) (hg ζ hζ), sub_self]

end Noether

end

end GeometricUnity.NoetherIdentity
~~~

[Return to file index](#file-index)

## D7RealTheorem.lean {#source-d7realtheorem-lean}

Assembles real Theorem 3.4, including the dimensions 200, 96, 56, and 48 and the closed-field Bianchi criterion.

~~~lean
import D7RealRanks
import D7RealJets
import Mathlib.Analysis.Matrix.Normed

/-! # The real Spin(7,7)-equivariant contraction spaces -/

namespace GeometricUnity.D7RealTheorem

open D7Exterior (Axis)
open D7SpinAction D7RealComparison
open scoped TensorProduct

noncomputable section

set_option backward.isDefEq.respectTransparency false
set_option maxHeartbeats 1200000

private theorem representation_inv_cancel {W : Type*} [AddCommMonoid W] [Module ℝ W]
    (τ : Representation ℝ Spin W) (g : Spin) (y : W) : τ g (τ g⁻¹ y) = y := by
  change (τ g * τ g⁻¹) y = y
  rw [← map_mul, mul_inv_cancel, map_one]
  rfl

private def currySymbols {U W E : Type*} [AddCommGroup U] [Module ℝ U]
    [AddCommGroup W] [Module ℝ W] [AddCommGroup E] [Module ℝ E]
    (ρ : Representation ℝ Spin U) (τ : Representation ℝ Spin W) (σ : Representation ℝ Spin E) :
    (ρ.tprod τ).IntertwiningMap σ ≃ₗ[ℝ] ρ.IntertwiningMap (Representation.linHom τ σ) where
  toFun T := ⟨TensorProduct.curry T.toLinearMap, by
    intro g
    apply LinearMap.ext
    intro x
    apply LinearMap.ext
    intro y
    have h := DFunLike.congr_fun (T.isIntertwining' g) (x ⊗ₜ[ℝ] τ g⁻¹ y)
    simp only [LinearMap.comp_apply, Representation.tprod_apply, TensorProduct.map_tmul,
      representation_inv_cancel] at h
    exact h⟩
  invFun S := ⟨TensorProduct.lift S.toLinearMap, by
    intro g
    apply TensorProduct.ext'
    intro x y
    have h := DFunLike.congr_fun (DFunLike.congr_fun (S.isIntertwining' g) x) (τ g y)
    have hy : τ g⁻¹ (τ g y) = y := by simpa only [inv_inv] using representation_inv_cancel τ g⁻¹ y
    simp only [LinearMap.comp_apply, Representation.linHom_apply, hy] at h
    exact h⟩
  left_inv T := by apply Representation.IntertwiningMap.ext; apply TensorProduct.ext'; intros; rfl
  right_inv S := by apply Representation.IntertwiningMap.ext; apply LinearMap.ext; intro x; ext y; rfl
  map_add' T S := by apply Representation.IntertwiningMap.ext; rfl
  map_smul' a T := by apply Representation.IntertwiningMap.ext; rfl

open D7RealJets (FormJets)

abbrev JetTensors := FormJets ⊗[ℝ] Coefficients

local instance : AddCommGroup FormJets :=
  TensorProduct.addCommGroup (R := ℝ) (M := Covector) (N := D7RealJets.Forms 2)

local instance : AddCommGroup JetTensors :=
  TensorProduct.addCommGroup (R := ℝ) (M := FormJets) (N := Coefficients)

private abbrev formJetAction := vectorRepresentation.dual.tprod (formAction 2)

def jetAction : Representation ℝ Spin JetTensors :=
  formJetAction.tprod coefficientAction

abbrev DivergenceSymbols := jetAction.IntertwiningMap coefficientAction

private def toJetRepresentation :
    ((formCoefficientsAction 2).tprod vectorRepresentation).Equiv jetAction :=
  (Representation.TensorProduct.comm (formCoefficientsAction 2) vectorRepresentation).trans
    ((liftTensorEquiv metricDualEquiv (formCoefficientsAction 2)).trans
      (Representation.TensorProduct.assoc vectorRepresentation.dual (formAction 2) coefficientAction).symm)

/-- Metric contraction of the one-form output gives the divergence symbol. -/
def divergenceSymbol : Operators ≃ₗ[ℝ] DivergenceSymbols := by
  let a := transportHom (Representation.Equiv.refl (formCoefficientsAction 2))
    (Representation.Equiv.dualTensorHom (V := Vector) (W := Coefficients)
      vectorRepresentation coefficientAction)
  let b := currySymbols (U := FormCoefficients 2) (W := Vector) (E := Coefficients)
    (formCoefficientsAction 2) vectorRepresentation coefficientAction
  let c := transportHom (M := FormCoefficients 2 ⊗[ℝ] Vector) (U := JetTensors)
    toJetRepresentation (Representation.Equiv.refl coefficientAction)
  exact a.trans (b.symm.trans c)

private def wedgeSymbol : jetAction.IntertwiningMap (formCoefficientsAction 3) :=
  (⟨D7RealJets.wedgeJet, fun g => D7RealJets.wedgeJet_natural (vectorRepresentation.dual g)⟩ :
    formJetAction.IntertwiningMap (formAction 3)).rTensor coefficientAction

private def alternatingSection : (formCoefficientsAction 3).IntertwiningMap jetAction :=
  (⟨D7RealJets.includeThree, fun g => D7RealJets.includeThree_natural (vectorRepresentation.dual g)⟩ :
    (formAction 3).IntertwiningMap formJetAction).rTensor coefficientAction

@[simp] private theorem wedge_section (x : FormCoefficients 3) :
    wedgeSymbol (alternatingSection x) = x := by
  suffices h : (wedgeSymbol.toLinearMap).comp alternatingSection.toLinearMap = LinearMap.id from
    DFunLike.congr_fun h x
  apply TensorProduct.ext'
  intro u a
  change D7RealJets.wedgeJet (D7RealJets.includeThree u) ⊗ₜ[ℝ] a = u ⊗ₜ[ℝ] a
  exact congrArg (fun v => v ⊗ₜ[ℝ] a) (DFunLike.congr_fun D7RealJets.wedge_includeThree u)

/-- The real operator subspace whose divergence vanishes on the kernel of alternation. -/
def bianchiOperators : Submodule ℝ Operators where
  carrier := {T | ∀ s, wedgeSymbol s = 0 → divergenceSymbol T s = 0}
  zero_mem' := by intro s _; simp
  add_mem' := by intro T U hT hU s hs; simp [hT s hs, hU s hs]
  smul_mem' := by intro c T hT s hs; simp [hT s hs]

theorem mem_bianchi_iff (T : Operators) :
    T ∈ bianchiOperators ↔ ∀ s, wedgeSymbol s = 0 → divergenceSymbol T s = 0 := Iff.rfl

/-- Evaluate the divergence symbol on a skew first jet in real coordinates. -/
def coordinateDivergence (T : Operators) : BianchiSymbol.Jet Axis Coefficients →ₗ[ℝ] Coefficients :=
  (divergenceSymbol T).toLinearMap.comp (D7RealJets.jetEquiv (E := Coefficients)).symm.toLinearMap

set_option maxRecDepth 8192 in
private theorem mem_bianchi_iff_compatible (T : Operators) :
    T ∈ bianchiOperators ↔ BianchiSymbol.Compatible (coordinateDivergence T) := by
  rw [mem_bianchi_iff]
  have hw (s : JetTensors) :
      BianchiSymbol.ClosedJet (D7RealJets.jetEquiv s) ↔ wedgeSymbol s = 0 :=
    D7RealJets.closed_tensorJet_iff s
  have hcoord (J : BianchiSymbol.Jet Axis Coefficients) :
      coordinateDivergence T J =
        divergenceSymbol T ((D7RealJets.jetEquiv (E := Coefficients)).symm J) := by
    simp only [coordinateDivergence, LinearMap.comp_apply, LinearEquiv.coe_coe,
      Representation.IntertwiningMap.toLinearMap_apply]
  unfold BianchiSymbol.Compatible
  constructor
  · intro h J hJ
    have hs := (hw ((D7RealJets.jetEquiv (E := Coefficients)).symm J)).mp
      (by rwa [LinearEquiv.apply_symm_apply])
    rw [hcoord]
    exact h (D7RealJets.jetEquiv.symm J) hs
  · intro h s hs
    have he := h (D7RealJets.jetEquiv s) ((hw s).mpr hs)
    rwa [hcoord, LinearEquiv.symm_apply_apply] at he

section ClosedFields

open scoped Matrix.Norms.Elementwise

/-- Vanishing on all real closed fields with coefficient matrices in the unitary real form. -/
def VanishesOnClosedFields (T : Operators) : Prop :=
  ∀ (F : (Axis → ℝ) → Axis → Axis → Coefficients)
    (hF : ∀ x b c, F x c b = -F x b c),
    (∀ x a b c, DifferentiableAt ℝ (fun t : ℝ => F (x + t • Pi.single a 1) b c) 0) →
    BianchiSymbol.ClosedField F →
    ∀ x, coordinateDivergence T (BianchiSymbol.firstJet F hF x) = 0

theorem mem_bianchi_iff_closed_fields (T : Operators) :
    T ∈ bianchiOperators ↔ VanishesOnClosedFields T :=
  (mem_bianchi_iff_compatible T).trans (BianchiSymbol.compatible_iff_closed_fields (coordinateDivergence T))

end ClosedFields

private theorem bianchi_factor (T : ↥bianchiOperators) (s : JetTensors) :
    divergenceSymbol T.val (alternatingSection (wedgeSymbol s)) = divergenceSymbol T.val s := by
  have hz : wedgeSymbol (s - alternatingSection (wedgeSymbol s)) = 0 := by
    rw [map_sub, wedge_section, sub_self]
  have h := (mem_bianchi_iff T.val).mp T.prop _ hz
  rwa [map_sub, sub_eq_zero, eq_comm] at h

/-- The Bianchi-compatible operators are exactly the alternating symbol channel. -/
def bianchiEquiv : ↥bianchiOperators ≃ₗ[ℝ] ExteriorSymbols 3 where
  toFun T := (divergenceSymbol T.val).comp alternatingSection
  invFun A := ⟨divergenceSymbol.symm (A.comp wedgeSymbol), by
    apply (mem_bianchi_iff _).mpr
    intro s hs
    rw [LinearEquiv.apply_symm_apply]
    change A (wedgeSymbol s) = 0
    rw [hs, map_zero]⟩
  left_inv T := by
    apply Subtype.ext
    apply divergenceSymbol.injective
    rw [LinearEquiv.apply_symm_apply]
    apply Representation.IntertwiningMap.ext
    exact LinearMap.ext (bianchi_factor T)
  right_inv A := by
    simp only [LinearEquiv.apply_symm_apply]
    apply Representation.IntertwiningMap.ext
    apply LinearMap.ext
    intro x
    exact congrArg A (wedge_section x)
  map_add' T U := by
    apply Representation.IntertwiningMap.ext
    apply LinearMap.ext
    intro x
    exact DFunLike.congr_fun (congrArg Representation.IntertwiningMap.toLinearMap
      (map_add divergenceSymbol T.val U.val)) (alternatingSection x)
  map_smul' c T := by
    apply Representation.IntertwiningMap.ext
    apply LinearMap.ext
    intro x
    exact DFunLike.congr_fun (congrArg Representation.IntertwiningMap.toLinearMap
      (map_smul divergenceSymbol c T.val)) (alternatingSection x)

theorem bianchi_dimension : Module.finrank ℝ ↥bianchiOperators = 96 :=
  bianchiEquiv.finrank_eq.trans exterior_symbol_dimensions.2

abbrev VectorSymbols := oneFormCoefficientsAction.IntertwiningMap coefficientAction

private def realExteriorOne : (formAction 1).Equiv vectorRepresentation.dual :=
  Representation.Equiv.mk (exteriorPower.oneEquiv ℝ Covector) fun g =>
    exteriorPower.oneEquiv_naturality (vectorRepresentation.dual g)

theorem vector_symbol_dimension : Module.finrank ℝ VectorSymbols = 56 :=
  (transportHom (liftTensorEquiv realExteriorOne coefficientAction).symm
    (Representation.Equiv.refl coefficientAction)).finrank_eq.trans exterior_symbol_dimensions.1

private def traceSymbol : jetAction.IntertwiningMap oneFormCoefficientsAction :=
  (⟨D7RealJets.traceJet, D7RealJets.traceJet_equivariant⟩ :
    formJetAction.IntertwiningMap vectorRepresentation.dual).rTensor coefficientAction

private def vectorSection : oneFormCoefficientsAction.IntertwiningMap jetAction :=
  (⟨D7RealJets.includeVector, D7RealJets.includeVector_equivariant⟩ :
    vectorRepresentation.dual.IntertwiningMap formJetAction).rTensor coefficientAction

@[simp] private theorem trace_section (x : OneFormCoefficients) :
    traceSymbol (vectorSection x) = x := by
  suffices h : traceSymbol.toLinearMap.comp vectorSection.toLinearMap = LinearMap.id from
    DFunLike.congr_fun h x
  apply TensorProduct.ext'
  intro u a
  change D7RealJets.traceJet (D7RealJets.includeVector u) ⊗ₜ[ℝ] a = u ⊗ₜ[ℝ] a
  exact congrArg (fun v => v ⊗ₜ[ℝ] a) (DFunLike.congr_fun D7RealJets.trace_includeVector u)

@[simp] private theorem trace_alternating (x : FormCoefficients 3) :
    traceSymbol (alternatingSection x) = 0 := by
  suffices h : traceSymbol.toLinearMap.comp alternatingSection.toLinearMap = 0 from
    DFunLike.congr_fun h x
  apply TensorProduct.ext'
  intro u a
  have h := DFunLike.congr_fun D7RealJets.trace_includeThree u
  change D7RealJets.traceJet (D7RealJets.includeThree u) = 0 at h
  change D7RealJets.traceJet (D7RealJets.includeThree u) ⊗ₜ[ℝ] a = 0
  rw [h, TensorProduct.zero_tmul]

@[simp] private theorem wedge_vector (x : OneFormCoefficients) :
    wedgeSymbol (vectorSection x) = 0 := by
  suffices h : wedgeSymbol.toLinearMap.comp vectorSection.toLinearMap = 0 from
    DFunLike.congr_fun h x
  apply TensorProduct.ext'
  intro u a
  have h := DFunLike.congr_fun D7RealJets.wedge_includeVector u
  change D7RealJets.wedgeJet (D7RealJets.includeVector u) = 0 at h
  change D7RealJets.wedgeJet (D7RealJets.includeVector u) ⊗ₜ[ℝ] a = 0
  rw [h, TensorProduct.zero_tmul]

private def channelRestrictions : DivergenceSymbols →ₗ[ℝ] ExteriorSymbols 3 × VectorSymbols where
  toFun S := (S.comp alternatingSection, S.comp vectorSection)
  map_add' S T := by
    apply Prod.ext <;> apply Representation.IntertwiningMap.ext <;> apply LinearMap.ext <;>
      intro x <;> rfl
  map_smul' c S := by
    apply Prod.ext <;> apply Representation.IntertwiningMap.ext <;> apply LinearMap.ext <;>
      intro x <;> rfl

private theorem channelRestrictions_surjective : Function.Surjective channelRestrictions := by
  rintro ⟨A, V⟩
  refine ⟨A.comp wedgeSymbol + V.comp traceSymbol, ?_⟩
  apply Prod.ext <;> apply Representation.IntertwiningMap.ext <;> apply LinearMap.ext <;> intro x
  · change A (wedgeSymbol (alternatingSection x)) + V (traceSymbol (alternatingSection x)) = A x
    simp
  · change A (wedgeSymbol (vectorSection x)) + V (traceSymbol (vectorSection x)) = V x
    simp

/-- Symbols supported on the traceless hook, equivalently the symbols vanishing on the
alternating and vector inclusions. -/
def hookSymbols : Submodule ℝ DivergenceSymbols := channelRestrictions.ker

/-- Project first jets to the joint kernel of alternation and trace. -/
def hookProjection : jetAction.IntertwiningMap jetAction :=
  Representation.IntertwiningMap.id jetAction -
    alternatingSection.comp wedgeSymbol - vectorSection.comp traceSymbol

theorem hookProjection_mem (x : JetTensors) :
    wedgeSymbol (hookProjection x) = 0 ∧ traceSymbol (hookProjection x) = 0 := by
  change wedgeSymbol (x - alternatingSection (wedgeSymbol x) - vectorSection (traceSymbol x)) = 0 ∧
    traceSymbol (x - alternatingSection (wedgeSymbol x) - vectorSection (traceSymbol x)) = 0
  simp

theorem mem_hook_iff_project (S : DivergenceSymbols) :
    S ∈ hookSymbols ↔ S.comp hookProjection = S := by
  change channelRestrictions S = 0 ↔ _
  constructor
  · intro h
    have hA := congrArg Prod.fst h
    have hV := congrArg Prod.snd h
    change S.comp alternatingSection = 0 at hA
    change S.comp vectorSection = 0 at hV
    apply Representation.IntertwiningMap.ext
    apply LinearMap.ext
    intro x
    have ha : S (alternatingSection (wedgeSymbol x)) = 0 :=
      DFunLike.congr_fun hA (wedgeSymbol x)
    have hv : S (vectorSection (traceSymbol x)) = 0 :=
      DFunLike.congr_fun hV (traceSymbol x)
    change S (x - alternatingSection (wedgeSymbol x) - vectorSection (traceSymbol x)) = S x
    simp [ha, hv]
  · intro h
    apply Prod.ext <;> apply Representation.IntertwiningMap.ext <;> apply LinearMap.ext <;> intro x
    · have ha := DFunLike.congr_fun h (alternatingSection x)
      change S (alternatingSection x - alternatingSection (wedgeSymbol (alternatingSection x)) -
        vectorSection (traceSymbol (alternatingSection x))) = S (alternatingSection x) at ha
      exact (by simpa using ha.symm : S (alternatingSection x) = 0)
    · have hv := DFunLike.congr_fun h (vectorSection x)
      change S (vectorSection x - alternatingSection (wedgeSymbol (vectorSection x)) -
        vectorSection (traceSymbol (vectorSection x))) = S (vectorSection x) at hv
      exact (by simpa using hv.symm : S (vectorSection x) = 0)

theorem hook_symbol_dimension : Module.finrank ℝ ↥hookSymbols = 48 := by
  let : AddCommGroup (ExteriorSymbols 3) :=
    Representation.IntertwiningMap.instAddCommGroup (formCoefficientsAction 3) coefficientAction
  let : AddCommGroup VectorSymbols :=
    Representation.IntertwiningMap.instAddCommGroup oneFormCoefficientsAction coefficientAction
  have : Module.Finite ℝ (ExteriorSymbols 3) :=
    Module.finite_of_finrank_eq_succ exterior_symbol_dimensions.2
  have : Module.Finite ℝ VectorSymbols :=
    Module.finite_of_finrank_eq_succ vector_symbol_dimension
  have h := LinearMap.finrank_range_add_finrank_ker (K := ℝ) (V := DivergenceSymbols)
    (V₂ := ExteriorSymbols 3 × VectorSymbols) channelRestrictions
  have he := LinearMap.range_eq_top.mpr channelRestrictions_surjective
  have hd := divergenceSymbol.finrank_eq.symm.trans unrestricted_dimension
  rw [he, finrank_top, Module.finrank_prod, exterior_symbol_dimensions.2,
    vector_symbol_dimension, hd] at h
  change Module.finrank ℝ ↥channelRestrictions.ker = 48
  omega

/-- Theorem 3.4 on the actual real Spin representation and the real closed-field test. -/
theorem theorem_3_4 :
    Module.finrank ℝ Operators = 200 ∧
    Module.finrank ℝ (ExteriorSymbols 3) = 96 ∧
    Module.finrank ℝ VectorSymbols = 56 ∧
    Module.finrank ℝ ↥hookSymbols = 48 ∧
    Module.finrank ℝ ↥bianchiOperators = 96 ∧
    (∀ T : Operators, T ∈ bianchiOperators ↔ VanishesOnClosedFields T) :=
  ⟨unrestricted_dimension, exterior_symbol_dimensions.2, vector_symbol_dimension,
    hook_symbol_dimension, bianchi_dimension, mem_bianchi_iff_closed_fields⟩

end
end GeometricUnity.D7RealTheorem
~~~

[Return to file index](#file-index)

## Audit.lean {#source-audit-lean}

Prints the axiom dependencies of the indexed mathematical results.

~~~lean
import Theorem52
import WitnessW1
import BianchiSymbol
import D7Counts
import NoetherIdentity
import D7Final
import D7BianchiFields
import D7UnitaryRealForm
import D7SpinAction
import D7CliffordMatrix
import D7CliffordAdjoint
import D7SpinNullFrame
import D7SpinRootLifts
import D7SpinOrientation
import D7RootInterpolation
import D7RootGeneration
import D7RealComparison
import D7RealTheorem

/-! Report the axiom dependencies of the Geometric Unity formal results. -/

#print axioms GeometricUnity.Theorem52.theorem_5_2
#print axioms GeometricUnity.Theorem52.stationary_iff
#print axioms GeometricUnity.Theorem52.correction_skew
#print axioms GeometricUnity.Theorem52.einstein_euler

#print axioms GeometricUnity.WitnessW1.correction_value
#print axioms GeometricUnity.WitnessW1.correction_ne_zero
#print axioms GeometricUnity.WitnessW1.blade_skew
#print axioms GeometricUnity.WitnessW1.pairing_density

#print axioms GeometricUnity.BianchiSymbol.compatible_iff_unique_factor
#print axioms GeometricUnity.BianchiSymbol.closed_linear_realization
#print axioms GeometricUnity.BianchiSymbol.compatible_iff_closed_fields

#print axioms GeometricUnity.D7Counts.targets
#print axioms GeometricUnity.D7Counts.first_table
#print axioms GeometricUnity.D7Counts.second_table
#print axioms GeometricUnity.D7Counts.third_table
#print axioms GeometricUnity.D7Counts.grade_rows
#print axioms GeometricUnity.D7Counts.totals

#print axioms GeometricUnity.D7Final.gradeChannelSplit
#print axioms GeometricUnity.D7Final.bianchi_iff_factor
#print axioms GeometricUnity.D7Final.bianchi_grade_total
#print axioms GeometricUnity.D7Final.bianchi_hom_dimension
#print axioms GeometricUnity.D7Final.hook_by_grade
#print axioms GeometricUnity.D7Final.complex_channel_dimensions
#print axioms GeometricUnity.D7Final.real_dimension_of_comparison
#print axioms GeometricUnity.D7Final.real_dimension_of_action_span

#print axioms GeometricUnity.D7BianchiFields.cyclic_average_eq_projection
#print axioms GeometricUnity.D7BianchiFields.coordinateDivergence_pure_pair
#print axioms GeometricUnity.D7BianchiFields.mem_bianchiHom_iff_closed_fields

#print axioms GeometricUnity.D7UnitaryRealForm.complexificationEquiv
#print axioms GeometricUnity.D7UnitaryRealForm.complexification_intertwines
#print axioms GeometricUnity.D7SpinAction.vectorRepresentation_preserves
#print axioms GeometricUnity.D7SpinAction.equivExterior_intertwines
#print axioms GeometricUnity.D7SpinAction.equivExterior_grade_action

#print axioms GeometricUnity.D7CliffordMatrix.spinor_finrank
#print axioms GeometricUnity.D7CliffordMatrix.matrixEquiv
#print axioms GeometricUnity.D7CliffordMatrix.complexMatrixEquiv_intertwines
#print axioms GeometricUnity.D7CliffordAdjoint.matrixEquiv_star
#print axioms GeometricUnity.D7CliffordAdjoint.signature_eigenvalue_counts
#print axioms GeometricUnity.D7CliffordAdjoint.spinorUnits_preserve_signature
#print axioms GeometricUnity.D7CliffordAdjoint.cliffordCoefficientEquiv_intertwines
#print axioms GeometricUnity.D7SpinNullFrame.complexNullAction_preserves
#print axioms GeometricUnity.D7SpinNullFrame.realNullAction_isotropicLift
#print axioms GeometricUnity.D7SpinRootLifts.isotropicLift_val
#print axioms GeometricUnity.D7SpinRootLifts.isotropicLift_action
#print axioms GeometricUnity.D7SpinOrientation.vectorRepresentation_det
#print axioms GeometricUnity.D7SpinNullFrame.spinToSO
#print axioms GeometricUnity.D7SpinNullFrame.exists_rootGroup_lift
#print axioms GeometricUnity.D7RootInterpolation.rootGroup_tensorActions_mem_spin_span
#print axioms GeometricUnity.D7RootInterpolation.rootClosure_tensorActions_mem_spin_span
#print axioms GeometricUnity.D7RootGeneration.splitSpecialOrthogonal_eq_rootClosure
#print axioms GeometricUnity.D7RootGeneration.splitSO_tensorActions_mem_spin_span
#print axioms GeometricUnity.D7RealComparison.coefficientComplexEquiv_intertwines
#print axioms GeometricUnity.D7RealComparison.formCoefficientComparison
#print axioms GeometricUnity.D7RealComparison.covectorCoefficientComparison
#print axioms GeometricUnity.D7RealTheorem.mem_bianchi_iff_closed_fields
#print axioms GeometricUnity.D7RealTheorem.mem_hook_iff_project
#print axioms GeometricUnity.D7RealTheorem.theorem_3_4

#print axioms GeometricUnity.NoetherIdentity.curvature_gauge
#print axioms GeometricUnity.NoetherIdentity.dressedAction_gauge
#print axioms GeometricUnity.NoetherIdentity.dressingJet_snd
#print axioms GeometricUnity.NoetherIdentity.dressingDerivative_eq_neg_pair
#print axioms GeometricUnity.NoetherIdentity.gaugeBoundary_iff_ordinary
#print axioms GeometricUnity.NoetherIdentity.dressingDerivative_eq_divergence
#print axioms GeometricUnity.NoetherIdentity.theorem_6_1
~~~

[Return to file index](#file-index)

## D7Counts.lean {#source-d7counts-lean}

Computes signed integer multiplicities and verifies the fifteen grade rows and channel totals.

~~~lean
import Mathlib.Data.Int.Basic

/-!
# Geometric Unity: the finite D₇ calculation in Theorem 3.4

The program computes the signed multiplicity tables and their pairings
over the integers. The exterior-grade highest-weight lists are inputs
to the calculation. Identifying these pairings with dimensions of
equivariant Hom spaces uses the representation-theoretic argument in
the note.
-/

namespace GeometricUnity.D7Counts

abbrev Weight := List ℤ
abbrev Multiplicities := List (Weight × ℤ)

def zeroWeight : Weight := List.replicate 7 0
def addWeight (w v : Weight) : Weight := List.zipWith (· + ·) w v
def subWeight (w v : Weight) : Weight := List.zipWith (· - ·) w v

def unitWeight (i : ℕ) (sign : ℤ) : Weight :=
  (List.range 7).map fun j => if i = j then sign else 0

def vectorWeights : List Weight :=
  (List.range 7).flatMap fun i => [unitWeight i 1, unitWeight i (-1)]

/-- Choose positions in a list, preserving repeated values in the output. -/
def choosePositions {α : Type} : ℕ → List α → List (List α)
  | 0, _ => [[]]
  | _ + 1, [] => []
  | n + 1, a :: rest =>
      (choosePositions n rest).map (a :: ·) ++ choosePositions (n + 1) rest

def exteriorWeights (r : ℕ) : List Weight :=
  (choosePositions r vectorWeights).map fun selected =>
    selected.foldl addWeight zeroWeight

def rho : Weight := [6, 5, 4, 3, 2, 1, 0]

/-- Insert by decreasing absolute value. Passing an entry reverses the
permutation sign. A repeated absolute value makes the weight singular. -/
def insertAbs (x : ℤ) : Weight → Option (Weight × ℤ)
  | [] => some ([x], 1)
  | y :: ys =>
      if x.natAbs = y.natAbs then none
      else if y.natAbs < x.natAbs then some (x :: y :: ys, 1)
      else (insertAbs x ys).map fun (zs, sign) => (y :: zs, -sign)

def sortAbs : Weight → Option (Weight × ℤ)
  | [] => some ([], 1)
  | x :: xs => do
      let (ys, sign₁) ← sortAbs xs
      let (zs, sign₂) ← insertAbs x ys
      pure (zs, sign₁ * sign₂)

/-- Make the first six coordinates positive and put the compensating
sign, when needed, on the seventh coordinate. The sign component is
the determinant because the number of coordinate sign flips is even. -/
def reflect (w : Weight) : Option (Weight × ℤ) := do
  let (sorted, sign) ← sortAbs w
  match sorted with
  | [a, b, c, d, e, f, g] =>
      let first := [a, b, c, d, e, f]
      let flips := (first.filter (· < 0)).length
      pure (first.map (fun x => (x.natAbs : ℤ)) ++ [if flips % 2 = 1 then -g else g], sign)
  | _ => none

def addMultiplicity (w : Weight) (m : ℤ) : Multiplicities → Multiplicities
  | [] => [(w, m)]
  | (v, n) :: tail =>
      match compare w v with
      | .lt => (w, m) :: (v, n) :: tail
      | .eq => (v, n + m) :: tail
      | .gt => (v, n) :: addMultiplicity w m tail

def tally (terms : Multiplicities) : Multiplicities :=
  let summed := terms.foldl (fun table (w, m) => addMultiplicity w m table) []
  summed.filter fun (_, m) => m != 0

def coefficient (terms : Multiplicities) (w : Weight) : ℤ :=
  (terms.lookup w).getD 0

def mu (k : ℕ) : Weight :=
  (List.range 7).map fun i => if i < k then 1 else 0

def muMinus : Weight := [1, 1, 1, 1, 1, 1, -1]

def nu (k : ℕ) : Weight := 2 :: (mu k).drop 1
def nuMinus : Weight := 2 :: muMinus.drop 1

/-- The supplied highest-weight labels for each exterior grade. -/
def gradeWeights (k : ℕ) : List Weight :=
  if k > 14 then []
  else
    let j := min k (14 - k)
    if j = 7 then [mu 7, muMinus] else [mu j]

def signedTerms (weights highestWeights : List Weight) : Multiplicities :=
  highestWeights.flatMap fun highest =>
    let shifted := addWeight highest rho
    weights.filterMap fun w =>
      (reflect (addWeight shifted w)).map fun (dom, sign) =>
        (subWeight dom rho, sign)

def cliffordMultiplicities : Multiplicities :=
  tally <| (List.range 15).flatMap fun k => (gradeWeights k).map (·, 1)

def vectorTarget : Multiplicities :=
  tally <| signedTerms (exteriorWeights 1) ((List.range 15).flatMap gradeWeights)

def gradeMultiplicities (r k : ℕ) : Multiplicities :=
  tally <| signedTerms (exteriorWeights r) (gradeWeights k)

def retain (target source : Multiplicities) : Multiplicities :=
  source.filter fun (w, _) => coefficient target w != 0

def pairing (source target : Multiplicities) : ℤ :=
  (source.map fun (w, n) => n * coefficient target w).sum

structure Row where
  unrestricted : ℤ
  alternating : ℤ
  vector : ℤ
  hook : ℤ
  deriving DecidableEq, Repr

def gradeRow (k : ℕ) : Row :=
  let u := pairing (gradeMultiplicities 2 k) vectorTarget
  let b := pairing (gradeMultiplicities 3 k) cliffordMultiplicities
  let v := pairing (gradeMultiplicities 1 k) cliffordMultiplicities
  ⟨u, b, v, u - b - v⟩

def rows : List Row := (List.range 15).map gradeRow

def addRows (x y : Row) : Row :=
  ⟨x.unrestricted + y.unrestricted, x.alternating + y.alternating,
    x.vector + y.vector, x.hook + y.hook⟩

def total : Row := rows.foldl addRows ⟨0, 0, 0, 0⟩

set_option maxRecDepth 4096 in
/-- The cardinalities count retained subsets, including those with the same
weight sum. -/
theorem exterior_weight_counts :
    ((exteriorWeights 1).length, (exteriorWeights 2).length, (exteriorWeights 3).length) =
      (14, 91, 364) := by decide

theorem chamber_examples :
    reflect [6, 5, 4, 3, 2, 1, -1] = none ∧
    reflect [5, -6, 4, 3, 2, 1, 0] = some ([6, 5, 4, 3, 2, 1, 0], -1) ∧
    reflect [-7, 6, 5, 4, 3, 2, 1] = some ([7, 6, 5, 4, 3, 2, -1], 1) := by decide

private def unitTable (weights : List Weight) : Multiplicities :=
  tally (weights.map (·, 1))

set_option maxRecDepth 4096 in
theorem targets :
    cliffordMultiplicities = tally (((List.range 7).map fun k => (mu k, 2)) ++
      [(mu 7, 1), (muMinus, 1)]) ∧
    vectorTarget = tally ([(mu 0, 2)] ++
      ((List.range 6).map fun k => (mu (k + 1), 4)) ++
      [(mu 7, 2), (muMinus, 2)] ++
      ((List.range 6).map fun k => (nu (k + 1), 2)) ++ [(nu 7, 1), (nuMinus, 1)]) := by
  decide +kernel

/-- The r = 2 entries contributing to the unrestricted pairing, in grades 0–7. -/
def expectedSecond : List (List Weight) :=
  [[mu 2],
   [mu 1, nu 2, mu 3],
   [mu 2, nu 1, nu 3, mu 0, mu 4],
   [mu 3, nu 2, nu 4, mu 1, mu 5],
   [mu 4, nu 3, nu 5, mu 2, mu 6],
   [mu 5, nu 4, nu 6, mu 3, mu 7, muMinus],
   [mu 6, mu 6, nu 5, nu 7, nuMinus, mu 4],
   [mu 7, muMinus, nu 6, nu 6, mu 5, mu 5]]

/-- The r = 3 entries contributing to the alternating pairing, in grades 0–7. -/
def expectedThird : List (List Weight) :=
  [[mu 3],
   [mu 2, mu 4],
   [mu 1, mu 3, mu 5],
   [mu 2, mu 4, mu 0, mu 6],
   [mu 3, mu 5, mu 1, mu 7, muMinus],
   [mu 4, mu 6, mu 6, mu 2],
   [mu 5, mu 5, mu 7, muMinus, mu 3],
   [mu 6, mu 6, mu 4, mu 4]]

/-- The r = 1 entries contributing to the vector pairing, in grades 0–7. -/
def expectedFirst : List (List Weight) :=
  [[mu 1], [mu 0, mu 2], [mu 1, mu 3], [mu 2, mu 4], [mu 3, mu 5],
   [mu 4, mu 6], [mu 5, mu 7, muMinus], [mu 6, mu 6]]

def retainedTable (r : ℕ) (target : Multiplicities) : List Multiplicities :=
  (List.range 8).map fun k => retain target (gradeMultiplicities r k)

set_option maxRecDepth 4096 in
set_option maxHeartbeats 4000000 in
theorem first_table : retainedTable 1 cliffordMultiplicities = expectedFirst.map unitTable := by
  decide +kernel

set_option maxRecDepth 4096 in
set_option maxHeartbeats 4000000 in
theorem second_table : retainedTable 2 vectorTarget = expectedSecond.map unitTable := by
  decide +kernel

set_option maxRecDepth 4096 in
set_option maxHeartbeats 4000000 in
theorem third_table : retainedTable 3 cliffordMultiplicities = expectedThird.map unitTable := by
  decide +kernel

def expectedRows : List Row :=
  [⟨4, 2, 2, 0⟩, ⟨10, 4, 4, 2⟩, ⟨14, 6, 4, 4⟩,
   ⟨16, 8, 4, 4⟩, ⟨16, 8, 4, 4⟩, ⟨16, 8, 4, 4⟩, ⟨16, 8, 4, 4⟩,
   ⟨16, 8, 4, 4⟩,
   ⟨16, 8, 4, 4⟩, ⟨16, 8, 4, 4⟩, ⟨16, 8, 4, 4⟩, ⟨16, 8, 4, 4⟩,
   ⟨14, 6, 4, 4⟩, ⟨10, 4, 4, 2⟩, ⟨4, 2, 2, 0⟩]

set_option maxRecDepth 4096 in
set_option maxHeartbeats 4000000 in
theorem grade_rows : rows = expectedRows := by decide +kernel

theorem totals : total = ⟨200, 96, 56, 48⟩ := by
  rw [total, grade_rows]
  decide

end GeometricUnity.D7Counts
~~~

[Return to file index](#file-index)

## D7Classification.lean {#source-d7classification-lean}

Provides general decomposition, intertwiner-dimension, block decomposition, and real-to-complex comparison lemmas.

~~~lean
import D7Counts
import Mathlib.Analysis.Complex.Polynomial.Basic
import Mathlib.CategoryTheory.Preadditive.Biproducts
import Mathlib.Data.Matrix.Mul
import Mathlib.LinearAlgebra.Complex.FiniteDimensional
import Mathlib.RepresentationTheory.FDRep
import Mathlib.Tactic.Module
import Mathlib.Tactic.NormNum

/-!
# Geometric Unity: representation-theoretic dimension bridge

The Hom-dimension calculation applies to decompositions into pairwise
nonisomorphic simple representations. For the D₇ application, the
decomposition isomorphisms identifying the signed weight tables with
exterior-power tensor products are explicit hypotheses.
-/

noncomputable section

namespace GeometricUnity.D7Classification

open CategoryTheory CategoryTheory.Limits
open scoped BigOperators

/-- The linear block-matrix description of maps between finite biproducts. -/
def blockHomEquiv (k : Type*) [Field k] {C : Type*} [Category C]
    [Preadditive C] [Linear k C] [HasFiniteBiproducts C]
    {I J : Type} [Fintype I] [Fintype J] (P : I → C) (Q : J → C) :
    (⨁ P ⟶ ⨁ Q) ≃ₗ[k] (∀ i j, P i ⟶ Q j) where
  toEquiv := biproduct.matrixEquiv (f := P) (g := Q)
  map_add' f g := by
    funext i j
    change biproduct.components (f + g) i j = _
    simp [biproduct.components, Preadditive.comp_add, Preadditive.add_comp]
  map_smul' r f := by
    funext i j
    change biproduct.components (r • f) i j = _
    simp [biproduct.components, Linear.comp_smul, Linear.smul_comp]

section Multiplicities

variable {k : Type*} [Field k] {G : Type*} [Monoid G]

local instance : HasFiniteBiproducts (FDRep k G) :=
  HasFiniteBiproducts.of_hasFiniteProducts

/-- The copies of the simple objects indicated by the multiplicity function. -/
abbrev Copies {I : Type} (S : I → FDRep k G) (m : I → ℕ) :
    (Σ i, Fin (m i)) → FDRep k G := fun i => S i.1

/-- A simple Hom block has rank one precisely when its two labels agree. -/
private theorem simple_block [IsAlgClosed k] {I : Type} [DecidableEq I]
    (S : I → FDRep k G) (simple : ∀ i, Simple (S i))
    (distinct : ∀ i j, i ≠ j → ¬ Nonempty (S i ≅ S j)) (i j : I) :
    Module.finrank k (S i ⟶ S j) = if i = j then 1 else 0 := by
  let : Simple (S i) := simple i
  let : Simple (S j) := simple j
  rw [FDRep.finrank_hom_simple_simple]
  by_cases h : i = j
  · subst j
    simp [show Nonempty (S i ≅ S i) from ⟨Iso.refl _⟩]
  · simp [h, distinct i j h]

/-- With explicit decomposition isomorphisms, the dimension of the
intertwiner space is the sum of the products of the multiplicities. -/
theorem finrank_hom_of_decompositions [IsAlgClosed k] {I : Type} [Fintype I]
    (S : I → FDRep k G) (simple : ∀ i, Simple (S i))
    (distinct : ∀ i j, i ≠ j → ¬ Nonempty (S i ≅ S j))
    (p q : I → ℕ) (P Q : FDRep k G) (eP : P ≅ ⨁ Copies S p) (eQ : Q ≅ ⨁ Copies S q) :
    Module.finrank k (P ⟶ Q) = ∑ i, p i * q i := by
  classical
  have sumTarget (i : I) :
      (∑ u : Σ j, Fin (q j), if i = u.1 then 1 else 0) = q i := by
    have h (j : I) : (∑ _ : Fin (q j), if i = j then 1 else 0) = if i = j then q j else 0 := by
      by_cases hij : i = j <;> simp [hij]
    simp only [Fintype.sum_sigma, h]
    rw [Finset.sum_eq_single i]
    · simp
    · intro j _ hji
      exact if_neg (Ne.symm hji)
    · simp
  calc
    Module.finrank k (P ⟶ Q) = Module.finrank k (⨁ Copies S p ⟶ ⨁ Copies S q) :=
      (Linear.homCongr k eP eQ).finrank_eq
    _ = Module.finrank k (∀ u v, Copies S p u ⟶ Copies S q v) :=
      (blockHomEquiv k (Copies S p) (Copies S q)).finrank_eq
    _ = ∑ u : Σ i, Fin (p i), q u.1 := by
      simp only [Module.finrank_pi_fintype, Copies, simple_block S simple distinct, sumTarget]
    _ = ∑ i, p i * q i := by
      rw [Fintype.sum_sigma]
      simp

/-- Intertwiner dimensions add over the source grades. -/
theorem finrank_hom_biproduct_source {I : Type} [Fintype I] (P : I → FDRep k G)
    (C Q : FDRep k G) (e : C ≅ ⨁ P) :
    Module.finrank k (C ⟶ Q) = ∑ i, Module.finrank k (P i ⟶ Q) := by
  let B : (⨁ P ⟶ Q) ≃ₗ[k] (∀ i, P i ⟶ Q) :=
    { toFun := fun f i => biproduct.ι P i ≫ f
      invFun := biproduct.desc
      left_inv := fun f => biproduct.hom_ext' _ _ (by simp)
      right_inv := fun f => funext fun i => biproduct.ι_desc f i
      map_add' := by intro f g; funext i; simp [Preadditive.comp_add]
      map_smul' := by intro r f; funext i; simp [Linear.comp_smul] }
  rw [(Linear.homCongr k e (Iso.refl Q)).finrank_eq, B.finrank_eq, Module.finrank_pi_fintype]

/-! The integer weight lists are read as multiplicity functions on the
union of their supports. -/

open D7Counts

private def keys (entries : Multiplicities) : Finset Weight :=
  (entries.map Prod.fst).toFinset

private theorem coefficient_cons (w v : Weight) (n : ℤ) (tail : Multiplicities) :
    coefficient ((v, n) :: tail) w = if w = v then n else coefficient tail w := by
  by_cases h : w = v
  · subst v
    simp [coefficient]
  · have hb : (w == v) = false := Bool.eq_false_iff.mpr (fun he => h (eq_of_beq he))
    simp [coefficient, List.lookup_cons, hb, h]

private theorem coefficient_outside (entries : Multiplicities) (w : Weight) (h : w ∉ keys entries) :
    coefficient entries w = 0 := by
  have hn : entries.lookup w = none := List.lookup_eq_none_iff.mpr fun entry he => by
    have hne : w ≠ entry.1 := fun hw => h (by
      unfold keys
      exact List.mem_toFinset.mpr (List.mem_map.mpr ⟨entry, he, hw.symm⟩))
    simp [hne]
  simp [coefficient, hn]

private theorem pairing_eq_sum_keys (source target : Multiplicities) (h : (source.map Prod.fst).Nodup) :
    pairing source target = ∑ w ∈ keys source, coefficient source w * coefficient target w := by
  induction source with
  | nil => simp [pairing, keys]
  | cons head tail ih =>
    rcases head with ⟨v, n⟩
    simp only [List.map_cons, List.nodup_cons] at h
    have hv : v ∉ keys tail := by simpa [keys] using h.1
    have keyCons : keys ((v, n) :: tail) = insert v (keys tail) := by simp [keys]
    change n * coefficient target v + pairing tail target = _
    rw [keyCons, Finset.sum_insert hv, coefficient_cons v v n tail, if_pos rfl, ih h.2]
    congr 1
    apply Finset.sum_congr rfl
    intro w hw
    have hne : w ≠ v := fun hwv => hv (hwv ▸ hw)
    rw [coefficient_cons w v n tail, if_neg hne]

def labels (source target : Multiplicities) : Finset Weight := keys source ∪ keys target

private theorem pairing_eq_sum_labels (source target : Multiplicities) (h : (source.map Prod.fst).Nodup) :
    pairing source target = ∑ w ∈ labels source target, coefficient source w * coefficient target w := by
  rw [pairing_eq_sum_keys _ _ h]
  apply Finset.sum_subset Finset.subset_union_left
  intro w _ hw
  rw [coefficient_outside source w hw, zero_mul]

private def multiplicity (entries : Multiplicities) (w : Weight) : ℕ :=
  (coefficient entries w).toNat

/-- The representation-theoretic input for a checked pair of weight tables.
In the application the simple objects are identified by highest weight,
and the two isomorphisms are the exterior-power/tensor-product decompositions. -/
structure TableDecomposition (source target : Multiplicities) (P Q : FDRep ℂ G) where
  simples : ↥(labels source target) → FDRep ℂ G
  simple : ∀ i, Simple (simples i)
  distinct : ∀ i j, i ≠ j → ¬ Nonempty (simples i ≅ simples j)
  source_nonnegative : ∀ i : ↥(labels source target), 0 ≤ coefficient source i.val
  target_nonnegative : ∀ i : ↥(labels source target), 0 ≤ coefficient target i.val
  source_iso : P ≅ ⨁ Copies simples (fun i => multiplicity source i.val)
  target_iso : Q ≅ ⨁ Copies simples (fun i => multiplicity target i.val)

theorem finrank_hom_eq_pairing {source target : Multiplicities} {P Q : FDRep ℂ G}
    (decomp : TableDecomposition source target P Q) (h : (source.map Prod.fst).Nodup) :
    (Module.finrank ℂ (P ⟶ Q) : ℤ) = pairing source target := by
  rw [finrank_hom_of_decompositions decomp.simples decomp.simple decomp.distinct _ _ P Q
    decomp.source_iso decomp.target_iso, pairing_eq_sum_labels _ _ h, Nat.cast_sum]
  rw [Finset.sum_subtype (labels source target) (fun _ => Iff.rfl)]
  apply Finset.sum_congr rfl
  intro i _
  simp only [Nat.cast_mul, multiplicity, Int.toNat_of_nonneg (decomp.source_nonnegative i),
    Int.toNat_of_nonneg (decomp.target_nonnegative i)]

set_option maxRecDepth 4096 in
set_option maxHeartbeats 4000000 in
private theorem grade_keys_nodup :
    ∀ (r : Fin 3) (k : Fin 15), ((gradeMultiplicities (r.val + 1) k.val).map Prod.fst).Nodup := by
  decide +kernel

/-- The ordinary and signed middle-degree labels both enter the calculation. -/
theorem middle_grade_labels : gradeWeights 7 = [mu 7, muMinus] := by decide

private theorem sum_grade_column (f : Row → ℤ) :
    (∑ k : Fin 15, f (gradeRow k.val)) = (expectedRows.map f).sum := by
  rw [Fin.sum_univ_eq_sum_range (fun k => f (gradeRow k)) 15]
  have h := List.sum_toFinset (fun k => f (gradeRow k)) (List.nodup_range (n := 15))
  rw [List.toFinset_range] at h
  rw [h]
  change ((List.range 15).map (f ∘ gradeRow)).sum = _
  rw [← List.map_map]
  change (rows.map f).sum = _
  rw [grade_rows]

/-- The three checked totals are dimensions under the indicated
equivariant decomposition isomorphisms. For Theorem 3.4, the intended
source families are Λ²V ⊗ Cₖ, Λ³V ⊗ Cₖ, and V ⊗ Cₖ. The respective
targets are V ⊗ C, C, and C. The middle exterior degree is included
in each of the fifteen grade families. -/
theorem checked_hom_dimensions
    (U B V : Fin 15 → FDRep ℂ G) (Uall Ball Vall VC C : FDRep ℂ G)
    (uGrades : Uall ≅ ⨁ U) (bGrades : Ball ≅ ⨁ B) (vGrades : Vall ≅ ⨁ V)
    (uDecomp : ∀ k : Fin 15, TableDecomposition (gradeMultiplicities 2 k.val) vectorTarget (U k) VC)
    (bDecomp : ∀ k : Fin 15, TableDecomposition (gradeMultiplicities 3 k.val) cliffordMultiplicities (B k) C)
    (vDecomp : ∀ k : Fin 15, TableDecomposition (gradeMultiplicities 1 k.val) cliffordMultiplicities (V k) C) :
    (Module.finrank ℂ (Uall ⟶ VC), Module.finrank ℂ (Ball ⟶ C), Module.finrank ℂ (Vall ⟶ C)) =
    (200, 96, 56) := by
  have hu (k : Fin 15) : (Module.finrank ℂ (U k ⟶ VC) : ℤ) = (gradeRow k.val).unrestricted :=
    finrank_hom_eq_pairing (uDecomp k) (grade_keys_nodup 1 k)
  have hb (k : Fin 15) : (Module.finrank ℂ (B k ⟶ C) : ℤ) = (gradeRow k.val).alternating :=
    finrank_hom_eq_pairing (bDecomp k) (grade_keys_nodup 2 k)
  have hv (k : Fin 15) : (Module.finrank ℂ (V k ⟶ C) : ℤ) = (gradeRow k.val).vector :=
    finrank_hom_eq_pairing (vDecomp k) (grade_keys_nodup 0 k)
  have hU : (Module.finrank ℂ (Uall ⟶ VC) : ℤ) = 200 := by
    rw [finrank_hom_biproduct_source U Uall VC uGrades, Nat.cast_sum]
    simp_rw [hu]
    rw [sum_grade_column Row.unrestricted]
    decide
  have hB : (Module.finrank ℂ (Ball ⟶ C) : ℤ) = 96 := by
    rw [finrank_hom_biproduct_source B Ball C bGrades, Nat.cast_sum]
    simp_rw [hb]
    rw [sum_grade_column Row.alternating]
    decide
  have hV : (Module.finrank ℂ (Vall ⟶ C) : ℤ) = 56 := by
    rw [finrank_hom_biproduct_source V Vall C vGrades, Nat.cast_sum]
    simp_rw [hv]
    rw [sum_grade_column Row.vector]
    decide
  have Udim : Module.finrank ℂ (Uall ⟶ VC) = 200 := by exact_mod_cast hU
  have Bdim : Module.finrank ℂ (Ball ⟶ C) = 96 := by exact_mod_cast hB
  have Vdim : Module.finrank ℂ (Vall ⟶ C) = 56 := by exact_mod_cast hV
  rw [Udim, Bdim, Vdim]

/-- The residual hook dimension follows from the direct-sum splitting
of the unrestricted symbol Hom space. -/
theorem hook_finrank_of_split (U B V H : Type*) [AddCommGroup U] [Module ℂ U]
    [AddCommGroup B] [Module ℂ B] [AddCommGroup V] [Module ℂ V] [AddCommGroup H] [Module ℂ H]
    [FiniteDimensional ℂ B] [FiniteDimensional ℂ V] [FiniteDimensional ℂ H]
    (split : U ≃ₗ[ℂ] B × V × H)
    (hU : Module.finrank ℂ U = 200) (hB : Module.finrank ℂ B = 96) (hV : Module.finrank ℂ V = 56) :
    Module.finrank ℂ H = 48 := by
  have h := split.finrank_eq
  rw [Module.finrank_prod, Module.finrank_prod, hU, hB, hV] at h
  omega

end Multiplicities

section RealDescent

variable {E : Type*} [AddCommGroup E] [Module ℂ E]

/-- The fixed vectors of the real-linear conjugation. -/
def Fixed (s : E →ₗ[ℝ] E) : Submodule ℝ E :=
  LinearMap.ker (s - LinearMap.id)

theorem mem_fixed (s : E →ₗ[ℝ] E) (x : E) : x ∈ Fixed s ↔ s x = x := by
  change s x - x = 0 ↔ _
  exact sub_eq_zero

private def mulI : E →ₗ[ℝ] E where
  toFun x := Complex.I • x
  map_add' _ _ := smul_add _ _ _
  map_smul' r x := smul_comm Complex.I r x

private theorem mulI_sq (x : E) : mulI (mulI x) = -x := by
  change Complex.I • (Complex.I • x) = -x
  rw [smul_smul, Complex.I_mul_I, neg_one_smul]

private def realPart (s : E →ₗ[ℝ] E) (invol : Function.Involutive s) : E →ₗ[ℝ] Fixed s :=
  ((1 / 2 : ℝ) • (LinearMap.id + s)).codRestrict (Fixed s) (fun x => by
    apply (mem_fixed _ _).2
    change s ((1 / 2 : ℝ) • (x + s x)) = (1 / 2 : ℝ) • (x + s x)
    rw [map_smul, map_add, invol, add_comm])

/-- Real and imaginary parts of a complex vector with respect to its
real form. The inverse sends the pair (u,v) to u + i v. -/
private def realFormEquiv (s : E →ₗ[ℝ] E) (invol : Function.Involutive s)
    (anti : ∀ x, s (mulI x) = -mulI (s x)) : E ≃ₗ[ℝ] Fixed s × Fixed s := by
  let R := realPart s invol
  let split : E →ₗ[ℝ] Fixed s × Fixed s := R.prod (R.comp (-mulI))
  refine { split with invFun := fun p => p.1.val + mulI p.2.val, left_inv := ?_, right_inv := ?_ }
  · intro x
    change (1 / 2 : ℝ) • (x + s x) +
      mulI ((1 / 2 : ℝ) • (-mulI x + s (-mulI x))) = x
    simp only [map_neg, anti, neg_neg, map_smul, map_add, mulI_sq]
    module
  · rintro ⟨u,v⟩
    have hu := (mem_fixed s u.val).1 u.property
    have hv := (mem_fixed s v.val).1 v.property
    apply Prod.ext
    · apply Subtype.ext
      change (1 / 2 : ℝ) • (u.val + mulI v.val + s (u.val + mulI v.val)) = u.val
      simp only [map_add, hu, anti, hv]
      module
    · apply Subtype.ext
      change (1 / 2 : ℝ) •
        (-mulI (u.val + mulI v.val) + s (-mulI (u.val + mulI v.val))) = v.val
      simp only [map_neg, map_add, mulI_sq, anti, hu, hv]
      module

/-- A complex representation space and its real form have equal dimensions
over their respective fields. The same statement applies to a Hom space
equipped with its induced conjugation. -/
theorem finrank_fixed_of_conjugation [FiniteDimensional ℂ E] (s : E →ₗ[ℝ] E)
    (invol : Function.Involutive s)
    (anti : ∀ x, s (Complex.I • x) = -(Complex.I • s x)) :
    Module.finrank ℝ (Fixed s) = Module.finrank ℂ E := by
  have h := (realFormEquiv s invol anti).finrank_eq
  rw [finrank_real_of_complex, Module.finrank_prod] at h
  omega

end RealDescent

section MatrixDescent

open scoped ComplexConjugate

variable {G m n : Type*} [Fintype m] [Fintype n]

/-- Intertwiner equations written in chosen bases. The scalar-extension
argument works for arbitrary families of action matrices. -/
def matrixIntertwiners {K : Type*} [Field K]
    (ρ : G → Matrix m m K) (τ : G → Matrix n n K) : Submodule K (Matrix n m K) where
  carrier := {M | ∀ g, M * ρ g = τ g * M}
  zero_mem' := by intro g; simp
  add_mem' := by
    intro X Y hX hY g
    change (X + Y) * ρ g = τ g * (X + Y)
    rw [Matrix.add_mul, Matrix.mul_add, hX g, hY g]
  smul_mem' := by
    intro r X hX g
    change (r • X) * ρ g = τ g * (r • X)
    rw [Matrix.smul_mul, Matrix.mul_smul, hX g]

def complexMatrices {j l : Type*} (X : Matrix j l ℝ) : Matrix j l ℂ :=
  X.map Complex.ofRealHom

private theorem complexMatrices_mul {j l r : Type*} [Fintype l]
    (M : Matrix j l ℝ) (N : Matrix l r ℝ) :
    complexMatrices (M * N) = complexMatrices M * complexMatrices N := Matrix.map_mul

variable (ρ : G → Matrix m m ℝ) (τ : G → Matrix n n ℝ)

abbrev ComplexIntertwiners := ↥(matrixIntertwiners (complexMatrices ∘ ρ) (complexMatrices ∘ τ))
abbrev RealIntertwiners := ↥(matrixIntertwiners ρ τ)

private theorem conjugate_real_matrix {j l : Type*} (X : Matrix j l ℝ) :
    (complexMatrices X).map conj = complexMatrices X := by
  ext i j
  exact Complex.conj_ofReal _

private def conjugateIntertwiner :
    ComplexIntertwiners ρ τ →ₗ[ℝ] ComplexIntertwiners ρ τ where
  toFun X := ⟨X.val.map conj, by
    intro g
    have h := congrArg (fun M : Matrix n m ℂ => M.map conj) (X.property g)
    simpa only [Function.comp_apply, Matrix.map_mul, conjugate_real_matrix] using h⟩
  map_add' X Y := by
    apply Subtype.ext
    ext i j
    exact map_add conj (X.val i j) (Y.val i j)
  map_smul' r X := by
    apply Subtype.ext
    ext i j
    exact map_smul Complex.conjAe.toLinearEquiv r (X.val i j)

private theorem conjugateIntertwiner_invol :
    Function.Involutive (conjugateIntertwiner ρ τ) := by
  intro X
  apply Subtype.ext
  ext i j
  exact star_star (X.val i j)

private theorem conjugateIntertwiner_anti (X : ComplexIntertwiners ρ τ) :
    conjugateIntertwiner ρ τ (Complex.I • X) = -(Complex.I • conjugateIntertwiner ρ τ X) := by
  apply Subtype.ext
  ext i j
  change conj (Complex.I * X.val i j) = -(Complex.I * conj (X.val i j))
  rw [map_mul, Complex.conj_I, neg_mul]

private def extendIntertwiner (X : RealIntertwiners ρ τ) : ComplexIntertwiners ρ τ :=
  ⟨complexMatrices X.val, by
    intro g
    have h := congrArg complexMatrices (X.property g)
    simpa only [complexMatrices, Matrix.map_mul, Function.comp_apply] using h⟩

private theorem extendIntertwiner_fixed (X : RealIntertwiners ρ τ) :
    extendIntertwiner ρ τ X ∈ Fixed (conjugateIntertwiner ρ τ) := by
  apply (mem_fixed _ _).2
  exact Subtype.ext (conjugate_real_matrix X.val)

private theorem fixed_eq_real_extension (X : Fixed (conjugateIntertwiner ρ τ)) :
    complexMatrices (X.val.val.map Complex.re) = X.val.val := by
  ext i j
  have hf := (mem_fixed _ _).1 X.property
  have hij : conj (X.val.val i j) = X.val.val i j :=
    congrArg (fun Y : ComplexIntertwiners ρ τ => Y.val i j) hf
  exact Complex.conj_eq_iff_re.mp hij

private def restrictIntertwiner (X : Fixed (conjugateIntertwiner ρ τ)) : RealIntertwiners ρ τ :=
  ⟨X.val.val.map Complex.re, by
    intro g
    apply Matrix.map_injective (f := Complex.ofRealHom) Complex.ofReal_injective
    have h := fixed_eq_real_extension ρ τ X
    change complexMatrices (_ * ρ g) = complexMatrices (τ g * _)
    rw [complexMatrices_mul, complexMatrices_mul, h]
    exact X.val.property g⟩

private def realIntertwinersEquivFixed :
    RealIntertwiners ρ τ ≃ₗ[ℝ] Fixed (conjugateIntertwiner ρ τ) where
  toFun X := ⟨extendIntertwiner ρ τ X, extendIntertwiner_fixed ρ τ X⟩
  invFun := restrictIntertwiner ρ τ
  left_inv X := by
    apply Subtype.ext
    ext i j
    exact Complex.ofReal_re _
  right_inv X := by
    apply Subtype.ext
    apply Subtype.ext
    exact fixed_eq_real_extension ρ τ X
  map_add' X Y := by
    apply Subtype.ext
    apply Subtype.ext
    ext i j
    exact map_add Complex.ofRealHom (X.val i j) (Y.val i j)
  map_smul' r X := by
    apply Subtype.ext
    apply Subtype.ext
    ext i j
    exact map_smul Complex.ofRealAm.toLinearMap r (X.val i j)

/-- Entrywise complexification of the action matrices preserves the
intertwiner dimension. This applies to a real group action in chosen
bases with the same group acting on the complexified spaces. -/
theorem finrank_real_complex_intertwiners :
    Module.finrank ℝ (RealIntertwiners ρ τ) = Module.finrank ℂ (ComplexIntertwiners ρ τ) :=
  (realIntertwinersEquivFixed ρ τ).finrank_eq.trans
    (finrank_fixed_of_conjugation (conjugateIntertwiner ρ τ)
      (conjugateIntertwiner_invol ρ τ) (conjugateIntertwiner_anti ρ τ))

end MatrixDescent

end GeometricUnity.D7Classification
~~~

[Return to file index](#file-index)

## D7Exterior.lean {#source-d7exterior-lean}

Defines the split complex orthogonal action and checks exterior weights, highest-weight candidates, and Weyl dimensions.

~~~lean
import D7Counts
import Mathlib.Data.Complex.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.LinearAlgebra.ExteriorPower.Basis
import Mathlib.LinearAlgebra.Basis.VectorSpace
import Mathlib.LinearAlgebra.Transvection.Basic
import Mathlib.RepresentationTheory.FDRep
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-!
# Weights of the exterior powers of the D₇ vector representation

The split basis is ordered `+e₁, -e₁, …, +e₇, -e₇`. The exterior basis
realizes the weight multisets used by `D7Counts`. In each degree, the
listed highest-weight candidates are nonzero torus weight vectors fixed
by the positive-root unipotents. The final checks evaluate the Weyl
products for these labels and compare them with the exterior dimensions.
-/

namespace GeometricUnity.D7Exterior

open scoped BigOperators

abbrev Axis := Fin 14
abbrev Pair := Fin 7
abbrev Space := Axis → ℂ
abbrev Index (k : ℕ) := Set.powersetCard Axis k

def pairIndex (j : Axis) : Pair := ⟨j.val / 2, by omega⟩

def axisSign (j : Axis) : ℤ := if j.val % 2 = 0 then 1 else -1

def axisWeight (j : Axis) (i : Pair) : ℤ :=
  if pairIndex j = i then axisSign j else 0

def subsetWeight (s : Finset Axis) (i : Pair) : ℤ := ∑ j ∈ s, axisWeight j i

def scale (t : Pair → ℂˣ) (j : Axis) : ℂˣ := t (pairIndex j) ^ axisSign j

def torus (t : Pair → ℂˣ) : Space →ₗ[ℂ] Space where
  toFun v j := (scale t j : ℂ) * v j
  map_add' v w := by ext j; exact mul_add _ _ _
  map_smul' c v := by ext j; exact mul_left_comm _ _ _

noncomputable def axisBasis : Module.Basis Axis ℂ Space := Pi.basisFun ℂ Axis

theorem torus_axis (t : Pair → ℂˣ) (j : Axis) :
    torus t (axisBasis j) = (scale t j : ℂ) • axisBasis j := by
  ext l
  change (scale t l : ℂ) * (axisBasis j) l = (scale t j : ℂ) * (axisBasis j) l
  by_cases h : l = j
  · subst l; rfl
  · simp [axisBasis, Pi.basisFun_apply, h]

private theorem scale_product (t : Pair → ℂˣ) (j : Axis) :
    (∏ i : Pair, t i ^ axisWeight j i) = scale t j := by
  rw [Finset.prod_eq_single (pairIndex j)]
  · simp [axisWeight, scale]
  · intro i _ hi
    simp [axisWeight, Ne.symm hi]
  · simp

private theorem pow_sum (t : ℂˣ) (s : Finset Axis) (w : Axis → ℤ) :
    t ^ (∑ j ∈ s, w j) = ∏ j ∈ s, t ^ w j := by
  induction s using Finset.induction_on with
  | empty => simp
  | @insert j s hj ih => simp [hj, zpow_add, ih]

theorem subset_character (t : Pair → ℂˣ) (s : Finset Axis) :
    (∏ j ∈ s, scale t j) = ∏ i : Pair, t i ^ subsetWeight s i := by
  simp only [← scale_product t, subsetWeight, pow_sum]
  exact Finset.prod_comm

/-- Every exterior basis vector is a weight vector for the diagonal torus. -/
theorem torus_exterior (t : Pair → ℂˣ) (k : ℕ) (s : Index k) :
    exteriorPower.map k (torus t) (axisBasis.exteriorPower k s) =
      ((∏ i : Pair, t i ^ subsetWeight s.val i : ℂˣ) : ℂ) • axisBasis.exteriorPower k s := by
  rw [← subset_character, exteriorPower.basis_apply, exteriorPower.map_apply_ιMulti_family]
  let e := s.val.orderIsoOfFin s.prop
  change exteriorPower.ιMulti ℂ k (fun j => torus t (axisBasis (e j).val)) =
    ((∏ j ∈ s.val, scale t j : ℂˣ) : ℂ) •
      exteriorPower.ιMulti ℂ k (fun j => axisBasis (e j).val)
  simp only [torus_axis]
  rw [AlternatingMap.map_smul_univ]
  congr 1
  rw [Units.coe_prod]
  trans ∏ j : s.val, (scale t j.val : ℂ)
  · exact Fintype.prod_equiv e.toEquiv (fun j => (scale t (e j).val : ℂ))
      (fun j => (scale t j.val : ℂ)) fun _ ↦ rfl
  · exact Finset.prod_coe_sort s.val (fun j => (scale t j : ℂ))

def axisLabel (j : Axis) : D7Counts.Weight := List.ofFn (axisWeight j)

theorem vector_weights_eq : (List.ofFn axisLabel) = D7Counts.vectorWeights := by
  decide +kernel

private theorem add_labels (u v : Pair → ℤ) :
    D7Counts.addWeight (List.ofFn u) (List.ofFn v) = List.ofFn fun i => u i + v i := by
  simp only [D7Counts.addWeight]
  apply List.ext_getElem
  · simp
  · intro n h₁ h₂
    simp

private theorem selected_label (l : List Axis) (v : Pair → ℤ) :
    (l.map axisLabel).foldl D7Counts.addWeight (List.ofFn v) =
      List.ofFn fun i => v i + (l.map fun j => axisWeight j i).sum := by
  induction l generalizing v with
  | nil => simp
  | cons a l ih =>
    simp only [List.map_cons, List.foldl_cons, axisLabel, add_labels, ih, List.sum_cons, add_assoc]

private theorem choosePositions_map {α β : Type} (f : α → β) (k : ℕ) (l : List α) :
    D7Counts.choosePositions k (l.map f) = (D7Counts.choosePositions k l).map (List.map f) := by
  induction l generalizing k with
  | nil => cases k <;> rfl
  | cons a l ih =>
    cases k with
    | zero => rfl
    | succ k => simp [D7Counts.choosePositions, ih, List.map_map, Function.comp_def]

private theorem choosePositions_perm {α : Type} (k : ℕ) (l : List α) :
    (D7Counts.choosePositions k l).Perm (l.sublistsLen k) := by
  induction l generalizing k with
  | nil => cases k <;> exact List.Perm.refl _
  | cons a l ih =>
    cases k with
    | zero => simp [D7Counts.choosePositions]
    | succ k =>
      rw [D7Counts.choosePositions, List.sublistsLen_succ_cons]
      exact List.perm_append_comm.trans ((ih (k + 1)).append ((ih k).map (a :: ·)))

private theorem chosen_subsets {α : Type} (k : ℕ) (l : List α) :
    (((D7Counts.choosePositions k l).map ((↑) : List α → Multiset α)) : Multiset (Multiset α)) =
      Multiset.powersetCard k (l : Multiset α) := by
  rw [Multiset.powersetCard_coe]
  exact Quot.sound ((choosePositions_perm k l).map ((↑) : List α → Multiset α))

def exteriorBasisLabels (k : ℕ) : Multiset D7Counts.Weight :=
  ((Finset.univ : Finset Axis).powersetCard k).val.map fun s => List.ofFn (subsetWeight s)

/-- The case computation uses the weights of the exterior basis, with their multiplicities. -/
theorem exterior_weights_eq (k : ℕ) :
    (D7Counts.exteriorWeights k : Multiset D7Counts.Weight) = exteriorBasisLabels k := by
  have haxes : ((List.ofFn (id : Axis → Axis) : List Axis) : Multiset Axis) = Finset.univ.val := by
    decide +kernel
  have hlabel : D7Counts.vectorWeights = (List.ofFn (id : Axis → Axis)).map axisLabel := by
    rw [← vector_weights_eq, List.map_ofFn]
    rfl
  let weight (s : Multiset Axis) : D7Counts.Weight :=
    List.ofFn fun i => (s.map fun j => axisWeight j i).sum
  calc
    _ = ((Multiset.powersetCard k ((List.ofFn (id : Axis → Axis) : List Axis) : Multiset Axis))).map weight := by
      rw [D7Counts.exteriorWeights, hlabel, choosePositions_map, ← chosen_subsets,
        List.map_map, Multiset.map_coe, List.map_map]
      congr 1
      apply List.map_congr_left
      intro l _
      change (l.map axisLabel).foldl D7Counts.addWeight D7Counts.zeroWeight = weight l
      rw [D7Counts.zeroWeight, ← List.ofFn_const, selected_label]
      simp [weight]
    _ = _ := by
      rw [haxes, ← Finset.map_val_val_powersetCard, Multiset.map_map]
      rfl

def lastMinus : Index 7 := ⟨{0, 2, 4, 6, 8, 10, 13}, by change Finset.card _ = 7; decide⟩

theorem lastMinus_weight : List.ofFn (subsetWeight lastMinus.val) = D7Counts.muMinus := by
  decide +kernel

def plusAxis (i : Pair) : Axis := ⟨2 * i.val, by omega⟩
def minusAxis (i : Pair) : Axis := ⟨2 * i.val + 1, by omega⟩

private def splitTerm (v w : Space) (i : Pair) : ℂ :=
  v (plusAxis i) * w (minusAxis i) + v (minusAxis i) * w (plusAxis i)

/-- The bilinear form in the null basis. -/
def splitForm (v w : Space) : ℂ := ∑ i : Pair, splitTerm v w i

private theorem plus_injective : Function.Injective plusAxis := by
  intro i j h
  have hn := congrArg Fin.val h
  change 2 * i.val = 2 * j.val at hn
  exact Fin.ext (by omega)

private theorem minus_injective : Function.Injective minusAxis := by
  intro i j h
  have hn := congrArg Fin.val h
  change 2 * i.val + 1 = 2 * j.val + 1 at hn
  exact Fin.ext (by omega)

private theorem plus_ne_minus (i j : Pair) : plusAxis i ≠ minusAxis j := by
  intro h
  have hn := congrArg Fin.val h
  change 2 * i.val = 2 * j.val + 1 at hn
  omega

private theorem minus_ne_plus (i j : Pair) : minusAxis i ≠ plusAxis j :=
  Ne.symm (plus_ne_minus j i)

theorem torus_preserves_splitForm (t : Pair → ℂˣ) (v w : Space) :
    splitForm (torus t v) (torus t w) = splitForm v w := by
  apply Finset.sum_congr rfl
  intro i _
  have hp : pairIndex (plusAxis i) = i := Fin.ext (by
    change (2 * i.val) / 2 = i.val
    omega)
  have hm : pairIndex (minusAxis i) = i := Fin.ext (by
    change (2 * i.val + 1) / 2 = i.val
    omega)
  have hsp : axisSign (plusAxis i) = 1 := if_pos (by change (2 * i.val) % 2 = 0; omega)
  have hsm : axisSign (minusAxis i) = -1 := if_neg (by change (2 * i.val + 1) % 2 ≠ 0; omega)
  change (scale t (plusAxis i) : ℂ) * v (plusAxis i) *
      ((scale t (minusAxis i) : ℂ) * w (minusAxis i)) +
    (scale t (minusAxis i) : ℂ) * v (minusAxis i) *
      ((scale t (plusAxis i) : ℂ) * w (plusAxis i)) =
    v (plusAxis i) * w (minusAxis i) + v (minusAxis i) * w (plusAxis i)
  have hc : (scale t (plusAxis i) : ℂ) * (scale t (minusAxis i) : ℂ) = 1 := by
    rw [← Units.val_mul]
    simp [scale, hp, hm, hsp, hsm]
  linear_combination (v (plusAxis i) * w (minusAxis i) +
    v (minusAxis i) * w (plusAxis i)) * hc

theorem torus_det (t : Pair → ℂˣ) : (torus t).det = 1 := by
  have hzero : ∀ i : Pair, subsetWeight Finset.univ i = 0 := by decide +kernel
  calc
    (torus t).det = axisBasis.det (torus t ∘ axisBasis) := by
      rw [Module.Basis.det_comp, Module.Basis.det_self, mul_one]
    _ = ∏ j : Axis, (scale t j : ℂ) := by
      simp only [Function.comp_def, torus_axis, AlternatingMap.map_smul_univ,
        Module.Basis.det_self, smul_eq_mul, mul_one]
    _ = 1 := by rw [← Units.coe_prod, subset_character]; simp [hzero]

private def highestAxes (k : Fin 15) : Finset Axis :=
  Finset.univ.filter fun a =>
    if k.val ≤ 7 then a.val % 2 = 0 ∧ a.val / 2 < k.val
    else a.val % 2 = 0 ∨ 14 - k.val ≤ a.val / 2

private theorem highestAxes_card : ∀ k : Fin 15, (highestAxes k).card = k.val := by
  decide +kernel

/-- In degrees above seven, keep all positive axes and include both axes of
the last `k - 7` pairs. -/
def highestPlus (k : Fin 15) : Index k.val := ⟨highestAxes k, highestAxes_card k⟩

private noncomputable def elementary (p q : Axis) : Space →ₗ[ℂ] Space :=
  (axisBasis.coord q).smulRight (axisBasis p)

private theorem elementary_axis (p q j : Axis) :
    elementary p q (axisBasis j) = if j = q then axisBasis p else 0 := by
  by_cases h : j = q
  · subst j; simp [elementary]
  · simp [elementary, h, Ne.symm h]

/-- The two signed elementary entries of a positive-root unipotent. -/
noncomputable def rootGroup (c : ℂ) (p q r u : Axis) : Space →ₗ[ℂ] Space :=
  LinearMap.id + c • elementary p q - c • elementary r u

noncomputable def rootMinus (c : ℂ) (i j : Pair) : Space →ₗ[ℂ] Space :=
  rootGroup c (plusAxis i) (plusAxis j) (minusAxis j) (minusAxis i)

noncomputable def rootPlus (c : ℂ) (i j : Pair) : Space →ₗ[ℂ] Space :=
  rootGroup c (plusAxis i) (minusAxis j) (plusAxis j) (minusAxis i)

private theorem rootGroup_factor (c : ℂ) (p q r u : Axis) (hqr : q ≠ r) :
    rootGroup c p q r u = (LinearMap.id + c • elementary p q).comp
      (LinearMap.id + (-c) • elementary r u) := by
  apply axisBasis.ext
  intro j
  by_cases hk : j = u <;>
    simp [rootGroup, LinearMap.comp_apply, elementary_axis, hk, Ne.symm hqr,
      sub_eq_add_neg, add_assoc, add_left_comm, add_comm]

private theorem elementary_transvection_det (c : ℂ) (p q : Axis) (hpq : p ≠ q) :
    (LinearMap.id + c • elementary p q).det = 1 := by
  have he : LinearMap.id + c • elementary p q =
      LinearMap.transvection (axisBasis.coord q) (c • axisBasis p) := by
    apply LinearMap.ext
    intro v
    change v + c • (axisBasis.coord q v • axisBasis p) =
      v + axisBasis.coord q v • (c • axisBasis p)
    rw [smul_comm]
  rw [he, LinearMap.transvection.det]
  simp [Ne.symm hpq]

private theorem rootGroup_det (c : ℂ) (p q r u : Axis) (hpq : p ≠ q) (hru : r ≠ u)
    (hqr : q ≠ r) : (rootGroup c p q r u).det = 1 := by
  rw [rootGroup_factor c p q r u hqr, LinearMap.det_comp,
    elementary_transvection_det _ _ _ hpq, elementary_transvection_det _ _ _ hru, mul_one]

theorem rootMinus_det (c : ℂ) (i j : Pair) (h : i < j) : (rootMinus c i j).det = 1 :=
  rootGroup_det _ _ _ _ _ (fun e => (ne_of_lt h) (plus_injective e))
    (fun e => (ne_of_gt h) (minus_injective e)) (plus_ne_minus j j)

theorem rootPlus_det (c : ℂ) (i j : Pair) : (rootPlus c i j).det = 1 :=
  rootGroup_det _ _ _ _ _ (plus_ne_minus i j) (plus_ne_minus j i) (minus_ne_plus j j)

private theorem rootGroup_coord (c : ℂ) (p q r u : Axis) (v : Space) (l : Axis) :
    rootGroup c p q r u v l = v l + (if l = p then c * v q else 0) -
      (if l = r then c * v u else 0) := by
  change v l + c * ((axisBasis.coord q v : ℂ) * axisBasis p l) -
    c * ((axisBasis.coord u v : ℂ) * axisBasis r l) = _
  simp [axisBasis, Module.Basis.coord_apply, Pi.basisFun_repr, Pi.basisFun_apply,
    Pi.single_apply, mul_ite]

private theorem sum_eq_of_pair (f g : Pair → ℂ) (i j : Pair) (h : i ≠ j)
    (hout : ∀ l, l ≠ i → l ≠ j → f l = g l) (hin : f i + f j = g i + g j) :
    ∑ l, f l = ∑ l, g l := by
  rw [← sub_eq_zero, ← Finset.sum_sub_distrib, ← Finset.sum_subset
    (s₁ := {i, j}) (s₂ := Finset.univ) (Finset.subset_univ _)]
  · rw [Finset.sum_pair h]
    linear_combination hin
  · intro l _ hl
    simp only [Finset.mem_insert, Finset.mem_singleton, not_or] at hl
    rw [hout l hl.1 hl.2, sub_self]

theorem rootMinus_preserves_splitForm (c : ℂ) (i j : Pair) (h : i < j) (v w : Space) :
    splitForm (rootMinus c i j v) (rootMinus c i j w) = splitForm v w := by
  apply sum_eq_of_pair _ _ i j (ne_of_lt h)
  · intro l hi hj
    simp [splitTerm, rootMinus, rootGroup_coord, plus_ne_minus, minus_ne_plus,
      plus_injective.eq_iff, minus_injective.eq_iff, hi, hj]
  · simp [splitTerm, rootMinus, rootGroup_coord, plus_ne_minus, minus_ne_plus,
      plus_injective.eq_iff, minus_injective.eq_iff, ne_of_lt h, ne_of_gt h]
    ring

theorem rootPlus_preserves_splitForm (c : ℂ) (i j : Pair) (h : i < j) (v w : Space) :
    splitForm (rootPlus c i j v) (rootPlus c i j w) = splitForm v w := by
  apply sum_eq_of_pair _ _ i j (ne_of_lt h)
  · intro l hi hj
    simp [splitTerm, rootPlus, rootGroup_coord, minus_ne_plus, plus_injective.eq_iff, hi, hj]
  · simp [splitTerm, rootPlus, rootGroup_coord, minus_ne_plus, plus_injective.eq_iff,
      ne_of_lt h, ne_of_gt h]
    ring

/-- The split special orthogonal elements, realized by their endomorphisms.
The determinant-one condition ensures invertibility. -/
noncomputable def splitSpecialOrthogonal : Submonoid (Module.End ℂ Space) where
  carrier := {f | f.det = 1 ∧ ∀ v w, splitForm (f v) (f w) = splitForm v w}
  one_mem' := ⟨map_one LinearMap.det, fun _ _ => rfl⟩
  mul_mem' := by
    rintro f g ⟨hf, hformf⟩ ⟨hg, hformg⟩
    exact ⟨by rw [map_mul, hf, hg, mul_one], fun v w => (hformf (g v) (g w)).trans (hformg v w)⟩

noncomputable def torusElement (t : Pair → ℂˣ) : splitSpecialOrthogonal :=
  ⟨torus t, torus_det t, torus_preserves_splitForm t⟩

noncomputable def rootMinusElement (c : ℂ) (i j : Pair) (h : i < j) : splitSpecialOrthogonal :=
  ⟨rootMinus c i j, rootMinus_det c i j h, rootMinus_preserves_splitForm c i j h⟩

noncomputable def rootPlusElement (c : ℂ) (i j : Pair) (h : i < j) : splitSpecialOrthogonal :=
  ⟨rootPlus c i j, rootPlus_det c i j, rootPlus_preserves_splitForm c i j h⟩

/-- The first positive axis is fixed by the positive-root maps of the vector action. -/
theorem firstAxis_root_fixed (c : ℂ) (i j : Pair) (h : i < j) :
    (rootMinusElement c i j h).val (axisBasis (plusAxis 0)) = axisBasis (plusAxis 0) ∧
    (rootPlusElement c i j h).val (axisBasis (plusAxis 0)) = axisBasis (plusAxis 0) := by
  have hj : (0 : Pair) ≠ j := (lt_of_le_of_lt (Fin.zero_le i) h).ne
  have haxis : plusAxis 0 ≠ plusAxis j := fun e => hj (plus_injective e)
  change rootMinus c i j (axisBasis (plusAxis 0)) = _ ∧ rootPlus c i j (axisBasis (plusAxis 0)) = _
  simp [rootMinus, rootPlus, rootGroup, elementary_axis, haxis, plus_ne_minus]

noncomputable def exteriorRepresentation (k : ℕ) :
    Representation ℂ splitSpecialOrthogonal (⋀[ℂ]^k Space) where
  toFun f := exteriorPower.map k f.val
  map_one' := exteriorPower.map_id
  map_mul' f g := exteriorPower.map_comp g.val f.val

noncomputable def exteriorFDRep (k : ℕ) : FDRep ℂ splitSpecialOrthogonal :=
  FDRep.of (exteriorRepresentation k)

theorem splitSpecialOrthogonal_isUnit (f : splitSpecialOrthogonal) : IsUnit f.val :=
  (LinearMap.isUnit_iff_isUnit_det f.val).mpr (f.property.1 ▸ isUnit_one)

private theorem wedge_fixed_by_single_addition (k : ℕ) (s : Index k) (f : Space →ₗ[ℂ] Space)
    (c : ℂ) (p q : Axis) (hpq : p ≠ q) (hmem : q ∈ s.val → p ∈ s.val)
    (hf : ∀ j ∈ s.val, f (axisBasis j) = axisBasis j + if j = q then c • axisBasis p else 0) :
    exteriorPower.map k f (axisBasis.exteriorPower k s) = axisBasis.exteriorPower k s := by
  let e := Set.powersetCard.ofFinEmbEquiv.symm s
  let v : Fin k → Space := axisBasis ∘ e
  rw [exteriorPower.basis_apply, exteriorPower.map_apply_ιMulti_family]
  change exteriorPower.ιMulti ℂ k (fun j => f (v j)) = exteriorPower.ιMulti ℂ k v
  have he (j : Fin k) : e j ∈ s.val :=
    Finset.orderEmbOfFin_mem s.val s.prop j
  by_cases hq : q ∈ s.val
  · obtain ⟨a, ha⟩ := (Set.powersetCard.mem_range_ofFinEmbEquiv_symm_iff_mem s q).mpr hq
    obtain ⟨b, hb⟩ := (Set.powersetCard.mem_range_ofFinEmbEquiv_symm_iff_mem s p).mpr (hmem hq)
    change e a = q at ha
    change e b = p at hb
    have hab : a ≠ b := fun h => hpq (hb.symm.trans (h ▸ ha))
    have hu : (fun j => f (v j)) = Function.update v a (v a + c • axisBasis p) := by
      funext j
      by_cases h : j = a
      · subst j
        have hfa := hf q hq
        simpa [v, ha] using hfa
      · have h' : e j ≠ q := fun hj => h (e.injective (hj.trans ha.symm))
        simp [v, hf _ (he j), Function.update_of_ne h, h']
    have hz : exteriorPower.ιMulti ℂ k (Function.update v a (axisBasis p)) = 0 := by
      apply (exteriorPower.ιMulti ℂ k).map_eq_zero_of_eq _ (i := a) (j := b) _ hab
      simp [v, Function.update_of_ne hab.symm, hb]
    rw [hu, AlternatingMap.map_update_add, AlternatingMap.map_update_smul, hz,
      smul_zero, add_zero]
    congr 1
    exact Function.update_eq_self a v
  · have hfix (j : Fin k) : f (v j) = v j := by
      have h : e j ≠ q := fun h => hq (h ▸ he j)
      simp [v, hf _ (he j), h]
    simp only [hfix]

private theorem wedge_fixed_by_root (k : ℕ) (s : Index k) (c : ℂ) (p q r u : Axis)
    (hpq : p ≠ q) (hru : r ≠ u) (hqr : q ≠ r)
    (hp : q ∈ s.val → p ∈ s.val) (hr : u ∈ s.val → r ∈ s.val) :
    exteriorPower.map k (rootGroup c p q r u) (axisBasis.exteriorPower k s) =
      axisBasis.exteriorPower k s := by
  let f : Space →ₗ[ℂ] Space := LinearMap.id + c • elementary p q
  let g : Space →ₗ[ℂ] Space := LinearMap.id + (-c) • elementary r u
  have hf : exteriorPower.map k f (axisBasis.exteriorPower k s) = axisBasis.exteriorPower k s := by
    apply wedge_fixed_by_single_addition k s f c p q hpq hp
    intro j _
    simp [f, elementary_axis, smul_ite]
  have hg : exteriorPower.map k g (axisBasis.exteriorPower k s) = axisBasis.exteriorPower k s := by
    apply wedge_fixed_by_single_addition k s g (-c) r u hru hr
    intro j _
    simp [g, elementary_axis, smul_ite]
  have hcomp : rootGroup c p q r u = f.comp g := rootGroup_factor c p q r u hqr
  rw [hcomp, exteriorPower.map_comp, LinearMap.comp_apply, hg, hf]

private def CanAdd (s : Finset Axis) (p q r u : Axis) : Prop :=
  p ≠ q ∧ r ≠ u ∧ q ≠ r ∧ (q ∈ s → p ∈ s) ∧ (u ∈ s → r ∈ s)

set_option maxRecDepth 4000 in
set_option maxHeartbeats 2000000 in
private theorem highestPlus_positions : ∀ (k : Fin 15) (i j : Pair), i < j →
    CanAdd (highestPlus k).val (plusAxis i) (plusAxis j) (minusAxis j) (minusAxis i) ∧
    CanAdd (highestPlus k).val (plusAxis i) (minusAxis j) (plusAxis j) (minusAxis i) := by
  unfold CanAdd
  decide +kernel

private theorem lastMinus_positions : ∀ i j : Pair, i < j →
    CanAdd lastMinus.val (plusAxis i) (plusAxis j) (minusAxis j) (minusAxis i) ∧
    CanAdd lastMinus.val (plusAxis i) (minusAxis j) (plusAxis j) (minusAxis i) := by
  unfold CanAdd
  decide +kernel

theorem highestPlus_weight : ∀ k : Fin 15,
    List.ofFn (subsetWeight (highestPlus k).val) = D7Counts.mu (min k.val (14 - k.val)) := by
  decide +kernel

private theorem fixed_of_positions (k : ℕ) (s : Index k) (c : ℂ)
    (i j : Pair)
    (h₁ : CanAdd s.val (plusAxis i) (plusAxis j) (minusAxis j) (minusAxis i))
    (h₂ : CanAdd s.val (plusAxis i) (minusAxis j) (plusAxis j) (minusAxis i)) :
    exteriorPower.map k (rootMinus c i j) (axisBasis.exteriorPower k s) = axisBasis.exteriorPower k s ∧
      exteriorPower.map k (rootPlus c i j) (axisBasis.exteriorPower k s) = axisBasis.exteriorPower k s := by
  rcases h₁ with ⟨hp₁, hr₁, hqu₁, hq₁, hu₁⟩
  rcases h₂ with ⟨hp₂, hr₂, hqu₂, hq₂, hu₂⟩
  exact ⟨wedge_fixed_by_root k s c _ _ _ _ hp₁ hr₁ hqu₁ hq₁ hu₁,
    wedge_fixed_by_root k s c _ _ _ _ hp₂ hr₂ hqu₂ hq₂ hu₂⟩

/-- In every degree the positive-label wedge is fixed by all positive-root maps. -/
theorem highestPlus_root_fixed (k : Fin 15) (c : ℂ) (i j : Pair) (h : i < j) :
    exteriorRepresentation k.val (rootMinusElement c i j h) (axisBasis.exteriorPower k.val (highestPlus k)) =
        axisBasis.exteriorPower k.val (highestPlus k) ∧
      exteriorRepresentation k.val (rootPlusElement c i j h) (axisBasis.exteriorPower k.val (highestPlus k)) =
        axisBasis.exteriorPower k.val (highestPlus k) :=
  fixed_of_positions _ _ c i j (highestPlus_positions k i j h).1 (highestPlus_positions k i j h).2

/-- The wedge with the seventh axis negative is also fixed by the positive roots. -/
theorem lastMinus_root_fixed (c : ℂ) (i j : Pair) (h : i < j) :
    exteriorRepresentation 7 (rootMinusElement c i j h) (axisBasis.exteriorPower 7 lastMinus) =
        axisBasis.exteriorPower 7 lastMinus ∧
      exteriorRepresentation 7 (rootPlusElement c i j h) (axisBasis.exteriorPower 7 lastMinus) =
        axisBasis.exteriorPower 7 lastMinus :=
  fixed_of_positions _ _ c i j (lastMinus_positions i j h).1 (lastMinus_positions i j h).2

/-- The list of candidate labels is the one used in every exterior grade table. -/
theorem grade_weights_eq : ∀ k : Fin 15,
    D7Counts.gradeWeights k.val = List.ofFn (subsetWeight (highestPlus k).val) ::
      (if k.val = 7 then [List.ofFn (subsetWeight lastMinus.val)] else []) := by
  decide +kernel

theorem highestPlus_ne_zero (k : Fin 15) : axisBasis.exteriorPower k.val (highestPlus k) ≠ 0 :=
  (axisBasis.exteriorPower k.val).ne_zero _

theorem lastMinus_ne_zero : axisBasis.exteriorPower 7 lastMinus ≠ 0 :=
  (axisBasis.exteriorPower 7).ne_zero _

/-- The two middle-grade candidates come from distinct exterior basis vectors. -/
theorem middle_candidates_independent :
    LinearIndependent ℂ (fun i : Fin 2 => axisBasis.exteriorPower 7
      (if i = 0 then highestPlus (7 : Fin 15) else lastMinus)) := by
  apply (axisBasis.exteriorPower 7).linearIndependent.comp
  have hne : highestPlus (7 : Fin 15) ≠ lastMinus := by
    intro h
    have hv := congrArg Subtype.val h
    have hvals : (highestPlus (7 : Fin 15)).val ≠ lastMinus.val := by decide +kernel
    exact hvals hv
  intro i j h
  fin_cases i <;> fin_cases j <;> simp_all

private def orderedPairs : Finset (Pair × Pair) :=
  Finset.univ.filter fun ij => ij.1 < ij.2

/-- The rational product obtained by inserting a label into the D₇ Weyl formula. -/
def weylProduct (w : D7Counts.Weight) : ℚ :=
  let shifted (i : Pair) : ℤ := (6 - (i.val : ℤ)) + w[i.val]?.getD 0
  ∏ ij ∈ orderedPairs,
    (((shifted ij.1)^2 - (shifted ij.2)^2 : ℤ) : ℚ) /
      (((6 - (ij.1.val : ℤ))^2 - (6 - (ij.2.val : ℤ))^2 : ℤ) : ℚ)

theorem weyl_product_values :
    (∀ k : Fin 7, weylProduct (D7Counts.mu k.val) = (Nat.choose 14 k.val : ℚ)) ∧
      weylProduct (D7Counts.mu 7) = 1716 ∧ weylProduct D7Counts.muMinus = 1716 := by
  decide +kernel

/-- The evaluated products exhaust the actual ambient exterior dimensions. -/
theorem grade_products_exhaust_finrank (k : Fin 15) :
    ((D7Counts.gradeWeights k.val).map weylProduct).sum =
      (Module.finrank ℂ (⋀[ℂ]^k.val Space) : ℚ) := by
  rw [exteriorPower.finrank_eq, Module.finrank_pi, Fintype.card_fin]
  have h : ∀ k : Fin 15, ((D7Counts.gradeWeights k.val).map weylProduct).sum =
      (Nat.choose 14 k.val : ℚ) := by decide +kernel
  exact h k

end GeometricUnity.D7Exterior
~~~

[Return to file index](#file-index)

## D7Hodge.lean {#source-d7hodge-lean}

Constructs the equivariant Hodge involution on the middle exterior power and its signed eigenspaces.

~~~lean
import D7Exterior
import Mathlib.Tactic.Module

/-!
# The middle exterior power of the split special orthogonal representation

An orthonormal basis for the complex bilinear form gives the Hodge operator
on the seventh exterior power. The determinant pairing proves equivariance
for the same action used in `D7Exterior`.
-/

namespace GeometricUnity.D7Hodge

open D7Exterior
open scoped BigOperators

noncomputable section

private theorem plus_index (i : Pair) : pairIndex (plusAxis i) = i := by
  apply Fin.ext
  change (2 * i.val) / 2 = i.val
  omega

private theorem minus_index (i : Pair) : pairIndex (minusAxis i) = i := by
  apply Fin.ext
  change (2 * i.val + 1) / 2 = i.val
  omega

private theorem axis_cases (j : Axis) : j = plusAxis (pairIndex j) ∨ j = minusAxis (pairIndex j) := by
  by_cases hj : j.val % 2 = 0
  · exact Or.inl (Fin.ext (by change j.val = 2 * (j.val / 2); omega))
  · exact Or.inr (Fin.ext (by change j.val = 2 * (j.val / 2) + 1; omega))

private def mix : Space →ₗ[ℂ] Space where
  toFun x j := if j.val % 2 = 0 then x j + Complex.I * x (minusAxis (pairIndex j))
    else (x (plusAxis (pairIndex j)) - Complex.I * x j) / 2
  map_add' x y := by
    funext j
    simp only [Pi.add_apply]
    split <;> ring
  map_smul' c x := by
    funext j
    simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]
    split <;> ring

private theorem mix_plus (x : Space) (i : Pair) :
    mix x (plusAxis i) = x (plusAxis i) + Complex.I * x (minusAxis i) := by
  have h : (plusAxis i).val % 2 = 0 := by change (2 * i.val) % 2 = 0; omega
  change (if _ then _ else _) = _
  simp [h, plus_index]

private theorem mix_minus (x : Space) (i : Pair) :
    mix x (minusAxis i) = (x (plusAxis i) - Complex.I * x (minusAxis i)) / 2 := by
  have h : (minusAxis i).val % 2 ≠ 0 := by change (2 * i.val + 1) % 2 ≠ 0; omega
  change (if _ then _ else _) = _
  simp [h, minus_index]

private theorem mix_injective : Function.Injective mix := by
  intro x y h
  have hp (i : Pair) := congrFun h (plusAxis i)
  have hm (i : Pair) := congrFun h (minusAxis i)
  simp only [mix_plus] at hp
  simp only [mix_minus] at hm
  funext j
  rcases axis_cases j with hj | hj
  · rw [hj]
    linear_combination (1 / 2 : ℂ) * hp (pairIndex j) + hm (pairIndex j)
  · rw [hj]
    linear_combination (-Complex.I / 2) * hp (pairIndex j) + Complex.I * hm (pairIndex j) +
      (x (minusAxis (pairIndex j)) - y (minusAxis (pairIndex j))) * Complex.I_mul_I

private def mixEquiv : Space ≃ₗ[ℂ] Space :=
  LinearEquiv.ofBijective mix ⟨mix_injective,
    LinearMap.injective_iff_surjective.mp mix_injective⟩

/-- Complex orthonormal coordinates for the bilinear form in the null basis. -/
def orthBasis : Module.Basis Axis ℂ Space := axisBasis.map mixEquiv

private def axesEquiv : Pair × Fin 2 ≃ Axis where
  toFun p := if p.2 = 0 then plusAxis p.1 else minusAxis p.1
  invFun j := (pairIndex j, ⟨j.val % 2, Nat.mod_lt _ (by decide)⟩)
  left_inv := by
    rintro ⟨i, a⟩
    fin_cases a
    · exact Prod.ext (plus_index i) (Fin.ext (by change (2 * i.val) % 2 = 0; omega))
    · exact Prod.ext (minus_index i) (Fin.ext (by change (2 * i.val + 1) % 2 = 1; omega))
  right_inv j := by
    change (if (⟨j.val % 2, _⟩ : Fin 2) = 0 then _ else _) = _
    by_cases h : j.val % 2 = 0
    · rw [if_pos (Fin.ext h)]
      apply Fin.ext; change 2 * (j.val / 2) = j.val; omega
    · rw [if_neg (fun e => h (congrArg Fin.val e))]
      apply Fin.ext; change 2 * (j.val / 2) + 1 = j.val; omega

private theorem sum_axes (f : Axis → ℂ) :
    ∑ j, f j = ∑ i : Pair, (f (plusAxis i) + f (minusAxis i)) := by
  rw [← axesEquiv.sum_comp f, Fintype.sum_prod_type]
  simp [Fin.sum_univ_two, axesEquiv]

private theorem splitForm_mix (x y : Space) : splitForm (mix x) (mix y) = ∑ j, x j * y j := by
  rw [sum_axes]
  apply Finset.sum_congr rfl
  intro i _
  change mix x (plusAxis i) * mix y (minusAxis i) +
    mix x (minusAxis i) * mix y (plusAxis i) = _
  rw [mix_plus, mix_minus, mix_plus, mix_minus]
  linear_combination -(x (minusAxis i) * y (minusAxis i)) * Complex.I_mul_I

abbrev Mid := ⋀[ℂ]^7 Space
abbrev MiddleIndex := Index 7

def middleBasis : Module.Basis MiddleIndex ℂ Mid := orthBasis.exteriorPower 7

def complement (s : MiddleIndex) : MiddleIndex :=
  ⟨s.valᶜ, by change (s.valᶜ).card = 7; simp [Finset.card_compl]⟩

theorem complement_complement (s : MiddleIndex) : complement (complement s) = s := by
  apply Subtype.ext
  exact compl_compl s.val

private theorem disjoint_complement (s : MiddleIndex) : Disjoint s.val (complement s).val :=
  disjoint_compl_right

private theorem disjoint_iff (s t : MiddleIndex) : Disjoint s.val t.val ↔ t = complement s := by
  constructor
  · intro h
    apply Subtype.ext
    apply Finset.eq_of_subset_of_card_le
    · intro i hi
      exact Finset.mem_compl.mpr (Finset.disjoint_left.mp h.symm hi)
    · exact Nat.le_of_eq ((complement s).prop.trans t.prop.symm)
  · rintro rfl
    exact disjoint_complement s

def volume : (⋀[ℂ]^14 Space) →ₗ[ℂ] ℂ :=
  exteriorPower.alternatingMapLinearEquiv orthBasis.det

private def wedge (x y : Mid) : ⋀[ℂ]^14 Space :=
  ⟨x.val * y.val, by
    change x.val * y.val ∈ (LinearMap.range (ExteriorAlgebra.ι ℂ : Space →ₗ[ℂ] _)) ^ (7 + 7)
    rw [pow_add]
    exact Submodule.mul_mem_mul x.prop y.prop⟩

private theorem wedge_pure (v w : Fin 7 → Space) :
    wedge (exteriorPower.ιMulti ℂ 7 v) (exteriorPower.ιMulti ℂ 7 w) =
      exteriorPower.ιMulti ℂ 14 (Fin.append v w) := by
  apply Subtype.ext
  exact ExteriorAlgebra.ιMulti_mul_ιMulti v w

/-- The coefficient of the positively oriented top wedge in a product of middle wedges. -/
def volumePair : Mid →ₗ[ℂ] Mid →ₗ[ℂ] ℂ :=
  LinearMap.mk₂ ℂ (fun x y => volume (wedge x y))
    (fun x₁ x₂ y => by rw [← map_add]; congr 1; apply Subtype.ext; exact add_mul _ _ _)
    (fun r x y => by rw [← map_smul]; congr 1; apply Subtype.ext; exact smul_mul_assoc _ _ _)
    (fun x y₁ y₂ => by rw [← map_add]; congr 1; apply Subtype.ext; exact mul_add _ _ _)
    (fun r x y => by rw [← map_smul]; congr 1; apply Subtype.ext; exact mul_smul_comm _ _ _)

theorem volumePair_pure (v w : Fin 7 → Space) :
    volumePair (exteriorPower.ιMulti ℂ 7 v) (exteriorPower.ιMulti ℂ 7 w) =
      orthBasis.det (Fin.append v w) := by
  change volume (wedge (exteriorPower.ιMulti ℂ 7 v) (exteriorPower.ιMulti ℂ 7 w)) = _
  rw [wedge_pure, volume, exteriorPower.alternatingMapLinearEquiv_apply_ιMulti]

private def blockSwap : Equiv.Perm Axis := finAddFlip (m := 7) (n := 7)

private theorem blockSwap_sign : blockSwap.sign = -1 := by
  decide +kernel

private theorem append_swap (v w : Fin 7 → Space) : Fin.append w v = Fin.append v w ∘ blockSwap := by
  funext j
  refine Fin.addCases ?_ ?_ j
  · intro i
    rw [Function.comp_apply, blockSwap, finAddFlip_apply_castAdd, Fin.append_left, Fin.append_right]
  · intro i
    rw [Function.comp_apply, blockSwap, finAddFlip_apply_natAdd, Fin.append_right, Fin.append_left]

private theorem ext_mid {W : Type*} [AddCommGroup W] [Module ℂ W] {f g : Mid →ₗ[ℂ] W}
    (h : ∀ v : Fin 7 → Space, f (exteriorPower.ιMulti ℂ 7 v) = g (exteriorPower.ιMulti ℂ 7 v)) :
    f = g := by
  apply exteriorPower.linearMap_ext
  ext v
  exact h v

private theorem ext_mid₂ {f g : Mid →ₗ[ℂ] Mid →ₗ[ℂ] ℂ}
    (h : ∀ v w : Fin 7 → Space,
      f (exteriorPower.ιMulti ℂ 7 v) (exteriorPower.ιMulti ℂ 7 w) =
      g (exteriorPower.ιMulti ℂ 7 v) (exteriorPower.ιMulti ℂ 7 w)) : f = g := by
  apply ext_mid
  intro v
  exact ext_mid (h v)

theorem volumePair_skew (x y : Mid) : volumePair y x = -volumePair x y := by
  have h : volumePair.flip = -volumePair := by
    apply ext_mid₂
    intro v w
    simp only [LinearMap.flip_apply, LinearMap.neg_apply, volumePair_pure]
    rw [append_swap, AlternatingMap.map_perm, blockSwap_sign]
    simp
  exact DFunLike.congr_fun (DFunLike.congr_fun h x) y

private theorem append_map (f : Space →ₗ[ℂ] Space) (v w : Fin 7 → Space) :
    Fin.append (f ∘ v) (f ∘ w) = f ∘ Fin.append v w := by
  funext j
  refine Fin.addCases ?_ ?_ j
  · intro i; rw [Function.comp_apply, Fin.append_left, Fin.append_left]; rfl
  · intro i; rw [Function.comp_apply, Fin.append_right, Fin.append_right]; rfl

theorem volumePair_invariant (g : splitSpecialOrthogonal) (x y : Mid) :
    volumePair (exteriorRepresentation 7 g x) (exteriorRepresentation 7 g y) = volumePair x y := by
  let A := exteriorRepresentation 7 g
  have h : ((volumePair.comp A).flip.comp A).flip = volumePair := by
    apply ext_mid₂
    intro v w
    change volumePair (exteriorPower.map 7 g.val (exteriorPower.ιMulti ℂ 7 v))
      (exteriorPower.map 7 g.val (exteriorPower.ιMulti ℂ 7 w)) = _
    rw [exteriorPower.map_apply_ιMulti, exteriorPower.map_apply_ιMulti, volumePair_pure,
      volumePair_pure, append_map, Module.Basis.det_comp, g.prop.1, one_mul]
  exact DFunLike.congr_fun (DFunLike.congr_fun h x) y

private def dotMetric : Space →ₗ[ℂ] Space →ₗ[ℂ] ℂ :=
  LinearMap.mk₂ ℂ (fun x y => ∑ j, x j * y j)
    (fun x₁ x₂ y => by simp [add_mul, Finset.sum_add_distrib])
    (fun r x y => by simp [smul_eq_mul, mul_assoc, Finset.mul_sum])
    (fun x y₁ y₂ => by simp [mul_add, Finset.sum_add_distrib])
    (fun r x y => by simp [smul_eq_mul, mul_left_comm, Finset.mul_sum])

def splitMetric : Space →ₗ[ℂ] Space →ₗ[ℂ] ℂ :=
  let f := mixEquiv.symm.toLinearMap
  ((dotMetric.comp f).flip.comp f).flip

theorem splitMetric_apply (x y : Space) : splitMetric x y = splitForm x y := by
  change (∑ j, (mixEquiv.symm x) j * (mixEquiv.symm y) j) = _
  rw [← splitForm_mix]
  change splitForm (mixEquiv (mixEquiv.symm x)) (mixEquiv (mixEquiv.symm y)) = _
  simp

theorem orthBasis_pair (i j : Axis) : splitForm (orthBasis i) (orthBasis j) = if i = j then 1 else 0 := by
  change splitForm (mix (axisBasis i)) (mix (axisBasis j)) = _
  rw [splitForm_mix, Finset.sum_eq_single i]
  · simp [axisBasis, Pi.basisFun_apply, Pi.single_apply]
  · intro l _ hl
    simp [axisBasis, Pi.basisFun_apply, hl]
  · simp

theorem preserves_splitForm_of_basis (f : Space →ₗ[ℂ] Space)
    (hb : ∀ i j, splitForm (f (orthBasis i)) (f (orthBasis j)) = splitForm (orthBasis i) (orthBasis j))
    (x y : Space) : splitForm (f x) (f y) = splitForm x y := by
  have h : ((splitMetric.comp f).flip.comp f).flip = splitMetric := by
    apply orthBasis.ext
    intro i
    apply orthBasis.ext
    intro j
    simp only [LinearMap.flip_apply, LinearMap.comp_apply, splitMetric_apply]
    exact hb i j
  simpa only [LinearMap.flip_apply, LinearMap.comp_apply, splitMetric_apply] using
    DFunLike.congr_fun (DFunLike.congr_fun h x) y

private theorem splitMetric_axis (i : Axis) : splitMetric (orthBasis i) = orthBasis.coord i := by
  apply orthBasis.ext
  intro j
  rw [splitMetric_apply, orthBasis_pair, Module.Basis.coord_apply, Module.Basis.repr_self,
    Finsupp.single_apply]
  simp [eq_comm]

/-- The determinant pairing induced by the split metric on exterior powers. -/
def exteriorMetric (n : ℕ) : (⋀[ℂ]^n Space) →ₗ[ℂ] (⋀[ℂ]^n Space) →ₗ[ℂ] ℂ :=
  (exteriorPower.pairingDual ℂ Space n).comp (exteriorPower.map n splitMetric)

abbrev metricPair : Mid →ₗ[ℂ] Mid →ₗ[ℂ] ℂ := exteriorMetric 7

theorem exteriorMetric_pure (n : ℕ) (u v : Fin n → Space) : exteriorMetric n
    (exteriorPower.ιMulti ℂ n u) (exteriorPower.ιMulti ℂ n v) =
      (Matrix.of fun i j => splitForm (u j) (v i)).det := by
  simp only [exteriorMetric, LinearMap.comp_apply, exteriorPower.map_apply_ιMulti,
    exteriorPower.pairingDual_ιMulti_ιMulti, Function.comp_apply, splitMetric_apply]

set_option maxRecDepth 4096 in
theorem exteriorMetric_axis (n : ℕ) (s : Index n) :
    exteriorMetric n (orthBasis.exteriorPower n s) = (orthBasis.exteriorPower n).coord s := by
  have h : splitMetric ∘ orthBasis = orthBasis.coord := funext splitMetric_axis
  calc
    exteriorMetric n (orthBasis.exteriorPower n s) = exteriorPower.ιMultiDual ℂ n orthBasis s := by
      simp only [exteriorMetric, LinearMap.comp_apply, exteriorPower.basis_apply,
        exteriorPower.map_apply_ιMulti_family, h, exteriorPower.ιMultiDual]
    _ = (orthBasis.exteriorPower n).coord s := (exteriorPower.basis_coord ℂ n orthBasis s).symm

private theorem metricPair_axis (s : MiddleIndex) : metricPair (middleBasis s) = middleBasis.coord s :=
  exteriorMetric_axis 7 s

theorem exteriorMetric_injective (n : ℕ) : Function.Injective (exteriorMetric n) := by
  let b := orthBasis.exteriorPower n
  have h (s : Index n) : (exteriorMetric n).flip (b s) = b.coord s := by
    apply b.ext
    intro t
    simp only [LinearMap.flip_apply, b, exteriorMetric_axis, Module.Basis.coord_apply,
      Module.Basis.repr_self, Finsupp.single_apply]
    simp [eq_comm]
  intro x y hxy
  apply b.repr.injective
  ext s
  change b.coord s x = b.coord s y
  rw [← h s]
  exact DFunLike.congr_fun hxy (b s)

private theorem metricPair_injective : Function.Injective metricPair := exteriorMetric_injective 7

theorem metricPair_invariant (g : splitSpecialOrthogonal) (x y : Mid) :
    metricPair (exteriorRepresentation 7 g x) (exteriorRepresentation 7 g y) = metricPair x y := by
  let A := exteriorRepresentation 7 g
  have h : ((metricPair.comp A).flip.comp A).flip = metricPair := by
    apply ext_mid₂
    intro v w
    change metricPair (exteriorPower.map 7 g.val (exteriorPower.ιMulti ℂ 7 v))
      (exteriorPower.map 7 g.val (exteriorPower.ιMulti ℂ 7 w)) = _
    simp only [metricPair, exteriorMetric, LinearMap.comp_apply, exteriorPower.map_apply_ιMulti,
      exteriorPower.pairingDual_ιMulti_ιMulti, Function.comp_apply, splitMetric_apply, g.prop.2]
  exact DFunLike.congr_fun (DFunLike.congr_fun h x) y

private def shuffleSign (s : MiddleIndex) : ℤˣ :=
  (Set.powersetCard.permOfDisjoint (disjoint_complement s)).sign

theorem volume_top (s : Index 14) : volume (exteriorPower.ιMulti_family ℂ 14 orthBasis s) = 1 := by
  have hs : s.val = Finset.univ := s.val.card_eq_iff_eq_univ.mp (by simp)
  have he : (Set.powersetCard.ofFinEmbEquiv.symm s : Axis ↪o Axis) = RelEmbedding.refl _ := by
    symm
    apply Finset.orderEmbOfFin_unique' s.prop
    rw [hs]
    intro i
    exact Finset.mem_univ _
  simp [volume, exteriorPower.ιMulti_family, he, Module.Basis.det_self]

private theorem wedge_complement (s : MiddleIndex) :
    wedge (middleBasis s) (middleBasis (complement s)) = shuffleSign s •
      exteriorPower.ιMulti_family ℂ 14 orthBasis (Set.powersetCard.disjUnion (disjoint_complement s)) := by
  apply Subtype.ext
  simpa only [wedge, middleBasis, exteriorPower.basis_apply, exteriorPower.ιMulti_family_apply_coe,
    Submodule.coe_smul_of_tower, shuffleSign]
    using ExteriorAlgebra.ιMulti_family_mul_of_disjoint ℂ orthBasis s (complement s) (disjoint_complement s)

private theorem volumePair_zero (s t : MiddleIndex) (h : t ≠ complement s) :
    volumePair (middleBasis s) (middleBasis t) = 0 := by
  have hz : wedge (middleBasis s) (middleBasis t) = 0 := by
    apply Subtype.ext
    simpa only [wedge, middleBasis, exteriorPower.basis_apply, exteriorPower.ιMulti_family_apply_coe,
      Submodule.coe_zero]
      using ExteriorAlgebra.ιMulti_family_mul_of_not_disjoint ℂ orthBasis s t (mt (disjoint_iff s t).mp h)
  change volume (wedge (middleBasis s) (middleBasis t)) = 0
  rw [hz, map_zero]

private def coefficient (s : MiddleIndex) : ℂ := volumePair (middleBasis s) (middleBasis (complement s))

private theorem coefficient_sq (s : MiddleIndex) : coefficient s * coefficient s = 1 := by
  change volume (wedge (middleBasis s) (middleBasis (complement s))) *
    volume (wedge (middleBasis s) (middleBasis (complement s))) = 1
  rw [wedge_complement]
  rcases Int.units_eq_one_or (shuffleSign s) with h | h
  · simp [h, volume_top]
  · simp [h, volume_top]

private theorem coefficient_complement (s : MiddleIndex) : coefficient (complement s) = -coefficient s := by
  simp only [coefficient, complement_complement, volumePair_skew (middleBasis s) (middleBasis (complement s))]

/-- Hodge star, with the chosen orthonormal volume. It squares to minus the identity. -/
def star : Mid →ₗ[ℂ] Mid :=
  middleBasis.constr ℂ fun s => coefficient s • middleBasis (complement s)

private theorem star_basis (s : MiddleIndex) : star (middleBasis s) = coefficient s • middleBasis (complement s) :=
  middleBasis.constr_basis _ _ _

theorem metric_star (x y : Mid) : metricPair (star x) y = volumePair x y := by
  have h : metricPair.comp star = volumePair := by
    apply middleBasis.ext
    intro s
    apply middleBasis.ext
    intro t
    simp only [LinearMap.comp_apply, star_basis, map_smul, LinearMap.smul_apply, metricPair_axis,
      Module.Basis.coord_apply, Module.Basis.repr_self, Finsupp.single_apply]
    by_cases he : t = complement s
    · subst t; simp [coefficient]
    · simp [he, volumePair_zero s t he]
  exact DFunLike.congr_fun (DFunLike.congr_fun h x) y

theorem star_square (x : Mid) : star (star x) = -x := by
  have h : star.comp star = -LinearMap.id := by
    apply middleBasis.ext
    intro s
    simp only [LinearMap.comp_apply, star_basis, map_smul, coefficient_complement,
      complement_complement, smul_smul, mul_neg, coefficient_sq, neg_one_smul, LinearMap.neg_apply,
      LinearMap.id_apply]
  exact DFunLike.congr_fun h x

theorem star_equivariant (g : splitSpecialOrthogonal) (x : Mid) :
    star (exteriorRepresentation 7 g x) = exteriorRepresentation 7 g (star x) := by
  apply metricPair_injective
  apply LinearMap.ext
  intro y
  let e := LinearMap.equivOfIsUnitDet (g.prop.1 ▸ isUnit_one : IsUnit g.val.det)
  have he : e.toLinearMap = g.val := LinearMap.coe_equivOfIsUnitDet _
  have hs : Function.Surjective (exteriorRepresentation 7 g) := by
    intro w
    refine ⟨exteriorPower.map 7 e.symm.toLinearMap w, ?_⟩
    change (exteriorPower.map 7 g.val).comp (exteriorPower.map 7 e.symm.toLinearMap) w = w
    rw [← exteriorPower.map_comp, ← he, LinearEquiv.comp_coe, LinearEquiv.symm_trans_self,
      LinearEquiv.refl_toLinearMap, exteriorPower.map_id, LinearMap.id_apply]
  obtain ⟨w, rfl⟩ := hs y
  rw [metric_star, volumePair_invariant, metricPair_invariant, metric_star]

def orthDiagonal (c : Axis → ℂ) : Space →ₗ[ℂ] Space :=
  orthBasis.constr ℂ fun j => c j • orthBasis j

theorem orthDiagonal_basis (c : Axis → ℂ) (j : Axis) :
    orthDiagonal c (orthBasis j) = c j • orthBasis j :=
  orthBasis.constr_basis _ _ _

theorem orthDiagonal_exterior (c : Axis → ℂ) (k : ℕ) (s : Index k) :
    exteriorPower.map k (orthDiagonal c) (orthBasis.exteriorPower k s) =
      (∏ j ∈ s.val, c j) • orthBasis.exteriorPower k s := by
  rw [exteriorPower.basis_apply, exteriorPower.map_apply_ιMulti_family]
  let e := s.val.orderIsoOfFin s.prop
  change exteriorPower.ιMulti ℂ k (fun j => orthDiagonal c (orthBasis (e j).val)) =
    (∏ j ∈ s.val, c j) • exteriorPower.ιMulti ℂ k (fun j => orthBasis (e j).val)
  simp only [orthDiagonal_basis, AlternatingMap.map_smul_univ]
  congr 1
  calc
    _ = ∏ j : s.val, c j.val := Fintype.prod_equiv e.toEquiv _ (fun j => c j.val) fun _ => rfl
    _ = _ := Finset.prod_coe_sort s.val c

/-- Reflection in the first orthonormal axis. -/
def vectorReflection : Space →ₗ[ℂ] Space := orthDiagonal fun j => if j = 0 then -1 else 1

theorem vectorReflection_square (x : Space) : vectorReflection (vectorReflection x) = x := by
  have h : vectorReflection.comp vectorReflection = LinearMap.id := by
    apply orthBasis.ext
    intro i
    simp only [LinearMap.comp_apply, vectorReflection, orthDiagonal_basis, map_smul, LinearMap.id_apply]
    by_cases hi : i = 0 <;> simp [hi]
  exact DFunLike.congr_fun h x

theorem vectorReflection_isometry (x y : Space) :
    splitForm (vectorReflection x) (vectorReflection y) = splitForm x y := by
  apply preserves_splitForm_of_basis
  intro i j
  simp only [vectorReflection, orthDiagonal_basis, ← splitMetric_apply,
    map_smul, LinearMap.smul_apply, smul_eq_mul]
  rw [splitMetric_apply, orthBasis_pair]
  by_cases h : i = j
  · subst j; by_cases hi : i = 0 <;> simp [hi]
  · simp [h]

def reflection : Mid →ₗ[ℂ] Mid := exteriorPower.map 7 vectorReflection

private theorem reflection_basis (s : MiddleIndex) : reflection (middleBasis s) =
    (if 0 ∈ s.val then (-1 : ℂ) else 1) • middleBasis s := by
  change exteriorPower.map 7 (orthDiagonal _) (orthBasis.exteriorPower 7 s) = _
  rw [orthDiagonal_exterior]
  congr 1
  by_cases h : (0 : Axis) ∈ s.val
  · rw [if_pos h, Finset.prod_eq_single 0]
    · simp
    · intro j _ hj; simp [hj]
    · exact fun h' => (h' h).elim
  · rw [if_neg h]
    apply Finset.prod_eq_one
    intro j hj
    have h' : j ≠ 0 := fun e => h (e ▸ hj)
    simp [h']

theorem reflection_square (x : Mid) : reflection (reflection x) = x := by
  have h : reflection.comp reflection = LinearMap.id := by
    apply middleBasis.ext
    intro s
    simp only [LinearMap.comp_apply, reflection_basis, map_smul, LinearMap.id_apply]
    by_cases hs : (0 : Axis) ∈ s.val <;> simp [hs, smul_smul]
  exact DFunLike.congr_fun h x

theorem star_reflection (x : Mid) : star (reflection x) = -reflection (star x) := by
  have h : star.comp reflection = -(reflection.comp star) := by
    apply middleBasis.ext
    intro s
    simp only [LinearMap.comp_apply, LinearMap.neg_apply, reflection_basis, map_smul, star_basis]
    by_cases h : (0 : Axis) ∈ s.val <;> simp [complement, h] <;> module
  exact DFunLike.congr_fun h x

/-- Normalizing the Hodge star makes its two eigenvalues `1` and `-1`. -/
def involution : Mid →ₗ[ℂ] Mid := Complex.I • star

theorem involution_square (x : Mid) : involution (involution x) = x := by
  simp [involution, LinearMap.smul_apply, smul_smul, Complex.I_mul_I, star_square]

theorem involution_equivariant (g : splitSpecialOrthogonal) (x : Mid) :
    involution (exteriorRepresentation 7 g x) = exteriorRepresentation 7 g (involution x) := by
  simp [involution, star_equivariant]

theorem involution_basis (s : MiddleIndex) :
    ∃ c : ℂ, c ≠ 0 ∧ involution (middleBasis s) = c • middleBasis (complement s) := by
  refine ⟨Complex.I * coefficient s, mul_ne_zero Complex.I_ne_zero ?_, ?_⟩
  · intro hc
    have h := coefficient_sq s
    rw [hc, zero_mul] at h
    exact zero_ne_one h
  · simp [involution, star_basis, smul_smul]

def involutionEigenspace {E : Type*} [AddCommGroup E] [Module ℂ E]
    (J : E →ₗ[ℂ] E) (a : ℂ) : Submodule ℂ E := LinearMap.ker (J - a • LinearMap.id)

theorem mem_involutionEigenspace {E : Type*} [AddCommGroup E] [Module ℂ E]
    (J : E →ₗ[ℂ] E) (a : ℂ) (x : E) : x ∈ involutionEigenspace J a ↔ J x = a • x := by
  simp [involutionEigenspace, LinearMap.mem_ker, sub_eq_zero]

abbrev sector (a : ℂ) : Submodule ℂ Mid := involutionEigenspace involution a

theorem mem_sector (a : ℂ) (x : Mid) : x ∈ sector a ↔ involution x = a • x := by
  exact mem_involutionEigenspace involution a x

theorem sector_invariant (a : ℂ) (g : splitSpecialOrthogonal) (x : Mid) (h : x ∈ sector a) :
    exteriorRepresentation 7 g x ∈ sector a := by
  rw [mem_sector] at h ⊢
  rw [involution_equivariant, h, map_smul]

theorem involution_eigenspaces_isCompl {E : Type*} [AddCommGroup E] [Module ℂ E]
    (J : E →ₗ[ℂ] E) (hJ : ∀ x, J (J x) = x) :
    IsCompl (involutionEigenspace J 1) (involutionEigenspace J (-1)) := by
  constructor
  · rw [Submodule.disjoint_def]
    intro x hx hy
    have hx' : J x = x := by simpa using (mem_involutionEigenspace J 1 x).mp hx
    have hy' : J x = -x := ((mem_involutionEigenspace J (-1) x).mp hy).trans (by module)
    have hv : (2 : ℂ) • x = 0 := by
      rw [two_smul]
      nth_rw 1 [hx'.symm.trans hy']
      exact neg_add_cancel x
    exact (smul_eq_zero.mp hv).resolve_left (by norm_num)
  · apply codisjoint_iff_le_sup.mpr
    intro x _
    rw [Submodule.mem_sup]
    refine ⟨(1 / 2 : ℂ) • (x + J x), ?_, (1 / 2 : ℂ) • (x - J x), ?_, ?_⟩
    · simp only [mem_involutionEigenspace, map_smul, map_add, hJ, one_smul]
      rw [add_comm (J x) x]
    · simp only [mem_involutionEigenspace, map_smul, map_sub, hJ]
      module
    · module

theorem middle_sectors_isCompl : IsCompl (sector 1) (sector (-1)) :=
  involution_eigenspaces_isCompl involution involution_square

private theorem reflection_sector (a : ℂ) (x : Mid) (h : x ∈ sector a) : reflection x ∈ sector (-a) := by
  rw [mem_sector] at h ⊢
  have he : involution (reflection x) = -reflection (involution x) := by
    simp [involution, star_reflection]
  rw [he, h, map_smul]
  module

private def sectorEquiv : sector 1 ≃ₗ[ℂ] sector (-1) where
  toFun x := ⟨reflection x.val, reflection_sector 1 x.val x.prop⟩
  invFun y := ⟨reflection y.val, by simpa using reflection_sector (-1) y.val y.prop⟩
  left_inv x := Subtype.ext (reflection_square x.val)
  right_inv y := Subtype.ext (reflection_square y.val)
  map_add' x y := Subtype.ext (reflection.map_add x.val y.val)
  map_smul' c x := Subtype.ext (reflection.map_smul c x.val)

/-- The degree-seven exterior representation is the direct sum of two invariant
subspaces of dimension 1716. -/
theorem middle_sector_dimensions :
    Module.finrank ℂ (sector 1) = 1716 ∧ Module.finrank ℂ (sector (-1)) = 1716 := by
  have h := Submodule.finrank_add_eq_of_isCompl middle_sectors_isCompl
  rw [exteriorPower.finrank_eq, Module.finrank_pi, Fintype.card_fin] at h
  have he := sectorEquiv.finrank_eq
  have hc : Nat.choose 14 7 = 3432 := by decide
  rw [hc] at h
  omega

private theorem axisBasis_coord (x : Space) (i : Axis) : axisBasis.coord i x = x i := by
  simp [axisBasis, Module.Basis.coord_apply, Pi.basisFun_repr]

private theorem axisBasis_value (j i : Axis) : axisBasis j i = if i = j then 1 else 0 := by
  simp [axisBasis, Pi.basisFun_apply, Pi.single_apply]

private theorem same_plus (i j : Pair) : plusAxis i = plusAxis j ↔ i = j :=
  ⟨fun h => by simpa only [plus_index] using congrArg pairIndex h, congrArg plusAxis⟩

private theorem same_minus (i j : Pair) : minusAxis i = minusAxis j ↔ i = j :=
  ⟨fun h => by simpa only [minus_index] using congrArg pairIndex h, congrArg minusAxis⟩

private theorem plus_diff_minus (i j : Pair) : plusAxis i ≠ minusAxis j := by
  intro h
  have e := congrArg Fin.val h
  change 2 * i.val = 2 * j.val + 1 at e
  omega

private theorem minus_diff_plus (i j : Pair) : minusAxis i ≠ plusAxis j :=
  Ne.symm (plus_diff_minus j i)

private theorem mix_det : mix.det = Complex.I := by
  let b := axisBasis.reindex (axesEquiv.symm.trans (Equiv.prodComm _ _))
  let A : Matrix (Fin 2) (Fin 2) ℂ := !![1, Complex.I; 1 / 2, -Complex.I / 2]
  have hA : LinearMap.toMatrix b b mix = Matrix.blockDiagonal (fun _ : Pair => A) := by
    ext ⟨a, i⟩ ⟨d, j⟩
    rw [LinearMap.toMatrix_apply, Matrix.blockDiagonal_apply]
    simp only [b, Module.Basis.reindex_apply, Module.Basis.repr_reindex_apply,
      Equiv.symm_trans_apply, Equiv.symm_symm, Equiv.prodComm_symm, Equiv.prodComm_apply]
    change axisBasis.coord (axesEquiv (i, a)) (mix (axisBasis (axesEquiv (j, d)))) = _
    rw [axisBasis_coord]
    fin_cases a <;> fin_cases d <;>
      simp [axesEquiv, mix_plus, mix_minus, axisBasis_value, same_plus, same_minus,
        plus_diff_minus, minus_diff_plus, A] <;>
      split <;> simp_all
  rw [← LinearMap.det_toMatrix b, hA, Matrix.det_blockDiagonal]
  have hc : A.det = -Complex.I := by
    rw [Matrix.det_fin_two]
    change 1 * (-Complex.I / 2) - Complex.I * (1 / 2) = -Complex.I
    ring
  rw [Finset.prod_const, Finset.card_univ, Fintype.card_fin, hc]
  calc
    (-Complex.I) ^ 7 = Complex.I * (Complex.I * Complex.I) ^ 3 * (-1) := by ring
    _ = Complex.I := by rw [Complex.I_mul_I]; ring

private theorem null_volume : orthBasis.det axisBasis = -Complex.I := by
  have hu : orthBasis.det (mix ∘ axisBasis) = 1 := Module.Basis.det_self orthBasis
  rw [Module.Basis.det_comp, mix_det] at hu
  linear_combination (-Complex.I) * hu + (orthBasis.det axisBasis) * Complex.I_mul_I

theorem splitMetric_null_plus (i : Pair) : splitMetric (axisBasis (plusAxis i)) = axisBasis.coord (minusAxis i) := by
  apply LinearMap.ext
  intro y
  rw [splitMetric_apply, axisBasis_coord]
  change (∑ j : Pair, (axisBasis (plusAxis i) (plusAxis j) * y (minusAxis j) +
    axisBasis (plusAxis i) (minusAxis j) * y (plusAxis j))) = _
  simp [axisBasis_value, same_plus, minus_diff_plus]

private theorem metric_minus (i : Pair) : splitMetric (axisBasis (minusAxis i)) = axisBasis.coord (plusAxis i) := by
  apply LinearMap.ext
  intro y
  rw [splitMetric_apply, axisBasis_coord]
  change (∑ j : Pair, (axisBasis (minusAxis i) (plusAxis j) * y (minusAxis j) +
    axisBasis (minusAxis i) (minusAxis j) * y (plusAxis j))) = _
  simp [axisBasis_value, same_minus, plus_diff_minus]

private def selected (minusLast : Bool) : MiddleIndex :=
  if minusLast then lastMinus else highestPlus (7 : Fin 15)

private def preferred (minusLast : Bool) (i : Pair) : Axis :=
  if minusLast && i == 6 then minusAxis i else plusAxis i

private theorem selected_order (minusLast : Bool) (i : Pair) :
    Set.powersetCard.ofFinEmbEquiv.symm (selected minusLast) i = preferred minusLast i := by
  have hmono : ∀ b : Bool, ∀ a d : Pair, a < d → preferred b a < preferred b d := by decide +kernel
  have hm : ∀ b : Bool, ∀ j : Pair, preferred b j ∈ (selected b).val := by decide +kernel
  let f := OrderEmbedding.ofStrictMono (preferred minusLast) (hmono minusLast)
  exact (congrArg (fun e : Pair ↪o Axis => e i)
    (Finset.orderEmbOfFin_unique' (selected minusLast).prop (f := f) (hm minusLast))).symm

private def opposite (minusLast : Bool) (i : Pair) : Axis :=
  if minusLast && i == 6 then plusAxis i else minusAxis i

private theorem opposite_order (minusLast : Bool) (i : Pair) :
    Set.powersetCard.ofFinEmbEquiv.symm (complement (selected minusLast)) i = opposite minusLast i := by
  have hmono : ∀ b : Bool, ∀ a d : Pair, a < d → opposite b a < opposite b d := by decide +kernel
  have hm : ∀ b : Bool, ∀ j : Pair, opposite b j ∈ (complement (selected b)).val := by decide +kernel
  let f := OrderEmbedding.ofStrictMono (opposite minusLast) (hmono minusLast)
  exact (congrArg (fun e : Pair ↪o Axis => e i)
    (Finset.orderEmbOfFin_unique' (complement (selected minusLast)).prop (f := f) (hm minusLast))).symm

private def nullShuffle (minusLast : Bool) : Equiv.Perm Axis :=
  Equiv.ofBijective (Fin.append (preferred minusLast) (opposite minusLast)) (by
    cases minusLast <;> constructor <;> intro j
    · revert j; decide +kernel
    · revert j; decide +kernel
    · revert j; decide +kernel
    · revert j; decide +kernel)

private theorem nullShuffle_sign (minusLast : Bool) :
    (nullShuffle minusLast).sign = if minusLast then 1 else -1 := by
  cases minusLast <;> decide +kernel

private abbrev nullBasis := axisBasis.exteriorPower 7

set_option maxRecDepth 4096 in
private theorem metric_selected (b : Bool) : metricPair (nullBasis (selected b)) =
    nullBasis.coord (complement (selected b)) := by
  calc
    _ = exteriorPower.ιMultiDual ℂ 7 axisBasis (complement (selected b)) := by
      simp only [metricPair, exteriorMetric, LinearMap.comp_apply, exteriorPower.basis_apply, exteriorPower.ιMultiDual,
        exteriorPower.ιMulti_family, exteriorPower.map_apply_ιMulti]
      congr 1
      congr 1
      funext j
      simp only [Function.comp_apply, selected_order, opposite_order, preferred, opposite]
      split <;> simp [splitMetric_null_plus, metric_minus]
    _ = _ := (exteriorPower.basis_coord ℂ 7 axisBasis _).symm

private theorem volume_selected_complement (b : Bool) :
    volumePair (nullBasis (selected b)) (nullBasis (complement (selected b))) =
      if b then -Complex.I else Complex.I := by
  simp only [exteriorPower.basis_apply, exteriorPower.ιMulti_family, volumePair_pure]
  have h : Fin.append (axisBasis ∘ Set.powersetCard.ofFinEmbEquiv.symm (selected b))
      (axisBasis ∘ Set.powersetCard.ofFinEmbEquiv.symm (complement (selected b))) =
      axisBasis ∘ nullShuffle b := by
    funext j
    refine Fin.addCases ?_ ?_ j
    · intro i
      rw [Fin.append_left, Function.comp_apply, selected_order]
      change _ = axisBasis (Fin.append (preferred b) (opposite b) (Fin.castAdd 7 i))
      rw [Fin.append_left]
    · intro i
      rw [Fin.append_right, Function.comp_apply, opposite_order]
      change _ = axisBasis (Fin.append (preferred b) (opposite b) (Fin.natAdd 7 i))
      rw [Fin.append_right]
  rw [h, AlternatingMap.map_perm, nullShuffle_sign, null_volume]
  cases b <;> simp

private theorem volume_selected (b : Bool) : volumePair (nullBasis (selected b)) =
    (if b then -Complex.I else Complex.I) • nullBasis.coord (complement (selected b)) := by
  apply nullBasis.ext
  intro t
  rw [LinearMap.smul_apply, smul_eq_mul, Module.Basis.coord_apply, Module.Basis.repr_self, Finsupp.single_apply]
  by_cases ht : t = complement (selected b)
  · subst t
    rw [if_pos rfl, mul_one, volume_selected_complement]
  · have hz : wedge (nullBasis (selected b)) (nullBasis t) = 0 := by
      apply Subtype.ext
      simpa only [wedge, exteriorPower.basis_apply, exteriorPower.ιMulti_family_apply_coe, Submodule.coe_zero]
        using ExteriorAlgebra.ιMulti_family_mul_of_not_disjoint ℂ axisBasis (selected b) t
          (mt (disjoint_iff (selected b) t).mp ht)
    change volume (wedge (nullBasis (selected b)) (nullBasis t)) = _
    rw [hz, map_zero, if_neg ht, mul_zero]

private theorem selected_star (b : Bool) : star (nullBasis (selected b)) =
    (if b then -Complex.I else Complex.I) • nullBasis (selected b) := by
  apply metricPair_injective
  apply LinearMap.ext
  intro y
  rw [metric_star, volume_selected, map_smul, metric_selected]

/-- The all-positive highest-weight wedge belongs to the negative Hodge sector
for the orientation and the involution `I • star` used here. -/
theorem highestPlus_mem_sector : nullBasis (highestPlus (7 : Fin 15)) ∈ sector (-1) := by
  rw [mem_sector]
  have h := selected_star false
  change star (nullBasis (highestPlus (7 : Fin 15))) =
    Complex.I • nullBasis (highestPlus (7 : Fin 15)) at h
  simp only [involution, LinearMap.smul_apply, h, smul_smul, Complex.I_mul_I]

/-- The sign-reversed highest-weight wedge belongs to the positive Hodge sector. -/
theorem lastMinus_mem_sector : nullBasis lastMinus ∈ sector 1 := by
  rw [mem_sector]
  have h := selected_star true
  change star (nullBasis lastMinus) = -Complex.I • nullBasis lastMinus at h
  simp only [involution, LinearMap.smul_apply, h, smul_smul, mul_neg, Complex.I_mul_I, neg_neg]

end
end GeometricUnity.D7Hodge
~~~

[Return to file index](#file-index)

## D7Irreducible.lean {#source-d7irreducible-lean}

Proves irreducibility of the non-middle exterior powers using signed coordinate actions.

~~~lean
import D7Hodge
import Mathlib.RepresentationTheory.Irreducible

/-!
# Irreducibility in the D₇ exterior powers

Double sign changes separate the orthonormal exterior basis up to
complementary index sets. Determinant-one signed permutations act
transitively on the index sets in each degree.
-/

namespace GeometricUnity.D7Irreducible

open D7Exterior D7Hodge
open scoped BigOperators

noncomputable section

abbrev Exterior (k : ℕ) := ⋀[ℂ]^k Space
abbrev basis (k : ℕ) := orthBasis.exteriorPower k

def signScalar {α : Type*} [DecidableEq α] [Fintype α] (σ : Equiv.Perm α) : ℂ :=
  σ.sign • (1 : ℂ)

private theorem signScalar_sq {α : Type*} [DecidableEq α] [Fintype α] (σ : Equiv.Perm α) :
    signScalar σ * signScalar σ = 1 := by
  rcases Int.units_eq_one_or σ.sign with h | h <;> simp [signScalar, h]

private theorem signScalar_ne_zero {α : Type*} [DecidableEq α] [Fintype α] (σ : Equiv.Perm α) :
    signScalar σ ≠ 0 := by
  intro h
  have hs := signScalar_sq σ
  rw [h, zero_mul] at hs
  exact zero_ne_one hs

private def monomial (σ : Equiv.Perm Axis) (c : Axis → ℂ) : Space →ₗ[ℂ] Space :=
  orthBasis.constr ℂ fun j => c j • orthBasis (σ j)

private theorem monomial_basis (σ : Equiv.Perm Axis) (c : Axis → ℂ) (j : Axis) :
    monomial σ c (orthBasis j) = c j • orthBasis (σ j) := orthBasis.constr_basis _ _ _

private theorem monomial_det (σ : Equiv.Perm Axis) (c : Axis → ℂ) :
    (monomial σ c).det = (∏ j, c j) * signScalar σ := by
  calc
    _ = orthBasis.det (monomial σ c ∘ orthBasis) := by
      rw [Module.Basis.det_comp, Module.Basis.det_self, mul_one]
    _ = (∏ j, c j) • orthBasis.det ((orthBasis : Axis → Space) ∘ σ) := by
      change orthBasis.det (fun j => monomial σ c (orthBasis j)) = _
      simp only [monomial_basis, AlternatingMap.map_smul_univ]
      rfl
    _ = _ := by rw [AlternatingMap.map_perm, Module.Basis.det_self]; rfl

private def specialMonomial (σ : Equiv.Perm Axis) (c : Axis → ℂ)
    (hsq : ∀ j, c j * c j = 1) (hdet : (∏ j, c j) * signScalar σ = 1) : splitSpecialOrthogonal := by
  refine ⟨monomial σ c, (monomial_det σ c).trans hdet, preserves_splitForm_of_basis _ ?_⟩
  intro i j
  have h := fun (v w : Space) => splitMetric_apply v w
  rw [monomial_basis, monomial_basis, ← h]
  simp only [map_smul, LinearMap.smul_apply, h, orthBasis_pair, σ.injective.eq_iff]
  by_cases he : i = j
  · subst j
    simpa [smul_eq_mul] using hsq i
  · simp [he]

def orientationCorrection (σ : Equiv.Perm Axis) (pivot j : Axis) : ℂ :=
  if j = pivot then signScalar σ else 1

theorem correction_sq (σ : Equiv.Perm Axis) (pivot j : Axis) :
    orientationCorrection σ pivot j * orientationCorrection σ pivot j = 1 := by
  by_cases h : j = pivot <;> simp [orientationCorrection, h, signScalar_sq]

def orientedPermAt (σ : Equiv.Perm Axis) (pivot : Axis) : splitSpecialOrthogonal := by
  refine specialMonomial σ (orientationCorrection σ pivot) (correction_sq σ pivot) ?_
  rw [Finset.prod_eq_single pivot]
  · simp [orientationCorrection, signScalar_sq]
  · intro j _ hj; simp [orientationCorrection, hj]
  · simp

theorem orientedPermAt_basis (σ : Equiv.Perm Axis) (pivot j : Axis) :
    (orientedPermAt σ pivot).val (orthBasis j) =
      orientationCorrection σ pivot j • orthBasis (σ j) := monomial_basis _ _ _

private abbrev orientedPerm (σ : Equiv.Perm Axis) := orientedPermAt σ 0

def permIndex (σ : Equiv.Perm Axis) {k : ℕ} (s : Index k) : Index k :=
  ⟨s.val.map σ.toEmbedding, by change (s.val.map σ.toEmbedding).card = k; simp⟩

theorem orientedPerm_exterior {k : ℕ} (σ : Equiv.Perm Axis) (pivot : Axis) (s : Index k) :
    ∃ a : ℂ, a ≠ 0 ∧ exteriorRepresentation k (orientedPermAt σ pivot) (basis k s) =
      a • basis k (permIndex σ s) := by
  let t := permIndex σ s
  let e := (s.val.orderIsoOfFin s.prop).toEquiv
  let d := (t.val.orderIsoOfFin t.prop).toEquiv
  let m : s.val ≃ t.val := Finset.equivMap (s := s.val) (f := σ.toEmbedding)
  let p : Equiv.Perm (Fin k) := (e.trans m).trans d.symm
  have hp (j : Fin k) : σ (e j).val = (d (p j)).val := by
    exact (congrArg Subtype.val (d.apply_symm_apply (m (e j)))).symm
  let c := orientationCorrection σ pivot
  refine ⟨(∏ j, c (e j).val) * signScalar p, mul_ne_zero ?_ (signScalar_ne_zero p), ?_⟩
  · apply Finset.prod_ne_zero_iff.mpr
    intro j _
    have h := correction_sq σ pivot (e j).val
    intro hzero
    rw [show orientationCorrection σ pivot (e j).val = 0 from hzero, zero_mul] at h
    exact zero_ne_one h
  change exteriorPower.map k (monomial σ c) (orthBasis.exteriorPower k s) = _ • orthBasis.exteriorPower k t
  rw [exteriorPower.basis_apply, exteriorPower.basis_apply]
  change exteriorPower.map k (monomial σ c) (exteriorPower.ιMulti ℂ k (fun j => orthBasis (e j).val)) =
    _ • exteriorPower.ιMulti ℂ k (fun j => orthBasis (d j).val)
  rw [exteriorPower.map_apply_ιMulti]
  change exteriorPower.ιMulti ℂ k (fun j => monomial σ c (orthBasis (e j).val)) = _
  simp_rw [monomial_basis, hp]
  have hw : (fun j => orthBasis (d (p j)).val) = (fun j => orthBasis (d j).val) ∘ p := rfl
  rw [AlternatingMap.map_smul_univ, hw, AlternatingMap.map_perm]
  rcases Int.units_eq_one_or p.sign with h | h <;> simp [signScalar, h]
  module

private theorem index_transitive {k : ℕ} (s t : Index k) : ∃ σ : Equiv.Perm Axis, permIndex σ s = t := by
  classical
  let e : s.val ≃ t.val := Finset.equivOfCardEq (s.prop.trans t.prop.symm)
  let e' : {j // j ∉ s.val} ≃ {j // j ∉ t.val} := Fintype.equivOfCardEq (by
    rw [Fintype.card_subtype_compl, Fintype.card_subtype_compl, Fintype.card_coe, Fintype.card_coe,
      s.prop, t.prop])
  let σ : Equiv.Perm Axis := ((Equiv.sumCompl (· ∈ s.val)).symm.trans (e.sumCongr e')).trans
    (Equiv.sumCompl (· ∈ t.val))
  have hσ (j : Axis) (hj : j ∈ s.val) : σ j = (e ⟨j, hj⟩).val := by
    change Equiv.sumCompl (· ∈ t.val) ((e.sumCongr e') ((Equiv.sumCompl (· ∈ s.val)).symm j)) = _
    rw [Equiv.sumCompl_symm_apply_pos ⟨j, hj⟩]
    rfl
  refine ⟨σ, Subtype.ext (Finset.eq_of_subset_of_card_le ?_ ?_)⟩
  · intro j hj
    obtain ⟨a, ha, rfl⟩ := Finset.mem_map.mp hj
    change σ a ∈ t.val
    rw [hσ a ha]
    exact (e ⟨a, ha⟩).prop
  · change t.val.card ≤ (s.val.map σ.toEmbedding).card
    rw [Finset.card_map, s.prop, t.prop]

private theorem basis_transitive {k : ℕ} (s t : Index k) :
    ∃ g : splitSpecialOrthogonal, ∃ a : ℂ, a ≠ 0 ∧
      exteriorRepresentation k g (basis k s) = a • basis k t := by
  obtain ⟨σ, hσ⟩ := index_transitive s t
  obtain ⟨a, ha, h⟩ := orientedPerm_exterior σ 0 s
  exact ⟨orientedPerm σ, a, ha, h.trans (by rw [hσ])⟩

def axisFlip (i j : Axis) : ℂ := if j = i then -1 else 1

def subsetFlip (s : Finset Axis) (i : Axis) : ℂ := if i ∈ s then -1 else 1

private theorem prod_axisFlip (s : Finset Axis) (i : Axis) : ∏ j ∈ s, axisFlip i j = subsetFlip s i := by
  by_cases hi : i ∈ s
  · rw [Finset.prod_eq_single i]
    · simp [axisFlip, subsetFlip, hi]
    · intro j _ h; simp [axisFlip, h]
    · exact fun h => (h hi).elim
  · rw [subsetFlip, if_neg hi]
    apply Finset.prod_eq_one
    intro j hj
    simp [axisFlip, show j ≠ i from fun h => hi (h ▸ hj)]

def doubleFlip (i j : Axis) : splitSpecialOrthogonal := by
  let c := fun a => axisFlip i a * axisFlip j a
  refine specialMonomial 1 c ?_ ?_
  · intro a
    have hs (b : Axis) : axisFlip b a * axisFlip b a = 1 := by
      by_cases h : a = b <;> simp [axisFlip, h]
    change (axisFlip i a * axisFlip j a) * (axisFlip i a * axisFlip j a) = 1
    rw [mul_mul_mul_comm, hs i, hs j, mul_one]
  · simp [c, Finset.prod_mul_distrib, prod_axisFlip, subsetFlip, signScalar]

theorem doubleFlip_basis (i j a : Axis) : (doubleFlip i j).val (orthBasis a) =
    (axisFlip i a * axisFlip j a) • orthBasis a := monomial_basis _ _ _

def character (s : Finset Axis) (i j : Axis) : ℂ := subsetFlip s i * subsetFlip s j

private theorem character_sq (s : Finset Axis) (i j : Axis) : character s i j * character s i j = 1 := by
  by_cases hi : i ∈ s <;> by_cases hj : j ∈ s <;> simp [character, subsetFlip, hi, hj]

theorem doubleFlip_exterior {k : ℕ} (i j : Axis) (s : Index k) :
    exteriorRepresentation k (doubleFlip i j) (basis k s) = character s.val i j • basis k s := by
  let c := fun a => axisFlip i a * axisFlip j a
  have h : (doubleFlip i j).val = orthDiagonal c := by
    apply orthBasis.ext
    intro a
    change monomial 1 c (orthBasis a) = orthDiagonal c (orthBasis a)
    rw [monomial_basis, orthDiagonal_basis]
    rfl
  change exteriorPower.map k (doubleFlip i j).val (basis k s) = _
  rw [h, orthDiagonal_exterior]
  simp only [c, Finset.prod_mul_distrib, prod_axisFlip, character]

private theorem character_separates (s t : Finset Axis) (hne : t ≠ s) (hnc : t ≠ sᶜ) :
    ∃ i j : Axis, character t i j = -character s i j := by
  classical
  have h₁ : ∃ i : Axis, ¬ (i ∈ t ↔ i ∈ s) := by
    by_contra! h
    exact hne (Finset.ext h)
  have h₂ : ∃ j : Axis, j ∈ t ↔ j ∈ s := by
    by_contra! h
    apply hnc
    ext j
    have hl := h j
    by_cases hm : j ∈ s <;> simp_all
  obtain ⟨i, hi⟩ := h₁
  obtain ⟨j, hj⟩ := h₂
  refine ⟨i, j, ?_⟩
  by_cases his : i ∈ s <;> by_cases hit : i ∈ t <;> by_cases hjs : j ∈ s <;>
    simp_all [character, subsetFlip]

/-- Stability under the actual split special orthogonal exterior representation. -/
def Stable {k : ℕ} (W : Submodule ℂ (Exterior k)) : Prop :=
  ∀ (g : splitSpecialOrthogonal) (x : Exterior k), x ∈ W → exteriorRepresentation k g x ∈ W

private theorem diagonal_coordinate {E ι : Type*} [AddCommGroup E] [Module ℂ E]
    (b : Module.Basis ι ℂ E) (f : E →ₗ[ℂ] E) (d : ι → ℂ) (hf : ∀ s, f (b s) = d s • b s)
    (x : E) (t : ι) : b.repr (f x) t = d t * b.repr x t := by
  classical
  let c := b.coord t
  have h : c.comp f = d t • c := by
    apply b.ext
    intro s
    simp only [LinearMap.comp_apply, hf, map_smul, LinearMap.smul_apply,
      c, Module.Basis.coord_apply, Module.Basis.repr_self, Finsupp.single_apply]
    by_cases h : t = s <;> simp [h, eq_comm, smul_eq_mul]
  exact DFunLike.congr_fun h x

private theorem coordinate_ne_zero {E ι : Type*} [AddCommGroup E] [Module ℂ E]
    (b : Module.Basis ι ℂ E) (x : E) (hx : x ≠ 0) : ∃ s : ι, b.repr x s ≠ 0 := by
  classical
  by_contra! h
  apply hx
  apply b.repr.injective
  ext s
  simpa using h s

/-- Coordinate sign changes separate subsets up to complement. A minimum-support
vector in a nonzero invariant subspace occupies one such block. -/
theorem support_sign_block {E ι : Type*} [AddCommGroup E] [Module ℂ E]
    (b : Module.Basis ι ℂ E) (weight : ι → Finset Axis) (f : Axis → Axis → E →ₗ[ℂ] E)
    (hf : ∀ i j s, f i j (b s) = character (weight s) i j • b s)
    (W : Submodule ℂ E) (hW : ∀ i j x, x ∈ W → f i j x ∈ W) (hne : W ≠ ⊥) :
    ∃ (x : E) (s : ι), x ∈ W ∧ b.repr x s ≠ 0 ∧
      ∀ t : ι, b.repr x t ≠ 0 → weight t = weight s ∨ weight t = (weight s)ᶜ := by
  classical
  let P (n : ℕ) : Prop := ∃ x ∈ W, x ≠ 0 ∧ (b.repr x).support.card = n
  obtain ⟨v, hv, hv0⟩ := Submodule.exists_mem_ne_zero_of_ne_bot hne
  have hex : ∃ n, P n := ⟨_, v, hv, hv0, rfl⟩
  obtain ⟨x, hx, hx0, hcard⟩ := Nat.find_spec hex
  obtain ⟨s, hs⟩ := coordinate_ne_zero b x hx0
  refine ⟨x, s, hx, hs, ?_⟩
  intro t ht
  by_contra! hst
  obtain ⟨i, j, hsep⟩ := character_separates (weight s) (weight t) hst.1 hst.2
  let a := character (weight s) i j
  let y := x + a • f i j x
  have hy : y ∈ W := W.add_mem hx (W.smul_mem a (hW _ _ _ hx))
  have hrepr (q : ι) : b.repr y q =
      (1 + a * character (weight q) i j) * b.repr x q := by
    simp only [y, map_add, map_smul, Finsupp.add_apply, Finsupp.smul_apply, smul_eq_mul,
      diagonal_coordinate b (f i j) (fun s => character (weight s) i j) (hf i j)]
    ring
  have hys : b.repr y s ≠ 0 := by
    rw [hrepr, show a * character (weight s) i j = 1 from character_sq (weight s) i j]
    exact mul_ne_zero (by norm_num) hs
  have hyt : b.repr y t = 0 := by
    rw [hrepr, hsep, mul_neg, show a * character (weight s) i j = 1 from character_sq (weight s) i j]
    ring
  have hy0 : y ≠ 0 := fun hy' => hys (by simp [hy'])
  have hsub : (b.repr y).support ⊂ (b.repr x).support := by
    apply Finset.ssubset_iff_subset_ne.mpr
    refine ⟨?_, ?_⟩
    · intro q hq
      rw [Finsupp.mem_support_iff, hrepr] at hq
      rw [Finsupp.mem_support_iff]
      exact (mul_ne_zero_iff.mp hq).2
    · intro he
      exact (Finsupp.mem_support_iff.not.mpr (not_not_intro hyt))
        (he.symm ▸ Finsupp.mem_support_iff.mpr ht)
  have hle := Nat.find_min' hex (show P (b.repr y).support.card from ⟨y, hy, hy0, rfl⟩)
  exact (not_lt_of_ge hle) (hcard ▸ Finset.card_lt_card hsub)

private theorem support_block {k : ℕ} (W : Submodule ℂ (Exterior k)) (hW : Stable W) (hne : W ≠ ⊥) :
    ∃ (x : Exterior k) (s : Index k), x ∈ W ∧ (basis k).repr x s ≠ 0 ∧
      ∀ t : Index k, (basis k).repr x t ≠ 0 → t = s ∨ t.val = s.valᶜ := by
  obtain ⟨x, s, hx, hs, hblock⟩ := support_sign_block (basis k) Subtype.val
    (fun i j => exteriorRepresentation k (doubleFlip i j)) doubleFlip_exterior W (fun i j => hW (doubleFlip i j)) hne
  exact ⟨x, s, hx, hs, fun t ht => (hblock t ht).imp Subtype.ext id⟩

theorem basis_mem_of_scaled {E : Type*} [AddCommGroup E] [Module ℂ E] (W : Submodule ℂ E) (x : E)
    (a : ℂ) (ha : a ≠ 0) (hx : a • x ∈ W) : x ∈ W := by
  have h := W.smul_mem a⁻¹ hx
  rwa [smul_smul, inv_mul_cancel₀ ha, one_smul] at h

/-- In every degree other than seven the exterior action admits only the zero
and whole invariant subspaces. -/
theorem exterior_irreducible (k : ℕ) (hk : k ≠ 7) (W : Submodule ℂ (Exterior k))
    (hW : Stable W) : W = ⊥ ∨ W = ⊤ := by
  classical
  by_cases hne : W = ⊥
  · exact Or.inl hne
  right
  obtain ⟨x, s, hx, hs, hblock⟩ := support_block W hW hne
  have hsupp (t : Index k) (ht : (basis k).repr x t ≠ 0) : t = s := by
    rcases hblock t ht with h | h
    · exact h
    · have hc := congrArg Finset.card h
      rw [t.prop, Finset.card_compl, Fintype.card_fin, s.prop] at hc
      exact (hk (by omega)).elim
  have he : x = (basis k).repr x s • basis k s := by
    apply (basis k).repr.injective
    ext t
    simp only [map_smul, Finsupp.smul_apply, Module.Basis.repr_self, Finsupp.single_apply]
    by_cases h : t = s
    · subst t; simp
    · have hz : (basis k).repr x t = 0 := by by_contra hh; exact h (hsupp _ hh)
      simp [hz, Ne.symm h]
  have hbs : basis k s ∈ W := basis_mem_of_scaled W _ _ hs (he ▸ hx)
  apply top_unique
  rw [← (basis k).span_eq]
  apply Submodule.span_le.mpr
  rintro _ ⟨t, rfl⟩
  obtain ⟨g, a, ha, h⟩ := basis_transitive s t
  exact basis_mem_of_scaled W _ _ ha (h ▸ hW g _ hbs)

private theorem complement_ne (s : MiddleIndex) : complement s ≠ s := by
  intro h
  have he : (0 : Axis) ∈ (complement s).val ↔ (0 : Axis) ∈ s.val := by rw [h]
  change (0 : Axis) ∈ s.valᶜ ↔ (0 : Axis) ∈ s.val at he
  by_cases h' : (0 : Axis) ∈ s.val <;> simp_all

private theorem middle_block_expansion (x : Mid) (s : MiddleIndex)
    (hblock : ∀ t : MiddleIndex, middleBasis.repr x t ≠ 0 → t = s ∨ t.val = s.valᶜ) :
    x = middleBasis.repr x s • middleBasis s +
      middleBasis.repr x (complement s) • middleBasis (complement s) := by
  classical
  apply middleBasis.repr.injective
  ext t
  by_cases h₁ : t = s
  · subst t
    simp [Module.Basis.repr_self, Ne.symm (complement_ne s)]
  · by_cases h₂ : t = complement s
    · subst t
      simp [Module.Basis.repr_self, complement_ne s]
    · have hz : middleBasis.repr x t = 0 := by
        by_contra hh
        exact (hblock t hh).elim h₁ fun hv => h₂ (Subtype.ext hv)
      simp [Module.Basis.repr_self, h₁, h₂, hz]

private def sectorMap (a : ℂ) : Mid →ₗ[ℂ] Mid := LinearMap.id + a • involution

private theorem sectorMap_self (a : ℂ) (ha : a * a = 1) (x : Mid) (hx : x ∈ sector a) :
    sectorMap a x = (2 : ℂ) • x := by
  change x + a • involution x = _
  rw [(mem_sector a x).mp hx, smul_smul, ha, one_smul, two_smul]

private theorem sectorMap_comp (a : ℂ) (ha : a * a = 1) (x : Mid) :
    sectorMap a (involution x) = a • sectorMap a x := by
  change involution x + a • involution (involution x) = a • (x + a • involution x)
  rw [involution_square, smul_add, smul_smul, ha, one_smul, add_comm]

private theorem sectorMap_equivariant (a : ℂ) (g : splitSpecialOrthogonal) (x : Mid) :
    exteriorRepresentation 7 g (sectorMap a x) = sectorMap a (exteriorRepresentation 7 g x) := by
  change exteriorRepresentation 7 g (x + a • involution x) = _ + a • involution _
  rw [map_add, map_smul, involution_equivariant, LinearMap.id_apply]

/-- Each middle Hodge eigenspace is irreducible under the same split action. -/
theorem middle_sector_irreducible (a : ℂ) (ha : a * a = 1) (W : Submodule ℂ Mid)
    (hW : Stable W) (hsub : W ≤ sector a) : W = ⊥ ∨ W = sector a := by
  classical
  by_cases hne : W = ⊥
  · exact Or.inl hne
  right
  obtain ⟨x, s, hx, hs, hblock⟩ := support_block W hW hne
  have h2x : sectorMap a x ∈ W := by rw [sectorMap_self a ha x (hsub hx)]; exact W.smul_mem _ hx
  have hx0 : x ≠ 0 := fun e => hs (by simp [e])
  obtain ⟨c, hc, hcs⟩ := involution_basis s
  have hm : sectorMap a (middleBasis (complement s)) = (c⁻¹ * a) • sectorMap a (middleBasis s) := by
    have he := sectorMap_comp a ha (middleBasis s)
    rw [hcs, map_smul] at he
    calc
      _ = c⁻¹ • (c • sectorMap a (middleBasis (complement s))) := by
        rw [smul_smul, inv_mul_cancel₀ hc, one_smul]
      _ = _ := by rw [he, smul_smul]
  let r := middleBasis.repr x s + middleBasis.repr x (complement s) * (c⁻¹ * a)
  have hr : sectorMap a x = r • sectorMap a (middleBasis s) := by
    conv_lhs => rw [middle_block_expansion x s hblock]
    rw [map_add, map_smul, map_smul, hm, smul_smul, ← add_smul]
  have hr0 : r ≠ 0 := by
    intro hz
    rw [hz, zero_smul, sectorMap_self a ha x (hsub hx)] at hr
    exact hx0 ((smul_eq_zero.mp hr).resolve_left (by norm_num))
  have hb : sectorMap a (middleBasis s) ∈ W := basis_mem_of_scaled W _ _ hr0 (hr ▸ h2x)
  have hall (t : MiddleIndex) : sectorMap a (middleBasis t) ∈ W := by
    obtain ⟨g, b, hb0, he⟩ := basis_transitive s t
    change exteriorRepresentation 7 g (middleBasis s) = b • middleBasis t at he
    have hf := hW g _ hb
    rw [sectorMap_equivariant, he, map_smul] at hf
    exact basis_mem_of_scaled W _ _ hb0 hf
  apply le_antisymm hsub
  intro y hy
  have hp : sectorMap a y ∈ W := by
    rw [← middleBasis.sum_repr y, map_sum]
    exact W.sum_mem fun t _ => by rw [map_smul]; exact W.smul_mem _ (hall t)
  rw [sectorMap_self a ha y hy] at hp
  exact basis_mem_of_scaled W _ _ (by norm_num : (2 : ℂ) ≠ 0) hp

theorem irreducible_of_subrepresentations {V : Type*} [AddCommGroup V] [Module ℂ V]
    [Nontrivial V] (ρ : Representation ℂ splitSpecialOrthogonal V)
    (h : ∀ U : Subrepresentation ρ, U = ⊥ ∨ U = ⊤) : ρ.IsIrreducible := by
  refine { toNontrivial := ⟨?_⟩, eq_bot_or_eq_top := h }
  refine ⟨⊥, ⊤, ?_⟩
  intro e
  obtain ⟨x, hx⟩ := exists_ne (0 : V)
  have hz : x ∈ (⊥ : Subrepresentation ρ).toSubmodule := by
    rw [e]
    exact Submodule.mem_top
  change x ∈ (⊥ : Submodule ℂ V) at hz
  rw [Submodule.mem_bot] at hz
  exact hx hz

/-- Mathlib's irreducibility predicate for each non-middle exterior power in dimension 14. -/
theorem exterior_isIrreducible (k : Fin 15) (hk : k.val ≠ 7) :
    (exteriorRepresentation k.val).IsIrreducible := by
  have : Nontrivial (Exterior k.val) :=
    ⟨⟨axisBasis.exteriorPower k.val (highestPlus k), 0, highestPlus_ne_zero k⟩⟩
  apply irreducible_of_subrepresentations
  intro U
  have h := exterior_irreducible k.val hk U.toSubmodule (fun g x hx => U.apply_mem_toSubmodule g (v := x) hx)
  exact h.imp (fun e => Subrepresentation.toSubmodule_injective e)
    (fun e => Subrepresentation.toSubmodule_injective e)

/-- The exterior action restricted to a middle Hodge eigenspace. -/
def sectorRepresentation (a : ℂ) : Representation ℂ splitSpecialOrthogonal (sector a) :=
  (exteriorRepresentation 7).subrepresentation (sector a) (fun g x hx => sector_invariant a g x hx)

/-- Both invariant middle Hodge eigenspaces satisfy Mathlib's irreducibility predicate. -/
theorem middle_isIrreducible (a : ℂ) (ha : a = 1 ∨ a = -1) :
    Representation.IsIrreducible (k := ℂ) (V := ↥(sector a)) (sectorRepresentation a) := by
  have hd : Module.finrank ℂ (sector a) = 1716 := by
    rcases ha with h | h
    · rw [h]; exact middle_sector_dimensions.1
    · rw [h]; exact middle_sector_dimensions.2
  have : Nontrivial (sector a) := Module.nontrivial_of_finrank_pos (by rw [hd]; decide)
  have ha' : a * a = 1 := by rcases ha with rfl | rfl <;> simp
  apply irreducible_of_subrepresentations
  intro U
  let W : Submodule ℂ Mid := U.toSubmodule.map (sector a).subtype
  have hW : Stable W := by
    intro g x hx
    obtain ⟨y, hy, rfl⟩ := Submodule.mem_map.mp hx
    exact Submodule.mem_map.mpr ⟨sectorRepresentation a g y, U.apply_mem_toSubmodule g hy, rfl⟩
  have hle : W ≤ sector a := by
    intro x hx
    obtain ⟨y, _, rfl⟩ := Submodule.mem_map.mp hx
    exact y.prop
  rcases middle_sector_irreducible a ha' W hW hle with h | h
  · left
    apply Subrepresentation.toSubmodule_injective
    apply Submodule.map_injective_of_injective (sector a).subtype_injective
    change W = (⊥ : Submodule ℂ (sector a)).map (sector a).subtype
    rw [Submodule.map_bot, h]
  · right
    apply Subrepresentation.toSubmodule_injective
    apply Submodule.map_injective_of_injective (sector a).subtype_injective
    change W = (⊤ : Submodule ℂ (sector a)).map (sector a).subtype
    rw [Submodule.map_top, Submodule.range_subtype, h]

/-- The subspace generated by the orbit of a vector in an exterior power. -/
def orbitSpan {k : ℕ} (x : Exterior k) : Submodule ℂ (Exterior k) :=
  Submodule.span ℂ (Set.range fun g => exteriorRepresentation k g x)

theorem orbitSpan_stable {k : ℕ} (x : Exterior k) : Stable (orbitSpan x) := by
  intro g y hy
  have hle : orbitSpan x ≤ (orbitSpan x).comap (exteriorRepresentation k g) := by
    apply Submodule.span_le.mpr
    rintro _ ⟨h, rfl⟩
    exact Submodule.subset_span ⟨g * h, by
      change exteriorRepresentation k (g * h) x = exteriorRepresentation k g (exteriorRepresentation k h x)
      rw [map_mul]
      rfl⟩
  exact hle hy

private theorem mem_orbitSpan {k : ℕ} (x : Exterior k) : x ∈ orbitSpan x :=
  Submodule.subset_span ⟨1, by
    change exteriorRepresentation k 1 x = x
    rw [map_one]
    rfl⟩

/-- The null-basis highest-weight wedge generates the full exterior power
in every non-middle degree. -/
theorem highestPlus_generates (k : Fin 15) (hk : k.val ≠ 7) :
    orbitSpan (axisBasis.exteriorPower k.val (highestPlus k)) = ⊤ := by
  let x := axisBasis.exteriorPower k.val (highestPlus k)
  have hx : orbitSpan x ≠ ⊥ := by
    intro h
    have hv := mem_orbitSpan x
    rw [h, Submodule.mem_bot] at hv
    exact highestPlus_ne_zero k hv
  exact (exterior_irreducible k.val hk (orbitSpan x) (orbitSpan_stable x)).resolve_left hx

private theorem orbitSpan_eq_sector (a : ℂ) (ha : a * a = 1) (x : Mid)
    (hx : x ≠ 0) (hmem : x ∈ sector a) : orbitSpan x = sector a := by
  have hle : orbitSpan x ≤ sector a := by
    apply Submodule.span_le.mpr
    rintro _ ⟨g, rfl⟩
    exact sector_invariant a g x hmem
  apply (middle_sector_irreducible a ha _ (orbitSpan_stable x) hle).resolve_left
  intro h
  have hv := mem_orbitSpan x
  rw [h, Submodule.mem_bot] at hv
  exact hx hv

/-- The degree-seven wedge of weight `μ₇⁺` generates the negative Hodge sector. -/
theorem middlePlus_generates :
    orbitSpan (axisBasis.exteriorPower 7 (highestPlus (7 : Fin 15))) = sector (-1) :=
  orbitSpan_eq_sector (-1) (by norm_num) _ (highestPlus_ne_zero (7 : Fin 15)) highestPlus_mem_sector

/-- The degree-seven wedge of weight `μ₇⁻` generates the positive Hodge sector. -/
theorem middleMinus_generates : orbitSpan (axisBasis.exteriorPower 7 lastMinus) = sector 1 :=
  orbitSpan_eq_sector 1 (by norm_num) _ lastMinus_ne_zero lastMinus_mem_sector

end
end GeometricUnity.D7Irreducible
~~~

[Return to file index](#file-index)

## D7VectorTensor.lean {#source-d7vectortensor-lean}

Constructs alternation, trace, and their sections and splits the vector times two-form representation into three channels.

~~~lean
import D7Hodge
import Mathlib.LinearAlgebra.Contraction
import Mathlib.RepresentationTheory.Intertwining

/-!
# Alternation and trace on the vector times two-form representation

The joint kernel is the traceless hook. The two projections and their
sections are formed using the exterior algebra and the same split form as
the exterior-power representation.
-/

namespace GeometricUnity.D7VectorTensor

open D7Exterior D7Hodge TensorProduct
open scoped BigOperators TensorProduct

noncomputable section

abbrev Two := ⋀[ℂ]^2 Space
abbrev Three := ⋀[ℂ]^3 Space
abbrev VTwo := Space ⊗[ℂ] Two

def vectorAction : Representation ℂ splitSpecialOrthogonal Space where
  toFun g := g.val
  map_one' := rfl
  map_mul' _ _ := rfl

def tensorAction : Representation ℂ splitSpecialOrthogonal VTwo :=
  vectorAction.tprod (exteriorRepresentation 2)

def wedgeTwo (x y : Space) : Two := exteriorPower.ιMulti ℂ 2 ![x, y]

def wedgeThree (x y z : Space) : Three := exteriorPower.ιMulti ℂ 3 ![x, y, z]

private theorem coe_wedgeTwo (x y : Space) : (wedgeTwo x y : ExteriorAlgebra ℂ Space) =
    ExteriorAlgebra.ι ℂ x * ExteriorAlgebra.ι ℂ y := by
  simp [wedgeTwo, ExteriorAlgebra.ιMulti_apply]

private theorem coe_wedgeThree (x y z : Space) : (wedgeThree x y z : ExteriorAlgebra ℂ Space) =
    ExteriorAlgebra.ι ℂ x * (ExteriorAlgebra.ι ℂ y * ExteriorAlgebra.ι ℂ z) := by
  simp [wedgeThree, ExteriorAlgebra.ιMulti_apply]

theorem wedgeTwo_self (x : Space) : wedgeTwo x x = 0 := by
  apply Subtype.ext
  rw [coe_wedgeTwo, Submodule.coe_zero, ExteriorAlgebra.ι_sq_zero]

theorem wedgeTwo_swap (x y : Space) : wedgeTwo y x = -wedgeTwo x y := by
  apply Subtype.ext
  simp only [Submodule.coe_neg, coe_wedgeTwo]
  exact eq_neg_of_add_eq_zero_left (ExteriorAlgebra.ι_add_mul_swap (R := ℂ) y x)

private def wedgeLeft (n : ℕ) (x : Space) (u : ⋀[ℂ]^n Space) : ⋀[ℂ]^(n + 1) Space :=
  ⟨ExteriorAlgebra.ι ℂ x * u.val, by
    change _ ∈ (LinearMap.range (ExteriorAlgebra.ι ℂ : Space →ₗ[ℂ] _)) ^ (n + 1)
    rw [Nat.add_comm n 1, pow_add, pow_one]
    exact Submodule.mul_mem_mul (LinearMap.mem_range_self _ x) u.prop⟩

def wedgeLeftLinear (n : ℕ) : Space →ₗ[ℂ] (⋀[ℂ]^n Space) →ₗ[ℂ] (⋀[ℂ]^(n + 1) Space) :=
  LinearMap.mk₂ ℂ (wedgeLeft n)
    (fun x y u => by apply Subtype.ext; change ExteriorAlgebra.ι ℂ (x + y) * u.val = _; rw [map_add]; exact add_mul _ _ _)
    (fun r x u => by apply Subtype.ext; change ExteriorAlgebra.ι ℂ (r • x) * u.val = _; rw [map_smul]; exact smul_mul_assoc _ _ _)
    (fun x u v => by apply Subtype.ext; exact mul_add _ _ _)
    (fun r x u => by apply Subtype.ext; exact mul_smul_comm _ _ _)

def alternation : VTwo →ₗ[ℂ] Three := TensorProduct.lift (wedgeLeftLinear 2)

@[simp] theorem alternation_pure (x y z : Space) :
    alternation (x ⊗ₜ[ℂ] wedgeTwo y z) = wedgeThree x y z := by
  rw [alternation, TensorProduct.lift.tmul]
  apply Subtype.ext
  change ExteriorAlgebra.ι ℂ x * (wedgeTwo y z).val = _
  rw [coe_wedgeTwo, coe_wedgeThree]

theorem wedgeTwo_add_left (x y z : Space) : wedgeTwo (x + y) z = wedgeTwo x z + wedgeTwo y z := by
  apply Subtype.ext
  simp [coe_wedgeTwo, add_mul]

private theorem wedgeTwo_add_right (x y z : Space) : wedgeTwo x (y + z) = wedgeTwo x y + wedgeTwo x z := by
  apply Subtype.ext
  simp [coe_wedgeTwo, mul_add]

theorem wedgeTwo_smul_left (c : ℂ) (x y : Space) : wedgeTwo (c • x) y = c • wedgeTwo x y := by
  apply Subtype.ext
  simp [coe_wedgeTwo]

theorem wedgeTwo_smul_right (c : ℂ) (x y : Space) : wedgeTwo x (c • y) = c • wedgeTwo x y := by
  apply Subtype.ext
  simp [coe_wedgeTwo]

private def traceTerm (y z : Space) : Space →ₗ[ℂ] Space :=
  (splitMetric.flip y).smulRight z - (splitMetric.flip z).smulRight y

private def traceAlt : Space [⋀^Fin 2]→ₗ[ℂ] (Space →ₗ[ℂ] Space) where
  toFun w := traceTerm (w 0) (w 1)
  map_update_add' w i a b := by
    apply LinearMap.ext
    intro x
    fin_cases i <;> simp [traceTerm, Function.update, smul_add, add_smul] <;> module
  map_update_smul' w i c a := by
    apply LinearMap.ext
    intro x
    fin_cases i <;> simp [traceTerm, Function.update, smul_smul, smul_sub] <;> module
  map_eq_zero_of_eq' w i j h hij := by
    fin_cases i <;> fin_cases j <;> simp_all [traceTerm]

def trace : VTwo →ₗ[ℂ] Space :=
  TensorProduct.lift (exteriorPower.alternatingMapLinearEquiv traceAlt).flip

@[simp] theorem trace_pure (x y z : Space) :
    trace (x ⊗ₜ[ℂ] wedgeTwo y z) = splitForm x y • z - splitForm x z • y := by
  simp [trace, wedgeTwo, traceAlt, traceTerm, splitMetric_apply]

private theorem map_wedgeTwo (f : Space →ₗ[ℂ] Space) (x y : Space) :
    exteriorPower.map 2 f (wedgeTwo x y) = wedgeTwo (f x) (f y) := by
  rw [wedgeTwo, wedgeTwo, exteriorPower.map_apply_ιMulti]
  congr 1
  funext i
  fin_cases i <;> rfl

private theorem map_wedgeThree (f : Space →ₗ[ℂ] Space) (x y z : Space) :
    exteriorPower.map 3 f (wedgeThree x y z) = wedgeThree (f x) (f y) (f z) := by
  rw [wedgeThree, wedgeThree, exteriorPower.map_apply_ιMulti]
  congr 1
  funext i
  fin_cases i <;> rfl

private theorem two_ext {W : Type*} [AddCommGroup W] [Module ℂ W] {f g : Two →ₗ[ℂ] W}
    (h : ∀ y z, f (wedgeTwo y z) = g (wedgeTwo y z)) : f = g := by
  apply exteriorPower.linearMap_ext
  apply AlternatingMap.ext
  intro v
  have hv : (![v 0, v 1] : Fin 2 → Space) = v := by funext i; fin_cases i <;> rfl
  simpa only [LinearMap.compAlternatingMap_apply, wedgeTwo, hv] using h (v 0) (v 1)

private theorem three_ext {W : Type*} [AddCommGroup W] [Module ℂ W] {f g : Three →ₗ[ℂ] W}
    (h : ∀ x y z, f (wedgeThree x y z) = g (wedgeThree x y z)) : f = g := by
  apply exteriorPower.linearMap_ext
  apply AlternatingMap.ext
  intro v
  have hv : (![v 0, v 1, v 2] : Fin 3 → Space) = v := by funext i; fin_cases i <;> rfl
  simpa only [LinearMap.compAlternatingMap_apply, wedgeThree, hv] using h (v 0) (v 1) (v 2)

private theorem tensor_ext {W : Type*} [AddCommGroup W] [Module ℂ W] {f g : VTwo →ₗ[ℂ] W}
    (h : ∀ x y z, f (x ⊗ₜ[ℂ] wedgeTwo y z) = g (x ⊗ₜ[ℂ] wedgeTwo y z)) : f = g := by
  apply TensorProduct.ext'
  intro x u
  have he : f.comp (TensorProduct.mk ℂ Space Two x) = g.comp (TensorProduct.mk ℂ Space Two x) :=
    two_ext (h x)
  exact DFunLike.congr_fun he u

theorem action_pure (g : splitSpecialOrthogonal) (x y z : Space) :
    tensorAction g (x ⊗ₜ[ℂ] wedgeTwo y z) = g.val x ⊗ₜ[ℂ] wedgeTwo (g.val y) (g.val z) := by
  change TensorProduct.map g.val (exteriorPower.map 2 g.val) _ = _
  rw [TensorProduct.map_tmul, map_wedgeTwo]

theorem alternation_equivariant (g : splitSpecialOrthogonal) :
    alternation.comp (tensorAction g) = (exteriorRepresentation 3 g).comp alternation := by
  apply tensor_ext
  intro x y z
  simp only [LinearMap.comp_apply, action_pure, alternation_pure]
  exact (map_wedgeThree g.val x y z).symm

theorem trace_equivariant (g : splitSpecialOrthogonal) :
    trace.comp (tensorAction g) = (vectorAction g).comp trace := by
  apply tensor_ext
  intro x y z
  simp only [LinearMap.comp_apply, action_pure, trace_pure, g.prop.2, map_sub, map_smul]
  rfl

def cyclicTensor (x y z : Space) : VTwo :=
  x ⊗ₜ[ℂ] wedgeTwo y z + y ⊗ₜ[ℂ] wedgeTwo z x + z ⊗ₜ[ℂ] wedgeTwo x y

private theorem cyclic_repeat (x z : Space) : cyclicTensor x x z = 0 := by
  unfold cyclicTensor
  rw [wedgeTwo_self, tmul_zero, add_zero, wedgeTwo_swap x z, tmul_neg, add_neg_cancel]

private theorem cyclic_rotate (x y z : Space) : cyclicTensor y z x = cyclicTensor x y z := by
  unfold cyclicTensor
  abel

private def cyclicFamily (w : Fin 3 → Space) : VTwo := cyclicTensor (w 0) (w 1) (w 2)

private theorem fin3_distinct (i j : Fin 3) (h : i.val ≠ j.val) : i ≠ j :=
  fun e => h (congrArg Fin.val e)

private theorem fin3_cases : ∀ i : Fin 3, i = 0 ∨ i = 1 ∨ i = 2 := by decide +kernel

private theorem cyclic_update_zero [DecidableEq (Fin 3)] (w : Fin 3 → Space) (x : Space) :
    cyclicFamily (Function.update w 0 x) = cyclicTensor x (w 1) (w 2) := by
  unfold cyclicFamily
  rw [Function.update_self, Function.update_of_ne (fin3_distinct 1 0 (by decide)),
    Function.update_of_ne (fin3_distinct 2 0 (by decide))]

private theorem cyclic_update_one [DecidableEq (Fin 3)] (w : Fin 3 → Space) (x : Space) :
    cyclicFamily (Function.update w 1 x) = cyclicTensor (w 0) x (w 2) := by
  unfold cyclicFamily
  rw [Function.update_self, Function.update_of_ne (fin3_distinct 0 1 (by decide)),
    Function.update_of_ne (fin3_distinct 2 1 (by decide))]

private theorem cyclic_update_two [DecidableEq (Fin 3)] (w : Fin 3 → Space) (x : Space) :
    cyclicFamily (Function.update w 2 x) = cyclicTensor (w 0) (w 1) x := by
  unfold cyclicFamily
  rw [Function.update_self, Function.update_of_ne (fin3_distinct 0 2 (by decide)),
    Function.update_of_ne (fin3_distinct 1 2 (by decide))]

private def cyclicAlternating : Space [⋀^Fin 3]→ₗ[ℂ] VTwo where
  toFun := cyclicFamily
  map_update_add' w i a b := by
    rcases fin3_cases i with rfl | rfl | rfl
    · simp only [cyclic_update_zero, cyclicTensor, wedgeTwo_add_left, wedgeTwo_add_right, add_tmul, tmul_add]; abel
    · simp only [cyclic_update_one, cyclicTensor, wedgeTwo_add_left, wedgeTwo_add_right, add_tmul, tmul_add]; abel
    · simp only [cyclic_update_two, cyclicTensor, wedgeTwo_add_left, wedgeTwo_add_right, add_tmul, tmul_add]; abel
  map_update_smul' w i c a := by
    rcases fin3_cases i with rfl | rfl | rfl
    · simp only [cyclic_update_zero, cyclicTensor, wedgeTwo_smul_left, wedgeTwo_smul_right, ← smul_tmul', tmul_smul]; module
    · simp only [cyclic_update_one, cyclicTensor, wedgeTwo_smul_left, wedgeTwo_smul_right, ← smul_tmul', tmul_smul]; module
    · simp only [cyclic_update_two, cyclicTensor, wedgeTwo_smul_left, wedgeTwo_smul_right, ← smul_tmul', tmul_smul]; module
  map_eq_zero_of_eq' w i j h hij := by
    have h₁ (x y : Space) : cyclicTensor x y x = 0 := by rw [cyclic_rotate x x y, cyclic_repeat]
    have h₂ (x y : Space) : cyclicTensor x y y = 0 := by rw [← cyclic_rotate x y y, cyclic_repeat]
    change cyclicTensor (w 0) (w 1) (w 2) = 0
    fin_cases i <;> fin_cases j
    · exact (hij rfl).elim
    · rw [← (show w 0 = w 1 from h), cyclic_repeat]
    · rw [← (show w 0 = w 2 from h), h₁]
    · rw [(show w 1 = w 0 from h), cyclic_repeat]
    · exact (hij rfl).elim
    · rw [← (show w 1 = w 2 from h), h₂]
    · rw [(show w 2 = w 0 from h), h₁]
    · rw [(show w 2 = w 1 from h), h₂]
    · exact (hij rfl).elim

def includeThree : Three →ₗ[ℂ] VTwo := (3 : ℂ)⁻¹ • exteriorPower.alternatingMapLinearEquiv cyclicAlternating

@[simp] theorem includeThree_pure (x y z : Space) : includeThree (wedgeThree x y z) =
    (3 : ℂ)⁻¹ • cyclicTensor x y z := by
  simp [includeThree, wedgeThree, cyclicAlternating, cyclicFamily]

theorem wedgeThree_rotate (x y z : Space) : wedgeThree y z x = wedgeThree x y z := by
  let p : Equiv.Perm (Fin 3) := Equiv.swap 0 2 * Equiv.swap 0 1
  have hp : p.sign = 1 := by decide +kernel
  have he : (![y, z, x] : Fin 3 → Space) = ![x, y, z] ∘ p := by
    funext i
    fin_cases i <;> rfl
  rw [wedgeThree, wedgeThree, he, AlternatingMap.map_perm, hp, one_smul]

theorem splitForm_symm (x y : Space) : splitForm x y = splitForm y x := by
  apply Finset.sum_congr rfl
  intro i _
  change x (plusAxis i) * y (minusAxis i) + x (minusAxis i) * y (plusAxis i) =
    y (plusAxis i) * x (minusAxis i) + y (minusAxis i) * x (plusAxis i)
  ring

theorem alternation_includeThree : alternation.comp includeThree = LinearMap.id := by
  apply three_ext
  intro x y z
  simp only [LinearMap.comp_apply, includeThree_pure, map_smul, cyclicTensor, map_add, alternation_pure,
    LinearMap.id_apply]
  rw [wedgeThree_rotate y z x, wedgeThree_rotate x y z]
  module

theorem trace_includeThree : trace.comp includeThree = 0 := by
  apply three_ext
  intro x y z
  simp only [LinearMap.comp_apply, includeThree_pure, map_smul, cyclicTensor, map_add, trace_pure,
    LinearMap.zero_apply]
  rw [splitForm_symm y x, splitForm_symm z x, splitForm_symm z y]
  module

theorem includeThree_equivariant (g : splitSpecialOrthogonal) :
    includeThree.comp (exteriorRepresentation 3 g) = (tensorAction g).comp includeThree := by
  apply three_ext
  intro x y z
  change includeThree (exteriorPower.map 3 g.val (wedgeThree x y z)) = tensorAction g (includeThree (wedgeThree x y z))
  simp only [map_wedgeThree, includeThree_pure, map_smul, cyclicTensor, map_add, action_pure]

private theorem metric_orthBasis (i : Axis) : splitMetric (orthBasis i) = orthBasis.coord i := by
  apply orthBasis.ext
  intro j
  rw [splitMetric_apply, orthBasis_pair, Module.Basis.coord_apply, Module.Basis.repr_self, Finsupp.single_apply]
  simp [eq_comm]

theorem orth_sum (x : Space) : ∑ i, splitForm (orthBasis i) x • orthBasis i = x := by
  have h (i : Axis) : splitForm (orthBasis i) x = orthBasis.repr x i := by
    rw [← splitMetric_apply, metric_orthBasis, Module.Basis.coord_apply]
  simp only [h, orthBasis.sum_repr]

private def metricIso : Space ≃ₗ[ℂ] Module.Dual ℂ Space :=
  orthBasis.equiv orthBasis.dualBasis (Equiv.refl Axis)

private theorem metricIso_eq : metricIso.toLinearMap = splitMetric := by
  apply orthBasis.ext
  intro i
  rw [metric_orthBasis]
  change orthBasis.equiv orthBasis.dualBasis (Equiv.refl Axis) (orthBasis i) = _
  simp

private def tensorEval : (Space ⊗[ℂ] Space) ≃ₗ[ℂ] (Space →ₗ[ℂ] Space) :=
  (TensorProduct.congr metricIso (LinearEquiv.refl ℂ Space)).trans (dualTensorHomEquiv ℂ Space Space)

private theorem tensorEval_tmul (x y z : Space) : tensorEval (x ⊗ₜ[ℂ] y) z = splitForm x z • y := by
  change dualTensorHom ℂ Space Space ((metricIso x) ⊗ₜ[ℂ] y) z = _
  rw [dualTensorHom_apply, ← LinearEquiv.coe_coe, metricIso_eq, splitMetric_apply]

def metricTensor : Space ⊗[ℂ] Space := ∑ i, orthBasis i ⊗ₜ[ℂ] orthBasis i

theorem metricTensor_invariant (g : splitSpecialOrthogonal) :
    TensorProduct.map g.val g.val metricTensor = metricTensor := by
  apply tensorEval.injective
  apply LinearMap.ext
  intro v
  let e := LinearMap.equivOfIsUnitDet (g.prop.1 ▸ isUnit_one : IsUnit g.val.det)
  obtain ⟨x, hx⟩ := e.surjective v
  have he : e.toLinearMap = g.val := LinearMap.coe_equivOfIsUnitDet _
  change e.toLinearMap x = v at hx
  rw [he] at hx
  rw [← hx]
  simp only [metricTensor, map_sum, map_tmul, LinearMap.sum_apply, tensorEval_tmul, g.prop.2, orth_sum]
  simp_rw [← map_smul g.val]
  rw [← map_sum, orth_sum]

private def rawVector : Space →ₗ[ℂ] VTwo where
  toFun x := ∑ i, orthBasis i ⊗ₜ[ℂ] wedgeTwo (orthBasis i) x
  map_add' x y := by simp [wedgeTwo_add_right, tmul_add, Finset.sum_add_distrib]
  map_smul' c x := by simp [wedgeTwo_smul_right, tmul_smul, Finset.smul_sum]

def includeVector : Space →ₗ[ℂ] VTwo := (13 : ℂ)⁻¹ • rawVector

theorem includeVector_apply (x : Space) : includeVector x =
    (13 : ℂ)⁻¹ • ∑ i, orthBasis i ⊗ₜ[ℂ] wedgeTwo (orthBasis i) x := rfl

private theorem trace_rawVector (x : Space) : trace (rawVector x) = (13 : ℂ) • x := by
  change trace (∑ i, orthBasis i ⊗ₜ[ℂ] wedgeTwo (orthBasis i) x) = _
  simp only [map_sum, trace_pure, orthBasis_pair, if_true, Finset.sum_sub_distrib,
    Finset.sum_const, Finset.card_univ, Fintype.card_fin, orth_sum]
  rw [← Nat.cast_smul_eq_nsmul ℂ]
  module

theorem wedgeThree_repeat (x y : Space) : wedgeThree x x y = 0 := by
  apply Subtype.ext
  rw [coe_wedgeThree, Submodule.coe_zero, ← mul_assoc, ExteriorAlgebra.ι_sq_zero, zero_mul]

theorem trace_includeVector : trace.comp includeVector = LinearMap.id := by
  apply LinearMap.ext
  intro x
  simp only [LinearMap.comp_apply, includeVector, LinearMap.smul_apply, map_smul, trace_rawVector,
    LinearMap.id_apply, smul_smul]
  norm_num

set_option maxHeartbeats 1000000 in
theorem alternation_includeVector : alternation.comp includeVector = 0 := by
  apply LinearMap.ext
  intro x
  change alternation ((13 : ℂ)⁻¹ • ∑ i, orthBasis i ⊗ₜ[ℂ] wedgeTwo (orthBasis i) x) = 0
  rw [map_smul, map_sum, Finset.sum_eq_zero fun i _ => by rw [alternation_pure, wedgeThree_repeat], smul_zero]

private def wedgeRight (x : Space) : Space →ₗ[ℂ] Two where
  toFun y := wedgeTwo y x
  map_add' y z := wedgeTwo_add_left y z x
  map_smul' c y := wedgeTwo_smul_left c y x

private def insertVector (x : Space) : (Space ⊗[ℂ] Space) →ₗ[ℂ] VTwo :=
  TensorProduct.map LinearMap.id (wedgeRight x)

private theorem insertVector_metricTensor (x : Space) : insertVector x metricTensor = rawVector x := by
  change TensorProduct.map LinearMap.id (wedgeRight x) metricTensor = _
  simp only [metricTensor, map_sum, map_tmul, LinearMap.id_apply]
  rfl

set_option maxHeartbeats 1000000 in
theorem includeVector_equivariant (g : splitSpecialOrthogonal) :
    includeVector.comp (vectorAction g) = (tensorAction g).comp includeVector := by
  have h (x : Space) : (tensorAction g).comp (insertVector x) =
      (insertVector (g.val x)).comp (TensorProduct.map g.val g.val) := by
    apply TensorProduct.ext'
    intro y z
    change tensorAction g (TensorProduct.map LinearMap.id (wedgeRight x) (y ⊗ₜ[ℂ] z)) =
      TensorProduct.map LinearMap.id (wedgeRight (g.val x)) (TensorProduct.map g.val g.val (y ⊗ₜ[ℂ] z))
    simp only [map_tmul, LinearMap.id_apply]
    exact action_pure g y z x
  apply LinearMap.ext
  intro x
  have he := DFunLike.congr_fun (h x) metricTensor
  change tensorAction g (insertVector x metricTensor) =
    insertVector (g.val x) (TensorProduct.map g.val g.val metricTensor) at he
  rw [metricTensor_invariant, insertVector_metricTensor, insertVector_metricTensor] at he
  change (13 : ℂ)⁻¹ • rawVector (g.val x) = tensorAction g ((13 : ℂ)⁻¹ • rawVector x)
  rw [map_smul, he]

/-- The joint kernel of alternation and trace. -/
def hook : Submodule ℂ VTwo := alternation.ker ⊓ trace.ker

theorem mem_hook (x : VTwo) : x ∈ hook ↔ alternation x = 0 ∧ trace x = 0 := by
  simp [hook, LinearMap.mem_ker]

theorem hook_invariant (g : splitSpecialOrthogonal) (x : VTwo) (hx : x ∈ hook) : tensorAction g x ∈ hook := by
  rw [mem_hook] at hx ⊢
  have ha := DFunLike.congr_fun (alternation_equivariant g) x
  have ht := DFunLike.congr_fun (trace_equivariant g) x
  simp only [LinearMap.comp_apply, hx.1, hx.2, map_zero] at ha ht
  exact ⟨ha, ht⟩

def hookAction : Representation ℂ splitSpecialOrthogonal hook :=
  tensorAction.subrepresentation hook (fun g x hx => hook_invariant g x hx)

@[simp] theorem alternation_three (u : Three) : alternation (includeThree u) = u :=
  DFunLike.congr_fun alternation_includeThree u

@[simp] theorem trace_three (u : Three) : trace (includeThree u) = 0 :=
  DFunLike.congr_fun trace_includeThree u

set_option maxHeartbeats 1000000 in
@[simp] theorem alternation_vector (v : Space) : alternation (includeVector v) = 0 := by
  have h : (alternation.comp includeVector) v = (0 : Space →ₗ[ℂ] Three) v :=
    LinearMap.congr_fun alternation_includeVector v
  simpa only [LinearMap.comp_apply, LinearMap.zero_apply] using h

set_option maxHeartbeats 1000000 in
@[simp] theorem trace_vector (v : Space) : trace (includeVector v) = v := by
  have h : (trace.comp includeVector) v = (LinearMap.id : Space →ₗ[ℂ] Space) v :=
    LinearMap.congr_fun trace_includeVector v
  simpa only [LinearMap.comp_apply, LinearMap.id_apply] using h

def residual : VTwo →ₗ[ℂ] VTwo := LinearMap.id - includeThree.comp alternation - includeVector.comp trace

theorem residual_mem (x : VTwo) : residual x ∈ hook := by
  simp [mem_hook, residual]

def splitLinear : VTwo ≃ₗ[ℂ] Three × Space × hook where
  toFun x := (alternation x, trace x, ⟨residual x, residual_mem x⟩)
  invFun p := includeThree p.1 + includeVector p.2.1 + p.2.2.val
  left_inv x := by
    change includeThree (alternation x) + includeVector (trace x) + residual x = x
    simp only [residual, LinearMap.sub_apply, LinearMap.id_apply, LinearMap.comp_apply]
    abel
  right_inv p := by
    rcases p with ⟨u, v, w⟩
    have hw := (mem_hook w.val).mp w.prop
    refine Prod.ext ?_ (Prod.ext ?_ (Subtype.ext ?_))
    · change alternation (includeThree u + includeVector v + w.val) = u
      simp [hw.1]
    · change trace (includeThree u + includeVector v + w.val) = v
      simp [hw.2]
    · change residual (includeThree u + includeVector v + w.val) = w.val
      simp [residual, hw.1, hw.2]
      abel
  map_add' x y := Prod.ext (alternation.map_add x y)
    (Prod.ext (trace.map_add x y) (Subtype.ext (residual.map_add x y)))
  map_smul' c x := Prod.ext (alternation.map_smul c x)
    (Prod.ext (trace.map_smul c x) (Subtype.ext (residual.map_smul c x)))

/-- The splitting intertwines the actual orthogonal actions. -/
theorem split_equivariant (g : splitSpecialOrthogonal) (x : VTwo) :
    splitLinear (tensorAction g x) =
      ((exteriorRepresentation 3).prod (vectorAction.prod hookAction)) g (splitLinear x) := by
  have ha := DFunLike.congr_fun (alternation_equivariant g) x
  have ht := DFunLike.congr_fun (trace_equivariant g) x
  simp only [LinearMap.comp_apply] at ha ht
  refine Prod.ext ha (Prod.ext ht (Subtype.ext ?_))
  change residual (tensorAction g x) = tensorAction g (residual x)
  simp only [residual, LinearMap.sub_apply, LinearMap.comp_apply, LinearMap.id_apply, ha, ht, map_sub]
  have h₁ := DFunLike.congr_fun (includeThree_equivariant g) (alternation x)
  have h₂ := DFunLike.congr_fun (includeVector_equivariant g) (trace x)
  simp only [LinearMap.comp_apply] at h₁ h₂
  rw [h₁, h₂]

def splitRepresentation : tensorAction.Equiv ((exteriorRepresentation 3).prod (vectorAction.prod hookAction)) :=
  Representation.Equiv.mk splitLinear (fun g => LinearMap.ext (split_equivariant g))

set_option backward.isDefEq.respectTransparency false in
/-- The trace-free, alternation-free part has dimension 896. -/
theorem hook_dimension : Module.finrank ℂ hook = 896 := by
  let : Module.Free ℂ (↥hook) := Module.Free.of_divisionRing ℂ (↥hook)
  have h := splitLinear.finrank_eq
  rw [Module.finrank_tensorProduct, Module.finrank_prod, Module.finrank_prod,
    exteriorPower.finrank_eq, exteriorPower.finrank_eq, Module.finrank_pi, Fintype.card_fin] at h
  have h₂ : Nat.choose 14 2 = 91 := by decide
  have h₃ : Nat.choose 14 3 = 364 := by decide
  rw [h₂, h₃] at h
  omega

private abbrev u (i : Pair) : Space := axisBasis (plusAxis i)

private theorem wedge_first_two : wedgeTwo (u 0) (u 1) =
    axisBasis.exteriorPower 2 (highestPlus (2 : Fin 15)) := by
  let axes : Fin 2 → Axis := ![plusAxis 0, plusAxis 1]
  have hstrict : ∀ i j, i < j → axes i < axes j := by decide +kernel
  have hmem : ∀ i, axes i ∈ (highestPlus (2 : Fin 15)).val := by decide +kernel
  let e := OrderEmbedding.ofStrictMono axes hstrict
  have he := Finset.orderEmbOfFin_unique' (highestPlus (2 : Fin 15)).prop (f := e) hmem
  rw [exteriorPower.basis_apply, exteriorPower.ιMulti_family,
    Set.powersetCard.ofFinEmbEquiv_symm_apply, ← he]
  rfl

/-- The null-basis hook candidate with weight two on the first pair and one on the second. -/
def hookHighest : VTwo := u 0 ⊗ₜ[ℂ] wedgeTwo (u 0) (u 1)

theorem hookHighest_ne_zero : hookHighest ≠ 0 := by
  rw [hookHighest, wedge_first_two]
  simpa only [Module.Basis.tensorProduct_apply'] using
    (axisBasis.tensorProduct (axisBasis.exteriorPower 2)).ne_zero (plusAxis 0, highestPlus (2 : Fin 15))

theorem hookHighest_mem : hookHighest ∈ hook := by
  have hz (j : Pair) : splitForm (u 0) (u j) = 0 := by
    rw [← splitMetric_apply, splitMetric_null_plus, Module.Basis.coord_apply,
      Module.Basis.repr_self, Finsupp.single_apply]
    have he : ∀ j : Pair, plusAxis j ≠ minusAxis 0 := by decide +kernel
    rw [if_neg (he j)]
  simp [mem_hook, hookHighest, wedgeThree_repeat, hz]

theorem hookHighest_torus (t : Pair → ℂˣ) :
    tensorAction (torusElement t) hookHighest = ((t 0 ^ 2 * t 1 : ℂˣ) : ℂ) • hookHighest := by
  have h0 : scale t (plusAxis 0) = t 0 := by change t 0 ^ (1 : ℤ) = _; rw [zpow_one]
  have h1 : scale t (plusAxis 1) = t 1 := by change t 1 ^ (1 : ℤ) = _; rw [zpow_one]
  have h (j : Pair) : torus t (u j) = (scale t (plusAxis j) : ℂ) • u j := torus_axis t _
  change tensorAction (torusElement t) (u 0 ⊗ₜ[ℂ] wedgeTwo (u 0) (u 1)) = _
  rw [action_pure]
  change torus t (u 0) ⊗ₜ[ℂ] wedgeTwo (torus t (u 0)) (torus t (u 1)) = _
  rw [h 0, h 1, h0, h1, wedgeTwo_smul_left, wedgeTwo_smul_right, smul_smul, smul_tmul_smul]
  change _ • hookHighest = _
  congr 1
  push_cast
  ring

theorem hookHighest_root_fixed (c : ℂ) (i j : Pair) (h : i < j) :
    tensorAction (rootMinusElement c i j h) hookHighest = hookHighest ∧
      tensorAction (rootPlusElement c i j h) hookHighest = hookHighest := by
  have hV := firstAxis_root_fixed c i j h
  have hW := highestPlus_root_fixed (2 : Fin 15) c i j h
  let v := axisBasis.exteriorPower 2 (highestPlus (2 : Fin 15))
  change exteriorRepresentation 2 (rootMinusElement c i j h) v = v ∧
    exteriorRepresentation 2 (rootPlusElement c i j h) v = v at hW
  rw [hookHighest, wedge_first_two]
  constructor
  · change TensorProduct.map (rootMinusElement c i j h).val (exteriorRepresentation 2 (rootMinusElement c i j h)) _ = _
    rw [map_tmul, hV.1, hW.1]
  · change TensorProduct.map (rootPlusElement c i j h).val (exteriorRepresentation 2 (rootPlusElement c i j h)) _ = _
    rw [map_tmul, hV.2, hW.2]

/-- The unfiltered signed table for this tensor product. -/
theorem vector_tensor_grade_two : D7Counts.gradeMultiplicities 1 2 =
    D7Counts.tally [(D7Counts.mu 1, 1), (D7Counts.mu 3, 1), (D7Counts.nu 2, 1)] := by
  decide +kernel

end
end GeometricUnity.D7VectorTensor
~~~

[Return to file index](#file-index)

## D7Hook.lean {#source-d7hook-lean}

Proves irreducibility of the traceless hook representation.

~~~lean
import D7Irreducible
import D7VectorTensor

/-!
# Irreducibility of the traceless hook

Double sign changes separate the tensor basis by the indices appearing an
odd number of times. A transposition within one such block extracts a
difference. Plane rotations connect differences from the two block types.
-/

namespace GeometricUnity.D7Hook

open D7Exterior D7Hodge D7Irreducible D7VectorTensor TensorProduct
open scoped BigOperators TensorProduct

noncomputable section

private abbrev e := orthBasis
private def blade (a i j : Axis) : VTwo := e a ⊗ₜ[ℂ] wedgeTwo (e i) (e j)
private def repeated (i k : Axis) : VTwo := blade i i k
private def diffRepeated (i j k : Axis) : VTwo := repeated i k - repeated j k
private def diffDistinct (i j k : Axis) : VTwo := blade i j k + blade j i k
private def Distinct (i j k : Axis) : Prop := i ≠ j ∧ i ≠ k ∧ j ≠ k

private theorem blade_swap (a i j : Axis) : blade a j i = -blade a i j := by
  rw [blade, blade, wedgeTwo_swap, tmul_neg]

private theorem repeated_self (i : Axis) : repeated i i = 0 := by
  simp [repeated, blade, wedgeTwo_self]

private def column (s : Index 2) (j : Fin 2) : Axis := Set.powersetCard.ofFinEmbEquiv.symm s j

private theorem column_ne (s : Index 2) : column s 0 ≠ column s 1 := by
  intro h
  have h' : (0 : Fin 2) = 1 := (Set.powersetCard.ofFinEmbEquiv.symm s).injective h
  exact (by decide : (0 : Fin 2) ≠ 1) h'

private theorem columns (s : Index 2) : s.val = {column s 0, column s 1} := by
  ext a
  change a ∈ s ↔ a ∈ ({column s 0, column s 1} : Finset Axis)
  rw [← Set.powersetCard.mem_range_ofFinEmbEquiv_symm_iff_mem s a]
  constructor
  · rintro ⟨j, rfl⟩
    fin_cases j
    · exact Finset.mem_insert_self _ _
    · exact Finset.mem_insert.mpr (Or.inr (Finset.mem_singleton_self _))
  · intro h
    rcases (Finset.mem_insert.mp h) with h | h
    · exact ⟨0, h.symm⟩
    · exact ⟨1, (Finset.mem_singleton.mp h).symm⟩

def tensorExteriorBasis (k : ℕ) : Module.Basis (Axis × Index k) ℂ (Space ⊗[ℂ] Exterior k) :=
  e.tensorProduct (basis k)

private abbrev tensorBasis := tensorExteriorBasis 2

private theorem tensorBasis_blade (t : Axis × Index 2) :
    tensorBasis t = blade t.1 (column t.2 0) (column t.2 1) := by
  rw [tensorBasis, tensorExteriorBasis, Module.Basis.tensorProduct_apply', exteriorPower.basis_apply]
  congr 1

def parity {k : ℕ} (t : Axis × Index k) : Finset Axis :=
  if t.1 ∈ t.2.val then t.2.val.erase t.1 else insert t.1 t.2.val

private theorem parity_card (t : Axis × Index 2) : (parity t).card = 1 ∨ (parity t).card = 3 := by
  by_cases h : t.1 ∈ t.2.val
  · left; rw [parity, if_pos h, Finset.card_erase_of_mem h, t.2.prop]
  · right; rw [parity, if_neg h, Finset.card_insert_of_notMem h, t.2.prop]

private theorem parity_not_complement (t s : Axis × Index 2) : parity t ≠ (parity s)ᶜ := by
  intro h
  have hc := congrArg Finset.card h
  rw [Finset.card_compl, Fintype.card_fin] at hc
  rcases parity_card s with hs | hs <;> rcases parity_card t with ht | ht <;> omega

private theorem parity_sign {k : ℕ} (t : Axis × Index k) (i : Axis) :
    subsetFlip (parity t) i = axisFlip i t.1 * subsetFlip t.2.val i := by
  by_cases ha : t.1 ∈ t.2.val <;> by_cases he : t.1 = i <;> by_cases hm : i ∈ t.2.val <;>
    simp_all [parity, subsetFlip, axisFlip, Finset.mem_erase, eq_comm]

theorem tensorExterior_doubleFlip {k : ℕ} (i j : Axis) (t : Axis × Index k) :
    (vectorAction.tprod (exteriorRepresentation k)) (doubleFlip i j) (tensorExteriorBasis k t) =
      character (parity t) i j • tensorExteriorBasis k t := by
  rw [tensorExteriorBasis, Module.Basis.tensorProduct_apply']
  change TensorProduct.map (doubleFlip i j).val (exteriorRepresentation k (doubleFlip i j))
    (e t.1 ⊗ₜ[ℂ] basis k t.2) = _
  rw [map_tmul, doubleFlip_basis, doubleFlip_exterior, smul_tmul_smul]
  congr 1
  simp only [character, parity_sign]
  ring

private theorem tensor_doubleFlip (i j : Axis) (t : Axis × Index 2) :
    tensorAction (doubleFlip i j) (tensorBasis t) = character (parity t) i j • tensorBasis t :=
  tensorExterior_doubleFlip i j t

private def Stable (W : Submodule ℂ VTwo) : Prop :=
  ∀ g : splitSpecialOrthogonal, ∀ x ∈ W, tensorAction g x ∈ W

private theorem block_in_submodule (W : Submodule ℂ VTwo) (hW : Stable W) (hne : W ≠ ⊥) :
    ∃ x : VTwo, ∃ s : Axis × Index 2, x ∈ W ∧ x ≠ 0 ∧
      ∀ t, tensorBasis.repr x t ≠ 0 → parity t = parity s := by
  obtain ⟨x, s, hx, hs, hw⟩ := support_sign_block tensorBasis parity
    (fun i j => tensorAction (doubleFlip i j)) tensor_doubleFlip W (fun i j => hW (doubleFlip i j)) hne
  exact ⟨x, s, hx, fun h => hs (by simp [h]), fun t ht => (hw t ht).resolve_right (parity_not_complement t s)⟩

private theorem basis_span_block (x : VTwo) (s : Finset Axis) (U : Submodule ℂ VTwo)
    (hs : ∀ t, tensorBasis.repr x t ≠ 0 → parity t = s)
    (hU : ∀ t, parity t = s → tensorBasis t ∈ U) : x ∈ U := by
  rw [← tensorBasis.sum_repr x]
  apply U.sum_mem
  intro t _
  by_cases h : tensorBasis.repr x t = 0
  · rw [h, zero_smul]; exact U.zero_mem
  · exact U.smul_mem _ (hU t (hs t h))

private theorem parity_singleton {t : Axis × Index 2} {k : Axis} (h : parity t = {k}) :
    ∃ i : {i : Axis // i ≠ k}, tensorBasis t = repeated i.val k ∨ tensorBasis t = -repeated i.val k := by
  have ht : t.1 ∈ t.2.val := by
    by_contra hn
    have hc := congrArg Finset.card h
    rw [parity, if_neg hn, Finset.card_insert_of_notMem hn, t.2.prop, Finset.card_singleton] at hc
    omega
  have he : t.2.val.erase t.1 = {k} := by simpa only [parity, if_pos ht] using h
  have hk : k ∈ t.2.val.erase t.1 := by rw [he]; exact Finset.mem_singleton_self _
  have hne : t.1 ≠ k := Ne.symm (Finset.mem_erase.mp hk).1
  have hcols := columns t.2
  have hleft : t.1 = column t.2 0 ∨ t.1 = column t.2 1 := by simpa only [hcols, Finset.mem_insert, Finset.mem_singleton] using ht
  have hright : k = column t.2 0 ∨ k = column t.2 1 := by
    simpa only [hcols, Finset.mem_insert, Finset.mem_singleton] using (Finset.mem_erase.mp hk).2
  refine ⟨⟨t.1, hne⟩, ?_⟩
  rw [tensorBasis_blade]
  rcases hleft with hl | hl <;> rcases hright with hr | hr
  · exact (hne (hl.trans hr.symm)).elim
  · left; rw [← hl, ← hr]; rfl
  · right; rw [← hl, ← hr, blade_swap]; rfl
  · exact (hne (hl.trans hr.symm)).elim

private def triple (i j k : Axis) : Fin 3 → VTwo := ![blade i j k, blade j k i, blade k i j]

private theorem parity_triple {t : Axis × Index 2} {i j k : Axis} (d : Distinct i j k)
    (h : parity t = {i, j, k}) :
    ∃ a : Fin 3, tensorBasis t = triple i j k a ∨ tensorBasis t = -triple i j k a := by
  have hc : ({i, j, k} : Finset Axis).card = 3 := by
    rw [Finset.card_insert_of_notMem (by simp [d.1, d.2.1]), Finset.card_pair d.2.2]
  have ht : t.1 ∉ t.2.val := by
    intro hm
    have hs := congrArg Finset.card h
    rw [parity, if_pos hm, Finset.card_erase_of_mem hm, t.2.prop, hc] at hs
    omega
  have hcols : ({t.1, column t.2 0, column t.2 1} : Finset Axis) = {i, j, k} := by
    rw [parity, if_neg ht, columns] at h
    exact h
  have hmem (a : Axis) (ha : a ∈ ({t.1, column t.2 0, column t.2 1} : Finset Axis)) :
      a = i ∨ a = j ∨ a = k := by
    rwa [hcols, Finset.mem_insert, Finset.mem_insert, Finset.mem_singleton] at ha
  let a := t.1
  let b := column t.2 0
  let c := column t.2 1
  have hab : a ≠ b := fun he => ht (by rw [columns, show t.1 = column t.2 0 from he]; simp)
  have hac : a ≠ c := fun he => ht (by rw [columns, show t.1 = column t.2 1 from he]; simp)
  have hbc : b ≠ c := column_ne t.2
  have ha := hmem a (by simp [a])
  have hb := hmem b (by simp [b])
  have hd := hmem c (by simp [c])
  change ∃ n : Fin 3, tensorBasis t = triple i j k n ∨ tensorBasis t = -triple i j k n
  rw [tensorBasis_blade]
  change ∃ n : Fin 3, blade a b c = triple i j k n ∨ blade a b c = -triple i j k n
  rcases ha with ha | ha | ha <;> rcases hb with hb | hb | hb <;> rcases hd with hd | hd | hd <;>
    try solve | exact (hab (ha.trans hb.symm)).elim | exact (hac (ha.trans hd.symm)).elim | exact (hbc (hb.trans hd.symm)).elim
  · exact ⟨0, Or.inl (by rw [ha, hb, hd]; rfl)⟩
  · exact ⟨0, Or.inr (by rw [ha, hb, hd]; exact blade_swap i j k)⟩
  · exact ⟨1, Or.inr (by rw [ha, hb, hd]; exact blade_swap j k i)⟩
  · exact ⟨1, Or.inl (by rw [ha, hb, hd]; rfl)⟩
  · exact ⟨2, Or.inl (by rw [ha, hb, hd]; rfl)⟩
  · exact ⟨2, Or.inr (by rw [ha, hb, hd]; exact blade_swap k i j)⟩

private theorem exists_pivot (i j k : Axis) (d : Distinct i j k) : ∃ p : Axis, p ≠ i ∧ p ≠ j ∧ p ≠ k := by
  by_contra! h
  have he : ({i, j, k} : Finset Axis) = Finset.univ := by
    apply Finset.eq_univ_of_forall
    intro p
    rw [Finset.mem_insert, Finset.mem_insert, Finset.mem_singleton]
    by_contra! he
    exact he.2.2 (h p he.1 he.2.1)
  have hc := congrArg Finset.card he
  rw [Finset.card_insert_of_notMem (by simp [d.1, d.2.1]), Finset.card_pair d.2.2,
    Finset.card_univ, Fintype.card_fin] at hc
  omega

private theorem action_blade_scaled (g : splitSpecialOrthogonal) (σ : Axis → Axis) (c : Axis → ℂ)
    (h : ∀ a, g.val (e a) = c a • e (σ a)) (a i j : Axis) :
    tensorAction g (blade a i j) = (c a * (c i * c j)) • blade (σ a) (σ i) (σ j) := by
  simp only [blade, action_pure, h, wedgeTwo_smul_left, wedgeTwo_smul_right, smul_smul, smul_tmul_smul]
  rw [mul_comm (c j) (c i)]

private theorem action_oriented_blade (σ : Equiv.Perm Axis) (p a i j : Axis)
    (ha : a ≠ p) (hi : i ≠ p) (hj : j ≠ p) :
    tensorAction (orientedPermAt σ p) (blade a i j) = blade (σ a) (σ i) (σ j) := by
  rw [action_blade_scaled _ σ (orientationCorrection σ p) (orientedPermAt_basis σ p)]
  simp [orientationCorrection, ha, hi, hj]

private theorem action_oriented_repeated (σ : Equiv.Perm Axis) (p i k : Axis) (hk : k ≠ p) :
    tensorAction (orientedPermAt σ p) (repeated i k) = repeated (σ i) (σ k) := by
  rw [repeated, repeated, action_blade_scaled _ σ (orientationCorrection σ p) (orientedPermAt_basis σ p)]
  have h : orientationCorrection σ p k = 1 := if_neg hk
  rw [h, mul_one, correction_sq, one_smul]

private theorem trace_repeated (i k : Axis) (h : i ≠ k) : trace (repeated i k) = e k := by
  unfold repeated blade
  rw [trace_pure, orthBasis_pair, orthBasis_pair, if_pos rfl, if_neg h]
  simp

private theorem trace_distinct (i j k : Axis) (d : Distinct i j k) : trace (blade i j k) = 0 := by
  unfold blade
  rw [trace_pure, orthBasis_pair, orthBasis_pair, if_neg d.1, if_neg d.2.1]
  simp

private theorem axes_triple_injective (i j k : Axis) (d : Distinct i j k) :
    Function.Injective (![i, j, k] : Fin 3 → Axis) := by
  intro a b h
  fin_cases a <;> fin_cases b
  · rfl
  · exact (d.1 h).elim
  · exact (d.2.1 h).elim
  · exact (d.1 h.symm).elim
  · rfl
  · exact (d.2.2 h).elim
  · exact (d.2.1 h.symm).elim
  · exact (d.2.2 h.symm).elim
  · rfl

private theorem wedge_three_ne_zero (i j k : Axis) (d : Distinct i j k) : wedgeThree (e i) (e j) (e k) ≠ 0 := by
  let a : Fin 3 → Axis := ![i, j, k]
  let f : Fin 3 → Module.Dual ℂ Space := fun j => e.coord (a j)
  let v : Fin 3 → Space := e ∘ a
  have hv : exteriorPower.ιMulti ℂ 3 v = wedgeThree (e i) (e j) (e k) := by
    congr 1
    funext j
    fin_cases j <;> rfl
  intro h
  have hm : Matrix.of (fun i j : Fin 3 => f j (v i)) = 1 := by
    ext i j
    have h : Function.Injective a := axes_triple_injective _ _ _ d
    simp only [f, v, Matrix.of_apply, Function.comp_apply, Module.Basis.coord_apply, Module.Basis.repr_self,
      Finsupp.single_apply, Matrix.one_apply, h.eq_iff]
  have he := exteriorPower.pairingDual_ιMulti_ιMulti (R := ℂ) f v
  rw [hv, h, map_zero, hm, Matrix.det_one] at he
  exact zero_ne_one he

private theorem triple_alternation (i j k : Axis) (a : Fin 3) :
    alternation (triple i j k a) = wedgeThree (e i) (e j) (e k) := by
  fin_cases a
  · exact alternation_pure _ _ _
  · exact (alternation_pure _ _ _).trans (wedgeThree_rotate _ _ _)
  · exact (alternation_pure _ _ _).trans ((wedgeThree_rotate (e j) (e k) (e i)).trans (wedgeThree_rotate _ _ _))

theorem swap_sum_difference {ι E : Type*} [Fintype ι] [DecidableEq ι] [AddCommGroup E] [Module ℂ E]
    (c : ι → ℂ) (v : ι → E)
    (a b : ι) (h : a ≠ b) :
    (∑ t, c t • v t) - (∑ t, c t • v (Equiv.swap a b t)) = (c a - c b) • (v a - v b) := by
  rw [← Finset.sum_sub_distrib, ← Finset.sum_subset (s₁ := {a, b}) (s₂ := Finset.univ) (Finset.subset_univ _)]
  · rw [Finset.sum_pair h, Equiv.swap_apply_left, Equiv.swap_apply_right]
    module
  · intro t _ ht
    simp only [Finset.mem_insert, Finset.mem_singleton, not_or] at ht
    rw [Equiv.swap_apply_of_ne_of_ne ht.1 ht.2, sub_self]

theorem coefficients_differ {ι E : Type*} [Fintype ι] [AddCommGroup E] [Module ℂ E] (c : ι → ℂ) (v : ι → E)
    (hc : ∑ t, c t = 0) (hv : (∑ t, c t • v t) ≠ 0) : ∃ a b, c a ≠ c b := by
  classical
  by_contra! he
  cases isEmpty_or_nonempty ι with
  | inl h => exact hv (Finset.sum_of_isEmpty _)
  | inr h =>
    let : Nonempty ι := h
    obtain ⟨i⟩ := h
    have hn : (Fintype.card ι : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr Fintype.card_ne_zero
    have hi : c i = 0 := by
      have h := hc
      simp_rw [he _ i] at h
      rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul] at h
      exact (mul_eq_zero.mp h).resolve_left hn
    exact hv (Finset.sum_eq_zero fun j _ => by rw [he j i, hi, zero_smul])

private theorem singleton_extract (W : Submodule ℂ VTwo) (hW : Stable W) (hsub : W ≤ hook) (k : Axis)
    (x : VTwo) (hx : x ∈ W) (hx0 : x ≠ 0)
    (hs : ∀ t, tensorBasis.repr x t ≠ 0 → parity t = {k}) :
    ∃ i j, Distinct i j k ∧ diffRepeated i j k ∈ W := by
  classical
  let v (i : {i : Axis // i ≠ k}) := repeated i.val k
  have hspan : x ∈ Submodule.span ℂ (Set.range v) := by
    apply basis_span_block x {k} _ hs
    intro t ht
    obtain ⟨i, hi | hi⟩ := parity_singleton ht
    · rw [hi]; exact Submodule.subset_span (Set.mem_range_self i)
    · rw [hi]; exact Submodule.neg_mem _ (Submodule.subset_span (Set.mem_range_self i))
  obtain ⟨c, rfl⟩ := (Submodule.mem_span_range_iff_exists_fun ℂ).mp hspan
  have htrace := ((mem_hook _).mp (hsub hx)).2
  have hc : ∑ i, c i = 0 := by
    have h (a : {i : Axis // i ≠ k}) : trace (v a) = e k := trace_repeated _ _ a.prop
    simp only [map_sum, map_smul, h, ← Finset.sum_smul] at htrace
    exact (smul_eq_zero.mp htrace).resolve_right (e.ne_zero k)
  obtain ⟨a, b, hne⟩ := coefficients_differ c v hc hx0
  have hab : a.val ≠ b.val := fun h => hne (congrArg c (Subtype.ext h))
  have d : Distinct a.val b.val k := ⟨hab, a.prop, b.prop⟩
  obtain ⟨p, _, _, hpk⟩ := exists_pivot _ _ _ d
  let σ := Equiv.swap a.val b.val
  let g := orientedPermAt σ p
  have hfix : σ k = k := Equiv.swap_apply_of_ne_of_ne (Ne.symm a.prop) (Ne.symm b.prop)
  have he (i : {i : Axis // i ≠ k}) : tensorAction g (v i) = v (Equiv.swap a b i) := by
    rw [show tensorAction g (v i) = repeated (σ i.val) (σ k) from
      action_oriented_repeated σ p _ _ (Ne.symm hpk), hfix]
    congr 1
    by_cases ha : i = a
    · subst i; simp [σ]
    · by_cases hb : i = b
      · subst i; simp [σ]
      · rw [Equiv.swap_apply_of_ne_of_ne ha hb]
        exact Equiv.swap_apply_of_ne_of_ne (fun h => ha (Subtype.ext h)) (fun h => hb (Subtype.ext h))
  have hm := W.sub_mem hx (hW g _ hx)
  simp only [map_sum, map_smul, he] at hm
  rw [swap_sum_difference c v a b (fun h => hne (congrArg c h))] at hm
  exact ⟨a.val, b.val, d, basis_mem_of_scaled W _ _ (sub_ne_zero.mpr hne) hm⟩

private theorem triple_swap_extract (W : Submodule ℂ VTwo) (hW : Stable W) (i j k : Axis) (d : Distinct i j k)
    (a b c : ℂ) (hab : a ≠ b)
    (hmem : a • blade i j k + b • blade j k i + c • blade k i j ∈ W) : diffDistinct i j k ∈ W := by
  obtain ⟨p, hpi, hpj, hpk⟩ := exists_pivot i j k d
  let σ := Equiv.swap i j
  let g := orientedPermAt σ p
  have hi : σ i = j := Equiv.swap_apply_left _ _
  have hj : σ j = i := Equiv.swap_apply_right _ _
  have hk : σ k = k := Equiv.swap_apply_of_ne_of_ne (Ne.symm d.2.1) (Ne.symm d.2.2)
  have hb₁ : tensorAction g (blade i j k) = -blade j k i := by
    rw [action_oriented_blade _ _ _ _ _ (Ne.symm hpi) (Ne.symm hpj) (Ne.symm hpk), hi, hj, hk, blade_swap j k i]
  have hb₂ : tensorAction g (blade j k i) = -blade i j k := by
    rw [action_oriented_blade _ _ _ _ _ (Ne.symm hpj) (Ne.symm hpk) (Ne.symm hpi), hi, hj, hk, blade_swap i j k]
  have hb₃ : tensorAction g (blade k i j) = -blade k i j := by
    rw [action_oriented_blade _ _ _ _ _ (Ne.symm hpk) (Ne.symm hpi) (Ne.symm hpj), hi, hj, hk, blade_swap k i j]
  have h := W.add_mem hmem (hW g _ hmem)
  simp only [map_add, map_smul, hb₁, hb₂, hb₃] at h
  apply basis_mem_of_scaled W _ _ (sub_ne_zero.mpr hab)
  have hd : (a - b) • diffDistinct i j k =
      (a • blade i j k + b • blade j k i + c • blade k i j) +
        (a • -blade j k i + b • -blade i j k + c • -blade k i j) := by
    rw [diffDistinct, blade_swap j k i]
    module
  rwa [hd]

private theorem triple_extract (W : Submodule ℂ VTwo) (hW : Stable W) (hsub : W ≤ hook)
    (i j k : Axis) (d : Distinct i j k) (x : VTwo) (hx : x ∈ W) (hx0 : x ≠ 0)
    (hs : ∀ t, tensorBasis.repr x t ≠ 0 → parity t = {i, j, k}) :
    ∃ i j k, Distinct i j k ∧ diffDistinct i j k ∈ W := by
  classical
  have hspan : x ∈ Submodule.span ℂ (Set.range (triple i j k)) := by
    apply basis_span_block x {i, j, k} _ hs
    intro t ht
    obtain ⟨a, ha | ha⟩ := parity_triple d ht
    · rw [ha]; exact Submodule.subset_span (Set.mem_range_self a)
    · rw [ha]; exact Submodule.neg_mem _ (Submodule.subset_span (Set.mem_range_self a))
  obtain ⟨c, rfl⟩ := (Submodule.mem_span_range_iff_exists_fun ℂ).mp hspan
  have halt := ((mem_hook _).mp (hsub hx)).1
  simp only [map_sum, map_smul, triple_alternation, ← Finset.sum_smul] at halt
  have hc : ∑ a, c a = 0 := (smul_eq_zero.mp halt).resolve_right (wedge_three_ne_zero i j k d)
  have hsum : (∑ a, c a • triple i j k a) =
      c 0 • blade i j k + c 1 • blade j k i + c 2 • blade k i j := by
    rw [Fin.sum_univ_three]; rfl
  rw [hsum] at hx hx0
  by_cases h₁ : c 0 = c 1
  · have h₂ : c 1 ≠ c 2 := by
      intro h₂
      have hz : c 2 = 0 := by
        rw [Fin.sum_univ_three, h₁, h₂] at hc
        linear_combination (1 / 3 : ℂ) * hc
      exact hx0 (by simp [h₁, h₂, hz])
    have d' : Distinct j k i := ⟨d.2.2, Ne.symm d.1, Ne.symm d.2.1⟩
    refine ⟨j, k, i, d', triple_swap_extract W hW j k i d' (c 1) (c 2) (c 0) h₂ ?_⟩
    convert hx using 1
    abel
  · exact ⟨i, j, k, d, triple_swap_extract W hW i j k d _ _ _ h₁ hx⟩

private def reflect (n : Space) : Space →ₗ[ℂ] Space :=
  LinearMap.transvection (splitMetric n) ((-2 : ℂ) • n)

private theorem reflect_apply (n x : Space) : reflect n x = x + (-2 * splitForm n x) • n := by
  change x + splitMetric n x • ((-2 : ℂ) • n) = _
  rw [splitMetric_apply, smul_smul, mul_comm]

private theorem reflect_det (n : Space) (hn : splitForm n n = 1) : (reflect n).det = -1 := by
  rw [reflect, LinearMap.transvection.det, map_smul, splitMetric_apply, hn, smul_eq_mul]
  norm_num

private theorem symmetric_metric (x y : Space) : splitMetric x y = splitMetric y x := by
  rw [splitMetric_apply, splitMetric_apply]
  apply Finset.sum_congr rfl
  intro i _
  change x (plusAxis i) * y (minusAxis i) + x (minusAxis i) * y (plusAxis i) =
    y (plusAxis i) * x (minusAxis i) + y (minusAxis i) * x (plusAxis i)
  ring

private theorem reflect_isometry (n : Space) (hn : splitForm n n = 1) (x y : Space) :
    splitForm (reflect n x) (reflect n y) = splitForm x y := by
  rw [reflect_apply, reflect_apply]
  simp only [← splitMetric_apply, LinearMap.map_add, LinearMap.map_smul, LinearMap.add_apply,
    LinearMap.smul_apply, smul_eq_mul]
  rw [symmetric_metric x n, show splitMetric n n = 1 by rw [splitMetric_apply, hn]]
  ring

private def normal (i j : Axis) : Space := (3 / 5 : ℂ) • e i + (4 / 5 : ℂ) • e j

private theorem normal_pair (i j k : Axis) : splitForm (normal i j) (e k) =
    (3 / 5 : ℂ) * (if i = k then 1 else 0) + (4 / 5 : ℂ) * (if j = k then 1 else 0) := by
  simp only [normal, ← splitMetric_apply, LinearMap.map_add, LinearMap.map_smul, LinearMap.add_apply,
    LinearMap.smul_apply, smul_eq_mul]
  rw [splitMetric_apply, splitMetric_apply, orthBasis_pair, orthBasis_pair]

private theorem normal_norm (i j : Axis) (h : i ≠ j) : splitForm (normal i j) (normal i j) = 1 := by
  conv_lhs => rw [← splitMetric_apply]
  conv_lhs => arg 2; unfold normal
  simp only [LinearMap.map_add, LinearMap.map_smul, smul_eq_mul, splitMetric_apply, normal_pair,
    if_neg h, if_neg (Ne.symm h)]
  norm_num

def rotation (i j : Axis) (h : i ≠ j) : splitSpecialOrthogonal :=
  ⟨(reflect (normal i j)).comp (reflect (e i)), by
    rw [LinearMap.det_comp, reflect_det _ (normal_norm i j h), reflect_det _ (by simp [orthBasis_pair])]
    norm_num,
   fun x y => (reflect_isometry _ (normal_norm i j h) _ _).trans
      (reflect_isometry _ (by simp [orthBasis_pair]) x y)⟩

theorem rotation_on_plane (i j : Axis) (h : i ≠ j) :
    (rotation i j h).val (e i) = (-7 / 25 : ℂ) • e i + (24 / 25 : ℂ) • e j ∧
    (rotation i j h).val (e j) = (-24 / 25 : ℂ) • e i + (-7 / 25 : ℂ) • e j := by
  have h₁ : reflect (e i) (e i) = -e i := by rw [reflect_apply, orthBasis_pair, if_pos rfl]; module
  have h₂ : reflect (e i) (e j) = e j := by simp [reflect_apply, orthBasis_pair, h]
  constructor
  · change reflect (normal i j) (reflect (e i) (e i)) = _
    rw [h₁, map_neg, reflect_apply, normal_pair, if_pos rfl, if_neg h.symm, normal]
    module
  · change reflect (normal i j) (reflect (e i) (e j)) = _
    rw [h₂, reflect_apply, normal_pair, if_neg h, if_pos rfl, normal]
    module

theorem rotation_off_plane (i j k : Axis) (h : i ≠ j) (hi : k ≠ i) (hj : k ≠ j) :
    (rotation i j h).val (e k) = e k := by
  have hk : reflect (e i) (e k) = e k := by simp [reflect_apply, orthBasis_pair, hi.symm]
  change reflect (normal i j) (reflect (e i) (e k)) = _
  rw [hk, reflect_apply, normal_pair, if_neg hi.symm, if_neg hj.symm]
  simp

private theorem rotation_basis (i j k : Axis) (d : Distinct i j k) :
    (rotation i j d.1).val (e i) = (-7 / 25 : ℂ) • e i + (24 / 25 : ℂ) • e j ∧
    (rotation i j d.1).val (e j) = (-24 / 25 : ℂ) • e i + (-7 / 25 : ℂ) • e j ∧
    (rotation i j d.1).val (e k) = e k :=
  ⟨(rotation_on_plane i j d.1).1, (rotation_on_plane i j d.1).2,
    rotation_off_plane i j k d.1 d.2.1.symm d.2.2.symm⟩

private theorem rotation_repeated (i j k : Axis) (d : Distinct i j k) :
    tensorAction (rotation i j d.1) (diffRepeated i j k) =
      (-527 / 625 : ℂ) • diffRepeated i j k + (-336 / 625 : ℂ) • diffDistinct i j k := by
  obtain ⟨hi, hj, hk⟩ := rotation_basis i j k d
  simp only [diffRepeated, diffDistinct, repeated, blade, map_sub, action_pure, hi, hj, hk,
    wedgeTwo_add_left, wedgeTwo_smul_left, add_tmul, tmul_add, ← smul_tmul', tmul_smul]
  module

private theorem rotation_distinct (i j k : Axis) (d : Distinct i j k) :
    tensorAction (rotation i j d.1) (diffDistinct i j k) =
      (336 / 625 : ℂ) • diffRepeated i j k + (-527 / 625 : ℂ) • diffDistinct i j k := by
  obtain ⟨hi, hj, hk⟩ := rotation_basis i j k d
  simp only [diffRepeated, diffDistinct, repeated, blade, map_add, action_pure, hi, hj, hk,
    wedgeTwo_add_left, wedgeTwo_smul_left, add_tmul, tmul_add, ← smul_tmul', tmul_smul]
  module

private theorem flip_differences (i j k p : Axis) (d : Distinct i j k) (hpi : p ≠ i) (hpj : p ≠ j) (hpk : p ≠ k) :
    tensorAction (doubleFlip i p) (diffRepeated i j k) = diffRepeated i j k ∧
      tensorAction (doubleFlip i p) (diffDistinct i j k) = -diffDistinct i j k := by
  let c := fun a => axisFlip i a * axisFlip p a
  have h (a : Axis) : (doubleFlip i p).val (e a) = c a • e (id a) := doubleFlip_basis _ _ _
  have hi : c i = -1 := by simp [c, axisFlip, Ne.symm hpi]
  have hj : c j = 1 := by simp [c, axisFlip, Ne.symm d.1, Ne.symm hpj]
  have hk : c k = 1 := by simp [c, axisFlip, Ne.symm d.2.1, Ne.symm hpk]
  simp only [diffRepeated, diffDistinct, repeated, map_sub, map_add, action_blade_scaled _ id c h,
    id_eq, hi, hj, hk]
  constructor <;> module

private theorem mix_differences (W : Submodule ℂ VTwo) (hW : Stable W) (i j k : Axis) (d : Distinct i j k) :
    diffRepeated i j k ∈ W ↔ diffDistinct i j k ∈ W := by
  obtain ⟨p, hpi, hpj, hpk⟩ := exists_pivot i j k d
  obtain ⟨hD, hT⟩ := flip_differences i j k p d hpi hpj hpk
  let g := rotation i j d.1
  let f := doubleFlip i p
  constructor
  · intro hx
    have hw := W.sub_mem (hW g _ hx) (hW f _ (hW g _ hx))
    change tensorAction (rotation i j d.1) (diffRepeated i j k) -
      tensorAction (doubleFlip i p) (tensorAction (rotation i j d.1) (diffRepeated i j k)) ∈ W at hw
    rw [rotation_repeated i j k d, map_add, map_smul, map_smul, hD, hT] at hw
    apply basis_mem_of_scaled W _ (-672 / 625 : ℂ) (by norm_num)
    convert hw using 1
    module
  · intro hx
    have hw := W.add_mem (hW g _ hx) (hW f _ (hW g _ hx))
    change tensorAction (rotation i j d.1) (diffDistinct i j k) +
      tensorAction (doubleFlip i p) (tensorAction (rotation i j d.1) (diffDistinct i j k)) ∈ W at hw
    rw [rotation_distinct i j k d, map_add, map_smul, map_smul, hD, hT] at hw
    apply basis_mem_of_scaled W _ (672 / 625 : ℂ) (by norm_num)
    convert hw using 1
    module

private theorem move_repeated (W : Submodule ℂ VTwo) (hW : Stable W) {i j k a b c : Axis}
    (d : Distinct i j k) (d' : Distinct a b c) (h : diffRepeated i j k ∈ W) : diffRepeated a b c ∈ W := by
  obtain ⟨σ, hσ⟩ := Equiv.Perm.exists_extending_pair ![i, j, k] ![a, b, c]
    (axes_triple_injective _ _ _ d) (axes_triple_injective _ _ _ d')
  obtain ⟨p, _, _, hpk⟩ := exists_pivot i j k d
  have hi : σ i = a := hσ 0
  have hj : σ j = b := hσ 1
  have hk : σ k = c := hσ 2
  have hw := hW (orientedPermAt σ p) _ h
  rwa [diffRepeated, map_sub, action_oriented_repeated _ _ _ _ (Ne.symm hpk),
    action_oriented_repeated _ _ _ _ (Ne.symm hpk), hi, hj, hk] at hw

private theorem some_difference (W : Submodule ℂ VTwo) (hW : Stable W) (hle : W ≤ hook) (hne : W ≠ ⊥) :
    ∃ i j k, Distinct i j k ∧ diffRepeated i j k ∈ W := by
  obtain ⟨x, s, hx, hx0, hs⟩ := block_in_submodule W hW hne
  let i := column s.2 0
  let j := column s.2 1
  by_cases hi : s.1 = i
  · have h : parity s = {j} := by
      rw [parity, columns, hi]
      simp [i, j, column_ne s.2]
    obtain ⟨a, b, hab, hw⟩ := singleton_extract W hW hle j x hx hx0 (fun t ht => (hs t ht).trans h)
    exact ⟨a, b, j, hab, hw⟩
  · by_cases hj : s.1 = j
    · have h : parity s = {i} := by
        rw [parity, columns, hj]
        change (if j ∈ ({i, j} : Finset Axis) then ({i, j} : Finset Axis).erase j else insert j {i, j}) = {i}
        rw [show ({i, j} : Finset Axis) = {j, i} from Finset.pair_comm i j]
        simp
        exact Ne.symm (column_ne s.2)
      obtain ⟨a, b, hab, hw⟩ := singleton_extract W hW hle i x hx hx0 (fun t ht => (hs t ht).trans h)
      exact ⟨a, b, i, hab, hw⟩
    · have h : parity s = {s.1, i, j} := by
        rw [parity, columns]
        simp [hi, hj, i, j]
      obtain ⟨a, b, c, d, hw⟩ := triple_extract W hW hle s.1 i j
        ⟨hi, hj, column_ne s.2⟩ x hx hx0 (fun t ht => (hs t ht).trans h)
      exact ⟨a, b, c, d, (mix_differences W hW a b c d).mpr hw⟩

private theorem residual_repeated_mem (W : Submodule ℂ VTwo)
    (hD : ∀ i j k, Distinct i j k → diffRepeated i j k ∈ W) (i k : Axis) (hik : i ≠ k) :
    residual (repeated i k) ∈ W := by
  classical
  let s := (Finset.univ : Finset Axis).erase k
  have hsum : (∑ j ∈ s, diffRepeated i j k) ∈ W := by
    apply W.sum_mem
    intro j hj
    have hjk : j ≠ k := (Finset.mem_erase.mp hj).1
    by_cases hij : i = j
    · subst j; simp [diffRepeated]
    · exact hD _ _ _ ⟨hij, hik, hjk⟩
  have hN : s.card = 13 := by
    change ((Finset.univ : Finset Axis).erase k).card = 13
    rw [Finset.card_erase_of_mem (Finset.mem_univ k), Finset.card_univ, Fintype.card_fin]
  have hS : (∑ j ∈ s, repeated j k) = ∑ j, repeated j k := by
    have he := Finset.sum_erase_add (Finset.univ : Finset Axis) (fun j => repeated j k) (Finset.mem_univ k)
    rwa [repeated_self, add_zero] at he
  have ha : alternation (repeated i k) = 0 := (alternation_pure _ _ _).trans (wedgeThree_repeat _ _)
  have hformula : residual (repeated i k) = (13 : ℂ)⁻¹ • ∑ j ∈ s, diffRepeated i j k := by
    simp only [residual, LinearMap.sub_apply, LinearMap.id_apply, LinearMap.comp_apply, ha, map_zero, sub_zero,
      trace_repeated i k hik, includeVector_apply, diffRepeated, Finset.sum_sub_distrib, Finset.sum_const, hN, hS]
    change repeated i k - (13 : ℂ)⁻¹ • (∑ j, repeated j k) = _
    rw [← Nat.cast_smul_eq_nsmul ℂ]
    module
  rw [hformula]
  exact W.smul_mem _ hsum

private theorem residual_distinct_mem (W : Submodule ℂ VTwo)
    (hT : ∀ i j k, Distinct i j k → diffDistinct i j k ∈ W) (i j k : Axis) (d : Distinct i j k) :
    residual (blade i j k) ∈ W := by
  have hformula : residual (blade i j k) = (3 : ℂ)⁻¹ • (diffDistinct i j k - diffDistinct i k j) := by
    have ha : alternation (blade i j k) = wedgeThree (e i) (e j) (e k) := alternation_pure _ _ _
    simp only [residual, LinearMap.sub_apply, LinearMap.id_apply, LinearMap.comp_apply, ha,
      trace_distinct i j k d, map_zero, sub_zero, includeThree_pure, cyclicTensor, diffDistinct]
    change blade i j k - (3 : ℂ)⁻¹ • (blade i j k + blade j k i + blade k i j) = _
    rw [blade_swap j k i, blade_swap i j k]
    module
  rw [hformula]
  exact W.smul_mem _ (W.sub_mem (hT i j k d) (hT i k j ⟨d.2.1, d.1, Ne.symm d.2.2⟩))

private theorem hook_invariant_subspace (W : Submodule ℂ VTwo) (hW : Stable W) (hle : W ≤ hook) :
    W = ⊥ ∨ W = hook := by
  by_cases hne : W = ⊥
  · exact Or.inl hne
  right
  obtain ⟨i, j, k, d, h⟩ := some_difference W hW hle hne
  have hD (a b c : Axis) (d' : Distinct a b c) : diffRepeated a b c ∈ W := move_repeated W hW d d' h
  have hT (a b c : Axis) (d' : Distinct a b c) : diffDistinct a b c ∈ W :=
    (mix_differences W hW a b c d').mp (hD a b c d')
  have hb (s : Axis × Index 2) : residual (tensorBasis s) ∈ W := by
    rw [tensorBasis_blade]
    let i := column s.2 0
    let j := column s.2 1
    have hij : i ≠ j := column_ne s.2
    change residual (blade s.1 i j) ∈ W
    by_cases hi : s.1 = i
    · rw [hi]
      exact residual_repeated_mem W hD i j hij
    · by_cases hj : s.1 = j
      · rw [hj, blade_swap j j i, map_neg]
        exact W.neg_mem (residual_repeated_mem W hD j i (Ne.symm hij))
      · exact residual_distinct_mem W hT _ _ _ ⟨hi, hj, hij⟩
  apply le_antisymm hle
  intro x hx
  have hres : residual x = x := by
    have hk := (mem_hook x).mp hx
    simp [residual, hk.1, hk.2]
  rw [← hres, ← tensorBasis.sum_repr x, map_sum]
  exact W.sum_mem fun s _ => by rw [map_smul]; exact W.smul_mem _ (hb s)

/-- The 896-dimensional joint kernel of alternation and trace is irreducible
under the complex split special orthogonal group. -/
theorem hook_isIrreducible : Representation.IsIrreducible (k := ℂ) (V := ↥hook) hookAction := by
  have : Nontrivial (↥hook) := ⟨⟨⟨hookHighest, hookHighest_mem⟩, 0, fun h =>
    hookHighest_ne_zero (congrArg Subtype.val h)⟩⟩
  apply irreducible_of_subrepresentations
  intro U
  let W : Submodule ℂ VTwo := U.toSubmodule.map hook.subtype
  have hW : Stable W := by
    intro g x hx
    obtain ⟨y, hy, rfl⟩ := Submodule.mem_map.mp hx
    exact Submodule.mem_map.mpr ⟨hookAction g y, U.apply_mem_toSubmodule g hy, rfl⟩
  have hle : W ≤ hook := by
    intro x hx
    obtain ⟨y, _, rfl⟩ := Submodule.mem_map.mp hx
    exact y.prop
  rcases hook_invariant_subspace W hW hle with h | h
  · left
    apply Subrepresentation.toSubmodule_injective
    apply Submodule.map_injective_of_injective hook.subtype_injective
    change W = (⊥ : Submodule ℂ (↥hook)).map hook.subtype
    rw [Submodule.map_bot, h]
  · right
    apply Subrepresentation.toSubmodule_injective
    apply Submodule.map_injective_of_injective hook.subtype_injective
    change W = (⊤ : Submodule ℂ (↥hook)).map hook.subtype
    rw [Submodule.map_top, Submodule.range_subtype, h]

/-- The highest-weight candidate generates the whole traceless hook. -/
theorem hookHighest_generates :
    Submodule.span ℂ (Set.range fun g => tensorAction g hookHighest) = hook := by
  let W := Submodule.span ℂ (Set.range fun g => tensorAction g hookHighest)
  have hW : Stable W := by
    intro g x hx
    have hle : W ≤ W.comap (tensorAction g) := by
      apply Submodule.span_le.mpr
      rintro _ ⟨h, rfl⟩
      exact Submodule.subset_span ⟨g * h, by
        change tensorAction (g * h) hookHighest = tensorAction g (tensorAction h hookHighest)
        rw [map_mul]
        rfl⟩
    exact hle hx
  have hle : W ≤ hook := by
    apply Submodule.span_le.mpr
    rintro _ ⟨g, rfl⟩
    exact hook_invariant g _ hookHighest_mem
  have hne : W ≠ ⊥ := by
    intro h
    have hv : hookHighest ∈ W := Submodule.subset_span ⟨1, by
      change tensorAction 1 hookHighest = hookHighest
      rw [map_one]
      rfl⟩
    rw [h, Submodule.mem_bot] at hv
    exact hookHighest_ne_zero hv
  exact (hook_invariant_subspace W hW hle).resolve_left hne

/-- The vector summand uses the same action as the first exterior power. -/
theorem vector_isIrreducible : vectorAction.IsIrreducible := by
  have : Nontrivial Space := ⟨⟨e 0, 0, e.ne_zero 0⟩⟩
  apply irreducible_of_subrepresentations
  intro U
  let f := exteriorPower.oneEquiv ℂ Space
  let W := U.toSubmodule.comap f.toLinearMap
  have hW : D7Irreducible.Stable W := by
    intro g x hx
    change f (exteriorRepresentation 1 g x) ∈ U.toSubmodule
    have h := LinearMap.congr_fun (exteriorPower.oneEquiv_naturality g.val) x
    change f (exteriorRepresentation 1 g x) = vectorAction g (f x) at h
    rw [h]
    exact U.apply_mem_toSubmodule g hx
  rcases exterior_irreducible 1 (by decide) W hW with h | h
  · left
    apply Subrepresentation.toSubmodule_injective
    apply Submodule.comap_injective_of_surjective f.surjective
    change W = (⊥ : Submodule ℂ Space).comap f.toLinearMap
    rw [h, Submodule.comap_bot, LinearMap.ker_eq_bot.mpr f.injective]
  · right
    apply Subrepresentation.toSubmodule_injective
    apply Submodule.comap_injective_of_surjective f.surjective
    change W = (⊤ : Submodule ℂ Space).comap f.toLinearMap
    rw [h, Submodule.comap_top]

end
end GeometricUnity.D7Hook
~~~

[Return to file index](#file-index)

## D7VectorGrades.lean {#source-d7vectorgrades-lean}

Constructs wedge and metric-contraction maps and their equivariant sections in all exterior degrees.

~~~lean
import D7VectorTensor
import Mathlib.LinearAlgebra.Alternating.Uncurry.Fin

/-!
# Wedge and contraction in all grades of the D₇ vector tensor product

The two maps use exterior multiplication and the split form. Their sections
come from alternating tensor insertion and the invariant metric tensor.
-/

namespace GeometricUnity.D7VectorGrades

open D7Exterior D7Hodge D7VectorTensor TensorProduct
open scoped BigOperators TensorProduct

noncomputable section

abbrev Ext (n : ℕ) := ⋀[ℂ]^n Space
abbrev Product (n : ℕ) := Space ⊗[ℂ] Ext n

def action (n : ℕ) : Representation ℂ splitSpecialOrthogonal (Product n) :=
  vectorAction.tprod (exteriorRepresentation n)

private abbrev pureWedge (n : ℕ) (v : Fin n → Space) : Ext n := exteriorPower.ιMulti ℂ n v

theorem ext_on_wedges {n : ℕ} {W : Type*} [AddCommGroup W] [Module ℂ W]
    {f g : Ext n →ₗ[ℂ] W} (h : ∀ v, f (pureWedge n v) = g (pureWedge n v)) : f = g := by
  apply exteriorPower.linearMap_ext
  exact AlternatingMap.ext h

theorem ext_on_tensor_wedges {n : ℕ} {W : Type*} [AddCommGroup W] [Module ℂ W]
    {f g : Product n →ₗ[ℂ] W}
    (h : ∀ x v, f (x ⊗ₜ[ℂ] pureWedge n v) = g (x ⊗ₜ[ℂ] pureWedge n v)) : f = g := by
  apply TensorProduct.ext'
  intro x u
  have he : f.comp (TensorProduct.mk ℂ Space (Ext n) x) =
      g.comp (TensorProduct.mk ℂ Space (Ext n) x) := ext_on_wedges (h x)
  exact DFunLike.congr_fun he u

theorem wedgeLeft_pure (n : ℕ) (x : Space) (v : Fin n → Space) :
    wedgeLeftLinear n x (pureWedge n v) = pureWedge (n + 1) (Matrix.vecCons x v) := by
  apply Subtype.ext
  change ExteriorAlgebra.ι ℂ x * ExteriorAlgebra.ιMulti ℂ n v =
    ExteriorAlgebra.ιMulti ℂ (n + 1) (Matrix.vecCons x v)
  simp only [ExteriorAlgebra.ιMulti_apply]
  rw [List.ofFn_succ, List.prod_cons]
  rfl

/-- Exterior multiplication `x ⊗ u ↦ x ∧ u`. -/
def wedge (n : ℕ) : Product n →ₗ[ℂ] Ext (n + 1) := TensorProduct.lift (wedgeLeftLinear n)

theorem wedge_pure (n : ℕ) (x : Space) (v : Fin n → Space) :
    wedge n (x ⊗ₜ[ℂ] pureWedge n v) = pureWedge (n + 1) (Matrix.vecCons x v) := by
  rw [wedge, TensorProduct.lift.tmul, wedgeLeft_pure]

private def metricAlternating (n : ℕ) :
    Space →ₗ[ℂ] Space →ₗ[ℂ] (Space [⋀^Fin n]→ₗ[ℂ] Ext n) :=
  LinearMap.mk₂ ℂ (fun x y => splitMetric x y • exteriorPower.ιMulti ℂ n)
    (fun x y z => by simp [add_smul])
    (fun c x y => by simp [smul_smul])
    (fun x y z => by simp [add_smul])
    (fun c x y => by simp [smul_smul])

private theorem metricAlternating_eval (n : ℕ) (x y : Space) (v : Fin n → Space) :
    metricAlternating n x y v = splitForm x y • pureWedge n v := by
  change splitMetric x y • pureWedge n v = _
  rw [splitMetric_apply]

private def contractAlt (n : ℕ) : Space →ₗ[ℂ] (Space [⋀^Fin (n + 1)]→ₗ[ℂ] Ext n) :=
  AlternatingMap.alternatizeUncurryFinLM.comp (metricAlternating n)

def contractLeft (n : ℕ) : Space →ₗ[ℂ] Ext (n + 1) →ₗ[ℂ] Ext n :=
  exteriorPower.alternatingMapLinearEquiv.toLinearMap.comp (contractAlt n)

/-- Metric contraction, with the alternating sign of the removed position. -/
def contract (n : ℕ) : Product (n + 1) →ₗ[ℂ] Ext n := TensorProduct.lift (contractLeft n)

theorem contract_pure (n : ℕ) (x : Space) (v : Fin (n + 1) → Space) :
    contract n (x ⊗ₜ[ℂ] pureWedge (n + 1) v) =
      ∑ i : Fin (n + 1), (-1 : ℤ) ^ i.val •
        (splitForm x (v i) • pureWedge n (i.removeNth v)) := by
  simp only [contract, TensorProduct.lift.tmul, contractLeft, LinearMap.comp_apply, LinearEquiv.coe_coe,
    exteriorPower.alternatingMapLinearEquiv_apply_ιMulti, contractAlt,
    AlternatingMap.alternatizeUncurryFinLM_apply, AlternatingMap.alternatizeUncurryFin_apply,
    metricAlternating_eval]

theorem action_tmul (n : ℕ) (g : splitSpecialOrthogonal) (x : Space) (u : Ext n) :
    action n g (x ⊗ₜ[ℂ] u) = g.val x ⊗ₜ[ℂ] exteriorPower.map n g.val u :=
  TensorProduct.map_tmul _ _ _ _

private theorem comp_vecCons (f : Space →ₗ[ℂ] Space) {n : ℕ} (x : Space) (v : Fin n → Space) :
    f ∘ Matrix.vecCons x v = Matrix.vecCons (f x) (f ∘ v) := by
  funext j
  refine Fin.cases ?_ (fun _ => ?_) j <;> rfl

theorem wedge_natural (n : ℕ) (f : Space →ₗ[ℂ] Space) :
    (wedge n).comp (TensorProduct.map f (exteriorPower.map n f)) =
      (exteriorPower.map (n + 1) f).comp (wedge n) := by
  apply ext_on_tensor_wedges
  intro x v
  simp only [LinearMap.comp_apply, TensorProduct.map_tmul, exteriorPower.map_apply_ιMulti, wedge_pure,
    comp_vecCons]

theorem wedge_equivariant (n : ℕ) (g : splitSpecialOrthogonal) :
    (wedge n).comp (action n g) = (exteriorRepresentation (n + 1) g).comp (wedge n) :=
  wedge_natural n g.val

theorem contract_natural (n : ℕ) (f : Space →ₗ[ℂ] Space)
    (hf : ∀ x y, splitForm (f x) (f y) = splitForm x y) :
    (contract n).comp (TensorProduct.map f (exteriorPower.map (n + 1) f)) =
      (exteriorPower.map n f).comp (contract n) := by
  apply ext_on_tensor_wedges
  intro x v
  simp only [LinearMap.comp_apply, TensorProduct.map_tmul, exteriorPower.map_apply_ιMulti, contract_pure,
    Function.comp_apply, hf, map_sum, map_zsmul, map_smul]
  rfl

theorem contract_equivariant (n : ℕ) (g : splitSpecialOrthogonal) :
    (contract n).comp (action (n + 1) g) = (exteriorRepresentation n g).comp (contract n) :=
  contract_natural n g.val g.prop.2

private def tensorAlternating (n : ℕ) : Space →ₗ[ℂ] (Space [⋀^Fin n]→ₗ[ℂ] Product n) where
  toFun x := (TensorProduct.mk ℂ Space (Ext n) x).compAlternatingMap (exteriorPower.ιMulti ℂ n)
  map_add' x y := by
    apply AlternatingMap.ext
    intro v
    exact TensorProduct.add_tmul _ _ _
  map_smul' c x := by
    apply AlternatingMap.ext
    intro v
    exact (TensorProduct.smul_tmul' c x (pureWedge n v)).symm

private def rawWedgeSection (n : ℕ) : Ext (n + 1) →ₗ[ℂ] Product n :=
  exteriorPower.alternatingMapLinearEquiv (AlternatingMap.alternatizeUncurryFin (tensorAlternating n))

private theorem rawWedgeSection_pure (n : ℕ) (v : Fin (n + 1) → Space) :
    rawWedgeSection n (pureWedge (n + 1) v) =
      ∑ i : Fin (n + 1), (-1 : ℤ) ^ i.val • (v i ⊗ₜ[ℂ] pureWedge n (i.removeNth v)) := by
  rw [rawWedgeSection, exteriorPower.alternatingMapLinearEquiv_apply_ιMulti,
    AlternatingMap.alternatizeUncurryFin_apply]
  rfl

private theorem wedge_rawWedgeSection (n : ℕ) :
    (wedge n).comp (rawWedgeSection n) = (n + 1 : ℂ) • LinearMap.id := by
  apply ext_on_wedges
  intro v
  simp only [LinearMap.comp_apply, rawWedgeSection_pure, map_sum, map_zsmul, wedge_pure,
    LinearMap.smul_apply, LinearMap.id_apply]
  have h (i : Fin (n + 1)) : (-1 : ℤ) ^ i.val • pureWedge (n + 1) (Matrix.vecCons (v i) (i.removeNth v)) =
      pureWedge (n + 1) v := by
    rw [← AlternatingMap.map_insertNth, Fin.insertNth_self_removeNth]
  simp only [h, Finset.sum_const, Finset.card_univ, Fintype.card_fin, ← Nat.cast_smul_eq_nsmul ℂ]
  norm_cast

private theorem rawWedgeSection_equivariant (n : ℕ) (g : splitSpecialOrthogonal) :
    (rawWedgeSection n).comp (exteriorRepresentation (n + 1) g) = (action n g).comp (rawWedgeSection n) := by
  apply ext_on_wedges
  intro v
  change rawWedgeSection n (exteriorPower.map (n + 1) g.val (pureWedge (n + 1) v)) = _
  simp only [exteriorPower.map_apply_ιMulti, rawWedgeSection_pure, LinearMap.comp_apply,
    map_sum, map_zsmul, action_tmul, Function.comp_apply]
  rfl

/-- Section of the wedge map normalized by the number of exterior slots. -/
def includeWedge (n : ℕ) : Ext (n + 1) →ₗ[ℂ] Product n := (n + 1 : ℂ)⁻¹ • rawWedgeSection n

theorem includeWedge_pure (n : ℕ) (v : Fin (n + 1) → Space) :
    includeWedge n (pureWedge (n + 1) v) = (n + 1 : ℂ)⁻¹ •
      ∑ i : Fin (n + 1), (-1 : ℤ) ^ i.val • (v i ⊗ₜ[ℂ] pureWedge n (i.removeNth v)) := by
  rw [includeWedge, LinearMap.smul_apply, rawWedgeSection_pure]

theorem wedge_includeWedge (n : ℕ) : (wedge n).comp (includeWedge n) = LinearMap.id := by
  have hn : (n + 1 : ℂ) ≠ 0 := by exact_mod_cast Nat.succ_ne_zero n
  rw [includeWedge, LinearMap.comp_smul, wedge_rawWedgeSection, smul_smul, inv_mul_cancel₀ hn, one_smul]

theorem includeWedge_equivariant (n : ℕ) (g : splitSpecialOrthogonal) :
    (includeWedge n).comp (exteriorRepresentation (n + 1) g) = (action n g).comp (includeWedge n) := by
  rw [includeWedge, LinearMap.smul_comp, LinearMap.comp_smul, rawWedgeSection_equivariant]

theorem contract_includeWedge (n : ℕ) : (contract n).comp (includeWedge (n + 1)) = 0 := by
  rw [includeWedge, LinearMap.comp_smul]
  suffices (contract n).comp (rawWedgeSection (n + 1)) = 0 by rw [this, smul_zero]
  apply ext_on_wedges
  intro v
  have hs (x y : Space) : metricAlternating n x y = metricAlternating n y x := by
    apply AlternatingMap.ext
    intro w
    rw [metricAlternating_eval, metricAlternating_eval, splitForm_symm x y]
  have h := DFunLike.congr_fun
    (AlternatingMap.alternatizeUncurryFin_alternatizeUncurryFinLM_comp_of_symmetric hs) v
  simpa only [AlternatingMap.alternatizeUncurryFin_apply, LinearMap.comp_apply,
    AlternatingMap.alternatizeUncurryFinLM_apply, metricAlternating_eval, AlternatingMap.zero_apply,
    rawWedgeSection_pure, map_sum, map_zsmul, contract_pure, LinearMap.zero_apply]
    using (show (AlternatingMap.alternatizeUncurryFin
      (AlternatingMap.alternatizeUncurryFinLM.comp (metricAlternating n))) v = 0 from h)

theorem contractLeft_pure (n : ℕ) (x : Space) (v : Fin (n + 1) → Space) :
    contractLeft n x (pureWedge (n + 1) v) =
      ∑ i : Fin (n + 1), (-1 : ℤ) ^ i.val •
        (splitForm x (v i) • pureWedge n (i.removeNth v)) := by
  have h := contract_pure n x v
  rw [contract, TensorProduct.lift.tmul] at h
  exact h

private theorem remove_vecCons {n : ℕ} (i : Fin (n + 1)) (y : Space) (v : Fin (n + 1) → Space) :
    i.succ.removeNth (Matrix.vecCons y v) = Matrix.vecCons y (i.removeNth v) :=
  Fin.cons_comp_succ_succAbove y v i

theorem contract_wedgeLeft (n : ℕ) (x y : Space) (u : Ext (n + 1)) :
    contractLeft (n + 1) x (wedgeLeftLinear (n + 1) y u) =
      splitForm x y • u - wedgeLeftLinear n y (contractLeft n x u) := by
  have h : (contractLeft (n + 1) x).comp (wedgeLeftLinear (n + 1) y) =
      splitForm x y • LinearMap.id - (wedgeLeftLinear n y).comp (contractLeft n x) := by
    apply ext_on_wedges
    intro v
    simp only [LinearMap.comp_apply, LinearMap.sub_apply, LinearMap.smul_apply, LinearMap.id_apply,
      wedgeLeft_pure, contractLeft_pure]
    rw [Fin.sum_univ_succ]
    simp only [Fin.val_zero, pow_zero, one_zsmul, Fin.removeNth_zero,
      Matrix.vecCons, Fin.tail_cons, Fin.val_succ, pow_succ, mul_neg_one,
      neg_zsmul, map_sum, map_zsmul, map_smul]
    rw [sub_eq_add_neg, ← Finset.sum_neg_distrib]
    congr 1
    apply Finset.sum_congr rfl
    intro i _
    rw [wedgeLeft_pure]
    have he := remove_vecCons i y v
    simp only [Matrix.vecCons] at he ⊢
    rw [Fin.cons_succ, he]
  exact DFunLike.congr_fun h u

theorem contract_wedgeLeft_zero (x y : Space) (u : Ext 0) :
    contractLeft 0 x (wedgeLeftLinear 0 y u) = splitForm x y • u := by
  have h : (contractLeft 0 x).comp (wedgeLeftLinear 0 y) = splitForm x y • LinearMap.id := by
    apply ext_on_wedges
    intro v
    simp only [LinearMap.comp_apply, LinearMap.smul_apply, LinearMap.id_apply, wedgeLeft_pure,
      contractLeft_pure]
    rw [Fin.sum_univ_succ]
    simp
  exact DFunLike.congr_fun h u

private theorem wedge_contract_sum (n : ℕ) (u : Ext (n + 1)) :
    (∑ a : Axis, wedgeLeftLinear n (orthBasis a) (contractLeft n (orthBasis a) u)) = (n + 1 : ℂ) • u := by
  have h : (∑ a : Axis, (wedgeLeftLinear n (orthBasis a)).comp (contractLeft n (orthBasis a))) =
      (n + 1 : ℂ) • (LinearMap.id : Ext (n + 1) →ₗ[ℂ] Ext (n + 1)) := by
    apply ext_on_wedges
    intro v
    simp only [LinearMap.sum_apply, LinearMap.comp_apply, LinearMap.smul_apply, LinearMap.id_apply,
      contractLeft_pure, map_sum, map_zsmul, map_smul]
    rw [Finset.sum_comm]
    have he (i : Fin (n + 1)) :
        (∑ a : Axis, splitForm (orthBasis a) (v i) •
          wedgeLeftLinear n (orthBasis a) (pureWedge n (i.removeNth v))) =
        wedgeLeftLinear n (v i) (pureWedge n (i.removeNth v)) := by
      conv_rhs => rw [← orth_sum (v i)]
      simp only [map_sum, map_smul, LinearMap.sum_apply, LinearMap.smul_apply]
    simp only [← Finset.smul_sum, he]
    simp only [wedgeLeft_pure, ← AlternatingMap.map_insertNth,
      Fin.insertNth_self_removeNth, Finset.sum_const, Finset.card_univ, Fintype.card_fin,
      ← Nat.cast_smul_eq_nsmul ℂ]
    norm_cast
  simpa only [LinearMap.sum_apply, LinearMap.comp_apply, LinearMap.smul_apply, LinearMap.id_apply]
    using DFunLike.congr_fun h u

private def rawMetricSection (n : ℕ) : Ext n →ₗ[ℂ] Product (n + 1) :=
  ∑ a : Axis, (TensorProduct.mk ℂ Space (Ext (n + 1)) (orthBasis a)).comp
    (wedgeLeftLinear n (orthBasis a))

private theorem rawMetricSection_apply (n : ℕ) (u : Ext n) : rawMetricSection n u =
    ∑ a : Axis, orthBasis a ⊗ₜ[ℂ] wedgeLeftLinear n (orthBasis a) u := by
  simp only [rawMetricSection, LinearMap.sum_apply, LinearMap.comp_apply, TensorProduct.mk_apply]

private theorem contract_rawMetricSection (n : ℕ) :
    (contract n).comp (rawMetricSection n) = (14 - (n : ℂ)) • LinearMap.id := by
  apply LinearMap.ext
  intro u
  simp only [LinearMap.comp_apply, rawMetricSection_apply, LinearMap.smul_apply, LinearMap.id_apply,
    map_sum, contract, TensorProduct.lift.tmul]
  cases n with
  | zero =>
    simp only [contract_wedgeLeft_zero, orthBasis_pair, if_true, one_smul, Finset.sum_const,
      Finset.card_univ, Fintype.card_fin, Nat.cast_zero, sub_zero, ← Nat.cast_smul_eq_nsmul ℂ]
    norm_cast
  | succ n =>
    simp only [contract_wedgeLeft, Finset.sum_sub_distrib, orthBasis_pair, if_true, one_smul,
      Finset.sum_const, Finset.card_univ, Fintype.card_fin, wedge_contract_sum,
      ← Nat.cast_smul_eq_nsmul ℂ, Nat.cast_succ]
    module

private theorem wedge_rawMetricSection (n : ℕ) : (wedge (n + 1)).comp (rawMetricSection n) = 0 := by
  apply LinearMap.ext
  intro u
  simp only [LinearMap.comp_apply, rawMetricSection_apply, map_sum, wedge, TensorProduct.lift.tmul,
    LinearMap.zero_apply]
  apply Finset.sum_eq_zero
  intro i _
  apply Subtype.ext
  change ExteriorAlgebra.ι ℂ (orthBasis i) * (ExteriorAlgebra.ι ℂ (orthBasis i) * u.val) = 0
  rw [← mul_assoc, ExteriorAlgebra.ι_sq_zero, zero_mul]

theorem wedgeLeft_naturality (n : ℕ) (g : splitSpecialOrthogonal) (x : Space) (u : Ext n) :
    exteriorPower.map (n + 1) g.val (wedgeLeftLinear n x u) =
      wedgeLeftLinear n (g.val x) (exteriorPower.map n g.val u) := by
  have h := DFunLike.congr_fun (wedge_equivariant n g) (x ⊗ₜ[ℂ] u)
  change wedge n (action n g (x ⊗ₜ[ℂ] u)) = exteriorPower.map (n + 1) g.val (wedge n (x ⊗ₜ[ℂ] u)) at h
  simpa only [LinearMap.comp_apply, action_tmul, wedge, TensorProduct.lift.tmul] using h.symm

theorem contractLeft_naturality (n : ℕ) (g : splitSpecialOrthogonal) (x : Space) (u : Ext (n + 1)) :
    exteriorPower.map n g.val (contractLeft n x u) =
      contractLeft n (g.val x) (exteriorPower.map (n + 1) g.val u) := by
  have h := DFunLike.congr_fun (contract_equivariant n g) (x ⊗ₜ[ℂ] u)
  change contract n (action (n + 1) g (x ⊗ₜ[ℂ] u)) = exteriorPower.map n g.val (contract n (x ⊗ₜ[ℂ] u)) at h
  simpa only [LinearMap.comp_apply, action_tmul, contract, TensorProduct.lift.tmul] using h.symm

private def insertMetric {n : ℕ} (u : Ext n) : Space ⊗[ℂ] Space →ₗ[ℂ] Product (n + 1) :=
  TensorProduct.map LinearMap.id ((wedgeLeftLinear n).flip u)

private theorem insertMetric_metricTensor {n : ℕ} (u : Ext n) :
    insertMetric u metricTensor = rawMetricSection n u := by
  simp only [insertMetric, metricTensor, rawMetricSection_apply, map_sum, TensorProduct.map_tmul,
    LinearMap.id_apply, LinearMap.flip_apply]

private theorem rawMetricSection_equivariant (n : ℕ) (g : splitSpecialOrthogonal) :
    (rawMetricSection n).comp (exteriorRepresentation n g) = (action (n + 1) g).comp (rawMetricSection n) := by
  apply LinearMap.ext
  intro u
  have h : (action (n + 1) g).comp (insertMetric u) =
      (insertMetric (exteriorPower.map n g.val u)).comp (TensorProduct.map g.val g.val) := by
    apply TensorProduct.ext'
    intro x y
    simp only [LinearMap.comp_apply, insertMetric, TensorProduct.map_tmul, LinearMap.id_apply,
      LinearMap.flip_apply, action_tmul, wedgeLeft_naturality]
  have he := DFunLike.congr_fun h metricTensor
  change (rawMetricSection n) (exteriorPower.map n g.val u) = action (n + 1) g (rawMetricSection n u)
  simpa only [LinearMap.comp_apply, metricTensor_invariant, insertMetric_metricTensor] using he.symm

/-- The section through the metric tensor. The normalization is nonzero for
`n < 14`, which covers tensor input degrees one through fourteen. -/
def includeMetric (n : ℕ) : Ext n →ₗ[ℂ] Product (n + 1) := (14 - (n : ℂ))⁻¹ • rawMetricSection n

theorem includeMetric_apply (n : ℕ) (u : Ext n) : includeMetric n u =
    (14 - (n : ℂ))⁻¹ • ∑ i : Axis, orthBasis i ⊗ₜ[ℂ] wedgeLeftLinear n (orthBasis i) u := by
  rw [includeMetric, LinearMap.smul_apply, rawMetricSection_apply]

theorem contract_includeMetric (n : ℕ) (hn : n < 14) : (contract n).comp (includeMetric n) = LinearMap.id := by
  have h : (14 - (n : ℂ)) ≠ 0 := sub_ne_zero.mpr (by exact_mod_cast (Nat.ne_of_lt hn).symm)
  rw [includeMetric, LinearMap.comp_smul, contract_rawMetricSection, smul_smul, inv_mul_cancel₀ h, one_smul]

theorem wedge_includeMetric (n : ℕ) : (wedge (n + 1)).comp (includeMetric n) = 0 := by
  rw [includeMetric, LinearMap.comp_smul, wedge_rawMetricSection, smul_zero]

theorem includeMetric_equivariant (n : ℕ) (g : splitSpecialOrthogonal) :
    (includeMetric n).comp (exteriorRepresentation n g) = (action (n + 1) g).comp (includeMetric n) := by
  rw [includeMetric, LinearMap.smul_comp, LinearMap.comp_smul, rawMetricSection_equivariant]

/-- The residual representation in input degree `n + 1`. -/
def jointKernel (n : ℕ) : Submodule ℂ (Product (n + 1)) := (wedge (n + 1)).ker ⊓ (contract n).ker

theorem mem_jointKernel (n : ℕ) (x : Product (n + 1)) :
    x ∈ jointKernel n ↔ wedge (n + 1) x = 0 ∧ contract n x = 0 := by
  simp [jointKernel, LinearMap.mem_ker]

theorem jointKernel_invariant (n : ℕ) (g : splitSpecialOrthogonal) (x : Product (n + 1))
    (hx : x ∈ jointKernel n) : action (n + 1) g x ∈ jointKernel n := by
  rw [mem_jointKernel] at hx ⊢
  have hw := DFunLike.congr_fun (wedge_equivariant (n + 1) g) x
  have hc := DFunLike.congr_fun (contract_equivariant n g) x
  simp only [LinearMap.comp_apply, hx.1, hx.2, map_zero] at hw hc
  exact ⟨hw, hc⟩

def jointKernelAction (n : ℕ) : Representation ℂ splitSpecialOrthogonal (jointKernel n) :=
  (action (n + 1)).subrepresentation (jointKernel n) (fun g x hx => jointKernel_invariant n g x hx)

private theorem wedge_section_eval (n : ℕ) (x : Ext (n + 1)) : wedge n (includeWedge n x) = x :=
  LinearMap.congr_fun (wedge_includeWedge n) x

private theorem contract_wedge_section_eval (n : ℕ) (x : Ext (n + 2)) : contract n (includeWedge (n + 1) x) = 0 :=
  LinearMap.congr_fun (contract_includeWedge n) x

private theorem contract_metric_section_eval (n : ℕ) (hn : n < 14) (x : Ext n) :
    contract n (includeMetric n x) = x := by
  have h := LinearMap.congr_fun (contract_includeMetric n hn) x
  simpa only [LinearMap.comp_apply, LinearMap.id_apply] using h

private theorem wedge_metric_section_eval (n : ℕ) (x : Ext n) : wedge (n + 1) (includeMetric n x) = 0 := by
  have h := LinearMap.congr_fun (wedge_includeMetric n) x
  simpa only [LinearMap.comp_apply, LinearMap.zero_apply] using h

private def remainder (n : ℕ) : Product (n + 1) →ₗ[ℂ] Product (n + 1) :=
  LinearMap.id - (includeWedge (n + 1)).comp (wedge (n + 1)) - (includeMetric n).comp (contract n)

private theorem remainder_mem (n : ℕ) (hn : n < 14) (x : Product (n + 1)) : remainder n x ∈ jointKernel n := by
  simp [mem_jointKernel, remainder, wedge_section_eval, wedge_metric_section_eval,
    contract_wedge_section_eval, contract_metric_section_eval n hn]

def splitLinear (n : ℕ) (hn : n < 14) : Product (n + 1) ≃ₗ[ℂ] Ext (n + 2) × Ext n × jointKernel n where
  toFun x := (wedge (n + 1) x, contract n x, ⟨remainder n x, remainder_mem n hn x⟩)
  invFun p := includeWedge (n + 1) p.1 + includeMetric n p.2.1 + p.2.2.val
  left_inv x := by
    change includeWedge (n + 1) (wedge (n + 1) x) + includeMetric n (contract n x) + remainder n x = x
    simp only [remainder, LinearMap.sub_apply, LinearMap.id_apply, LinearMap.comp_apply]
    abel
  right_inv p := by
    rcases p with ⟨u, v, w⟩
    have hw := (mem_jointKernel n w.val).mp w.prop
    refine Prod.ext ?_ (Prod.ext ?_ (Subtype.ext ?_))
    · change wedge (n + 1) (includeWedge (n + 1) u + includeMetric n v + w.val) = u
      simp [wedge_section_eval, wedge_metric_section_eval, hw.1]
    · change contract n (includeWedge (n + 1) u + includeMetric n v + w.val) = v
      simp [contract_wedge_section_eval, contract_metric_section_eval n hn, hw.2]
    · change remainder n (includeWedge (n + 1) u + includeMetric n v + w.val) = w.val
      simp [remainder, wedge_section_eval, wedge_metric_section_eval, contract_wedge_section_eval,
        contract_metric_section_eval n hn, hw.1, hw.2]
      abel
  map_add' x y := Prod.ext ((wedge (n + 1)).map_add x y)
    (Prod.ext ((contract n).map_add x y) (Subtype.ext ((remainder n).map_add x y)))
  map_smul' c x := Prod.ext ((wedge (n + 1)).map_smul c x)
    (Prod.ext ((contract n).map_smul c x) (Subtype.ext ((remainder n).map_smul c x)))

private theorem splitLinear_equivariant (n : ℕ) (hn : n < 14) (g : splitSpecialOrthogonal) (x : Product (n + 1)) :
    splitLinear n hn (action (n + 1) g x) =
      ((exteriorRepresentation (n + 2)).prod ((exteriorRepresentation n).prod (jointKernelAction n))) g
        (splitLinear n hn x) := by
  have hw := DFunLike.congr_fun (wedge_equivariant (n + 1) g) x
  have hc := DFunLike.congr_fun (contract_equivariant n g) x
  simp only [LinearMap.comp_apply] at hw hc
  refine Prod.ext hw (Prod.ext hc (Subtype.ext ?_))
  change remainder n (action (n + 1) g x) = action (n + 1) g (remainder n x)
  simp only [remainder, LinearMap.sub_apply, LinearMap.comp_apply, LinearMap.id_apply, hw, hc, map_sub]
  have h₁ := DFunLike.congr_fun (includeWedge_equivariant (n + 1) g) (wedge (n + 1) x)
  have h₂ := DFunLike.congr_fun (includeMetric_equivariant n g) (contract n x)
  simp only [LinearMap.comp_apply] at h₁ h₂
  rw [h₁, h₂]

/-- Equivariant wedge, contraction, and joint-kernel decomposition in every
positive exterior input degree up to fourteen. -/
def splitRepresentation (n : ℕ) (hn : n < 14) :
    (action (n + 1)).Equiv ((exteriorRepresentation (n + 2)).prod
      ((exteriorRepresentation n).prod (jointKernelAction n))) :=
  Representation.Equiv.mk (splitLinear n hn) (fun g => LinearMap.ext (splitLinear_equivariant n hn g))

set_option backward.isDefEq.respectTransparency false in
theorem jointKernel_finrank (n : ℕ) (hn : n < 14) : Module.finrank ℂ (jointKernel n) =
    14 * Nat.choose 14 (n + 1) - Nat.choose 14 (n + 2) - Nat.choose 14 n := by
  let : Module.Free ℂ (↥(jointKernel n)) := Module.Free.of_divisionRing ℂ (↥(jointKernel n))
  have h := (splitLinear n hn).finrank_eq
  rw [Module.finrank_tensorProduct, Module.finrank_prod, Module.finrank_prod,
    exteriorPower.finrank_eq, exteriorPower.finrank_eq, exteriorPower.finrank_eq,
    Module.finrank_pi, Fintype.card_fin] at h
  omega

/-- Degree zero gives the vector representation via multiplication by the scalar wedge. -/
def degreeZero : (action 0).Equiv vectorAction := by
  let f : Product 0 ≃ₗ[ℂ] Space :=
    (TensorProduct.congr (LinearEquiv.refl ℂ Space) (exteriorPower.zeroEquiv ℂ Space)).trans
      (TensorProduct.rid ℂ Space)
  refine Representation.Equiv.mk f fun g => TensorProduct.ext' fun x u => ?_
  have h := DFunLike.congr_fun (exteriorPower.zeroEquiv_naturality g.val) u
  change exteriorPower.zeroEquiv ℂ Space (exteriorPower.map 0 g.val u) = exteriorPower.zeroEquiv ℂ Space u at h
  simp only [LinearMap.comp_apply, LinearEquiv.coe_coe, f, action_tmul, LinearEquiv.trans_apply,
    TensorProduct.congr_tmul, LinearEquiv.refl_apply, TensorProduct.rid_tmul, map_smul, h]
  rfl

/-- In degree two, applying the canonical degree-one identification to the
uniform contraction gives the trace already used in the hook proof. -/
theorem degreeTwo_contract : (exteriorPower.oneEquiv ℂ Space).toLinearMap.comp (contract 1) = trace := by
  apply ext_on_tensor_wedges
  intro x v
  have hv : (![v 0, v 1] : Fin 2 → Space) = v := by funext i; fin_cases i <;> rfl
  simp only [LinearMap.comp_apply, contract_pure, LinearEquiv.coe_coe, map_sum, map_zsmul, map_smul,
    exteriorPower.oneEquiv_ιMulti]
  conv_rhs => rw [← hv]
  change _ = trace (x ⊗ₜ[ℂ] wedgeTwo (v 0) (v 1))
  rw [trace_pure]
  simp [Fin.removeNth, Fin.succAbove, sub_eq_add_neg]

theorem degreeTwo_jointKernel : jointKernel 1 = hook := by
  ext x
  rw [mem_jointKernel, mem_hook]
  have ht := DFunLike.congr_fun degreeTwo_contract x
  change exteriorPower.oneEquiv ℂ Space (contract 1 x) = trace x at ht
  rw [← ht, (exteriorPower.oneEquiv ℂ Space).map_eq_zero_iff]
  rfl

private abbrev firstAxis : Space := axisBasis (plusAxis 0)

/-- The tensor of the first positive null axis with a null-basis wedge. -/
def nullTensor {k : ℕ} (s : Index k) : Product k := firstAxis ⊗ₜ[ℂ] axisBasis.exteriorPower k s

theorem nullTensor_ne_zero {k : ℕ} (s : Index k) : nullTensor s ≠ 0 := by
  simpa only [nullTensor, Module.Basis.tensorProduct_apply'] using
    (axisBasis.tensorProduct (axisBasis.exteriorPower k)).ne_zero (plusAxis 0, s)

theorem nullTensor_mem_jointKernel (n : ℕ) (s : Index (n + 1)) (hp : plusAxis 0 ∈ s.val)
    (hm : minusAxis 0 ∉ s.val) : nullTensor s ∈ jointKernel n := by
  rw [mem_jointKernel]
  let a := Set.powersetCard.ofFinEmbEquiv.symm s
  have hmem (i : Fin (n + 1)) : a i ∈ s.val := Finset.orderEmbOfFin_mem s.val s.prop i
  have hb : nullTensor s = firstAxis ⊗ₜ[ℂ] pureWedge (n + 1) (axisBasis ∘ a) := by
    rw [nullTensor, exteriorPower.basis_apply, exteriorPower.ιMulti_family]
  rw [hb]
  constructor
  · rw [wedge_pure]
    change plusAxis 0 ∈ s at hp
    obtain ⟨i, hi⟩ := (Set.powersetCard.mem_range_ofFinEmbEquiv_symm_iff_mem s _).mpr hp
    change a i = plusAxis 0 at hi
    exact (exteriorPower.ιMulti ℂ (n + 2)).map_eq_zero_of_eq _ (i := 0) (j := i.succ)
      (show firstAxis = axisBasis (a i) by rw [hi]) (Ne.symm (Fin.succ_ne_zero i))
  · rw [contract_pure]
    apply Finset.sum_eq_zero
    intro i _
    have hi : a i ≠ minusAxis 0 := fun e => hm (e ▸ hmem i)
    have h : splitForm firstAxis (axisBasis (a i)) = 0 := by
      rw [← splitMetric_apply, splitMetric_null_plus, Module.Basis.coord_apply,
        Module.Basis.repr_self, Finsupp.single_apply, if_neg hi]
    simp only [Function.comp_apply, h, zero_smul, smul_zero]

def nullTensorWeight {k : ℕ} (s : Index k) (i : Pair) : ℤ :=
  axisWeight (plusAxis 0) i + subsetWeight s.val i

theorem nullTensor_torus {k : ℕ} (s : Index k) (t : Pair → ℂˣ) :
    action k (torusElement t) (nullTensor s) =
      ((∏ i : Pair, t i ^ nullTensorWeight s i : ℂˣ) : ℂ) • nullTensor s := by
  rw [nullTensor, action_tmul]
  change torus t firstAxis ⊗ₜ[ℂ] exteriorPower.map k (torus t) (axisBasis.exteriorPower k s) = _
  rw [torus_axis, torus_exterior, smul_tmul_smul]
  congr 1
  rw [← Units.val_mul]
  congr 1
  have h := subset_character t ({plusAxis 0} : Finset Axis)
  rw [Finset.prod_singleton] at h
  simp only [subsetWeight, Finset.sum_singleton] at h
  simp only [nullTensorWeight, zpow_add, Finset.prod_mul_distrib, ← h]

private theorem nullTensor_fixed {k : ℕ} (s : Index k) (g : splitSpecialOrthogonal)
    (hx : g.val firstAxis = firstAxis)
    (hw : exteriorRepresentation k g (axisBasis.exteriorPower k s) = axisBasis.exteriorPower k s) :
    action k g (nullTensor s) = nullTensor s := by
  rw [nullTensor, action_tmul, hx]
  change firstAxis ⊗ₜ[ℂ] exteriorRepresentation k g (axisBasis.exteriorPower k s) = _
  rw [hw]

/-- Positive input degrees with a nontrivial joint kernel. -/
def internalGrade (n : Fin 13) : Fin 15 := ⟨n.val + 1, by omega⟩

theorem internalGrade_candidate (n : Fin 13) :
    nullTensor (highestPlus (internalGrade n)) ∈ jointKernel n.val := by
  have hp : ∀ n : Fin 13, plusAxis 0 ∈ (highestPlus (internalGrade n)).val := by decide +kernel
  have hm : ∀ n : Fin 13, minusAxis 0 ∉ (highestPlus (internalGrade n)).val := by decide +kernel
  exact nullTensor_mem_jointKernel n.val (highestPlus (internalGrade n)) (hp n) (hm n)

theorem internalGrade_label : ∀ n : Fin 13,
    List.ofFn (nullTensorWeight (highestPlus (internalGrade n))) =
      D7Counts.nu (min (n.val + 1) (13 - n.val)) := by
  decide +kernel

theorem internalGrade_candidate_fixed (n : Fin 13) (c : ℂ) (i j : Pair) (h : i < j) :
    action (n.val + 1) (rootMinusElement c i j h) (nullTensor (highestPlus (internalGrade n))) =
        nullTensor (highestPlus (internalGrade n)) ∧
      action (n.val + 1) (rootPlusElement c i j h) (nullTensor (highestPlus (internalGrade n))) =
        nullTensor (highestPlus (internalGrade n)) := by
  have ha := firstAxis_root_fixed c i j h
  have hw := highestPlus_root_fixed (internalGrade n) c i j h
  exact ⟨nullTensor_fixed _ _ ha.1 hw.1, nullTensor_fixed _ _ ha.2 hw.2⟩

theorem middleMinus_candidate : nullTensor lastMinus ∈ jointKernel 6 :=
  nullTensor_mem_jointKernel 6 lastMinus (by decide +kernel) (by decide +kernel)

theorem middleMinus_label : List.ofFn (nullTensorWeight lastMinus) = D7Counts.nuMinus := by
  decide +kernel

theorem middleMinus_candidate_fixed (c : ℂ) (i j : Pair) (h : i < j) :
    action 7 (rootMinusElement c i j h) (nullTensor lastMinus) = nullTensor lastMinus ∧
      action 7 (rootPlusElement c i j h) (nullTensor lastMinus) = nullTensor lastMinus := by
  have ha := firstAxis_root_fixed c i j h
  have hw := lastMinus_root_fixed c i j h
  exact ⟨nullTensor_fixed _ _ ha.1 hw.1, nullTensor_fixed _ _ ha.2 hw.2⟩

/-- The numerical Weyl products of the candidate labels exhaust the rank of
the joint kernel. Degree seven contributes both signed labels. -/
theorem candidate_products_eq_jointKernel_finrank (n : Fin 13) :
    (Module.finrank ℂ (jointKernel n.val) : ℚ) =
      weylProduct (D7Counts.nu (min (n.val + 1) (13 - n.val))) +
        (if n.val = 6 then weylProduct D7Counts.nuMinus else 0) := by
  rw [jointKernel_finrank n.val (by omega)]
  have h : ∀ n : Fin 13,
      ((14 * Nat.choose 14 (n.val + 1) - Nat.choose 14 (n.val + 2) - Nat.choose 14 n.val : ℕ) : ℚ) =
        weylProduct (D7Counts.nu (min (n.val + 1) (13 - n.val))) +
          (if n.val = 6 then weylProduct D7Counts.nuMinus else 0) := by decide +kernel
  exact h n

set_option maxRecDepth 4096 in
set_option maxHeartbeats 2000000 in
/-- The signed vector-product table in all fifteen degrees. The exterior
labels are those of the two split summands, and the residual labels are the
checked highest-weight candidates. -/
theorem vector_grade_multiplicities : ∀ k : Fin 15,
    D7Counts.gradeMultiplicities 1 k.val = D7Counts.tally
      ((if k.val = 0 then D7Counts.gradeWeights 1 else
        D7Counts.gradeWeights (k.val + 1) ++ D7Counts.gradeWeights (k.val - 1) ++
          (if k.val = 14 then [] else if k.val = 7 then [D7Counts.nu 7, D7Counts.nuMinus]
            else [D7Counts.nu (min k.val (14 - k.val))])).map (·, 1)) := by
  decide +kernel

end
end GeometricUnity.D7VectorGrades
~~~

[Return to file index](#file-index)

## D7MiddleTensor.lean {#source-d7middletensor-lean}

Constructs the two signed residual summands in the middle degree.

~~~lean
import D7VectorGrades

/-!
# The two signed residual summands in degree seven

The middle Hodge involution exchanges the wedge and contraction constraints.
The exchange uses the adjointness of wedge and contraction for the determinant
metric and the vanishing of a fifteen-fold alternating form in dimension fourteen.
-/

namespace GeometricUnity.D7MiddleTensor

open D7Exterior D7Hodge D7VectorGrades TensorProduct
open scoped BigOperators TensorProduct

noncomputable section

private abbrev pureWedge (n : ℕ) (v : Fin n → Space) : Ext n := exteriorPower.ιMulti ℂ n v

private theorem exteriorMetric_symm (n : ℕ) (u v : Ext n) : exteriorMetric n u v = exteriorMetric n v u := by
  have h : exteriorMetric n = (exteriorMetric n).flip := by
    apply ext_on_wedges
    intro a
    apply ext_on_wedges
    intro b
    simp only [LinearMap.flip_apply, exteriorMetric_pure]
    rw [← Matrix.det_transpose]
    congr 1
    ext i j
    exact D7VectorTensor.splitForm_symm _ _
  exact DFunLike.congr_fun (DFunLike.congr_fun h u) v

/-- With the determinant metric, left wedging by a vector is adjoint to
contraction by that vector. The expansion is along the first column. -/
theorem wedge_contract_adjoint (n : ℕ) (x : Space) (u : Ext n) (v : Ext (n + 1)) :
    exteriorMetric (n + 1) (D7VectorTensor.wedgeLeftLinear n x u) v =
      exteriorMetric n u (contractLeft n x v) := by
  have h : (exteriorMetric (n + 1)).comp (D7VectorTensor.wedgeLeftLinear n x) =
      (((exteriorMetric n).flip.comp (contractLeft n x)).flip) := by
    apply ext_on_wedges
    intro a
    apply ext_on_wedges
    intro b
    simp only [LinearMap.comp_apply, LinearMap.flip_apply, wedgeLeft_pure, exteriorMetric_pure,
      contractLeft_pure, map_sum, map_zsmul, map_smul, LinearMap.sum_apply, LinearMap.smul_apply]
    rw [Matrix.det_succ_column_zero]
    apply Finset.sum_congr rfl
    intro i _
    simp only [← Int.cast_smul_eq_zsmul ℂ, Int.cast_pow, Int.cast_neg, Int.cast_one, smul_eq_mul]
    rw [mul_assoc]
    rfl
  exact DFunLike.congr_fun (DFunLike.congr_fun h u) v

private def multiplyValue (m n : ℕ) (u : Ext m) (v : Ext n) : Ext (m + n) :=
  ⟨u.val * v.val, by
    change u.val * v.val ∈ (LinearMap.range (ExteriorAlgebra.ι ℂ : Space →ₗ[ℂ] _)) ^ (m + n)
    rw [pow_add]
    exact Submodule.mul_mem_mul u.prop v.prop⟩

def multiply (m n : ℕ) : Ext m →ₗ[ℂ] Ext n →ₗ[ℂ] Ext (m + n) :=
  LinearMap.mk₂ ℂ (multiplyValue m n)
    (fun _ _ _ => Subtype.ext (add_mul _ _ _))
    (fun _ _ _ => Subtype.ext (smul_mul_assoc _ _ _))
    (fun _ _ _ => Subtype.ext (mul_add _ _ _))
    (fun _ _ _ => Subtype.ext (mul_smul_comm _ _ _))

theorem multiply_pure (m n : ℕ) (u : Fin m → Space) (v : Fin n → Space) :
    multiply m n (pureWedge m u) (pureWedge n v) = pureWedge (m + n) (Fin.append u v) :=
  Subtype.ext (ExteriorAlgebra.ιMulti_mul_ιMulti _ _)

private def volume68 : Ext 6 →ₗ[ℂ] Ext 8 →ₗ[ℂ] ℂ := (multiply 6 8).compr₂ₛₗ volume
private def volume86 : Ext 8 →ₗ[ℂ] Ext 6 →ₗ[ℂ] ℂ := (multiply 8 6).compr₂ₛₗ volume

private theorem volume68_pure (u : Fin 6 → Space) (v : Fin 8 → Space) :
    volume68 (pureWedge 6 u) (pureWedge 8 v) = orthBasis.det (Fin.append u v) := by
  simp only [volume68, LinearMap.compr₂ₛₗ_apply, multiply_pure, volume,
    exteriorPower.alternatingMapLinearEquiv_apply_ιMulti]

private theorem volume86_pure (u : Fin 8 → Space) (v : Fin 6 → Space) :
    volume86 (pureWedge 8 u) (pureWedge 6 v) = orthBasis.det (Fin.append u v) := by
  simp only [volume86, LinearMap.compr₂ₛₗ_apply, multiply_pure, volume,
    exteriorPower.alternatingMapLinearEquiv_apply_ιMulti]

private theorem remove_append_left (u : Fin 7 → Space) (v : Fin 8 → Space) (i : Fin 7) :
    (i.castAdd 8).removeNth (Fin.append (m := 7) (n := 8) u v) =
      Fin.append (m := 6) (n := 8) (i.removeNth u) v := by
  have hl : ∀ (i : Fin 7) (j : Fin 6), (i.castAdd 8).succAbove (j.castAdd 8) = (i.succAbove j).castAdd 8 := by
    decide +kernel
  have hr : ∀ (i : Fin 7) (j : Fin 8), (i.castAdd 8).succAbove (Fin.natAdd 6 j) = Fin.natAdd 7 j := by
    decide +kernel
  funext j
  refine Fin.addCases (m := 6) (n := 8) ?_ ?_ j
  · intro a; rw [Fin.removeNth_apply, hl, Fin.append_left, Fin.append_left, Fin.removeNth_apply]
  · intro a; rw [Fin.removeNth_apply, hr, Fin.append_right, Fin.append_right]

private theorem remove_append_right (u : Fin 7 → Space) (v : Fin 8 → Space) (i : Fin 8) :
    (Fin.natAdd 7 i).removeNth (Fin.append (m := 7) (n := 8) u v) =
      Fin.append (m := 7) (n := 7) u (i.removeNth v) := by
  have hl : ∀ (i : Fin 8) (j : Fin 7), (Fin.natAdd 7 i).succAbove (j.castAdd 7) = j.castAdd 8 := by
    decide +kernel
  have hr : ∀ (i : Fin 8) (j : Fin 7), (Fin.natAdd 7 i).succAbove (Fin.natAdd 7 j) = Fin.natAdd 7 (i.succAbove j) := by
    decide +kernel
  funext j
  refine Fin.addCases (m := 7) (n := 7) ?_ ?_ j
  · intro a; rw [Fin.removeNth_apply, hl, Fin.append_left, Fin.append_left]
  · intro a; rw [Fin.removeNth_apply, hr, Fin.append_right, Fin.append_right, Fin.removeNth_apply]

/-- Contracting a fifteen-fold pure wedge gives zero in the oriented top
degree. Splitting the fifteen terms at the seventh slot gives this identity. -/
private theorem volume_contract_right (x : Space) (u : Fin 7 → Space) (v : Ext 8) :
    volumePair (pureWedge 7 u) (contractLeft 7 x v) = volume68 (contractLeft 6 x (pureWedge 7 u)) v := by
  have hb : (volumePair (pureWedge 7 u)).comp (contractLeft 7 x) = volume68 (contractLeft 6 x (pureWedge 7 u)) := by
    apply ext_on_wedges
    intro w
    let f : Space →ₗ[ℂ] (Space [⋀^Fin 14]→ₗ[ℂ] ℂ) := (splitMetric x).smulRight orthBasis.det
    let F := AlternatingMap.alternatizeUncurryFin f
    have hz : Module.finrank ℂ (Ext 15) = 0 := by
      rw [exteriorPower.finrank_eq, Module.finrank_pi, Fintype.card_fin]
      decide
    let : Subsingleton (Ext 15) := (Module.finrank_eq_zero_iff_of_free ℂ (Ext 15)).mp hz
    have hzero : pureWedge 15 (Fin.append u w) = 0 := Subsingleton.elim _ _
    have he := congrArg (exteriorPower.alternatingMapLinearEquiv F) hzero
    rw [exteriorPower.alternatingMapLinearEquiv_apply_ιMulti, map_zero] at he
    simp only [F, AlternatingMap.alternatizeUncurryFin_apply, f, LinearMap.smulRight_apply,
      AlternatingMap.smul_apply, splitMetric_apply] at he
    rw [Fin.sum_univ_add (a := 7) (b := 8)] at he
    simp only [Fin.val_castAdd, Fin.val_natAdd, Fin.append_left, Fin.append_right, remove_append_left,
      remove_append_right, pow_add, show (-1 : ℤ) ^ 7 = -1 by decide, neg_one_mul, neg_zsmul,
      Finset.sum_neg_distrib, ← sub_eq_add_neg] at he
    have h := sub_eq_zero.mp he
    simp only [LinearMap.comp_apply, contractLeft_pure, map_sum, map_zsmul, map_smul, volumePair_pure,
      LinearMap.sum_apply, LinearMap.smul_apply]
    have h68 (a : Fin 6 → Space) : volume68 (pureWedge 6 a) (pureWedge (7 + 1) w) =
        orthBasis.det (Fin.append a w) := volume68_pure a w
    simp only [h68]
    exact h.symm
  exact DFunLike.congr_fun hb v

private theorem insert_volume_slot (x : Space) (u : Fin 7 → Space) (v : Fin 6 → Space) :
    (Fin.natAdd 7 (0 : Fin 7)).insertNth x (Fin.append u v) = Fin.append u (Matrix.vecCons x v) := by
  let p := Fin.natAdd 7 (0 : Fin 7)
  have hl : ∀ j : Fin 7, p.succAbove (j.castAdd 6) = j.castAdd 7 := by decide +kernel
  have hr : ∀ j : Fin 6, p.succAbove (Fin.natAdd 7 j) = Fin.natAdd 7 j.succ := by decide +kernel
  apply Fin.insertNth_eq_iff.mpr
  constructor
  · change x = Fin.append u (Matrix.vecCons x v) (Fin.natAdd 7 (0 : Fin 7))
    rw [Fin.append_right]
    rfl
  · symm
    funext j
    refine Fin.addCases (m := 7) (n := 6) ?_ ?_ j
    · intro a; rw [Fin.removeNth_apply, hl, Fin.append_left, Fin.append_left]
    · intro a; rw [Fin.removeNth_apply, hr, Fin.append_right, Fin.append_right]; rfl

private theorem volume_wedge_right (x : Space) (u : Fin 7 → Space) (v : Ext 6) :
    volumePair (pureWedge 7 u) (D7VectorTensor.wedgeLeftLinear 6 x v) =
      -volume86 (D7VectorTensor.wedgeLeftLinear 7 x (pureWedge 7 u)) v := by
  have hb : (volumePair (pureWedge 7 u)).comp (D7VectorTensor.wedgeLeftLinear 6 x) =
      -volume86 (D7VectorTensor.wedgeLeftLinear 7 x (pureWedge 7 u)) := by
    apply ext_on_wedges
    intro w
    simp only [LinearMap.comp_apply, LinearMap.neg_apply, wedgeLeft_pure]
    change volumePair (pureWedge 7 u) (pureWedge 7 (Matrix.vecCons x w)) =
      -volume86 (pureWedge 8 (Matrix.vecCons x u)) (pureWedge 6 w)
    rw [volumePair_pure, volume86_pure]
    rw [← insert_volume_slot, AlternatingMap.map_insertNth]
    have h : Fin.append (Matrix.vecCons x u) w = Matrix.vecCons x (Fin.append u w) := by
      rw [Matrix.vecCons, Matrix.vecCons, Fin.append_cons]
      rfl
    rw [h]
    change (-1 : ℤ) ^ 7 • orthBasis.det (Matrix.vecCons x (Fin.append u w)) = _
    rw [show (-1 : ℤ) ^ 7 = -1 by decide, neg_one_zsmul]
  exact DFunLike.congr_fun hb v

def tensorInvolution : Product 7 →ₗ[ℂ] Product 7 := TensorProduct.map LinearMap.id involution

private theorem metric_involution (x y : Mid) : exteriorMetric 7 (involution x) y = Complex.I * volumePair x y := by
  change metricPair (Complex.I • star x) y = _
  rw [map_smul, LinearMap.smul_apply, metric_star, smul_eq_mul]

private theorem wedge_involution_pair (t : Product 7) (v : Ext 8) :
    exteriorMetric 8 (wedge 7 (tensorInvolution t)) v = Complex.I * volume68 (contract 6 t) v := by
  have h : ((exteriorMetric 8).flip v).comp ((wedge 7).comp tensorInvolution) =
      Complex.I • ((volume68.flip v).comp (contract 6)) := by
    apply ext_on_tensor_wedges
    intro x u
    simp only [LinearMap.comp_apply, LinearMap.flip_apply, tensorInvolution, TensorProduct.map_tmul,
      LinearMap.id_apply, LinearMap.smul_apply, smul_eq_mul, wedge, contract, TensorProduct.lift.tmul]
    rw [wedge_contract_adjoint, metric_involution, volume_contract_right]
  exact DFunLike.congr_fun h t

private theorem contract_involution_pair (t : Product 7) (v : Ext 6) :
    exteriorMetric 6 (contract 6 (tensorInvolution t)) v = -Complex.I * volume86 (wedge 7 t) v := by
  have h : ((exteriorMetric 6).flip v).comp ((contract 6).comp tensorInvolution) =
      (-Complex.I) • ((volume86.flip v).comp (wedge 7)) := by
    apply ext_on_tensor_wedges
    intro x u
    simp only [LinearMap.comp_apply, LinearMap.flip_apply, tensorInvolution, TensorProduct.map_tmul,
      LinearMap.id_apply, LinearMap.smul_apply, smul_eq_mul, wedge, contract, TensorProduct.lift.tmul]
    rw [exteriorMetric_symm 6, ← wedge_contract_adjoint 6, exteriorMetric_symm 7,
      metric_involution, volume_wedge_right, mul_neg, neg_mul]
  exact DFunLike.congr_fun h t

private theorem wedge_involution_zero (t : Product 7) (ht : contract 6 t = 0) :
    wedge 7 (tensorInvolution t) = 0 := by
  apply exteriorMetric_injective 8
  apply LinearMap.ext
  intro v
  rw [wedge_involution_pair, ht, map_zero, LinearMap.zero_apply, mul_zero, map_zero, LinearMap.zero_apply]

private theorem contract_involution_zero (t : Product 7) (ht : wedge 7 t = 0) :
    contract 6 (tensorInvolution t) = 0 := by
  apply exteriorMetric_injective 6
  apply LinearMap.ext
  intro v
  rw [contract_involution_pair, ht, map_zero, LinearMap.zero_apply, mul_zero, map_zero, LinearMap.zero_apply]

/-- The two kernel conditions are preserved by the Hodge action on the tensor factor. -/
theorem jointKernel_tensorInvolution (t : Product 7) (ht : t ∈ jointKernel 6) :
    tensorInvolution t ∈ jointKernel 6 := by
  rw [mem_jointKernel] at ht ⊢
  exact ⟨wedge_involution_zero t ht.2, contract_involution_zero t ht.1⟩

theorem tensorInvolution_square (t : Product 7) : tensorInvolution (tensorInvolution t) = t := by
  have h : tensorInvolution.comp tensorInvolution = LinearMap.id := by
    apply TensorProduct.ext'
    intro x u
    simp only [tensorInvolution, LinearMap.comp_apply, TensorProduct.map_tmul, LinearMap.id_apply, involution_square]
  exact DFunLike.congr_fun h t

theorem wedge_involution_zero_iff (t : Product 7) : wedge 7 (tensorInvolution t) = 0 ↔ contract 6 t = 0 := by
  refine ⟨fun h => ?_, wedge_involution_zero t⟩
  simpa only [tensorInvolution_square] using contract_involution_zero (tensorInvolution t) h

theorem contract_involution_zero_iff (t : Product 7) : contract 6 (tensorInvolution t) = 0 ↔ wedge 7 t = 0 := by
  refine ⟨fun h => ?_, contract_involution_zero t⟩
  simpa only [tensorInvolution_square] using wedge_involution_zero (tensorInvolution t) h

/-- Within a Hodge eigenspace, either constraint suffices to define the residual kernel. -/
theorem wedge_zero_iff_contract_zero_on_eigenspace (t : Product 7) (a : ℂ) (ha : a ≠ 0)
    (ht : tensorInvolution t = a • t) : wedge 7 t = 0 ↔ contract 6 t = 0 := by
  have h := wedge_involution_zero_iff t
  rw [ht, map_smul] at h
  exact (show a • wedge 7 t = 0 ↔ wedge 7 t = 0 from
    ⟨fun hz => (smul_eq_zero.mp hz).resolve_left ha, fun hz => by rw [hz, smul_zero]⟩).symm.trans h

theorem tensorInvolution_equivariant (g : splitSpecialOrthogonal) (t : Product 7) :
    tensorInvolution (action 7 g t) = action 7 g (tensorInvolution t) := by
  have h : tensorInvolution.comp (action 7 g) = (action 7 g).comp tensorInvolution := by
    apply TensorProduct.ext'
    intro x u
    simp only [tensorInvolution, action, Representation.tprod_apply, LinearMap.comp_apply, TensorProduct.map_tmul,
      LinearMap.id_apply, involution_equivariant]
  exact DFunLike.congr_fun h t

private def tensorReflection : Product 7 →ₗ[ℂ] Product 7 := TensorProduct.map vectorReflection reflection

private theorem jointKernel_reflection (t : Product 7) (ht : t ∈ jointKernel 6) :
    tensorReflection t ∈ jointKernel 6 := by
  rw [mem_jointKernel] at ht ⊢
  have hw := DFunLike.congr_fun (wedge_natural 7 vectorReflection) t
  have hc := DFunLike.congr_fun (contract_natural 6 vectorReflection vectorReflection_isometry) t
  simp only [LinearMap.comp_apply, ht.1, ht.2, map_zero] at hw hc
  exact ⟨hw, hc⟩

private theorem tensorReflection_square (t : Product 7) : tensorReflection (tensorReflection t) = t := by
  have h : tensorReflection.comp tensorReflection = LinearMap.id := by
    apply TensorProduct.ext'
    intro x u
    simp only [tensorReflection, LinearMap.comp_apply, TensorProduct.map_tmul, LinearMap.id_apply,
      vectorReflection_square, reflection_square]
  exact DFunLike.congr_fun h t

private theorem tensorInvolution_reflection (t : Product 7) :
    tensorInvolution (tensorReflection t) = -tensorReflection (tensorInvolution t) := by
  have h : tensorInvolution.comp tensorReflection = -(tensorReflection.comp tensorInvolution) := by
    apply TensorProduct.ext'
    intro x u
    simp only [tensorInvolution, tensorReflection, LinearMap.comp_apply, LinearMap.neg_apply,
      TensorProduct.map_tmul, LinearMap.id_apply]
    have he : involution (reflection u) = -reflection (involution u) := by
      simp [involution, star_reflection]
    rw [he, tmul_neg]
  exact DFunLike.congr_fun h t

/-- Hodge involution restricted to the entire middle residual representation. -/
def residualInvolution : (↥(jointKernel 6)) →ₗ[ℂ] (↥(jointKernel 6)) :=
  tensorInvolution.restrict (fun _ ht => jointKernel_tensorInvolution _ ht)

set_option backward.isDefEq.respectTransparency false in
def residualSector (a : ℂ) : Submodule ℂ (jointKernel 6) :=
  involutionEigenspace (E := ↥(jointKernel 6)) residualInvolution a

set_option backward.isDefEq.respectTransparency false in
theorem tensorInvolution_of_mem_residualSector (a : ℂ) (x : ↥(jointKernel 6))
    (hx : x ∈ residualSector a) : tensorInvolution x.val = a • x.val := by
  rw [residualSector, mem_involutionEigenspace] at hx
  exact congrArg (fun y : ↥(jointKernel 6) => y.val) hx

set_option backward.isDefEq.respectTransparency false in
set_option maxHeartbeats 500000 in
theorem residualSectors_isCompl : IsCompl (residualSector 1) (residualSector (-1)) := by
  have h (x : ↥(jointKernel 6)) : residualInvolution (residualInvolution x) = x := by
    apply Subtype.ext
    exact tensorInvolution_square x.val
  exact involution_eigenspaces_isCompl (E := ↥(jointKernel 6)) residualInvolution h

theorem residualSector_invariant (a : ℂ) (g : splitSpecialOrthogonal) (x : ↥(jointKernel 6))
    (hx : x ∈ residualSector a) : jointKernelAction 6 g x ∈ residualSector a := by
  rw [residualSector, mem_involutionEigenspace] at hx ⊢
  apply Subtype.ext
  have h : tensorInvolution x.val = a • x.val := congrArg Subtype.val hx
  change tensorInvolution (action 7 g x.val) = a • action 7 g x.val
  rw [tensorInvolution_equivariant, h, map_smul]

def residualSectorAction (a : ℂ) : Representation ℂ splitSpecialOrthogonal (residualSector a) :=
  (jointKernelAction 6).subrepresentation (residualSector a) (fun g x hx => residualSector_invariant a g x hx)

set_option backward.isDefEq.respectTransparency false in
/-- The middle residual action is the direct sum of the two Hodge actions. -/
def residualSignedDecomposition : ((residualSectorAction 1).prod (residualSectorAction (-1))).Equiv
    (jointKernelAction 6) := by
  let f : (↥(residualSector 1) × ↥(residualSector (-1))) ≃ₗ[ℂ] ↥(jointKernel 6) :=
    Submodule.prodEquivOfIsCompl (R := ℂ) (E := ↥(jointKernel 6))
      (residualSector 1) (residualSector (-1)) residualSectors_isCompl
  refine Representation.Equiv.mk f fun g => ?_
  apply LinearMap.ext
  intro x
  change (jointKernelAction 6 g x.1.val) + (jointKernelAction 6 g x.2.val) = jointKernelAction 6 g (x.1.val + x.2.val)
  rw [map_add]

private def residualReflection : ↥(jointKernel 6) →ₗ[ℂ] ↥(jointKernel 6) :=
  tensorReflection.restrict (fun _ ht => jointKernel_reflection _ ht)

private theorem residualReflection_sector (a : ℂ) (x : ↥(jointKernel 6)) (hx : x ∈ residualSector a) :
    residualReflection x ∈ residualSector (-a) := by
  rw [residualSector, mem_involutionEigenspace] at hx ⊢
  apply Subtype.ext
  have h : tensorInvolution x.val = a • x.val := congrArg Subtype.val hx
  change tensorInvolution (tensorReflection x.val) = (-a) • tensorReflection x.val
  rw [tensorInvolution_reflection, h, map_smul]
  module

private def reflectionEquiv : residualSector 1 ≃ₗ[ℂ] residualSector (-1) where
  toFun x := ⟨residualReflection x.val, residualReflection_sector 1 x.val x.prop⟩
  invFun y := ⟨residualReflection y.val, by simpa using residualReflection_sector (-1) y.val y.prop⟩
  left_inv x := Subtype.ext (Subtype.ext (tensorReflection_square x.val.val))
  right_inv y := Subtype.ext (Subtype.ext (tensorReflection_square y.val.val))
  map_add' x y := Subtype.ext (residualReflection.map_add x.val y.val)
  map_smul' r x := Subtype.ext (residualReflection.map_smul r x.val)

set_option backward.isDefEq.respectTransparency false in
theorem residualSector_dimensions :
    Module.finrank ℂ (residualSector 1) = 21021 ∧ Module.finrank ℂ (residualSector (-1)) = 21021 := by
  have h : Module.finrank ℂ (residualSector 1) + Module.finrank ℂ (residualSector (-1)) =
      Module.finrank ℂ (jointKernel 6) :=
    Submodule.finrank_add_eq_of_isCompl (K := ℂ) (V := ↥(jointKernel 6)) residualSectors_isCompl
  have hk : Module.finrank ℂ (jointKernel 6) = 42042 := by
    rw [jointKernel_finrank 6 (by decide)]
    decide
  rw [hk] at h
  have he := reflectionEquiv.finrank_eq
  omega

def plusLabelCandidate : ↥(jointKernel 6) :=
  ⟨nullTensor (highestPlus (7 : Fin 15)), internalGrade_candidate (6 : Fin 13)⟩

def minusLabelCandidate : ↥(jointKernel 6) := ⟨nullTensor lastMinus, middleMinus_candidate⟩

/-- For the chosen orientation, the weight `ν₇⁺` occurs in the `-1` Hodge sector. -/
theorem plusLabelCandidate_sector : plusLabelCandidate ∈ residualSector (-1) := by
  rw [residualSector, mem_involutionEigenspace]
  apply Subtype.ext
  have h := (mem_sector (-1) _).mp highestPlus_mem_sector
  change tensorInvolution (nullTensor (highestPlus (7 : Fin 15))) = (-1 : ℂ) • nullTensor (highestPlus (7 : Fin 15))
  simp only [tensorInvolution, nullTensor, TensorProduct.map_tmul, LinearMap.id_apply, h, tmul_smul]
  rfl

/-- For the chosen orientation, the weight `ν₇⁻` occurs in the `+1` Hodge sector. -/
theorem minusLabelCandidate_sector : minusLabelCandidate ∈ residualSector 1 := by
  rw [residualSector, mem_involutionEigenspace]
  apply Subtype.ext
  have h := (mem_sector 1 _).mp lastMinus_mem_sector
  change tensorInvolution (nullTensor lastMinus) = (1 : ℂ) • nullTensor lastMinus
  simp only [tensorInvolution, nullTensor, TensorProduct.map_tmul, LinearMap.id_apply, h, tmul_smul]

end
end GeometricUnity.D7MiddleTensor
~~~

[Return to file index](#file-index)

## D7MiddleIrreducible.lean {#source-d7middleirreducible-lean}

Proves irreducibility of the signed middle residual summands.

~~~lean
import D7MiddleTensor
import D7TensorRotations

/-!
# Irreducibility of the two signed middle residual modules

The Hodge involution pairs repeated-index columns with distinct-index columns
in complementary sign blocks. In either eigenspace the repeated-index part
determines the vector. Its zero-trace blocks are generated by coordinate
differences, and determinant-one signed permutations transport those differences.
-/

namespace GeometricUnity.D7MiddleIrreducible

open D7Exterior D7Hodge D7Irreducible D7VectorTensor D7VectorGrades D7Hook D7MiddleTensor TensorProduct
open D7TensorColumns (repeated trace_repeated repeated_sub_metric)
open D7TensorRotations (perm_repeated perm_marked)
open scoped BigOperators TensorProduct

noncomputable section

private abbrev Column := Axis × Index 7
private abbrev b := tensorExteriorBasis 7
private abbrev e := orthBasis

private theorem basis_tmul (t : Column) : b t = e t.1 ⊗ₜ[ℂ] basis 7 t.2 :=
  Module.Basis.tensorProduct_apply' _ _ _

private theorem involution_column (t : Column) : ∃ z : ℂ,
    tensorInvolution (b t) = z • b (t.1, complement t.2) := by
  obtain ⟨z, _, hz⟩ := involution_basis t.2
  refine ⟨z, ?_⟩
  rw [basis_tmul, basis_tmul]
  simp only [tensorInvolution, TensorProduct.map_tmul, LinearMap.id_apply]
  change e t.1 ⊗ₜ[ℂ] involution (middleBasis t.2) = z • (e t.1 ⊗ₜ[ℂ] middleBasis (complement t.2))
  rw [hz, tmul_smul]

private def repeatedProjection : Product 7 →ₗ[ℂ] Product 7 :=
  b.constr ℂ (fun t => if t.1 ∈ t.2.val then b t else 0)

private theorem repeatedProjection_basis (t : Column) : repeatedProjection (b t) =
    if t.1 ∈ t.2.val then b t else 0 := b.constr_basis _ _ _

private theorem repeatedProjection_exchange : repeatedProjection.comp tensorInvolution =
    tensorInvolution.comp (LinearMap.id - repeatedProjection) := by
  apply b.ext
  intro t
  obtain ⟨z, hz⟩ := involution_column t
  simp only [LinearMap.comp_apply, LinearMap.sub_apply, LinearMap.id_apply, hz, map_smul,
    repeatedProjection_basis]
  have hmem : t.1 ∈ (complement t.2).val ↔ t.1 ∉ t.2.val := Finset.mem_compl
  by_cases ht : t.1 ∈ t.2.val
  · simp [ht, hmem]
  · simp [ht, hmem, hz]

private def eigenLift (a : ℂ) : Product 7 →ₗ[ℂ] Product 7 := LinearMap.id + a • tensorInvolution

private theorem eigenLift_projection (a : ℂ) (t : Product 7) (ht : tensorInvolution t = a • t) :
    eigenLift a (repeatedProjection t) = t := by
  have h := DFunLike.congr_fun repeatedProjection_exchange t
  change repeatedProjection (tensorInvolution t) = tensorInvolution (t - repeatedProjection t) at h
  rw [ht, map_smul] at h
  have he := congrArg tensorInvolution h
  rw [map_smul, tensorInvolution_square] at he
  change repeatedProjection t + a • tensorInvolution (repeatedProjection t) = t
  rw [he]
  abel

private theorem eigenLift_equivariant (a : ℂ) (g : splitSpecialOrthogonal) (x : Product 7) :
    action 7 g (eigenLift a x) = eigenLift a (action 7 g x) := by
  change action 7 g (x + a • tensorInvolution x) = action 7 g x + a • tensorInvolution (action 7 g x)
  rw [map_add, map_smul, tensorInvolution_equivariant]

private abbrev eraseIndex (t : Column) (ht : t.1 ∈ t.2.val) : Index 6 :=
  D7TensorColumns.eraseIndex t.2 t.1 ht

private theorem repeated_column (t : Column) (ht : t.1 ∈ t.2.val) :
    ∃ z : ℂ, b t = z • repeated (eraseIndex t ht) t.1 := by
  obtain ⟨z, _, hz⟩ := D7TensorColumns.repeated_column t ht
  exact ⟨z, hz⟩

private theorem trace_projection : (contract 6).comp repeatedProjection = contract 6 := by
  apply b.ext
  intro t
  rw [LinearMap.comp_apply, repeatedProjection_basis]
  by_cases ht : t.1 ∈ t.2.val
  · rw [if_pos ht]
  · rw [if_neg ht, map_zero, basis_tmul, contract, TensorProduct.lift.tmul,
      D7TensorColumns.contractLeft_basis_zero t.2 t.1 ht]

private def Stable (W : Submodule ℂ (Product 7)) : Prop :=
  ∀ g : splitSpecialOrthogonal, ∀ x ∈ W, action 7 g x ∈ W

private def repeatBlock (s : Column) : Index 6 :=
  if hs : s.1 ∈ s.2.val then eraseIndex s hs else ⟨(parity s)ᶜ, by
    change ((parity s)ᶜ).card = 6
    rw [Finset.card_compl, Fintype.card_fin, parity, if_neg hs, Finset.card_insert_of_notMem hs, s.2.prop]⟩

private theorem repeated_block (t s : Column) (ht : t.1 ∈ t.2.val)
    (h : parity t = parity s ∨ parity t = (parity s)ᶜ) : eraseIndex t ht = repeatBlock s := by
  have hval : (eraseIndex t ht).val = parity t := (if_pos ht).symm
  have hc : (parity t).card = 6 := hval ▸ (eraseIndex t ht).prop
  apply Subtype.ext
  rw [hval]
  by_cases hs : s.1 ∈ s.2.val
  · rw [repeatBlock, dif_pos hs]
    rcases h with h | h
    · exact h.trans (if_pos hs)
    · rw [h, Finset.card_compl, Fintype.card_fin, parity, if_pos hs, Finset.card_erase_of_mem hs, s.2.prop] at hc
      omega
  · rw [repeatBlock, dif_neg hs]
    rcases h with h | h
    · rw [h, parity, if_neg hs, Finset.card_insert_of_notMem hs, s.2.prop] at hc
      omega
    · exact h

private theorem repeatedProjection_span (x : Product 7) (s : Column)
    (hs : ∀ t, b.repr x t ≠ 0 → parity t = parity s ∨ parity t = (parity s)ᶜ) :
    repeatedProjection x ∈ Submodule.span ℂ
      (Set.range fun i : {i : Axis // i ∉ (repeatBlock s).val} => repeated (repeatBlock s) i.val) := by
  classical
  rw [← b.sum_repr x, map_sum]
  apply Submodule.sum_mem
  intro t _
  by_cases h0 : b.repr x t = 0
  · rw [h0, zero_smul, map_zero]; exact Submodule.zero_mem _
  · rw [map_smul, repeatedProjection_basis]
    apply Submodule.smul_mem
    by_cases ht : t.1 ∈ t.2.val
    · rw [if_pos ht]
      obtain ⟨z, hz⟩ := repeated_column t ht
      have he := repeated_block t s ht (hs t h0)
      rw [hz, he]
      apply Submodule.smul_mem
      apply Submodule.subset_span
      have hi : t.1 ∉ (repeatBlock s).val := by
        rw [← he]
        exact Finset.notMem_erase _ _
      exact ⟨⟨t.1, hi⟩, rfl⟩
    · rw [if_neg ht]; exact Submodule.zero_mem _

private theorem swap_map_of_notMem (R : Index 6) {i j : Axis}
    (hi : i ∉ R.val) (hj : j ∉ R.val) : permIndex (Equiv.swap i j) R = R := by
  apply Subtype.ext
  apply Finset.eq_of_subset_of_card_le
  · intro k hk
    obtain ⟨l, hl, rfl⟩ := Finset.mem_map.mp hk
    change Equiv.swap i j l ∈ R.val
    have hli : l ≠ i := fun h => hi (h ▸ hl)
    have hlj : l ≠ j := fun h => hj (h ▸ hl)
    rwa [Equiv.swap_apply_of_ne_of_ne hli hlj]
  · simp [permIndex]

private theorem swap_subtype_val {R : Index 6} {i j : {k : Axis // k ∉ R.val}}
    (k : {k : Axis // k ∉ R.val}) :
    Equiv.swap i.val j.val k.val = (Equiv.swap i j k).val := by
  classical
  by_cases hi : k = i
  · subst k; simp
  by_cases hj : k = j
  · subst k; simp
  rw [Equiv.swap_apply_of_ne_of_ne hi hj,
    Equiv.swap_apply_of_ne_of_ne (fun h => hi (Subtype.ext h)) (fun h => hj (Subtype.ext h))]

private theorem difference_in_submodule (a : ℂ) (W : Submodule ℂ (Product 7)) (hW : Stable W)
    (hK : W ≤ jointKernel 6) (hJ : ∀ x ∈ W, tensorInvolution x = a • x) (hne : W ≠ ⊥) :
    ∃ (R : Index 6) (i j : Axis), i ∉ R.val ∧ j ∉ R.val ∧ i ≠ j ∧
      eigenLift a (repeated R i - repeated R j) ∈ W := by
  classical
  obtain ⟨x, s, hx, hs, hblock⟩ := support_sign_block b parity (fun i j => action 7 (doubleFlip i j))
    tensorExterior_doubleFlip W (fun i j => hW (doubleFlip i j)) hne
  let R := repeatBlock s
  let v (i : {i : Axis // i ∉ R.val}) := repeated R i.val
  obtain ⟨c, hc⟩ := (Submodule.mem_span_range_iff_exists_fun ℂ).mp (repeatedProjection_span x s hblock)
  change (∑ i, c i • v i) = repeatedProjection x at hc
  have hx0 : x ≠ 0 := fun h => hs (by simp [h])
  have hP := eigenLift_projection a x (hJ x hx)
  have hsum0 : (∑ i, c i • v i) ≠ 0 := by
    intro h
    rw [hc] at h
    rw [h, map_zero] at hP
    exact hx0 hP.symm
  have htrace := DFunLike.congr_fun trace_projection x
  change contract 6 (repeatedProjection x) = contract 6 x at htrace
  have htraceV (k : {i : Axis // i ∉ R.val}) : contract 6 (v k) = basis 6 R :=
    trace_repeated R k.val k.prop
  rw [← hc, ((mem_jointKernel 6 x).mp (hK hx)).2, map_sum] at htrace
  simp only [map_smul, htraceV, ← Finset.sum_smul] at htrace
  have hsum := (smul_eq_zero.mp htrace).resolve_right ((basis 6).ne_zero R)
  obtain ⟨i, j, hij⟩ := coefficients_differ c v hsum hsum0
  have hij' : i ≠ j := fun h => hij (congrArg c h)
  let σ := Equiv.swap i.val j.val
  let g := orientedPermAt σ 0
  obtain ⟨d, hd, hperm⟩ := perm_repeated σ 0 R
  rw [swap_map_of_notMem R i.prop j.prop] at hperm
  let w (k : {i : Axis // i ∉ R.val}) := eigenLift a (v k)
  have hw (k : {i : Axis // i ∉ R.val}) : action 7 g (w k) = d • w (Equiv.swap i j k) := by
    change action 7 g (eigenLift a (repeated R k.val)) = _
    rw [eigenLift_equivariant, hperm, map_smul]
    change d • eigenLift a (repeated R (Equiv.swap i.val j.val k.val)) = _
    rw [swap_subtype_val k]
  have hexp : x = ∑ k, c k • w k := by
    rw [← hP, ← hc, map_sum]
    simp only [map_smul, w]
  have hm := W.sub_mem hx (W.smul_mem d⁻¹ (hW g x hx))
  rw [hexp] at hm
  have hcancel (y : Product 7) : d⁻¹ • (d • y) = y := by
    rw [smul_smul, inv_mul_cancel₀ hd, one_smul]
  simp only [map_sum, map_smul, hw, Finset.smul_sum, smul_comm (c _) d, hcancel] at hm
  rw [swap_sum_difference c w i j hij'] at hm
  have hdiff := basis_mem_of_scaled W _ _ (sub_ne_zero.mpr hij) hm
  refine ⟨R, i.val, j.val, i.prop, j.prop, fun h => hij' (Subtype.ext h), ?_⟩
  rw [map_sub]
  exact hdiff

private theorem all_differences (a : ℂ) (W : Submodule ℂ (Product 7)) (hW : Stable W)
    (hK : W ≤ jointKernel 6) (hJ : ∀ x ∈ W, tensorInvolution x = a • x) (hne : W ≠ ⊥)
    (S : Index 6) (k l : Axis) (hk : k ∉ S.val) (hl : l ∉ S.val) :
    eigenLift a (repeated S k - repeated S l) ∈ W := by
  by_cases hkl : k = l
  · subst l
    rw [sub_self, map_zero]
    exact W.zero_mem
  obtain ⟨R, i, j, hi, hj, hij, hx⟩ := difference_in_submodule a W hW hK hJ hne
  obtain ⟨σ, hR, hki, hlj⟩ := perm_marked R S i j k l hi hj hij hk hl hkl
  obtain ⟨d, hd, hσ⟩ := perm_repeated σ 0 R
  have h := hW (orientedPermAt σ 0) _ hx
  rw [eigenLift_equivariant, map_sub, hσ i, hσ j, hR, hki, hlj,
    ← smul_sub d (repeated S k) (repeated S l), map_smul] at h
  exact basis_mem_of_scaled W _ d hd h

private def residualProjection (a : ℂ) : Product 7 →ₗ[ℂ] Product 7 :=
  (eigenLift a).comp ((LinearMap.id - (includeMetric 6).comp (contract 6)).comp repeatedProjection)

private theorem residualProjection_apply (a : ℂ) (x : Product 7) :
    residualProjection a x = eigenLift a (repeatedProjection x - includeMetric 6 (contract 6 x)) := by
  have h := DFunLike.congr_fun trace_projection x
  change contract 6 (repeatedProjection x) = contract 6 x at h
  simp only [residualProjection, LinearMap.comp_apply, LinearMap.sub_apply, LinearMap.id_apply, h]

private theorem traceRemoval (R : Index 6) (i : Axis) :
    repeated R i - includeMetric 6 (basis 6 R) =
      (8 : ℂ)⁻¹ • ∑ j ∈ R.valᶜ, (repeated R i - repeated R j) := by
  have h : (14 - ((6 : ℕ) : ℂ))⁻¹ = (8 : ℂ)⁻¹ := by norm_num
  rw [← h]
  exact repeated_sub_metric (n := 6) (by decide) R i

private theorem sector_le_of_nonzero (a : ℂ) (W : Submodule ℂ (Product 7)) (hW : Stable W)
    (hK : W ≤ jointKernel 6) (hJ : ∀ x ∈ W, tensorInvolution x = a • x) (hne : W ≠ ⊥)
    (x : Product 7) (hx : x ∈ jointKernel 6) (he : tensorInvolution x = a • x) : x ∈ W := by
  have hfixed : residualProjection a x = x := by
    rw [residualProjection_apply, ((mem_jointKernel 6 x).mp hx).2, map_zero, sub_zero,
      eigenLift_projection a x he]
  have hcolumn (t : Column) : residualProjection a (b t) ∈ W := by
    by_cases ht : t.1 ∈ t.2.val
    · obtain ⟨z, hz⟩ := repeated_column t ht
      have hi : t.1 ∉ (eraseIndex t ht).val := Finset.notMem_erase _ _
      have hc : contract 6 (b t) = z • basis 6 (eraseIndex t ht) := by
        rw [hz, map_smul, trace_repeated _ _ hi]
      rw [residualProjection_apply, repeatedProjection_basis, if_pos ht, hc, hz,
        map_smul (includeMetric 6),
        ← smul_sub z (repeated (eraseIndex t ht) t.1) (includeMetric 6 (basis 6 (eraseIndex t ht))),
        traceRemoval, map_smul, map_smul, map_sum]
      exact W.smul_mem _ (W.smul_mem _ (W.sum_mem fun j hj =>
        all_differences a W hW hK hJ hne _ _ _ hi (Finset.mem_compl.mp hj)))
    · have hp := repeatedProjection_basis t
      rw [if_neg ht] at hp
      rw [residualProjection, LinearMap.comp_apply, LinearMap.comp_apply, hp, map_zero, map_zero]
      exact W.zero_mem
  rw [← hfixed, ← b.sum_repr x, map_sum]
  exact W.sum_mem fun t _ => by rw [map_smul]; exact W.smul_mem _ (hcolumn t)

local instance (a : ℂ) : AddCommGroup ↥(residualSector a) :=
  Submodule.addCommGroup (R := ℂ) (M := ↥(jointKernel 6)) (residualSector a)

local instance (a : ℂ) : Module ℂ ↥(residualSector a) :=
  Submodule.module (R := ℂ) (M := ↥(jointKernel 6)) (residualSector a)

set_option backward.isDefEq.respectTransparency false in
set_option maxHeartbeats 500000 in
/-- Both Hodge eigenspaces of the degree-seven joint kernel carry irreducible
complex special orthogonal representations. -/
theorem residualSector_isIrreducible (a : ℂ) (ha : a = 1 ∨ a = -1) :
    Representation.IsIrreducible (k := ℂ) (V := ↥(residualSector a)) (residualSectorAction a) := by
  have hd : Module.finrank ℂ (residualSector a) = 21021 := by
    rcases ha with h | h
    · rw [h]; exact residualSector_dimensions.1
    · rw [h]; exact residualSector_dimensions.2
  have : Nontrivial (↥(residualSector a)) := Module.nontrivial_of_finrank_pos (by rw [hd]; decide)
  apply irreducible_of_subrepresentations
  intro U
  let f := (jointKernel 6).subtype.comp (residualSector a).subtype
  have hf : Function.Injective f := (jointKernel 6).subtype_injective.comp (residualSector a).subtype_injective
  let W : Submodule ℂ (Product 7) := U.toSubmodule.map f
  have hincl (y : ↥(residualSector a)) : f y ∈ jointKernel 6 := y.val.prop
  have heig (y : ↥(residualSector a)) : tensorInvolution (f y) = a • f y :=
    tensorInvolution_of_mem_residualSector a y.val y.prop
  have hW : Stable W := by
    intro g x hx
    obtain ⟨y, hy, rfl⟩ := Submodule.mem_map.mp hx
    exact Submodule.mem_map.mpr ⟨residualSectorAction a g y, U.apply_mem_toSubmodule g hy, rfl⟩
  have hK : W ≤ jointKernel 6 := by
    rintro x ⟨y, _, rfl⟩
    exact hincl y
  have hJ : ∀ x ∈ W, tensorInvolution x = a • x := by
    rintro x ⟨y, _, rfl⟩
    exact heig y
  by_cases hne : W = ⊥
  · left
    apply Subrepresentation.toSubmodule_injective
    apply Submodule.map_injective_of_injective hf
    change W = (⊥ : Submodule ℂ (residualSector a)).map f
    rw [Submodule.map_bot, hne]
  · right
    apply Subrepresentation.toSubmodule_injective
    change U.toSubmodule = ⊤
    refine top_unique fun y _ => ?_
    have hm := sector_le_of_nonzero a W hW hK hJ hne (f y) (hincl y) (heig y)
    obtain ⟨z, hz, hzy⟩ := Submodule.mem_map.mp hm
    exact hf hzy ▸ hz

end
end GeometricUnity.D7MiddleIrreducible
~~~

[Return to file index](#file-index)

## D7TensorColumns.lean {#source-d7tensorcolumns-lean}

Organizes repeated-index and distinct-index tensor coordinates used in the kernel arguments.

~~~lean
import D7Hook
import D7VectorGrades
import Mathlib.LinearAlgebra.Basis.SMul

/-!
# Coordinate columns of the vector–exterior tensor product

Repeated-index columns are normalized by contraction. Distinct-index columns
are normalized by exterior multiplication. In either family the corresponding
linear map takes every column in a block to the same exterior basis vector.
-/

namespace GeometricUnity.D7TensorColumns

open D7Exterior D7Hodge D7Irreducible D7VectorTensor D7VectorGrades D7Hook TensorProduct
open scoped BigOperators TensorProduct

noncomputable section

private abbrev e := orthBasis

def eraseIndex {n : ℕ} (S : Index (n + 1)) (i : Axis) (hi : i ∈ S.val) : Index n :=
  ⟨S.val.erase i, by change (S.val.erase i).card = n; rw [Finset.card_erase_of_mem hi, S.prop]; omega⟩

def insertIndex {n : ℕ} (R : Index n) (i : Axis) (hi : i ∉ R.val) : Index (n + 1) :=
  ⟨insert i R.val, by change (insert i R.val).card = n + 1; rw [Finset.card_insert_of_notMem hi, R.prop]⟩

theorem notMem_eraseIndex {n : ℕ} (S : Index (n + 1)) (i : Axis) (hi : i ∈ S.val) :
    i ∉ (eraseIndex S i hi).val := Finset.notMem_erase _ _

set_option backward.isDefEq.respectTransparency false in
theorem basis_eq_wedge_erase {n : ℕ} (S : Index (n + 1)) (i : Axis) (hi : i ∈ S.val) :
    ∃ z : ℂ, z ≠ 0 ∧ basis (n + 1) S = z • wedgeLeftLinear n (e i) (basis n (eraseIndex S i hi)) := by
  let R := eraseIndex S i hi
  let a := Set.powersetCard.ofFinEmbEquiv.symm S
  have hm : i ∈ S := hi
  obtain ⟨j, hj⟩ := (Set.powersetCard.mem_range_ofFinEmbEquiv_symm_iff_mem S _).mpr hm
  change a j = i at hj
  let d := OrderEmbedding.ofStrictMono (fun k => a (j.succAbove k))
    (a.strictMono.comp (Fin.strictMono_succAbove j))
  have hd (k : Fin n) : d k ∈ R.val := by
    apply Finset.mem_erase.mpr
    refine ⟨?_, Finset.orderEmbOfFin_mem S.val S.prop (j.succAbove k)⟩
    exact fun h => Fin.succAbove_ne j k (a.injective (h.trans hj.symm))
  have he := Finset.orderEmbOfFin_unique' R.prop (f := d) hd
  have hor : j.removeNth (e ∘ a) = e ∘ Set.powersetCard.ofFinEmbEquiv.symm R := by
    funext k
    change e (d k) = e ((R.val.orderEmbOfFin R.prop) k)
    rw [he]
  let z := (-1 : ℤ) ^ j.val
  refine ⟨(z : ℂ), Int.cast_ne_zero.mpr (pow_ne_zero _ (by norm_num)), ?_⟩
  calc
    basis (n + 1) S = z • wedgeLeftLinear n (e i) (basis n R) := by
      rw [exteriorPower.basis_apply, exteriorPower.basis_apply, exteriorPower.ιMulti_family,
        exteriorPower.ιMulti_family, wedgeLeft_pure, ← hor, ← AlternatingMap.map_insertNth]
      have hval : (e ∘ a) j = e i := congrArg e hj
      rw [← hval, Fin.insertNth_self_removeNth]
    _ = (z : ℂ) • wedgeLeftLinear n (e i) (basis n R) := (Int.cast_smul_eq_zsmul ℂ z _).symm

theorem wedgeLeft_basis_zero {n : ℕ} (R : Index n) (i : Axis) (hi : i ∈ R.val) :
    wedgeLeftLinear n (e i) (basis n R) = 0 := by
  change i ∈ R at hi
  obtain ⟨j, hj⟩ := (Set.powersetCard.mem_range_ofFinEmbEquiv_symm_iff_mem R i).mpr hi
  rw [exteriorPower.basis_apply, exteriorPower.ιMulti_family, wedgeLeft_pure]
  apply (exteriorPower.ιMulti ℂ (n + 1)).map_eq_zero_of_eq _ (i := 0) (j := j.succ)
  · change e i = e (Set.powersetCard.ofFinEmbEquiv.symm R j)
    rw [hj]
  · exact Ne.symm (Fin.succ_ne_zero j)

theorem contractLeft_basis_zero {n : ℕ} (S : Index (n + 1)) (i : Axis) (hi : i ∉ S.val) :
    contractLeft n (e i) (basis (n + 1) S) = 0 := by
  rw [exteriorPower.basis_apply, exteriorPower.ιMulti_family, contractLeft_pure]
  apply Finset.sum_eq_zero
  intro j _
  let a := Set.powersetCard.ofFinEmbEquiv.symm S
  have hm : a j ∈ S.val := Finset.orderEmbOfFin_mem S.val S.prop j
  have he : i ≠ Set.powersetCard.ofFinEmbEquiv.symm S j := fun hc => hi (hc.symm ▸ hm)
  simp only [Function.comp_apply, orthBasis_pair, if_neg he, zero_smul, smul_zero]

theorem contract_wedge_basis {n : ℕ} (R : Index n) (i : Axis) (hi : i ∉ R.val) :
    contractLeft n (e i) (wedgeLeftLinear n (e i) (basis n R)) = basis n R := by
  cases n with
  | zero => rw [contract_wedgeLeft_zero, orthBasis_pair, if_pos rfl, one_smul]
  | succ n =>
    rw [contract_wedgeLeft, orthBasis_pair, if_pos rfl, one_smul, contractLeft_basis_zero R i hi,
      map_zero, sub_zero]

theorem wedgeLeft_sq {n : ℕ} (x : Space) (u : Ext n) :
    wedgeLeftLinear (n + 1) x (wedgeLeftLinear n x u) = 0 := by
  apply Subtype.ext
  change ExteriorAlgebra.ι ℂ x * (ExteriorAlgebra.ι ℂ x * u.val) = 0
  rw [← mul_assoc, ExteriorAlgebra.ι_sq_zero, zero_mul]

theorem wedgeLeft_swap {n : ℕ} (x y : Space) (u : Ext n) :
    wedgeLeftLinear (n + 1) x (wedgeLeftLinear n y u) =
      -wedgeLeftLinear (n + 1) y (wedgeLeftLinear n x u) := by
  apply Subtype.ext
  change ExteriorAlgebra.ι ℂ x * (ExteriorAlgebra.ι ℂ y * u.val) =
    -(ExteriorAlgebra.ι ℂ y * (ExteriorAlgebra.ι ℂ x * u.val))
  rw [← mul_assoc, ← mul_assoc, ← neg_mul]
  exact congrArg (fun z => z * u.val)
    (eq_neg_of_add_eq_zero_left (ExteriorAlgebra.ι_add_mul_swap (R := ℂ) x y))

/-- A repeated-index tensor normalized to have unit contraction in its block. -/
def repeated {n : ℕ} (R : Index n) (i : Axis) : Product (n + 1) :=
  e i ⊗ₜ[ℂ] wedgeLeftLinear n (e i) (basis n R)

/-- A distinct-index tensor normalized to have unit alternation in its block. -/
def distinct {n : ℕ} (S : Index (n + 1)) (i : Axis) : Product n :=
  e i ⊗ₜ[ℂ] contractLeft n (e i) (basis (n + 1) S)

theorem repeated_zero {n : ℕ} (R : Index n) (i : Axis) (hi : i ∈ R.val) : repeated R i = 0 := by
  rw [repeated, wedgeLeft_basis_zero R i hi, tmul_zero]

theorem distinct_zero {n : ℕ} (S : Index (n + 1)) (i : Axis) (hi : i ∉ S.val) : distinct S i = 0 := by
  rw [distinct, contractLeft_basis_zero S i hi, tmul_zero]

theorem trace_repeated {n : ℕ} (R : Index n) (i : Axis) (hi : i ∉ R.val) :
    contract n (repeated R i) = basis n R := by
  rw [repeated, contract, TensorProduct.lift.tmul, contract_wedge_basis R i hi]

theorem wedge_repeated {n : ℕ} (R : Index n) (i : Axis) : wedge (n + 1) (repeated R i) = 0 := by
  rw [repeated, wedge, TensorProduct.lift.tmul, wedgeLeft_sq]

theorem repeated_column {n : ℕ} (t : Axis × Index (n + 1)) (ht : t.1 ∈ t.2.val) :
    ∃ z : ℂ, z ≠ 0 ∧
      tensorExteriorBasis (n + 1) t = z • repeated (eraseIndex t.2 t.1 ht) t.1 := by
  obtain ⟨z, hz, h⟩ := basis_eq_wedge_erase t.2 t.1 ht
  refine ⟨z, hz, ?_⟩
  rw [tensorExteriorBasis, Module.Basis.tensorProduct_apply', h, tmul_smul, repeated]

theorem distinct_column {n : ℕ} (S : Index (n + 1)) (i : Axis) (hi : i ∈ S.val) :
    ∃ z : ℂ, z ≠ 0 ∧ basis (n + 1) S = z • wedgeLeftLinear n (e i) (basis n (eraseIndex S i hi)) ∧
      distinct S i = z • tensorExteriorBasis n (i, eraseIndex S i hi) := by
  obtain ⟨z, hz, h⟩ := basis_eq_wedge_erase S i hi
  refine ⟨z, hz, h, ?_⟩
  rw [distinct, h, map_smul, contract_wedge_basis _ _ (notMem_eraseIndex S i hi),
    tmul_smul, tensorExteriorBasis, Module.Basis.tensorProduct_apply']

theorem wedge_distinct {n : ℕ} (S : Index (n + 1)) (i : Axis) (hi : i ∈ S.val) :
    wedge n (distinct S i) = basis (n + 1) S := by
  obtain ⟨z, _, h, hD⟩ := distinct_column S i hi
  rw [hD, map_smul, tensorExteriorBasis, Module.Basis.tensorProduct_apply', wedge, TensorProduct.lift.tmul, ← h]

theorem trace_distinct {n : ℕ} (S : Index (n + 2)) (i : Axis) : contract n (distinct S i) = 0 := by
  by_cases hi : i ∈ S.val
  · obtain ⟨z, _, _, hz⟩ := distinct_column S i hi
    rw [hz, map_smul, tensorExteriorBasis, Module.Basis.tensorProduct_apply', contract, TensorProduct.lift.tmul,
      contractLeft_basis_zero _ _ (notMem_eraseIndex S i hi), smul_zero]
  · rw [distinct_zero S i hi, map_zero]

theorem column_of_distinct {n : ℕ} (t : Axis × Index n) (ht : t.1 ∉ t.2.val) :
    ∃ z : ℂ, z ≠ 0 ∧ tensorExteriorBasis n t = z • distinct (insertIndex t.2 t.1 ht) t.1 := by
  let S := insertIndex t.2 t.1 ht
  have hi : t.1 ∈ S.val := Finset.mem_insert_self _ _
  have hS : eraseIndex S t.1 hi = t.2 := Subtype.ext (Finset.erase_insert ht)
  obtain ⟨z, hz, _, h⟩ := distinct_column S t.1 hi
  rw [hS] at h
  refine ⟨z⁻¹, inv_ne_zero hz, ?_⟩
  rw [h, smul_smul, inv_mul_cancel₀ hz, one_smul]

theorem includeWedge_basis {n : ℕ} (S : Index (n + 1)) :
    includeWedge n (basis (n + 1) S) = (n + 1 : ℂ)⁻¹ • ∑ i ∈ S.val, distinct S i := by
  let a := Set.powersetCard.ofFinEmbEquiv.symm S
  let v : Fin (n + 1) → Space := e ∘ a
  have hb : basis (n + 1) S = exteriorPower.ιMulti ℂ (n + 1) v := by
    rw [exteriorPower.basis_apply, exteriorPower.ιMulti_family]
  have himage : Finset.univ.map a.toEmbedding = S.val := by
    ext i
    rw [Finset.mem_map]
    change (∃ j : Fin (n + 1), j ∈ Finset.univ ∧ a j = i) ↔ i ∈ S
    simp only [Finset.mem_univ, true_and]
    exact Set.powersetCard.mem_range_ofFinEmbEquiv_symm_iff_mem S i
  have hterm (j : Fin (n + 1)) : distinct S (a j) =
      (-1 : ℤ) ^ j.val • (v j ⊗ₜ[ℂ] exteriorPower.ιMulti ℂ n (j.removeNth v)) := by
    rw [distinct, hb, contractLeft_pure, Finset.sum_eq_single j]
    · have hp : splitForm (e (a j)) (v j) = 1 := by
        change splitForm (e (a j)) (e (a j)) = 1
        simp [orthBasis_pair]
      rw [hp, one_smul]
      simp only [← Int.cast_smul_eq_zsmul ℂ, tmul_smul]
      rfl
    · intro k _ hk
      have he : a j ≠ a k := fun h => hk (a.injective h).symm
      change (-1 : ℤ) ^ k.val • ((splitForm (e (a j)) (e (a k))) • _) = _
      simp [orthBasis_pair, he]
    · simp
  rw [hb, includeWedge_pure, ← himage, Finset.sum_map]
  congr 1
  exact Finset.sum_congr rfl fun j _ => (hterm j).symm

private theorem sub_average {E ι : Type*} [AddCommGroup E] [Module ℂ E]
    (s : Finset ι) (hs : s.card ≠ 0) (v : ι → E) (i : ι) :
    v i - (s.card : ℂ)⁻¹ • ∑ j ∈ s, v j =
      (s.card : ℂ)⁻¹ • ∑ j ∈ s, (v i - v j) := by
  rw [Finset.sum_sub_distrib, Finset.sum_const, smul_sub, ← Nat.cast_smul_eq_nsmul ℂ,
    smul_smul, inv_mul_cancel₀ (Nat.cast_ne_zero.mpr hs), one_smul]

theorem repeated_sub_metric {n : ℕ} (hn : n < 14) (R : Index n) (i : Axis) :
    repeated R i - includeMetric n (basis n R) =
      (14 - (n : ℂ))⁻¹ • ∑ j ∈ R.valᶜ, (repeated R i - repeated R j) := by
  have hcard : R.valᶜ.card = 14 - n := by rw [Finset.card_compl, Fintype.card_fin, R.prop]
  have hsum : ∑ j ∈ R.valᶜ, repeated R j = ∑ j : Axis, repeated R j := by
    apply Finset.sum_subset (Finset.subset_univ _)
    intro j _ hj
    exact repeated_zero R j (by simpa using hj)
  rw [includeMetric_apply]
  change repeated R i - (14 - (n : ℂ))⁻¹ • (∑ j, repeated R j) = _
  rw [← hsum]
  have hcast : (R.valᶜ.card : ℂ) = 14 - (n : ℂ) := by
    rw [hcard, Nat.cast_sub hn.le]
    norm_num
  rw [← hcast]
  exact sub_average R.valᶜ (by rw [hcard]; omega) (repeated R) i

theorem distinct_sub_wedge {n : ℕ} (S : Index (n + 1)) (i : Axis) :
    distinct S i - includeWedge n (basis (n + 1) S) =
      (n + 1 : ℂ)⁻¹ • ∑ j ∈ S.val, (distinct S i - distinct S j) := by
  rw [includeWedge_basis]
  have hcard : S.val.card = n + 1 := S.prop
  have hcast : (S.val.card : ℂ) = (n + 1 : ℂ) := by rw [hcard, Nat.cast_add, Nat.cast_one]
  rw [← hcast]
  exact sub_average S.val (by rw [hcard]; omega) (distinct S) i

/-- Repeated and distinct differences span the simultaneous kernel of
exterior multiplication and contraction in every supported input degree. -/
theorem jointKernel_le_of_differences (n : ℕ) (hn : n < 14) (W : Submodule ℂ (Product (n + 1)))
    (hR : ∀ (R : Index n) i j, i ∉ R.val → j ∉ R.val → repeated R i - repeated R j ∈ W)
    (hS : ∀ (S : Index (n + 2)) i j, i ∈ S.val → j ∈ S.val → distinct S i - distinct S j ∈ W) :
    jointKernel n ≤ W := by
  let P : Product (n + 1) →ₗ[ℂ] Product (n + 1) :=
    LinearMap.id - (includeWedge (n + 1)).comp (wedge (n + 1)) - (includeMetric n).comp (contract n)
  have hP (y : Product (n + 1)) :
      P y = y - includeWedge (n + 1) (wedge (n + 1) y) - includeMetric n (contract n y) := rfl
  have hcolumn (t : Axis × Index (n + 1)) : P (tensorExteriorBasis (n + 1) t) ∈ W := by
    by_cases ht : t.1 ∈ t.2.val
    · obtain ⟨z, _, hz⟩ := repeated_column t ht
      let R := eraseIndex t.2 t.1 ht
      have hi : t.1 ∉ R.val := notMem_eraseIndex t.2 t.1 ht
      rw [hz, map_smul, hP, wedge_repeated, trace_repeated R t.1 hi, map_zero, sub_zero,
        repeated_sub_metric hn]
      exact W.smul_mem _ (W.smul_mem _ (W.sum_mem fun j hj => hR R t.1 j hi (Finset.mem_compl.mp hj)))
    · obtain ⟨z, _, hz⟩ := column_of_distinct t ht
      let S := insertIndex t.2 t.1 ht
      have hi : t.1 ∈ S.val := Finset.mem_insert_self _ _
      rw [hz, map_smul, hP, wedge_distinct S t.1 hi, trace_distinct, map_zero, sub_zero, distinct_sub_wedge]
      exact W.smul_mem _ (W.smul_mem _ (W.sum_mem fun j hj => hS S t.1 j hi hj))
  intro x hx
  have ⟨hw, hc⟩ := (mem_jointKernel n x).mp hx
  have hxP : P x = x := by rw [hP, hw, hc, map_zero, map_zero, sub_zero, sub_zero]
  rw [← hxP, ← (tensorExteriorBasis (n + 1)).sum_repr x, map_sum]
  exact W.sum_mem fun t _ => by rw [map_smul]; exact W.smul_mem _ (hcolumn t)

abbrev RepeatedIndex (n : ℕ) := Σ R : Index n, {i : Axis // i ∉ R.val}
abbrev DistinctIndex (n : ℕ) := Σ S : Index (n + 2), ↥S.val
abbrev NormalizedIndex (n : ℕ) := RepeatedIndex n ⊕ DistinctIndex n

private def toColumn {n : ℕ} : NormalizedIndex n → Axis × Index (n + 1)
  | .inl ⟨R, i⟩ => (i.val, insertIndex R i.val i.prop)
  | .inr ⟨S, i⟩ => (i.val, eraseIndex S i.val i.prop)

private def fromColumn {n : ℕ} (t : Axis × Index (n + 1)) : NormalizedIndex n :=
  if h : t.1 ∈ t.2.val then .inl ⟨eraseIndex t.2 t.1 h, ⟨t.1, notMem_eraseIndex t.2 t.1 h⟩⟩
  else .inr ⟨insertIndex t.2 t.1 h, ⟨t.1, Finset.mem_insert_self _ _⟩⟩

private theorem erase_insertIndex {n : ℕ} (R : Index n) (i : Axis) (hi : i ∉ R.val) :
    eraseIndex (insertIndex R i hi) i (Finset.mem_insert_self _ _) = R :=
  Subtype.ext (Finset.erase_insert hi)

private theorem insert_eraseIndex {n : ℕ} (S : Index (n + 1)) (i : Axis) (hi : i ∈ S.val) :
    insertIndex (eraseIndex S i hi) i (notMem_eraseIndex S i hi) = S :=
  Subtype.ext (Finset.insert_erase hi)

private def columnEquiv (n : ℕ) : NormalizedIndex n ≃ Axis × Index (n + 1) where
  toFun := toColumn
  invFun := fromColumn
  left_inv := by
    rintro (⟨R, i⟩ | ⟨S, i⟩)
    · have h : i.val ∈ (insertIndex R i.val i.prop).val := Finset.mem_insert_self _ _
      change fromColumn (i.val, insertIndex R i.val i.prop) = .inl ⟨R, i⟩
      rw [fromColumn, dif_pos h]
      congr 1
      apply Sigma.subtype_ext
      · exact erase_insertIndex R i.val i.prop
      · rfl
    · have h := notMem_eraseIndex S i.val i.prop
      change fromColumn (i.val, eraseIndex S i.val i.prop) = .inr ⟨S, i⟩
      rw [fromColumn, dif_neg h]
      congr 1
      apply Sigma.subtype_ext
      · exact insert_eraseIndex S i.val i.prop
      · rfl
  right_inv := by
    rintro ⟨i, S⟩
    by_cases h : i ∈ S.val
    · simp only [fromColumn, toColumn, dif_pos h, insert_eraseIndex]
    · simp only [fromColumn, toColumn, dif_neg h, erase_insertIndex]

private def columnVector {n : ℕ} : NormalizedIndex n → Product (n + 1)
  | .inl ⟨R, i⟩ => repeated R i.val
  | .inr ⟨S, i⟩ => distinct S i.val

private theorem columnVector_scaled {n : ℕ} (q : NormalizedIndex n) :
    ∃ z : ℂ, z ≠ 0 ∧ columnVector q = z • tensorExteriorBasis (n + 1) (columnEquiv n q) := by
  rcases q with ⟨R, i⟩ | ⟨S, i⟩
  · let t := (i.val, insertIndex R i.val i.prop)
    have ht : t.1 ∈ t.2.val := Finset.mem_insert_self _ _
    obtain ⟨z, hz, h⟩ := repeated_column t ht
    change tensorExteriorBasis (n + 1) t =
      z • repeated (eraseIndex (insertIndex R i.val i.prop) i.val ht) i.val at h
    rw [erase_insertIndex] at h
    refine ⟨z⁻¹, inv_ne_zero hz, ?_⟩
    change repeated R i.val = z⁻¹ • tensorExteriorBasis (n + 1) t
    rw [h, smul_smul, inv_mul_cancel₀ hz, one_smul]
  · obtain ⟨z, hz, _, h⟩ := distinct_column S i.val i.prop
    exact ⟨z, hz, h⟩

/-- The orthogonal tensor basis, grouped by normalized contraction and wedge blocks. -/
def normalizedBasis (n : ℕ) : Module.Basis (NormalizedIndex n) ℂ (Product (n + 1)) :=
  ((tensorExteriorBasis (n + 1)).reindex (columnEquiv n).symm).unitsSMul fun q =>
    Units.mk0 (columnVector_scaled q).choose (columnVector_scaled q).choose_spec.1

private theorem normalizedBasis_apply {n : ℕ} (q : NormalizedIndex n) :
    normalizedBasis n q = columnVector q := by
  rw [normalizedBasis, Module.Basis.unitsSMul_apply, Module.Basis.reindex_apply, Units.smul_def]
  exact (columnVector_scaled q).choose_spec.2.symm

@[simp] theorem normalizedBasis_repeated {n : ℕ} (R : Index n) (i : {i : Axis // i ∉ R.val}) :
    normalizedBasis n (.inl ⟨R, i⟩) = repeated R i.val := normalizedBasis_apply _

@[simp] theorem normalizedBasis_distinct {n : ℕ} (S : Index (n + 2)) (i : ↥S.val) :
    normalizedBasis n (.inr ⟨S, i⟩) = distinct S i.val := normalizedBasis_apply _

def block {n : ℕ} : NormalizedIndex n → Finset Axis
  | .inl ⟨R, _⟩ => R.val
  | .inr ⟨S, _⟩ => S.val

private theorem parity_column {n : ℕ} (q : NormalizedIndex n) : parity (columnEquiv n q) = block q := by
  rcases q with ⟨R, i⟩ | ⟨S, i⟩
  · change parity (i.val, insertIndex R i.val i.prop) = R.val
    have h : i.val ∈ (insertIndex R i.val i.prop).val := Finset.mem_insert_self _ _
    rw [parity, if_pos h]
    exact Finset.erase_insert i.prop
  · change parity (i.val, eraseIndex S i.val i.prop) = S.val
    rw [parity, if_neg (notMem_eraseIndex S i.val i.prop)]
    exact Finset.insert_erase i.prop

theorem normalizedBasis_doubleFlip {n : ℕ} (i j : Axis) (q : NormalizedIndex n) :
    action (n + 1) (doubleFlip i j) (normalizedBasis n q) =
      character (block q) i j • normalizedBasis n q := by
  obtain ⟨z, _, hz⟩ := columnVector_scaled q
  have h := tensorExterior_doubleFlip i j (columnEquiv n q)
  change action (n + 1) (doubleFlip i j) (tensorExteriorBasis (n + 1) (columnEquiv n q)) = _ at h
  rw [normalizedBasis_apply, hz, map_smul, h, parity_column, smul_comm z]

end
end GeometricUnity.D7TensorColumns
~~~

[Return to file index](#file-index)

## D7TensorRotations.lean {#source-d7tensorrotations-lean}

Calculates the plane rotations that connect the two tensor-coordinate families.

~~~lean
import D7TensorColumns

/-!
# Plane rotations on vector–exterior coordinates

A quarter-turn permutes the normalized coefficients in either block family.
An ordinary plane rotation converts a repeated difference into a distinct
difference and conversely.
-/

namespace GeometricUnity.D7TensorRotations

open D7Exterior D7Hodge D7Irreducible D7VectorTensor D7VectorGrades D7Hook D7TensorColumns TensorProduct
open scoped BigOperators TensorProduct

noncomputable section

private abbrev e := orthBasis

theorem map_basis_fixed {n : ℕ} (g : splitSpecialOrthogonal) (R : Index n)
    (h : ∀ k ∈ R.val, g.val (e k) = e k) :
    exteriorPower.map n g.val (basis n R) = basis n R := by
  rw [exteriorPower.basis_apply, exteriorPower.ιMulti_family, exteriorPower.map_apply_ιMulti]
  congr 1
  funext k
  exact h _ (Finset.orderEmbOfFin_mem R.val R.prop k)

private theorem wedge_plane {n : ℕ} (x y : Space) (u : Ext n) (c s : ℂ)
    (h : c * c + s * s = 1) :
    wedgeLeftLinear (n + 1) (c • x + s • y) (wedgeLeftLinear n ((-s) • x + c • y) u) =
      wedgeLeftLinear (n + 1) x (wedgeLeftLinear n y u) := by
  calc
    _ = (c * c + s * s) • wedgeLeftLinear (n + 1) x (wedgeLeftLinear n y u) := by
      simp only [map_add, LinearMap.add_apply, map_smul, LinearMap.smul_apply, wedgeLeft_sq,
        smul_zero, zero_add, add_zero, wedgeLeft_swap y x u]
      module
    _ = _ := by rw [h, one_smul]

/-- A plane rotation fixes the coordinate wedge when the block contains both
rotated axes or when it contains neither. -/
theorem map_basis_plane {n : ℕ} (g : splitSpecialOrthogonal) (i j : Axis) (hij : i ≠ j) (c s : ℂ)
    (hc : c * c + s * s = 1)
    (hi : g.val (e i) = c • e i + s • e j) (hj : g.val (e j) = (-s) • e i + c • e j)
    (hoff : ∀ k, k ≠ i → k ≠ j → g.val (e k) = e k)
    (R : Index n) (hR : i ∈ R.val ↔ j ∈ R.val) : exteriorPower.map n g.val (basis n R) = basis n R := by
  by_cases hRi : i ∈ R.val
  · have hRj := hR.mp hRi
    cases n with
    | zero =>
      have hempty : R.val = ∅ := Finset.card_eq_zero.mp R.prop
      simp [hempty] at hRi
    | succ n =>
      let S := eraseIndex R i hRi
      have hSj : j ∈ S.val := Finset.mem_erase.mpr ⟨hij.symm, hRj⟩
      cases n with
      | zero =>
        have hempty : S.val = ∅ := Finset.card_eq_zero.mp S.prop
        simp [hempty] at hSj
      | succ n =>
        let T := eraseIndex S j hSj
        have hT := map_basis_fixed g T (fun k hk => hoff k
          (Finset.mem_erase.mp (Finset.mem_erase.mp hk).2).1 (Finset.mem_erase.mp hk).1)
        change exteriorPower.map n g.val (basis n (eraseIndex S j hSj)) = _ at hT
        obtain ⟨d, _, hd⟩ := basis_eq_wedge_erase R i hRi
        obtain ⟨z, _, hz⟩ := basis_eq_wedge_erase S j hSj
        rw [hd]
        change exteriorPower.map (n + 2) g.val (d • wedgeLeftLinear (n + 1) (e i) (basis (n + 1) S)) = _
        rw [hz]
        simp only [map_smul, wedgeLeft_naturality, hT, hi, hj, wedge_plane _ _ _ _ _ hc]
        rfl
  · have hRj : j ∉ R.val := fun h => hRi (hR.mpr h)
    exact map_basis_fixed g R fun k hk => hoff k (fun h => hRi (h ▸ hk)) (fun h => hRj (h ▸ hk))

def quarterTurn (i j : Axis) : splitSpecialOrthogonal := orientedPermAt (Equiv.swap i j) i

theorem quarterTurn_basis (i j : Axis) (hij : i ≠ j) :
    (quarterTurn i j).val (e i) = -e j ∧ (quarterTurn i j).val (e j) = e i := by
  constructor
  · simp [quarterTurn, orientedPermAt_basis, orientationCorrection, signScalar, Equiv.Perm.sign_swap hij]
  · simp [quarterTurn, orientedPermAt_basis, orientationCorrection, hij.symm]

theorem quarterTurn_off_plane (i j k : Axis) (hi : k ≠ i) (hj : k ≠ j) :
    (quarterTurn i j).val (e k) = e k := by
  simp [quarterTurn, orientedPermAt_basis, orientationCorrection, Equiv.swap_apply_of_ne_of_ne hi hj, hi]

theorem quarterTurn_exterior {n : ℕ} (i j : Axis) (hij : i ≠ j) (R : Index n)
    (hR : i ∈ R.val ↔ j ∈ R.val) :
    exteriorPower.map n (quarterTurn i j).val (basis n R) = basis n R := by
  obtain ⟨hi, hj⟩ := quarterTurn_basis i j hij
  apply map_basis_plane _ i j hij 0 (-1) (by norm_num) _ _ (quarterTurn_off_plane i j) R hR
  · simpa using hi
  · simpa using hj

theorem quarterTurn_repeated {n : ℕ} (i j : Axis) (hij : i ≠ j) (R : Index n)
    (hR : i ∈ R.val ↔ j ∈ R.val) (k : Axis) :
    action (n + 1) (quarterTurn i j) (repeated R k) = repeated R (Equiv.swap i j k) := by
  rw [repeated, action_tmul, wedgeLeft_naturality, quarterTurn_exterior i j hij R hR,
    quarterTurn, orientedPermAt_basis]
  simp only [map_smul, LinearMap.smul_apply, smul_tmul_smul, correction_sq, one_smul, repeated]

theorem quarterTurn_distinct {n : ℕ} (i j : Axis) (hij : i ≠ j) (S : Index (n + 2))
    (hS : i ∈ S.val ↔ j ∈ S.val) (k : Axis) :
    action (n + 1) (quarterTurn i j) (distinct S k) = distinct S (Equiv.swap i j k) := by
  rw [distinct, action_tmul, contractLeft_naturality, quarterTurn_exterior i j hij S hS,
    quarterTurn, orientedPermAt_basis]
  simp only [map_smul, LinearMap.smul_apply, smul_tmul_smul, correction_sq, one_smul, distinct]

theorem perm_repeated {n : ℕ} (σ : Equiv.Perm Axis) (p : Axis) (R : Index n) :
    ∃ d : ℂ, d ≠ 0 ∧ ∀ i,
      action (n + 1) (orientedPermAt σ p) (repeated R i) = d • repeated (permIndex σ R) (σ i) := by
  let g := orientedPermAt σ p
  obtain ⟨d, hd, he⟩ := orientedPerm_exterior σ p R
  change exteriorPower.map n g.val (basis n R) = _ at he
  refine ⟨d, hd, fun i => ?_⟩
  rw [repeated, action_tmul, wedgeLeft_naturality n g, he, orientedPermAt_basis]
  simp only [map_smul, LinearMap.smul_apply, smul_smul, smul_tmul_smul, repeated]
  rw [mul_comm d (orientationCorrection σ p i), ← mul_assoc, correction_sq, one_mul]

private def markedCoordinates {n : ℕ} (R : Index n) (i j : Axis) : Bool ⊕ ↥R.val → Axis :=
  Sum.elim (fun q => if q then i else j) Subtype.val

private theorem markedCoordinates_injective {n : ℕ} (R : Index n) (i j : Axis)
    (hi : i ∉ R.val) (hj : j ∉ R.val) (hij : i ≠ j) :
    Function.Injective (markedCoordinates R i j) := by
  intro x y h
  cases x with
  | inl x =>
    cases y with
    | inl y => cases x <;> cases y <;> simp_all [markedCoordinates]
    | inr y =>
      cases x
      · change j = y.val at h
        exact (hj (h ▸ y.prop)).elim
      · change i = y.val at h
        exact (hi (h ▸ y.prop)).elim
  | inr x =>
    cases y with
    | inl y =>
      cases y
      · change x.val = j at h
        exact (hj (h ▸ x.prop)).elim
      · change x.val = i at h
        exact (hi (h ▸ x.prop)).elim
    | inr y => exact congrArg Sum.inr (Subtype.ext h)

theorem perm_marked {n : ℕ} (R S : Index n) (i j k l : Axis)
    (hi : i ∉ R.val) (hj : j ∉ R.val) (hij : i ≠ j)
    (hk : k ∉ S.val) (hl : l ∉ S.val) (hkl : k ≠ l) :
    ∃ σ : Equiv.Perm Axis, permIndex σ R = S ∧ σ i = k ∧ σ j = l := by
  let q := Equiv.sumCongr (Equiv.refl Bool) (R.val.equivOfCardEq (R.prop.trans S.prop.symm))
  obtain ⟨σ, hσ⟩ := Equiv.Perm.exists_extending_pair (markedCoordinates R i j)
    (markedCoordinates S k l ∘ q) (markedCoordinates_injective R i j hi hj hij)
    ((markedCoordinates_injective S k l hk hl hkl).comp q.injective)
  refine ⟨σ, ?_, hσ (.inl true), hσ (.inl false)⟩
  apply Subtype.ext
  apply Finset.eq_of_subset_of_card_le
  · intro a ha
    obtain ⟨b, hb, rfl⟩ := Finset.mem_map.mp ha
    let y := R.val.equivOfCardEq (R.prop.trans S.prop.symm) ⟨b, hb⟩
    have h : σ b = y.val := hσ (.inr ⟨b, hb⟩)
    exact h.symm ▸ y.prop
  · simp [permIndex]

private abbrev bridgeTerm {n : ℕ} (R : Index n) (i j : Axis) : Product (n + 1) :=
  e i ⊗ₜ[ℂ] wedgeLeftLinear n (e j) (basis n R)

theorem contract_wedge_basis_of_ne {n : ℕ} (R : Index n) (i j : Axis) (hij : i ≠ j) (hi : i ∉ R.val) :
    contractLeft n (e i) (wedgeLeftLinear n (e j) (basis n R)) = 0 := by
  cases n with
  | zero => rw [contract_wedgeLeft_zero, orthBasis_pair, if_neg hij, zero_smul]
  | succ n =>
    rw [contract_wedgeLeft, orthBasis_pair, if_neg hij, zero_smul, contractLeft_basis_zero R i hi, map_zero, sub_zero]

private theorem contract_pair {n : ℕ} (R : Index n) (i j : Axis) (hij : i ≠ j) (hi : i ∉ R.val) :
    contractLeft (n + 1) (e i) (wedgeLeftLinear (n + 1) (e i) (wedgeLeftLinear n (e j) (basis n R))) =
      wedgeLeftLinear n (e j) (basis n R) := by
  rw [contract_wedgeLeft, orthBasis_pair, if_pos rfl, one_smul,
    contract_wedge_basis_of_ne R i j hij hi, map_zero, sub_zero]

private theorem basis_pair {n : ℕ} (R : Index n) (S : Index (n + 2)) (i j : Axis)
    (hij : i ≠ j) (hiR : i ∉ R.val) (hjR : j ∉ R.val) (hS : S.val = insert i (insert j R.val)) :
    ∃ d : ℂ, d ≠ 0 ∧ basis (n + 2) S =
      d • wedgeLeftLinear (n + 1) (e i) (wedgeLeftLinear n (e j) (basis n R)) := by
  have hi : i ∈ S.val := by rw [hS]; exact Finset.mem_insert_self _ _
  let T := eraseIndex S i hi
  have hT : T.val = insert j R.val := by
    change S.val.erase i = _
    rw [hS, Finset.erase_insert (by simp [hij, hiR])]
  have hj : j ∈ T.val := by rw [hT]; exact Finset.mem_insert_self _ _
  have hR : eraseIndex T j hj = R := by
    apply Subtype.ext
    change T.val.erase j = _
    rw [hT, Finset.erase_insert hjR]
  obtain ⟨a, ha, hA⟩ := basis_eq_wedge_erase S i hi
  obtain ⟨b, hb, hB⟩ := basis_eq_wedge_erase T j hj
  rw [hR] at hB
  refine ⟨a * b, mul_ne_zero ha hb, ?_⟩
  rw [hA]
  change a • wedgeLeftLinear (n + 1) (e i) (basis (n + 1) T) = _
  rw [hB, map_smul, smul_smul]

private theorem bridge_coord {n : ℕ} (R : Index n) (S : Index (n + 2)) (i j : Axis)
    (hij : i ≠ j) (hi : i ∉ R.val) (hj : j ∉ R.val) (hS : S.val = insert i (insert j R.val)) :
    ∃ d : ℂ, d ≠ 0 ∧ distinct S i - distinct S j = d • (bridgeTerm R i j + bridgeTerm R j i) := by
  obtain ⟨d, hd, h⟩ := basis_pair R S i j hij hi hj hS
  have h₁ : distinct S i = d • bridgeTerm R i j := by
    rw [distinct, h, map_smul, contract_pair R i j hij hi, tmul_smul]
  have h₂ : distinct S j = - (d • bridgeTerm R j i) := by
    rw [distinct, h, map_smul, wedgeLeft_swap (e i) (e j), map_neg, contract_pair R j i hij.symm hj,
      smul_neg, tmul_neg, tmul_smul]
  refine ⟨d, hd, ?_⟩
  rw [h₁, h₂, sub_neg_eq_add, smul_add]

private theorem plane_mix {n : ℕ} (R : Index n) (i j : Axis) (hij : i ≠ j)
    (hi : i ∉ R.val) (hj : j ∉ R.val) :
    let A := repeated R i - repeated R j
    let B := bridgeTerm R i j + bridgeTerm R j i
    let g := rotation i j hij
    action (n + 1) g A = (-527 / 625 : ℂ) • A + (-336 / 625 : ℂ) • B ∧
    action (n + 1) g B = (336 / 625 : ℂ) • A + (-527 / 625 : ℂ) • B := by
  let g := rotation i j hij
  obtain ⟨hi', hj'⟩ := rotation_on_plane i j hij
  have hR := map_basis_fixed g R (fun k hk => rotation_off_plane i j k hij
    (fun h => hi (h ▸ hk)) (fun h => hj (h ▸ hk)))
  change exteriorPower.map n (rotation i j hij).val (basis n R) = basis n R at hR
  dsimp only
  simp only [repeated, map_sub, map_add, action_tmul, wedgeLeft_naturality, hR, hi', hj',
    LinearMap.add_apply, map_smul, LinearMap.smul_apply, add_tmul, tmul_add, ← smul_tmul', tmul_smul]
  constructor <;> module

theorem rotation_bridge {n : ℕ} (W : Submodule ℂ (Product (n + 1)))
    (hW : ∀ g : splitSpecialOrthogonal, ∀ x ∈ W, action (n + 1) g x ∈ W)
    (R : Index n) (S : Index (n + 2)) (i j : Axis)
    (hij : i ≠ j) (hi : i ∉ R.val) (hj : j ∉ R.val) (hS : S.val = insert i (insert j R.val)) :
    repeated R i - repeated R j ∈ W ↔ distinct S i - distinct S j ∈ W := by
  obtain ⟨d, hd, hD⟩ := bridge_coord R S i j hij hi hj hS
  obtain ⟨hA, hB⟩ := plane_mix R i j hij hi hj
  let A := repeated R i - repeated R j
  let B := bridgeTerm R i j + bridgeTerm R j i
  let g := rotation i j hij
  rw [hD]
  change A ∈ W ↔ d • B ∈ W
  constructor
  · intro hx
    have hm := W.sub_mem (hW g A hx) (W.smul_mem (-527 / 625 : ℂ) hx)
    change action (n + 1) g A - (-527 / 625 : ℂ) • A ∈ W at hm
    rw [hA, add_sub_cancel_left] at hm
    exact W.smul_mem d (basis_mem_of_scaled W B _ (by norm_num) hm)
  · intro hx
    have hb := basis_mem_of_scaled W B d hd hx
    have hm := W.sub_mem (hW g B hb) (W.smul_mem (-527 / 625 : ℂ) hb)
    change action (n + 1) g B - (-527 / 625 : ℂ) • B ∈ W at hm
    rw [hB, add_sub_cancel_right] at hm
    exact basis_mem_of_scaled W A _ (by norm_num) hm

end
end GeometricUnity.D7TensorRotations
~~~

[Return to file index](#file-index)

## D7GradeIrreducible.lean {#source-d7gradeirreducible-lean}

Proves irreducibility of the non-middle vector-exterior kernels.

~~~lean
import D7TensorRotations

/-!
# Irreducibility of the non-middle vector–exterior kernels

Even sign changes select a block up to complement. Within a chosen block,
zero contraction or zero wedge forces the sum of the coefficients to vanish.
A quarter-turn extracts a difference from two unequal coefficients and fixes
any complementary block. Signed permutations and plane rotations transport
the difference to the two spanning families.
-/

namespace GeometricUnity.D7GradeIrreducible

open D7Exterior D7Hodge D7Irreducible D7VectorGrades D7Hook D7TensorColumns D7TensorRotations
open scoped BigOperators

noncomputable section

private def Stable {n : ℕ} (W : Submodule ℂ (Product (n + 1))) : Prop :=
  ∀ g : splitSpecialOrthogonal, ∀ x ∈ W, action (n + 1) g x ∈ W

private theorem block_sums_zero {n : ℕ} (x : Product (n + 1)) (hx : x ∈ jointKernel n) :
    let c := (normalizedBasis n).repr x
    (∀ R : Index n, ∑ i : {i : Axis // i ∉ R.val}, c (.inl ⟨R, i⟩) = 0) ∧
    (∀ S : Index (n + 2), ∑ i : ↥S.val, c (.inr ⟨S, i⟩) = 0) := by
  classical
  let c := (normalizedBasis n).repr x
  have hex := (normalizedBasis n).sum_repr x
  have ⟨hw, hc⟩ := (mem_jointKernel n x).mp hx
  rw [Fintype.sum_sum_type, Fintype.sum_sigma, Fintype.sum_sigma] at hex
  have hR := congrArg (contract n) hex
  have hS := congrArg (wedge (n + 1)) hex
  have hcon (R : Index n) (i : {i : Axis // i ∉ R.val}) :
      contract n (repeated R i.val) = basis n R := trace_repeated R i.val i.prop
  have hwedge (S : Index (n + 2)) (i : ↥S.val) :
      wedge (n + 1) (distinct S i.val) = basis (n + 2) S := wedge_distinct S i.val i.prop
  simp only [hc, normalizedBasis_repeated, normalizedBasis_distinct, map_add, map_sum, map_smul,
    hcon, trace_distinct, smul_zero, Finset.sum_const_zero, add_zero, ← Finset.sum_smul] at hR
  simp only [hw, normalizedBasis_repeated, normalizedBasis_distinct, map_add, map_sum, map_smul,
    hwedge, wedge_repeated, smul_zero, Finset.sum_const_zero, zero_add, ← Finset.sum_smul] at hS
  exact ⟨Fintype.linearIndependent_iff.mp (basis n).linearIndependent _ hR,
    Fintype.linearIndependent_iff.mp (basis (n + 2)).linearIndependent _ hS⟩

private theorem second_coefficient {ι : Type*} [Fintype ι] (c : ι → ℂ) (i : ι)
    (hs : ∑ k, c k = 0) (hi : c i ≠ 0) : ∃ j, c i ≠ c j := by
  by_contra! h
  simp_rw [← h] at hs
  rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul] at hs
  have : Nonempty ι := ⟨i⟩
  exact hi ((mul_eq_zero.mp hs).resolve_left (Nat.cast_ne_zero.mpr Fintype.card_ne_zero))

private theorem extract_by_swap {n : ℕ} (W : Submodule ℂ (Product (n + 1))) (hW : Stable W)
    (x : Product (n + 1)) (hx : x ∈ W) (a b : NormalizedIndex n)
    (hne : (normalizedBasis n).repr x a ≠ (normalizedBasis n).repr x b)
    (g : splitSpecialOrthogonal)
    (hg : ∀ t, (normalizedBasis n).repr x t ≠ 0 →
      action (n + 1) g (normalizedBasis n t) = normalizedBasis n (Equiv.swap a b t)) :
    normalizedBasis n a - normalizedBasis n b ∈ W := by
  classical
  let c := (normalizedBasis n).repr x
  have hne' : a ≠ b := fun h => hne (congrArg c h)
  have hact : action (n + 1) g x = ∑ t, c t • normalizedBasis n (Equiv.swap a b t) := by
    conv_lhs => rw [← (normalizedBasis n).sum_repr x, map_sum]
    apply Finset.sum_congr rfl
    intro t _
    rw [map_smul]
    by_cases ht : c t = 0
    · rw [ht, zero_smul, zero_smul]
    · rw [hg t ht]
  have h := W.sub_mem hx (hW g x hx)
  have he := congrArg (fun y => y - ∑ t, c t • normalizedBasis n (Equiv.swap a b t))
    ((normalizedBasis n).sum_repr x)
  rw [swap_sum_difference c (normalizedBasis n) a b hne'] at he
  rw [hact, ← he] at h
  exact basis_mem_of_scaled W _ _ (sub_ne_zero.mpr hne) h

private theorem not_compl_mixed {n : ℕ} (hn : n ≠ 6) (R : Index n) (S : Index (n + 2)) :
    R.val ≠ S.val ∧ R.val ≠ S.valᶜ := by
  constructor <;> intro h
  · have hc := congrArg Finset.card h
    rw [R.prop, S.prop] at hc
    omega
  · have hc := congrArg Finset.card h
    rw [R.prop, Finset.card_compl, Fintype.card_fin, S.prop] at hc
    have hc' := Finset.card_le_univ S.val
    rw [Fintype.card_fin, S.prop] at hc'
    omega

private theorem repeated_swap_action {n : ℕ} (hn : n ≠ 6) (R : Index n)
    (i j : {k : Axis // k ∉ R.val}) (hij : i.val ≠ j.val) (t : NormalizedIndex n)
    (ht : block t = R.val ∨ block t = R.valᶜ) :
    action (n + 1) (quarterTurn i.val j.val) (normalizedBasis n t) =
      normalizedBasis n (Equiv.swap (.inl ⟨R, i⟩) (.inl ⟨R, j⟩) t) := by
  let a : NormalizedIndex n := .inl ⟨R, i⟩
  let b : NormalizedIndex n := .inl ⟨R, j⟩
  by_cases ha : t = a
  · rw [ha, Equiv.swap_apply_left, normalizedBasis_repeated, normalizedBasis_repeated,
      quarterTurn_repeated _ _ hij R (iff_of_false i.prop j.prop), Equiv.swap_apply_left]
  by_cases hb : t = b
  · rw [hb, Equiv.swap_apply_right, normalizedBasis_repeated, normalizedBasis_repeated,
      quarterTurn_repeated _ _ hij R (iff_of_false i.prop j.prop), Equiv.swap_apply_right]
  rw [Equiv.swap_apply_of_ne_of_ne ha hb]
  rcases t with ⟨Q, k⟩ | ⟨S, k⟩
  · simp only [block] at ht
    have hk : k.val ≠ i.val ∧ k.val ≠ j.val := by
      rcases ht with h | h
      · have hQR : Q = R := Subtype.ext h
        subst Q
        let f (l : {k : Axis // k ∉ R.val}) : NormalizedIndex n := .inl ⟨R, l⟩
        exact ⟨fun h => ha (congrArg f (Subtype.ext h)), fun h => hb (congrArg f (Subtype.ext h))⟩
      · have hiQ : i.val ∈ Q.val := h.symm ▸ Finset.mem_compl.mpr i.prop
        have hjQ : j.val ∈ Q.val := h.symm ▸ Finset.mem_compl.mpr j.prop
        exact ⟨fun h => k.prop (h.symm ▸ hiQ), fun h => k.prop (h.symm ▸ hjQ)⟩
    have hQ : i.val ∈ Q.val ↔ j.val ∈ Q.val := by
      rcases ht with h | h
      · rw [h]; exact iff_of_false i.prop j.prop
      · rw [h]; exact iff_of_true (Finset.mem_compl.mpr i.prop) (Finset.mem_compl.mpr j.prop)
    rw [normalizedBasis_repeated, quarterTurn_repeated _ _ hij Q hQ, Equiv.swap_apply_of_ne_of_ne hk.1 hk.2]
  · simp only [block] at ht
    have hm := not_compl_mixed hn R S
    exact (ht.elim (fun h => hm.1 h.symm)
      (fun h => hm.2 (by rw [h, compl_compl]))).elim

private theorem distinct_swap_action {n : ℕ} (hn : n ≠ 6) (S : Index (n + 2))
    (i j : ↥S.val) (hij : i.val ≠ j.val) (t : NormalizedIndex n)
    (ht : block t = S.val ∨ block t = S.valᶜ) :
    action (n + 1) (quarterTurn i.val j.val) (normalizedBasis n t) =
      normalizedBasis n (Equiv.swap (.inr ⟨S, i⟩) (.inr ⟨S, j⟩) t) := by
  let a : NormalizedIndex n := .inr ⟨S, i⟩
  let b : NormalizedIndex n := .inr ⟨S, j⟩
  by_cases ha : t = a
  · rw [ha, Equiv.swap_apply_left, normalizedBasis_distinct, normalizedBasis_distinct,
      quarterTurn_distinct _ _ hij S (iff_of_true i.prop j.prop), Equiv.swap_apply_left]
  by_cases hb : t = b
  · rw [hb, Equiv.swap_apply_right, normalizedBasis_distinct, normalizedBasis_distinct,
      quarterTurn_distinct _ _ hij S (iff_of_true i.prop j.prop), Equiv.swap_apply_right]
  rw [Equiv.swap_apply_of_ne_of_ne ha hb]
  rcases t with ⟨R, k⟩ | ⟨Q, k⟩
  · simp only [block] at ht
    have hm := not_compl_mixed hn R S
    exact (ht.elim hm.1 hm.2).elim
  · simp only [block] at ht
    have hk : k.val ≠ i.val ∧ k.val ≠ j.val := by
      rcases ht with h | h
      · have hQS : Q = S := Subtype.ext h
        subst Q
        let f (l : ↥S.val) : NormalizedIndex n := .inr ⟨S, l⟩
        exact ⟨fun h => ha (congrArg f (Subtype.ext h)), fun h => hb (congrArg f (Subtype.ext h))⟩
      · have hiQ : i.val ∉ Q.val := by rw [h]; exact fun hh => (Finset.mem_compl.mp hh) i.prop
        have hjQ : j.val ∉ Q.val := by rw [h]; exact fun hh => (Finset.mem_compl.mp hh) j.prop
        exact ⟨fun h => hiQ (h ▸ k.prop), fun h => hjQ (h ▸ k.prop)⟩
    have hQ : i.val ∈ Q.val ↔ j.val ∈ Q.val := by
      rcases ht with h | h
      · rw [h]; exact iff_of_true i.prop j.prop
      · rw [h]; exact iff_of_false (fun hi => (Finset.mem_compl.mp hi) i.prop)
          (fun hj => (Finset.mem_compl.mp hj) j.prop)
    rw [normalizedBasis_distinct, quarterTurn_distinct _ _ hij Q hQ, Equiv.swap_apply_of_ne_of_ne hk.1 hk.2]

private theorem some_difference {n : ℕ} (hn : n ≠ 6) (W : Submodule ℂ (Product (n + 1)))
    (hW : Stable W) (hK : W ≤ jointKernel n) (hne : W ≠ ⊥) :
    (∃ (R : Index n) (i j : Axis), i ∉ R.val ∧ j ∉ R.val ∧ i ≠ j ∧ repeated R i - repeated R j ∈ W) ∨
    (∃ (S : Index (n + 2)) (i j : Axis), i ∈ S.val ∧ j ∈ S.val ∧ i ≠ j ∧ distinct S i - distinct S j ∈ W) := by
  classical
  obtain ⟨x, q, hx, hq, hblock⟩ := support_sign_block (normalizedBasis n) block
    (fun i j => action (n + 1) (doubleFlip i j)) normalizedBasis_doubleFlip
    W (fun i j => hW (doubleFlip i j)) hne
  have ⟨hR, hS⟩ := block_sums_zero x (hK hx)
  rcases q with ⟨R, i⟩ | ⟨S, i⟩
  · let c := fun t : {i : Axis // i ∉ R.val} => (normalizedBasis n).repr x (.inl ⟨R, t⟩)
    obtain ⟨j, hj⟩ := second_coefficient c i (hR R) hq
    have hij : i.val ≠ j.val := fun h => hj (congrArg c (Subtype.ext h))
    have hdiff := extract_by_swap W hW x hx (.inl ⟨R, i⟩) (.inl ⟨R, j⟩) hj
      (quarterTurn i.val j.val) (fun t ht => repeated_swap_action hn R i j hij t (hblock t ht))
    rw [normalizedBasis_repeated, normalizedBasis_repeated] at hdiff
    exact Or.inl ⟨R, i.val, j.val, i.prop, j.prop, hij, hdiff⟩
  · let c := fun t : ↥S.val => (normalizedBasis n).repr x (.inr ⟨S, t⟩)
    obtain ⟨j, hj⟩ := second_coefficient c i (hS S) hq
    have hij : i.val ≠ j.val := fun h => hj (congrArg c (Subtype.ext h))
    have hdiff := extract_by_swap W hW x hx (.inr ⟨S, i⟩) (.inr ⟨S, j⟩) hj
      (quarterTurn i.val j.val) (fun t ht => distinct_swap_action hn S i j hij t (hblock t ht))
    rw [normalizedBasis_distinct, normalizedBasis_distinct] at hdiff
    exact Or.inr ⟨S, i.val, j.val, i.prop, j.prop, hij, hdiff⟩

private theorem erase_pair {n : ℕ} (S : Index (n + 2)) (i j : Axis)
    (hi : i ∈ S.val) (hj : j ∈ S.val) (hij : i ≠ j) :
    ∃ R : Index n, i ∉ R.val ∧ j ∉ R.val ∧ S.val = insert i (insert j R.val) := by
  let T := eraseIndex S i hi
  have hjT : j ∈ T.val := Finset.mem_erase.mpr ⟨hij.symm, hj⟩
  let R := eraseIndex T j hjT
  refine ⟨R, fun h => (notMem_eraseIndex S i hi) (Finset.mem_erase.mp h).2,
    notMem_eraseIndex T j hjT, ?_⟩
  change S.val = insert i (insert j (T.val.erase j))
  rw [Finset.insert_erase hjT]
  change S.val = insert i (S.val.erase i)
  rw [Finset.insert_erase hi]

private theorem some_repeated {n : ℕ} (hn : n ≠ 6) (W : Submodule ℂ (Product (n + 1)))
    (hW : Stable W) (hK : W ≤ jointKernel n) (hne : W ≠ ⊥) :
    ∃ (R : Index n) (i j : Axis), i ∉ R.val ∧ j ∉ R.val ∧ i ≠ j ∧ repeated R i - repeated R j ∈ W := by
  rcases some_difference hn W hW hK hne with h | ⟨S, i, j, hi, hj, hij, hd⟩
  · exact h
  · obtain ⟨R, hiR, hjR, hS⟩ := erase_pair S i j hi hj hij
    exact ⟨R, i, j, hiR, hjR, hij, (rotation_bridge W hW R S i j hij hiR hjR hS).mpr hd⟩

private theorem transport_repeated {n : ℕ} (W : Submodule ℂ (Product (n + 1))) (hW : Stable W)
    (R S : Index n) (i j a b : Axis)
    (hi : i ∉ R.val) (hj : j ∉ R.val) (hij : i ≠ j)
    (ha : a ∉ S.val) (hb : b ∉ S.val) (hd : repeated R i - repeated R j ∈ W) :
    repeated S a - repeated S b ∈ W := by
  by_cases hab : a = b
  · subst b
    rw [sub_self]
    exact W.zero_mem
  obtain ⟨σ, hS, hia, hjb⟩ := perm_marked R S i j a b hi hj hij ha hb hab
  obtain ⟨d, hd', hσ⟩ := perm_repeated σ 0 R
  have h := hW (orientedPermAt σ 0) _ hd
  rw [map_sub, hσ i, hσ j, hS, hia, hjb, ← smul_sub d (repeated S a) (repeated S b)] at h
  exact basis_mem_of_scaled W _ d hd' h

theorem jointKernel_invariant_subspace {n : ℕ} (hn : n < 14) (hm : n ≠ 6)
    (W : Submodule ℂ (Product (n + 1)))
    (hW : ∀ g : splitSpecialOrthogonal, ∀ x ∈ W, action (n + 1) g x ∈ W)
    (hK : W ≤ jointKernel n) : W = ⊥ ∨ W = jointKernel n := by
  by_cases hne : W = ⊥
  · exact Or.inl hne
  obtain ⟨R, i, j, hi, hj, hij, hdiff⟩ := some_repeated hm W hW hK hne
  have hR (S : Index n) (a b : Axis) (ha : a ∉ S.val) (hb : b ∉ S.val) :
      repeated S a - repeated S b ∈ W :=
    transport_repeated W hW R S i j a b hi hj hij ha hb hdiff
  have hS (S : Index (n + 2)) (a b : Axis) (ha : a ∈ S.val) (hb : b ∈ S.val) :
      distinct S a - distinct S b ∈ W := by
    by_cases hab : a = b
    · subst b
      rw [sub_self]
      exact W.zero_mem
    obtain ⟨T, haT, hbT, he⟩ := erase_pair S a b ha hb hab
    exact (rotation_bridge W hW T S a b hab haT hbT he).mp (hR T a b haT hbT)
  exact Or.inr (le_antisymm hK (jointKernel_le_of_differences n hn W hR hS))

set_option backward.isDefEq.respectTransparency false in
/-- In input degrees one through thirteen, except for degree seven, the
joint kernel carries an irreducible complex special orthogonal action. -/
theorem jointKernel_isIrreducible (n : Fin 13) (hn : n.val ≠ 6) :
    Representation.IsIrreducible (k := ℂ) (V := ↥(jointKernel n.val)) (jointKernelAction n.val) := by
  have : Nontrivial (↥(jointKernel n.val)) :=
    ⟨⟨⟨nullTensor (highestPlus (internalGrade n)), internalGrade_candidate n⟩, 0,
      fun h => nullTensor_ne_zero _ (congrArg Subtype.val h)⟩⟩
  apply irreducible_of_subrepresentations
  intro U
  let K := jointKernel n.val
  let W : Submodule ℂ (Product (n.val + 1)) := U.toSubmodule.map K.subtype
  have hW : Stable W := by
    intro g x hx
    obtain ⟨y, hy, rfl⟩ := Submodule.mem_map.mp hx
    exact Submodule.mem_map.mpr ⟨jointKernelAction n.val g y, U.apply_mem_toSubmodule g hy, rfl⟩
  have hK : W ≤ K := by
    intro x hx
    obtain ⟨y, _, rfl⟩ := Submodule.mem_map.mp hx
    exact y.prop
  rcases jointKernel_invariant_subspace (n.isLt.trans (by decide)) hn W hW hK with h | h
  · left
    apply Subrepresentation.toSubmodule_injective
    apply Submodule.map_injective_of_injective K.subtype_injective
    change W = (⊥ : Submodule ℂ K).map K.subtype
    rw [Submodule.map_bot, h]
  · right
    apply Subrepresentation.toSubmodule_injective
    apply Submodule.map_injective_of_injective K.subtype_injective
    change W = (⊤ : Submodule ℂ K).map K.subtype
    rw [Submodule.map_top, Submodule.range_subtype, h]

end
end GeometricUnity.D7GradeIrreducible
~~~

[Return to file index](#file-index)

## D7ComplementaryGrades.lean {#source-d7complementarygrades-lean}

Transports exterior representations and their tensor kernels between complementary degrees by Hodge duality.

~~~lean
import D7GradeIrreducible
import D7MiddleTensor

/-!
# Hodge duality for complementary degrees

The determinant metric and oriented volume determine the Hodge map. On the
orthogonal wedge basis it takes a subset to its complement with the volume
sign. The induced tensor equivalence restricts to the joint kernels in
complementary non-middle degrees.
-/

namespace GeometricUnity.D7ComplementaryGrades

open D7Exterior D7Hodge D7Irreducible D7VectorGrades D7GradeIrreducible TensorProduct
open D7MiddleTensor (multiply multiply_pure)
open scoped TensorProduct

noncomputable section

private abbrev pure (k : ℕ) (v : Fin k → Space) : Ext k := exteriorPower.ιMulti ℂ k v

private def complementIndex {m n : ℕ} (h : m + n = 14) (s : Index m) : Index n :=
  ⟨s.valᶜ, by
    change (s.valᶜ).card = n
    rw [Finset.card_compl, Fintype.card_fin, s.prop]
    omega⟩

private def complementEquiv {m n : ℕ} (h : m + n = 14) : Index m ≃ Index n where
  toFun := complementIndex h
  invFun := complementIndex ((Nat.add_comm n m).trans h)
  left_inv s := Subtype.ext (compl_compl s.val)
  right_inv s := Subtype.ext (compl_compl s.val)

private theorem disjoint_iff_complement {m n : ℕ} (h : m + n = 14) (s : Index m) (t : Index n) :
    Disjoint s.val t.val ↔ t = complementEquiv h s := by
  constructor
  · intro hd
    apply Subtype.ext
    apply Finset.eq_of_subset_of_card_le
    · intro a ha
      exact Finset.mem_compl.mpr (Finset.disjoint_left.mp hd.symm ha)
    · exact Nat.le_of_eq ((complementEquiv h s).prop.trans t.prop.symm)
  · rintro rfl
    exact disjoint_compl_right

private def topVolume {k : ℕ} (h : k = 14) : Ext k →ₗ[ℂ] ℂ := by
  subst k
  exact volume

private theorem topVolume_basis {k : ℕ} (h : k = 14) (s : Index k) : topVolume h (basis k s) = 1 := by
  subst k
  rw [exteriorPower.basis_apply]
  exact volume_top s

private theorem topVolume_map {k : ℕ} (h : k = 14) (g : splitSpecialOrthogonal) (v : Fin k → Space) :
    topVolume h (pure k (g.val ∘ v)) = topVolume h (pure k v) := by
  subst k
  simp only [topVolume, volume, exteriorPower.alternatingMapLinearEquiv_apply_ιMulti,
    Module.Basis.det_comp, g.prop.1, one_mul]

/-- Oriented top coefficient of a product of complementary exterior powers. -/
def pairing {m n : ℕ} (h : m + n = 14) : Ext m →ₗ[ℂ] Ext n →ₗ[ℂ] ℂ :=
  (multiply m n).compr₂ₛₗ (topVolume h)

theorem append_map {m n : ℕ} (f : Space →ₗ[ℂ] Space) (u : Fin m → Space) (v : Fin n → Space) :
    Fin.append (f ∘ u) (f ∘ v) = f ∘ Fin.append u v := by
  funext j
  refine Fin.addCases ?_ ?_ j
  · intro i; rw [Function.comp_apply, Fin.append_left, Fin.append_left]; rfl
  · intro i; rw [Function.comp_apply, Fin.append_right, Fin.append_right]; rfl

private theorem pairing_invariant {m n : ℕ} (h : m + n = 14) (g : splitSpecialOrthogonal)
    (x : Ext m) (y : Ext n) :
    pairing h (exteriorRepresentation m g x) (exteriorRepresentation n g y) = pairing h x y := by
  let A := exteriorRepresentation m g
  let B := exteriorRepresentation n g
  have he : (((pairing h).comp A).flip.comp B).flip = pairing h := by
    apply ext_on_wedges
    intro u
    apply ext_on_wedges
    intro v
    change pairing h (exteriorPower.map m g.val (pure m u)) (exteriorPower.map n g.val (pure n v)) = _
    simp only [exteriorPower.map_apply_ιMulti, pairing, LinearMap.compr₂ₛₗ_apply,
      multiply_pure, append_map, topVolume_map]
  exact DFunLike.congr_fun (DFunLike.congr_fun he x) y

theorem metric_map_invariant (k : ℕ) (f : Space →ₗ[ℂ] Space)
    (hf : ∀ x y, splitForm (f x) (f y) = splitForm x y) (x y : Ext k) :
    exteriorMetric k (exteriorPower.map k f x) (exteriorPower.map k f y) = exteriorMetric k x y := by
  let A := exteriorPower.map k f
  have he : (((exteriorMetric k).comp A).flip.comp A).flip = exteriorMetric k := by
    apply ext_on_wedges
    intro u
    apply ext_on_wedges
    intro v
    change exteriorMetric k (exteriorPower.map k f (pure k u)) (exteriorPower.map k f (pure k v)) = _
    simp only [exteriorPower.map_apply_ιMulti, exteriorMetric_pure, Function.comp_apply, hf]
  exact DFunLike.congr_fun (DFunLike.congr_fun he x) y

theorem metric_invariant (k : ℕ) (g : splitSpecialOrthogonal) (x y : Ext k) :
    exteriorMetric k (exteriorRepresentation k g x) (exteriorRepresentation k g y) = exteriorMetric k x y :=
  metric_map_invariant k g.val g.prop.2 x y

private theorem pairing_zero {m n : ℕ} (h : m + n = 14) (s : Index m) (t : Index n)
    (ht : t ≠ complementEquiv h s) : pairing h (basis m s) (basis n t) = 0 := by
  have hz : multiply m n (basis m s) (basis n t) = 0 := by
    apply Subtype.ext
    change (basis m s).val * (basis n t).val = 0
    simpa only [exteriorPower.basis_apply, exteriorPower.ιMulti_family_apply_coe] using
      ExteriorAlgebra.ιMulti_family_mul_of_not_disjoint ℂ orthBasis s t (mt (disjoint_iff_complement h s t).mp ht)
  change topVolume h (multiply m n (basis m s) (basis n t)) = 0
  rw [hz, map_zero]

private def scale {m n : ℕ} (h : m + n = 14) (s : Index m) : ℂ :=
  pairing h (basis m s) (basis n (complementEquiv h s))

private theorem scale_ne_zero {m n : ℕ} (h : m + n = 14) (s : Index m) : scale h s ≠ 0 := by
  let t := complementEquiv h s
  have hd : Disjoint s.val t.val := disjoint_compl_right
  let p := (Set.powersetCard.permOfDisjoint hd).sign
  have hm : multiply m n (basis m s) (basis n t) =
      p • basis (m + n) (Set.powersetCard.disjUnion hd) := by
    apply Subtype.ext
    change (basis m s).val * (basis n t).val =
      (p • basis (m + n) (Set.powersetCard.disjUnion hd) : Ext (m + n)).val
    simpa only [exteriorPower.basis_apply, exteriorPower.ιMulti_family_apply_coe,
      Submodule.coe_smul_of_tower, p] using
      ExteriorAlgebra.ιMulti_family_mul_of_disjoint ℂ orthBasis s t hd
  change topVolume h (multiply m n (basis m s) (basis n t)) ≠ 0
  rw [hm]
  rcases Int.units_eq_one_or p with hp | hp
  · rw [hp, one_smul, topVolume_basis]
    exact one_ne_zero
  · have hneg : (-1 : ℤˣ) • basis (m + n) (Set.powersetCard.disjUnion hd) =
        -basis (m + n) (Set.powersetCard.disjUnion hd) := by simp
    rw [hp, hneg, map_neg, topVolume_basis]
    norm_num

/-- The Hodge linear equivalence sends each coordinate wedge to its signed
complement. Both degrees use the same orthonormal orientation. -/
def starEquiv {m n : ℕ} (h : m + n = 14) : Ext m ≃ₗ[ℂ] Ext n :=
  (basis m).equiv ((basis n).unitsSMul fun t =>
    Units.mk0 (scale h ((complementEquiv h).symm t)) (scale_ne_zero h _)) (complementEquiv h)

private theorem starEquiv_basis {m n : ℕ} (h : m + n = 14) (s : Index m) :
    starEquiv h (basis m s) = scale h s • basis n (complementEquiv h s) := by
  simp only [starEquiv, Module.Basis.equiv_apply, Module.Basis.unitsSMul_apply,
    Equiv.symm_apply_apply, Units.smul_def, Units.val_mk0]

theorem starEquiv_complement {m n : ℕ} (h : m + n = 14) (s : Index m) :
    ∃ t : Index n, t.val = s.valᶜ ∧ ∃ a : ℂ, a ≠ 0 ∧ starEquiv h (basis m s) = a • basis n t :=
  ⟨complementEquiv h s, rfl, scale h s, scale_ne_zero h s, starEquiv_basis h s⟩

theorem metric_starEquiv {m n : ℕ} (h : m + n = 14) (x : Ext m) (y : Ext n) :
    exteriorMetric n (starEquiv h x) y = pairing h x y := by
  have he : (exteriorMetric n).comp (starEquiv h).toLinearMap = pairing h := by
    apply (basis m).ext
    intro s
    apply (basis n).ext
    intro t
    change exteriorMetric n (starEquiv h (basis m s)) (basis n t) = _
    simp only [starEquiv_basis, map_smul, LinearMap.smul_apply, exteriorMetric_axis,
      Module.Basis.coord_apply, Module.Basis.repr_self, Finsupp.single_apply]
    by_cases ht : t = complementEquiv h s
    · subst t
      simp [scale]
    · rw [if_neg ht, smul_zero, pairing_zero h s t ht]
  exact DFunLike.congr_fun (DFunLike.congr_fun he x) y

theorem exterior_surjective (n : ℕ) (g : splitSpecialOrthogonal) :
    Function.Surjective (exteriorRepresentation n g) := by
  let e := LinearMap.equivOfIsUnitDet (g.prop.1 ▸ isUnit_one : IsUnit g.val.det)
  have he : e.toLinearMap = g.val := LinearMap.coe_equivOfIsUnitDet _
  intro w
  refine ⟨exteriorPower.map n e.symm.toLinearMap w, ?_⟩
  change (exteriorPower.map n g.val).comp (exteriorPower.map n e.symm.toLinearMap) w = w
  rw [← exteriorPower.map_comp, ← he, LinearEquiv.comp_coe, LinearEquiv.symm_trans_self,
    LinearEquiv.refl_toLinearMap, exteriorPower.map_id, LinearMap.id_apply]

theorem starEquiv_equivariant {m n : ℕ} (h : m + n = 14) (g : splitSpecialOrthogonal) (x : Ext m) :
    starEquiv h (exteriorRepresentation m g x) = exteriorRepresentation n g (starEquiv h x) := by
  apply exteriorMetric_injective n
  apply LinearMap.ext
  intro y
  obtain ⟨w, rfl⟩ := exterior_surjective n g y
  rw [metric_starEquiv, pairing_invariant, metric_invariant, metric_starEquiv]

/-- Hodge equivalence of the complementary exterior representations. -/
def exteriorDuality {m n : ℕ} (h : m + n = 14) :
    (exteriorRepresentation m).Equiv (exteriorRepresentation n) :=
  Representation.Equiv.mk (starEquiv h) (fun g => LinearMap.ext (starEquiv_equivariant h g))

/-- Hodge equivalence tensoring on the left by the vector representation. -/
def tensorDuality {m n : ℕ} (h : m + n = 14) : (action m).Equiv (action n) :=
  Representation.Equiv.mk (TensorProduct.congr (LinearEquiv.refl ℂ Space) (starEquiv h)) (by
    intro g
    apply TensorProduct.ext'
    intro x u
    simp only [LinearMap.comp_apply, action_tmul, LinearEquiv.coe_coe, TensorProduct.congr_tmul,
      LinearEquiv.refl_apply]
    congr 1
    exact starEquiv_equivariant h g u)

/-- The degree-fourteen vector product is another copy of the vector action. -/
def degreeFourteen : (action 14).Equiv D7VectorTensor.vectorAction :=
  (tensorDuality (m := 14) (n := 0) (by decide)).trans degreeZero

private theorem pairing_middle (x y : Mid) : pairing (m := 7) (n := 7) (by decide) x y = volumePair x y := by
  have he : pairing (m := 7) (n := 7) (by decide) = volumePair := by
    apply ext_on_wedges
    intro u
    apply ext_on_wedges
    intro v
    simp only [pairing, LinearMap.compr₂ₛₗ_apply, multiply_pure, topVolume, volume,
      exteriorPower.alternatingMapLinearEquiv_apply_ιMulti, volumePair_pure]
  exact DFunLike.congr_fun (DFunLike.congr_fun he x) y

/-- In degree seven the general Hodge map has the same orientation as the
middle-degree star used to define the two signed sectors. -/
theorem starEquiv_middle (x : Mid) : starEquiv (m := 7) (n := 7) (by decide) x = star x := by
  apply exteriorMetric_injective 7
  apply LinearMap.ext
  intro y
  rw [metric_starEquiv, pairing_middle]
  exact (metric_star x y).symm

private abbrev kernelRank (n : ℕ) :=
  14 * Nat.choose 14 (n + 1) - Nat.choose 14 (n + 2) - Nat.choose 14 n

private theorem complementary_ranks :
    ∀ p q : Fin 13, (p.val + 1) + (q.val + 1) = 14 →
      Nat.choose 14 (q.val + 2) < kernelRank p.val ∧ Nat.choose 14 q.val < kernelRank p.val ∧
        kernelRank p.val = kernelRank q.val := by
  decide +kernel

private theorem ext_finrank (k : ℕ) : Module.finrank ℂ (Ext k) = Nat.choose 14 k := by
  rw [exteriorPower.finrank_eq, Module.finrank_pi, Fintype.card_fin]

private theorem intertwiner_zero_of_small_target {U W : Type*}
    [AddCommGroup U] [AddCommGroup W] [Module ℂ U] [Module ℂ W] [Module.Finite ℂ W]
    {ρ : Representation ℂ splitSpecialOrthogonal U} {σ : Representation ℂ splitSpecialOrthogonal W}
    (hρ : ρ.IsIrreducible) (f : Representation.IntertwiningMap ρ σ)
    (h : Module.finrank ℂ W < Module.finrank ℂ U) (x : U) : f x = 0 := by
  rcases hρ.eq_bot_or_eq_top f.ker with hb | ht
  · have hf : f.toLinearMap.ker = ⊥ := congrArg Subrepresentation.toSubmodule hb
    exact (not_le_of_gt h (LinearMap.finrank_le_finrank_of_injective (LinearMap.ker_eq_bot.mp hf))).elim
  · have hx : x ∈ f.ker := by rw [ht]; exact Submodule.mem_top
    exact (Representation.IntertwiningMap.mem_ker ρ σ f x).mp hx

set_option backward.isDefEq.respectTransparency false in
private theorem projectedDual_zero (p q : Fin 13) (h : (p.val + 1) + (q.val + 1) = 14) (hp : p.val ≠ 6)
    {W : Type} [AddCommGroup W] [Module ℂ W] [Module.Finite ℂ W]
    (σ : Representation ℂ splitSpecialOrthogonal W) (F : Product (q.val + 1) →ₗ[ℂ] W)
    (hF : ∀ g, F.comp (action (q.val + 1) g) = (σ g).comp F)
    (hd : Module.finrank ℂ W < Module.finrank ℂ (jointKernel p.val)) (x : ↥(jointKernel p.val)) :
    F ((tensorDuality h).toLinearEquiv x.val) = 0 := by
  let d := tensorDuality h
  let f := (F.comp d.toLinearMap).comp (jointKernel p.val).subtype
  have hf (g : splitSpecialOrthogonal) (y : ↥(jointKernel p.val)) :
      f (jointKernelAction p.val g y) = σ g (f y) := by
    change F (d.toLinearEquiv (action (p.val + 1) g y.val)) = σ g (F (d.toLinearEquiv y.val))
    have he : d.toLinearEquiv (action (p.val + 1) g y.val) = action (q.val + 1) g (d.toLinearEquiv y.val) :=
      Representation.IntertwiningMap.isIntertwining (action (p.val + 1)) (action (q.val + 1))
        d.toIntertwiningMap g y.val
    rw [he]
    exact DFunLike.congr_fun (hF g) (d.toLinearEquiv y.val)
  exact intertwiner_zero_of_small_target (jointKernel_isIrreducible p hp)
    (f.intertwiningMap_of_isIntertwiningMap _ σ hf) hd x

private theorem tensorDual_mem_jointKernel (p q : Fin 13) (h : (p.val + 1) + (q.val + 1) = 14)
    (hp : p.val ≠ 6) (x : ↥(jointKernel p.val)) :
    (tensorDuality h).toLinearEquiv x.val ∈ jointKernel q.val := by
  obtain ⟨hw, hc, _⟩ := complementary_ranks p q h
  rw [mem_jointKernel]
  constructor
  · apply projectedDual_zero p q h hp (exteriorRepresentation (q.val + 2)) _ (wedge_equivariant _) _ x
    rw [ext_finrank, jointKernel_finrank p.val (by omega)]
    exact hw
  · apply projectedDual_zero p q h hp (exteriorRepresentation q.val) _ (contract_equivariant _) _ x
    rw [ext_finrank, jointKernel_finrank p.val (by omega)]
    exact hc

set_option backward.isDefEq.respectTransparency false in
/-- Tensor Hodge duality restricts to an equivalence of the irreducible joint
kernels in complementary non-middle grades. -/
def residualDuality (p q : Fin 13) (h : (p.val + 1) + (q.val + 1) = 14) (hp : p.val ≠ 6) :
    (jointKernelAction p.val).Equiv (jointKernelAction q.val) := by
  let d := tensorDuality h
  let K := jointKernel p.val
  let L := jointKernel q.val
  let f : K →ₗ[ℂ] L := (d.toLinearMap.comp K.subtype).codRestrict L (tensorDual_mem_jointKernel p q h hp)
  have hi : Function.Injective f := fun x y hxy =>
    Subtype.ext (d.toLinearEquiv.injective (congrArg Subtype.val hxy))
  have hr : Module.finrank ℂ K = Module.finrank ℂ L := by
    change Module.finrank ℂ (jointKernel p.val) = Module.finrank ℂ (jointKernel q.val)
    rw [jointKernel_finrank p.val (by omega), jointKernel_finrank q.val (by omega)]
    exact (complementary_ranks p q h).2.2
  have hs : Function.Surjective f :=
    (LinearMap.injective_iff_surjective_of_finrank_eq_finrank (K := ℂ) (V := ↥K) (V₂ := ↥L) hr (f := f)).mp hi
  refine Representation.Equiv.mk (LinearEquiv.ofBijective f ⟨hi, hs⟩) (fun g => ?_)
  apply LinearMap.ext
  intro x
  apply Subtype.ext
  exact Representation.IntertwiningMap.isIntertwining (action (p.val + 1)) (action (q.val + 1))
    d.toIntertwiningMap g x.val

private theorem exterior_rank_matches :
    ∀ p q : Fin 15, Nat.choose 14 p.val = Nat.choose 14 q.val → p = q ∨ p.val + q.val = 14 := by
  decide +kernel

private theorem residual_rank_matches :
    ∀ p q : Fin 13, kernelRank p.val = kernelRank q.val →
      p = q ∨ (p.val + 1) + (q.val + 1) = 14 := by
  decide +kernel

private theorem residual_rank_ne_exterior :
    ∀ (p : Fin 13) (q : Fin 15), kernelRank p.val ≠ Nat.choose 14 q.val := by
  decide +kernel

/-- The full exterior powers are equivalent exactly for equal or complementary degrees. -/
theorem exterior_equiv_iff (p q : Fin 15) :
    Nonempty ((exteriorRepresentation p.val).Equiv (exteriorRepresentation q.val)) ↔
      p = q ∨ p.val + q.val = 14 := by
  constructor
  · rintro ⟨e⟩
    have he := e.toLinearEquiv.finrank_eq
    rw [ext_finrank, ext_finrank] at he
    exact exterior_rank_matches p q he
  · rintro (rfl | h)
    · exact ⟨Representation.Equiv.refl _⟩
    · exact ⟨exteriorDuality h⟩

/-- The irreducible non-middle residuals are equivalent exactly for equal or
complementary input degrees. The indexing of `jointKernel` is one below the
exterior input degree. -/
theorem residual_equiv_iff (p q : Fin 13) (hp : p.val ≠ 6) :
    Nonempty ((jointKernelAction p.val).Equiv (jointKernelAction q.val)) ↔
      p = q ∨ (p.val + 1) + (q.val + 1) = 14 := by
  constructor
  · rintro ⟨e⟩
    have he := e.toLinearEquiv.finrank_eq
    rw [jointKernel_finrank p.val (by omega), jointKernel_finrank q.val (by omega)] at he
    exact residual_rank_matches p q he
  · rintro (rfl | h)
    · exact ⟨Representation.Equiv.refl _⟩
    · exact ⟨residualDuality p q h hp⟩

theorem residual_not_equiv_exterior (p : Fin 13) (q : Fin 15) :
    ¬ Nonempty ((jointKernelAction p.val).Equiv (exteriorRepresentation q.val)) := by
  rintro ⟨e⟩
  have he := e.toLinearEquiv.finrank_eq
  rw [jointKernel_finrank p.val (by omega), ext_finrank] at he
  exact residual_rank_ne_exterior p q he

end
end GeometricUnity.D7ComplementaryGrades
~~~

[Return to file index](#file-index)

## D7SignedDistinction.lean {#source-d7signeddistinction-lean}

Distinguishes the two signed middle constituents using a diagonal torus action.

~~~lean
import D7ComplementaryGrades

/-!
# Separation of the signed middle constituents

One diagonal torus element detects the distinction between the two signs.
For the exterior action the top eigenvalue has only the all-plus coordinate
wedge. For the vector tensor action each top eigenvector has that same
exterior factor. Both eigenspaces lie in the negative Hodge sector.
-/

namespace GeometricUnity.D7SignedDistinction

open D7Exterior D7Hodge D7Irreducible D7VectorGrades D7MiddleTensor
open scoped BigOperators TensorProduct

noncomputable section

private abbrev plusIndex := highestPlus (7 : Fin 15)
private abbrev nullBasis := axisBasis.exteriorPower 7
private abbrev nullTensorBasis := axisBasis.tensorProduct nullBasis

private def exponent (s : Finset Axis) : ℤ := ∑ i ∈ s, axisSign i

private theorem axisSign_le_one (i : Axis) : axisSign i ≤ 1 := by
  unfold axisSign
  split <;> norm_num

private theorem plus_axis_iff : ∀ i : Axis, i ∈ plusIndex.val ↔ axisSign i = 1 := by decide +kernel

private theorem plus_exponent : exponent plusIndex.val = 7 := by
  unfold exponent
  rw [Finset.sum_congr rfl (fun i hi => (plus_axis_iff i).mp hi), Finset.sum_const]
  rfl

private theorem plusIndex_of_max (s : Index 7) (hs : 7 ≤ exponent s.val) : s = plusIndex := by
  apply Subtype.ext
  apply Finset.eq_of_subset_of_card_le _ (Nat.le_of_eq (plusIndex.prop.trans s.prop.symm))
  intro j hj
  by_contra hn
  have hlt : axisSign j < 1 :=
    lt_of_le_of_ne (axisSign_le_one j) (fun he => hn ((plus_axis_iff j).mpr he))
  have hh : exponent s.val < ∑ i ∈ s.val, (1 : ℤ) :=
    Finset.sum_lt_sum (fun i _ => axisSign_le_one i) ⟨j, hj, hlt⟩
  rw [Finset.sum_const, show s.val.card = 7 from s.prop] at hh
  norm_num at hh
  omega

private def t : Pair → ℂˣ := fun _ => Units.mk0 (2 : ℂ) (by norm_num)
private def g : splitSpecialOrthogonal := torusElement t

private theorem scale_t (i : Axis) : (scale t i : ℂ) = (2 : ℂ) ^ axisSign i := by
  simp [scale, t]

private theorem exponent_power (s : Finset Axis) : (∏ i ∈ s, (2 : ℂ) ^ axisSign i) = (2 : ℂ) ^ exponent s := by
  induction s using Finset.induction_on with
  | empty => simp [exponent]
  | @insert i s hi ih => simp [exponent, hi, ih, zpow_add₀ (show (2 : ℂ) ≠ 0 by norm_num)]

private theorem exterior_diagonal (s : Index 7) :
    exteriorRepresentation 7 g (nullBasis s) = (2 : ℂ) ^ exponent s.val • nullBasis s := by
  change exteriorPower.map 7 (torus t) (nullBasis s) = _
  rw [torus_exterior, ← subset_character, Units.coe_prod]
  simp only [scale_t, exponent_power]

private theorem tensor_diagonal (q : Axis × Index 7) :
    action 7 g (nullTensorBasis q) = (2 : ℂ) ^ (axisSign q.1 + exponent q.2.val) • nullTensorBasis q := by
  rw [Module.Basis.tensorProduct_apply', action_tmul]
  have h₁ : g.val (axisBasis q.1) = (2 : ℂ) ^ axisSign q.1 • axisBasis q.1 := by
    change torus t (axisBasis q.1) = _
    rw [torus_axis, scale_t]
  have h₂ : exteriorPower.map 7 g.val (nullBasis q.2) =
      (2 : ℂ) ^ exponent q.2.val • nullBasis q.2 := exterior_diagonal q.2
  rw [h₁, h₂, TensorProduct.smul_tmul_smul, ← zpow_add₀ (show (2 : ℂ) ≠ 0 by norm_num)]

private theorem two_power_injective : Function.Injective (fun n : ℤ => (2 : ℂ) ^ n) := by
  intro i j hij
  change (2 : ℂ) ^ i = (2 : ℂ) ^ j at hij
  have hr : (2 : ℝ) ^ i = (2 : ℝ) ^ j := by
    apply Complex.ofReal_injective
    simpa only [Complex.ofReal_zpow, Complex.ofReal_ofNat] using hij
  exact (zpow_right_strictMono₀ (a := (2 : ℝ)) (by norm_num)).injective hr

private theorem diagonal_sign {E ι : Type*} [AddCommGroup E] [Module ℂ E] [Fintype ι]
    (b : Module.Basis ι ℂ E) (f J : E →ₗ[ℂ] E) (d : ι → ℂ) (a : ℂ)
    (hf : ∀ s, f (b s) = d s • b s)
    (hJ : ∀ s, d s = a → J (b s) = -b s)
    {x : E} (hx : f x = a • x) : J x = -x := by
  classical
  have hsupport (s : ι) (hs : b.repr x s ≠ 0) : d s = a := by
    let c := b.coord s
    have hc : c.comp f = d s • c := by
      apply b.ext
      intro u
      simp only [LinearMap.comp_apply, hf, map_smul, LinearMap.smul_apply,
        c, Module.Basis.coord_apply, Module.Basis.repr_self, Finsupp.single_apply]
      by_cases hu : s = u <;> simp [hu, eq_comm, smul_eq_mul]
    have he := DFunLike.congr_fun hc x
    change c (f x) = d s • c x at he
    rw [hx, map_smul] at he
    exact (mul_right_cancel₀ hs he).symm
  have hsum := congrArg J (b.sum_repr x)
  simp only [map_sum, map_smul] at hsum
  rw [← hsum]
  calc
    _ = ∑ i, b.repr x i • (-b i) := by
      apply Finset.sum_congr rfl
      intro i _
      by_cases hi : b.repr x i = 0
      · rw [hi, zero_smul, zero_smul]
      · rw [hJ i (hsupport i hi)]
    _ = -x := by simp only [smul_neg, Finset.sum_neg_distrib, b.sum_repr]

private theorem exterior_top_sign (x : Mid)
    (hx : exteriorRepresentation 7 g x = (2 : ℂ) ^ (7 : ℤ) • x) : involution x = -x := by
  apply diagonal_sign nullBasis (exteriorRepresentation 7 g) involution
    (fun s => (2 : ℂ) ^ exponent s.val) _ exterior_diagonal _ hx
  intro s hs
  have he : exponent s.val = 7 := two_power_injective hs
  rw [plusIndex_of_max s (ge_of_eq he)]
  exact ((mem_sector (-1) (nullBasis plusIndex)).mp highestPlus_mem_sector).trans
    (neg_one_smul ℂ (nullBasis plusIndex))

private theorem tensor_top_sign (x : Product 7)
    (hx : action 7 g x = (2 : ℂ) ^ (8 : ℤ) • x) : tensorInvolution x = -x := by
  apply diagonal_sign nullTensorBasis (action 7 g) tensorInvolution
    (fun s => (2 : ℂ) ^ (axisSign s.1 + exponent s.2.val)) _ tensor_diagonal _ hx
  intro ⟨i, s⟩ hs
  have he : axisSign i + exponent s.val = 8 := two_power_injective hs
  have hs' : s = plusIndex := plusIndex_of_max s (by have := axisSign_le_one i; omega)
  subst s
  have hJ := (mem_sector (-1) (nullBasis plusIndex)).mp highestPlus_mem_sector
  rw [neg_one_smul ℂ (nullBasis plusIndex)] at hJ
  rw [Module.Basis.tensorProduct_apply', tensorInvolution, TensorProduct.map_tmul, LinearMap.id_apply, hJ,
    TensorProduct.tmul_neg]

private theorem zero_of_eq_neg {E : Type*} [AddCommGroup E] [Module ℂ E] (x : E) (hx : x = -x) : x = 0 := by
  have hs : (2 : ℂ) • x = 0 := by rw [two_smul]; exact add_eq_zero_iff_eq_neg.mpr hx
  exact (smul_eq_zero.mp hs).resolve_left (by norm_num)

/-- The two signed middle exterior representations have distinct isomorphism classes. -/
theorem exterior_sectors_inequivalent :
    ¬ Nonempty ((sectorRepresentation (-1)).Equiv (sectorRepresentation 1)) := by
  rintro ⟨e⟩
  let x : ↥(sector (-1)) := ⟨nullBasis plusIndex, highestPlus_mem_sector⟩
  let y := e.toLinearEquiv x
  have hx : sectorRepresentation (-1) g x = (2 : ℂ) ^ (7 : ℤ) • x := by
    apply Subtype.ext
    change exteriorRepresentation 7 g (nullBasis plusIndex) = _
    rw [exterior_diagonal, plus_exponent]
    rfl
  have h := Representation.IntertwiningMap.isIntertwining (sectorRepresentation (-1))
    (sectorRepresentation 1) e.toIntertwiningMap g x
  change e.toLinearEquiv (sectorRepresentation (-1) g x) = sectorRepresentation 1 g y at h
  rw [hx, map_smul] at h
  have hy : exteriorRepresentation 7 g y.val = (2 : ℂ) ^ (7 : ℤ) • y.val :=
    congrArg Subtype.val h.symm
  have hp := (mem_sector 1 y.val).mp y.prop
  rw [one_smul, exterior_top_sign y.val hy] at hp
  have hz : y = 0 := Subtype.ext (zero_of_eq_neg y.val hp.symm)
  exact highestPlus_ne_zero (7 : Fin 15) (congrArg Subtype.val (e.toLinearEquiv.map_eq_zero_iff.mp hz))

set_option backward.isDefEq.respectTransparency false in
/-- The two signed middle residual representations have distinct isomorphism classes. -/
theorem residual_sectors_inequivalent :
    ¬ Nonempty ((residualSectorAction (-1)).Equiv (residualSectorAction 1)) := by
  rintro ⟨e⟩
  let x : ↥(residualSector (-1)) := ⟨plusLabelCandidate, plusLabelCandidate_sector⟩
  let y := e.toLinearEquiv x
  have hx : residualSectorAction (-1) g x = (2 : ℂ) ^ (8 : ℤ) • x := by
    have hB : nullTensor plusIndex = nullTensorBasis (plusAxis 0, plusIndex) :=
      (Module.Basis.tensorProduct_apply' axisBasis nullBasis (plusAxis 0, plusIndex)).symm
    have he : action 7 g (nullTensor plusIndex) = (2 : ℂ) ^ (8 : ℤ) • nullTensor plusIndex := by
      rw [hB, tensor_diagonal, plus_exponent, show axisSign (plusAxis 0) = 1 by decide,
        show (1 + 7 : ℤ) = 8 by decide]
    apply Subtype.ext
    apply Subtype.ext
    exact he
  have h := Representation.IntertwiningMap.isIntertwining (residualSectorAction (-1))
    (residualSectorAction 1) e.toIntertwiningMap g x
  change e.toLinearEquiv (residualSectorAction (-1) g x) = residualSectorAction 1 g y at h
  rw [hx, map_smul] at h
  have hy : action 7 g y.val.val = (2 : ℂ) ^ (8 : ℤ) • y.val.val :=
    congrArg (fun z : ↥(residualSector 1) => z.val.val) h.symm
  have hp := tensorInvolution_of_mem_residualSector 1 y.val y.prop
  rw [one_smul, tensor_top_sign y.val.val hy] at hp
  have hz : y = 0 := Subtype.ext (Subtype.ext (zero_of_eq_neg y.val.val hp.symm))
  have hx0 := e.toLinearEquiv.map_eq_zero_iff.mp hz
  exact nullTensor_ne_zero plusIndex (congrArg (fun z : ↥(residualSector (-1)) => z.val.val) hx0)

end
end GeometricUnity.D7SignedDistinction
~~~

[Return to file index](#file-index)

## D7TripleInvariants.lean {#source-d7tripleinvariants-lean}

Classifies invariant trilinear exterior forms and bounds the vector and alternating multiplicities.

~~~lean
import D7ComplementaryGrades
import Mathlib.Data.Finset.SymmDiff
import Mathlib.LinearAlgebra.Dual.Basis

/-!
# Invariant forms on three exterior powers

The even coordinate sign changes force a nonzero coefficient of an invariant
form to have empty or full symmetric difference. Within each parity, the
three wedge degrees determine the orbit under signed coordinate permutations.
-/

namespace GeometricUnity.D7TripleInvariants

open D7Exterior D7Hodge D7Irreducible D7VectorGrades
open scoped symmDiff TensorProduct BigOperators

noncomputable section

abbrev Form (r k l : ℕ) := Ext r →ₗ[ℂ] Ext k →ₗ[ℂ] Ext l →ₗ[ℂ] ℂ
abbrev Triple (r k l : ℕ) := Index r × Index k × Index l

def invariantForms (r k l : ℕ) : Submodule ℂ (Form r k l) where
  carrier := {F | ∀ (g : splitSpecialOrthogonal) x y z,
    F (exteriorRepresentation r g x) (exteriorRepresentation k g y) (exteriorRepresentation l g z) = F x y z}
  add_mem' hF hG g x y z := by simp only [LinearMap.add_apply, hF g x y z, hG g x y z]
  zero_mem' := by
    change ∀ (g : splitSpecialOrthogonal) (x : Ext r) (y : Ext k) (z : Ext l), _ = _
    intros; rfl
  smul_mem' c F hF g x y z := by simp only [LinearMap.smul_apply, hF g x y z]

def value {r k l : ℕ} (F : Form r k l) (q : Triple r k l) : ℂ :=
  F (basis r q.1) (basis k q.2.1) (basis l q.2.2)

theorem value_ext {r k l : ℕ} {F G : Form r k l}
    (h : ∀ q : Triple r k l, value F q = value G q) : F = G := by
  apply (basis r).ext
  intro s
  apply (basis k).ext
  intro t
  apply (basis l).ext
  intro u
  exact h (s, t, u)

def parity {r k l : ℕ} (q : Triple r k l) : Finset Axis := (q.1.val ∆ q.2.1.val) ∆ q.2.2.val

theorem subsetFlip_diff (s t : Finset Axis) (i : Axis) :
    subsetFlip (s ∆ t) i = subsetFlip s i * subsetFlip t i := by
  by_cases hs : i ∈ s <;> by_cases ht : i ∈ t <;>
    simp [subsetFlip, Finset.mem_symmDiff, hs, ht]

theorem character_diff (s t : Finset Axis) (i j : Axis) :
    character (s ∆ t) i j = character s i j * character t i j := by
  simp only [character, subsetFlip_diff]
  ring

theorem support_parity {r k l : ℕ} (F : ↥(invariantForms r k l)) (q : Triple r k l)
    (h : value F.val q ≠ 0) : parity q = ∅ ∨ parity q = Finset.univ := by
  classical
  by_contra! hn
  obtain ⟨i, hi⟩ := hn.1
  have hex : ∃ j, j ∉ parity q := by
    by_contra! he
    exact hn.2 (Finset.eq_univ_of_forall he)
  obtain ⟨j, hj⟩ := hex
  have hchar : character (parity q) i j = -1 := by simp [character, subsetFlip, hi, hj]
  have hf := F.prop (doubleFlip i j) (basis r q.1) (basis k q.2.1) (basis l q.2.2)
  rw [doubleFlip_exterior, doubleFlip_exterior, doubleFlip_exterior] at hf
  change _ = value F.val q at hf
  simp only [map_smul, LinearMap.smul_apply, smul_eq_mul] at hf
  change character q.2.2.val i j * (character q.2.1.val i j *
    (character q.1.val i j * value F.val q)) = value F.val q at hf
  have he : character (parity q) i j * value F.val q = value F.val q := by
    rw [parity, character_diff, character_diff]
    calc
      _ = character q.2.2.val i j * (character q.2.1.val i j *
        (character q.1.val i j * value F.val q)) := by ac_rfl
      _ = _ := hf
  rw [hchar, neg_one_mul] at he
  have hz : (2 : ℂ) * value F.val q = 0 := by linear_combination -he
  exact h ((mul_eq_zero.mp hz).resolve_left (by norm_num))

theorem third_of_parity {r k l : ℕ} (q : Triple r k l) (b : Bool)
    (hq : parity q = if b then Finset.univ else ∅) :
    q.2.2.val = if b then (q.1.val ∆ q.2.1.val)ᶜ else q.1.val ∆ q.2.1.val := by
  ext i
  have h := congrArg (fun s : Finset Axis => i ∈ s) hq
  change (i ∈ (q.1.val ∆ q.2.1.val) ∆ q.2.2.val) =
    (i ∈ if b then Finset.univ else ∅) at h
  rw [Finset.mem_symmDiff] at h
  have hh := Iff.of_eq h
  cases b
  · change i ∈ q.2.2.val ↔ i ∈ q.1.val ∆ q.2.1.val
    change (_ ↔ i ∈ (∅ : Finset Axis)) at hh
    simp only [Finset.notMem_empty, iff_false] at hh
    tauto
  · change i ∈ q.2.2.val ↔ i ∈ (q.1.val ∆ q.2.1.val)ᶜ
    change (_ ↔ i ∈ (Finset.univ : Finset Axis)) at hh
    simp only [Finset.mem_univ, iff_true] at hh
    rw [Finset.mem_compl]
    tauto

theorem diff_card (s t : Finset Axis) :
    (s ∆ t).card + 2 * (s ∩ t).card = s.card + t.card := by
  rw [Finset.symmDiff_def, Finset.card_union_of_disjoint]
  · have hs := Finset.card_sdiff_add_card_inter s t
    have ht := Finset.card_sdiff_add_card_inter t s
    rw [Finset.inter_comm t s] at ht
    omega
  · exact Finset.disjoint_left.mpr fun i hi hj => (Finset.mem_sdiff.mp hi).2 (Finset.mem_sdiff.mp hj).1

private def pairCode (s t : Finset Axis) (i : Axis) : Bool × Bool :=
  (decide (i ∈ s), decide (i ∈ t))

private def cell (s t : Finset Axis) : Bool × Bool → Finset Axis
  | (true, true) => s ∩ t
  | (true, false) => s \ t
  | (false, true) => t \ s
  | (false, false) => (s ∪ t)ᶜ

private theorem mem_cell (s t : Finset Axis) (i : Axis) (c : Bool × Bool) :
    i ∈ cell s t c ↔ pairCode s t i = c := by
  obtain ⟨a, b⟩ := c
  cases a <;> cases b <;>
    simp [cell, pairCode, and_comm]

private theorem cell_cards {s t u v : Finset Axis} (hs : s.card = u.card) (ht : t.card = v.card)
    (hi : (s ∩ t).card = (u ∩ v).card) (c : Bool × Bool) :
    (cell s t c).card = (cell u v c).card := by
  obtain ⟨a, b⟩ := c
  cases a <;> cases b
  · simp only [cell, Finset.card_compl]
    have hst := Finset.card_union_add_card_inter s t
    have huv := Finset.card_union_add_card_inter u v
    omega
  · simp only [cell, Finset.card_sdiff, ht, hi]
  · simp only [cell, Finset.card_sdiff, hs, Finset.inter_comm t s, Finset.inter_comm v u, hi]
  · exact hi

private theorem perm_pair_of_code {s t u v : Finset Axis} (σ : Equiv.Perm Axis)
    (he : ∀ a, pairCode u v (σ a) = pairCode s t a) :
    s.map σ.toEmbedding = u ∧ t.map σ.toEmbedding = v := by
  constructor
  · ext i
    obtain ⟨a, rfl⟩ := σ.surjective i
    rw [show σ a ∈ s.map σ.toEmbedding ↔ a ∈ s from Finset.mem_map' σ.toEmbedding]
    have ha := congrArg Prod.fst (he a)
    change decide (σ a ∈ u) = decide (a ∈ s) at ha
    by_cases hu : σ a ∈ u <;> by_cases hs : a ∈ s <;> simp_all
  · ext i
    obtain ⟨a, rfl⟩ := σ.surjective i
    rw [show σ a ∈ t.map σ.toEmbedding ↔ a ∈ t from Finset.mem_map' σ.toEmbedding]
    have ha := congrArg Prod.snd (he a)
    change decide (σ a ∈ v) = decide (a ∈ t) at ha
    by_cases hv : σ a ∈ v <;> by_cases ht : a ∈ t <;> simp_all

private theorem perm_preserves_pairCode {s t u v : Finset Axis} (hs : s.card = u.card) (ht : t.card = v.card)
    (hi : (s ∩ t).card = (u ∩ v).card) :
    ∃ σ : Equiv.Perm Axis, ∀ a, pairCode u v (σ a) = pairCode s t a := by
  let e (c : Bool × Bool) : {a // pairCode s t a = c} ≃ {a // pairCode u v a = c} :=
    (Equiv.subtypeEquivRight (mem_cell s t · c)).symm.trans
      (((cell s t c).equivOfCardEq (cell_cards hs ht hi c)).trans
        (Equiv.subtypeEquivRight (mem_cell u v · c)))
  exact ⟨Equiv.ofFiberEquiv e, Equiv.ofFiberEquiv_map e⟩

private theorem perm_pair {s t u v : Finset Axis} (hs : s.card = u.card) (ht : t.card = v.card)
    (hi : (s ∩ t).card = (u ∩ v).card) :
    ∃ σ : Equiv.Perm Axis, s.map σ.toEmbedding = u ∧ t.map σ.toEmbedding = v := by
  obtain ⟨σ, hσ⟩ := perm_preserves_pairCode hs ht hi
  exact ⟨σ, perm_pair_of_code σ hσ⟩

theorem perm_pair_with_point {s t u v : Finset Axis} {a b : Axis}
    (hs : s.card = u.card) (ht : t.card = v.card)
    (hi : (s ∩ t).card = (u ∩ v).card) (ha : a ∈ s ↔ b ∈ u) (hb : a ∈ t ↔ b ∈ v) :
    ∃ σ : Equiv.Perm Axis, σ a = b ∧ s.map σ.toEmbedding = u ∧ t.map σ.toEmbedding = v := by
  obtain ⟨σ, hσ⟩ := perm_preserves_pairCode hs ht hi
  let τ := σ.trans (Equiv.swap (σ a) b)
  have hcode : pairCode u v (σ a) = pairCode u v b := by
    rw [hσ a]
    simp only [pairCode, propext ha, propext hb]
  have he (x : Axis) : pairCode u v (τ x) = pairCode s t x := by
    rw [← hσ x]
    change pairCode u v (Equiv.swap (σ a) b (σ x)) = pairCode u v (σ x)
    by_cases h₁ : σ x = σ a
    · rw [h₁, Equiv.swap_apply_left, hcode]
    by_cases h₂ : σ x = b
    · rw [h₂, Equiv.swap_apply_right, hcode]
    rw [Equiv.swap_apply_of_ne_of_ne h₁ h₂]
  exact ⟨τ, Equiv.swap_apply_left _ _, perm_pair_of_code τ he⟩

private theorem perm_triple {r k l : ℕ} (q q' : Triple r k l) (b : Bool)
    (h : parity q = if b then Finset.univ else ∅)
    (h' : parity q' = if b then Finset.univ else ∅) :
    ∃ σ : Equiv.Perm Axis,
      permIndex σ q.1 = q'.1 ∧ permIndex σ q.2.1 = q'.2.1 ∧ permIndex σ q.2.2 = q'.2.2 := by
  have hu := third_of_parity q b h
  have hv := third_of_parity q' b h'
  have hdiff : (q.1.val ∆ q.2.1.val).card = (q'.1.val ∆ q'.2.1.val).card := by
    have h₁ := q.2.2.prop
    have h₂ := q'.2.2.prop
    change q.2.2.val.card = l at h₁
    change q'.2.2.val.card = l at h₂
    cases b
    · simp only [Bool.false_eq_true, if_false] at hu hv
      rw [hu] at h₁
      rw [hv] at h₂
      exact h₁.trans h₂.symm
    · simp only [if_true] at hu hv
      rw [hu, Finset.card_compl, Fintype.card_fin] at h₁
      rw [hv, Finset.card_compl, Fintype.card_fin] at h₂
      have hr := Finset.card_le_univ (q.1.val ∆ q.2.1.val)
      have hs := Finset.card_le_univ (q'.1.val ∆ q'.2.1.val)
      rw [Fintype.card_fin] at hr hs
      omega
  have hs := q.1.prop.trans q'.1.prop.symm
  have ht := q.2.1.prop.trans q'.2.1.prop.symm
  have hi : (q.1.val ∩ q.2.1.val).card = (q'.1.val ∩ q'.2.1.val).card := by
    have h₁ := diff_card q.1.val q.2.1.val
    have h₂ := diff_card q'.1.val q'.2.1.val
    omega
  obtain ⟨σ, hs', ht'⟩ := perm_pair hs ht hi
  refine ⟨σ, Subtype.ext hs', Subtype.ext ht', ?_⟩
  apply Subtype.ext
  ext i
  obtain ⟨a, rfl⟩ := σ.surjective i
  change σ a ∈ q.2.2.val.map σ.toEmbedding ↔ σ a ∈ q'.2.2.val
  have hm (s : Finset Axis) : σ a ∈ s.map σ.toEmbedding ↔ a ∈ s := Finset.mem_map' σ.toEmbedding
  have hs₀ : σ a ∈ q'.1.val ↔ a ∈ q.1.val := hs' ▸ hm q.1.val
  have ht₀ : σ a ∈ q'.2.1.val ↔ a ∈ q.2.1.val := ht' ▸ hm q.2.1.val
  rw [hm, hu, hv]
  cases b <;> simp [Finset.mem_symmDiff, hs₀, ht₀]

private theorem same_orbit_zero {r k l : ℕ} (F : ↥(invariantForms r k l)) (q q' : Triple r k l)
    (b : Bool) (h : parity q = if b then Finset.univ else ∅)
    (h' : parity q' = if b then Finset.univ else ∅) (hz : value F.val q' = 0) :
    value F.val q = 0 := by
  obtain ⟨σ, hs, ht, hu⟩ := perm_triple q q' b h h'
  obtain ⟨a, _, ha⟩ := orientedPerm_exterior σ 0 q.1
  obtain ⟨c, _, hc⟩ := orientedPerm_exterior σ 0 q.2.1
  obtain ⟨d, _, hd⟩ := orientedPerm_exterior σ 0 q.2.2
  have he := F.prop (orientedPermAt σ 0) (basis r q.1) (basis k q.2.1) (basis l q.2.2)
  rw [ha, hc, hd, hs, ht, hu] at he
  change _ = value F.val q at he
  simp only [map_smul, LinearMap.smul_apply] at he
  change d • c • a • value F.val q' = value F.val q at he
  rw [hz, smul_zero, smul_zero, smul_zero] at he
  exact he.symm

private abbrev ParityClass (r k l : ℕ) :=
  {b : Bool // ∃ q : Triple r k l, parity q = if b then Finset.univ else ∅}

private def sample {r k l : ℕ} (b : ParityClass r k l) : Triple r k l := Classical.choose b.prop

private theorem sample_parity {r k l : ℕ} (b : ParityClass r k l) :
    parity (sample b) = if b.val then Finset.univ else ∅ := Classical.choose_spec b.prop

private def orbitEvaluation (r k l : ℕ) : invariantForms r k l →ₗ[ℂ] (ParityClass r k l → ℂ) where
  toFun F b := value F.val (sample b)
  map_add' F G := by ext b; rfl
  map_smul' a F := by ext b; rfl

local instance (r k l : ℕ) : AddCommGroup ↥(invariantForms r k l) :=
  Submodule.addCommGroup (R := ℂ) (M := Form r k l) (invariantForms r k l)

private theorem orbitEvaluation_injective (r k l : ℕ) : Function.Injective (orbitEvaluation r k l) := by
  intro A B hab
  apply sub_eq_zero.mp
  let F := A - B
  have hF : orbitEvaluation r k l F = 0 := by rw [map_sub, hab, sub_self]
  change F = 0
  apply Subtype.ext
  apply value_ext
  intro q
  change value F.val q = 0
  by_contra hn
  have hzero (b : ParityClass r k l) : value F.val (sample b) = 0 := congrFun hF b
  rcases support_parity F q hn with he | ho
  · let b : ParityClass r k l := ⟨false, ⟨q, he⟩⟩
    exact hn (same_orbit_zero F q (sample b) b.val he (sample_parity b) (hzero b))
  · let b : ParityClass r k l := ⟨true, ⟨q, ho⟩⟩
    exact hn (same_orbit_zero F q (sample b) b.val ho (sample_parity b) (hzero b))

/-- Arithmetic feasibility of the empty-parity orbit. The witness counts
the axes shared by the first two wedges. -/
def feasible (r k l : ℕ) : Prop :=
  ∃ d : Fin 15, d.val ≤ r ∧ d.val ≤ k ∧ r + k = l + 2 * d.val ∧ r + k ≤ 14 + d.val

instance (r k l : ℕ) : Decidable (feasible r k l) := inferInstanceAs (Decidable (∃ d : Fin 15,
  d.val ≤ r ∧ d.val ≤ k ∧ r + k = l + 2 * d.val ∧ r + k ≤ 14 + d.val))

def parityBound (r k l : ℕ) : ℕ :=
  (if feasible r k l then 1 else 0) + (if feasible r k (14 - l) then 1 else 0)

private theorem feasible_of_parity {r k l : ℕ} (b : ParityClass r k l) :
    feasible r k (if b.val then 14 - l else l) := by
  let q := sample b
  have h := third_of_parity q b.val (sample_parity b)
  let d := q.1.val ∩ q.2.1.val
  have hd : d.card ≤ 14 := by simpa using Finset.card_le_univ d
  have hr : d.card ≤ q.1.val.card := Finset.card_mono Finset.inter_subset_left
  have hk : d.card ≤ q.2.1.val.card := Finset.card_mono Finset.inter_subset_right
  rw [q.1.prop] at hr
  rw [q.2.1.prop] at hk
  have hu := Finset.card_union_add_card_inter q.1.val q.2.1.val
  rw [q.1.prop, q.2.1.prop] at hu
  change (q.1.val ∪ q.2.1.val).card + d.card = r + k at hu
  have hU : (q.1.val ∪ q.2.1.val).card ≤ 14 := by simpa using Finset.card_le_univ (q.1.val ∪ q.2.1.val)
  have hf := diff_card q.1.val q.2.1.val
  rw [q.1.prop, q.2.1.prop] at hf
  change (q.1.val ∆ q.2.1.val).card + 2 * d.card = r + k at hf
  have hl : q.2.2.val.card = l := q.2.2.prop
  refine ⟨⟨d.card, by omega⟩, hr, hk, ?_, by change r + k ≤ 14 + d.card; omega⟩
  change r + k = (if b.val then 14 - l else l) + 2 * d.card
  by_cases hb : b.val = true
  · rw [if_pos hb] at h ⊢
    rw [h, Finset.card_compl, Fintype.card_fin] at hl
    have hc : (q.1.val ∆ q.2.1.val).card ≤ 14 := by simpa using Finset.card_le_univ (q.1.val ∆ q.2.1.val)
    omega
  · rw [if_neg hb] at h ⊢
    rw [h] at hl
    omega

theorem empty_parity_feasible {r k l : ℕ} (q : Triple r k l) (h : parity q = ∅) :
    feasible r k l :=
  feasible_of_parity (⟨false, ⟨q, h⟩⟩ : ParityClass r k l)

/-- A nonzero coefficient has one of two parity types, and the dimensions
of the three wedges permit at most one orbit of each type. -/
theorem finrank_invariantForms_le (r k l : ℕ) :
    Module.finrank ℂ (invariantForms r k l) ≤ parityBound r k l := by
  classical
  let P := ParityClass r k l
  let Q := {b : Bool // feasible r k (if b then 14 - l else l)}
  let f (b : P) : Q := ⟨b.val, feasible_of_parity b⟩
  have hfin : Fintype.card P ≤ Fintype.card Q :=
    Fintype.card_le_of_injective f (fun a b h => Subtype.ext (congrArg (fun x : Q => x.val) h))
  have hcard : Fintype.card Q = parityBound r k l := by
    change Fintype.card {b : Bool // feasible r k (if b then 14 - l else l)} = _
    rw [Fintype.card_subtype]
    have he : (Finset.univ : Finset Bool) = {false, true} := by decide
    rw [he]
    by_cases he : feasible r k l <;> by_cases ho : feasible r k (14 - l) <;>
      simp [Finset.filter_insert, Finset.filter_singleton, parityBound, he, ho]
  have hu := LinearMap.finrank_le_finrank_of_injective (orbitEvaluation_injective r k l)
  rw [Module.finrank_pi] at hu
  exact hu.trans (hfin.trans_eq hcard)

abbrev ExteriorIntertwiners (r k l : ℕ) :=
  Representation.IntertwiningMap ((exteriorRepresentation r).tprod (exteriorRepresentation k))
    (exteriorRepresentation l)

private def asForm {r k l : ℕ} (T : ExteriorIntertwiners r k l) : Form r k l :=
  LinearMap.mk₂ ℂ (fun x y => exteriorMetric l (T (x ⊗ₜ[ℂ] y)))
    (fun x x' y => by simp only [TensorProduct.add_tmul, map_add])
    (fun c x y => by simp only [← TensorProduct.smul_tmul', map_smul])
    (fun x y y' => by simp only [TensorProduct.tmul_add, map_add])
    (fun c x y => by simp only [TensorProduct.tmul_smul, map_smul])

private theorem asForm_invariant {r k l : ℕ} (T : ExteriorIntertwiners r k l) :
    asForm T ∈ invariantForms r k l := by
  intro g x y z
  have h := Representation.IntertwiningMap.isIntertwining
    ((exteriorRepresentation r).tprod (exteriorRepresentation k)) (exteriorRepresentation l) T g (x ⊗ₜ[ℂ] y)
  simp only [Representation.tprod_apply, TensorProduct.map_tmul] at h
  change exteriorMetric l (T (exteriorRepresentation r g x ⊗ₜ[ℂ] exteriorRepresentation k g y))
    (exteriorRepresentation l g z) = exteriorMetric l (T (x ⊗ₜ[ℂ] y)) z
  rw [h, D7ComplementaryGrades.metric_invariant]

private def formOfIntertwiner (r k l : ℕ) : ExteriorIntertwiners r k l →ₗ[ℂ] invariantForms r k l where
  toFun T := ⟨asForm T, asForm_invariant T⟩
  map_add' T U := by
    apply Subtype.ext
    apply LinearMap.ext
    intro x
    apply LinearMap.ext
    intro y
    apply LinearMap.ext
    intro z
    change exteriorMetric l ((T + U) (x ⊗ₜ[ℂ] y)) z = _
    simp only [Representation.IntertwiningMap.coe_add, Pi.add_apply, map_add, LinearMap.add_apply]
    rfl
  map_smul' c T := by
    apply Subtype.ext
    apply LinearMap.ext
    intro x
    apply LinearMap.ext
    intro y
    apply LinearMap.ext
    intro z
    change exteriorMetric l ((c • T) (x ⊗ₜ[ℂ] y)) z = _
    simp only [Representation.IntertwiningMap.coe_smul, Pi.smul_apply, map_smul, LinearMap.smul_apply,
      RingHom.id_apply]
    rfl

private theorem formOfIntertwiner_injective (r k l : ℕ) : Function.Injective (formOfIntertwiner r k l) := by
  intro T U h
  apply Representation.IntertwiningMap.ext
  apply TensorProduct.ext'
  intro x y
  apply exteriorMetric_injective l
  exact DFunLike.congr_fun (DFunLike.congr_fun (congrArg Subtype.val h) x) y

def metricEquiv (l : ℕ) : Ext l ≃ₗ[ℂ] (Ext l →ₗ[ℂ] ℂ) := (basis l).toDualEquiv

theorem metricEquiv_toLinearMap (l : ℕ) : (metricEquiv l).toLinearMap = exteriorMetric l := by
  apply (basis l).ext
  intro s
  apply LinearMap.ext
  intro z
  change (basis l).toDual (basis l s) z = exteriorMetric l (basis l s) z
  rw [Module.Basis.toDual_apply_right, exteriorMetric_axis, Module.Basis.coord_apply]

private theorem formOfIntertwiner_surjective (r k l : ℕ) : Function.Surjective (formOfIntertwiner r k l) := by
  intro F
  let f := (metricEquiv l).symm.toLinearMap.comp (TensorProduct.lift F.val)
  have hmetric (x : Ext r) (y : Ext k) : exteriorMetric l (f (x ⊗ₜ[ℂ] y)) = F.val x y := by
    rw [← metricEquiv_toLinearMap]
    change metricEquiv l ((metricEquiv l).symm (TensorProduct.lift F.val (x ⊗ₜ[ℂ] y))) = _
    rw [LinearEquiv.apply_symm_apply, TensorProduct.lift.tmul]
  let T : ExteriorIntertwiners r k l :=
    { toLinearMap := f
      isIntertwining' g := by
        apply TensorProduct.ext'
        intro x y
        simp only [LinearMap.comp_apply, Representation.tprod_apply, TensorProduct.map_tmul]
        apply exteriorMetric_injective l
        apply LinearMap.ext
        intro z
        obtain ⟨w, rfl⟩ := D7ComplementaryGrades.exterior_surjective l g z
        rw [D7ComplementaryGrades.metric_invariant, hmetric, hmetric]
        exact F.prop g x y w }
  refine ⟨T, Subtype.ext ?_⟩
  apply LinearMap.ext
  intro x
  apply LinearMap.ext
  intro y
  exact hmetric x y

/-- Lowering the output index with the determinant metric identifies
intertwiners with invariant trilinear forms. -/
def exteriorIntertwinerEquiv (r k l : ℕ) : ExteriorIntertwiners r k l ≃ₗ[ℂ] invariantForms r k l :=
  LinearEquiv.ofBijective (formOfIntertwiner r k l)
    ⟨formOfIntertwiner_injective r k l, formOfIntertwiner_surjective r k l⟩

theorem finrank_exteriorIntertwiners_le (r k l : ℕ) :
    Module.finrank ℂ (ExteriorIntertwiners r k l) ≤ parityBound r k l :=
  (exteriorIntertwinerEquiv r k l).finrank_eq.le.trans
    (finrank_invariantForms_le r k l)

set_option maxRecDepth 8192 in
set_option maxHeartbeats 4000000 in
theorem alternating_bounds_by_grade :
    (List.ofFn fun k : Fin 15 => ∑ l : Fin 15, parityBound 3 k.val l.val) =
      D7Counts.expectedRows.map (fun row => row.alternating.toNat) := by decide +kernel

set_option maxRecDepth 8192 in
set_option maxHeartbeats 4000000 in
theorem vector_bounds_by_grade :
    (List.ofFn fun k : Fin 15 => ∑ l : Fin 15, parityBound 1 k.val l.val) =
      D7Counts.expectedRows.map (fun row => row.vector.toNat) := by decide +kernel

set_option maxRecDepth 8192 in
set_option maxHeartbeats 4000000 in
theorem vector_and_alternating_upper_bounds :
    (∑ k : Fin 15, ∑ l : Fin 15, Module.finrank ℂ (ExteriorIntertwiners 1 k.val l.val)) ≤ 56 ∧
    (∑ k : Fin 15, ∑ l : Fin 15, Module.finrank ℂ (ExteriorIntertwiners 3 k.val l.val)) ≤ 96 := by
  constructor
  · have h := Finset.sum_le_sum fun k : Fin 15 => fun _ : k ∈ Finset.univ =>
      Finset.sum_le_sum fun l : Fin 15 => fun _ : l ∈ Finset.univ => finrank_exteriorIntertwiners_le 1 k.val l.val
    exact h.trans (by decide +kernel)
  · have h := Finset.sum_le_sum fun k : Fin 15 => fun _ : k ∈ Finset.univ =>
      Finset.sum_le_sum fun l : Fin 15 => fun _ : l ∈ Finset.univ => finrank_exteriorIntertwiners_le 3 k.val l.val
    exact h.trans (by decide +kernel)

end
end GeometricUnity.D7TripleInvariants
~~~

[Return to file index](#file-index)

## D7TripleMultiplicity.lean {#source-d7triplemultiplicity-lean}

Realizes the trilinear invariants and proves the vector and alternating totals of 56 and 96.

~~~lean
import D7TripleInvariants
import D7Classification

/-!
# Realization of the three-exterior-factor multiplicities

Exterior multiplication realizes disjoint pairings. In the mixed degree-three
case, split off one vector, contract it against the second wedge, and wedge
the other two slots into the result. Hodge duality produces the odd-parity
forms from the even-parity forms.
-/

namespace GeometricUnity.D7TripleMultiplicity

open D7Exterior D7Hodge D7Irreducible D7VectorTensor D7VectorGrades D7TensorColumns
open D7MiddleTensor (multiply multiply_pure)
open D7TensorRotations (contract_wedge_basis_of_ne)
open D7ComplementaryGrades D7TripleInvariants
open scoped TensorProduct BigOperators symmDiff

noncomputable section

private abbrev pure (k : ℕ) (u : Fin k → Space) : Ext k := exteriorPower.ιMulti ℂ k u
private abbrev e := orthBasis

def Orthogonal (f : Space →ₗ[ℂ] Space) : Prop :=
  ∀ x y, splitForm (f x) (f y) = splitForm x y

def orthInvariant {r k l : ℕ} (F : Form r k l) : Prop :=
  ∀ (f : Space →ₗ[ℂ] Space), Orthogonal f → ∀ x y z,
    F (exteriorPower.map r f x) (exteriorPower.map k f y) (exteriorPower.map l f z) = F x y z

private theorem multiply_natural {r k : ℕ} (f : Space →ₗ[ℂ] Space) (x : Ext r) (y : Ext k) :
    multiply r k (exteriorPower.map r f x) (exteriorPower.map k f y) =
      exteriorPower.map (r + k) f (multiply r k x y) := by
  have h : (((multiply r k).comp (exteriorPower.map r f)).flip.comp (exteriorPower.map k f)).flip =
      (multiply r k).compr₂ₛₗ (exteriorPower.map (r + k) f) := by
    apply ext_on_wedges (n := r) (W := Ext k →ₗ[ℂ] Ext (r + k))
    intro u
    apply ext_on_wedges (n := k) (W := Ext (r + k))
    intro v
    simp only [LinearMap.comp_apply, LinearMap.flip_apply, LinearMap.compr₂ₛₗ_apply,
      exteriorPower.map_apply_ιMulti, multiply_pure, append_map]
  exact DFunLike.congr_fun (DFunLike.congr_fun h x) y

private def wedgeForm (r k : ℕ) : Form r k (r + k) :=
  (multiply r k).compr₂ₛₗ (exteriorMetric (r + k))

private theorem wedgeForm_invariant (r k : ℕ) : orthInvariant (wedgeForm r k) := by
  intro f hf x y z
  change exteriorMetric (r + k) (multiply r k (exteriorPower.map r f x) (exteriorPower.map k f y))
    (exteriorPower.map (r + k) f z) = _
  rw [multiply_natural, metric_map_invariant _ _ hf]
  rfl

private theorem wedgeForm_ne_zero (r k : ℕ) (h : r + k ≤ 14) : wedgeForm r k ≠ 0 := by
  have hu : (Finset.univ : Finset Axis).card = 14 := by simp
  obtain ⟨s, _, hs⟩ := Finset.exists_subset_card_eq (s := (Finset.univ : Finset Axis)) (by omega : r ≤ _)
  have hc : sᶜ.card = 14 - r := by rw [Finset.card_compl, Fintype.card_fin, hs]
  obtain ⟨t, ht, htcard⟩ := Finset.exists_subset_card_eq (s := sᶜ) (by omega : k ≤ _)
  have hd : Disjoint s t := disjoint_compl_right.mono_right ht
  let S : Index r := ⟨s, hs⟩
  let T : Index k := ⟨t, htcard⟩
  let U := Set.powersetCard.disjUnion (s := S) (t := T) hd
  let a := (Set.powersetCard.permOfDisjoint (s := S) (t := T) hd).sign
  have hmul : multiply r k (basis r S) (basis k T) = a • basis (r + k) U := by
    apply Subtype.ext
    change (basis r S).val * (basis k T).val = (a • basis (r + k) U : Ext (r + k)).val
    simpa only [exteriorPower.basis_apply, exteriorPower.ιMulti_family_apply_coe,
      Submodule.coe_smul_of_tower, a, U] using
      ExteriorAlgebra.ιMulti_family_mul_of_disjoint ℂ orthBasis S T hd
  intro hz
  have hz' := DFunLike.congr_fun (DFunLike.congr_fun hz (basis r S)) (basis k T)
  change exteriorMetric (r + k) (multiply r k (basis r S) (basis k T)) = 0 at hz'
  have h0 := exteriorMetric_injective (r + k) (hz'.trans (map_zero _).symm)
  rw [hmul] at h0
  have hb : basis (r + k) U = 0 := by
    have h1 := congrArg (fun x : Ext (r + k) => a⁻¹ • x) h0
    simpa only [smul_smul, inv_mul_cancel, one_smul, smul_zero] using h1
  exact (basis (r + k)).ne_zero U hb

theorem contract_natural_left (n : ℕ) (f : Space →ₗ[ℂ] Space) (hf : Orthogonal f)
    (x : Space) (y : Ext (n + 1)) :
    contractLeft n (f x) (exteriorPower.map (n + 1) f y) =
      exteriorPower.map n f (contractLeft n x y) := by
  have h := DFunLike.congr_fun (contract_natural n f hf) (x ⊗ₜ[ℂ] y)
  simpa only [LinearMap.comp_apply, TensorProduct.map_tmul, contract, TensorProduct.lift.tmul] using h

private theorem includeWedge_natural (n : ℕ) (f : Space →ₗ[ℂ] Space) (x : Ext (n + 1)) :
    includeWedge n (exteriorPower.map (n + 1) f x) =
      TensorProduct.map f (exteriorPower.map n f) (includeWedge n x) := by
  have h : (includeWedge n).comp (exteriorPower.map (n + 1) f) =
      (TensorProduct.map f (exteriorPower.map n f)).comp (includeWedge n) := by
    apply ext_on_wedges
    intro v
    simp only [LinearMap.comp_apply, exteriorPower.map_apply_ιMulti, includeWedge_pure, map_smul,
      map_sum, map_zsmul, TensorProduct.map_tmul, Function.comp_apply]
    rfl
  exact DFunLike.congr_fun h x

private def transfer (b c : ℕ) : Space →ₗ[ℂ] Ext b →ₗ[ℂ] Ext (c + 1) →ₗ[ℂ] Ext (b + c) :=
  LinearMap.mk₂ ℂ (fun x u => (multiply b c u).comp (contractLeft c x))
    (fun x x' u => by
      apply LinearMap.ext
      intro y
      simp only [LinearMap.comp_apply, map_add, LinearMap.add_apply])
    (fun a x u => by
      apply LinearMap.ext
      intro y
      simp only [LinearMap.comp_apply, map_smul, LinearMap.smul_apply])
    (fun x u u' => by
      apply LinearMap.ext
      intro y
      simp only [LinearMap.comp_apply, map_add, LinearMap.add_apply])
    (fun a x u => by
      apply LinearMap.ext
      intro y
      simp only [LinearMap.comp_apply, map_smul, LinearMap.smul_apply])

private theorem transfer_apply (b c : ℕ) (x : Space) (u : Ext b) (y : Ext (c + 1)) :
    transfer b c x u y = multiply b c u (contractLeft c x y) := rfl

private def mixedMap (b c : ℕ) : Ext (b + 1) →ₗ[ℂ] Ext (c + 1) →ₗ[ℂ] Ext (b + c) :=
  (TensorProduct.lift (transfer b c)).comp (includeWedge b)

private def mixedForm (b c : ℕ) : Form (b + 1) (c + 1) (b + c) :=
  (mixedMap b c).compr₂ₛₗ (exteriorMetric (b + c))

private theorem mixedForm_invariant (b c : ℕ) : orthInvariant (mixedForm b c) := by
  intro f hf x y z
  have h : ((TensorProduct.lift (transfer b c)).comp (TensorProduct.map f (exteriorPower.map b f))).flip.comp
      (exteriorPower.map (c + 1) f) =
      (((TensorProduct.lift (transfer b c)).compr₂ₛₗ (exteriorPower.map (b + c) f)).flip) := by
    apply LinearMap.ext
    intro y
    apply TensorProduct.ext'
    intro x u
    simp only [LinearMap.comp_apply, LinearMap.flip_apply, TensorProduct.map_tmul,
      TensorProduct.lift.tmul, transfer_apply, LinearMap.compr₂ₛₗ_apply]
    rw [contract_natural_left c f hf, multiply_natural]
  change exteriorMetric (b + c)
    (TensorProduct.lift (transfer b c) (includeWedge b (exteriorPower.map (b + 1) f x)) (exteriorPower.map (c + 1) f y))
    (exteriorPower.map (b + c) f z) = _
  rw [includeWedge_natural]
  have he := DFunLike.congr_fun (DFunLike.congr_fun h y) (includeWedge b x)
  change TensorProduct.lift (transfer b c) (TensorProduct.map f (exteriorPower.map b f) (includeWedge b x))
    (exteriorPower.map (c + 1) f y) = exteriorPower.map (b + c) f (mixedMap b c x y) at he
  rw [he, metric_map_invariant _ _ hf]
  rfl

theorem enlarged_wedge {c : ℕ} (R : Index c) (i : Axis) (hi : i ∉ R.val) :
    ∃ a : ℂ, a ≠ 0 ∧ basis (c + 1) (insertIndex R i hi) =
      a • wedgeLeftLinear c (e i) (basis c R) := by
  have hm : i ∈ (insertIndex R i hi).val := Finset.mem_insert_self _ _
  obtain ⟨a, ha, h⟩ := basis_eq_wedge_erase (insertIndex R i hi) i hm
  have he : eraseIndex (insertIndex R i hi) i hm = R := Subtype.ext (Finset.erase_insert hi)
  rw [he] at h
  exact ⟨a, ha, h⟩

private theorem two_wedge_ne_zero {c : ℕ} (R : Index c) (i j : Axis) (hij : i ≠ j)
    (hi : i ∉ R.val) (hj : j ∉ R.val) :
    wedgeLeftLinear (c + 1) (e i) (wedgeLeftLinear c (e j) (basis c R)) ≠ 0 := by
  let S := insertIndex R j hj
  have hiS : i ∉ S.val := by
    change i ∉ insert j R.val
    simp [hij, hi]
  obtain ⟨a, _, hA⟩ := enlarged_wedge R j hj
  obtain ⟨b, _, hB⟩ := enlarged_wedge S i hiS
  change basis (c + 1) S = _ at hA
  intro h
  rw [hA, map_smul, h, smul_zero, smul_zero] at hB
  exact (basis (c + 2)).ne_zero _ hB

private theorem mixedMap_ne_zero (c : ℕ) (hc : c ≤ 11) :
    ∃ (x : Ext 3) (y : Ext (c + 1)), mixedMap 2 c x y ≠ 0 := by
  let s : Finset Axis := ({0, 1, 2} : Finset Axis)ᶜ
  have hs : s.card = 11 := by decide
  obtain ⟨r, hr, hrc⟩ := Finset.exists_subset_card_eq (s := s) (by omega : c ≤ _)
  let R : Index c := ⟨r, hrc⟩
  have h0 : (0 : Axis) ∉ R.val := fun h => (Finset.mem_compl.mp (hr h)) (by simp)
  have h1 : (1 : Axis) ∉ R.val := fun h => (Finset.mem_compl.mp (hr h)) (by simp)
  have h2 : (2 : Axis) ∉ R.val := fun h => (Finset.mem_compl.mp (hr h)) (by simp)
  let v : Fin 3 → Space := ![e 0, e 1, e 2]
  let y := wedgeLeftLinear c (e 0) (basis c R)
  refine ⟨pure 3 v, y, ?_⟩
  have hy0 : contractLeft c (v 0) y = basis c R := contract_wedge_basis R 0 h0
  have hy1 : contractLeft c (v 1) y = 0 := contract_wedge_basis_of_ne R 1 0 (by decide) h1
  have hy2 : contractLeft c (v 2) y = 0 := contract_wedge_basis_of_ne R 2 0 (by decide) h2
  rw [mixedMap, LinearMap.comp_apply, includeWedge_pure, map_smul, map_sum, Fin.sum_univ_three]
  simp only [map_zsmul, TensorProduct.lift.tmul, LinearMap.smul_apply, LinearMap.add_apply,
    transfer_apply, hy0, hy1, hy2, map_zero, zsmul_zero, add_zero,
    Fin.val_zero, pow_zero, one_zsmul]
  apply smul_ne_zero (by norm_num : (((2 : ℕ) : ℂ) + 1)⁻¹ ≠ 0)
  have hv : (0 : Fin 3).removeNth v = ![e 1, e 2] := by
    funext i
    fin_cases i <;> rfl
  rw [hv]
  have he : (multiply 2 c (pure 2 ![e 1, e 2]) (basis c R)).val =
      (wedgeLeftLinear (c + 1) (e 1) (wedgeLeftLinear c (e 2) (basis c R))).val := by
    change (pure 2 ![e 1, e 2]).val * (basis c R).val =
      ExteriorAlgebra.ι ℂ (e 1) * (ExteriorAlgebra.ι ℂ (e 2) * (basis c R).val)
    rw [exteriorPower.ιMulti_apply_coe, ExteriorAlgebra.ιMulti_apply, List.ofFn_succ, List.ofFn_succ]
    simp only [List.ofFn_zero, List.prod_cons, List.prod_nil, mul_one]
    rw [mul_assoc]
    rfl
  intro hz
  have hv' := congrArg Subtype.val hz
  rw [he] at hv'
  exact two_wedge_ne_zero R 1 2 (by decide) h1 h2 (Subtype.ext hv')

private theorem mixedForm_ne_zero (c : ℕ) (hc : c ≤ 11) : mixedForm 2 c ≠ 0 := by
  obtain ⟨x, y, hxy⟩ := mixedMap_ne_zero c hc
  intro hz
  have h := DFunLike.congr_fun (DFunLike.congr_fun hz x) y
  change exteriorMetric (2 + c) (mixedMap 2 c x y) = 0 at h
  exact hxy (exteriorMetric_injective (2 + c) (h.trans (map_zero _).symm))

private theorem mixedForm_one_ne_zero (c : ℕ) (hc : c ≤ 12) : mixedForm 1 c ≠ 0 := by
  let s : Finset Axis := ({0, 1} : Finset Axis)ᶜ
  have hs : s.card = 12 := by decide
  obtain ⟨r, hr, hrc⟩ := Finset.exists_subset_card_eq (s := s) (by omega : c ≤ _)
  let R : Index c := ⟨r, hrc⟩
  have h0 : (0 : Axis) ∉ R.val := fun h => (Finset.mem_compl.mp (hr h)) (by simp)
  have h1 : (1 : Axis) ∉ R.val := fun h => (Finset.mem_compl.mp (hr h)) (by simp)
  let v : Fin 2 → Space := ![e 0, e 1]
  let y := wedgeLeftLinear c (e 0) (basis c R)
  have hy0 : contractLeft c (v 0) y = basis c R := contract_wedge_basis R 0 h0
  have hy1 : contractLeft c (v 1) y = 0 := contract_wedge_basis_of_ne R 1 0 (by decide) h1
  have hx : mixedMap 1 c (pure 2 v) y ≠ 0 := by
    rw [mixedMap, LinearMap.comp_apply, includeWedge_pure, map_smul, map_sum, Fin.sum_univ_two]
    simp only [map_zsmul, TensorProduct.lift.tmul, LinearMap.smul_apply, LinearMap.add_apply,
      transfer_apply, hy0, hy1, map_zero, zsmul_zero, add_zero, Fin.val_zero, pow_zero, one_zsmul]
    apply smul_ne_zero (by norm_num : (((1 : ℕ) : ℂ) + 1)⁻¹ ≠ 0)
    have hv : (0 : Fin 2).removeNth v = fun _ => e 1 := by
      funext j
      fin_cases j
      rfl
    rw [hv]
    have he : (multiply 1 c (pure 1 (fun _ => e 1)) (basis c R)).val =
        (wedgeLeftLinear c (e 1) (basis c R)).val := by
      change (pure 1 (fun _ => e 1)).val * (basis c R).val = _
      rw [exteriorPower.ιMulti_apply_coe, ExteriorAlgebra.ιMulti_apply, List.ofFn_succ]
      simp only [List.ofFn_zero, List.prod_cons, List.prod_nil, mul_one]
      rfl
    intro h
    have he' := congrArg (fun w : Ext (1 + c) => w.val) h
    rw [he] at he'
    obtain ⟨a, _, ha⟩ := enlarged_wedge R 1 h1
    have hb : wedgeLeftLinear c (e 1) (basis c R) = 0 := Subtype.ext he'
    rw [hb, smul_zero] at ha
    exact (basis (c + 1)).ne_zero _ ha
  intro hz
  have h := DFunLike.congr_fun (DFunLike.congr_fun hz (pure 2 v)) y
  change exteriorMetric (1 + c) (mixedMap 1 c (pure 2 v) y) = 0 at h
  exact hx (exteriorMetric_injective (1 + c) (h.trans (map_zero _).symm))

private def swapLast {r k l : ℕ} (F : Form r k l) : Form r l k where
  toFun x := (F x).flip
  map_add' x y := by
    apply LinearMap.ext
    intro z
    apply LinearMap.ext
    intro w
    simp only [LinearMap.flip_apply, map_add, LinearMap.add_apply]
  map_smul' c x := by
    apply LinearMap.ext
    intro z
    apply LinearMap.ext
    intro w
    simp only [LinearMap.flip_apply, map_smul, LinearMap.smul_apply, RingHom.id_apply]

private theorem swapLast_invariant {r k l : ℕ} {F : Form r k l} (h : orthInvariant F) :
    orthInvariant (swapLast F) := fun f hf x y z => h f hf x z y

private theorem swapLast_ne_zero {r k l : ℕ} {F : Form r k l} (h : F ≠ 0) : swapLast F ≠ 0 := by
  intro hz
  apply h
  apply LinearMap.ext
  intro x
  apply LinearMap.ext
  intro y
  apply LinearMap.ext
  intro z
  exact DFunLike.congr_fun (DFunLike.congr_fun (DFunLike.congr_fun hz x) z) y

theorem even_exists {r k l : ℕ} (hr : r = 1 ∨ r = 3) (h : feasible r k l) :
    ∃ F : Form r k l, orthInvariant F ∧ F ≠ 0 := by
  obtain ⟨d, hdr, hdk, he, hN⟩ := h
  by_cases h0 : d.val = 0
  · have hl : l = r + k := by omega
    subst l
    exact ⟨wedgeForm r k, wedgeForm_invariant r k, wedgeForm_ne_zero r k (by omega)⟩
  by_cases hR : d.val = r
  · have hk : k = r + l := by omega
    subst k
    exact ⟨swapLast (wedgeForm r l), swapLast_invariant (wedgeForm_invariant r l),
      swapLast_ne_zero (wedgeForm_ne_zero r l (by omega))⟩
  have h3 : r = 3 := by omega
  subst r
  by_cases h1 : d.val = 1
  · let c := k - 1
    have hk : k = c + 1 := by dsimp [c]; omega
    have hl : l = 2 + c := by dsimp [c]; omega
    have hc : c ≤ 11 := by dsimp [c]; omega
    rw [hk, hl]
    exact ⟨mixedForm 2 c, mixedForm_invariant 2 c, mixedForm_ne_zero c hc⟩
  · have h2 : d.val = 2 := by omega
    let c := l - 1
    have hl : l = c + 1 := by dsimp [c]; omega
    have hk : k = 2 + c := by dsimp [c]; omega
    have hc : c ≤ 11 := by dsimp [c]; omega
    rw [hk, hl]
    exact ⟨swapLast (mixedForm 2 c), swapLast_invariant (mixedForm_invariant 2 c),
      swapLast_ne_zero (mixedForm_ne_zero c hc)⟩

theorem even_exists_two {k l : ℕ} (h : feasible 2 k l) :
    ∃ F : Form 2 k l, orthInvariant F ∧ F ≠ 0 := by
  obtain ⟨d, hd, hk, he, hN⟩ := h
  by_cases h0 : d.val = 0
  · have hl : l = 2 + k := by omega
    subst l
    exact ⟨wedgeForm 2 k, wedgeForm_invariant 2 k, wedgeForm_ne_zero 2 k (by omega)⟩
  by_cases h2 : d.val = 2
  · have hk' : k = 2 + l := by omega
    subst k
    exact ⟨swapLast (wedgeForm 2 l), swapLast_invariant (wedgeForm_invariant 2 l),
      swapLast_ne_zero (wedgeForm_ne_zero 2 l (by omega))⟩
  have h1 : d.val = 1 := by omega
  let c := k - 1
  have hk' : k = c + 1 := by dsimp [c]; omega
  have hl : l = 1 + c := by dsimp [c]; omega
  have hc : c ≤ 12 := by dsimp [c]; omega
  rw [hk', hl]
  exact ⟨mixedForm 1 c, mixedForm_invariant 1 c, mixedForm_one_ne_zero c hc⟩

theorem reflect_basis {k : ℕ} (s : Index k) :
    exteriorPower.map k vectorReflection (basis k s) = subsetFlip s.val 0 • basis k s := by
  rw [vectorReflection, orthDiagonal_exterior]
  congr 1
  unfold subsetFlip
  by_cases h : (0 : Axis) ∈ s.val
  · rw [if_pos h, Finset.prod_eq_single 0]
    · simp
    · intro j _ hj; simp [hj]
    · exact fun h' => (h' h).elim
  · rw [if_neg h]
    apply Finset.prod_eq_one
    intro j hj
    have h' : j ≠ 0 := fun he => h (he ▸ hj)
    simp [h']

private theorem even_vanishes_on_full {r k l : ℕ} {F : Form r k l}
    (h : orthInvariant F) (q : Triple r k l) (hq : parity q = Finset.univ) : value F q = 0 := by
  have hx := h vectorReflection vectorReflection_isometry (basis r q.1) (basis k q.2.1) (basis l q.2.2)
  simp only [reflect_basis, map_smul, LinearMap.smul_apply, smul_eq_mul] at hx
  change subsetFlip q.2.2.val 0 * (subsetFlip q.2.1.val 0 * (subsetFlip q.1.val 0 * value F q)) =
    value F q at hx
  have hs : subsetFlip (parity q) 0 = -1 := by rw [hq]; simp [subsetFlip]
  rw [parity, subsetFlip_diff, subsetFlip_diff] at hs
  have hz : -value F q = value F q := by
    calc
      _ = (subsetFlip q.1.val 0 * subsetFlip q.2.1.val 0 * subsetFlip q.2.2.val 0) * value F q := by
        rw [hs, neg_one_mul]
      _ = _ := by exact (show _ = _ by ac_rfl).trans hx
  have htwo : (2 : ℂ) * value F q = 0 := by linear_combination -hz
  exact (mul_eq_zero.mp htwo).resolve_left (by norm_num)

private theorem as_invariant {r k l : ℕ} {F : Form r k l} (h : orthInvariant F) :
    F ∈ invariantForms r k l := fun g x y z => h g.val g.prop.2 x y z

private def twistLast {r k l m : ℕ} (h : l + m = 14) (F : Form r k m) : Form r k l where
  toFun x := (LinearMap.lcomp ℂ ℂ (starEquiv h).toLinearMap).comp (F x)
  map_add' x y := by simp only [map_add, LinearMap.comp_add]
  map_smul' c x := by simp only [map_smul, LinearMap.comp_smul, RingHom.id_apply]

private theorem twistLast_apply {r k l m : ℕ} (h : l + m = 14) (F : Form r k m)
    (x : Ext r) (y : Ext k) (z : Ext l) : twistLast h F x y z = F x y (starEquiv h z) := rfl

private theorem twistLast_invariant {r k l m : ℕ} (h : l + m = 14) {F : Form r k m}
    (hF : orthInvariant F) : twistLast h F ∈ invariantForms r k l := by
  intro g x y z
  rw [twistLast_apply, twistLast_apply, starEquiv_equivariant]
  exact hF g.val g.prop.2 x y (starEquiv h z)

private theorem twistLast_ne_zero {r k l m : ℕ} (h : l + m = 14) {F : Form r k m}
    (hF : F ≠ 0) : twistLast h F ≠ 0 := by
  intro hz
  apply hF
  apply LinearMap.ext
  intro x
  apply LinearMap.ext
  intro y
  apply LinearMap.ext
  intro z
  obtain ⟨w, rfl⟩ := (starEquiv h).surjective z
  exact DFunLike.congr_fun (DFunLike.congr_fun (DFunLike.congr_fun hz x) y) w

private theorem odd_vanishes_on_empty {r k l m : ℕ} (h : l + m = 14) {F : Form r k m}
    (hF : orthInvariant F) (q : Triple r k l) (hq : parity q = ∅) : value (twistLast h F) q = 0 := by
  obtain ⟨u, hu, a, _, he⟩ := starEquiv_complement h q.2.2
  let p : Triple r k m := (q.1, q.2.1, u)
  have hqu := third_of_parity q false hq
  have hp : parity p = Finset.univ := by
    change (q.1.val ∆ q.2.1.val) ∆ u.val = Finset.univ
    rw [hu, show q.2.2.val = q.1.val ∆ q.2.1.val from hqu]
    ext i
    rw [Finset.mem_symmDiff]
    simp only [Finset.mem_compl, Finset.mem_univ, iff_true]
    tauto
  change twistLast h F (basis r q.1) (basis k q.2.1) (basis l q.2.2) = 0
  rw [twistLast_apply, he, map_smul]
  change a • value F p = 0
  rw [even_vanishes_on_full hF p hp, smul_zero]

private theorem exists_value_ne_zero {r k l : ℕ} {F : Form r k l} (h : F ≠ 0) :
    ∃ q : Triple r k l, value F q ≠ 0 := by
  by_contra! hn
  exact h (value_ext hn)

theorem even_nonzero_coordinate {r k l : ℕ} {F : Form r k l} (hF : orthInvariant F) (hF0 : F ≠ 0) :
    ∃ q : Triple r k l, parity q = ∅ ∧ value F q ≠ 0 := by
  obtain ⟨q, hq⟩ := exists_value_ne_zero hF0
  have h := support_parity ⟨F, as_invariant hF⟩ q hq
  exact ⟨q, h.resolve_right (fun hp => hq (even_vanishes_on_full hF q hp)), hq⟩

local instance (r k l : ℕ) : AddCommGroup ↥(invariantForms r k l) :=
  Submodule.addCommGroup (R := ℂ) (M := Form r k l) (invariantForms r k l)

private def evaluation {r k l : ℕ} (q : Triple r k l) : invariantForms r k l →ₗ[ℂ] ℂ where
  toFun F := value F.val q
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

private theorem two_le_finrank {r k l : ℕ} (A B : ↥(invariantForms r k l))
    (s t : Triple r k l)
    (hAs : value A.val s ≠ 0) (hBs : value B.val s = 0)
    (hAt : value A.val t = 0) (hBt : value B.val t ≠ 0) :
    2 ≤ Module.finrank ℂ (invariantForms r k l) := by
  let M : ℂ × ℂ →ₗ[ℂ] invariantForms r k l :=
    (LinearMap.fst ℂ ℂ ℂ).smulRight A + (LinearMap.snd ℂ ℂ ℂ).smulRight B
  have he (q : Triple r k l) (p : ℂ × ℂ) :
      evaluation q (M p) = p.1 * value A.val q + p.2 * value B.val q := by
    change evaluation q (p.1 • A + p.2 • B) = _
    rw [map_add, map_smul, map_smul]
    rfl
  have hi : Function.Injective M := by
    intro p q h
    have hs := congrArg (evaluation s) h
    have ht := congrArg (evaluation t) h
    rw [he, he, hBs, mul_zero, add_zero, mul_zero, add_zero] at hs
    rw [he, he, hAt, mul_zero, zero_add, mul_zero, zero_add] at ht
    exact Prod.ext (mul_right_cancel₀ hAs hs) (mul_right_cancel₀ hBt ht)
  simpa using LinearMap.finrank_le_finrank_of_injective hi

private theorem one_le_finrank {r k l : ℕ} (F : ↥(invariantForms r k l)) (hF : F.val ≠ 0) :
    1 ≤ Module.finrank ℂ (invariantForms r k l) := by
  have hex : ∃ x : ↥(invariantForms r k l), x ≠ 0 :=
    ⟨F, fun h => hF (congrArg (fun G : ↥(invariantForms r k l) => G.val) h)⟩
  have hpos : 0 < Module.finrank ℂ (invariantForms r k l) :=
    Module.finrank_pos_iff_exists_ne_zero.mpr hex
  omega

/-- In the vector and alternating channels, each feasible parity contributes
one independent intertwiner for every pair of exterior grades. -/
theorem finrank_exteriorIntertwiners (r k l : ℕ) (hr : r = 1 ∨ r = 3) (hl : l ≤ 14) :
    Module.finrank ℂ (ExteriorIntertwiners r k l) = parityBound r k l := by
  rw [(exteriorIntertwinerEquiv r k l).finrank_eq]
  apply le_antisymm (finrank_invariantForms_le r k l)
  have hsum : l + (14 - l) = 14 := by omega
  by_cases he : feasible r k l <;> by_cases ho : feasible r k (14 - l)
  · obtain ⟨A, hA, hA0⟩ := even_exists hr he
    obtain ⟨B, hB, hB0⟩ := even_exists hr ho
    let X : ↥(invariantForms r k l) := ⟨A, as_invariant hA⟩
    let Y : ↥(invariantForms r k l) := ⟨twistLast hsum B, twistLast_invariant hsum hB⟩
    obtain ⟨s, hs⟩ := exists_value_ne_zero hA0
    obtain ⟨t, ht⟩ := exists_value_ne_zero (twistLast_ne_zero hsum hB0)
    have hsP : parity s = ∅ := (support_parity X s hs).resolve_right (fun h => hs (even_vanishes_on_full hA s h))
    have htP : parity t = Finset.univ :=
      (support_parity Y t ht).resolve_left (fun h => ht (odd_vanishes_on_empty hsum hB t h))
    simp only [parityBound, if_pos he, if_pos ho]
    exact two_le_finrank X Y s t hs (odd_vanishes_on_empty hsum hB s hsP) (even_vanishes_on_full hA t htP) ht
  · obtain ⟨F, hF, hF0⟩ := even_exists hr he
    simpa [parityBound, he, ho] using one_le_finrank ⟨F, as_invariant hF⟩ hF0
  · obtain ⟨F, hF, hF0⟩ := even_exists hr ho
    simpa [parityBound, he, ho] using one_le_finrank
      ⟨twistLast hsum F, twistLast_invariant hsum hF⟩ (twistLast_ne_zero hsum hF0)
  · simp [parityBound, he, ho]

theorem alternating_multiplicities_by_grade :
    (List.ofFn fun k : Fin 15 => ∑ l : Fin 15, Module.finrank ℂ (ExteriorIntertwiners 3 k.val l.val)) =
      D7Counts.expectedRows.map (fun row => row.alternating.toNat) := by
  have h (k l : Fin 15) := finrank_exteriorIntertwiners 3 k.val l.val (Or.inr rfl) (by omega)
  simp_rw [h]
  exact alternating_bounds_by_grade

theorem vector_multiplicities_by_grade :
    (List.ofFn fun k : Fin 15 => ∑ l : Fin 15, Module.finrank ℂ (ExteriorIntertwiners 1 k.val l.val)) =
      D7Counts.expectedRows.map (fun row => row.vector.toNat) := by
  have h (k l : Fin 15) := finrank_exteriorIntertwiners 1 k.val l.val (Or.inl rfl) (by omega)
  simp_rw [h]
  exact vector_bounds_by_grade

set_option maxRecDepth 8192 in
set_option maxHeartbeats 4000000 in
theorem vector_and_alternating_totals :
    (∑ k : Fin 15, ∑ l : Fin 15, Module.finrank ℂ (ExteriorIntertwiners 1 k.val l.val)) = 56 ∧
    (∑ k : Fin 15, ∑ l : Fin 15, Module.finrank ℂ (ExteriorIntertwiners 3 k.val l.val)) = 96 := by
  constructor
  · have h (k l : Fin 15) := finrank_exteriorIntertwiners 1 k.val l.val (Or.inl rfl) (by omega)
    simp_rw [h]
    decide +kernel
  · have h (k l : Fin 15) := finrank_exteriorIntertwiners 3 k.val l.val (Or.inr rfl) (by omega)
    simp_rw [h]
    decide +kernel

section Bundled

open CategoryTheory CategoryTheory.Limits

local instance : HasFiniteBiproducts (FDRep ℂ splitSpecialOrthogonal) :=
  HasFiniteBiproducts.of_hasFiniteProducts

def sourceGrade (r : ℕ) (k : Fin 15) : FDRep ℂ splitSpecialOrthogonal :=
  FDRep.of (V := Ext r ⊗[ℂ] Ext k.val) ((exteriorRepresentation r).tprod (exteriorRepresentation k.val))

def targetGrade (l : Fin 15) : FDRep ℂ splitSpecialOrthogonal :=
  FDRep.of (exteriorRepresentation l.val)

def summedSource (r : ℕ) : FDRep ℂ splitSpecialOrthogonal := ⨁ sourceGrade r

def summedTarget : FDRep ℂ splitSpecialOrthogonal := ⨁ targetGrade

def bundledHomEquiv {U W : Type} [AddCommGroup U] [Module ℂ U] [Module.Finite ℂ U]
    [AddCommGroup W] [Module ℂ W] [Module.Finite ℂ W]
    (ρ : Representation ℂ splitSpecialOrthogonal U) (σ : Representation ℂ splitSpecialOrthogonal W) :
    (FDRep.of ρ ⟶ FDRep.of σ) ≃ₗ[ℂ] ρ.IntertwiningMap σ where
  toFun f :=
    { toLinearMap := f.hom.hom.hom
      isIntertwining' g := congrArg
        (fun f : (FDRep.of ρ).V ⟶ (FDRep.of σ).V => f.hom.hom) (f.comm g) }
  invFun f :=
    { hom := FGModuleCat.ofHom f.toLinearMap
      comm g := FGModuleCat.hom_ext (f.isIntertwining' g) }
  left_inv _ := Action.hom_ext _ _ (FGModuleCat.hom_ext rfl)
  right_inv _ := Representation.IntertwiningMap.ext rfl
  map_add' _ _ := Representation.IntertwiningMap.ext rfl
  map_smul' _ _ := Representation.IntertwiningMap.ext rfl

set_option backward.isDefEq.respectTransparency false in
private def gradeHomEquiv (r : ℕ) (k l : Fin 15) :
    (sourceGrade r k ⟶ targetGrade l) ≃ₗ[ℂ] ExteriorIntertwiners r k.val l.val :=
  bundledHomEquiv (U := Ext r ⊗[ℂ] Ext k.val) (W := Ext l.val)
    ((exteriorRepresentation r).tprod (exteriorRepresentation k.val)) (exteriorRepresentation l.val)

private theorem summedHom_finrank (r : ℕ) : Module.finrank ℂ (summedSource r ⟶ summedTarget) =
    ∑ k : Fin 15, ∑ l : Fin 15, Module.finrank ℂ (ExteriorIntertwiners r k.val l.val) := by
  change Module.finrank ℂ (⨁ sourceGrade r ⟶ ⨁ targetGrade) = _
  rw [(D7Classification.blockHomEquiv ℂ (sourceGrade r) targetGrade).finrank_eq,
    Module.finrank_pi_fintype]
  apply Finset.sum_congr rfl
  intro k _
  rw [Module.finrank_pi_fintype]
  exact Finset.sum_congr rfl fun l _ => (gradeHomEquiv r k l).finrank_eq

/-- The complex Hom dimensions for the vector and Bianchi channels on the
biproduct of all exterior grades. -/
theorem vector_and_bianchi_hom_dimensions :
    Module.finrank ℂ (summedSource 1 ⟶ summedTarget) = 56 ∧
    Module.finrank ℂ (summedSource 3 ⟶ summedTarget) = 96 := by
  rw [summedHom_finrank, summedHom_finrank]
  exact vector_and_alternating_totals

end Bundled

end
end GeometricUnity.D7TripleMultiplicity
~~~

[Return to file index](#file-index)

## D7QuadInvariants.lean {#source-d7quadinvariants-lean}

Classifies the invariant forms with a vector factor and three exterior factors.

~~~lean
import D7TripleMultiplicity

/-!
# Invariant forms with one vector and three exterior factors

In empty parity, a vector coordinate occurs in one or three exterior factors.
The first case gives the three possible partners of the vector slot. A plane
rotation into an unused axis determines the second case from the first.
-/

namespace GeometricUnity.D7QuadInvariants

open D7Exterior D7Hodge D7Irreducible D7VectorTensor D7VectorGrades D7TensorColumns
open D7TensorRotations D7ComplementaryGrades D7TripleMultiplicity
open D7TripleInvariants (character_diff subsetFlip_diff diff_card perm_pair_with_point feasible empty_parity_feasible)
open scoped symmDiff BigOperators TensorProduct

noncomputable section

abbrev Form (k l : ℕ) := Space →ₗ[ℂ] D7TripleInvariants.Form 2 k l

structure Quad (k l : ℕ) where
  axis : Axis
  first : Index 2
  second : Index k
  third : Index l

def invariantForms (k l : ℕ) : Submodule ℂ (Form k l) where
  carrier := {F | ∀ (g : splitSpecialOrthogonal) x y z w,
    F (g.val x) (exteriorRepresentation 2 g y) (exteriorRepresentation k g z)
      (exteriorRepresentation l g w) = F x y z w}
  add_mem' hF hG g x y z w := by simp only [LinearMap.add_apply, hF g x y z w, hG g x y z w]
  zero_mem' := by
    change ∀ (g : splitSpecialOrthogonal) (x : Space) (y : Ext 2) (z : Ext k) (w : Ext l), _ = _
    intros; rfl
  smul_mem' c F hF g x y z w := by simp only [LinearMap.smul_apply, hF g x y z w]

def parity {k l : ℕ} (q : Quad k l) : Finset Axis :=
  ((q.first.val ∆ q.second.val) ∆ {q.axis}) ∆ q.third.val

def code {k l : ℕ} (q : Quad k l) : Bool × Bool :=
  (decide (q.axis ∈ q.first.val), decide (q.axis ∈ q.second.val))

def regular {k l : ℕ} (q : Quad k l) : Prop :=
  q.axis ∉ q.first.val ∨ q.axis ∉ q.second.val

def coefficient {k l : ℕ} (F : Form k l) (q : Quad k l) : ℂ :=
  F (orthBasis q.axis) (basis 2 q.first) (basis k q.second) (basis l q.third)

theorem coefficient_ext {k l : ℕ} {F G : Form k l}
    (h : ∀ q, coefficient F q = coefficient G q) : F = G := by
  apply orthBasis.ext
  intro a
  apply (basis 2).ext
  intro s
  apply (basis k).ext
  intro t
  apply (basis l).ext
  intro u
  exact h ⟨a, s, t, u⟩

private theorem doubleFlip_singleton (i j a : Axis) :
    (doubleFlip i j).val (orthBasis a) = character ({a} : Finset Axis) i j • orthBasis a := by
  simpa only [character, subsetFlip, axisFlip, Finset.mem_singleton, eq_comm] using doubleFlip_basis i j a

set_option maxHeartbeats 600000 in
theorem support_parity {k l : ℕ} (F : ↥(invariantForms k l)) (q : Quad k l)
    (h : coefficient F.val q ≠ 0) : parity q = ∅ ∨ parity q = Finset.univ := by
  classical
  by_contra! hn
  obtain ⟨i, hi⟩ := hn.1
  have hex : ∃ j, j ∉ parity q := by
    by_contra! he
    exact hn.2 (Finset.eq_univ_of_forall he)
  obtain ⟨j, hj⟩ := hex
  have hc : character (parity q) i j = -1 := by simp [character, subsetFlip, hi, hj]
  have he := F.prop (doubleFlip i j) (orthBasis q.axis) (basis 2 q.first)
    (basis k q.second) (basis l q.third)
  rw [doubleFlip_singleton, doubleFlip_exterior, doubleFlip_exterior, doubleFlip_exterior] at he
  simp only [map_smul, LinearMap.smul_apply, smul_eq_mul] at he
  change character q.third.val i j * (character q.second.val i j *
    (character q.first.val i j * (character {q.axis} i j * coefficient F.val q))) = coefficient F.val q at he
  have he' : character (parity q) i j * coefficient F.val q = coefficient F.val q := by
    rw [parity, character_diff, character_diff, character_diff]
    calc
      _ = character q.third.val i j * (character q.second.val i j *
        (character q.first.val i j * (character {q.axis} i j * coefficient F.val q))) := by ac_rfl
      _ = _ := he
  rw [hc, neg_one_mul] at he'
  have hz : (2 : ℂ) * coefficient F.val q = 0 := by linear_combination -he'
  exact h ((mul_eq_zero.mp hz).resolve_left (by norm_num))

theorem third_of_even {k l : ℕ} (q : Quad k l) (h : parity q = ∅) :
    q.third.val = (q.first.val ∆ q.second.val) ∆ {q.axis} :=
  (Finset.symmDiff_eq_empty.mp h).symm

theorem axis_mem_third_even {k l : ℕ} (q : Quad k l) (h : parity q = ∅) :
    q.axis ∈ q.third.val ↔ (q.axis ∈ q.first.val ↔ q.axis ∈ q.second.val) := by
  rw [third_of_even q h]
  simp only [Finset.mem_symmDiff, Finset.mem_singleton, not_true, and_false, false_or, true_and]
  tauto

private theorem pair_diff_card {k l : ℕ} (q : Quad k l) (h : parity q = ∅) :
    (q.first.val ∆ q.second.val).card + 1 = l +
      2 * (if q.axis ∈ q.first.val ∆ q.second.val then 1 else 0) := by
  have he := diff_card (q.first.val ∆ q.second.val) {q.axis}
  rw [← third_of_even q h, q.third.prop, Finset.card_singleton, Finset.inter_singleton] at he
  by_cases ha : q.axis ∈ q.first.val ∆ q.second.val <;> simpa [ha] using he.symm

theorem perm_even {k l : ℕ} (q q' : Quad k l) (h : parity q = ∅) (h' : parity q' = ∅)
    (hc : code q = code q') :
    ∃ σ : Equiv.Perm Axis, σ q.axis = q'.axis ∧ permIndex σ q.first = q'.first ∧
      permIndex σ q.second = q'.second ∧ permIndex σ q.third = q'.third := by
  have h₁ : q.axis ∈ q.first.val ↔ q'.axis ∈ q'.first.val := by
    have he := congrArg Prod.fst hc
    change decide (q.axis ∈ q.first.val) = decide (q'.axis ∈ q'.first.val) at he
    by_cases hq : q.axis ∈ q.first.val <;> by_cases hq' : q'.axis ∈ q'.first.val <;> simp_all
  have h₂ : q.axis ∈ q.second.val ↔ q'.axis ∈ q'.second.val := by
    have he := congrArg Prod.snd hc
    change decide (q.axis ∈ q.second.val) = decide (q'.axis ∈ q'.second.val) at he
    by_cases hq : q.axis ∈ q.second.val <;> by_cases hq' : q'.axis ∈ q'.second.val <;> simp_all
  have hd : (q.first.val ∆ q.second.val).card = (q'.first.val ∆ q'.second.val).card := by
    have hx := pair_diff_card q h
    have hy := pair_diff_card q' h'
    have ha : q.axis ∈ q.first.val ∆ q.second.val ↔ q'.axis ∈ q'.first.val ∆ q'.second.val := by
      simp only [Finset.mem_symmDiff, h₁, h₂]
    by_cases hm : q.axis ∈ q.first.val ∆ q.second.val
    · rw [if_pos hm] at hx
      rw [if_pos (ha.mp hm)] at hy
      omega
    · rw [if_neg hm] at hx
      rw [if_neg (fun h => hm (ha.mpr h))] at hy
      omega
  have hi : (q.first.val ∩ q.second.val).card = (q'.first.val ∩ q'.second.val).card := by
    have hs := diff_card q.first.val q.second.val
    have ht := diff_card q'.first.val q'.second.val
    rw [q.first.prop, q.second.prop] at hs
    rw [q'.first.prop, q'.second.prop] at ht
    omega
  obtain ⟨σ, ha, hs, ht⟩ := perm_pair_with_point (q.first.prop.trans q'.first.prop.symm)
    (q.second.prop.trans q'.second.prop.symm) hi h₁ h₂
  refine ⟨σ, ha, Subtype.ext hs, Subtype.ext ht, ?_⟩
  apply Subtype.ext
  ext i
  obtain ⟨x, rfl⟩ := σ.surjective i
  change σ x ∈ q.third.val.map σ.toEmbedding ↔ σ x ∈ q'.third.val
  have hm (s : Finset Axis) : σ x ∈ s.map σ.toEmbedding ↔ x ∈ s := Finset.mem_map' σ.toEmbedding
  have hs' : σ x ∈ q'.first.val ↔ x ∈ q.first.val := hs ▸ hm q.first.val
  have ht' : σ x ∈ q'.second.val ↔ x ∈ q.second.val := ht ▸ hm q.second.val
  have ha' : σ x ∈ ({q'.axis} : Finset Axis) ↔ x ∈ ({q.axis} : Finset Axis) := by
    rw [← ha]
    simp
  rw [hm, third_of_even q h, third_of_even q' h']
  simp only [Finset.mem_symmDiff, hs', ht', ha']

set_option maxHeartbeats 600000 in
theorem same_even_zero {k l : ℕ} (F : ↥(invariantForms k l)) (q q' : Quad k l)
    (h : parity q = ∅) (h' : parity q' = ∅) (hc : code q = code q')
    (hz : coefficient F.val q' = 0) : coefficient F.val q = 0 := by
  obtain ⟨σ, ha, hs, ht, hu⟩ := perm_even q q' h h' hc
  obtain ⟨a, _, hA⟩ := orientedPerm_exterior σ 0 q.first
  obtain ⟨b, _, hB⟩ := orientedPerm_exterior σ 0 q.second
  obtain ⟨c, _, hC⟩ := orientedPerm_exterior σ 0 q.third
  have he := F.prop (orientedPermAt σ 0) (orthBasis q.axis) (basis 2 q.first)
    (basis k q.second) (basis l q.third)
  rw [orientedPermAt_basis, ha, hA, hB, hC, hs, ht, hu] at he
  simp only [map_smul, LinearMap.smul_apply] at he
  change c • b • a • orientationCorrection σ 0 q.axis • coefficient F.val q' = coefficient F.val q at he
  rw [hz, smul_zero, smul_zero, smul_zero, smul_zero] at he
  exact he.symm

theorem insert_eq_diff (s : Finset Axis) (a : Axis) (h : a ∉ s) :
    insert a s = s ∆ {a} := by
  ext i
  by_cases hi : i = a <;> simp [Finset.mem_symmDiff, hi, h]

private theorem insert_erase_val {n : ℕ} (s : Index (n + 1)) (a : Axis) (h : a ∈ s.val) :
    s.val = (eraseIndex s a h).val ∆ {a} := by
  rw [← insert_eq_diff _ _ (notMem_eraseIndex s a h)]
  exact (Finset.insert_erase h).symm

private theorem collision_residual_even {k l : ℕ} (q : Quad (k + 1) (l + 1))
    (hp : parity q = ∅) (hs : q.axis ∈ q.first.val) (ht : q.axis ∈ q.second.val)
    (hu : q.axis ∈ q.third.val) :
    ((eraseIndex q.first q.axis hs).val ∆ (eraseIndex q.second q.axis ht).val) ∆
      (eraseIndex q.third q.axis hu).val = ∅ := by
  let a : Finset Axis := {q.axis}
  let S := (eraseIndex q.first q.axis hs).val
  let T := (eraseIndex q.second q.axis ht).val
  let U := (eraseIndex q.third q.axis hu).val
  have hS : q.first.val = S ∆ a := insert_erase_val q.first q.axis hs
  have hT : q.second.val = T ∆ a := insert_erase_val q.second q.axis ht
  have hU : q.third.val = U ∆ a := insert_erase_val q.third q.axis hu
  change ((q.first.val ∆ q.second.val) ∆ a) ∆ q.third.val = ∅ at hp
  rw [hS, hT, hU] at hp
  have he : (((S ∆ a) ∆ (T ∆ a)) ∆ a) ∆ (U ∆ a) = ((S ∆ T) ∆ U) ∆ ((a ∆ a) ∆ (a ∆ a)) := by ac_rfl
  rw [he] at hp
  simpa using hp

private theorem exists_unused {k l : ℕ} (hk : k ≤ 7) (q : Quad k l) (hp : parity q = ∅) :
    ∃ b : Axis, b ≠ q.axis ∧ b ∉ q.first.val ∧ b ∉ q.second.val ∧ b ∉ q.third.val := by
  let s := insert q.axis (q.first.val ∪ q.second.val)
  have hA := Finset.card_insert_le q.axis (q.first.val ∪ q.second.val)
  have hB := Finset.card_union_le q.first.val q.second.val
  rw [q.first.prop, q.second.prop] at hB
  have hcard : s.card < (Finset.univ : Finset Axis).card := by
    rw [Finset.card_univ, Fintype.card_fin]
    dsimp [s]
    omega
  obtain ⟨b, _, hb⟩ := Finset.exists_mem_notMem_of_card_lt_card hcard
  have hx : b ≠ q.axis ∧ b ∉ q.first.val ∧ b ∉ q.second.val := by
    simpa [s, not_or] using hb
  refine ⟨b, hx.1, hx.2.1, hx.2.2, ?_⟩
  rw [third_of_even q hp]
  simp [Finset.mem_symmDiff, hx.1, hx.2.1, hx.2.2]

private abbrev e := orthBasis

private theorem rotation_wedge_fixed_tail {n : ℕ} (i j : Axis) (h : i ≠ j) (R : Index n)
    (hi : i ∉ R.val) (hj : j ∉ R.val) :
    exteriorRepresentation (n + 1) (D7Hook.rotation i j h)
      (wedgeLeftLinear n (e i) (basis n R)) =
        (-7 / 25 : ℂ) • wedgeLeftLinear n (e i) (basis n R) +
          (24 / 25 : ℂ) • wedgeLeftLinear n (e j) (basis n R) := by
  let g := D7Hook.rotation i j h
  have hR := map_basis_fixed g R (fun x hx => D7Hook.rotation_off_plane i j x h
    (fun he => hi (he ▸ hx)) (fun he => hj (he ▸ hx)))
  change exteriorPower.map (n + 1) g.val (wedgeLeftLinear n (e i) (basis n R)) = _
  rw [wedgeLeft_naturality n g, hR]
  have he := (D7Hook.rotation_on_plane i j h).1
  change g.val (e i) = _ at he
  rw [he, map_add, LinearMap.add_apply, map_smul, map_smul,
    LinearMap.smul_apply, LinearMap.smul_apply]

private theorem quarter_wedge_fixed_tail {n : ℕ} (i j : Axis) (h : i ≠ j) (R : Index n)
    (hi : i ∉ R.val) (hj : j ∉ R.val) :
    exteriorRepresentation (n + 1) (quarterTurn i j)
      (wedgeLeftLinear n (e i) (basis n R)) = -wedgeLeftLinear n (e j) (basis n R) := by
  let g := quarterTurn i j
  change exteriorPower.map (n + 1) g.val (wedgeLeftLinear n (e i) (basis n R)) = _
  rw [wedgeLeft_naturality n g, quarterTurn_exterior i j h R (iff_of_false hi hj),
    (quarterTurn_basis i j h).1, map_neg, LinearMap.neg_apply]

private theorem scaled_zero {a b c x : ℂ} (ha : a ≠ 0) (hb : b ≠ 0) (hc : c ≠ 0)
    (h : c • b • a • x = 0) : x = 0 := by
  exact (smul_eq_zero.mp ((smul_eq_zero.mp ((smul_eq_zero.mp h).resolve_left hc)).resolve_left hb)).resolve_left ha

set_option maxHeartbeats 800000 in
private theorem collision_wedge_zero {k l : ℕ} (F : ↥(invariantForms (k + 1) (l + 1)))
    (hz : ∀ q : Quad (k + 1) (l + 1), parity q = ∅ → regular q → coefficient F.val q = 0)
    (i j : Axis) (hij : i ≠ j) (R : Index 1) (S : Index k) (T : Index l)
    (hiR : i ∉ R.val) (hiS : i ∉ S.val) (hiT : i ∉ T.val)
    (hjR : j ∉ R.val) (hjS : j ∉ S.val) (hjT : j ∉ T.val)
    (hp : (R.val ∆ S.val) ∆ T.val = ∅) :
    F.val (e i) (wedgeLeftLinear 1 (e i) (basis 1 R))
      (wedgeLeftLinear k (e i) (basis k S)) (wedgeLeftLinear l (e i) (basis l T)) = 0 := by
  let a (b : Bool) : Axis := if b then j else i
  have ha : Function.Injective a := by
    intro b c h
    cases b <;> cases c <;> simp_all [a]
  have haR (b : Bool) : a b ∉ R.val := by
    cases b
    · exact hiR
    · exact hjR
  have haS (b : Bool) : a b ∉ S.val := by
    cases b
    · exact hiS
    · exact hjS
  have haT (b : Bool) : a b ∉ T.val := by
    cases b
    · exact hiT
    · exact hjT
  let X (b : Bool) := e (a b)
  let Y (b : Bool) := wedgeLeftLinear 1 (X b) (basis 1 R)
  let Z (b : Bool) := wedgeLeftLinear k (X b) (basis k S)
  let W (b : Bool) := wedgeLeftLinear l (X b) (basis l T)
  have hsmall : ({i, j} : Finset Axis).card < (Finset.univ : Finset Axis).card := by
    rw [Finset.card_pair hij, Finset.card_univ, Fintype.card_fin]
    decide
  obtain ⟨p, _, hpj⟩ := Finset.exists_mem_notMem_of_card_lt_card hsmall
  have hpmark (b : Bool) : p ≠ a b := by
    cases b
    · exact fun h => hpj (Finset.mem_insert.mpr (Or.inl h))
    · exact fun h => hpj (Finset.mem_insert.mpr (Or.inr (Finset.mem_singleton.mpr h)))
  have hMix (b c d f : Bool) (hh : b ≠ c ∨ b ≠ d ∨ b ≠ f) :
      F.val (X b) (Y c) (Z d) (W f) = 0 := by
    let q : Quad (k + 1) (l + 1) :=
      ⟨a b, insertIndex R (a c) (haR c), insertIndex S (a d) (haS d), insertIndex T (a f) (haT f)⟩
    have hpar : parity q = ((({a c} : Finset Axis) ∆ {a d}) ∆ {a b}) ∆ {a f} := by
      change ((insert (a c) R.val ∆ insert (a d) S.val) ∆ {a b}) ∆ insert (a f) T.val = _
      rw [insert_eq_diff _ _ (haR c), insert_eq_diff _ _ (haS d), insert_eq_diff _ _ (haT f)]
      have h : (((R.val ∆ {a c}) ∆ (S.val ∆ {a d})) ∆ {a b}) ∆ (T.val ∆ {a f}) =
          ((R.val ∆ S.val) ∆ T.val) ∆ ((({a c} ∆ {a d}) ∆ {a b}) ∆ {a f}) := by ac_rfl
      rw [h, hp]
      exact bot_symmDiff _
    have hnot : parity q ≠ Finset.univ := by
      intro he
      have he' : p ∈ parity q := he.symm ▸ Finset.mem_univ p
      rw [hpar] at he'
      simp [Finset.mem_symmDiff, hpmark] at he'
    have hzq : coefficient F.val q = 0 := by
      by_contra hn
      have he := (support_parity F q hn).resolve_right hnot
      have hrel : regular q := by
        by_contra h
        have h₁ : q.axis ∈ q.first.val := by by_contra hn; exact h (Or.inl hn)
        have h₂ : q.axis ∈ q.second.val := by by_contra hn; exact h (Or.inr hn)
        have hT' := (axis_mem_third_even q he).mpr (iff_of_true h₁ h₂)
        have hc : b = c := ha ((Finset.mem_insert.mp h₁).resolve_right (haR b))
        have hd : b = d := ha ((Finset.mem_insert.mp h₂).resolve_right (haS b))
        have hf : b = f := ha ((Finset.mem_insert.mp hT').resolve_right (haT b))
        exact hh.elim (fun H => H hc) (fun H => H.elim (fun H' => H' hd) (fun H' => H' hf))
      exact hn (hz q he hrel)
    obtain ⟨u, hu, hu'⟩ := enlarged_wedge R (a c) (haR c)
    obtain ⟨v, hv, hv'⟩ := enlarged_wedge S (a d) (haS d)
    obtain ⟨w, hw, hw'⟩ := enlarged_wedge T (a f) (haT f)
    change F.val (X b) (basis 2 (insertIndex R (a c) (haR c)))
      (basis (k + 1) (insertIndex S (a d) (haS d))) (basis (l + 1) (insertIndex T (a f) (haT f))) = 0 at hzq
    rw [hu', hv', hw'] at hzq
    simp only [map_smul, LinearMap.smul_apply] at hzq
    exact scaled_zero hu hv hw hzq
  have hQ := F.prop (quarterTurn i j) (X false) (Y false) (Z false) (W false)
  have hQx : (quarterTurn i j).val (X false) = -X true := (quarterTurn_basis i j hij).1
  have hQy : exteriorRepresentation 2 (quarterTurn i j) (Y false) = -Y true :=
    quarter_wedge_fixed_tail i j hij R hiR hjR
  have hQz : exteriorRepresentation (k + 1) (quarterTurn i j) (Z false) = -Z true :=
    quarter_wedge_fixed_tail i j hij S hiS hjS
  have hQw : exteriorRepresentation (l + 1) (quarterTurn i j) (W false) = -W true :=
    quarter_wedge_fixed_tail i j hij T hiT hjT
  rw [hQx, hQy, hQz, hQw] at hQ
  simp only [map_neg, LinearMap.neg_apply, neg_neg] at hQ
  let g := D7Hook.rotation i j hij
  let u : ℂ := -7 / 25
  let v : ℂ := 24 / 25
  have hx : g.val (X false) = u • X false + v • X true := (D7Hook.rotation_on_plane i j hij).1
  have hy : exteriorRepresentation 2 g (Y false) = u • Y false + v • Y true :=
    rotation_wedge_fixed_tail i j hij R hiR hjR
  have hZ : exteriorRepresentation (k + 1) g (Z false) = u • Z false + v • Z true :=
    rotation_wedge_fixed_tail i j hij S hiS hjS
  have hW : exteriorRepresentation (l + 1) g (W false) = u • W false + v • W true :=
    rotation_wedge_fixed_tail i j hij T hiT hjT
  have h := F.prop g (X false) (Y false) (Z false) (W false)
  rw [hx, hy, hZ, hW] at h
  simp (disch := decide) only [map_add, map_smul, LinearMap.add_apply, LinearMap.smul_apply, hMix,
    smul_eq_mul, hQ] at h
  change F.val (X false) (Y false) (Z false) (W false) = 0
  dsimp only [u, v] at h
  linear_combination -(390625 / 56448 : ℂ) * h

theorem even_coefficients_zero {k l : ℕ} (hk : k ≤ 7) (F : ↥(invariantForms k l))
    (hz : ∀ q : Quad k l, parity q = ∅ → regular q → coefficient F.val q = 0)
    (q : Quad k l) (hp : parity q = ∅) : coefficient F.val q = 0 := by
  by_cases hreg : regular q
  · exact hz q hp hreg
  have hs : q.axis ∈ q.first.val := by by_contra h; exact hreg (Or.inl h)
  have ht : q.axis ∈ q.second.val := by by_contra h; exact hreg (Or.inr h)
  have hu := (axis_mem_third_even q hp).mpr (iff_of_true hs ht)
  obtain ⟨j, hj, hjR, hjS, hjT⟩ := exists_unused hk q hp
  cases k with
  | zero =>
    have he : q.second.val = ∅ := Finset.card_eq_zero.mp q.second.prop
    rw [he] at ht
    exact (Finset.notMem_empty _ ht).elim
  | succ k =>
    cases l with
    | zero =>
      have he : q.third.val = ∅ := Finset.card_eq_zero.mp q.third.prop
      rw [he] at hu
      exact (Finset.notMem_empty _ hu).elim
    | succ l =>
      let R := eraseIndex q.first q.axis hs
      let S := eraseIndex q.second q.axis ht
      let T := eraseIndex q.third q.axis hu
      have h := collision_wedge_zero F hz q.axis j hj.symm R S T
        (notMem_eraseIndex _ _ _) (notMem_eraseIndex _ _ _) (notMem_eraseIndex _ _ _)
        (fun h => hjR (Finset.mem_erase.mp h).2) (fun h => hjS (Finset.mem_erase.mp h).2)
        (fun h => hjT (Finset.mem_erase.mp h).2) (collision_residual_even q hp hs ht hu)
      obtain ⟨a, _, ha⟩ := basis_eq_wedge_erase q.first q.axis hs
      obtain ⟨b, _, hb⟩ := basis_eq_wedge_erase q.second q.axis ht
      obtain ⟨c, _, hc⟩ := basis_eq_wedge_erase q.third q.axis hu
      change F.val (e q.axis) (basis 2 q.first) (basis (k + 1) q.second) (basis (l + 1) q.third) = 0
      rw [ha, hb, hc]
      simp only [map_smul, LinearMap.smul_apply]
      change c • b • a • F.val (e q.axis) (wedgeLeftLinear 1 (e q.axis) (basis 1 R))
        (wedgeLeftLinear k (e q.axis) (basis k S)) (wedgeLeftLinear l (e q.axis) (basis l T)) = 0
      rw [h, smul_zero, smul_zero, smul_zero]

def possible (k l : ℕ) : Bool × Bool → Prop
  | (true, false) => feasible 1 k l
  | (false, true) => 0 < k ∧ feasible 2 (k - 1) l
  | (false, false) => 0 < l ∧ feasible 2 k (l - 1)
  | (true, true) => False

instance (k l : ℕ) (c : Bool × Bool) : Decidable (possible k l c) := by
  rcases c with ⟨a, b⟩
  cases a <;> cases b <;> simp only [possible] <;> infer_instance

abbrev OrbitCode := Bool × (Bool × Bool)

def allowed (k l : ℕ) (c : OrbitCode) : Prop :=
  possible k (if c.1 then 14 - l else l) c.2

instance (k l : ℕ) (c : OrbitCode) : Decidable (allowed k l c) :=
  inferInstanceAs (Decidable (possible k (if c.1 then 14 - l else l) c.2))

def quadMultiplicity (k l : ℕ) : ℕ := Fintype.card {c : OrbitCode // allowed k l c}

private theorem cancel_insert₁ (s t u a : Finset Axis) :
    (((s ∆ a) ∆ t) ∆ a) ∆ u = (s ∆ t) ∆ u := by
  rw [symmDiff_right_comm s a t, symmDiff_symmDiff_cancel_right]

private theorem cancel_insert₃ (s t u a : Finset Axis) :
    ((s ∆ t) ∆ a) ∆ (u ∆ a) = (s ∆ t) ∆ u := by
  rw [← symmDiff_assoc, symmDiff_right_comm (s ∆ t) a u, symmDiff_symmDiff_cancel_right]

theorem possible_of_even {k l : ℕ} (q : Quad k l) (hp : parity q = ∅) (hr : regular q) :
    possible k l (code q) := by
  by_cases hS : q.axis ∈ q.first.val
  · have hT : q.axis ∉ q.second.val := hr.resolve_left (not_not_intro hS)
    have he := insert_erase_val q.first q.axis hS
    rw [parity, he, cancel_insert₁] at hp
    simp only [code, hS, hT, decide_true, decide_false, possible]
    exact empty_parity_feasible (eraseIndex q.first q.axis hS, q.second, q.third) hp
  by_cases hT : q.axis ∈ q.second.val
  · cases k with
    | zero =>
      have ht : q.second.val = ∅ := Finset.card_eq_zero.mp q.second.prop
      rw [ht] at hT
      exact (Finset.notMem_empty _ hT).elim
    | succ k =>
      have he := insert_erase_val q.second q.axis hT
      rw [parity, he, ← symmDiff_assoc q.first.val, symmDiff_symmDiff_cancel_right] at hp
      simp only [code, hS, hT, decide_true, decide_false, possible, Nat.add_sub_cancel]
      exact ⟨by omega, empty_parity_feasible (q.first, eraseIndex q.second q.axis hT, q.third) hp⟩
  have hU := (axis_mem_third_even q hp).mpr (iff_of_false hS hT)
  cases l with
  | zero =>
    have ht : q.third.val = ∅ := Finset.card_eq_zero.mp q.third.prop
    rw [ht] at hU
    exact (Finset.notMem_empty _ hU).elim
  | succ l =>
    have he := insert_erase_val q.third q.axis hU
    rw [parity, he, cancel_insert₃] at hp
    simp only [code, hS, hT, decide_false, possible, Nat.add_sub_cancel]
    exact ⟨by omega, empty_parity_feasible (q.first, q.second, eraseIndex q.third q.axis hU) hp⟩

def complementThird {k l m : ℕ} (h : l + m = 14) (q : Quad k l) : Quad k m :=
  ⟨q.axis, q.first, q.second, ⟨q.third.valᶜ, by
    change q.third.valᶜ.card = m
    rw [Finset.card_compl, Fintype.card_fin, q.third.prop]
    omega⟩⟩

theorem complementThird_parity {k l m : ℕ} (h : l + m = 14) (q : Quad k l) :
    parity (complementThird h q) = (parity q)ᶜ := by
  ext i
  change i ∈ (((q.first.val ∆ q.second.val) ∆ {q.axis}) ∆ q.third.valᶜ) ↔
    i ∈ ((((q.first.val ∆ q.second.val) ∆ {q.axis}) ∆ q.third.val)ᶜ)
  simp only [Finset.mem_symmDiff, Finset.mem_compl]
  tauto

theorem allowed_of_regular {k l : ℕ} (hl : l ≤ 14) (q : Quad k l) (hr : regular q) (b : Bool)
    (hp : parity q = if b then Finset.univ else ∅) : allowed k l (b, code q) := by
  cases b
  · exact possible_of_even q hp hr
  · have h : l + (14 - l) = 14 := by omega
    have hp' : parity (complementThird h q) = ∅ := by
      rw [complementThird_parity, hp]
      simp
    exact possible_of_even (complementThird h q) hp' hr

def twistThird {k l m : ℕ} (h : l + m = 14) (F : Form k m) : Form k l where
  toFun x :=
    { toFun y := ((LinearMap.lcomp ℂ ℂ (starEquiv h).toLinearMap).comp (F x y))
      map_add' y z := by simp only [map_add, LinearMap.comp_add]
      map_smul' c y := by simp only [map_smul, LinearMap.comp_smul, RingHom.id_apply] }
  map_add' x y := by
    apply LinearMap.ext
    intro z
    apply LinearMap.ext
    intro w
    apply LinearMap.ext
    intro u
    change F (x + y) z w (starEquiv h u) = F x z w (starEquiv h u) + F y z w (starEquiv h u)
    simp only [map_add, LinearMap.add_apply]
  map_smul' c x := by
    apply LinearMap.ext
    intro z
    apply LinearMap.ext
    intro w
    apply LinearMap.ext
    intro u
    change F (c • x) z w (starEquiv h u) = c • F x z w (starEquiv h u)
    simp only [map_smul, LinearMap.smul_apply]

theorem twistThird_apply {k l m : ℕ} (h : l + m = 14) (F : Form k m) (x : Space)
    (y : Ext 2) (z : Ext k) (w : Ext l) :
    twistThird h F x y z w = F x y z (starEquiv h w) := rfl

theorem twistThird_mem {k l m : ℕ} (h : l + m = 14) (F : ↥(invariantForms k m)) :
    twistThird h F.val ∈ invariantForms k l := by
  intro g x y z w
  rw [twistThird_apply, twistThird_apply, starEquiv_equivariant]
  exact F.prop g x y z (starEquiv h w)

theorem eval_twistThird {k l m : ℕ} (h : l + m = 14) (F : Form k m) (q : Quad k l) :
    ∃ a : ℂ, a ≠ 0 ∧ coefficient (twistThird h F) q = a • coefficient F (complementThird h q) := by
  obtain ⟨s, hs, a, ha, he⟩ := starEquiv_complement h q.third
  have hS : s = (complementThird h q).third := Subtype.ext hs
  refine ⟨a, ha, ?_⟩
  change twistThird h F (e q.axis) (basis 2 q.first) (basis k q.second) (basis l q.third) = _
  rw [twistThird_apply, he, hS, map_smul]
  rfl

theorem complementary_twice {k l m : ℕ} (h : l + m = 14) (h' : m + l = 14) (q : Quad k l) :
    complementThird h' (complementThird h q) = q := by
  cases q with
  | mk a s t u =>
    have he : (complementThird h' (complementThird h ⟨a, s, t, u⟩)).third = u :=
      Subtype.ext (compl_compl u.val)
    exact congrArg (Quad.mk a s t) he

private abbrev RegularOrbit (k l : ℕ) :=
  {c : OrbitCode // ∃ q : Quad k l, regular q ∧ code q = c.2 ∧
    parity q = if c.1 then Finset.univ else ∅}

private def sample {k l : ℕ} (c : RegularOrbit k l) : Quad k l := Classical.choose c.prop

private theorem sample_spec {k l : ℕ} (c : RegularOrbit k l) :
    regular (sample c) ∧ code (sample c) = c.val.2 ∧
      parity (sample c) = if c.val.1 then Finset.univ else ∅ := Classical.choose_spec c.prop

private def orbitEvaluation (k l : ℕ) : invariantForms k l →ₗ[ℂ] (RegularOrbit k l → ℂ) where
  toFun F c := coefficient F.val (sample c)
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

@[instance_reducible] def invariantFormsAddCommGroup (k l : ℕ) : AddCommGroup ↥(invariantForms k l) := by
  letI : AddCommGroup (D7TripleInvariants.Form 2 k l) := inferInstance
  letI : AddCommGroup (Form k l) := LinearMap.addCommGroup
  exact Submodule.addCommGroup (R := ℂ) (M := Form k l) (invariantForms k l)

local instance (k l : ℕ) : AddCommGroup ↥(invariantForms k l) := invariantFormsAddCommGroup k l

set_option maxHeartbeats 800000 in
private theorem orbitEvaluation_injective {k l : ℕ} (hk : k ≤ 7) (hl : l ≤ 14) :
    Function.Injective (orbitEvaluation k l) := by
  intro U V hUV
  apply sub_eq_zero.mp
  let F := U - V
  have hF : orbitEvaluation k l F = 0 := by rw [map_sub, hUV, sub_self]
  change F = 0
  have hsample (c : RegularOrbit k l) : coefficient F.val (sample c) = 0 := congrFun hF c
  have he (q : Quad k l) (h : parity q = ∅) : coefficient F.val q = 0 := by
    apply even_coefficients_zero hk F _ q h
    intro Q hQ hr
    let c : RegularOrbit k l := ⟨(false, code Q), Q, hr, rfl, hQ⟩
    obtain ⟨_, hc, hp⟩ := sample_spec c
    exact same_even_zero F Q (sample c) hQ hp hc.symm (hsample c)
  have hf : l + (14 - l) = 14 := by omega
  have hh : (14 - l) + l = 14 := by omega
  let G : ↥(invariantForms k (14 - l)) := ⟨twistThird hh F.val, twistThird_mem hh F⟩
  have ho (q : Quad k l) (h : parity q = Finset.univ) : coefficient F.val q = 0 := by
    let Q := complementThird hf q
    have hp : parity Q = ∅ := by rw [complementThird_parity, h]; simp
    have hG : coefficient G.val Q = 0 := by
      apply even_coefficients_zero hk G _ Q hp
      intro T hT hr
      let T' := complementThird hh T
      have ht : parity T' = Finset.univ := by rw [complementThird_parity, hT]; simp
      let c : RegularOrbit k l := ⟨(true, code T'), T', hr, rfl, ht⟩
      obtain ⟨_, hc, ht'⟩ := sample_spec c
      let S := complementThird hf (sample c)
      have hS : parity S = ∅ := by rw [complementThird_parity, ht']; simp
      have hGS : coefficient G.val S = 0 := by
        obtain ⟨a, _, ha⟩ := eval_twistThird hh F.val S
        change coefficient G.val S = _ at ha
        change _ = a • coefficient F.val (complementThird hh (complementThird hf (sample c))) at ha
        rw [complementary_twice, hsample c, smul_zero] at ha
        exact ha
      exact same_even_zero G T S hT hS hc.symm hGS
    obtain ⟨a, ha, ha'⟩ := eval_twistThird hh F.val Q
    change coefficient G.val Q = a • coefficient F.val (complementThird hh (complementThird hf q)) at ha'
    rw [complementary_twice, hG] at ha'
    exact (smul_eq_zero.mp ha'.symm).resolve_left ha
  apply Subtype.ext
  apply coefficient_ext
  intro q
  change coefficient F.val q = 0
  by_contra h
  rcases support_parity F q h with h₁ | h₂
  · exact h (he q h₁)
  · exact h (ho q h₂)

theorem invariantForms_finite {k l : ℕ} (hk : k ≤ 7) (hl : l ≤ 14) :
    Module.Finite ℂ ↥(invariantForms k l) := by
  classical
  exact Module.Finite.of_injective (orbitEvaluation k l) (orbitEvaluation_injective hk hl)

/-- There is at most one independent coefficient for each feasible parity
and partner of the vector slot. -/
theorem finrank_invariantForms_le {k l : ℕ} (hk : k ≤ 7) (hl : l ≤ 14) :
    Module.finrank ℂ (invariantForms k l) ≤ quadMultiplicity k l := by
  classical
  let j (c : RegularOrbit k l) : {b : OrbitCode // allowed k l b} := ⟨c.val, by
    have h := allowed_of_regular hl (sample c) (sample_spec c).1 c.val.1 (sample_spec c).2.2
    rw [(sample_spec c).2.1] at h
    exact h⟩
  have hj : Function.Injective j := fun a b h => Subtype.ext (congrArg (fun t : {b : OrbitCode // allowed k l b} => t.val) h)
  have hh := LinearMap.finrank_le_finrank_of_injective (orbitEvaluation_injective hk hl)
  rw [Module.finrank_pi] at hh
  exact hh.trans (Fintype.card_le_of_injective j hj)

end
end GeometricUnity.D7QuadInvariants
~~~

[Return to file index](#file-index)

## D7QuadMultiplicity.lean {#source-d7quadmultiplicity-lean}

Realizes the invariant four-factor forms needed for the unrestricted contraction count.

~~~lean
import D7QuadInvariants

/-!
# Realization of the unrestricted intertwiners

A contraction selects one of the three partners of the vector slot. The
remaining three wedges are evaluated by an even invariant trilinear form.
Complementing the last grade by Hodge duality realizes the other parity.
-/

namespace GeometricUnity.D7QuadMultiplicity

open D7Exterior D7Hodge D7Irreducible D7VectorTensor D7VectorGrades D7TensorColumns
open D7ComplementaryGrades D7TripleMultiplicity D7QuadInvariants
open scoped BigOperators symmDiff TensorProduct

noncomputable section

private abbrev e := orthBasis
private abbrev Triform := D7TripleInvariants.Form

private def OrthInvariant {k l : ℕ} (F : Form k l) : Prop :=
  ∀ (f : Space →ₗ[ℂ] Space), Orthogonal f → ∀ x y z w,
    F (f x) (exteriorPower.map 2 f y) (exteriorPower.map k f z) (exteriorPower.map l f w) = F x y z w

private theorem invariant_of_orth {k l : ℕ} {F : Form k l} (h : OrthInvariant F) :
    F ∈ invariantForms k l := fun g x y z w => h g.val g.prop.2 x y z w

set_option maxHeartbeats 600000 in
private theorem full_parity_zero {k l : ℕ} {F : Form k l} (h : OrthInvariant F)
    (q : Quad k l) (hp : parity q = Finset.univ) : coefficient F q = 0 := by
  have hx := h vectorReflection vectorReflection_isometry (e q.axis) (basis 2 q.first)
    (basis k q.second) (basis l q.third)
  have hvec : vectorReflection (e q.axis) = subsetFlip {q.axis} 0 • e q.axis := by
    simp only [vectorReflection, orthDiagonal_basis, subsetFlip, Finset.mem_singleton, eq_comm]
  rw [hvec, reflect_basis, reflect_basis, reflect_basis] at hx
  simp only [map_smul, LinearMap.smul_apply, smul_eq_mul] at hx
  change subsetFlip q.third.val 0 * (subsetFlip q.second.val 0 * (subsetFlip q.first.val 0 *
    (subsetFlip {q.axis} 0 * coefficient F q))) = coefficient F q at hx
  have hs : subsetFlip (parity q) 0 = -1 := by rw [hp]; simp [subsetFlip]
  rw [parity, D7TripleInvariants.subsetFlip_diff, D7TripleInvariants.subsetFlip_diff,
    D7TripleInvariants.subsetFlip_diff] at hs
  have hz : -coefficient F q = coefficient F q := by
    calc
      _ = (subsetFlip q.first.val 0 * subsetFlip q.second.val 0 * subsetFlip {q.axis} 0 *
          subsetFlip q.third.val 0) * coefficient F q := by rw [hs, neg_one_mul]
      _ = _ := by
        convert hx using 1
        ac_rfl
  have hz' : (2 : ℂ) * coefficient F q = 0 := by linear_combination -hz
  exact (mul_eq_zero.mp hz').resolve_left (by norm_num)

private def contractFirst {k l : ℕ} (F : Triform 1 k l) : Form k l :=
  (contractLeft 1).compr₂ₛₗ F

private def contractSecond {k l : ℕ} (F : Triform 2 k l) : Form (k + 1) l where
  toFun x := (LinearMap.lcomp ℂ (Ext l →ₗ[ℂ] ℂ) (contractLeft k x)).comp F
  map_add' _ _ := by
    apply LinearMap.ext
    intro y
    apply LinearMap.ext
    intro z
    simp only [LinearMap.comp_apply, LinearMap.lcomp_apply, map_add, LinearMap.add_apply]
  map_smul' _ _ := by
    apply LinearMap.ext
    intro y
    apply LinearMap.ext
    intro z
    simp only [LinearMap.comp_apply, LinearMap.lcomp_apply, map_smul, LinearMap.smul_apply, RingHom.id_apply]

private def contractThird {k l : ℕ} (F : Triform 2 k l) : Form k (l + 1) where
  toFun x :=
    { toFun y := (LinearMap.lcomp ℂ ℂ (contractLeft l x)).comp (F y)
      map_add' _ _ := by simp only [map_add, LinearMap.comp_add]
      map_smul' _ _ := by simp only [map_smul, LinearMap.comp_smul, RingHom.id_apply] }
  map_add' x x' := by
    apply LinearMap.ext
    intro y
    apply LinearMap.ext
    intro z
    apply LinearMap.ext
    intro w
    change F y z (contractLeft l (x + x') w) = F y z (contractLeft l x w) + F y z (contractLeft l x' w)
    simp only [map_add, LinearMap.add_apply]
  map_smul' c x := by
    apply LinearMap.ext
    intro y
    apply LinearMap.ext
    intro z
    apply LinearMap.ext
    intro w
    change F y z (contractLeft l (c • x) w) = c • F y z (contractLeft l x w)
    simp only [map_smul, LinearMap.smul_apply]

private theorem contractFirst_invariant {k l : ℕ} {F : Triform 1 k l}
    (h : orthInvariant F) : OrthInvariant (contractFirst F) := by
  intro f hf x y z w
  change F (contractLeft 1 (f x) (exteriorPower.map 2 f y)) (exteriorPower.map k f z)
    (exteriorPower.map l f w) = F (contractLeft 1 x y) z w
  rw [contract_natural_left 1 f hf]
  exact h f hf _ _ _

private theorem contractSecond_invariant {k l : ℕ} {F : Triform 2 k l}
    (h : orthInvariant F) : OrthInvariant (contractSecond F) := by
  intro f hf x y z w
  change F (exteriorPower.map 2 f y) (contractLeft k (f x) (exteriorPower.map (k + 1) f z))
    (exteriorPower.map l f w) = F y (contractLeft k x z) w
  rw [contract_natural_left k f hf]
  exact h f hf _ _ _

private theorem contractThird_invariant {k l : ℕ} {F : Triform 2 k l}
    (h : orthInvariant F) : OrthInvariant (contractThird F) := by
  intro f hf x y z w
  change F (exteriorPower.map 2 f y) (exteriorPower.map k f z)
    (contractLeft l (f x) (exteriorPower.map (l + 1) f w)) = F y z (contractLeft l x w)
  rw [contract_natural_left l f hf]
  exact h f hf _ _ _

private theorem contract_insert {n : ℕ} (R : Index n) (a : Axis) (ha : a ∉ R.val) :
    ∃ z : ℂ, z ≠ 0 ∧ contractLeft n (e a) (basis (n + 1) (insertIndex R a ha)) = z • basis n R := by
  obtain ⟨z, hz, he⟩ := enlarged_wedge R a ha
  refine ⟨z, hz, ?_⟩
  rw [he, map_smul, contract_wedge_basis R a ha]

private theorem even_with_unused {r k l : ℕ} (hf : r + k < 14) {F : Triform r k l}
    (hF : orthInvariant F) (hF0 : F ≠ 0) :
    ∃ q : D7TripleInvariants.Triple r k l, D7TripleInvariants.parity q = ∅ ∧
      D7TripleInvariants.value F q ≠ 0 ∧ ∃ a : Axis, a ∉ q.1.val ∧ a ∉ q.2.1.val ∧ a ∉ q.2.2.val := by
  obtain ⟨q, hp, hz⟩ := even_nonzero_coordinate hF hF0
  have hc := Finset.card_union_le q.1.val q.2.1.val
  rw [q.1.prop, q.2.1.prop] at hc
  have hb : (q.1.val ∪ q.2.1.val).card < (Finset.univ : Finset Axis).card := by
    rw [Finset.card_univ, Fintype.card_fin]
    omega
  obtain ⟨a, _, ha⟩ := Finset.exists_mem_notMem_of_card_lt_card hb
  have ha₁ : a ∉ q.1.val := fun h => ha (Finset.mem_union_left _ h)
  have ha₂ : a ∉ q.2.1.val := fun h => ha (Finset.mem_union_right _ h)
  refine ⟨q, hp, hz, a, ha₁, ha₂, ?_⟩
  have hq : q.2.2.val = q.1.val ∆ q.2.1.val := D7TripleInvariants.third_of_parity q false hp
  exact fun hm => ha (Finset.symmDiff_subset_union (hq ▸ hm))

private structure EvenWitness (k l : ℕ) (c : Bool × Bool) where
  form : Form k l
  invariant : OrthInvariant form
  q : Quad k l
  even : parity q = ∅
  reg : regular q
  tag : code q = c
  nonzero : coefficient form q ≠ 0
  other : ∀ p : Quad k l, parity p = ∅ → regular p → code p ≠ c → coefficient form p = 0

private theorem firstWitness {k l : ℕ} (hk : k ≤ 7) (h : D7TripleInvariants.feasible 1 k l) :
    Nonempty (EvenWitness k l (true, false)) := by
  obtain ⟨F, hf, hF0⟩ := even_exists (Or.inl rfl) h
  obtain ⟨q, hp, hz, a, ha, hb, _⟩ := even_with_unused (by omega) hf hF0
  let p : Quad k l := ⟨a, insertIndex q.1 a ha, q.2.1, q.2.2⟩
  have hA : a ∈ p.first.val := Finset.mem_insert_self _ _
  have hP : parity p = ∅ := by
    change ((insert a q.1.val ∆ q.2.1.val) ∆ {a}) ∆ q.2.2.val = _
    rw [insert_eq_diff _ _ ha, symmDiff_right_comm q.1.val {a} q.2.1.val, symmDiff_symmDiff_cancel_right]
    exact hp
  refine ⟨⟨contractFirst F, contractFirst_invariant hf, p, hP, Or.inr hb, ?_, ?_, ?_⟩⟩
  · change (decide (a ∈ p.first.val), decide (a ∈ q.2.1.val)) = _
    simp [hA, hb]
  · obtain ⟨z, hz', he⟩ := contract_insert q.1 a ha
    change F (contractLeft 1 (e a) (basis 2 (insertIndex q.1 a ha))) (basis k q.2.1) (basis l q.2.2) ≠ 0
    rw [he, map_smul, LinearMap.smul_apply, LinearMap.smul_apply]
    exact smul_ne_zero hz' hz
  · intro q' _ hr ht
    have ha' : q'.axis ∉ q'.first.val := by
      intro h
      have ht' := hr.resolve_left (not_not_intro h)
      apply ht
      simp [code, h, ht']
    change F (contractLeft 1 (e q'.axis) (basis 2 q'.first)) (basis k q'.second) (basis l q'.third) = 0
    rw [contractLeft_basis_zero q'.first q'.axis ha', map_zero, LinearMap.zero_apply, LinearMap.zero_apply]

private theorem secondWitness {k l : ℕ} (hk : k + 1 ≤ 7) (h : D7TripleInvariants.feasible 2 k l) :
    Nonempty (EvenWitness (k + 1) l (false, true)) := by
  obtain ⟨F, hf, hF0⟩ := even_exists_two h
  obtain ⟨q, hp, hz, a, ha, hb, _⟩ := even_with_unused (by omega) hf hF0
  let p : Quad (k + 1) l := ⟨a, q.1, insertIndex q.2.1 a hb, q.2.2⟩
  have hB : a ∈ p.second.val := Finset.mem_insert_self _ _
  have hP : parity p = ∅ := by
    change ((q.1.val ∆ insert a q.2.1.val) ∆ {a}) ∆ q.2.2.val = _
    rw [insert_eq_diff _ _ hb, ← symmDiff_assoc q.1.val, symmDiff_symmDiff_cancel_right]
    exact hp
  refine ⟨⟨contractSecond F, contractSecond_invariant hf, p, hP, Or.inl ha, ?_, ?_, ?_⟩⟩
  · change (decide (a ∈ q.1.val), decide (a ∈ p.second.val)) = _
    simp [ha, hB]
  · obtain ⟨z, hz', he⟩ := contract_insert q.2.1 a hb
    change F (basis 2 q.1) (contractLeft k (e a) (basis (k + 1) (insertIndex q.2.1 a hb))) (basis l q.2.2) ≠ 0
    rw [he, map_smul, LinearMap.smul_apply]
    exact smul_ne_zero hz' hz
  · intro q' _ hr ht
    have ha' : q'.axis ∉ q'.second.val := by
      intro h
      have ht' := hr.resolve_right (not_not_intro h)
      apply ht
      simp [code, h, ht']
    change F (basis 2 q'.first) (contractLeft k (e q'.axis) (basis (k + 1) q'.second)) (basis l q'.third) = 0
    rw [contractLeft_basis_zero q'.second q'.axis ha', map_zero, LinearMap.zero_apply]

private theorem thirdWitness {k l : ℕ} (hk : k ≤ 7) (h : D7TripleInvariants.feasible 2 k l) :
    Nonempty (EvenWitness k (l + 1) (false, false)) := by
  obtain ⟨F, hf, hF0⟩ := even_exists_two h
  obtain ⟨q, hp, hz, a, ha, hb, hc⟩ := even_with_unused (by omega) hf hF0
  let p : Quad k (l + 1) := ⟨a, q.1, q.2.1, insertIndex q.2.2 a hc⟩
  have hP : parity p = ∅ := by
    change ((q.1.val ∆ q.2.1.val) ∆ {a}) ∆ insert a q.2.2.val = _
    rw [insert_eq_diff _ _ hc, ← symmDiff_assoc, symmDiff_right_comm (q.1.val ∆ q.2.1.val) {a} q.2.2.val,
      symmDiff_symmDiff_cancel_right]
    exact hp
  refine ⟨⟨contractThird F, contractThird_invariant hf, p, hP, Or.inl ha, ?_, ?_, ?_⟩⟩
  · change (decide (a ∈ q.1.val), decide (a ∈ q.2.1.val)) = _
    simp [ha, hb]
  · obtain ⟨z, hz', he⟩ := contract_insert q.2.2 a hc
    change F (basis 2 q.1) (basis k q.2.1) (contractLeft l (e a)
      (basis (l + 1) (insertIndex q.2.2 a hc))) ≠ 0
    rw [he, map_smul]
    exact smul_ne_zero hz' hz
  · intro q' hp' hr ht
    have ha' : q'.axis ∉ q'.third.val := by
      intro h
      have hi := (axis_mem_third_even q' hp').mp h
      have hA : q'.axis ∉ q'.first.val := hr.elim id (fun h' hx => h' (hi.mp hx))
      have hB : q'.axis ∉ q'.second.val := fun hx => hA (hi.mpr hx)
      apply ht
      simp [code, hA, hB]
    change F (basis 2 q'.first) (basis k q'.second)
      (contractLeft l (e q'.axis) (basis (l + 1) q'.third)) = 0
    rw [contractLeft_basis_zero q'.third q'.axis ha', map_zero]

private theorem realizeEven {k l : ℕ} (hk : k ≤ 7) (c : Bool × Bool) (h : possible k l c) :
    Nonempty (EvenWitness k l c) := by
  rcases c with ⟨a, b⟩
  cases a <;> cases b
  · have h' : 0 < l ∧ D7TripleInvariants.feasible 2 k (l - 1) := h
    cases l
    · omega
    · exact thirdWitness hk h'.2
  · have h' : 0 < k ∧ D7TripleInvariants.feasible 2 (k - 1) l := h
    cases k
    · omega
    · exact secondWitness hk h'.2
  · exact firstWitness hk h
  · exact h.elim

private def recognizes {k l : ℕ} (c : OrbitCode) (q : Quad k l) : Prop :=
  regular q ∧ code q = c.2 ∧ parity q = if c.1 then Finset.univ else ∅

private structure Witness (k l : ℕ) (c : OrbitCode) where
  form : ↥(invariantForms k l)
  q : Quad k l
  recognized : recognizes c q
  nonzero : coefficient form.val q ≠ 0
  other : ∀ p : Quad k l, ∀ d : OrbitCode, recognizes d p → d ≠ c → coefficient form.val p = 0

private theorem realize {k l : ℕ} (hk : k ≤ 7) (hl : l ≤ 14) (c : OrbitCode) (hc : allowed k l c) :
    Nonempty (Witness k l c) := by
  rcases c with ⟨b, c⟩
  cases b
  · obtain ⟨w⟩ := realizeEven hk c hc
    refine ⟨⟨⟨w.form, invariant_of_orth w.invariant⟩, w.q, ⟨w.reg, w.tag, w.even⟩, w.nonzero, ?_⟩⟩
    rintro p ⟨b, t⟩ ⟨hr, ht, hp⟩ he
    cases b
    · exact w.other p hp hr (fun h => he (Prod.ext rfl (ht.symm.trans h)))
    · exact full_parity_zero w.invariant p hp
  · have h : l + (14 - l) = 14 := by omega
    have h' : (14 - l) + l = 14 := by omega
    obtain ⟨w⟩ := realizeEven hk c hc
    let F := twistThird h w.form
    let q := complementThird h' w.q
    have hq : parity q = Finset.univ := by rw [complementThird_parity, w.even]; simp
    refine ⟨⟨⟨F, twistThird_mem h ⟨w.form, invariant_of_orth w.invariant⟩⟩, q,
      ⟨w.reg, w.tag, hq⟩, ?_, ?_⟩⟩
    · obtain ⟨a, ha, he⟩ := eval_twistThird h w.form q
      change coefficient F q = a • coefficient w.form (complementThird h (complementThird h' w.q)) at he
      rw [complementary_twice] at he
      rw [he]
      exact smul_ne_zero ha w.nonzero
    · rintro p ⟨b, t⟩ ⟨hr, ht, hp⟩ he
      obtain ⟨a, _, hA⟩ := eval_twistThird h w.form p
      change coefficient F p = a • coefficient w.form (complementThird h p) at hA
      change coefficient F p = 0
      rw [hA]
      cases b
      · have hp' : parity (complementThird h p) = Finset.univ := by rw [complementThird_parity, hp]; simp
        rw [full_parity_zero w.invariant _ hp', smul_zero]
      · have hp' : parity (complementThird h p) = ∅ := by rw [complementThird_parity, hp]; simp
        rw [w.other _ hp' hr (fun hh => he (Prod.ext rfl (ht.symm.trans hh))), smul_zero]

private def evaluation {k l : ℕ} (q : Quad k l) : invariantForms k l →ₗ[ℂ] ℂ where
  toFun F := coefficient F.val q
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

local instance (k l : ℕ) : AddCommGroup ↥(invariantForms k l) :=
  invariantFormsAddCommGroup k l

local instance (k l : ℕ) : Module ℂ ↥(invariantForms k l) :=
  Submodule.module (R := ℂ) (M := Form k l) (invariantForms k l)

set_option maxHeartbeats 600000 in
private theorem finrank_lower {k l : ℕ} (hk : k ≤ 7) (hl : l ≤ 14) :
    quadMultiplicity k l ≤ Module.finrank ℂ (invariantForms k l) := by
  classical
  let : Module.Finite ℂ ↥(invariantForms k l) := invariantForms_finite hk hl
  let I := {c : OrbitCode // allowed k l c}
  let w (i : I) : Witness k l i.val := Classical.choice (realize hk hl i.val i.prop)
  let v (i : I) : ↥(invariantForms k l) := (w i).form
  have hv : LinearIndependent ℂ v := by
    apply Fintype.linearIndependent_iff.mpr
    intro a ha i
    have h := congrArg (evaluation (w i).q) ha
    rw [map_sum, map_zero] at h
    simp only [map_smul, smul_eq_mul] at h
    rw [Finset.sum_eq_single i] at h
    · exact (mul_eq_zero.mp h).resolve_right (w i).nonzero
    · intro j _ hj
      have hz : evaluation (w i).q (v j) = 0 :=
        (w j).other (w i).q i.val (w i).recognized (fun he => hj (Subtype.ext he.symm))
      rw [hz, mul_zero]
    · simp
  exact hv.fintype_card_le_finrank

/-- In each grade pair there is exactly one independent invariant for
each feasible partner of the vector slot and each feasible parity. -/
theorem finrank_invariantForms {k l : ℕ} (hk : k ≤ 7) (hl : l ≤ 14) :
    Module.finrank ℂ (invariantForms k l) = quadMultiplicity k l :=
  le_antisymm (finrank_invariantForms_le hk hl) (finrank_lower hk hl)

end
end GeometricUnity.D7QuadMultiplicity
~~~

[Return to file index](#file-index)

## D7Unrestricted.lean {#source-d7unrestricted-lean}

Identifies unrestricted intertwiners with invariant forms and proves the total dimension 200.

~~~lean
import D7QuadMultiplicity
import Mathlib.LinearAlgebra.Contraction

/-!
# The unrestricted complex exterior-grade Hom count

The product metric lowers the two output indices. The resulting invariant
four-linear forms have the multiplicities proved in D7QuadMultiplicity.
-/

namespace GeometricUnity.D7Unrestricted

open D7Exterior D7Hodge D7Irreducible D7VectorTensor D7VectorGrades D7TensorColumns
open D7ComplementaryGrades D7QuadInvariants D7TripleMultiplicity
open D7TripleInvariants (metricEquiv metricEquiv_toLinearMap)
open scoped BigOperators TensorProduct

noncomputable section

abbrev Source (k : ℕ) := Ext 2 ⊗[ℂ] Ext k
private abbrev e := orthBasis

def sourceAction (k : ℕ) : Representation ℂ splitSpecialOrthogonal (Source k) :=
  (exteriorRepresentation 2).tprod (exteriorRepresentation k)

abbrev Intertwiners (k l : ℕ) := Representation.IntertwiningMap (sourceAction k) (action l)

private theorem spaceMetric (x y : Space) : orthBasis.toDualEquiv x y = splitForm x y := by
  have h : orthBasis.toDualEquiv.toLinearMap = splitMetric := by
    apply orthBasis.ext
    intro i
    apply orthBasis.ext
    intro j
    change orthBasis.toDual (orthBasis i) (orthBasis j) = splitMetric (orthBasis i) (orthBasis j)
    rw [Module.Basis.toDual_apply, splitMetric_apply, orthBasis_pair]
  have hx := DFunLike.congr_fun (DFunLike.congr_fun h x) y
  exact hx.trans (splitMetric_apply x y)

/-- The product of the vector metric and the exterior coefficient metric. -/
def tensorMetric (l : ℕ) : Product l ≃ₗ[ℂ] (Product l →ₗ[ℂ] ℂ) :=
  (TensorProduct.congr orthBasis.toDualEquiv (metricEquiv l)).trans
    (TensorProduct.dualDistribEquivOfBasis orthBasis (basis l))

private theorem tensorMetric_tmul (l : ℕ) (x y : Space) (u v : Ext l) :
    tensorMetric l (x ⊗ₜ[ℂ] u) (y ⊗ₜ[ℂ] v) = splitForm x y * exteriorMetric l u v := by
  unfold tensorMetric
  rw [LinearEquiv.trans_apply, TensorProduct.congr_tmul]
  change TensorProduct.dualDistrib ℂ Space (Ext l) (orthBasis.toDualEquiv x ⊗ₜ[ℂ] metricEquiv l u)
    (y ⊗ₜ[ℂ] v) = _
  rw [TensorProduct.dualDistrib_apply, spaceMetric]
  have h := DFunLike.congr_fun (DFunLike.congr_fun (metricEquiv_toLinearMap l) u) v
  exact congrArg (fun t : ℂ => splitForm x y * t) h

private theorem tensorMetric_invariant (l : ℕ) (g : splitSpecialOrthogonal) (x y : Product l) :
    tensorMetric l (action l g x) (action l g y) = tensorMetric l x y := by
  let f := (tensorMetric l).toLinearMap
  let g' := action l g
  have h : ((f.comp g').flip.comp g').flip = f := by
    apply TensorProduct.ext'
    intro a u
    apply TensorProduct.ext'
    intro b v
    change tensorMetric l (action l g (a ⊗ₜ[ℂ] u)) (action l g (b ⊗ₜ[ℂ] v)) =
      tensorMetric l (a ⊗ₜ[ℂ] u) (b ⊗ₜ[ℂ] v)
    rw [action_tmul, action_tmul, tensorMetric_tmul, tensorMetric_tmul, g.prop.2]
    change splitForm a b * exteriorMetric l (exteriorRepresentation l g u) (exteriorRepresentation l g v) =
      splitForm a b * exteriorMetric l u v
    rw [metric_invariant]
  exact DFunLike.congr_fun (DFunLike.congr_fun h x) y

private def asForm {k l : ℕ} (G : Source k →ₗ[ℂ] Product l →ₗ[ℂ] ℂ) : Form k l where
  toFun x := TensorProduct.curry (((TensorProduct.mk ℂ Space (Ext l) x).dualMap).comp G)
  map_add' x y := by
    apply LinearMap.ext
    intro u
    apply LinearMap.ext
    intro v
    apply LinearMap.ext
    intro z
    change G (u ⊗ₜ[ℂ] v) ((x + y) ⊗ₜ[ℂ] z) = G (u ⊗ₜ[ℂ] v) (x ⊗ₜ[ℂ] z) + G (u ⊗ₜ[ℂ] v) (y ⊗ₜ[ℂ] z)
    rw [TensorProduct.add_tmul, map_add]
  map_smul' c x := by
    apply LinearMap.ext
    intro u
    apply LinearMap.ext
    intro v
    apply LinearMap.ext
    intro z
    change G (u ⊗ₜ[ℂ] v) ((c • x) ⊗ₜ[ℂ] z) = c • G (u ⊗ₜ[ℂ] v) (x ⊗ₜ[ℂ] z)
    rw [← TensorProduct.smul_tmul', map_smul]

private def asBilinear {k l : ℕ} (F : Form k l) :
    Ext 2 →ₗ[ℂ] Ext k →ₗ[ℂ] Space →ₗ[ℂ] Ext l →ₗ[ℂ] ℂ where
  toFun u := (F.flip u).flip
  map_add' u v := by
    apply LinearMap.ext
    intro x
    apply LinearMap.ext
    intro y
    simp only [LinearMap.flip_apply, map_add, LinearMap.add_apply]
  map_smul' c u := by
    apply LinearMap.ext
    intro x
    apply LinearMap.ext
    intro y
    simp only [LinearMap.flip_apply, map_smul, LinearMap.smul_apply, RingHom.id_apply]

private def asRaw {k l : ℕ} (F : Form k l) : Source k →ₗ[ℂ] Product l →ₗ[ℂ] ℂ :=
  TensorProduct.lift ((asBilinear F).compr₂ₛₗ (TensorProduct.uncurry (RingHom.id ℂ) Space (Ext l) ℂ))

private theorem asRaw_tmul {k l : ℕ} (F : Form k l) (x : Space) (u : Ext 2) (v : Ext k) (w : Ext l) :
    asRaw F (u ⊗ₜ[ℂ] v) (x ⊗ₜ[ℂ] w) = F x u v w := rfl

private theorem source_tmul (k : ℕ) (g : splitSpecialOrthogonal) (u : Ext 2) (v : Ext k) :
    sourceAction k g (u ⊗ₜ[ℂ] v) = exteriorRepresentation 2 g u ⊗ₜ[ℂ] exteriorRepresentation k g v :=
  TensorProduct.map_tmul _ _ _ _

private def lower {k l : ℕ} (T : Intertwiners k l) : Form k l :=
  asForm ((tensorMetric l).toLinearMap.comp T.toLinearMap)

private theorem lower_mem {k l : ℕ} (T : Intertwiners k l) : lower T ∈ invariantForms k l := by
  intro g x u v w
  have h := Representation.IntertwiningMap.isIntertwining (sourceAction k) (action l) T g (u ⊗ₜ[ℂ] v)
  rw [source_tmul] at h
  change tensorMetric l (T (exteriorRepresentation 2 g u ⊗ₜ[ℂ] exteriorRepresentation k g v))
    (g.val x ⊗ₜ[ℂ] exteriorRepresentation l g w) = tensorMetric l (T (u ⊗ₜ[ℂ] v)) (x ⊗ₜ[ℂ] w)
  have hw : action l g (x ⊗ₜ[ℂ] w) = g.val x ⊗ₜ[ℂ] exteriorRepresentation l g w :=
    action_tmul l g x w
  rw [h, ← hw, tensorMetric_invariant]

private def lowerLinear (k l : ℕ) : Intertwiners k l →ₗ[ℂ] invariantForms k l where
  toFun T := ⟨lower T, lower_mem T⟩
  map_add' T U := by
    apply Subtype.ext
    apply coefficient_ext
    intro q
    change tensorMetric l ((T + U) (basis 2 q.first ⊗ₜ[ℂ] basis k q.second))
      (e q.axis ⊗ₜ[ℂ] basis l q.third) = _
    simp only [Representation.IntertwiningMap.coe_add, Pi.add_apply, map_add, LinearMap.add_apply]
    rfl
  map_smul' a T := by
    apply Subtype.ext
    apply coefficient_ext
    intro q
    change tensorMetric l ((a • T) (basis 2 q.first ⊗ₜ[ℂ] basis k q.second))
      (e q.axis ⊗ₜ[ℂ] basis l q.third) = _
    simp only [Representation.IntertwiningMap.coe_smul, Pi.smul_apply, map_smul, LinearMap.smul_apply]
    rfl

private theorem lower_injective (k l : ℕ) : Function.Injective (lowerLinear k l) := by
  intro T U h
  apply Representation.IntertwiningMap.ext
  apply TensorProduct.ext'
  intro u v
  apply (tensorMetric l).injective
  apply TensorProduct.ext'
  intro x w
  have he := congrArg (fun F : ↥(invariantForms k l) => F.val x u v w) h
  exact he

private theorem vector_surjective (g : splitSpecialOrthogonal) : Function.Surjective g.val := by
  let e := LinearMap.equivOfIsUnitDet (g.prop.1 ▸ isUnit_one : IsUnit g.val.det)
  have he : e.toLinearMap = g.val := LinearMap.coe_equivOfIsUnitDet _
  rw [← he, LinearEquiv.coe_coe]
  exact e.surjective

private theorem lower_surjective (k l : ℕ) : Function.Surjective (lowerLinear k l) := by
  intro F
  let f := (tensorMetric l).symm.toLinearMap.comp (asRaw F.val)
  have hmetric (u : Source k) : tensorMetric l (f u) = asRaw F.val u :=
    (tensorMetric l).apply_symm_apply _
  let T : Intertwiners k l :=
    { toLinearMap := f
      isIntertwining' g := by
        apply TensorProduct.ext'
        intro u v
        simp only [LinearMap.comp_apply, source_tmul]
        apply (tensorMetric l).injective
        apply TensorProduct.ext'
        intro x w
        obtain ⟨x', rfl⟩ := vector_surjective g x
        obtain ⟨w', rfl⟩ := exterior_surjective l g w
        have hw : action l g (x' ⊗ₜ[ℂ] w') = g.val x' ⊗ₜ[ℂ] exteriorRepresentation l g w' :=
          action_tmul l g x' w'
        rw [← hw, tensorMetric_invariant, hmetric, hmetric, hw, asRaw_tmul, asRaw_tmul]
        exact F.prop g x' u v w' }
  refine ⟨T, Subtype.ext ?_⟩
  apply coefficient_ext
  intro q
  change tensorMetric l (f (basis 2 q.first ⊗ₜ[ℂ] basis k q.second))
    (e q.axis ⊗ₜ[ℂ] basis l q.third) = _
  rw [hmetric, asRaw_tmul]
  rfl

/-- Lowering the vector and exterior output indices identifies the
unrestricted intertwiners with the invariant four-linear forms. -/
def intertwinerEquiv (k l : ℕ) : Intertwiners k l ≃ₗ[ℂ] invariantForms k l :=
  LinearEquiv.ofBijective (lowerLinear k l) ⟨lower_injective k l, lower_surjective k l⟩

theorem intertwinerEquiv_apply {k l : ℕ} (T : Intertwiners k l)
    (a : Space) (u : Ext 2) (x : Ext k) (y : Ext l) :
    (intertwinerEquiv k l T).val a u x y =
      tensorMetric l (T (u ⊗ₜ[ℂ] x)) (a ⊗ₜ[ℂ] y) := rfl

private def sourceDuality {k m : ℕ} (h : k + m = 14) : (sourceAction k).Equiv (sourceAction m) :=
  Representation.Equiv.mk (TensorProduct.congr (LinearEquiv.refl ℂ (Ext 2)) (starEquiv h)) (by
    intro g
    apply TensorProduct.ext'
    intro u v
    simp only [LinearMap.comp_apply, source_tmul, LinearEquiv.coe_coe, TensorProduct.congr_tmul,
      LinearEquiv.refl_apply, starEquiv_equivariant])

private def precomposeDuality {k m : ℕ} (h : k + m = 14) (l : ℕ) :
    Intertwiners m l ≃ₗ[ℂ] Intertwiners k l where
  toFun T := T.comp (sourceDuality h).toIntertwiningMap
  invFun T := T.comp (sourceDuality h).symm.toIntertwiningMap
  left_inv T := by
    apply Representation.IntertwiningMap.ext
    apply LinearMap.ext
    intro x
    change T ((sourceDuality h) ((sourceDuality h).symm x)) = T x
    rw [Representation.Equiv.apply_symm_apply]
  right_inv T := by
    apply Representation.IntertwiningMap.ext
    apply LinearMap.ext
    intro x
    change T ((sourceDuality h).symm ((sourceDuality h) x)) = T x
    rw [Representation.Equiv.symm_apply_apply]
  map_add' _ _ := Representation.IntertwiningMap.ext rfl
  map_smul' _ _ := Representation.IntertwiningMap.ext rfl

/-- The source grade can be replaced by its Hodge complement before
evaluating the partner and parity count. -/
theorem finrank_intertwiners (k l : Fin 15) :
    Module.finrank ℂ (Intertwiners k.val l.val) = quadMultiplicity (min k.val (14 - k.val)) l.val := by
  have hl : l.val ≤ 14 := by omega
  by_cases hk : k.val ≤ 7
  · have hle : k.val ≤ 14 - k.val := by omega
    rw [Nat.min_eq_left hle, (intertwinerEquiv k.val l.val).finrank_eq]
    exact D7QuadMultiplicity.finrank_invariantForms hk hl
  · have hsum : (14 - k.val) + k.val = 14 := by omega
    have hle : 14 - k.val ≤ k.val := by omega
    rw [Nat.min_eq_right hle, (precomposeDuality hsum l.val).finrank_eq,
      (intertwinerEquiv (14 - k.val) l.val).finrank_eq]
    exact D7QuadMultiplicity.finrank_invariantForms (by omega) hl

set_option maxRecDepth 8192 in
set_option maxHeartbeats 4000000 in
theorem unrestricted_by_grade :
    (List.ofFn fun k : Fin 15 => ∑ l : Fin 15, Module.finrank ℂ (Intertwiners k.val l.val)) =
      D7Counts.expectedRows.map (fun row => row.unrestricted.toNat) := by
  simp_rw [finrank_intertwiners]
  decide +kernel

set_option maxRecDepth 8192 in
set_option maxHeartbeats 4000000 in
theorem unrestricted_total :
    (∑ k : Fin 15, ∑ l : Fin 15, Module.finrank ℂ (Intertwiners k.val l.val)) = 200 := by
  simp_rw [finrank_intertwiners]
  decide +kernel

section Bundled

open CategoryTheory CategoryTheory.Limits

local instance : HasFiniteBiproducts (FDRep ℂ splitSpecialOrthogonal) :=
  HasFiniteBiproducts.of_hasFiniteProducts

def vectorTargetGrade (l : Fin 15) : FDRep ℂ splitSpecialOrthogonal :=
  FDRep.of (V := Product l.val) (action l.val)

def summedVectorTarget : FDRep ℂ splitSpecialOrthogonal := ⨁ vectorTargetGrade

set_option backward.isDefEq.respectTransparency false in
/-- Identify a bundled Hom block with the underlying intertwining maps. -/
def gradeHomEquiv (k l : Fin 15) :
    (sourceGrade 2 k ⟶ vectorTargetGrade l) ≃ₗ[ℂ] Intertwiners k.val l.val :=
  bundledHomEquiv (U := Source k.val) (W := Product l.val) (sourceAction k.val) (action l.val)

/-- The complex Hom dimension of the unrestricted symbol, on the
biproduct of all exterior grades. -/
theorem unrestricted_hom_dimension :
    Module.finrank ℂ (summedSource 2 ⟶ summedVectorTarget) = 200 := by
  change Module.finrank ℂ (⨁ sourceGrade 2 ⟶ ⨁ vectorTargetGrade) = _
  rw [(D7Classification.blockHomEquiv ℂ (sourceGrade 2) vectorTargetGrade).finrank_eq,
    Module.finrank_pi_fintype, ← unrestricted_total]
  apply Finset.sum_congr rfl
  intro k _
  rw [Module.finrank_pi_fintype]
  exact Finset.sum_congr rfl fun l _ => (gradeHomEquiv k l).finrank_eq

end Bundled

end
end GeometricUnity.D7Unrestricted
~~~

[Return to file index](#file-index)

## D7Final.lean {#source-d7final-lean}

Assembles the complex symbol channels, the Bianchi factorization, the hook count, and the general action-span comparison.

~~~lean
import D7Unrestricted

/-!
# The complex symbol channels and their dimensions

Lower the output indices with the determinant metrics and combine the vector
and two-form slots into a symbol. Equivariant restriction to the alternating,
trace, and joint-kernel summands then gives the channel decomposition.
-/

namespace GeometricUnity.D7Final

open D7Exterior D7Hodge D7Irreducible D7VectorTensor D7VectorGrades D7ComplementaryGrades
open D7Unrestricted (Intertwiners intertwinerEquiv summedVectorTarget unrestricted_hom_dimension)
open D7TripleInvariants (ExteriorIntertwiners metricEquiv metricEquiv_toLinearMap)
open D7TripleMultiplicity (sourceGrade targetGrade summedSource summedTarget bundledHomEquiv
  vector_and_bianchi_hom_dimensions vector_and_alternating_totals)
open scoped BigOperators TensorProduct

set_option backward.isDefEq.respectTransparency false

noncomputable section

private abbrev Group14 := ↥splitSpecialOrthogonal

abbrev SymbolForm (S : Type) [AddCommMonoid S] [Module ℂ S] (k l : ℕ) :=
  S →ₗ[ℂ] Ext k →ₗ[ℂ] Ext l →ₗ[ℂ] ℂ

def invariantSymbols {S : Type} [AddCommMonoid S] [Module ℂ S]
    (ρ : Representation ℂ Group14 S) (k l : ℕ) : Submodule ℂ (SymbolForm S k l) where
  carrier := {F | ∀ (g : Group14) s x y,
    F (ρ g s) (exteriorRepresentation k g x) (exteriorRepresentation l g y) = F s x y}
  add_mem' hF hG g s x y := by simp only [LinearMap.add_apply, hF g s x y, hG g s x y]
  zero_mem' := by
    change ∀ (g : Group14) (s : S) (x : Ext k) (y : Ext l), _ = _
    intros; rfl
  smul_mem' c F hF g s x y := by simp only [LinearMap.smul_apply, hF g s x y]

abbrev Symbols {S : Type} [AddCommMonoid S] [Module ℂ S]
    (ρ : Representation ℂ Group14 S) (k l : ℕ) := ↥(invariantSymbols ρ k l)

private abbrev Imm (k l : ℕ) := ↥(D7QuadInvariants.invariantForms k l)

private def evaluate {k l : ℕ} (x : Ext k) (y : Ext l) :
    (Ext k →ₗ[ℂ] Ext l →ₗ[ℂ] ℂ) →ₗ[ℂ] ℂ where
  toFun f := f x y
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

private theorem uncurry_invariant {k l : ℕ} (F : Imm k l) :
    TensorProduct.lift F.val ∈ invariantSymbols tensorAction k l := by
  intro g s x y
  let f := TensorProduct.lift F.val
  have h : ((evaluate (exteriorRepresentation k g x) (exteriorRepresentation l g y)).comp f).comp
      (tensorAction g) = (evaluate x y).comp f := by
    apply TensorProduct.ext'
    intro a u
    change f ((action 2) g (a ⊗ₜ[ℂ] u)) (exteriorRepresentation k g x) (exteriorRepresentation l g y) =
      f (a ⊗ₜ[ℂ] u) x y
    rw [action_tmul]
    exact F.prop g a u x y
  exact DFunLike.congr_fun h s

private theorem curry_invariant {k l : ℕ} (F : Symbols tensorAction k l) :
    TensorProduct.curry F.val ∈ D7QuadInvariants.invariantForms k l := by
  intro g a u x y
  have h := F.prop g (a ⊗ₜ[ℂ] u) x y
  change F.val ((action 2) g (a ⊗ₜ[ℂ] u)) _ _ = _ at h
  rw [action_tmul] at h
  exact h

/-- Lowering the output vector index turns the two exterior input slots
and the output vector slot into the divergence symbol. -/
def uncurrySymbol (k l : ℕ) : Imm k l ≃ₗ[ℂ] Symbols tensorAction k l where
  toFun F := ⟨TensorProduct.lift F.val, uncurry_invariant F⟩
  invFun F := ⟨TensorProduct.curry F.val, curry_invariant F⟩
  left_inv F := by
    apply Subtype.ext
    apply LinearMap.ext
    intro a
    apply LinearMap.ext
    intro u
    rfl
  right_inv F := by
    apply Subtype.ext
    apply TensorProduct.ext'
    intro a u
    rfl
  map_add' F G := by
    apply Subtype.ext
    apply TensorProduct.ext'
    intro a u
    rfl
  map_smul' c F := by
    apply Subtype.ext
    apply TensorProduct.ext'
    intro a u
    rfl

section Restriction

variable {S T : Type} [AddCommMonoid S] [Module ℂ S] [AddCommMonoid T] [Module ℂ T]
variable {ρ : Representation ℂ Group14 S} {σ : Representation ℂ Group14 T} {k l : ℕ}

def restrictSymbol (f : σ.IntertwiningMap ρ) : Symbols ρ k l →ₗ[ℂ] Symbols σ k l where
  toFun F := ⟨F.val.comp f.toLinearMap, by
    intro g s x y
    change F.val (f (σ g s)) _ _ = F.val (f s) x y
    rw [Representation.IntertwiningMap.isIntertwining σ ρ f]
    exact F.prop g (f s) x y⟩
  map_add' F G := by
    apply Subtype.ext
    apply LinearMap.ext
    intro x
    rfl
  map_smul' c F := by
    apply Subtype.ext
    apply LinearMap.ext
    intro x
    rfl

@[simp] theorem restrictSymbol_apply (f : σ.IntertwiningMap ρ) (F : Symbols ρ k l)
    (s : T) (x : Ext k) (y : Ext l) :
    (restrictSymbol f F).val s x y = F.val (f s) x y := rfl

def restrictEquiv (e : σ.Equiv ρ) : Symbols ρ k l ≃ₗ[ℂ] Symbols σ k l :=
  LinearEquiv.ofLinearMap (restrictSymbol e.toIntertwiningMap) (restrictSymbol e.symm.toIntertwiningMap)
    (by
      apply LinearMap.ext
      intro F
      apply Subtype.ext
      apply LinearMap.ext
      intro s
      change F.val (e.symm (e s)) = F.val s
      rw [Representation.Equiv.symm_apply_apply])
    (by
      apply LinearMap.ext
      intro F
      apply Subtype.ext
      apply LinearMap.ext
      intro s
      change F.val (e (e.symm s)) = F.val s
      rw [Representation.Equiv.apply_symm_apply])

private def symbolInl (ρ : Representation ℂ Group14 S) (σ : Representation ℂ Group14 T) :
    ρ.IntertwiningMap (ρ.prod σ) := Representation.IntertwiningMap.inl ℂ ρ σ
private def symbolInr (ρ : Representation ℂ Group14 S) (σ : Representation ℂ Group14 T) :
    σ.IntertwiningMap (ρ.prod σ) := Representation.IntertwiningMap.inr ℂ ρ σ

def productSymbols (ρ : Representation ℂ Group14 S) (σ : Representation ℂ Group14 T) (k l : ℕ) :
    Symbols (ρ.prod σ) k l ≃ₗ[ℂ] Symbols ρ k l × Symbols σ k l where
  toFun F := (restrictSymbol (symbolInl ρ σ) F, restrictSymbol (symbolInr ρ σ) F)
  invFun p := restrictSymbol (Representation.IntertwiningMap.fst ℂ ρ σ) p.1 +
    restrictSymbol (Representation.IntertwiningMap.snd ℂ ρ σ) p.2
  left_inv F := by
    apply Subtype.ext
    apply LinearMap.ext
    intro s
    change F.val (s.1, 0) + F.val (0, s.2) = F.val s
    rw [← map_add]
    congr 1
    exact Prod.ext (add_zero _) (zero_add _)
  right_inv p := by
    apply Prod.ext
    · apply Subtype.ext
      apply LinearMap.ext
      intro s
      change p.1.val s + p.2.val 0 = p.1.val s
      rw [map_zero, add_zero]
    · apply Subtype.ext
      apply LinearMap.ext
      intro t
      change p.1.val 0 + p.2.val t = p.2.val t
      rw [map_zero, zero_add]
  map_add' F G := Prod.ext (map_add _ _ _) (map_add _ _ _)
  map_smul' c F := Prod.ext (map_smul _ _ _) (map_smul _ _ _)

end Restriction

section Lowering

variable {S : Type} [AddCommMonoid S] [Module ℂ S]

abbrev SymbolIntertwiners (ρ : Representation ℂ Group14 S) (k l : ℕ) :=
  (ρ.tprod (exteriorRepresentation k)).IntertwiningMap (exteriorRepresentation l)

private def lowerSymbol {ρ : Representation ℂ Group14 S} {k l : ℕ} (T : SymbolIntertwiners ρ k l) :
    SymbolForm S k l :=
  TensorProduct.curry ((metricEquiv l).toLinearMap.comp T.toLinearMap)

private theorem lowerSymbol_apply {ρ : Representation ℂ Group14 S} {k l : ℕ} (T : SymbolIntertwiners ρ k l)
    (s : S) (x : Ext k) (y : Ext l) :
    lowerSymbol T s x y = exteriorMetric l (T (s ⊗ₜ[ℂ] x)) y := by
  change (metricEquiv l).toLinearMap (T (s ⊗ₜ[ℂ] x)) y = _
  rw [metricEquiv_toLinearMap]

private theorem lowerSymbol_invariant {ρ : Representation ℂ Group14 S} {k l : ℕ}
    (T : SymbolIntertwiners ρ k l) : lowerSymbol T ∈ invariantSymbols ρ k l := by
  intro g s x y
  rw [lowerSymbol_apply, lowerSymbol_apply]
  have he := Representation.IntertwiningMap.isIntertwining
    (ρ.tprod (exteriorRepresentation k)) (exteriorRepresentation l) T g (s ⊗ₜ[ℂ] x)
  simp only [Representation.tprod_apply, TensorProduct.map_tmul] at he
  rw [he, metric_invariant]

private def lower (ρ : Representation ℂ Group14 S) (k l : ℕ) :
    SymbolIntertwiners ρ k l →ₗ[ℂ] Symbols ρ k l where
  toFun T := ⟨lowerSymbol T, lowerSymbol_invariant T⟩
  map_add' T U := by
    apply Subtype.ext
    apply LinearMap.ext
    intro s
    apply LinearMap.ext
    intro x
    apply LinearMap.ext
    intro y
    change lowerSymbol (T + U) s x y = lowerSymbol T s x y + lowerSymbol U s x y
    simp only [lowerSymbol_apply, Representation.IntertwiningMap.coe_add,
      Pi.add_apply, map_add, LinearMap.add_apply]
  map_smul' c T := by
    apply Subtype.ext
    apply LinearMap.ext
    intro s
    apply LinearMap.ext
    intro x
    apply LinearMap.ext
    intro y
    change lowerSymbol (c • T) s x y = c • lowerSymbol T s x y
    simp only [lowerSymbol_apply, Representation.IntertwiningMap.coe_smul,
      Pi.smul_apply, map_smul, LinearMap.smul_apply]

private theorem lower_injective (ρ : Representation ℂ Group14 S) (k l : ℕ) :
    Function.Injective (lower ρ k l) := by
  intro T U h
  apply Representation.IntertwiningMap.ext
  apply TensorProduct.ext'
  intro s x
  apply (metricEquiv l).injective
  exact congrArg (fun F : Symbols ρ k l => F.val s x) h

private theorem lower_surjective (ρ : Representation ℂ Group14 S) (k l : ℕ) :
    Function.Surjective (lower ρ k l) := by
  intro F
  let f := (metricEquiv l).symm.toLinearMap.comp (TensorProduct.lift F.val)
  have hv (s : S) (x : Ext k) : exteriorMetric l (f (s ⊗ₜ[ℂ] x)) = F.val s x := by
    rw [← metricEquiv_toLinearMap]
    change metricEquiv l ((metricEquiv l).symm (TensorProduct.lift F.val (s ⊗ₜ[ℂ] x))) = _
    rw [LinearEquiv.apply_symm_apply, TensorProduct.lift.tmul]
  let T : SymbolIntertwiners ρ k l :=
    { toLinearMap := f
      isIntertwining' g := by
        apply TensorProduct.ext'
        intro s x
        simp only [LinearMap.comp_apply, Representation.tprod_apply, TensorProduct.map_tmul]
        apply exteriorMetric_injective l
        apply LinearMap.ext
        intro y
        obtain ⟨z, rfl⟩ := exterior_surjective l g y
        rw [metric_invariant, hv, hv]
        exact F.prop g s x z }
  refine ⟨T, Subtype.ext ?_⟩
  apply LinearMap.ext
  intro s
  apply LinearMap.ext
  intro x
  apply LinearMap.ext
  intro y
  change lowerSymbol T s x y = _
  rw [lowerSymbol_apply]
  exact DFunLike.congr_fun (hv s x) y

/-- Raising the last exterior index recovers the intertwiners of the
symbol representation tensored with the input grade. -/
def symbolIntertwinerEquiv (ρ : Representation ℂ Group14 S) (k l : ℕ) :
    SymbolIntertwiners ρ k l ≃ₗ[ℂ] Symbols ρ k l :=
  LinearEquiv.ofBijective (lower ρ k l) ⟨lower_injective ρ k l, lower_surjective ρ k l⟩

private theorem freeSymbolIntertwiners (ρ : Representation ℂ Group14 S) (k l : ℕ) :
    Module.Free ℂ (SymbolIntertwiners ρ k l) :=
  @Module.Free.of_divisionRing ℂ (SymbolIntertwiners ρ k l) _
    (Representation.IntertwiningMap.instAddCommGroup
      (ρ.tprod (exteriorRepresentation k)) (exteriorRepresentation l)) _

end Lowering

private theorem finiteSymbolIntertwiners {S : Type} [AddCommGroup S] [Module ℂ S]
    [Module.Finite ℂ S]
    (ρ : Representation ℂ Group14 S) (k l : ℕ) :
    Module.Finite ℂ (SymbolIntertwiners ρ k l) :=
  Module.Finite.of_injective
    (Representation.IntertwiningMap.toLinearMapl
      (ρ := ρ.tprod (exteriorRepresentation k)) (σ := exteriorRepresentation l))
    (Representation.IntertwiningMap.toLinearMap_injective _ _)

private def oneExterior : (exteriorRepresentation 1).Equiv vectorAction :=
  Representation.Equiv.mk (exteriorPower.oneEquiv ℂ Space) (fun g =>
    exteriorPower.oneEquiv_naturality g.val)

local instance hookTensorAddCommGroup (k : ℕ) : AddCommGroup (↥hook ⊗[ℂ] Ext k) :=
  @TensorProduct.addCommGroup ℂ _ ↥hook (Ext k) hook.addCommGroup _ _ _

abbrev HookIntertwiners (k l : ℕ) := SymbolIntertwiners hookAction k l

/-- Lower both output indices and combine the vector and two-form slots. -/
def divergenceSymbol (k l : ℕ) : Intertwiners k l ≃ₗ[ℂ] Symbols tensorAction k l :=
  (intertwinerEquiv k l).trans (uncurrySymbol k l)

theorem divergenceSymbol_tmul {k l : ℕ} (T : Intertwiners k l)
    (a : Space) (u : Ext 2) (x : Ext k) (y : Ext l) :
    (divergenceSymbol k l T).val (a ⊗ₜ[ℂ] u) x y =
      D7Unrestricted.tensorMetric l (T (u ⊗ₜ[ℂ] x)) (a ⊗ₜ[ℂ] y) :=
  D7Unrestricted.intertwinerEquiv_apply T a u x y

/-- Restrict the divergence symbol to the alternating, vector, and
traceless hook summands and raise the exterior output index in each. -/
def gradeChannelSplit (k l : ℕ) :
    Intertwiners k l ≃ₗ[ℂ]
      ExteriorIntertwiners 3 k l × ExteriorIntertwiners 1 k l × HookIntertwiners k l := by
  let A := exteriorRepresentation 3
  let B := vectorAction
  let H := hookAction
  let split := restrictEquiv (k := k) (l := l) D7VectorTensor.splitRepresentation.symm
  let splitFirst := productSymbols A (B.prod H) k l
  let splitRest := productSymbols B H k l
  let alternating := (symbolIntertwinerEquiv A k l).symm
  let vector := (restrictEquiv (k := k) (l := l) oneExterior).trans
    (symbolIntertwinerEquiv (exteriorRepresentation 1) k l).symm
  let residual := (symbolIntertwinerEquiv H k l).symm
  exact (divergenceSymbol k l).trans (split.trans (splitFirst.trans
    (alternating.prodCongr (splitRest.trans (vector.prodCongr residual)))))

theorem grade_dimension_sum (k l : ℕ) :
    Module.finrank ℂ (Intertwiners k l) =
      Module.finrank ℂ (ExteriorIntertwiners 3 k l) +
      Module.finrank ℂ (ExteriorIntertwiners 1 k l) +
      Module.finrank ℂ (HookIntertwiners k l) := by
  have hA : Module.Finite ℂ (ExteriorIntertwiners 3 k l) :=
    finiteSymbolIntertwiners (exteriorRepresentation 3) k l
  have hV : Module.Finite ℂ (ExteriorIntertwiners 1 k l) :=
    finiteSymbolIntertwiners (exteriorRepresentation 1) k l
  have hH : Module.Finite ℂ (HookIntertwiners k l) :=
    @finiteSymbolIntertwiners ↥hook hook.addCommGroup hook.module
      (FiniteDimensional.finiteDimensional_submodule hook) hookAction k l
  have fA : Module.Free ℂ (ExteriorIntertwiners 3 k l) :=
    freeSymbolIntertwiners (exteriorRepresentation 3) k l
  have fV : Module.Free ℂ (ExteriorIntertwiners 1 k l) :=
    freeSymbolIntertwiners (exteriorRepresentation 1) k l
  have fH : Module.Free ℂ (HookIntertwiners k l) :=
    freeSymbolIntertwiners (S := ↥hook) hookAction k l
  rw [(gradeChannelSplit k l).finrank_eq,
    Module.finrank_prod (M := ExteriorIntertwiners 3 k l)
      (M' := ExteriorIntertwiners 1 k l × HookIntertwiners k l),
    Module.finrank_prod (M := ExteriorIntertwiners 1 k l) (M' := HookIntertwiners k l)]
  omega

def altMap : tensorAction.IntertwiningMap (exteriorRepresentation 3) :=
  ⟨alternation, alternation_equivariant⟩

private def threeMap : (exteriorRepresentation 3).IntertwiningMap tensorAction :=
  ⟨includeThree, includeThree_equivariant⟩

/-- Bianchi-compatible symbols annihilate the kernel of alternation. -/
def bianchiSymbols (k l : ℕ) : Submodule ℂ (Symbols tensorAction k l) where
  carrier := {F | ∀ s, alternation s = 0 → F.val s = 0}
  zero_mem' := fun _ _ => rfl
  add_mem' {F G} hF hG s hs := by
    change F.val s + G.val s = 0
    rw [hF s hs, hG s hs, add_zero]
  smul_mem' c F hF s hs := by
    change c • F.val s = 0
    rw [hF s hs, smul_zero]

private theorem pullback_alt_mem {k l : ℕ} (A : Symbols (exteriorRepresentation 3) k l) :
    restrictSymbol altMap A ∈ bianchiSymbols k l := by
  intro s hs
  change A.val (alternation s) = 0
  rw [hs, map_zero]

private theorem recover_from_three {k l : ℕ} {F : Symbols tensorAction k l}
    (h : F ∈ bianchiSymbols k l) :
    restrictSymbol altMap (restrictSymbol threeMap F) = F := by
  apply Subtype.ext
  apply LinearMap.ext
  intro s
  change F.val (includeThree (alternation s)) = F.val s
  have hker : alternation (s - includeThree (alternation s)) = 0 := by
    rw [map_sub, alternation_three, sub_self]
  have hzero := h _ hker
  rw [map_sub, sub_eq_zero] at hzero
  exact hzero.symm

private theorem recover_from_alt {k l : ℕ} (A : Symbols (exteriorRepresentation 3) k l) :
    restrictSymbol threeMap (restrictSymbol altMap A) = A := by
  apply Subtype.ext
  apply LinearMap.ext
  intro u
  change A.val (alternation (includeThree u)) = A.val u
  rw [alternation_three]

/-- The Bianchi condition is equivalent to unique equivariant factorization
through alternation in the symbol argument. -/
theorem bianchi_iff_factor {k l : ℕ} (F : Symbols tensorAction k l) :
    F ∈ bianchiSymbols k l ↔
      ∃! A : Symbols (exteriorRepresentation 3) k l, restrictSymbol altMap A = F := by
  constructor
  · intro h
    refine ⟨restrictSymbol threeMap F, recover_from_three h, ?_⟩
    intro A hA
    rw [← hA, recover_from_alt]
  · rintro ⟨A, rfl, _⟩
    exact pullback_alt_mem A

/-- Restriction to the alternating summand and pullback along alternation
are inverse on the Bianchi-compatible subspace. -/
def bianchiEquiv (k l : ℕ) :
    ↥(bianchiSymbols k l) ≃ₗ[ℂ] ExteriorIntertwiners 3 k l := by
  let f := (restrictSymbol (k := k) (l := l) threeMap).comp (bianchiSymbols k l).subtype
  let g := (restrictSymbol (k := k) (l := l) altMap).codRestrict (bianchiSymbols k l) pullback_alt_mem
  let e : ↥(bianchiSymbols k l) ≃ₗ[ℂ] Symbols (exteriorRepresentation 3) k l :=
    LinearEquiv.ofLinearMap f g
    (LinearMap.ext recover_from_alt)
    (LinearMap.ext fun F => Subtype.ext (recover_from_three F.prop))
  exact e.trans (symbolIntertwinerEquiv (exteriorRepresentation 3) k l).symm

/-- The subspace of the original two-form-to-vector intertwiners selected
by the Bianchi condition on their divergence symbols. -/
def bianchiIntertwiners (k l : ℕ) : Submodule ℂ (Intertwiners k l) :=
  (bianchiSymbols k l).comap (divergenceSymbol k l).toLinearMap

def bianchiIntertwinerEquiv (k l : ℕ) :
    ↥(bianchiIntertwiners k l) ≃ₗ[ℂ] ExteriorIntertwiners 3 k l :=
  ((divergenceSymbol k l).ofSubmodules (bianchiIntertwiners k l) (bianchiSymbols k l)
    ((bianchiSymbols k l).map_comap_eq_of_surjective (divergenceSymbol k l).surjective)).trans
    (bianchiEquiv k l)

theorem bianchi_grade_total :
    (∑ k : Fin 15, ∑ l : Fin 15, Module.finrank ℂ ↥(bianchiIntertwiners k.val l.val)) = 96 := by
  calc
    _ = ∑ k : Fin 15, ∑ l : Fin 15, Module.finrank ℂ (ExteriorIntertwiners 3 k.val l.val) :=
      Finset.sum_congr rfl fun k _ =>
        Finset.sum_congr rfl fun l _ => (bianchiIntertwinerEquiv k.val l.val).finrank_eq
    _ = 96 := vector_and_alternating_totals.2

private theorem hook_grade_difference (k : Fin 15) :
    (∑ l : Fin 15, Module.finrank ℂ (HookIntertwiners k.val l.val)) =
      (∑ l : Fin 15, Module.finrank ℂ (Intertwiners k.val l.val)) -
        (∑ l : Fin 15, Module.finrank ℂ (ExteriorIntertwiners 3 k.val l.val)) -
        (∑ l : Fin 15, Module.finrank ℂ (ExteriorIntertwiners 1 k.val l.val)) := by
  have h (l : Fin 15) := grade_dimension_sum k.val l.val
  conv_rhs =>
    rw [show (∑ l : Fin 15, Module.finrank ℂ (Intertwiners k.val l.val)) = _ from
      Finset.sum_congr rfl (fun l _ => h l)]
  simp only [Finset.sum_add_distrib]
  omega

private def rowDifference (unrestricted alternating vector : List ℕ) : List ℕ :=
  List.zipWith (· - ·) (List.zipWith (· - ·) unrestricted alternating) vector

/-- The fifteen input-grade rows for the actual complex hook intertwiners. -/
theorem hook_by_grade :
    (List.ofFn fun k : Fin 15 => ∑ l : Fin 15, Module.finrank ℂ (HookIntertwiners k.val l.val)) =
      D7Counts.expectedRows.map (fun row => row.hook.toNat) := by
  rw [show (List.ofFn fun k : Fin 15 => ∑ l : Fin 15,
      Module.finrank ℂ (HookIntertwiners k.val l.val)) =
    rowDifference
      (List.ofFn fun k : Fin 15 => ∑ l : Fin 15, Module.finrank ℂ (Intertwiners k.val l.val))
      (List.ofFn fun k : Fin 15 => ∑ l : Fin 15, Module.finrank ℂ (ExteriorIntertwiners 3 k.val l.val))
      (List.ofFn fun k : Fin 15 => ∑ l : Fin 15, Module.finrank ℂ (ExteriorIntertwiners 1 k.val l.val)) by
        apply List.ext_getElem
        · simp [rowDifference]
        · intro i hi _
          simp only [rowDifference, List.getElem_zipWith, List.getElem_ofFn]
          exact hook_grade_difference ⟨i, by simpa using hi⟩]
  rw [D7Unrestricted.unrestricted_by_grade, D7TripleMultiplicity.alternating_multiplicities_by_grade,
    D7TripleMultiplicity.vector_multiplicities_by_grade]
  decide +kernel

theorem hook_grade_total :
    (∑ k : Fin 15, ∑ l : Fin 15, Module.finrank ℂ (HookIntertwiners k.val l.val)) = 48 := by
  have h : (∑ k : Fin 15, ∑ l : Fin 15, Module.finrank ℂ (Intertwiners k.val l.val)) =
      (∑ k : Fin 15, ∑ l : Fin 15, Module.finrank ℂ (ExteriorIntertwiners 3 k.val l.val)) +
      (∑ k : Fin 15, ∑ l : Fin 15, Module.finrank ℂ (ExteriorIntertwiners 1 k.val l.val)) +
      (∑ k : Fin 15, ∑ l : Fin 15, Module.finrank ℂ (HookIntertwiners k.val l.val)) := by
    simp_rw [grade_dimension_sum]
    simp only [Finset.sum_add_distrib]
  rw [D7Unrestricted.unrestricted_total, vector_and_alternating_totals.1,
    vector_and_alternating_totals.2] at h
  omega

section Bundled

open CategoryTheory CategoryTheory.Limits

local instance : HasFiniteBiproducts (FDRep ℂ splitSpecialOrthogonal) :=
  HasFiniteBiproducts.of_hasFiniteProducts

/-- The grade blocks of the full two-form-to-vector Hom space. -/
def unrestrictedBlocks :
    (summedSource 2 ⟶ summedVectorTarget) ≃ₗ[ℂ]
      (∀ k l : Fin 15, Intertwiners k.val l.val) :=
  (D7Classification.blockHomEquiv ℂ (sourceGrade 2) D7Unrestricted.vectorTargetGrade).trans
    (LinearEquiv.piCongrRight fun k =>
      LinearEquiv.piCongrRight fun l => D7Unrestricted.gradeHomEquiv k l)

/-- A full equivariant operator is Bianchi-compatible when its divergence
symbol in every input and output grade annihilates the kernel of alternation. -/
def bianchiHom : Submodule ℂ (summedSource 2 ⟶ summedVectorTarget) :=
  (Submodule.pi Set.univ fun k : Fin 15 =>
    Submodule.pi Set.univ fun l : Fin 15 => bianchiIntertwiners k.val l.val).comap
    unrestrictedBlocks.toLinearMap

theorem mem_bianchiHom (T : summedSource 2 ⟶ summedVectorTarget) :
    T ∈ bianchiHom ↔ ∀ k l : Fin 15,
      unrestrictedBlocks T k l ∈ bianchiIntertwiners k.val l.val := by
  simp [bianchiHom, Submodule.mem_pi]

private def bianchiHomBlocks :
    ↥bianchiHom ≃ₗ[ℂ] (∀ k l : Fin 15, ↥(bianchiIntertwiners k.val l.val)) where
  toFun T k l := ⟨unrestrictedBlocks T.val k l, (mem_bianchiHom T.val).mp T.prop k l⟩
  invFun B := ⟨unrestrictedBlocks.symm (fun k l => (B k l).val), by
    apply (mem_bianchiHom _).mpr
    rw [LinearEquiv.apply_symm_apply]
    exact fun k l => (B k l).prop⟩
  left_inv T := Subtype.ext (unrestrictedBlocks.symm_apply_apply T.val)
  right_inv B := by
    funext k l
    apply Subtype.ext
    exact congrFun (congrFun (unrestrictedBlocks.apply_symm_apply (fun k l => (B k l).val)) k) l
  map_add' T S := by
    funext k l
    apply Subtype.ext
    exact congrFun (congrFun (map_add unrestrictedBlocks T.val S.val) k) l
  map_smul' c T := by
    funext k l
    apply Subtype.ext
    exact congrFun (congrFun (map_smul unrestrictedBlocks c T.val) k) l

set_option maxHeartbeats 1200000 in
/-- Assemble the unique alternating factor of each block into a map
from the full alternating source. -/
def bianchiHomEquiv : ↥bianchiHom ≃ₗ[ℂ] (summedSource 3 ⟶ summedTarget) := by
  let grade (k l : Fin 15) :
      (sourceGrade 3 k ⟶ targetGrade l) ≃ₗ[ℂ] ExteriorIntertwiners 3 k.val l.val :=
    bundledHomEquiv (U := Ext 3 ⊗[ℂ] Ext k.val) (W := Ext l.val)
      ((exteriorRepresentation 3).tprod (exteriorRepresentation k.val))
      (exteriorRepresentation l.val)
  let blocks : (∀ k l : Fin 15, ↥(bianchiIntertwiners k.val l.val)) ≃ₗ[ℂ]
      (∀ k l : Fin 15, sourceGrade 3 k ⟶ targetGrade l) :=
    LinearEquiv.piCongrRight fun k => LinearEquiv.piCongrRight fun l =>
      (bianchiIntertwinerEquiv k.val l.val).trans (grade k l).symm
  change ↥bianchiHom ≃ₗ[ℂ] (⨁ sourceGrade 3 ⟶ ⨁ targetGrade)
  exact bianchiHomBlocks.trans (blocks.trans
    (D7Classification.blockHomEquiv ℂ (sourceGrade 3) targetGrade).symm)

/-- The Bianchi-compatible subspace of the full unrestricted complex Hom
space has dimension 96. -/
theorem bianchi_hom_dimension : Module.finrank ℂ ↥bianchiHom = 96 :=
  bianchiHomEquiv.finrank_eq.trans vector_and_bianchi_hom_dimensions.2

def hookGrade (k : Fin 15) : FDRep ℂ splitSpecialOrthogonal :=
  FDRep.of (V := ↥hook ⊗[ℂ] Ext k.val) (hookAction.tprod (exteriorRepresentation k.val))

def summedHook : FDRep ℂ splitSpecialOrthogonal := ⨁ hookGrade

private def hookGradeHomEquiv (k l : Fin 15) :
    (hookGrade k ⟶ targetGrade l) ≃ₗ[ℂ] HookIntertwiners k.val l.val :=
  bundledHomEquiv (U := ↥hook ⊗[ℂ] Ext k.val) (W := Ext l.val)
    (hookAction.tprod (exteriorRepresentation k.val)) (exteriorRepresentation l.val)

theorem hook_hom_dimension : Module.finrank ℂ (summedHook ⟶ summedTarget) = 48 := by
  change Module.finrank ℂ (⨁ hookGrade ⟶ ⨁ targetGrade) = _
  rw [(D7Classification.blockHomEquiv ℂ hookGrade targetGrade).finrank_eq,
    Module.finrank_pi_fintype, ← hook_grade_total]
  apply Finset.sum_congr rfl
  intro k _
  rw [Module.finrank_pi_fintype]
  exact Finset.sum_congr rfl fun l _ => (hookGradeHomEquiv k l).finrank_eq

/-- The unrestricted, alternating, vector, and hook Hom space dimensions. -/
theorem complex_channel_dimensions :
    (Module.finrank ℂ (summedSource 2 ⟶ summedVectorTarget),
     Module.finrank ℂ (summedSource 3 ⟶ summedTarget),
     Module.finrank ℂ (summedSource 1 ⟶ summedTarget),
     Module.finrank ℂ (summedHook ⟶ summedTarget)) = (200, 96, 56, 48) := by
  rw [unrestricted_hom_dimension, vector_and_bianchi_hom_dimensions.2,
    vector_and_bianchi_hom_dimensions.1, hook_hom_dimension]

end Bundled

/-- Transport the dimension once the complexified real action has been
compared with the complex intertwiner space. -/
theorem real_dimension_of_comparison {G m n : Type} [Fintype m] [Fintype n]
    (ρ : G → Matrix m m ℝ) (τ : G → Matrix n n ℝ)
    {E : Type} [AddCommGroup E] [Module ℂ E]
    (e : D7Classification.ComplexIntertwiners ρ τ ≃ₗ[ℂ] E) :
    Module.finrank ℝ (D7Classification.RealIntertwiners ρ τ) = Module.finrank ℂ E :=
  (D7Classification.finrank_real_complex_intertwiners ρ τ).trans e.finrank_eq

section RealAction

variable {G H m n U W : Type} [Monoid G] [Monoid H]
variable [AddCommGroup U] [AddCommGroup W] [Module ℂ U] [Module ℂ W]

private def intertwiningDefect (T : U →ₗ[ℂ] W) :
    (Module.End ℂ U × Module.End ℂ W) →ₗ[ℂ] (U →ₗ[ℂ] W) where
  toFun p := T.comp p.1 - p.2.comp T
  map_add' p q := by
    change T.comp (p.1 + q.1) - (p.2 + q.2).comp T =
      (T.comp p.1 - p.2.comp T) + (T.comp q.1 - q.2.comp T)
    rw [LinearMap.comp_add, LinearMap.add_comp]
    abel
  map_smul' c p := by
    change T.comp (c • p.1) - (c • p.2).comp T = c • (T.comp p.1 - p.2.comp T)
    rw [LinearMap.comp_smul, LinearMap.smul_comp, smul_sub]

/-- It suffices for the restricted actions to span the pairs of ambient
actions on source and target. The intertwining equation is linear in
that pair for each candidate intertwiner. -/
def restrictGroupEquiv (φ : H →* G) (ρ : Representation ℂ G U) (τ : Representation ℂ G W)
    (hspan : ∀ g, (ρ g, τ g) ∈ Submodule.span ℂ (Set.range fun h => (ρ (φ h), τ (φ h)))) :
    ρ.IntertwiningMap τ ≃ₗ[ℂ] Representation.IntertwiningMap (ρ.comp φ) (τ.comp φ) where
  toFun T := ⟨T.toLinearMap, fun h => T.isIntertwining' (φ h)⟩
  invFun T := ⟨T.toLinearMap, by
    let d := intertwiningDefect T.toLinearMap
    have hker : Submodule.span ℂ (Set.range fun h => (ρ (φ h), τ (φ h))) ≤ d.ker := by
      apply Submodule.span_le.mpr
      rintro _ ⟨h, rfl⟩
      exact sub_eq_zero.mpr (T.isIntertwining' h)
    intro g
    exact sub_eq_zero.mp (hker (hspan g))⟩
  left_inv _ := Representation.IntertwiningMap.ext rfl
  right_inv _ := Representation.IntertwiningMap.ext rfl
  map_add' _ _ := Representation.IntertwiningMap.ext rfl
  map_smul' _ _ := Representation.IntertwiningMap.ext rfl

variable [Fintype m] [Fintype n] [DecidableEq m] [DecidableEq n]

/-- Coordinates identify equivariant linear maps with the matrix intertwiner equations. -/
def intertwinerMatrices {K X Y : Type*} [Field K] [AddCommGroup X] [AddCommGroup Y]
    [Module K X] [Module K Y] (b : Module.Basis m K X) (c : Module.Basis n K Y)
    (ρ : Representation K H X) (τ : Representation K H Y) :
    ρ.IntertwiningMap τ ≃ₗ[K] ↥(D7Classification.matrixIntertwiners
      (fun h => LinearMap.toMatrix b b (ρ h)) (fun h => LinearMap.toMatrix c c (τ h))) where
  toFun T := ⟨LinearMap.toMatrix b c T.toLinearMap, by
    intro h
    change LinearMap.toMatrix b c T.toLinearMap * LinearMap.toMatrix b b (ρ h) =
      LinearMap.toMatrix c c (τ h) * LinearMap.toMatrix b c T.toLinearMap
    rw [← LinearMap.toMatrix_comp b b c, ← LinearMap.toMatrix_comp b c c, T.isIntertwining']⟩
  invFun X := ⟨(LinearMap.toMatrix b c).symm X.val, by
    intro h
    apply (LinearMap.toMatrix b c).injective
    rw [LinearMap.toMatrix_comp b b c, LinearMap.toMatrix_comp b c c, LinearEquiv.apply_symm_apply]
    exact X.prop h⟩
  left_inv T := Representation.IntertwiningMap.ext ((LinearMap.toMatrix b c).symm_apply_apply _)
  right_inv X := Subtype.ext ((LinearMap.toMatrix b c).apply_symm_apply _)
  map_add' T S := Subtype.ext (map_add (LinearMap.toMatrix b c) T.toLinearMap S.toLinearMap)
  map_smul' a T := Subtype.ext (map_smul (LinearMap.toMatrix b c) a T.toLinearMap)

/-- Real descent with explicit comparison conditions. In the chosen complex
bases, the real matrices must complexify to the restricted actions, and
those actions must span the ambient pairs. -/
theorem real_dimension_of_action_span
    (φ : H →* G) (ρ : Representation ℂ G U) (τ : Representation ℂ G W)
    (a : H → Matrix m m ℝ) (b : H → Matrix n n ℝ)
    (u : Module.Basis m ℂ U) (w : Module.Basis n ℂ W)
    (ha : ∀ h, D7Classification.complexMatrices (a h) = LinearMap.toMatrix u u (ρ (φ h)))
    (hb : ∀ h, D7Classification.complexMatrices (b h) = LinearMap.toMatrix w w (τ (φ h)))
    (hspan : ∀ g, (ρ g, τ g) ∈ Submodule.span ℂ (Set.range fun h => (ρ (φ h), τ (φ h)))) :
    Module.finrank ℝ (D7Classification.RealIntertwiners a b) =
      Module.finrank ℂ (ρ.IntertwiningMap τ) := by
  apply real_dimension_of_comparison a b
  have e := (restrictGroupEquiv φ ρ τ hspan).trans (intertwinerMatrices u w (ρ.comp φ) (τ.comp φ))
  have ha' : D7Classification.complexMatrices ∘ a = fun h => LinearMap.toMatrix u u ((ρ.comp φ) h) :=
    funext ha
  have hb' : D7Classification.complexMatrices ∘ b = fun h => LinearMap.toMatrix w w ((τ.comp φ) h) :=
    funext hb
  change ↥(D7Classification.matrixIntertwiners (D7Classification.complexMatrices ∘ a)
    (D7Classification.complexMatrices ∘ b)) ≃ₗ[ℂ] ρ.IntertwiningMap τ
  rw [ha', hb']
  exact e.symm

end RealAction

end
end GeometricUnity.D7Final
~~~

[Return to file index](#file-index)

## D7BianchiFields.lean {#source-d7bianchifields-lean}

Matches the complex tensor symbols to coordinate first jets and proves the closed-field criterion in every grade.

~~~lean
import D7Final
import BianchiSymbol
import Mathlib.LinearAlgebra.TensorProduct.Basis

/-!
# Coordinate first jets for the D₇ divergence symbol

The real coordinate labels refer to the split frame. Its raised covectors
are represented by the vectors of `axisBasis`. The coordinate array is
skew in the last two slots; the inverse tensor conversion sums over both
orders of those slots and therefore uses a factor of one half.
-/

namespace GeometricUnity.D7BianchiFields

open D7Exterior D7Hodge D7VectorGrades D7VectorTensor
open scoped BigOperators TensorProduct

noncomputable section

set_option backward.isDefEq.respectTransparency false

private def pairCoordinate (b c : Axis) : Two →ₗ[ℂ] ℂ :=
  exteriorPower.pairingDual ℂ Space 2
    (exteriorPower.ιMulti ℂ 2 ![axisBasis.coord b, axisBasis.coord c])

private theorem pairCoordinate_wedge (b c : Axis) (y z : Space) :
    pairCoordinate b c (wedgeTwo y z) =
      axisBasis.coord b y * axisBasis.coord c z - axisBasis.coord c y * axisBasis.coord b z := by
  simp [pairCoordinate, wedgeTwo, exteriorPower.pairingDual_ιMulti_ιMulti, Matrix.det_fin_two]

private theorem two_ext {f g : Two →ₗ[ℂ] ℂ}
    (h : ∀ x y, f (wedgeTwo x y) = g (wedgeTwo x y)) : f = g := by
  apply exteriorPower.linearMap_ext
  apply AlternatingMap.ext
  intro v
  have hv : (![v 0, v 1] : Fin 2 → Space) = v := by funext i; fin_cases i <;> rfl
  simpa only [LinearMap.compAlternatingMap_apply, wedgeTwo, hv] using h (v 0) (v 1)

private theorem pairCoordinate_swap (b c : Axis) :
    pairCoordinate c b = -pairCoordinate b c := by
  apply two_ext
  intro x y
  simp only [LinearMap.neg_apply, pairCoordinate_wedge]
  ring

private def tripleCoordinate (a b c : Axis) : VTwo →ₗ[ℂ] ℂ :=
  TensorProduct.lift ((axisBasis.coord a).smulRight (pairCoordinate b c))

@[simp] private theorem tripleCoordinate_tmul (a b c : Axis) (x : Space) (u : Two) :
    tripleCoordinate a b c (x ⊗ₜ[ℂ] u) = axisBasis.coord a x * pairCoordinate b c u := rfl

private theorem tripleCoordinate_swap (a b c : Axis) :
    tripleCoordinate a c b = -tripleCoordinate a b c := by
  apply TensorProduct.ext'
  intro x u
  rw [tripleCoordinate_tmul, LinearMap.neg_apply, tripleCoordinate_tmul,
    pairCoordinate_swap b c, LinearMap.neg_apply, mul_neg]

private theorem tripleCoordinate_average (a b c : Axis) (s : VTwo) :
    tripleCoordinate a b c (includeThree (D7VectorTensor.alternation s)) =
      (3 : ℂ)⁻¹ * (tripleCoordinate a b c s + tripleCoordinate b c a s +
        tripleCoordinate c a b s) := by
  let f := (tripleCoordinate a b c).comp (includeThree.comp D7VectorTensor.alternation)
  let g := (3 : ℂ)⁻¹ • (tripleCoordinate a b c + tripleCoordinate b c a +
    tripleCoordinate c a b)
  have h : f = g := by
    apply TensorProduct.ext'
    intro x u
    let m := TensorProduct.mk ℂ Space Two x
    have hm : f.comp m = g.comp m := by
      apply two_ext
      intro y z
      simp only [f, g, m, LinearMap.comp_apply, TensorProduct.mk_apply, alternation_pure,
        includeThree_pure, cyclicTensor, map_smul, map_add, LinearMap.smul_apply,
        LinearMap.add_apply, tripleCoordinate_tmul, pairCoordinate_wedge, smul_eq_mul]
      ring
    exact DFunLike.congr_fun hm u
  exact DFunLike.congr_fun h s

section Coefficients

variable {E : Type} [AddCommGroup E] [Module ℂ E]

private def coordinateEntry (a b c : Axis) : (VTwo ⊗[ℂ] E) →ₗ[ℂ] E :=
  (TensorProduct.lid ℂ E).toLinearMap.comp ((tripleCoordinate a b c).rTensor E)

@[simp] private theorem coordinateEntry_tmul (a b c : Axis) (s : VTwo) (x : E) :
    coordinateEntry a b c (s ⊗ₜ[ℂ] x) = tripleCoordinate a b c s • x := by
  simp [coordinateEntry]

private theorem coordinateEntry_swap (a b c : Axis) :
    (coordinateEntry a c b : (VTwo ⊗[ℂ] E) →ₗ[ℂ] E) = -coordinateEntry a b c := by
  apply TensorProduct.ext'
  intro s x
  rw [coordinateEntry_tmul, LinearMap.neg_apply, coordinateEntry_tmul,
    tripleCoordinate_swap a b c, LinearMap.neg_apply, neg_smul]

variable [Module ℝ E] [IsScalarTower ℝ ℂ E]

/-- The coordinates of a tensor with the derivative slot first and the
skew two-form slots second and third. -/
def tensorJet : (VTwo ⊗[ℂ] E) →ₗ[ℝ] BianchiSymbol.Jet Axis E where
  toFun s := ⟨fun a b c => coordinateEntry a b c s, by
    intro a b c
    change coordinateEntry a c b s = -coordinateEntry a b c s
    rw [coordinateEntry_swap, LinearMap.neg_apply]⟩
  map_add' s t := by
    apply Subtype.ext
    funext a b c
    exact map_add (coordinateEntry a b c) s t
  map_smul' r s := by
    apply Subtype.ext
    funext a b c
    exact (coordinateEntry a b c).restrictScalars ℝ |>.map_smul r s

/-- Assemble the skew pair using all ordered coordinate pairs. -/
def assembleJet (J : BianchiSymbol.Jet Axis E) : VTwo ⊗[ℂ] E :=
  (2 : ℂ)⁻¹ • ∑ a : Axis, ∑ b : Axis, ∑ c : Axis,
    (axisBasis a ⊗ₜ[ℂ] wedgeTwo (axisBasis b) (axisBasis c)) ⊗ₜ[ℂ] J.val a b c

private theorem axisCoordinate_basis (i j : Axis) :
    axisBasis.coord i (axisBasis j) = if i = j then 1 else 0 := by
  simp [Module.Basis.coord_apply, Finsupp.single_apply, eq_comm]

private theorem tensorJet_assemble (J : BianchiSymbol.Jet Axis E) :
    tensorJet (assembleJet J) = J := by
  apply Subtype.ext
  funext i j k
  change coordinateEntry i j k (assembleJet J) = J.val i j k
  simp only [assembleJet, map_smul, map_sum, coordinateEntry_tmul, tripleCoordinate_tmul,
    pairCoordinate_wedge, axisCoordinate_basis]
  have h (a b c : Axis) :
      ((if i = a then (1 : ℂ) else 0) *
        ((if j = b then 1 else 0) * (if k = c then 1 else 0) -
          (if k = b then 1 else 0) * (if j = c then 1 else 0))) • J.val a b c =
      (if k = c then if j = b then if i = a then J.val a b c else 0 else 0 else 0) -
      (if j = c then if k = b then if i = a then J.val a b c else 0 else 0 else 0) := by
    split_ifs <;> simp
  simp_rw [h, Finset.sum_sub_distrib]
  simp only [Finset.sum_ite_eq, Finset.mem_univ, if_true]
  rw [J.prop i j k]
  module

private def tensorBasis : Module.Basis (Axis × Index 2) ℂ VTwo :=
  axisBasis.tensorProduct (axisBasis.exteriorPower 2)

private theorem pairCoordinate_basis (s : Index 2) :
    let e := s.val.orderIsoOfFin s.prop
    pairCoordinate (e 0).val (e 1).val = (axisBasis.exteriorPower 2).coord s := by
  let e := s.val.orderIsoOfFin s.prop
  have he : (![axisBasis.coord (e 0).val, axisBasis.coord (e 1).val] : Fin 2 → _) =
      fun j => axisBasis.coord (e j).val := by
    funext j
    fin_cases j <;> rfl
  change pairCoordinate (e 0).val (e 1).val = _
  rw [pairCoordinate, he]
  exact (exteriorPower.basis_coord ℂ 2 axisBasis s).symm

private theorem tripleCoordinate_basis (a : Axis) (s : Index 2) :
    let e := s.val.orderIsoOfFin s.prop
    tripleCoordinate a (e 0).val (e 1).val = tensorBasis.coord (a, s) := by
  apply TensorProduct.ext'
  intro x u
  rw [tripleCoordinate_tmul, pairCoordinate_basis]
  simp only [Module.Basis.coord_apply, tensorBasis, Module.Basis.tensorProduct_repr_tmul_apply,
    smul_eq_mul]
  exact mul_comm _ _

private theorem tensorJet_injective :
    Function.Injective (tensorJet : (VTwo ⊗[ℂ] E) →ₗ[ℝ] BianchiSymbol.Jet Axis E) := by
  intro s t h
  apply (TensorProduct.equivFinsuppOfBasisLeft tensorBasis).injective
  ext ⟨a, ij⟩
  let e := ij.val.orderIsoOfFin ij.prop
  have hentry : coordinateEntry a (e 0).val (e 1).val s =
      coordinateEntry a (e 0).val (e 1).val t :=
    congrArg (fun J : BianchiSymbol.Jet Axis E => J.val a (e 0).val (e 1).val) h
  have hcoord : tripleCoordinate a (e 0).val (e 1).val = tensorBasis.coord (a, ij) :=
    tripleCoordinate_basis a ij
  simpa only [TensorProduct.equivFinsuppOfBasisLeft_apply, coordinateEntry, LinearMap.comp_apply,
    LinearEquiv.coe_coe, hcoord] using hentry

/-- Tensor and skew-array descriptions of a first jet. -/
def jetEquiv : (VTwo ⊗[ℂ] E) ≃ₗ[ℝ] BianchiSymbol.Jet Axis E where
  __ := tensorJet
  invFun := assembleJet
  left_inv s := tensorJet_injective (tensorJet_assemble (tensorJet s))
  right_inv := tensorJet_assemble

private theorem coordinateEntry_average (a b c : Axis) (s : VTwo ⊗[ℂ] E) :
    coordinateEntry a b c (includeThree.rTensor E (D7VectorTensor.alternation.rTensor E s)) =
      (3 : ℂ)⁻¹ • BianchiSymbol.cyclicSum (tensorJet s).val a b c := by
  let p := (includeThree.rTensor E).comp (D7VectorTensor.alternation.rTensor E)
  have h : (coordinateEntry a b c).comp p =
      (3 : ℂ)⁻¹ • ((coordinateEntry a b c) + coordinateEntry b c a + coordinateEntry c a b) := by
    apply TensorProduct.ext'
    intro t x
    simp only [p, LinearMap.comp_apply, LinearMap.rTensor_tmul, coordinateEntry_tmul,
      LinearMap.smul_apply, LinearMap.add_apply, tripleCoordinate_average, mul_smul, add_smul]
  exact DFunLike.congr_fun h s

/-- The cyclic mean in the coordinate model is the projection obtained
by exterior alternation followed by the normalized three-form inclusion. -/
theorem cyclic_average_eq_projection (s : VTwo ⊗[ℂ] E) (a b c : Axis) :
    (BianchiSymbol.alternation (tensorJet s)).val.val a b c =
      (tensorJet (includeThree.rTensor E (D7VectorTensor.alternation.rTensor E s))).val a b c := by
  rw [BianchiSymbol.alternation_apply]
  change _ = coordinateEntry a b c (includeThree.rTensor E (D7VectorTensor.alternation.rTensor E s))
  rw [coordinateEntry_average, ← algebraMap_smul ℂ (1 / 3 : ℝ)]
  congr 1
  norm_num

/-- The coordinate closed-jet condition is exactly the kernel of wedge
alternation on the derivative and form slots. -/
theorem closed_tensorJet_iff (s : VTwo ⊗[ℂ] E) :
    BianchiSymbol.ClosedJet (tensorJet s) ↔ D7VectorTensor.alternation.rTensor E s = 0 := by
  have hsection : (D7VectorTensor.alternation.rTensor E).comp (includeThree.rTensor E) =
      LinearMap.id := by
    apply TensorProduct.ext'
    intro u x
    simp only [LinearMap.comp_apply, LinearMap.rTensor_tmul, alternation_three, LinearMap.id_apply]
  rw [BianchiSymbol.closed_iff_alternation_eq_zero]
  constructor
  · intro h
    have hj : tensorJet (includeThree.rTensor E (D7VectorTensor.alternation.rTensor E s)) = 0 := by
      apply Subtype.ext
      funext a b c
      rw [← cyclic_average_eq_projection, h]
      rfl
    have hz := tensorJet_injective (hj.trans (map_zero tensorJet).symm)
    have hp := DFunLike.congr_fun hsection (D7VectorTensor.alternation.rTensor E s)
    change D7VectorTensor.alternation.rTensor E
        (includeThree.rTensor E (D7VectorTensor.alternation.rTensor E s)) = _ at hp
    rw [hz, map_zero] at hp
    exact hp.symm
  · intro h
    apply Subtype.ext
    apply Subtype.ext
    funext a b c
    rw [cyclic_average_eq_projection, h, map_zero, map_zero]
    rfl

end Coefficients

open D7Final
open D7Unrestricted (Intertwiners)
open D7TripleInvariants (metricEquiv metricEquiv_toLinearMap)

/-- Exterior blade coefficients in the split coordinate frame. -/
abbrev Coefficients (k : ℕ) := Index k → ℂ

def coefficientEquiv (k : ℕ) : Ext k ≃ₗ[ℂ] Coefficients k :=
  (axisBasis.exteriorPower k).equivFun

private def divergenceWithSymbol {S : Type} [AddCommMonoid S] [Module ℂ S] {k l : ℕ}
    (F : SymbolForm S k l) : S ⊗[ℂ] Coefficients k →ₗ[ℂ] Coefficients l :=
  ((metricEquiv l).symm.trans (coefficientEquiv l)).toLinearMap.comp
    ((TensorProduct.lift F).comp
      (TensorProduct.map LinearMap.id (coefficientEquiv k).symm.toLinearMap))

private theorem divergenceWithSymbol_tmul {S : Type} [AddCommMonoid S] [Module ℂ S] {k l : ℕ}
    (F : SymbolForm S k l) (s : S) (x : Coefficients k) :
    divergenceWithSymbol F (s ⊗ₜ[ℂ] x) =
      ((metricEquiv l).symm.trans (coefficientEquiv l)) (F s ((coefficientEquiv k).symm x)) := rfl

/-- The coordinate divergence of a block, expressed as a linear map of
first jets. The vector output index is paired with the raised derivative
index and the exterior output index is raised with its determinant metric. -/
def coordinateDivergence {k l : ℕ} (T : Intertwiners k l) :
    BianchiSymbol.Jet Axis (Coefficients k) →ₗ[ℝ] Coefficients l :=
  ((divergenceWithSymbol (divergenceSymbol k l T).val).restrictScalars ℝ).comp
    jetEquiv.symm.toLinearMap

private theorem coordinateDivergence_tensorJet {k l : ℕ} (T : Intertwiners k l)
    (s : VTwo ⊗[ℂ] Coefficients k) :
    coordinateDivergence T (tensorJet s) = divergenceWithSymbol (divergenceSymbol k l T).val s := by
  unfold coordinateDivergence
  change divergenceWithSymbol (divergenceSymbol k l T).val (jetEquiv.symm (jetEquiv s)) = _
  rw [LinearEquiv.symm_apply_apply]

theorem coordinateDivergence_pure_pair {k l : ℕ} (T : Intertwiners k l)
    (a : Space) (u : Ext 2) (x : Coefficients k) (y : Ext l) :
    exteriorMetric l ((coefficientEquiv l).symm
      (coordinateDivergence T (tensorJet ((a ⊗ₜ[ℂ] u) ⊗ₜ[ℂ] x)))) y =
      D7Unrestricted.tensorMetric l (T (u ⊗ₜ[ℂ] (coefficientEquiv k).symm x))
        (a ⊗ₜ[ℂ] y) := by
  rw [coordinateDivergence_tensorJet, ← metricEquiv_toLinearMap]
  simp only [divergenceWithSymbol_tmul, LinearEquiv.coe_coe, LinearEquiv.trans_apply,
    LinearEquiv.symm_apply_apply, LinearEquiv.apply_symm_apply, divergenceSymbol_tmul]

theorem mem_bianchiIntertwiners_iff_compatible {k l : ℕ} (T : Intertwiners k l) :
    T ∈ bianchiIntertwiners k l ↔ BianchiSymbol.Compatible (coordinateDivergence T) := by
  let F := divergenceSymbol k l T
  change F ∈ bianchiSymbols k l ↔ _
  constructor
  · intro h J hJ
    obtain ⟨A, hA, _⟩ := (bianchi_iff_factor F).mp h
    obtain ⟨s, rfl⟩ := jetEquiv.surjective J
    change BianchiSymbol.ClosedJet (tensorJet s) at hJ
    change coordinateDivergence T (tensorJet s) = 0
    have hF : divergenceWithSymbol F.val =
        (divergenceWithSymbol A.val).comp (D7VectorTensor.alternation.rTensor (Coefficients k)) := by
      rw [← hA]
      apply TensorProduct.ext'
      intro t x
      rfl
    rw [coordinateDivergence_tensorJet]
    change divergenceWithSymbol F.val s = 0
    rw [hF, LinearMap.comp_apply, (closed_tensorJet_iff s).mp hJ, map_zero]
  · intro h s hs
    apply LinearMap.ext
    intro x
    let t := s ⊗ₜ[ℂ] (coefficientEquiv k x)
    have ht : D7VectorTensor.alternation.rTensor (Coefficients k) t = 0 := by
      simp only [t, LinearMap.rTensor_tmul, hs, TensorProduct.zero_tmul]
    have hz := h (tensorJet t) ((closed_tensorJet_iff t).mpr ht)
    change coordinateDivergence T (tensorJet t) = 0 at hz
    rw [coordinateDivergence_tensorJet, divergenceWithSymbol_tmul,
      LinearEquiv.symm_apply_apply] at hz
    apply ((metricEquiv l).symm.trans (coefficientEquiv l)).injective
    rw [LinearMap.zero_apply, map_zero]
    exact hz

/-- Vanishing of the block divergence on all coordinatewise differentiable
closed two-forms with degree-`k` coefficients. -/
def VanishesOnClosedFields {k l : ℕ} (T : Intertwiners k l) : Prop :=
  ∀ (F : (Axis → ℝ) → Axis → Axis → Coefficients k)
    (hF : ∀ x b c, F x c b = -F x b c),
    (∀ x a b c, DifferentiableAt ℝ (fun t : ℝ => F (x + t • Pi.single a 1) b c) 0) →
    BianchiSymbol.ClosedField F →
    ∀ x, coordinateDivergence T (BianchiSymbol.firstJet F hF x) = 0

theorem mem_bianchiIntertwiners_iff_closed_fields {k l : ℕ} (T : Intertwiners k l) :
    T ∈ bianchiIntertwiners k l ↔ VanishesOnClosedFields T :=
  (mem_bianchiIntertwiners_iff_compatible T).trans
    (BianchiSymbol.compatible_iff_closed_fields (coordinateDivergence T))

section Bundled

open CategoryTheory

/-- The bundled Bianchi subspace is exactly the space of operators whose
divergences vanish on the closed-coordinate-field test in every block. -/
theorem mem_bianchiHom_iff_each_block
    (T : D7TripleMultiplicity.summedSource 2 ⟶ D7Unrestricted.summedVectorTarget) :
    T ∈ bianchiHom ↔ ∀ k l : Fin 15, VanishesOnClosedFields (unrestrictedBlocks T k l) := by
  rw [mem_bianchiHom]
  exact forall_congr' fun k => forall_congr' fun l =>
    mem_bianchiIntertwiners_iff_closed_fields _

private abbrev Field (k : Fin 15) := (Axis → ℝ) → Axis → Axis → Coefficients k.val

private theorem zeroField_closed (k : Fin 15) : BianchiSymbol.ClosedField (0 : Field k) := by
  intro x a b c
  simp [BianchiSymbol.cyclicSum, BianchiSymbol.coordinateDerivative]

private theorem zeroField_firstJet (k : Fin 15)
    (h : ∀ x b c, (0 : Field k) x c b = -(0 : Field k) x b c) (x : Axis → ℝ) :
    BianchiSymbol.firstJet (0 : Field k) h x = 0 := by
  apply Subtype.ext
  funext a b c
  simp [BianchiSymbol.firstJet, BianchiSymbol.coordinateDerivative]

/-- A full field is given by its exterior coefficient grades. Each output
grade of its divergence sums the contributions from all input grades. -/
def FullDivergenceVanishes
    (T : D7TripleMultiplicity.summedSource 2 ⟶ D7Unrestricted.summedVectorTarget) : Prop :=
  ∀ (F : ∀ k : Fin 15, Field k) (hF : ∀ k x b c, F k x c b = -F k x b c),
    (∀ k x a b c, DifferentiableAt ℝ (fun t : ℝ => F k (x + t • Pi.single a 1) b c) 0) →
    (∀ k, BianchiSymbol.ClosedField (F k)) →
    ∀ x l, (∑ k : Fin 15, coordinateDivergence (unrestrictedBlocks T k l)
      (BianchiSymbol.firstJet (F k) (hF k) x)) = 0

/-- Vanishing on all closed fields with arbitrary exterior-grade
coefficients is precisely membership in the bundled Bianchi subspace. -/
theorem mem_bianchiHom_iff_closed_fields
    (T : D7TripleMultiplicity.summedSource 2 ⟶ D7Unrestricted.summedVectorTarget) :
    T ∈ bianchiHom ↔ FullDivergenceVanishes T := by
  rw [mem_bianchiHom_iff_each_block]
  constructor
  · intro h F hF hd hc x l
    exact Finset.sum_eq_zero fun k _ => h k l (F k) (hF k) (hd k) (hc k) x
  · intro h k l F hF hd hc x
    let G : ∀ j : Fin 15, Field j := Function.update 0 k F
    have hG : ∀ j y b c, G j y c b = -G j y b c := by
      intro j y b c
      by_cases hj : j = k
      · subst j
        simpa only [G, Function.update_self] using hF y b c
      · simp [G, Function.update_of_ne hj]
    have hdiff : ∀ j y a b c,
        DifferentiableAt ℝ (fun t : ℝ => G j (y + t • Pi.single a 1) b c) 0 := by
      intro j y a b c
      by_cases hj : j = k
      · subst j
        simpa only [G, Function.update_self] using hd y a b c
      · simp [G, Function.update_of_ne hj]
    have hclosed : ∀ j, BianchiSymbol.ClosedField (G j) := by
      intro j
      by_cases hj : j = k
      · subst j
        simpa only [G, Function.update_self] using hc
      · simpa only [G, Function.update_of_ne hj, Pi.zero_apply] using zeroField_closed j
    have hz := h G hG hdiff hclosed x l
    rw [Finset.sum_eq_single k] at hz
    · simpa only [G, Function.update_self] using hz
    · intro j _ hj
      have hzero : G j = 0 := by simp [G, Function.update_of_ne hj]
      simp only [hzero, zeroField_firstJet, map_zero]
    · simp

end Bundled

end

end GeometricUnity.D7BianchiFields
~~~

[Return to file index](#file-index)

## D7UnitaryRealForm.lean {#source-d7unitaryrealform-lean}

Models skew-adjoint coefficient matrices as a real form and identifies their complexification.

~~~lean
import D7Classification
import Mathlib.LinearAlgebra.Matrix.ConjTranspose
import Mathlib.LinearAlgebra.TensorProduct.Tower

/-!
# The real coefficient space inside the complex matrix algebra

The real form is fixed by the negative adjoint for a Hermitian signature
matrix. Its scalar extension is the full complex matrix module. This
identification respects conjugation by units preserving the signature.
-/

namespace GeometricUnity.D7UnitaryRealForm

open D7Classification (Fixed mem_fixed finrank_fixed_of_conjugation)
open scoped Matrix TensorProduct

noncomputable section

variable {n : Type} [Fintype n]

/-- Conjugation for the skew-adjoint real form. -/
def realConjugation (J : Matrix n n ℂ) : Matrix n n ℂ →ₗ[ℝ] Matrix n n ℂ where
  toFun X := -(J * Xᴴ * J)
  map_add' X Y := by
    simp only [Matrix.conjTranspose_add, Matrix.mul_add, Matrix.add_mul, neg_add]
  map_smul' r X := by
    simp only [Matrix.conjTranspose_smul, star_trivial, Matrix.mul_smul, Matrix.smul_mul, smul_neg,
      RingHom.id_apply]

theorem realConjugation_apply (J X : Matrix n n ℂ) :
    realConjugation J X = -(J * Xᴴ * J) := rfl

/-- The real vector space of matrices skew-adjoint for the form with
signature matrix `J`. -/
def skewAdjoint (J : Matrix n n ℂ) : Submodule ℝ (Matrix n n ℂ) :=
  Fixed (realConjugation J)

theorem mem_skewAdjoint (J X : Matrix n n ℂ) :
    X ∈ skewAdjoint J ↔ X = -(J * Xᴴ * J) :=
  (mem_fixed (realConjugation J) X).trans eq_comm

private theorem realConjugation_anti (J : Matrix n n ℂ) (X : Matrix n n ℂ) :
    realConjugation J (Complex.I • X) = -(Complex.I • realConjugation J X) := by
  simp only [realConjugation_apply, Matrix.conjTranspose_smul, Complex.star_def, Complex.conj_I,
    Matrix.mul_neg, Matrix.neg_mul, Matrix.mul_smul, Matrix.smul_mul, neg_smul, neg_neg, smul_neg]

private theorem realConjugation_involutive [DecidableEq n] {J : Matrix n n ℂ}
    (hJ : Jᴴ = J) (hJJ : J * J = 1) : Function.Involutive (realConjugation J) := by
  intro X
  simp only [realConjugation_apply, Matrix.conjTranspose_neg, Matrix.conjTranspose_mul, hJ,
    Matrix.conjTranspose_conjTranspose, Matrix.mul_neg, Matrix.neg_mul, neg_neg]
  calc
    J * (J * (X * J)) * J = (J * J) * X * (J * J) := by simp only [Matrix.mul_assoc]
    _ = X := by rw [hJJ, Matrix.one_mul, Matrix.mul_one]

private def extendScalars (J : Matrix n n ℂ) :
    ℂ ⊗[ℝ] ↥(skewAdjoint J) →ₗ[ℂ] Matrix n n ℂ :=
  TensorProduct.AlgebraTensorModule.lift {
    toFun c := c • (skewAdjoint J).subtype
    map_add' c d := add_smul c d _
    map_smul' c d := smul_assoc c d _ }

@[simp] private theorem extendScalars_tmul (J : Matrix n n ℂ) (c : ℂ) (X : skewAdjoint J) :
    extendScalars J (c ⊗ₜ[ℝ] X) = c • X.val := rfl

variable [DecidableEq n]

private theorem extendScalars_surjective {J : Matrix n n ℂ}
    (hJ : Jᴴ = J) (hJJ : J * J = 1) : Function.Surjective (extendScalars J) := by
  let s := realConjugation J
  have hinv := realConjugation_involutive hJ hJJ
  intro X
  let A : skewAdjoint J := ⟨(1 / 2 : ℝ) • (X + s X), (mem_fixed s _).mpr (by
    rw [map_smul, map_add, hinv X, add_comm (s X) X])⟩
  let B : skewAdjoint J := ⟨(1 / 2 : ℝ) • (-(Complex.I • X) + Complex.I • s X),
    (mem_fixed s _).mpr (by
      rw [map_smul, map_add, map_neg, realConjugation_anti, realConjugation_anti, hinv X,
        neg_neg, add_comm])⟩
  refine ⟨(1 : ℂ) ⊗ₜ[ℝ] A + Complex.I ⊗ₜ[ℝ] B, ?_⟩
  rw [map_add, extendScalars_tmul, extendScalars_tmul, one_smul]
  change (1 / 2 : ℝ) • (X + s X) +
    Complex.I • ((1 / 2 : ℝ) • (-(Complex.I • X) + Complex.I • s X)) = X
  rw [smul_comm Complex.I (1 / 2 : ℝ)]
  simp only [smul_add, smul_neg, smul_smul, Complex.I_mul_I, neg_one_smul, neg_neg]
  module

/-- Scalar extension identifies the real coefficient space with the
whole complex matrix module. -/
def complexificationEquiv {J : Matrix n n ℂ} (hJ : Jᴴ = J) (hJJ : J * J = 1) :
    ℂ ⊗[ℝ] ↥(skewAdjoint J) ≃ₗ[ℂ] Matrix n n ℂ := by
  have h := finrank_fixed_of_conjugation (realConjugation J)
    (realConjugation_involutive hJ hJJ) (realConjugation_anti J)
  have hd : Module.finrank ℂ (ℂ ⊗[ℝ] ↥(skewAdjoint J)) =
      Module.finrank ℂ (Matrix n n ℂ) := Module.finrank_baseChange.trans h
  have hs := extendScalars_surjective hJ hJJ
  exact LinearEquiv.ofBijective (extendScalars J)
    ⟨(LinearMap.injective_iff_surjective_of_finrank_eq_finrank hd).mpr hs, hs⟩

@[simp] theorem complexificationEquiv_tmul {J : Matrix n n ℂ}
    (hJ : Jᴴ = J) (hJJ : J * J = 1) (c : ℂ) (X : skewAdjoint J) :
    complexificationEquiv hJ hJJ (c ⊗ₜ[ℝ] X) = c • X.val := rfl

local notation "SpinIndex" => Fin 64 ⊕ Fin 64

/-- The diagonal presentation of the signature `(64,64)`. -/
def signature : Matrix SpinIndex SpinIndex ℂ :=
  Matrix.diagonal (Sum.elim (fun _ => 1) (fun _ => -1))

theorem signature_hermitian : signatureᴴ = signature := by
  rw [signature, Matrix.diagonal_conjTranspose]
  congr 1
  funext i
  cases i <;> simp

theorem signature_sq : signature * signature = 1 := by
  rw [signature, Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]
  congr 1
  funext i
  cases i <;> simp

/-- Conjugation on the complex coefficient matrices. -/
def matrixConjugation (U : (Matrix n n ℂ)ˣ) : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ :=
  LinearMap.mulLeftRight ℂ (↑U, ↑U⁻¹)

theorem realConjugation_commutes {J : Matrix n n ℂ}
    (hJJ : J * J = 1) (U : (Matrix n n ℂ)ˣ) (hU : (U : Matrix n n ℂ)ᴴ * J * U = J)
    (X : Matrix n n ℂ) :
    realConjugation J (matrixConjugation U X) = matrixConjugation U (realConjugation J X) := by
  let u : Matrix n n ℂ := U
  let v : Matrix n n ℂ := ↑U⁻¹
  have hu : u * v = 1 := U.mul_inv
  change uᴴ * J * u = J at hU
  have hright : uᴴ * J = J * v := by
    have h := congrArg (fun X : Matrix n n ℂ => X * v) hU
    simpa only [Matrix.mul_assoc, hu, Matrix.mul_one] using h
  have ht : vᴴ * uᴴ = 1 := by rw [← Matrix.conjTranspose_mul, hu, Matrix.conjTranspose_one]
  have hleft : J * vᴴ = u * J := by
    have h0 : J * u = vᴴ * J := by
      have h : vᴴ * (uᴴ * J * u) = vᴴ * J := congrArg (fun X => vᴴ * X) hU
      simpa only [← Matrix.mul_assoc, ht, Matrix.one_mul] using h
    calc
      J * vᴴ = J * (vᴴ * J) * J := by simp only [Matrix.mul_assoc, hJJ, Matrix.mul_one]
      _ = u * J := by rw [← h0, ← Matrix.mul_assoc J J u, hJJ, Matrix.one_mul]
  change -(J * (u * X * v)ᴴ * J) = u * (-(J * Xᴴ * J)) * v
  calc
    _ = -(J * vᴴ * Xᴴ * (uᴴ * J)) := by simp only [Matrix.conjTranspose_mul, Matrix.mul_assoc]
    _ = -(u * J * Xᴴ * (J * v)) := by rw [hleft, hright]
    _ = _ := by simp only [Matrix.mul_neg, Matrix.neg_mul, Matrix.mul_assoc]

/-- A unit preserving the signature acts on the skew-adjoint real form. -/
def realMatrixConjugation {J : Matrix n n ℂ} (hJJ : J * J = 1)
    (U : (Matrix n n ℂ)ˣ) (hU : (U : Matrix n n ℂ)ᴴ * J * U = J) :
    ↥(skewAdjoint J) →ₗ[ℝ] ↥(skewAdjoint J) :=
  (((matrixConjugation U).restrictScalars ℝ).comp (skewAdjoint J).subtype).codRestrict
    (skewAdjoint J) (fun X => (mem_fixed (realConjugation J) _).mpr (by
      change realConjugation J (matrixConjugation U X.val) = matrixConjugation U X.val
      rw [realConjugation_commutes hJJ U hU, (mem_fixed (realConjugation J) _).mp X.prop]))

/-- The matrix real-form identification intertwines conjugation after
scalar extension. -/
theorem complexification_intertwines {J : Matrix n n ℂ} (hJ : Jᴴ = J) (hJJ : J * J = 1)
    (U : (Matrix n n ℂ)ˣ) (hU : (U : Matrix n n ℂ)ᴴ * J * U = J) :
    (complexificationEquiv hJ hJJ).toLinearMap.comp ((realMatrixConjugation hJJ U hU).baseChange ℂ) =
      (matrixConjugation U).comp (complexificationEquiv hJ hJJ).toLinearMap := by
  apply TensorProduct.AlgebraTensorModule.ext
  intro a X
  simp only [LinearMap.comp_apply, LinearMap.baseChange_tmul, LinearEquiv.coe_coe,
    complexificationEquiv_tmul, map_smul]
  rfl

end

end GeometricUnity.D7UnitaryRealForm
~~~

[Return to file index](#file-index)

## D7SpinAction.lean {#source-d7spinaction-lean}

Defines the real Spin vector and Clifford conjugation actions and their exterior-algebra identification.

~~~lean
import WitnessW1
import Mathlib.LinearAlgebra.CliffordAlgebra.SpinGroup
import Mathlib.LinearAlgebra.ExteriorPower.Basic
import Mathlib.RepresentationTheory.Basic

/-!
# The real Spin action on the split quadratic space

Clifford conjugation gives a linear action on the embedded vectors.
The Clifford square relation proves that this action preserves the
quadratic form of signature `(7,7)`.
-/

namespace GeometricUnity.D7SpinAction

open WitnessW1 (Index splitForm Cl)

noncomputable section

abbrev Vector := Index → ℝ
abbrev Spin := ↥(spinGroup splitForm)

private abbrev iota := CliffordAlgebra.ι splitForm

theorem iota_injective : Function.Injective (CliffordAlgebra.ι splitForm) := by
  intro x y h
  have h' := congrArg (CliffordAlgebra.equivExterior splitForm) h
  apply (ExteriorAlgebra.ι_inj ℝ x y).mp
  simpa only [CliffordAlgebra.equivExterior, CliffordAlgebra.changeFormEquiv_apply,
    CliffordAlgebra.changeForm_ι] using h'

private abbrev units : Spin →* Clˣ := spinGroup.toUnits

private def vectorAction (g : Spin) : Vector →ₗ[ℝ] Vector :=
  (((LinearMap.mulLeftRight ℝ ((units g : Cl), (↑(units g)⁻¹ : Cl)) : Cl →ₗ[ℝ] Cl).comp
    iota).codRestrictOfInjective iota iota_injective (by
      intro x
      simpa only [LinearMap.comp_apply, LinearMap.mulLeftRight_apply, ConjAct.units_smul_def,
        ConjAct.ofConjAct_toConjAct] using
        spinGroup.conjAct_smul_ι_mem_range_ι (x := units g) g.prop x))

private theorem iota_vectorAction (g : Spin) (x : Vector) :
    iota (vectorAction g x) = (units g : Cl) * iota x * (↑(units g)⁻¹ : Cl) :=
  LinearMap.codRestrictOfInjective_comp_apply _ _ _ _ x

/-- The vector representation of the real Clifford Spin group. -/
def vectorRepresentation : Representation ℝ Spin Vector where
  toFun := vectorAction
  map_one' := by
    apply LinearMap.ext
    intro x
    apply iota_injective
    change iota (vectorAction 1 x) = iota x
    simp only [iota_vectorAction, map_one, inv_one, Units.val_one, one_mul, mul_one]
  map_mul' g h := by
    apply LinearMap.ext
    intro x
    apply iota_injective
    change iota (vectorAction (g * h) x) = iota (vectorAction g (vectorAction h x))
    simp only [iota_vectorAction, map_mul, Units.val_mul, mul_inv_rev, mul_assoc]

theorem iota_vectorRepresentation (g : Spin) (x : Vector) :
    iota (vectorRepresentation g x) = (units g : Cl) * iota x * (↑(units g)⁻¹ : Cl) :=
  iota_vectorAction g x

/-- The real Spin vector action is orthogonal for the split quadratic form. -/
theorem vectorRepresentation_preserves (g : Spin) (x : Vector) :
    splitForm (vectorRepresentation g x) = splitForm x := by
  apply (algebraMap ℝ Cl).injective
  rw [← CliffordAlgebra.ι_sq_scalar splitForm (vectorRepresentation g x),
    iota_vectorRepresentation]
  let u : Cl := units g
  let v : Cl := ↑(units g)⁻¹
  have h : v * u = 1 := (units g).inv_mul
  have h' : u * v = 1 := (units g).mul_inv
  change (u * iota x * v) * (u * iota x * v) = algebraMap ℝ Cl (splitForm x)
  calc
    _ = (u * iota x) * (v * u) * iota x * v := by simp only [mul_assoc]
    _ = u * (iota x * iota x) * v := by rw [h, mul_one, mul_assoc u (iota x) (iota x)]
    _ = _ := by rw [CliffordAlgebra.ι_sq_scalar, ← Algebra.commutes, mul_assoc, h', mul_one]

/-- Spin conjugation on the entire real Clifford algebra. -/
def cliffordConjugation (g : Spin) : Cl ≃ₐ[ℝ] Cl :=
  MulSemiringAction.toAlgEquiv ℝ Cl (ConjAct.toConjAct (units g))

private theorem cliffordConjugation_iota (g : Spin) (x : Vector) :
    cliffordConjugation g (iota x) = iota (vectorRepresentation g x) :=
  (iota_vectorRepresentation g x).symm

theorem associated_preserves (g : Spin) (x y : Vector) :
    splitForm.associated (vectorRepresentation g x) (vectorRepresentation g y) =
      splitForm.associated x y := by
  rw [QuadraticMap.associated_apply, QuadraticMap.associated_apply, ← map_add,
    vectorRepresentation_preserves, vectorRepresentation_preserves, vectorRepresentation_preserves]

private theorem exteriorMap_contract
    (v : Vector →ₗ[ℝ] Vector) (d : Module.Dual ℝ Vector) (x : ExteriorAlgebra ℝ Vector) :
    ExteriorAlgebra.map v (CliffordAlgebra.contractLeft (d.comp v) x) =
      CliffordAlgebra.contractLeft d (ExteriorAlgebra.map v x) := by
  induction x using CliffordAlgebra.left_induction with
  | algebraMap r =>
    simp only [CliffordAlgebra.contractLeft_algebraMap, map_zero, AlgHom.commutes]
  | add x y hx hy =>
    simp only [map_add, hx, hy]
  | ι_mul z a hz =>
    change ExteriorAlgebra.map v
        (CliffordAlgebra.contractLeft (d.comp v) (ExteriorAlgebra.ι ℝ a * z)) =
      CliffordAlgebra.contractLeft d (ExteriorAlgebra.map v (ExteriorAlgebra.ι ℝ a * z))
    simp only [map_mul, ExteriorAlgebra.map_apply_ι]
    rw [CliffordAlgebra.contractLeft_ι_mul, CliffordAlgebra.contractLeft_ι_mul]
    simp only [map_sub, map_smul, LinearMap.comp_apply, map_mul, ExteriorAlgebra.map_apply_ι, hz]

/-- The canonical Clifford-to-exterior linear equivalence intertwines
real Spin conjugation with the induced action on the exterior algebra. -/
theorem equivExterior_intertwines (g : Spin) (x : Cl) :
    CliffordAlgebra.equivExterior splitForm (cliffordConjugation g x) =
      ExteriorAlgebra.map (vectorRepresentation g) (CliffordAlgebra.equivExterior splitForm x) := by
  let q := splitForm
  let v := vectorRepresentation g
  let B := QuadraticMap.associated (-q)
  let hB : B.toQuadraticMap = 0 - q := CliffordAlgebra.changeForm.associated_neg_proof
  change CliffordAlgebra.changeForm hB (cliffordConjugation g x) =
    ExteriorAlgebra.map v (CliffordAlgebra.changeForm hB x)
  induction x using CliffordAlgebra.left_induction with
  | algebraMap r =>
    change CliffordAlgebra.changeForm hB
        (cliffordConjugation g (algebraMap ℝ (CliffordAlgebra q) r)) =
      ExteriorAlgebra.map v (CliffordAlgebra.changeForm hB (algebraMap ℝ (CliffordAlgebra q) r))
    have hr := CliffordAlgebra.changeForm_algebraMap hB r
    have hconj : cliffordConjugation g (algebraMap ℝ (CliffordAlgebra q) r) =
        algebraMap ℝ (CliffordAlgebra q) r := AlgEquiv.commutes _ _
    rw [hconj, hr]
    exact (AlgHom.commutes (ExteriorAlgebra.map v) r).symm
  | add x y hx hy =>
    simp only [map_add, hx, hy]
  | ι_mul z a hz =>
    rw [map_mul, cliffordConjugation_iota, CliffordAlgebra.changeForm_ι_mul,
      CliffordAlgebra.changeForm_ι_mul, map_sub, map_mul, hz]
    have he : (B (v a)).comp v = B a := by
      apply LinearMap.ext
      intro b
      change QuadraticMap.associated (-splitForm) (v a) (v b) =
        QuadraticMap.associated (-splitForm) a b
      simp only [map_neg, LinearMap.neg_apply, v, associated_preserves]
    have ha : ExteriorAlgebra.map v (CliffordAlgebra.ι (0 : QuadraticForm ℝ Vector) a) =
        CliffordAlgebra.ι 0 (v a) := ExteriorAlgebra.map_apply_ι v a
    rw [← he, exteriorMap_contract, ha]

/-- Under the Clifford-to-exterior equivalence, each grade transforms by
the corresponding exterior power of the vector representation. -/
theorem equivExterior_grade_action (g : Spin) {k : ℕ} (x : ⋀[ℝ]^k Vector) :
    CliffordAlgebra.equivExterior splitForm
        (cliffordConjugation g ((CliffordAlgebra.equivExterior splitForm).symm x.val)) =
      (exteriorPower.map k (vectorRepresentation g) x).val := by
  rw [equivExterior_intertwines, LinearEquiv.apply_symm_apply]
  let v := vectorRepresentation g
  have h :
      (ExteriorAlgebra.map v).toLinearMap.comp (Submodule.subtype (⋀[ℝ]^k Vector)) =
        (Submodule.subtype (⋀[ℝ]^k Vector)).comp (exteriorPower.map k v) := by
    apply exteriorPower.linearMap_ext
    apply AlternatingMap.ext
    intro m
    simp only [LinearMap.compAlternatingMap_apply, LinearMap.comp_apply, Submodule.subtype_apply,
      exteriorPower.map_apply_ιMulti, exteriorPower.ιMulti_apply_coe, AlgHom.toLinearMap_apply,
      ExteriorAlgebra.map_apply_ιMulti]
  exact DFunLike.congr_fun h x

end

end GeometricUnity.D7SpinAction
~~~

[Return to file index](#file-index)

## D7CliffordMatrix.lean {#source-d7cliffordmatrix-lean}

Constructs the split Clifford algebra as matrices on the 128-dimensional exterior spinor module.

~~~lean
import D7SpinAction
import Mathlib.Algebra.Ring.Action.ConjAct
import Mathlib.LinearAlgebra.Complex.Module
import Mathlib.LinearAlgebra.ExteriorAlgebra.Basis
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.LinearAlgebra.TensorProduct.Basis
import Mathlib.RingTheory.TensorProduct.Maps

/-!
# The split Clifford algebra on seven exterior generators

The spinor module is the real exterior algebra of a seven-dimensional
space. A split vector with positive and negative coordinates `p` and
`n` acts by creation with `p + n` and contraction by `p - n`.
-/

namespace GeometricUnity.D7CliffordMatrix

open WitnessW1 (Index Cl splitForm metricSign gamma)
open scoped BigOperators Matrix TensorProduct

noncomputable section

abbrev Half := Fin 7 → ℝ
abbrev Spinor := ExteriorAlgebra ℝ Half
abbrev SpinorIndex := Finset (Fin 7)
abbrev Mat := Matrix SpinorIndex SpinorIndex ℝ

def spinorBasis : Module.Basis SpinorIndex ℝ Spinor :=
  (Pi.basisFun ℝ (Fin 7)).ExteriorAlgebra

theorem spinor_finrank : Module.finrank ℝ Spinor = 128 := by
  rw [Module.finrank_eq_card_basis spinorBasis, Fintype.card_finset, Fintype.card_fin]
  rfl

private def positive : (Index → ℝ) →ₗ[ℝ] Half :=
  LinearMap.pi fun i => LinearMap.proj (Fin.castAdd 7 i)

private def negative : (Index → ℝ) →ₗ[ℝ] Half :=
  LinearMap.pi fun i => LinearMap.proj (Fin.natAdd 7 i)

/-- Left exterior multiplication by a vector on the spinor space. -/
def creation : Half →ₗ[ℝ] Module.End ℝ Spinor :=
  (Algebra.lmul ℝ Spinor).toLinearMap.comp (ExteriorAlgebra.ι ℝ)

/-- Contraction by a covector on the spinor space. -/
def contraction : Module.Dual ℝ Half →ₗ[ℝ] Module.End ℝ Spinor :=
  CliffordAlgebra.contractLeft (Q := (0 : QuadraticForm ℝ Half))

private def vectorOperator : (Index → ℝ) →ₗ[ℝ] Module.End ℝ Spinor :=
  creation.comp (positive + negative) +
    contraction.comp ((dotProductBilin ℝ ℝ).comp (positive - negative))

private theorem dot_creation_contraction (x : Index → ℝ) :
    dotProductBilin ℝ ℝ ((positive - negative) x) ((positive + negative) x) = splitForm x := by
  change (∑ i : Fin 7, (x (Fin.castAdd 7 i) - x (Fin.natAdd 7 i)) *
    (x (Fin.castAdd 7 i) + x (Fin.natAdd 7 i))) = _
  rw [splitForm, QuadraticMap.weightedSumSquares_apply,
    Fin.sum_univ_add (a := 7) (b := 7) (fun i => metricSign i • (x i * x i))]
  simp only [metricSign, Fin.val_castAdd, Fin.val_natAdd, Fin.isLt, if_true,
    show ∀ i : Fin 7, ¬ 7 + i.val < 7 from fun i => by omega, if_false, smul_eq_mul,
    one_mul, neg_one_mul, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro i _
  ring

private theorem creation_contraction_square (v : Half) (d : Module.Dual ℝ Half) (z : Spinor) :
    (creation v + contraction d) ((creation v + contraction d) z) = d v • z := by
  change ExteriorAlgebra.ι ℝ v * (ExteriorAlgebra.ι ℝ v * z + contraction d z) +
    contraction d (ExteriorAlgebra.ι ℝ v * z + contraction d z) = _
  have h : contraction d (ExteriorAlgebra.ι ℝ v * z) =
      d v • z - ExteriorAlgebra.ι ℝ v * contraction d z :=
    CliffordAlgebra.contractLeft_ι_mul (Q := (0 : QuadraticForm ℝ Half)) d v z
  have hzero : contraction d (contraction d z) = 0 :=
    CliffordAlgebra.contractLeft_contractLeft (Q := (0 : QuadraticForm ℝ Half)) d z
  rw [mul_add, ← mul_assoc (ExteriorAlgebra.ι ℝ v) (ExteriorAlgebra.ι ℝ v),
    ExteriorAlgebra.ι_sq_zero, zero_mul, zero_add, map_add, h, hzero, add_zero]
  abel

private theorem vectorOperator_square (x : Index → ℝ) :
    vectorOperator x * vectorOperator x = algebraMap ℝ (Module.End ℝ Spinor) (splitForm x) := by
  apply LinearMap.ext
  intro z
  change (creation ((positive + negative) x) + contraction
      (dotProductBilin ℝ ℝ ((positive - negative) x)))
      ((creation ((positive + negative) x) + contraction
        (dotProductBilin ℝ ℝ ((positive - negative) x))) z) = splitForm x • z
  rw [creation_contraction_square, dot_creation_contraction]

/-- Creation and contraction give the split real Clifford action. -/
def endRepresentation : Cl →ₐ[ℝ] Module.End ℝ Spinor :=
  CliffordAlgebra.lift splitForm ⟨vectorOperator, vectorOperator_square⟩

private theorem positive_basis (i : Fin 7) :
    positive (WitnessW1.basisVector (Fin.castAdd 7 i)) = Pi.basisFun ℝ (Fin 7) i := by
  funext j
  change WitnessW1.basisVector (Fin.castAdd 7 i) (Fin.castAdd 7 j) =
    Pi.basisFun ℝ (Fin 7) i j
  have h : Fin.castAdd 7 j = Fin.castAdd 7 i ↔ j = i := by simp [Fin.ext_iff]
  simp only [WitnessW1.basisVector, Pi.basisFun_apply, Pi.single_apply, h]

private theorem negative_basis (i : Fin 7) :
    negative (WitnessW1.basisVector (Fin.natAdd 7 i)) = Pi.basisFun ℝ (Fin 7) i := by
  funext j
  change WitnessW1.basisVector (Fin.natAdd 7 i) (Fin.natAdd 7 j) =
    Pi.basisFun ℝ (Fin 7) i j
  have h : Fin.natAdd 7 j = Fin.natAdd 7 i ↔ j = i := by simp [Fin.ext_iff]
  simp only [WitnessW1.basisVector, Pi.basisFun_apply, Pi.single_apply, h]

private theorem positive_wrongHalf (i : Fin 7) :
    positive (WitnessW1.basisVector (Fin.natAdd 7 i)) = 0 := by
  funext j
  have h : Fin.castAdd 7 j ≠ Fin.natAdd 7 i := by
    simp [Fin.ext_iff]
    omega
  change WitnessW1.basisVector (Fin.natAdd 7 i) (Fin.castAdd 7 j) = 0
  rw [WitnessW1.basisVector, Pi.single_apply, if_neg h]

private theorem negative_wrongHalf (i : Fin 7) :
    negative (WitnessW1.basisVector (Fin.castAdd 7 i)) = 0 := by
  funext j
  have h : Fin.natAdd 7 j ≠ Fin.castAdd 7 i := by
    simp [Fin.ext_iff]
    omega
  change WitnessW1.basisVector (Fin.castAdd 7 i) (Fin.natAdd 7 j) = 0
  rw [WitnessW1.basisVector, Pi.single_apply, if_neg h]

private theorem dotProduct_basis (i : Fin 7) :
    dotProductBilin ℝ ℝ (Pi.basisFun ℝ (Fin 7) i) = (Pi.basisFun ℝ (Fin 7)).coord i := by
  apply LinearMap.ext
  intro x
  simp [dotProductBilin, dotProduct, Pi.basisFun_apply, Pi.single_apply,
    Module.Basis.coord_apply, Pi.basisFun_repr, ite_mul]

theorem endRepresentation_gamma_pos (i : Fin 7) :
    endRepresentation (gamma (Fin.castAdd 7 i)) =
      creation (Pi.basisFun ℝ (Fin 7) i) + contraction ((Pi.basisFun ℝ (Fin 7)).coord i) := by
  rw [gamma, endRepresentation, CliffordAlgebra.lift_ι_apply]
  simp only [vectorOperator, LinearMap.comp_apply, LinearMap.add_apply, LinearMap.sub_apply,
    positive_basis, negative_wrongHalf, add_zero, sub_zero, dotProduct_basis]

theorem endRepresentation_gamma_neg (i : Fin 7) :
    endRepresentation (gamma (Fin.natAdd 7 i)) =
      creation (Pi.basisFun ℝ (Fin 7) i) - contraction ((Pi.basisFun ℝ (Fin 7)).coord i) := by
  rw [gamma, endRepresentation, CliffordAlgebra.lift_ι_apply]
  simp only [vectorOperator, LinearMap.comp_apply, LinearMap.add_apply, LinearMap.sub_apply,
    positive_wrongHalf, negative_basis, zero_add, zero_sub, map_neg, dotProduct_basis]
  rw [sub_eq_add_neg]

/-- The Clifford action in the exterior basis of the spinor space. -/
def matrixRepresentation : Cl →ₐ[ℝ] Mat :=
  (LinearMap.toMatrixAlgEquiv spinorBasis).toAlgHom.comp endRepresentation

theorem clifford_finrank : Module.finrank ℝ Cl = 16384 := by
  let b := (Pi.basisFun ℝ Index).ExteriorAlgebra
  rw [(CliffordAlgebra.equivExterior splitForm).finrank_eq, Module.finrank_eq_card_basis b,
    Fintype.card_finset, Fintype.card_fin]
  rfl

private theorem matrix_finrank : Module.finrank ℝ Mat = 16384 := by
  rw [Module.finrank_matrix, Module.finrank_self, Fintype.card_finset, Fintype.card_fin]
  rfl

private theorem generator_inverse (i : Index) :
    gamma i * (metricSign i • gamma i) = 1 := by
  rw [mul_smul_comm, WitnessW1.gamma_square, Algebra.smul_def, ← map_mul]
  have hs : metricSign i * metricSign i = 1 := by unfold metricSign; split <;> norm_num
  rw [hs, map_one]

private def generatorUnit (i : Index) : Clˣ where
  val := gamma i
  inv := metricSign i • gamma i
  val_inv := generator_inverse i
  inv_val := by rw [smul_mul_assoc, ← mul_smul_comm, generator_inverse]

private def matrixGenerator (i : Index) : Matˣ :=
  Units.map matrixRepresentation.toMonoidHom (generatorUnit i)

private def bladeUnit (S : Finset Index) : Matˣ := (S.toList.map matrixGenerator).prod

private def conjugation (u : Matˣ) : Mat ≃ₐ[ℝ] Mat :=
  MulSemiringAction.toAlgEquiv ℝ Mat (ConjAct.toConjAct u)

private theorem conjugation_apply (u : Matˣ) (X : Mat) :
    conjugation u X = (u : Mat) * X * (↑u⁻¹ : Mat) := by
  change ConjAct.toConjAct u • X = _
  rw [ConjAct.units_smul_def, ConjAct.ofConjAct_toConjAct]

private def generatorSign (i j : Index) : ℝ := if i = j then 1 else -1

private theorem conjugation_generator (i j : Index) :
    conjugation (matrixGenerator i) (matrixGenerator j : Mat) =
      generatorSign i j • (matrixGenerator j : Mat) := by
  by_cases h : i = j
  · subst j
    rw [conjugation_apply, generatorSign, if_pos rfl, one_smul, mul_assoc,
      (matrixGenerator i).mul_inv, mul_one]
  · have hswap : (matrixGenerator i : Mat) * (matrixGenerator j : Mat) =
        -((matrixGenerator j : Mat) * (matrixGenerator i : Mat)) := by
      change matrixRepresentation (gamma i) * matrixRepresentation (gamma j) =
        -(matrixRepresentation (gamma j) * matrixRepresentation (gamma i))
      rw [← map_mul, WitnessW1.gamma_anticommute i j h, map_neg, map_mul]
    rw [conjugation_apply, generatorSign, if_neg h, hswap, neg_mul, mul_assoc,
      (matrixGenerator i).mul_inv, mul_one, neg_one_smul]

private def character (i : Index) (S : Finset Index) : ℝ :=
  ∏ j ∈ S, generatorSign i j

private theorem conjugation_blade (i : Index) (S : Finset Index) :
    conjugation (matrixGenerator i) (bladeUnit S : Mat) = character i S • (bladeUnit S : Mat) := by
  have h (L : List Index) : conjugation (matrixGenerator i) (↑(L.map matrixGenerator).prod : Mat) =
      (L.map (generatorSign i)).prod • (↑(L.map matrixGenerator).prod : Mat) := by
    induction L with
    | nil => simp
    | cons j L ih =>
      simp only [List.map_cons, List.prod_cons, Units.val_mul, map_mul, conjugation_generator,
        ih, Matrix.smul_mul, Matrix.mul_smul, smul_smul]
      rw [mul_comm]
  exact (h S.toList).trans (by rw [Finset.prod_map_toList]; rfl)

private def membershipSign (i : Index) (S : Finset Index) : ℝ :=
  if i ∈ S then -1 else 1

private theorem character_formula (i : Index) (S : Finset Index) :
    character i S = (-1 : ℝ) ^ S.card * membershipSign i S := by
  induction S using Finset.induction_on with
  | empty => simp [character, membershipSign]
  | insert j S hj ih =>
    rw [show character i (insert j S) = generatorSign i j * character i S from
      Finset.prod_insert hj, ih, Finset.card_insert_of_notMem hj, pow_succ]
    by_cases hij : i = j
    · subst j
      simp [generatorSign, membershipSign, hj]
    · simp [generatorSign, membershipSign, hij]

private theorem generatorSign_total (j : Index) : (∏ i : Index, generatorSign i j) = -1 := by
  calc
    _ = (∏ i ∈ Finset.univ.erase j, generatorSign i j) * generatorSign j j :=
      (Finset.prod_erase_mul Finset.univ (fun i => generatorSign i j) (Finset.mem_univ j)).symm
    _ = (∏ i ∈ Finset.univ.erase j, (-1 : ℝ)) * 1 := by
      congr 1
      · exact Finset.prod_congr rfl fun i hi => if_neg (Finset.ne_of_mem_erase hi)
      · exact if_pos rfl
    _ = -1 := by
      rw [mul_one, Finset.prod_const, Finset.card_erase_of_mem (Finset.mem_univ j),
        Finset.card_univ, Fintype.card_fin]
      norm_num

private theorem character_total (S : Finset Index) :
    (∏ i : Index, character i S) = (-1 : ℝ) ^ S.card := by
  unfold character
  rw [Finset.prod_comm, Finset.prod_congr rfl (fun j _ => generatorSign_total j), Finset.prod_const]

private theorem character_injective : Function.Injective (fun S : Finset Index => fun i =>
    character i S) := by
  intro S T h
  have hpar : (-1 : ℝ) ^ S.card = (-1 : ℝ) ^ T.card :=
    (character_total S).symm.trans
      ((congrArg (fun f : Index → ℝ => ∏ i, f i) h).trans (character_total T))
  ext i
  have hi := congrFun h i
  change character i S = character i T at hi
  rw [character_formula, character_formula, hpar] at hi
  have hs : membershipSign i S = membershipSign i T :=
    mul_left_cancel₀ (pow_ne_zero _ (by norm_num)) hi
  by_cases hsS : i ∈ S <;> by_cases hsT : i ∈ T <;> simp [hsS, hsT]
  all_goals norm_num [membershipSign, hsS, hsT] at hs

private theorem trace_conjugation (u : Matˣ) (X : Mat) :
    Matrix.trace (conjugation u X) = Matrix.trace X := by
  rw [conjugation_apply, Matrix.trace_mul_comm _ (↑u⁻¹ : Mat), ← mul_assoc, u.inv_mul, one_mul]

private def tracePair (S : Finset Index) : Mat →ₗ[ℝ] ℝ :=
  (Matrix.traceLinearMap SpinorIndex ℝ ℝ).comp (LinearMap.mulLeft ℝ (↑(bladeUnit S)⁻¹ : Mat))

private theorem tracePair_self (S : Finset Index) : tracePair S (bladeUnit S : Mat) = 128 := by
  change Matrix.trace ((↑(bladeUnit S)⁻¹ : Mat) * (bladeUnit S : Mat)) = _
  rw [(bladeUnit S).inv_mul, Matrix.trace_one, Fintype.card_finset, Fintype.card_fin]
  norm_num

private theorem tracePair_other {S T : Finset Index} (h : S ≠ T) :
    tracePair S (bladeUnit T : Mat) = 0 := by
  obtain ⟨i, hi⟩ := Function.ne_iff.mp (character_injective.ne h)
  let f := conjugation (matrixGenerator i)
  let u := bladeUnit S
  let v := bladeUnit T
  let A : Mat := ↑u⁻¹ * (v : Mat)
  have hu : f (u : Mat) = character i S • (u : Mat) := conjugation_blade i S
  have hv : f (v : Mat) = character i T • (v : Mat) := conjugation_blade i T
  have hinv : character i S • f (↑u⁻¹ : Mat) = (↑u⁻¹ : Mat) := by
    calc
      _ = (↑u⁻¹ : Mat) * (f (u : Mat) * f (↑u⁻¹ : Mat)) := by
        rw [hu, Matrix.smul_mul, Matrix.mul_smul, ← mul_assoc, u.inv_mul, one_mul]
      _ = _ := by rw [← map_mul, u.mul_inv, map_one, mul_one]
  have hscale : character i S • f A = character i T • A := by
    change character i S • f ((↑u⁻¹ : Mat) * ↑v) = _
    rw [map_mul, hv, Matrix.mul_smul, smul_comm, ← Matrix.smul_mul, hinv]
  have ht := congrArg Matrix.trace hscale
  simp only [Matrix.trace_smul, f, trace_conjugation, smul_eq_mul] at ht
  change Matrix.trace A = 0
  exact (mul_eq_zero.mp (show (character i S - character i T) * Matrix.trace A = 0 by
    rw [sub_mul, ht, sub_self])).resolve_left (sub_ne_zero.mpr hi)

private theorem matrixBlades_independent :
    LinearIndependent ℝ (fun S : Finset Index => (bladeUnit S : Mat)) := by
  apply Fintype.linearIndependent_iff.mpr
  intro c hc S
  have hz := congrArg (tracePair S) hc
  simp only [map_sum, map_smul, map_zero] at hz
  rw [Finset.sum_eq_single S] at hz
  · rw [tracePair_self, smul_eq_mul] at hz
    exact (mul_eq_zero.mp hz).resolve_right (by norm_num)
  · intro T _ hTS
    rw [tracePair_other hTS.symm, smul_zero]
  · simp

private theorem blade_in_image (S : Finset Index) :
    ∃ x : Cl, matrixRepresentation x = (bladeUnit S : Mat) := by
  refine ⟨(S.toList.map gamma).prod, ?_⟩
  unfold bladeUnit
  generalize S.toList = L
  induction L with
  | nil => simp
  | cons i L ih =>
    simp only [List.map_cons, List.prod_cons, map_mul, Units.val_mul, ih]
    rfl

private theorem matrixRepresentation_surjective : Function.Surjective matrixRepresentation := by
  have hcard : Fintype.card (Finset Index) = Module.finrank ℝ Mat := by
    rw [matrix_finrank, Fintype.card_finset, Fintype.card_fin]
    rfl
  let b := basisOfLinearIndependentOfCardEqFinrank' _ matrixBlades_independent hcard
  have hb : ⇑b = fun S : Finset Index => (bladeUnit S : Mat) :=
    coe_basisOfLinearIndependentOfCardEqFinrank' _ _ _
  change Function.Surjective matrixRepresentation.toLinearMap
  apply LinearMap.range_eq_top.mp
  apply top_unique
  rw [← b.span_eq, hb]
  exact Submodule.span_le.mpr (by rintro _ ⟨S, rfl⟩; exact blade_in_image S)

/-- The real Clifford algebra of signature `(7,7)` is the full real
matrix algebra on the 128 exterior basis states. -/
def matrixEquiv : Cl ≃ₐ[ℝ] Mat := by
  let b := ((Pi.basisFun ℝ Index).ExteriorAlgebra).map (CliffordAlgebra.equivExterior splitForm).symm
  have : Module.Finite ℝ Cl := Module.Finite.of_basis b
  have hdim := clifford_finrank.trans matrix_finrank.symm
  exact AlgEquiv.ofBijective matrixRepresentation
    ⟨(LinearMap.injective_iff_surjective_of_finrank_eq_finrank hdim
      (f := matrixRepresentation.toLinearMap)).mpr matrixRepresentation_surjective,
      matrixRepresentation_surjective⟩

@[simp] theorem matrixEquiv_apply (x : Cl) : matrixEquiv x = matrixRepresentation x := rfl

abbrev ComplexMat := Matrix SpinorIndex SpinorIndex ℂ

/-- Embed the real spinor matrices entrywise into complex matrices. -/
def complexEmbedding : Mat →ₐ[ℝ] ComplexMat :=
  (Algebra.ofId ℝ ℂ).mapMatrix

private def complexMatrixRepresentation : ℂ ⊗[ℝ] Cl →ₐ[ℂ] ComplexMat :=
  Algebra.TensorProduct.lift (Algebra.ofId ℂ ComplexMat)
    (complexEmbedding.comp matrixRepresentation) (fun z X =>
      Algebra.commutes z (complexEmbedding (matrixRepresentation X)))

private theorem complexMatrixRepresentation_tmul (z : ℂ) (x : Cl) :
    complexMatrixRepresentation (z ⊗ₜ[ℝ] x) = z • complexEmbedding (matrixRepresentation x) := by
  change (algebraMap ℂ ComplexMat) z * complexEmbedding (matrixRepresentation x) = _
  rw [Algebra.smul_def]

private theorem complexMatrixRepresentation_surjective :
    Function.Surjective complexMatrixRepresentation := by
  intro X
  obtain ⟨x, hx⟩ := matrixRepresentation_surjective (X.map Complex.re)
  obtain ⟨y, hy⟩ := matrixRepresentation_surjective (X.map Complex.im)
  refine ⟨(1 : ℂ) ⊗ₜ[ℝ] x + Complex.I ⊗ₜ[ℝ] y, ?_⟩
  rw [map_add, complexMatrixRepresentation_tmul, complexMatrixRepresentation_tmul, hx, hy, one_smul]
  ext i j
  change (↑(X i j).re : ℂ) + Complex.I * ↑(X i j).im = X i j
  rw [mul_comm Complex.I]
  exact Complex.re_add_im _

/-- The complexified split Clifford algebra in the same spinor basis. -/
def complexMatrixEquiv : ℂ ⊗[ℝ] Cl ≃ₐ[ℂ] ComplexMat := by
  let b := ((Pi.basisFun ℝ Index).ExteriorAlgebra).map (CliffordAlgebra.equivExterior splitForm).symm
  have : Module.Finite ℂ (ℂ ⊗[ℝ] Cl) := Module.Finite.of_basis (b.baseChange ℂ)
  have hdim : Module.finrank ℂ (ℂ ⊗[ℝ] Cl) = Module.finrank ℂ ComplexMat := by
    rw [Module.finrank_baseChange, clifford_finrank, Module.finrank_matrix, Module.finrank_self,
      Fintype.card_finset, Fintype.card_fin]
    rfl
  exact AlgEquiv.ofBijective complexMatrixRepresentation
    ⟨(LinearMap.injective_iff_surjective_of_finrank_eq_finrank hdim
      (f := complexMatrixRepresentation.toLinearMap)).mpr complexMatrixRepresentation_surjective,
      complexMatrixRepresentation_surjective⟩

theorem complexMatrixEquiv_tmul (z : ℂ) (x : Cl) :
    complexMatrixEquiv (z ⊗ₜ[ℝ] x) = z • complexEmbedding (matrixEquiv x) :=
  complexMatrixRepresentation_tmul z x

/-- The Spin group acts on the spinor space by the units of the Clifford
matrix model. -/
def spinorUnits : D7SpinAction.Spin →* ComplexMatˣ :=
  (Units.map (complexEmbedding.comp matrixRepresentation).toMonoidHom).comp spinGroup.toUnits

theorem spinorUnits_val (g : D7SpinAction.Spin) :
    (spinorUnits g : ComplexMat) = complexEmbedding (matrixEquiv g.val) := rfl

private theorem spinorUnits_conjugation (g : D7SpinAction.Spin) (x : Cl) :
    complexEmbedding (matrixEquiv (D7SpinAction.cliffordConjugation g x)) =
      (spinorUnits g : ComplexMat) * complexEmbedding (matrixEquiv x) *
        (↑(spinorUnits g)⁻¹ : ComplexMat) := by
  change complexEmbedding (matrixRepresentation
    (ConjAct.toConjAct (spinGroup.toUnits g) • x)) = _
  rw [ConjAct.units_smul_def, ConjAct.ofConjAct_toConjAct]
  simp only [map_mul]
  rfl

/-- The actual Clifford Spin conjugation becomes matrix conjugation
after complexifying the Clifford algebra. -/
theorem complexMatrixEquiv_intertwines (g : D7SpinAction.Spin) :
    complexMatrixEquiv.toLinearMap.comp
        ((D7SpinAction.cliffordConjugation g).toLinearMap.baseChange ℂ) =
      (LinearMap.mulLeftRight ℂ ((spinorUnits g : ComplexMat), (↑(spinorUnits g)⁻¹ : ComplexMat))).comp
        complexMatrixEquiv.toLinearMap := by
  apply TensorProduct.AlgebraTensorModule.ext
  intro z x
  simp only [LinearMap.comp_apply, LinearMap.baseChange_tmul, AlgEquiv.toLinearMap_apply,
    complexMatrixEquiv_tmul, LinearMap.mulLeftRight_apply, Matrix.mul_smul, Matrix.smul_mul,
    spinorUnits_conjugation]

end

end GeometricUnity.D7CliffordMatrix
~~~

[Return to file index](#file-index)

## D7CliffordAdjoint.lean {#source-d7cliffordadjoint-lean}

Identifies the matrix adjoint, checks Hermitian signature (64,64), and intertwines coefficient conjugation.

~~~lean
import D7CliffordMatrix
import D7UnitaryRealForm
import Mathlib.Analysis.Matrix.Spectrum

/-!
# Transpose on the split Clifford matrix generators

In the exterior basis, creation inserts an index with its exterior sign.
Contraction removes the same index with the same sign. Consequently
transpose fixes the positive Clifford generators and negates the negative
ones.
-/

namespace GeometricUnity.D7CliffordAdjoint

open D7CliffordMatrix
open WitnessW1 (Index Cl splitForm gamma metricSign)
open scoped BigOperators Matrix TensorProduct

noncomputable section

private abbrev basisVector := Pi.basisFun ℝ (Fin 7)
private abbrev creator (i : Fin 7) := creation (basisVector i)
private abbrev annihilator (i : Fin 7) := contraction (basisVector.coord i)

private def singletonIndex (i : Fin 7) : Set.powersetCard (Fin 7) 1 :=
  Set.powersetCard.ofCard (by simp : ({i} : SpinorIndex).card = 1)

private theorem basis_singleton (i : Fin 7) :
    spinorBasis {i} = ExteriorAlgebra.ι ℝ (basisVector i) := by
  let s := singletonIndex i
  change basisVector.ExteriorAlgebra s.val = _
  rw [ExteriorAlgebra.basis_apply_powersetCard]
  let order := s.val.orderIsoOfFin s.prop
  have h : (order 0).val = i := Finset.mem_singleton.mp (order 0).prop
  change ExteriorAlgebra.ιMulti ℝ 1 (fun k => basisVector (order k).val) = _
  rw [ExteriorAlgebra.ιMulti_apply, List.ofFn_succ, List.ofFn_zero, List.prod_cons, List.prod_nil,
    mul_one, h]

private theorem creator_zero (i : Fin 7) (S : SpinorIndex) (hi : i ∈ S) :
    creator i (spinorBasis S) = 0 := by
  change ExteriorAlgebra.ι ℝ (basisVector i) * spinorBasis S = 0
  rw [← basis_singleton]
  let s := singletonIndex i
  let t := Set.powersetCard.ofCard (rfl : S.card = S.card)
  have hn : ¬ Disjoint s.val t.val := fun h => Finset.disjoint_left.mp h (by simp [s, singletonIndex]) hi
  exact ExteriorAlgebra.basis_mul_of_not_disjoint basisVector s t hn

private theorem creator_insert (i : Fin 7) (S : SpinorIndex) (hi : i ∉ S) :
    ∃ c : ℝ, (c = 1 ∨ c = -1) ∧ creator i (spinorBasis S) = c • spinorBasis (insert i S) := by
  change ∃ c : ℝ, _ ∧ ExteriorAlgebra.ι ℝ (basisVector i) * spinorBasis S = _
  rw [← basis_singleton]
  let s := singletonIndex i
  let t := Set.powersetCard.ofCard (rfl : S.card = S.card)
  have hd : Disjoint s.val t.val := Finset.disjoint_singleton_left.mpr hi
  have h := ExteriorAlgebra.basis_mul_of_disjoint basisVector s t hd
  have he : (Set.powersetCard.disjUnion hd).val = insert i S := by
    rw [Set.powersetCard.coe_disjUnion, Finset.disjUnion_eq_union]
    exact Finset.singleton_union _ _
  rw [he] at h
  change spinorBasis {i} * spinorBasis S =
    (Set.powersetCard.permOfDisjoint hd).sign • spinorBasis (insert i S) at h
  rcases Int.units_eq_one_or (Set.powersetCard.permOfDisjoint hd).sign with hp | hp
  · exact ⟨1, Or.inl rfl, by simpa only [hp, one_smul] using h⟩
  · refine ⟨-1, Or.inr rfl, ?_⟩
    rw [hp] at h
    change spinorBasis {i} * spinorBasis S = (-1 : ℤ) • spinorBasis (insert i S) at h
    simpa only [neg_one_smul, neg_one_zsmul] using h

private theorem annihilator_zero (i : Fin 7) (S : SpinorIndex) (hi : i ∉ S) :
    annihilator i (spinorBasis S) = 0 := by
  have hproduct (L : List (Fin 7)) (hL : i ∉ L) :
      annihilator i ((L.map fun j => ExteriorAlgebra.ι ℝ (basisVector j)).prod) = 0 := by
    induction L with
    | nil =>
      exact CliffordAlgebra.contractLeft_one (Q := (0 : QuadraticForm ℝ Half)) (basisVector.coord i)
    | cons j L ih =>
      have hij : i ≠ j := fun hij => hL (List.mem_cons.mpr (Or.inl hij))
      have hnot : i ∉ L := fun hm => hL (List.mem_cons.mpr (Or.inr hm))
      have hcoord : basisVector.coord i (basisVector j) = 0 := by
        simp [Module.Basis.coord_apply, hij]
      rw [List.map_cons, List.prod_cons]
      change CliffordAlgebra.contractLeft (Q := (0 : QuadraticForm ℝ Half)) (basisVector.coord i)
        (CliffordAlgebra.ι 0 (basisVector j) *
          (L.map fun k => ExteriorAlgebra.ι ℝ (basisVector k)).prod) = 0
      rw [CliffordAlgebra.contractLeft_ι_mul, hcoord, zero_smul]
      change 0 - ExteriorAlgebra.ι ℝ (basisVector j) *
        annihilator i ((L.map fun k => ExteriorAlgebra.ι ℝ (basisVector k)).prod) = 0
      rw [ih hnot, mul_zero, sub_zero]
  let s := Set.powersetCard.ofCard (rfl : S.card = S.card)
  let order := s.val.orderIsoOfFin s.prop
  let L := List.ofFn (fun j => (order j).val)
  have hL : i ∉ L := by
    intro h
    obtain ⟨j, hj⟩ := List.mem_ofFn.mp h
    exact hi (hj ▸ (order j).prop)
  change annihilator i (basisVector.ExteriorAlgebra s.val) = 0
  rw [ExteriorAlgebra.basis_apply_powersetCard]
  change annihilator i (ExteriorAlgebra.ιMulti ℝ S.card (fun j => basisVector (order j).val)) = 0
  rw [ExteriorAlgebra.ιMulti_apply]
  have h := hproduct L hL
  rw [show L.map (fun j => ExteriorAlgebra.ι ℝ (basisVector j)) =
    List.ofFn (fun j => ExteriorAlgebra.ι ℝ (basisVector (order j).val)) from List.map_ofFn] at h
  exact h

private theorem annihilator_insert (i : Fin 7) (S : SpinorIndex) (hi : i ∉ S) {c : ℝ}
    (hc : c = 1 ∨ c = -1) (h : creator i (spinorBasis S) = c • spinorBasis (insert i S)) :
    annihilator i (spinorBasis (insert i S)) = c • spinorBasis S := by
  have hu := CliffordAlgebra.contractLeft_ι_mul (Q := (0 : QuadraticForm ℝ Half))
    (basisVector.coord i) (basisVector i) (spinorBasis S)
  change annihilator i (creator i (spinorBasis S)) =
    basisVector.coord i (basisVector i) • spinorBasis S -
      ExteriorAlgebra.ι ℝ (basisVector i) * annihilator i (spinorBasis S) at hu
  rw [h, map_smul, annihilator_zero i S hi, mul_zero, sub_zero] at hu
  have hcoord : basisVector.coord i (basisVector i) = 1 := by simp [Module.Basis.coord_apply]
  rw [hcoord, one_smul] at hu
  rcases hc with rfl | rfl
  · simpa only [one_smul] using hu
  · simpa only [neg_one_smul, neg_neg] using congrArg Neg.neg hu

private theorem creator_repr_zero (i : Fin 7) (S T : SpinorIndex) (h : T ≠ insert i S) :
    spinorBasis.repr (creator i (spinorBasis S)) T = 0 := by
  by_cases hi : i ∈ S
  · rw [creator_zero i S hi]
    simp
  · obtain ⟨c, _, hc⟩ := creator_insert i S hi
    rw [hc, map_smul, Module.Basis.repr_self]
    simp [h]

private theorem creator_transpose (i : Fin 7) :
    (LinearMap.toMatrix spinorBasis spinorBasis (creator i))ᵀ =
      LinearMap.toMatrix spinorBasis spinorBasis (annihilator i) := by
  ext S T
  rw [Matrix.transpose_apply, LinearMap.toMatrix_apply, LinearMap.toMatrix_apply]
  by_cases hi : i ∈ T
  · let U := T.erase i
    have he : insert i U = T := Finset.insert_erase hi
    obtain ⟨c, hc, hcreate⟩ := creator_insert i U (Finset.notMem_erase i T)
    have hcontract := annihilator_insert i U (Finset.notMem_erase i T) hc hcreate
    rw [he] at hcreate hcontract
    by_cases hSU : S = U
    · rw [hSU, hcreate, hcontract]
      simp
    · have hzero : spinorBasis.repr (creator i (spinorBasis S)) T = 0 := by
        by_cases his : i ∈ S
        · rw [creator_zero i S his]
          simp
        · apply creator_repr_zero i S T
          intro hTI
          apply hSU
          change S = T.erase i
          rw [hTI, Finset.erase_insert his]
      rw [hzero, hcontract, map_smul, Module.Basis.repr_self]
      simp [hSU]
  · rw [annihilator_zero i T hi]
    have hTI : T ≠ insert i S := fun h => hi (h.symm ▸ Finset.mem_insert_self i S)
    rw [creator_repr_zero i S T hTI]
    simp

theorem gamma_pos_transpose (i : Fin 7) :
    (matrixEquiv (gamma (Fin.castAdd 7 i)))ᵀ = matrixEquiv (gamma (Fin.castAdd 7 i)) := by
  change (LinearMap.toMatrix spinorBasis spinorBasis
    (endRepresentation (gamma (Fin.castAdd 7 i))))ᵀ = _
  rw [matrixEquiv_apply]
  change _ = LinearMap.toMatrix spinorBasis spinorBasis (endRepresentation (gamma (Fin.castAdd 7 i)))
  rw [endRepresentation_gamma_pos, map_add, Matrix.transpose_add, creator_transpose]
  have h := congrArg Matrix.transpose (creator_transpose i)
  rw [Matrix.transpose_transpose] at h
  rw [← h, add_comm]

theorem gamma_neg_transpose (i : Fin 7) :
    (matrixEquiv (gamma (Fin.natAdd 7 i)))ᵀ = -matrixEquiv (gamma (Fin.natAdd 7 i)) := by
  change (LinearMap.toMatrix spinorBasis spinorBasis
    (endRepresentation (gamma (Fin.natAdd 7 i))))ᵀ = _
  rw [matrixEquiv_apply]
  change _ = -LinearMap.toMatrix spinorBasis spinorBasis (endRepresentation (gamma (Fin.natAdd 7 i)))
  rw [endRepresentation_gamma_neg, map_sub, Matrix.transpose_sub, creator_transpose]
  have h := congrArg Matrix.transpose (creator_transpose i)
  rw [Matrix.transpose_transpose] at h
  rw [← h, neg_sub]

theorem gamma_transpose (i : Index) :
    (matrixEquiv (gamma i))ᵀ = metricSign i • matrixEquiv (gamma i) := by
  refine Fin.addCases (m := 7) (n := 7) ?_ ?_ i
  · intro j
    rw [show metricSign (Fin.castAdd 7 j) = 1 from if_pos j.isLt, one_smul]
    exact gamma_pos_transpose j
  · intro j
    have h : metricSign (Fin.natAdd 7 j) = -1 := if_neg (by
      change ¬ 7 + j.val < 7
      omega)
    rw [h, neg_one_smul]
    exact gamma_neg_transpose j

/-- The product of the seven negative Clifford generators, in increasing
order. Its spinor matrix is the signature operator. -/
def negativeVolume : Cl := gamma 7 * gamma 8 * gamma 9 * gamma 10 * gamma 11 * gamma 12 * gamma 13

private theorem swapDescending (i j : Index) (h : j < i) (x : Cl) :
    gamma i * (gamma j * x) = -(gamma j * (gamma i * x)) := by
  rw [← mul_assoc, WitnessW1.gamma_anticommute i j (ne_of_gt h), neg_mul, mul_assoc]

private theorem cancelNegative (i : Index) (h : 7 ≤ i.val) (x : Cl) :
    gamma i * (gamma i * x) = -x := by
  rw [← mul_assoc, WitnessW1.gamma_square, metricSign, if_neg (by omega), map_neg,
    map_one, neg_mul, one_mul]

theorem negativeVolume_square : negativeVolume * negativeVolume = 1 := by
  rw [← mul_one (negativeVolume * negativeVolume)]
  simp (disch := decide) only [negativeVolume, mul_assoc, swapDescending, cancelNegative,
    neg_mul, mul_neg, neg_neg]

private theorem gamma_negativeVolume (i : Index) :
    gamma i * negativeVolume = (-metricSign i) • (negativeVolume * gamma i) := by
  fin_cases i <;> norm_num [metricSign]
  all_goals
    have h (i j : Index) (hji : j < i) : gamma i * gamma j = -(gamma j * gamma i) :=
      WitnessW1.gamma_anticommute i j (ne_of_gt hji)
    simp (disch := decide) only [negativeVolume, mul_assoc, swapDescending, h,
      mul_neg, neg_neg] <;> rfl

/-- The signature operator on the real spinor space. -/
def signatureMatrix : Mat := matrixEquiv negativeVolume

theorem signatureMatrix_square : signatureMatrix * signatureMatrix = 1 := by
  rw [signatureMatrix, ← map_mul, negativeVolume_square, map_one]

private theorem negative_gamma_orthogonal (i : Index) (h : 7 ≤ i.val) :
    (matrixEquiv (gamma i))ᵀ * matrixEquiv (gamma i) = 1 := by
  have hs : metricSign i = -1 := if_neg (by omega)
  rw [gamma_transpose, hs, neg_one_smul, Matrix.neg_mul, ← map_mul, WitnessW1.gamma_square,
    hs, map_neg, map_one, map_neg, map_one, neg_neg]

private theorem negative_gamma_orthogonal_mul (i : Index) (h : 7 ≤ i.val) (X : Mat) :
    (matrixEquiv (gamma i))ᵀ * (matrixEquiv (gamma i) * X) = X := by
  rw [← mul_assoc, negative_gamma_orthogonal i h, one_mul]

theorem signatureMatrix_transpose : signatureMatrixᵀ = signatureMatrix := by
  have h : signatureMatrixᵀ * signatureMatrix = 1 := by
    simp (disch := decide) only [signatureMatrix, negativeVolume, map_mul, Matrix.transpose_mul,
      mul_assoc, negative_gamma_orthogonal_mul, negative_gamma_orthogonal]
  calc
    signatureMatrixᵀ = signatureMatrixᵀ * (signatureMatrix * signatureMatrix) := by
      rw [signatureMatrix_square, mul_one]
    _ = signatureMatrix := by rw [← mul_assoc, h, one_mul]

private def signatureAdjoint : Mat →ₗ[ℝ] Mat :=
  (LinearMap.mulLeftRight ℝ (signatureMatrix, signatureMatrix)).comp
    (Matrix.transposeLinearEquiv SpinorIndex SpinorIndex ℝ ℝ).toLinearMap

private theorem signatureAdjoint_mul (X Y : Mat) :
    signatureAdjoint (X * Y) = signatureAdjoint Y * signatureAdjoint X := by
  change signatureMatrix * (X * Y)ᵀ * signatureMatrix =
    (signatureMatrix * Yᵀ * signatureMatrix) * (signatureMatrix * Xᵀ * signatureMatrix)
  simp only [Matrix.transpose_mul, mul_assoc]
  rw [← mul_assoc signatureMatrix signatureMatrix, signatureMatrix_square, one_mul]

private theorem signatureAdjoint_gamma (i : Index) :
    signatureAdjoint (matrixEquiv (gamma i)) = -matrixEquiv (gamma i) := by
  change signatureMatrix * (matrixEquiv (gamma i))ᵀ * signatureMatrix =
    -matrixEquiv (gamma i)
  have hsign : metricSign i * -metricSign i = -1 := by unfold metricSign; split <;> norm_num
  have h := congrArg matrixEquiv (gamma_negativeVolume i)
  simp only [map_mul, map_smul] at h
  change matrixEquiv (gamma i) * signatureMatrix =
    (-metricSign i) • (signatureMatrix * matrixEquiv (gamma i)) at h
  rw [gamma_transpose, Matrix.mul_smul, Matrix.smul_mul, mul_assoc, h, Matrix.mul_smul,
    smul_smul, hsign, neg_one_smul, ← mul_assoc, signatureMatrix_square, one_mul]

private theorem signatureAdjoint_generator (v : Index → ℝ) :
    signatureAdjoint (matrixEquiv (CliffordAlgebra.ι splitForm v)) =
      -matrixEquiv (CliffordAlgebra.ι splitForm v) := by
  let f := matrixEquiv.toLinearMap.comp (CliffordAlgebra.ι splitForm)
  have h : signatureAdjoint.comp f = -f := by
    apply (Pi.basisFun ℝ Index).ext
    intro i
    have hBasis : Pi.basisFun ℝ Index i = WitnessW1.basisVector i := by
      simp [Pi.basisFun_apply, WitnessW1.basisVector]
    rw [hBasis]
    simpa only [f, LinearMap.comp_apply, LinearMap.neg_apply, AlgEquiv.toLinearMap_apply,
      gamma] using signatureAdjoint_gamma i
  exact DFunLike.congr_fun h v

/-- Clifford conjugation is the transpose adjoint for the signature
matrix of the spinor realization. -/
theorem matrixEquiv_star (x : Cl) :
    matrixEquiv (star x) = signatureMatrix * (matrixEquiv x)ᵀ * signatureMatrix := by
  change matrixEquiv (star x) = signatureAdjoint (matrixEquiv x)
  induction x using CliffordAlgebra.left_induction with
  | algebraMap r =>
    change matrixEquiv (star (algebraMap ℝ Cl r)) = signatureAdjoint (matrixEquiv (algebraMap ℝ Cl r))
    rw [CliffordAlgebra.star_algebraMap, AlgEquiv.commutes, Algebra.algebraMap_eq_smul_one, map_smul]
    have h : signatureAdjoint 1 = 1 := by
      change signatureMatrix * (1 : Mat)ᵀ * signatureMatrix = 1
      rw [Matrix.transpose_one, mul_one, signatureMatrix_square]
    rw [h]
  | add x y hx hy =>
    simp only [star_add, map_add, hx, hy]
  | ι_mul x v hx =>
    rw [star_mul, CliffordAlgebra.star_ι, map_mul, map_neg, map_mul,
      signatureAdjoint_mul, signatureAdjoint_generator v, hx]

/-- The Hermitian signature matrix in the complex spinor space. -/
def complexSignature : ComplexMat := complexEmbedding signatureMatrix

private theorem complexEmbedding_transpose (X : Mat) :
    complexEmbedding Xᵀ = (complexEmbedding X)ᴴ := by
  ext i j
  change ((X j i : ℝ) : ℂ) = star ((X j i : ℝ) : ℂ)
  simp

theorem complexSignature_hermitian : complexSignatureᴴ = complexSignature := by
  rw [complexSignature, ← complexEmbedding_transpose, signatureMatrix_transpose]

theorem complexSignature_square : complexSignature * complexSignature = 1 := by
  rw [complexSignature, ← map_mul, signatureMatrix_square, map_one]

private theorem complexSignature_trace : Matrix.trace complexSignature = 0 := by
  let a := complexEmbedding (matrixEquiv (gamma 0))
  have ha : a * a = 1 := by
    change complexEmbedding (matrixEquiv (gamma 0)) * complexEmbedding (matrixEquiv (gamma 0)) = 1
    rw [← map_mul, ← map_mul, WitnessW1.gamma_square, show metricSign 0 = 1 from rfl,
      map_one, map_one, map_one]
  have hanti : a * complexSignature = -(complexSignature * a) := by
    have h := congrArg (complexEmbedding.comp matrixEquiv.toAlgHom) (gamma_negativeVolume 0)
    simpa only [AlgHom.comp_apply, AlgEquiv.coe_toAlgHom, map_mul, map_smul, map_neg,
      show metricSign 0 = 1 from rfl, neg_one_smul, complexSignature, signatureMatrix, a] using h
  have htrace : Matrix.trace complexSignature = -Matrix.trace complexSignature := by
    calc
      _ = Matrix.trace (a * (a * complexSignature)) := by rw [← mul_assoc, ha, one_mul]
      _ = Matrix.trace (a * complexSignature * a) := Matrix.trace_mul_comm _ _
      _ = _ := by rw [hanti, Matrix.neg_mul, mul_assoc, ha, mul_one, Matrix.trace_neg]
  have hzero : (2 : ℂ) * Matrix.trace complexSignature = 0 := by
    rw [two_mul, ← eq_neg_iff_add_eq_zero]
    exact htrace
  exact (mul_eq_zero.mp hzero).resolve_left (by norm_num)

private theorem signature_isHermitian : complexSignature.IsHermitian :=
  complexSignature_hermitian

/-- The real eigenvalues of the Hermitian signature matrix. -/
def signatureEigenvalue : SpinorIndex → ℝ := signature_isHermitian.eigenvalues

theorem signatureEigenvalue_sign (i : SpinorIndex) :
    signatureEigenvalue i = 1 ∨ signatureEigenvalue i = -1 := by
  let D : ComplexMat := Matrix.diagonal (fun j => (signatureEigenvalue j : ℂ))
  let U := Unitary.conjStarAlgAut ℂ ComplexMat signature_isHermitian.eigenvectorUnitary
  have hn : complexSignature = U D := signature_isHermitian.spectral_theorem
  have hd : D * D = 1 := by
    apply U.injective
    calc
      U (D * D) = U D * U D := map_mul U D D
      _ = 1 := by rw [← hn, complexSignature_square]
      _ = U 1 := (map_one U).symm
  have hm := congrArg (fun M : ComplexMat => M i i) hd
  change (D * D) i i = (1 : ComplexMat) i i at hm
  have hmul : signatureEigenvalue i * signatureEigenvalue i = 1 := by
    apply Complex.ofReal_injective
    simpa only [D, Matrix.diagonal_mul_diagonal, Matrix.diagonal_apply_eq, Pi.mul_apply,
      Matrix.one_apply_eq, Complex.ofReal_mul, Complex.ofReal_one] using hm
  exact mul_self_eq_one_iff.mp hmul

/-- The Hermitian form has 64 positive and 64 negative eigenvalues. -/
theorem signature_eigenvalue_counts :
    (Finset.univ.filter fun i => signatureEigenvalue i = 1).card = 64 ∧
      (Finset.univ.filter fun i => signatureEigenvalue i = -1).card = 64 := by
  classical
  let positive := Finset.univ.filter fun i => signatureEigenvalue i = 1
  let negative := Finset.univ.filter fun i => signatureEigenvalue i = -1
  have hcover : positive ∪ negative = Finset.univ := by
    ext i
    simp [positive, negative, signatureEigenvalue_sign i]
  have hdisjoint : Disjoint positive negative := Finset.disjoint_left.mpr fun i hp hn => by
    have hP := (Finset.mem_filter.mp hp).2
    have hN := (Finset.mem_filter.mp hn).2
    rw [hP] at hN
    norm_num at hN
  have hsumC : (∑ i : SpinorIndex, (signatureEigenvalue i : ℂ)) = 0 :=
    signature_isHermitian.trace_eq_sum_eigenvalues.symm.trans complexSignature_trace
  have hsum : (∑ i : SpinorIndex, signatureEigenvalue i) = 0 := by exact_mod_cast hsumC
  have hp : (∑ i ∈ positive, signatureEigenvalue i) = (positive.card : ℝ) := by
    rw [Finset.sum_congr rfl (fun _ hi => (Finset.mem_filter.mp hi).2), Finset.sum_const, nsmul_one]
  have hn : (∑ i ∈ negative, signatureEigenvalue i) = -(negative.card : ℝ) := by
    rw [Finset.sum_congr rfl (fun _ hi => (Finset.mem_filter.mp hi).2), Finset.sum_const]
    simp [negative, nsmul_eq_mul]
  rw [← hcover, Finset.sum_union hdisjoint, hp, hn, ← sub_eq_add_neg] at hsum
  have hcards : positive.card + negative.card = 128 := by
    rw [← Finset.card_union_of_disjoint hdisjoint, hcover, Finset.card_univ,
      Fintype.card_finset, Fintype.card_fin]
    rfl
  have heq : positive.card = negative.card := by exact_mod_cast sub_eq_zero.mp hsum
  change positive.card = 64 ∧ negative.card = 64
  omega

/-- The actual Spin matrices preserve the Hermitian signature form. -/
theorem spinorUnits_preserve_signature (g : D7SpinAction.Spin) :
    (spinorUnits g : ComplexMat)ᴴ * complexSignature * (spinorUnits g : ComplexMat) =
      complexSignature := by
  have hg : star (g.val : Cl) * g.val = 1 :=
    Unitary.star_mul_self_of_mem (pinGroup.mem_unitary (spinGroup.mem_pin g.prop))
  have h := congrArg (complexEmbedding.comp matrixEquiv.toAlgHom) hg
  simp only [AlgHom.comp_apply, AlgEquiv.coe_toAlgHom, map_mul, map_one, matrixEquiv_star,
    complexEmbedding_transpose, ← spinorUnits_val g] at h
  have h' := congrArg (fun X : ComplexMat => complexSignature * X) h
  change complexSignature *
      ((complexSignature * (spinorUnits g : ComplexMat)ᴴ * complexSignature) *
        (spinorUnits g : ComplexMat)) = complexSignature * 1 at h'
  simpa only [← mul_assoc, complexSignature_square, one_mul, mul_one] using h'

/-- Spin conjugation on the skew-adjoint real coefficient matrices of
the spinor model. -/
def coefficientConjugation (g : D7SpinAction.Spin) :
    ↥(D7UnitaryRealForm.skewAdjoint complexSignature) →ₗ[ℝ]
      ↥(D7UnitaryRealForm.skewAdjoint complexSignature) :=
  D7UnitaryRealForm.realMatrixConjugation complexSignature_square
    (spinorUnits g) (spinorUnits_preserve_signature g)

/-- Identify the complexification of the actual skew-adjoint coefficient
space with the complexified split Clifford algebra. -/
def cliffordCoefficientEquiv :
    ℂ ⊗[ℝ] ↥(D7UnitaryRealForm.skewAdjoint complexSignature) ≃ₗ[ℂ] ℂ ⊗[ℝ] Cl :=
  (D7UnitaryRealForm.complexificationEquiv complexSignature_hermitian
    complexSignature_square).trans complexMatrixEquiv.toLinearEquiv.symm

/-- The coefficient identification intertwines the actual Spin actions. -/
theorem cliffordCoefficientEquiv_intertwines (g : D7SpinAction.Spin) :
    cliffordCoefficientEquiv.toLinearMap.comp ((coefficientConjugation g).baseChange ℂ) =
      ((D7SpinAction.cliffordConjugation g).toLinearMap.baseChange ℂ).comp
        cliffordCoefficientEquiv.toLinearMap := by
  let e := D7UnitaryRealForm.complexificationEquiv complexSignature_hermitian
    complexSignature_square
  have he z : complexMatrixEquiv (cliffordCoefficientEquiv z) = e z :=
    complexMatrixEquiv.apply_symm_apply (e z)
  apply LinearMap.ext
  intro z
  apply complexMatrixEquiv.injective
  change complexMatrixEquiv (cliffordCoefficientEquiv ((coefficientConjugation g).baseChange ℂ z)) =
    complexMatrixEquiv ((D7SpinAction.cliffordConjugation g).toLinearMap.baseChange ℂ
      (cliffordCoefficientEquiv z))
  rw [he]
  have hspin := DFunLike.congr_fun (complexMatrixEquiv_intertwines g) (cliffordCoefficientEquiv z)
  change complexMatrixEquiv ((D7SpinAction.cliffordConjugation g).toLinearMap.baseChange ℂ
      (cliffordCoefficientEquiv z)) =
    D7UnitaryRealForm.matrixConjugation (spinorUnits g)
      (complexMatrixEquiv (cliffordCoefficientEquiv z)) at hspin
  rw [hspin, he]
  exact DFunLike.congr_fun (D7UnitaryRealForm.complexification_intertwines
    complexSignature_hermitian complexSignature_square (spinorUnits g)
    (spinorUnits_preserve_signature g)) z

end

end GeometricUnity.D7CliffordAdjoint
~~~

[Return to file index](#file-index)

## D7SpinNullFrame.lean {#source-d7spinnullframe-lean}

Changes the real vector action into split null coordinates and maps its complexification into the orthogonal action.

~~~lean
import D7SpinRootLifts
import D7SpinOrientation
import D7Hodge
import Mathlib.LinearAlgebra.Complex.Module
import Mathlib.LinearAlgebra.Matrix.ToLin

/-!
# The real Spin vector action in split null coordinates

The two entries of each diagonal pair `(p,n)` become `p+n` and
`(p-n)/2`. This normalization gives the exact complex pairing used by
`D7Exterior.splitForm`.
-/

namespace GeometricUnity.D7SpinNullFrame

open D7Exterior
open scoped BigOperators Matrix

noncomputable section

abbrev RealSpace := Axis → ℝ

private abbrev diagPositive (i : Pair) : Axis := Fin.castAdd 7 i
private abbrev diagNegative (i : Pair) : Axis := Fin.natAdd 7 i
private abbrev coordinate (i : Axis) : RealSpace →ₗ[ℝ] ℝ := LinearMap.proj i

theorem pairIndex_plus (i : Pair) : pairIndex (plusAxis i) = i :=
  Fin.ext (by change 2 * i.val / 2 = i.val; omega)

theorem pairIndex_minus (i : Pair) : pairIndex (minusAxis i) = i :=
  Fin.ext (by change (2 * i.val + 1) / 2 = i.val; omega)

private def toNull : RealSpace →ₗ[ℝ] RealSpace :=
  LinearMap.pi fun j =>
    let i := pairIndex j
    if j.val % 2 = 0 then
      coordinate (diagPositive i) + coordinate (diagNegative i)
    else
      (1 / 2 : ℝ) • (coordinate (diagPositive i) - coordinate (diagNegative i))

private def fromNull : RealSpace →ₗ[ℝ] RealSpace :=
  LinearMap.pi (Fin.addCases (m := 7) (n := 7)
    (fun i => (1 / 2 : ℝ) • LinearMap.proj (plusAxis i) + LinearMap.proj (minusAxis i))
    (fun i => (1 / 2 : ℝ) • LinearMap.proj (plusAxis i) - LinearMap.proj (minusAxis i)))

private theorem toNull_plus (x : RealSpace) (i : Pair) :
    toNull x (plusAxis i) = x (diagPositive i) + x (diagNegative i) := by
  have hp : (plusAxis i).val % 2 = 0 := by
    change (2 * i.val) % 2 = 0
    omega
  simp only [toNull, LinearMap.pi_apply, pairIndex_plus, hp, if_true, LinearMap.add_apply,
    LinearMap.proj_apply]

private theorem toNull_minus (x : RealSpace) (i : Pair) :
    toNull x (minusAxis i) = (1 / 2 : ℝ) * (x (diagPositive i) - x (diagNegative i)) := by
  have hp : (minusAxis i).val % 2 ≠ 0 := by
    change (2 * i.val + 1) % 2 ≠ 0
    omega
  simp only [toNull, LinearMap.pi_apply, pairIndex_minus, if_neg hp, LinearMap.smul_apply,
    LinearMap.sub_apply, LinearMap.proj_apply, smul_eq_mul]

private theorem fromNull_pos (x : RealSpace) (i : Pair) :
    fromNull x (diagPositive i) = (1 / 2 : ℝ) * x (plusAxis i) + x (minusAxis i) := by
  simp only [fromNull, LinearMap.pi_apply, Fin.addCases_left, LinearMap.add_apply,
    LinearMap.smul_apply, LinearMap.proj_apply, smul_eq_mul]

private theorem fromNull_neg (x : RealSpace) (i : Pair) :
    fromNull x (diagNegative i) = (1 / 2 : ℝ) * x (plusAxis i) - x (minusAxis i) := by
  simp only [fromNull, LinearMap.pi_apply, Fin.addCases_right, LinearMap.sub_apply,
    LinearMap.smul_apply, LinearMap.proj_apply, smul_eq_mul]

theorem null_axis_cases (j : Axis) :
    j = plusAxis (pairIndex j) ∨ j = minusAxis (pairIndex j) := by
  by_cases h : j.val % 2 = 0
  · exact Or.inl (Fin.ext (by change j.val = 2 * (j.val / 2); omega))
  · exact Or.inr (Fin.ext (by change j.val = 2 * (j.val / 2) + 1; omega))

/-- The real diagonal-to-null linear equivalence. -/
def nullFrame : RealSpace ≃ₗ[ℝ] RealSpace where
  __ := toNull
  invFun := fromNull
  left_inv x := by
    funext j
    refine Fin.addCases (m := 7) (n := 7) ?_ ?_ j
    · intro i
      change fromNull (toNull x) (diagPositive i) = _
      rw [fromNull_pos, toNull_plus, toNull_minus]
      ring
    · intro i
      change fromNull (toNull x) (diagNegative i) = _
      rw [fromNull_neg, toNull_plus, toNull_minus]
      ring
  right_inv x := by
    funext j
    change toNull (fromNull x) j = x j
    rcases null_axis_cases j with h | h
    · conv_lhs => rw [h]
      conv_rhs => rw [h]
      rw [toNull_plus, fromNull_pos, fromNull_neg]
      ring
    · conv_lhs => rw [h]
      conv_rhs => rw [h]
      rw [toNull_minus, fromNull_pos, fromNull_neg]
      ring

/-- The real form of the complex pairing in the split coordinates. -/
def realSplitPairing (x y : RealSpace) : ℝ :=
  ∑ i : Pair, (x (plusAxis i) * y (minusAxis i) + x (minusAxis i) * y (plusAxis i))

private theorem splitForm_diag (x : RealSpace) :
    WitnessW1.splitForm x =
      ∑ i : Pair, (x (diagPositive i) ^ 2 - x (diagNegative i) ^ 2) := by
  rw [WitnessW1.splitForm, QuadraticMap.weightedSumSquares_apply,
    Fin.sum_univ_add (a := 7) (b := 7) (fun i => WitnessW1.metricSign i • (x i * x i))]
  simp only [WitnessW1.metricSign, Fin.val_castAdd, Fin.val_natAdd, Fin.isLt, if_true,
    show ∀ i : Pair, ¬ 7 + i.val < 7 from fun i => by omega, if_false, smul_eq_mul,
    one_mul, neg_one_mul, ← Finset.sum_add_distrib, pow_two, sub_eq_add_neg]

theorem nullFrame_pairing (x y : RealSpace) :
    realSplitPairing (nullFrame x) (nullFrame y) =
      (WitnessW1.splitForm (x + y) - WitnessW1.splitForm x - WitnessW1.splitForm y) / 2 := by
  change realSplitPairing (toNull x) (toNull y) = _
  simp only [realSplitPairing, toNull_plus, toNull_minus, splitForm_diag, Pi.add_apply,
    ← Finset.sum_sub_distrib, div_eq_mul_inv, Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro i _
  ring

theorem polar_eq_pairing (x y : RealSpace) :
    QuadraticMap.polar WitnessW1.splitForm x y =
      2 * realSplitPairing (nullFrame x) (nullFrame y) := by
  rw [nullFrame_pairing, QuadraticMap.polar]
  ring

/-- The real Spin action in the normalized null basis. -/
def realNullAction : Representation ℝ D7SpinAction.Spin RealSpace :=
  (nullFrame.conjAlgEquiv ℝ).toAlgHom.toMonoidHom.comp D7SpinAction.vectorRepresentation

theorem realNullAction_apply (g : D7SpinAction.Spin) (x : RealSpace) :
    realNullAction g x = nullFrame (D7SpinAction.vectorRepresentation g (nullFrame.symm x)) := rfl

theorem realNullAction_preserves (g : D7SpinAction.Spin) (x y : RealSpace) :
    realSplitPairing (realNullAction g x) (realNullAction g y) = realSplitPairing x y := by
  obtain ⟨x, rfl⟩ := nullFrame.surjective x
  obtain ⟨y, rfl⟩ := nullFrame.surjective y
  simp only [realNullAction_apply, LinearEquiv.symm_apply_apply, nullFrame_pairing, ← map_add,
    D7SpinAction.vectorRepresentation_preserves]

theorem realNullAction_det (g : D7SpinAction.Spin) : (realNullAction g).det = 1 := by
  change ((nullFrame.conjAlgEquiv ℝ) (D7SpinAction.vectorRepresentation g)).det = 1
  rw [LinearEquiv.conjAlgEquiv_apply, LinearMap.det_comp, LinearMap.det_comp,
    D7SpinOrientation.vectorRepresentation_det, one_mul, LinearEquiv.det_mul_det_symm]

/-- The Clifford lift acts by the two signed terms of a split
transvection in null coordinates. The root parameter is twice the
coefficient of the bivector in the Clifford lift. -/
theorem realNullAction_isotropicLift (a b c x : RealSpace) (r : ℝ)
    (ha : WitnessW1.splitForm a = 0) (hb : WitnessW1.splitForm b = 0)
    (hc : WitnessW1.splitForm c = 1)
    (hab : WitnessW1.splitForm.IsOrtho a b) (hac : WitnessW1.splitForm.IsOrtho a c)
    (hbc : WitnessW1.splitForm.IsOrtho b c) :
    realNullAction (D7SpinRootLifts.isotropicLift a b c (r / 2) ha hb hc hab hac hbc) x =
      x + r • (realSplitPairing (nullFrame b) x • nullFrame a -
        realSplitPairing (nullFrame a) x • nullFrame b) := by
  rw [realNullAction_apply, D7SpinRootLifts.isotropicLift_action,
    polar_eq_pairing b, polar_eq_pairing a]
  simp only [map_add, map_sub, map_smul, LinearEquiv.apply_symm_apply]
  funext i
  simp only [Pi.add_apply, Pi.sub_apply, Pi.smul_apply, smul_eq_mul]
  ring

private def complexifyEnd : Module.End ℝ RealSpace →ₐ[ℝ] Module.End ℂ Space :=
  ((Matrix.toLinAlgEquiv' : Matrix Axis Axis ℂ ≃ₐ[ℂ] Module.End ℂ Space).toAlgHom.restrictScalars ℝ).comp
    ((Algebra.ofId ℝ ℂ).mapMatrix.comp LinearMap.toMatrixAlgEquiv'.toAlgHom)

/-- The real vector action extended to the complex split coordinate space. -/
def complexNullAction : Representation ℂ D7SpinAction.Spin Space :=
  complexifyEnd.toMonoidHom.comp realNullAction

theorem complexNullAction_det (g : D7SpinAction.Spin) : (complexNullAction g).det = 1 := by
  let M : Matrix Axis Axis ℝ := LinearMap.toMatrixAlgEquiv' (realNullAction g)
  have hM : LinearMap.toMatrix' (complexNullAction g) = M.map Complex.ofRealHom :=
    LinearMap.toMatrixAlgEquiv'.apply_symm_apply (M.map Complex.ofRealHom)
  rw [← LinearMap.det_toMatrix', hM]
  change (Complex.ofRealHom.mapMatrix M).det = 1
  rw [← Complex.ofRealHom.map_det]
  change Complex.ofRealHom (Matrix.det (LinearMap.toMatrix' (realNullAction g))) = 1
  rw [LinearMap.det_toMatrix', realNullAction_det, map_one]

private def ofRealVector (x : RealSpace) : Space := fun i => ↑(x i)

theorem complexNullAction_ofReal (g : D7SpinAction.Spin) (x : RealSpace) :
    complexNullAction g (ofRealVector x) = ofRealVector (realNullAction g x) := by
  let M : Matrix Axis Axis ℝ := LinearMap.toMatrixAlgEquiv' (realNullAction g)
  have hM : M.mulVecLin = realNullAction g := LinearMap.toMatrixAlgEquiv'.symm_apply_apply _
  funext i
  change (M.map Complex.ofRealHom *ᵥ (Complex.ofRealHom ∘ x)) i = ↑((realNullAction g x) i)
  rw [← Complex.ofRealHom.map_mulVec, ← Matrix.mulVecLin_apply, hM]
  rfl

private theorem splitPairing_ofReal (x y : RealSpace) :
    splitForm (ofRealVector x) (ofRealVector y) = (realSplitPairing x y : ℂ) := by
  change (∑ i : Pair, ((x (plusAxis i) : ℂ) * (y (minusAxis i) : ℂ) +
    (x (minusAxis i) : ℂ) * (y (plusAxis i) : ℂ))) =
    Complex.ofRealHom (∑ i : Pair,
      (x (plusAxis i) * y (minusAxis i) + x (minusAxis i) * y (plusAxis i)))
  simp only [map_sum, map_add, map_mul, Complex.ofRealHom_eq_coe]

private theorem axisBasis_ofReal (i : Axis) :
    axisBasis i = ofRealVector (Pi.basisFun ℝ Axis i) := by
  funext j
  by_cases h : j = i <;> simp [axisBasis, Pi.basisFun_apply, ofRealVector, h]

theorem complexNullAction_preserves (g : D7SpinAction.Spin) (x y : Space) :
    splitForm (complexNullAction g x) (complexNullAction g y) = splitForm x y := by
  let f := complexNullAction g
  have h : (f.dualMap.comp D7Hodge.splitMetric).comp f = D7Hodge.splitMetric := by
    apply axisBasis.ext
    intro i
    apply axisBasis.ext
    intro j
    change D7Hodge.splitMetric (f (axisBasis i)) (f (axisBasis j)) =
      D7Hodge.splitMetric (axisBasis i) (axisBasis j)
    simp only [D7Hodge.splitMetric_apply, axisBasis_ofReal, f, complexNullAction_ofReal,
      splitPairing_ofReal, realNullAction_preserves]
  have hv := DFunLike.congr_fun (DFunLike.congr_fun h x) y
  change D7Hodge.splitMetric (f x) (f y) = D7Hodge.splitMetric x y at hv
  simpa only [D7Hodge.splitMetric_apply] using hv

/-- The complexified real Spin action as a homomorphism into the split
special orthogonal group used in the (D_7) calculation. -/
def spinToSO : D7SpinAction.Spin →* splitSpecialOrthogonal where
  toFun g := ⟨complexNullAction g, complexNullAction_det g, complexNullAction_preserves g⟩
  map_one' := Subtype.ext (map_one complexNullAction)
  map_mul' g h := Subtype.ext (map_mul complexNullAction g h)

/-! ## Real parameters in the split root families -/

/-- The other null axis in the same hyperbolic pair. -/
def pairedAxis (i : Axis) : Axis :=
  if i.val % 2 = 0 then minusAxis (pairIndex i) else plusAxis (pairIndex i)

@[simp] theorem pairedAxis_plus (i : Pair) : pairedAxis (plusAxis i) = minusAxis i := by
  rw [pairedAxis, pairIndex_plus, if_pos]
  change (2 * i.val) % 2 = 0
  omega

@[simp] theorem pairedAxis_minus (i : Pair) : pairedAxis (minusAxis i) = plusAxis i := by
  rw [pairedAxis, pairIndex_minus, if_neg]
  change (2 * i.val + 1) % 2 ≠ 0
  omega

private theorem plus_ne_minus (i j : Pair) : plusAxis i ≠ minusAxis j := by
  intro h
  have h' := congrArg Fin.val h
  change 2 * i.val = 2 * j.val + 1 at h'
  omega

theorem pairedAxis_pairIndex (i : Axis) : pairIndex (pairedAxis i) = pairIndex i := by
  rcases null_axis_cases i with h | h
  · rw [h, pairedAxis_plus, pairIndex_plus, pairIndex_minus]
  · rw [h, pairedAxis_minus, pairIndex_plus, pairIndex_minus]

theorem pairedAxis_ne (i : Axis) : pairedAxis i ≠ i := by
  rcases null_axis_cases i with h | h
  · rw [h, pairedAxis_plus]
    exact (plus_ne_minus _ _).symm
  · rw [h, pairedAxis_minus]
    exact plus_ne_minus _ _

@[simp] theorem pairedAxis_pairedAxis (i : Axis) : pairedAxis (pairedAxis i) = i := by
  rcases null_axis_cases i with h | h
  · rw [h, pairedAxis_plus, pairedAxis_minus]
  · rw [h, pairedAxis_minus, pairedAxis_plus]

private abbrev realBasis := Pi.basisFun ℝ Axis

private theorem realBasis_apply (i j : Axis) : realBasis i j = if j = i then 1 else 0 := by
  rw [Pi.basisFun_apply, Pi.single_apply]

private theorem realSplitPairing_basis (i : Axis) (x : RealSpace) :
    realSplitPairing (realBasis i) x = x (pairedAxis i) := by
  have hplus (j k : Pair) : plusAxis j = plusAxis k ↔ j = k := by
    constructor
    · intro h
      simpa only [pairIndex_plus] using congrArg pairIndex h
    · exact congrArg plusAxis
  have hminus (j k : Pair) : minusAxis j = minusAxis k ↔ j = k := by
    constructor
    · intro h
      simpa only [pairIndex_minus] using congrArg pairIndex h
    · exact congrArg minusAxis
  rcases null_axis_cases i with h | h
  · rw [h, pairedAxis_plus]
    simp only [realSplitPairing, realBasis_apply, hplus, Ne.symm (plus_ne_minus _ _), if_false,
      zero_mul, add_zero, ite_mul, one_mul, Finset.sum_ite_eq', Finset.mem_univ, if_true]
  · rw [h, pairedAxis_minus]
    simp only [realSplitPairing, realBasis_apply, hminus, plus_ne_minus, if_false, zero_mul,
      zero_add, ite_mul, one_mul, Finset.sum_ite_eq', Finset.mem_univ, if_true]

private theorem realSplitPairing_add_left (x y z : RealSpace) :
    realSplitPairing (x + y) z = realSplitPairing x z + realSplitPairing y z := by
  simp only [realSplitPairing, Pi.add_apply, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro i _
  ring

private theorem realSplitPairing_smul_left (r : ℝ) (x y : RealSpace) :
    realSplitPairing (r • x) y = r * realSplitPairing x y := by
  simp only [realSplitPairing, Pi.smul_apply, smul_eq_mul, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i _
  ring

private theorem quadratic_eq_pairing (x : RealSpace) :
    WitnessW1.splitForm x = realSplitPairing (nullFrame x) (nullFrame x) := by
  have h := polar_eq_pairing x x
  rw [QuadraticMap.polar_self, two_smul] at h
  linarith

private theorem ortho_of_null_pairing {x y : RealSpace}
    (h : realSplitPairing (nullFrame x) (nullFrame y) = 0) :
    WitnessW1.splitForm.IsOrtho x y := by
  apply QuadraticMap.isOrtho_polarBilin.mp
  rw [QuadraticMap.polarBilin_apply_apply, polar_eq_pairing, h, mul_zero]

private theorem auxiliary_pair (i j : Pair) (h : i ≠ j) : ∃ k : Pair, k ≠ i ∧ k ≠ j := by
  classical
  by_contra! hn
  have hsub : (Finset.univ : Finset Pair) ⊆ {i, j} := by
    intro k _
    simp only [Finset.mem_insert, Finset.mem_singleton]
    specialize hn k
    tauto
  have hcard := Finset.card_le_card hsub
  rw [Finset.card_univ, Fintype.card_fin, Finset.card_pair_eq_two_iff.mpr h] at hcard
  omega

private theorem rootGroup_ofReal (r : ℝ) (a q b u : Axis) (x : RealSpace) :
    rootGroup (r : ℂ) a q b u (ofRealVector x) =
      ofRealVector (x + r • (x q • realBasis a - x u • realBasis b)) := by
  have hcoord (i : Axis) : axisBasis.coord i (ofRealVector x) = (x i : ℂ) := by
    simp [axisBasis, Module.Basis.coord_apply, Pi.basisFun_repr, ofRealVector]
  change ofRealVector x + (r : ℂ) • (axisBasis.coord q (ofRealVector x) • axisBasis a) -
    (r : ℂ) • (axisBasis.coord u (ofRealVector x) • axisBasis b) = _
  rw [hcoord, hcoord, axisBasis_ofReal a, axisBasis_ofReal b]
  funext i
  simp only [Pi.add_apply, Pi.sub_apply, Pi.smul_apply, ofRealVector, smul_eq_mul,
    Complex.ofReal_add, Complex.ofReal_mul, Complex.ofReal_sub]
  ring

/-- Each pair of axes from distinct hyperbolic pairs gives a split root
action at every real parameter, realized by an element of real Spin. -/
theorem exists_rootGroup_lift (a b : Axis) (hab : pairIndex a ≠ pairIndex b) (r : ℝ) :
    ∃ g : D7SpinAction.Spin,
      complexNullAction g = rootGroup (r : ℂ) a (pairedAxis b) b (pairedAxis a) := by
  obtain ⟨k, hka, hkb⟩ := auxiliary_pair (pairIndex a) (pairIndex b) hab
  let A := nullFrame.symm (realBasis a)
  let B := nullFrame.symm (realBasis b)
  let cNull := realBasis (plusAxis k) + (1 / 2 : ℝ) • realBasis (minusAxis k)
  let C := nullFrame.symm cNull
  have hA : nullFrame A = realBasis a := nullFrame.apply_symm_apply _
  have hB : nullFrame B = realBasis b := nullFrame.apply_symm_apply _
  have hC : nullFrame C = cNull := nullFrame.apply_symm_apply _
  have ha0 : WitnessW1.splitForm A = 0 := by
    rw [quadratic_eq_pairing, hA, realSplitPairing_basis, realBasis_apply, if_neg (pairedAxis_ne a)]
  have hb0 : WitnessW1.splitForm B = 0 := by
    rw [quadratic_eq_pairing, hB, realSplitPairing_basis, realBasis_apply, if_neg (pairedAxis_ne b)]
  have hc1 : WitnessW1.splitForm C = 1 := by
    rw [quadratic_eq_pairing, hC]
    simp only [cNull, realSplitPairing_add_left, realSplitPairing_smul_left, realSplitPairing_basis,
      pairedAxis_plus, pairedAxis_minus, Pi.add_apply, Pi.smul_apply, smul_eq_mul, realBasis_apply,
      plus_ne_minus, Ne.symm (plus_ne_minus _ _), if_false, if_true]
    norm_num
  have hab' : WitnessW1.splitForm.IsOrtho A B := by
    apply ortho_of_null_pairing
    rw [hA, hB, realSplitPairing_basis, realBasis_apply]
    apply if_neg
    intro h
    exact hab (by simpa only [pairedAxis_pairIndex] using congrArg pairIndex h)
  have hcp (i : Axis) (hi : k ≠ pairIndex i) : cNull (pairedAxis i) = 0 := by
    have hplus : pairedAxis i ≠ plusAxis k := by
      intro h
      exact hi (by simpa only [pairedAxis_pairIndex, pairIndex_plus] using (congrArg pairIndex h).symm)
    have hminus : pairedAxis i ≠ minusAxis k := by
      intro h
      exact hi (by simpa only [pairedAxis_pairIndex, pairIndex_minus] using (congrArg pairIndex h).symm)
    simp only [cNull, Pi.add_apply, Pi.smul_apply, realBasis_apply, if_neg hplus, if_neg hminus,
      smul_zero, add_zero]
  have hac : WitnessW1.splitForm.IsOrtho A C := by
    apply ortho_of_null_pairing
    rw [hA, hC, realSplitPairing_basis, hcp a hka]
  have hbc : WitnessW1.splitForm.IsOrtho B C := by
    apply ortho_of_null_pairing
    rw [hB, hC, realSplitPairing_basis, hcp b hkb]
  let g := D7SpinRootLifts.isotropicLift A B C (r / 2) ha0 hb0 hc1 hab' hac hbc
  have hreal (x : RealSpace) : realNullAction g x =
      x + r • (x (pairedAxis b) • realBasis a - x (pairedAxis a) • realBasis b) := by
    rw [show realNullAction g x =
      x + r • (realSplitPairing (nullFrame B) x • nullFrame A -
        realSplitPairing (nullFrame A) x • nullFrame B) from
      realNullAction_isotropicLift A B C x r ha0 hb0 hc1 hab' hac hbc,
      hA, hB, realSplitPairing_basis, realSplitPairing_basis]
  refine ⟨g, axisBasis.ext ?_⟩
  intro j
  rw [axisBasis_ofReal, complexNullAction_ofReal, hreal, rootGroup_ofReal]

theorem exists_rootMinus_lift (i j : Pair) (h : i ≠ j) (r : ℝ) :
    ∃ g : D7SpinAction.Spin, complexNullAction g = rootMinus (r : ℂ) i j := by
  have hn : pairIndex (plusAxis i) ≠ pairIndex (minusAxis j) := by
    simpa only [pairIndex_plus, pairIndex_minus] using h
  simpa only [pairedAxis_plus, pairedAxis_minus, rootMinus] using
    exists_rootGroup_lift (plusAxis i) (minusAxis j) hn r

theorem exists_rootPlus_lift (i j : Pair) (h : i ≠ j) (r : ℝ) :
    ∃ g : D7SpinAction.Spin, complexNullAction g = rootPlus (r : ℂ) i j := by
  have hn : pairIndex (plusAxis i) ≠ pairIndex (plusAxis j) := by
    simpa only [pairIndex_plus] using h
  simpa only [pairedAxis_plus, rootPlus] using
    exists_rootGroup_lift (plusAxis i) (plusAxis j) hn r

theorem rootMinusElement_mem_spinRange (i j : Pair) (h : i < j) (r : ℝ) :
    rootMinusElement (r : ℂ) i j h ∈ Set.range spinToSO := by
  obtain ⟨g, hg⟩ := exists_rootMinus_lift i j (ne_of_lt h) r
  exact ⟨g, Subtype.ext hg⟩

theorem rootPlusElement_mem_spinRange (i j : Pair) (h : i < j) (r : ℝ) :
    rootPlusElement (r : ℂ) i j h ∈ Set.range spinToSO := by
  obtain ⟨g, hg⟩ := exists_rootPlus_lift i j (ne_of_lt h) r
  exact ⟨g, Subtype.ext hg⟩

end

end GeometricUnity.D7SpinNullFrame
~~~

[Return to file index](#file-index)

## D7SpinRootLifts.lean {#source-d7spinrootlifts-lean}

Constructs real Spin lifts of the isotropic root transvections.

~~~lean
import D7SpinAction
import Mathlib.Tactic.NoncommRing

/-!
# Real Spin lifts of isotropic transvections

For orthogonal isotropic vectors `a,b`, the lift of the root action has
Clifford value `1 + t • (ι a * ι b)`. An auxiliary orthogonal vector
`c` of square one expresses that element as a product of four vectors
of square one.
-/

namespace GeometricUnity.D7SpinRootLifts

open D7SpinAction (Vector Spin)
open WitnessW1 (splitForm Cl)

noncomputable section

private abbrev ι := CliffordAlgebra.ι splitForm

private theorem vector_square_one {v : Vector} (h : splitForm v = 1) : ι v * ι v = 1 := by
  rw [CliffordAlgebra.ι_sq_scalar, h, map_one]

private def vectorUnit (v : Vector) (h : splitForm v = 1) : Clˣ :=
  ⟨ι v, ι v, vector_square_one h, vector_square_one h⟩

private theorem vectorUnit_mem (v : Vector) (h : splitForm v = 1) :
    vectorUnit v h ∈ lipschitzGroup splitForm :=
  Subgroup.subset_closure ⟨v, rfl⟩

private def vectorPair (v w : Vector) (hv : splitForm v = 1) (hw : splitForm w = 1) : Spin :=
  ⟨ι v * ι w, spinGroup.mem_iff.mpr ⟨by
    apply (pinGroup.units_mem_iff (x := vectorUnit v hv * vectorUnit w hw)).mpr
    refine ⟨(lipschitzGroup splitForm).mul_mem (vectorUnit_mem v hv) (vectorUnit_mem w hw),
      Unitary.mem_iff.mpr ?_⟩
    change star (ι v * ι w) * (ι v * ι w) = 1 ∧ (ι v * ι w) * star (ι v * ι w) = 1
    simp only [star_mul, CliffordAlgebra.star_ι, neg_mul_neg]
    constructor
    · rw [mul_assoc (ι w), ← mul_assoc (ι v) (ι v), vector_square_one hv, one_mul,
        vector_square_one hw]
    · rw [mul_assoc (ι v), ← mul_assoc (ι w) (ι w), vector_square_one hw, one_mul,
        vector_square_one hv]
    , CliffordAlgebra.ι_mul_ι_mem_evenOdd_zero splitForm v w⟩⟩

private theorem isotropic_square {a : Vector} (ha : splitForm a = 0) : ι a * ι a = 0 := by
  rw [CliffordAlgebra.ι_sq_scalar, ha, map_zero]

private theorem isotropic_mul_mul {a u : Vector} (ha : splitForm a = 0)
    (h : splitForm.IsOrtho a u) : ι a * ι u * ι a = 0 := by
  rw [mul_assoc, CliffordAlgebra.ι_mul_ι_comm_of_isOrtho h.symm, mul_neg, ← mul_assoc,
    isotropic_square ha, zero_mul, neg_zero]

private theorem add_isotropic_square {a u : Vector} (t : ℝ)
    (ha : splitForm a = 0) (hu : splitForm u = 1) (h : splitForm.IsOrtho a u) :
    splitForm (u + t • a) = 1 := by
  have horth : splitForm.IsOrtho u (t • a) := by
    apply QuadraticMap.isOrtho_polarBilin.mp
    rw [QuadraticMap.polarBilin_apply_apply, QuadraticMap.polar_smul_right, h.symm.polar_eq_zero,
      smul_zero]
  rw [QuadraticMap.isOrtho_def] at horth
  rw [horth, QuadraticMap.map_smul, ha, hu, smul_zero, add_zero]

private theorem isOrtho_add {a b c : Vector} (hab : splitForm.IsOrtho a b)
    (hac : splitForm.IsOrtho a c) : splitForm.IsOrtho a (b + c) := by
  apply QuadraticMap.isOrtho_polarBilin.mp
  rw [QuadraticMap.polarBilin_apply_apply, QuadraticMap.polar_add_right, hab.polar_eq_zero,
    hac.polar_eq_zero, add_zero]

/-- An element of the actual real Spin group whose value is the
transvection Clifford word. -/
def isotropicLift (a b c : Vector) (t : ℝ) (ha : splitForm a = 0)
    (hb : splitForm b = 0) (hc : splitForm c = 1)
    (hab : splitForm.IsOrtho a b) (hac : splitForm.IsOrtho a c)
    (hbc : splitForm.IsOrtho b c) : Spin :=
  let hsum : splitForm (b + c) = 1 := by
    rw [QuadraticMap.isOrtho_def] at hbc
    rw [hbc, hb, hc, zero_add]
  vectorPair ((b + c) + t • a) (b + c)
      (add_isotropic_square t ha hsum (isOrtho_add hab hac)) hsum *
    vectorPair (c + (-t) • a) c (add_isotropic_square (-t) ha hc hac) hc

theorem isotropicLift_val (a b c : Vector) (t : ℝ) (ha : splitForm a = 0)
    (hb : splitForm b = 0) (hc : splitForm c = 1)
    (hab : splitForm.IsOrtho a b) (hac : splitForm.IsOrtho a c)
    (hbc : splitForm.IsOrtho b c) :
    (isotropicLift a b c t ha hb hc hab hac hbc).val = 1 + t • (ι a * ι b) := by
  have hsum : splitForm (b + c) = 1 := by
    rw [QuadraticMap.isOrtho_def] at hbc
    rw [hbc, hb, hc, zero_add]
  change (ι ((b + c) + t • a) * ι (b + c)) * (ι (c + (-t) • a) * ι c) = _
  have hp : ι ((b + c) + t • a) * ι (b + c) = 1 + t • (ι a * ι (b + c)) := by
    rw [map_add, add_mul, map_smul, smul_mul_assoc, vector_square_one hsum]
  have hm : ι (c + (-t) • a) * ι c = 1 + (-t) • (ι a * ι c) := by
    rw [map_add, add_mul, map_smul, smul_mul_assoc, vector_square_one hc]
  have hzero : (ι a * ι (b + c)) * (ι a * ι c) = 0 := by
    rw [← mul_assoc, isotropic_mul_mul ha (isOrtho_add hab hac), zero_mul]
  rw [hp, hm]
  simp only [mul_add, add_mul, one_mul, mul_one, smul_mul_assoc, mul_smul_comm,
    hzero, smul_zero, add_zero]
  rw [map_add, mul_add, smul_add, neg_smul]
  abel

private theorem bivector_commutator (a b x : Vector) :
    (ι a * ι b) * ι x - ι x * (ι a * ι b) =
      QuadraticMap.polar splitForm b x • ι a - QuadraticMap.polar splitForm a x • ι b := by
  calc
    _ = ι a * (ι b * ι x + ι x * ι b) - (ι a * ι x + ι x * ι a) * ι b := by
      noncomm_ring
    _ = _ := by
      rw [CliffordAlgebra.ι_mul_ι_add_swap (Q := splitForm) b x,
        CliffordAlgebra.ι_mul_ι_add_swap (Q := splitForm) a x,
        Algebra.algebraMap_eq_smul_one, Algebra.algebraMap_eq_smul_one,
        mul_smul_comm, smul_mul_assoc, mul_one, one_mul]

/-- The induced vector action is the isotropic orthogonal transvection. -/
theorem isotropicLift_action (a b c x : Vector) (t : ℝ) (ha : splitForm a = 0)
    (hb : splitForm b = 0) (hc : splitForm c = 1)
    (hab : splitForm.IsOrtho a b) (hac : splitForm.IsOrtho a c)
    (hbc : splitForm.IsOrtho b c) :
    D7SpinAction.vectorRepresentation (isotropicLift a b c t ha hb hc hab hac hbc) x =
      x + t • (QuadraticMap.polar splitForm b x • a - QuadraticMap.polar splitForm a x • b) := by
  let g := isotropicLift a b c t ha hb hc hab hac hbc
  let D := ι a * ι b
  let X := ι x
  have hDA : D * ι a = 0 := isotropic_mul_mul ha hab
  have hDB : D * ι b = 0 := by
    change (ι a * ι b) * ι b = 0
    rw [mul_assoc, isotropic_square hb, mul_zero]
  have hDD : D * D = 0 := by
    change D * (ι a * ι b) = 0
    rw [← mul_assoc, hDA, zero_mul]
  have hcomm : D * X - X * D =
      QuadraticMap.polar splitForm b x • ι a - QuadraticMap.polar splitForm a x • ι b :=
    bivector_commutator a b x
  have hquad : (D * X) * D = 0 := by
    calc
      _ = D * (D * X) - D * (D * X - X * D) := by noncomm_ring
      _ = 0 := by
        rw [← mul_assoc D D X, hDD, zero_mul, hcomm, mul_sub, mul_smul_comm, mul_smul_comm,
          hDA, hDB, smul_zero, smul_zero, sub_zero, sub_zero]
  have hg : (g.val : Cl) = 1 + t • D := isotropicLift_val a b c t ha hb hc hab hac hbc
  have hstar : star (g.val : Cl) = 1 + (-t) • D := by
    rw [hg, star_add, star_one, CliffordAlgebra.star_smul]
    change 1 + t • star (ι a * ι b) = _
    rw [star_mul, CliffordAlgebra.star_ι, CliffordAlgebra.star_ι, neg_mul_neg,
      CliffordAlgebra.ι_mul_ι_comm_of_isOrtho hab.symm, smul_neg, neg_smul]
  have hact := D7SpinAction.iota_vectorRepresentation g x
  change ι (D7SpinAction.vectorRepresentation g x) = (g.val : Cl) * X * star (g.val : Cl) at hact
  apply D7SpinAction.iota_injective
  rw [hact, hstar, hg]
  calc
    (1 + t • D) * X * (1 + (-t) • D) =
        X + t • (D * X) + (-t) • (X * D) + (-t) • (t • ((D * X) * D)) := by
      simp only [mul_add, add_mul, one_mul, mul_one, smul_mul_assoc, mul_smul_comm, smul_add]
      abel
    _ = X + t • (D * X - X * D) := by
      rw [hquad, smul_zero, smul_zero, add_zero, smul_sub, neg_smul]
      abel
    _ = _ := by rw [hcomm, map_add, map_smul, map_sub, map_smul, map_smul]

end

end GeometricUnity.D7SpinRootLifts
~~~

[Return to file index](#file-index)

## D7SpinOrientation.lean {#source-d7spinorientation-lean}

Proves that the real Spin vector action has determinant one.

~~~lean
import D7SpinAction
import Mathlib.LinearAlgebra.Transvection.Basic

/-!
# Orientation of the real Spin vector action

Twisted conjugation by a vector unit is a reflection of determinant
`-1`. On the subgroup generated by vector units the determinant is
the scalar by which the grade involution changes the unit. Spin
elements are even, so the twist disappears and the determinant is one.
-/

namespace GeometricUnity.D7SpinOrientation

open D7SpinAction (Vector Spin iota_injective vectorRepresentation iota_vectorRepresentation)
open WitnessW1 (Cl splitForm)
open CliffordAlgebra

noncomputable section

private abbrev iota := ι splitForm
private abbrev Lipschitz := ↥(lipschitzGroup splitForm)

private def twistedAction (u : Lipschitz) : Module.End ℝ Vector :=
  let conjugate := (LinearMap.mulLeftRight ℝ (involute (u.val : Cl), (↑u.val⁻¹ : Cl))).comp iota
  conjugate.codRestrictOfInjective iota iota_injective
    (fun x => lipschitzGroup.involute_act_ι_mem_range_ι u.prop x)

private theorem iota_twisted (u : Lipschitz) (x : Vector) :
    iota (twistedAction u x) = involute (u.val : Cl) * iota x * (↑u.val⁻¹ : Cl) :=
  LinearMap.codRestrictOfInjective_comp_apply _ _ _ _ x

private def twistedRepresentation : Representation ℝ Lipschitz Vector where
  toFun := twistedAction
  map_one' := by
    apply LinearMap.ext
    intro x
    apply iota_injective
    change iota (twistedAction 1 x) = iota x
    simp only [iota_twisted, Subgroup.coe_one, Units.val_one, map_one, inv_one, one_mul, mul_one]
  map_mul' u v := by
    apply LinearMap.ext
    intro x
    apply iota_injective
    change iota (twistedAction (u * v) x) = iota (twistedAction u (twistedAction v x))
    simp only [iota_twisted, Subgroup.coe_mul, Units.val_mul, map_mul, mul_inv_rev, mul_assoc]

private def orientation : Lipschitz →* ℝ :=
  LinearMap.det.comp twistedRepresentation

private theorem twisted_det_vector (u : Lipschitz) (a : Vector) (ha : iota a = (u.val : Cl)) :
    orientation u = -1 := by
  let : Invertible (u.val : Cl) := u.val.invertible
  let : Invertible (iota a) := by rwa [ha]
  let : Invertible (splitForm a) := invertibleOfInvertibleι splitForm a
  let d : Module.Dual ℝ Vector := -(⅟(splitForm a) • splitForm.polarBilin a)
  have hr : twistedAction u = LinearMap.transvection d a := by
    apply LinearMap.ext
    intro x
    apply iota_injective
    rw [iota_twisted]
    simp_rw [← invOf_units u.val, ← ha, involute_ι, neg_mul,
      ι_mul_ι_mul_invOf_ι splitForm a x, ← map_neg]
    congr 1
    change -((⅟(splitForm a) * QuadraticMap.polar splitForm a x) • a - x) = x + d x • a
    simp only [d, LinearMap.neg_apply, LinearMap.smul_apply, QuadraticMap.polarBilin_apply_apply,
      smul_eq_mul, neg_smul, sub_eq_add_neg, neg_add, neg_neg]
    exact add_comm _ _
  change (twistedAction u).det = _
  rw [hr, LinearMap.transvection.det]
  change 1 + -(⅟(splitForm a) * QuadraticMap.polar splitForm a a) = -1
  rw [QuadraticMap.polar_self, two_smul, mul_add, invOf_mul_self]
  norm_num

private theorem involute_orientation (u : Lipschitz) :
    involute (u.val : Cl) = orientation u • (u.val : Cl) := by
  let P (v : Clˣ) (h : v ∈ lipschitzGroup splitForm) :=
    involute (v : Cl) = orientation ⟨v, h⟩ • (v : Cl)
  change P u.val u.prop
  refine Subgroup.closure_induction (p := P) ?_ ?_ ?_ ?_ u.prop
  · intro v hv
    let U : Lipschitz := ⟨v, Subgroup.subset_closure hv⟩
    obtain ⟨a, ha⟩ := hv
    change involute (v : Cl) = orientation U • (v : Cl)
    rw [twisted_det_vector U a ha, ← ha, involute_ι, neg_one_smul]
  · change involute (1 : Cl) = orientation 1 • (1 : Cl)
    rw [map_one, map_one, one_smul]
  · intro v w hv hw ihv ihw
    let U : Lipschitz := ⟨v, hv⟩
    let W : Lipschitz := ⟨w, hw⟩
    change involute ((v : Cl) * (w : Cl)) = orientation (U * W) • ((v : Cl) * (w : Cl))
    change involute (v : Cl) = orientation U • (v : Cl) at ihv
    change involute (w : Cl) = orientation W • (w : Cl) at ihw
    rw [map_mul, ihv, ihw, map_mul, smul_mul_assoc, mul_smul_comm, smul_smul]
  · intro v hv ih
    let U : Lipschitz := ⟨v, hv⟩
    change involute (↑v⁻¹ : Cl) = orientation (U⁻¹) • (↑v⁻¹ : Cl)
    change involute (v : Cl) = orientation U • (v : Cl) at ih
    have hs : orientation (U⁻¹) * orientation U = 1 := by
      rw [← map_mul, inv_mul_cancel, map_one]
    have hvv : involute (v : Cl) * involute (↑v⁻¹ : Cl) = 1 := by
      rw [← map_mul, v.mul_inv, map_one]
    calc
      _ = ((orientation (U⁻¹) • (↑v⁻¹ : Cl)) * involute (v : Cl)) * involute (↑v⁻¹ : Cl) := by
        rw [ih, smul_mul_assoc, mul_smul_comm, smul_smul, hs, v.inv_mul, one_smul, one_mul]
      _ = _ := by rw [mul_assoc, hvv, mul_one]

/-- The actual real Spin vector representation has determinant one. -/
theorem vectorRepresentation_det (g : Spin) : (vectorRepresentation g).det = 1 := by
  let v := spinGroup.toUnits g
  have hg : (v : Cl) ∈ spinGroup splitForm := g.prop
  let U : Lipschitz := ⟨v, spinGroup.units_mem_lipschitzGroup hg⟩
  have he : twistedAction U = vectorRepresentation g := by
    apply LinearMap.ext
    intro x
    apply iota_injective
    rw [iota_twisted, iota_vectorRepresentation]
    change involute (v : Cl) * iota x * (↑v⁻¹ : Cl) = (v : Cl) * iota x * (↑v⁻¹ : Cl)
    rw [spinGroup.involute_eq hg]
  have h := involute_orientation U
  change involute (v : Cl) = (twistedAction U).det • (v : Cl) at h
  rw [spinGroup.involute_eq hg, he] at h
  have hscalar := congrArg (fun a : Cl => a * (↑v⁻¹ : Cl)) h
  rw [smul_mul_assoc, v.mul_inv, ← Algebra.algebraMap_eq_smul_one] at hscalar
  exact ((algebraMap ℝ Cl).injective (by simpa only [map_one] using hscalar)).symm

end

end GeometricUnity.D7SpinOrientation
~~~

[Return to file index](#file-index)

## D7RootInterpolation.lean {#source-d7rootinterpolation-lean}

Uses polynomial interpolation to place complex split-root tensor actions in the span of real Spin actions.

~~~lean
import D7SpinNullFrame
import D7VectorGrades
import Mathlib.Algebra.Polynomial.Roots
import Mathlib.LinearAlgebra.Dual.Lemmas

/-!
# Interpolation of split root actions

Real Spin lifts give the paired tensor actions at real parameters.
Exterior powers and tensor products make these actions polynomial in the
parameter. A linear functional annihilating the real action span then
annihilates the action at every complex parameter.
-/

namespace GeometricUnity.D7RootInterpolation

open D7Exterior D7VectorGrades D7SpinNullFrame
open scoped BigOperators TensorProduct Polynomial

noncomputable section

private def polynomialCurves (E : Type*) [AddCommGroup E] [Module ℂ E] :
    Submodule ℂ (ℂ → E) :=
  Submodule.span ℂ {f | ∃ (p : ℂ[X]) (v : E), f = fun z => p.eval z • v}

section Curves

variable {E F G : Type*} [AddCommGroup E] [Module ℂ E]
variable [AddCommGroup F] [Module ℂ F] [AddCommGroup G] [Module ℂ G]

private theorem polynomialTerm (p : ℂ[X]) (v : E) :
    (fun z => p.eval z • v) ∈ polynomialCurves E :=
  Submodule.subset_span ⟨p, v, rfl⟩

private theorem curve_map (L : E →ₗ[ℂ] F) {f : ℂ → E} (hf : f ∈ polynomialCurves E) :
    (fun z => L (f z)) ∈ polynomialCurves F := by
  let T : (ℂ → E) →ₗ[ℂ] (ℂ → F) := LinearMap.pi fun z => L.comp (LinearMap.proj z)
  have h : polynomialCurves E ≤ (polynomialCurves F).comap T := by
    apply Submodule.span_le.mpr
    rintro _ ⟨p, v, rfl⟩
    change (fun z => L (p.eval z • v)) ∈ polynomialCurves F
    simpa only [map_smul] using polynomialTerm p (L v)
  exact h hf

private def pointwiseBilinear (L : E →ₗ[ℂ] F →ₗ[ℂ] G) :
    (ℂ → E) →ₗ[ℂ] (ℂ → F) →ₗ[ℂ] (ℂ → G) :=
  LinearMap.mk₂ ℂ (fun f g z => L (f z) (g z))
    (fun _ _ _ => funext fun _ => by simp)
    (fun _ _ _ => funext fun _ => by simp)
    (fun _ _ _ => funext fun _ => by simp)
    (fun _ _ _ => funext fun _ => by simp)

private theorem curve_bilinear (L : E →ₗ[ℂ] F →ₗ[ℂ] G) {f : ℂ → E} {g : ℂ → F}
    (hf : f ∈ polynomialCurves E) (hg : g ∈ polynomialCurves F) :
    (fun z => L (f z) (g z)) ∈ polynomialCurves G := by
  let T := pointwiseBilinear L
  change T f g ∈ polynomialCurves G
  refine Submodule.span_induction₂ (p := fun f g _ _ => T f g ∈ polynomialCurves G)
    ?_ ?_ ?_ ?_ ?_ ?_ ?_ hf hg
  · rintro _ _ ⟨p, x, rfl⟩ ⟨q, y, rfl⟩
    change (fun z => L (p.eval z • x) (q.eval z • y)) ∈ polynomialCurves G
    simpa only [map_smul, LinearMap.smul_apply, smul_smul, Polynomial.eval_mul]
      using polynomialTerm (q * p) (L x y)
  · intro g _
    rw [map_zero, LinearMap.zero_apply]
    exact (polynomialCurves G).zero_mem
  · intro f _
    rw [map_zero]
    exact (polynomialCurves G).zero_mem
  · intro f₁ f₂ g _ _ _ h₁ h₂
    rw [map_add, LinearMap.add_apply]
    exact (polynomialCurves G).add_mem h₁ h₂
  · intro f g₁ g₂ _ _ _ h₁ h₂
    rw [map_add]
    exact (polynomialCurves G).add_mem h₁ h₂
  · intro r f g _ _ h
    rw [map_smul, LinearMap.smul_apply]
    exact (polynomialCurves G).smul_mem r h
  · intro r f g _ _ h
    rw [map_smul]
    exact (polynomialCurves G).smul_mem r h

private theorem scalar_polynomial {f : ℂ → ℂ} (hf : f ∈ polynomialCurves ℂ) :
    ∃ p : ℂ[X], f = p.eval := by
  induction hf using Submodule.span_induction with
  | mem f h =>
    obtain ⟨p, v, rfl⟩ := h
    exact ⟨p * Polynomial.C v, funext fun z => by simp [smul_eq_mul]⟩
  | zero => exact ⟨0, funext fun z => by simp⟩
  | add f g _ _ hf hg =>
    obtain ⟨p, rfl⟩ := hf
    obtain ⟨q, rfl⟩ := hg
    exact ⟨p + q, funext fun z => by simp⟩
  | smul r f _ hf =>
    obtain ⟨p, rfl⟩ := hf
    exact ⟨Polynomial.C r * p, funext fun z => by simp [smul_eq_mul]⟩

private theorem curve_mem_of_real {f : ℂ → E} (hf : f ∈ polynomialCurves E)
    (S : Submodule ℂ E) (hr : ∀ r : ℝ, f (r : ℂ) ∈ S) (z : ℂ) : f z ∈ S := by
  apply (Subspace.forall_mem_dualAnnihilator_apply_eq_zero_iff S (f z)).mp
  intro L hL
  obtain ⟨p, hp⟩ := scalar_polynomial (curve_map L hf)
  have hroot : Set.range Complex.ofReal ⊆ {w | p.IsRoot w} := by
    rintro _ ⟨r, rfl⟩
    change p.eval (r : ℂ) = 0
    rw [← congrFun hp (r : ℂ)]
    exact (Submodule.mem_dualAnnihilator L).mp hL _ (hr r)
  have hp0 := p.eq_zero_of_infinite_isRoot
    ((Set.infinite_range_of_injective Complex.ofReal_injective).mono hroot)
  rw [congrFun hp z, hp0, Polynomial.eval_zero]

end Curves

private theorem exterior_curve_on_blade (N : Module.End ℂ Space) (k : ℕ)
    (v : Fin k → Space) :
    (fun z => exteriorPower.map k (LinearMap.id + z • N) (exteriorPower.ιMulti ℂ k v)) ∈
      polynomialCurves (Ext k) := by
  classical
  let blade := exteriorPower.ιMulti ℂ k (M := Space)
  let vN : Fin k → Space := fun i => N (v i)
  have h (z : ℂ) : exteriorPower.map k (LinearMap.id + z • N) (blade v) =
      ∑ s : Finset (Fin k), z ^ s.card • blade (s.piecewise vN v) := by
    rw [exteriorPower.map_apply_ιMulti]
    change blade (fun i => (LinearMap.id + z • N : Module.End ℂ Space) (v i)) = _
    have hv : (fun i => (LinearMap.id + z • N : Module.End ℂ Space) (v i)) =
        (fun i => z • vN i) + v := by
      funext i
      exact add_comm (v i) (z • N (v i))
    rw [hv]
    change blade ((fun i => z • vN i) + v) = _
    rw [AlternatingMap.map_add_univ]
    apply Finset.sum_congr rfl
    intro s _
    rw [show s.piecewise (fun i => z • vN i) v =
        s.piecewise (fun i => z • s.piecewise vN v i) (s.piecewise vN v) by
      funext i
      by_cases hi : i ∈ s <;> simp [Finset.piecewise, hi]]
    exact (blade.toMultilinearMap.map_piecewise_smul (fun _ => z) (s.piecewise vN v) s).trans
      (by rw [Finset.prod_const]; rfl)
  have hsum : (∑ s : Finset (Fin k), fun z : ℂ => z ^ s.card • blade (s.piecewise vN v)) ∈
      polynomialCurves (Ext k) :=
    Submodule.sum_mem _ fun s _ => by
      simpa only [Polynomial.eval_pow, Polynomial.eval_X] using
        polynomialTerm (Polynomial.X ^ s.card) (blade (s.piecewise vN v))
  have he : (fun z : ℂ => exteriorPower.map k (LinearMap.id + z • N) (blade v)) =
      ∑ s : Finset (Fin k), fun z => z ^ s.card • blade (s.piecewise vN v) := by
    funext z
    rw [Finset.sum_apply, h]
  change (fun z => exteriorPower.map k (LinearMap.id + z • N) (blade v)) ∈ _
  rw [he]
  exact hsum

private theorem exterior_curve (N : Module.End ℂ Space) (k : ℕ) :
    (fun z => exteriorPower.map k (LinearMap.id + z • N)) ∈
      polynomialCurves (Module.End ℂ (Ext k)) := by
  classical
  let b := axisBasis.exteriorPower k
  let F (z : ℂ) := exteriorPower.map k (LinearMap.id + z • N)
  have hx (i : Index k) : (fun z => F z (b i)) ∈ polynomialCurves (Ext k) := by
    change (fun z => F z ((axisBasis.exteriorPower k) i)) ∈ _
    rw [exteriorPower.basis_apply]
    exact exterior_curve_on_blade N k _
  have he : F = ∑ i : Index k, fun z => (b.coord i).smulRight (F z (b i)) := by
    funext z
    rw [Finset.sum_apply]
    apply b.ext
    intro j
    symm
    simp only [LinearMap.sum_apply, LinearMap.smulRight_apply, Module.Basis.coord_apply,
      Module.Basis.repr_self, Finsupp.single_apply, ite_smul, one_smul, zero_smul]
    simp
  change F ∈ _
  rw [he]
  exact Submodule.sum_mem _ fun i _ => curve_map (LinearMap.smulRightₗ (b.coord i)) (hx i)

local instance exteriorTensor_addCommGroup (k l : ℕ) : AddCommGroup (Ext k ⊗[ℂ] Ext l) :=
  @TensorProduct.addCommGroup ℂ _ (Ext k) (Ext l) (⋀[ℂ]^k Space).addCommGroup _ _ _

/-- The action on a tensor product of two exterior powers. -/
def exteriorTensorMap (k l : ℕ) (f : Module.End ℂ Space) : Module.End ℂ (Ext k ⊗[ℂ] Ext l) :=
  TensorProduct.map (exteriorPower.map k f) (exteriorPower.map l f)

private theorem exteriorTensor_curve (N : Module.End ℂ Space) (k l : ℕ) :
    (fun z => exteriorTensorMap k l (LinearMap.id + z • N)) ∈
      polynomialCurves (Module.End ℂ (Ext k ⊗[ℂ] Ext l)) :=
  curve_bilinear (TensorProduct.mapBilinear (R := ℂ) (RingHom.id ℂ) (Ext k) (Ext l) (Ext k) (Ext l))
    (exterior_curve N k) (exterior_curve N l)

private theorem root_affine (a b : Axis) (z : ℂ) :
    rootGroup z a (pairedAxis b) b (pairedAxis a) =
      LinearMap.id + z • (rootGroup 1 a (pairedAxis b) b (pairedAxis a) - LinearMap.id) := by
  unfold rootGroup
  module

/-- For the paired tensor actions needed in the dimension calculation,
every complex split root parameter lies in the complex linear span of
pairs of actual real Spin actions. -/
theorem rootGroup_tensorActions_mem_spin_span (a b : Axis) (hab : pairIndex a ≠ pairIndex b)
    (k l m n : ℕ) (z : ℂ) :
    (exteriorTensorMap k l (rootGroup z a (pairedAxis b) b (pairedAxis a)),
      exteriorTensorMap m n (rootGroup z a (pairedAxis b) b (pairedAxis a))) ∈
    Submodule.span ℂ (Set.range fun g : D7SpinAction.Spin =>
      (exteriorTensorMap k l (complexNullAction g), exteriorTensorMap m n (complexNullAction g))) := by
  let U := Module.End ℂ (Ext k ⊗[ℂ] Ext l)
  let W := Module.End ℂ (Ext m ⊗[ℂ] Ext n)
  let F (w : ℂ) : U × W :=
    (exteriorTensorMap k l (rootGroup w a (pairedAxis b) b (pairedAxis a)),
      exteriorTensorMap m n (rootGroup w a (pairedAxis b) b (pairedAxis a)))
  let S : Submodule ℂ (U × W) :=
    Submodule.span ℂ (Set.range fun g : D7SpinAction.Spin =>
      (exteriorTensorMap k l (complexNullAction g), exteriorTensorMap m n (complexNullAction g)))
  have hF : F ∈ polynomialCurves (U × W) := by
    let N := rootGroup 1 a (pairedAxis b) b (pairedAxis a) - LinearMap.id
    have h₁ := curve_map (LinearMap.inl ℂ U W) (exteriorTensor_curve N k l)
    have h₂ := curve_map (LinearMap.inr ℂ U W) (exteriorTensor_curve N m n)
    have he : F = (fun w => LinearMap.inl ℂ U W (exteriorTensorMap k l (LinearMap.id + w • N))) +
        (fun w => LinearMap.inr ℂ U W (exteriorTensorMap m n (LinearMap.id + w • N))) := by
      funext w
      change (exteriorTensorMap k l (rootGroup w a (pairedAxis b) b (pairedAxis a)),
        exteriorTensorMap m n (rootGroup w a (pairedAxis b) b (pairedAxis a))) = _
      rw [root_affine a b w]
      simp [N]
    rw [he]
    exact (polynomialCurves (U × W)).add_mem h₁ h₂
  refine curve_mem_of_real hF S ?_ z
  intro r
  obtain ⟨g, hg⟩ := exists_rootGroup_lift a b hab r
  exact Submodule.subset_span ⟨g, congrArg (fun f =>
    (exteriorTensorMap k l f, exteriorTensorMap m n f)) hg⟩

/-- All split root maps with arbitrary complex parameters. -/
def splitRootMaps : Set (Module.End ℂ Space) :=
  {f | ∃ (a b : Axis) (z : ℂ), pairIndex a ≠ pairIndex b ∧
    f = rootGroup z a (pairedAxis b) b (pairedAxis a)}

private def exteriorTensorHom (k l : ℕ) : Module.End ℂ Space →*
    Module.End ℂ (Ext k ⊗[ℂ] Ext l) where
  toFun := exteriorTensorMap k l
  map_one' := by simp only [exteriorTensorMap, Module.End.one_eq_id, exteriorPower.map_id,
    TensorProduct.map_id]
  map_mul' f g := by
    simp only [exteriorTensorMap, Module.End.mul_eq_comp, exteriorPower.map_comp]
    exact TensorProduct.map_comp (exteriorPower.map k f) (exteriorPower.map l f)
      (exteriorPower.map k g) (exteriorPower.map l g)

set_option maxHeartbeats 800000 in
/-- The paired action span also contains the action of every finite
product of complex split root maps. -/
theorem rootClosure_tensorActions_mem_spin_span (k l m n : ℕ) {f : Module.End ℂ Space}
    (hf : f ∈ Submonoid.closure splitRootMaps) :
    (exteriorTensorMap k l f, exteriorTensorMap m n f) ∈
      Submodule.span ℂ (Set.range fun g : D7SpinAction.Spin =>
        (exteriorTensorMap k l (complexNullAction g),
          exteriorTensorMap m n (complexNullAction g))) := by
  let X := Module.End ℂ (Ext k ⊗[ℂ] Ext l) × Module.End ℂ (Ext m ⊗[ℂ] Ext n)
  let paired : Module.End ℂ Space →* X := (exteriorTensorHom k l).prod (exteriorTensorHom m n)
  let spin : D7SpinAction.Spin →* X := paired.comp complexNullAction
  let A : Subalgebra ℂ X := Algebra.adjoin ℂ (Set.range spin)
  have hA : A.toSubmodule = Submodule.span ℂ (Set.range spin) := by
    let S := MonoidHom.mrange spin
    change (Algebra.adjoin ℂ (S : Set X)).toSubmodule = Submodule.span ℂ (S : Set X)
    rw [Algebra.adjoin_eq_span, S.closure_eq]
  have hroots : splitRootMaps ⊆ A.toSubmonoid.comap paired := by
    rintro _ ⟨a, b, z, hab, rfl⟩
    change paired (rootGroup z a (pairedAxis b) b (pairedAxis a)) ∈ A.toSubmodule
    rw [hA]
    exact rootGroup_tensorActions_mem_spin_span a b hab k l m n z
  change paired f ∈ Submodule.span ℂ (Set.range spin)
  rw [← hA]
  exact (Submonoid.closure_le.mpr hroots) hf

end

end GeometricUnity.D7RootInterpolation
~~~

[Return to file index](#file-index)

## D7RootGeneration.lean {#source-d7rootgeneration-lean}

Proves generation of the complex split special orthogonal action by split roots and extends the action-span result.

~~~lean
import D7RootInterpolation
import Mathlib.Analysis.Complex.Polynomial.Basic

/-!
# Generation of the split special orthogonal action

Root operations change two null coordinates at a time. The elimination
uses these operations to restore the two columns of a hyperbolic pair
while keeping every previously restored pair fixed.
-/

namespace GeometricUnity.D7RootGeneration

open D7Exterior D7SpinNullFrame D7RootInterpolation
open scoped BigOperators

noncomputable section

private abbrev End := Module.End ℂ Space
private abbrev e := axisBasis
local notation "mate" => pairedAxis
local notation "B" => D7Hodge.splitMetric

private theorem basis_apply (a j : Axis) : e a j = if j = a then 1 else 0 := by
  simp only [axisBasis, Pi.basisFun_apply, Pi.single_apply]

private theorem basis_coord (a : Axis) (x : Space) : e.coord a x = x a := by
  simp [axisBasis, Module.Basis.coord_apply, Pi.basisFun_repr]

private theorem split_apply (x y : Space) :
    B x y = ∑ i : Pair, (x (plusAxis i) * y (minusAxis i) + x (minusAxis i) * y (plusAxis i)) :=
  D7Hodge.splitMetric_apply x y

private theorem metric_symm (x y : Space) : B x y = B y x := by
  rw [split_apply, split_apply]
  apply Finset.sum_congr rfl
  intro i _
  ring

private theorem plus_ne_minus (i j : Pair) : plusAxis i ≠ minusAxis j := by
  intro h
  have he := congrArg Fin.val h
  change 2 * i.val = 2 * j.val + 1 at he
  omega

private theorem plus_eq (i j : Pair) : plusAxis i = plusAxis j ↔ i = j := by
  constructor
  · intro h
    simpa only [pairIndex_plus] using congrArg pairIndex h
  · exact congrArg plusAxis

private theorem minus_eq (i j : Pair) : minusAxis i = minusAxis j ↔ i = j := by
  constructor
  · intro h
    simpa only [pairIndex_minus] using congrArg pairIndex h
  · exact congrArg minusAxis

@[simp] private theorem metric_basis (a : Axis) (x : Space) : B (e a) x = x (mate a) := by
  rcases null_axis_cases a with h | h
  · rw [h, pairedAxis_plus, split_apply]
    simp only [basis_apply, plus_eq, Ne.symm (plus_ne_minus _ _), if_false, zero_mul, add_zero,
      ite_mul, one_mul, Finset.sum_ite_eq', Finset.mem_univ, if_true]
  · rw [h, pairedAxis_minus, split_apply]
    simp only [basis_apply, minus_eq, plus_ne_minus, if_false, zero_mul, zero_add,
      ite_mul, one_mul, Finset.sum_ite_eq', Finset.mem_univ, if_true]

@[simp] private theorem metric_basis_right (a : Axis) (x : Space) : B x (e a) = x (mate a) := by
  rw [metric_symm x, metric_basis]

private def root (a b : Axis) (t : ℂ) : End := rootGroup t a (mate b) b (mate a)

private theorem root_mem (a b : Axis) (hab : pairIndex a ≠ pairIndex b) (t : ℂ) :
    root a b t ∈ Submonoid.closure splitRootMaps :=
  Submonoid.subset_closure ⟨a, b, t, hab, rfl⟩

private theorem root_apply (a b : Axis) (t : ℂ) (x : Space) :
    root a b t x = x + (t * x (mate b)) • e a - (t * x (mate a)) • e b := by
  change x + t • (e.coord (mate b) x • e a) - t • (e.coord (mate a) x • e b) = _
  rw [basis_coord, basis_coord, smul_smul, smul_smul]

private theorem root_coord (a b : Axis) (t : ℂ) (x : Space) (j : Axis) :
    root a b t x j = x j + (if j = a then t * x (mate b) else 0) -
      (if j = b then t * x (mate a) else 0) := by
  rw [root_apply]
  simp only [Pi.sub_apply, Pi.add_apply, Pi.smul_apply, smul_eq_mul, basis_apply, mul_ite,
    mul_one, mul_zero]

private theorem axis_ne_of_pair_ne {a b : Axis} (h : pairIndex a ≠ pairIndex b) : a ≠ b :=
  fun he => h (congrArg pairIndex he)

private theorem root_mate_left (a b : Axis) (hab : pairIndex a ≠ pairIndex b) (t : ℂ) (x : Space) :
    root a b t x (mate a) = x (mate a) := by
  have hn : mate a ≠ b := axis_ne_of_pair_ne (by simpa only [pairedAxis_pairIndex] using hab)
  simp only [root_coord, if_neg (pairedAxis_ne a), if_neg hn, add_zero, sub_zero]

private theorem root_mate_right (a b : Axis) (hab : pairIndex a ≠ pairIndex b) (t : ℂ) (x : Space) :
    root a b t x (mate b) = x (mate b) := by
  have hn : mate b ≠ a := axis_ne_of_pair_ne (by simpa only [pairedAxis_pairIndex] using hab.symm)
  simp only [root_coord, if_neg (pairedAxis_ne b), if_neg hn, add_zero, sub_zero]

private theorem root_inv_mul (a b : Axis) (hab : pairIndex a ≠ pairIndex b) (t : ℂ) :
    root a b (-t) * root a b t = 1 := by
  apply LinearMap.ext
  intro x
  funext j
  change root a b (-t) (root a b t x) j = x j
  rw [root_coord, root_mate_left a b hab, root_mate_right a b hab, root_coord]
  have hn := axis_ne_of_pair_ne hab
  by_cases ha : j = a <;> by_cases hb : j = b <;> simp [ha, hb, hn, hn.symm]

private def rootUnit (a b : Axis) (hab : pairIndex a ≠ pairIndex b) (t : ℂ) : Endˣ :=
  ⟨root a b t, root a b (-t), by simpa only [neg_neg] using root_inv_mul a b hab (-t),
    root_inv_mul a b hab t⟩

private theorem root_preserves (a b : Axis) (hab : pairIndex a ≠ pairIndex b)
    (t : ℂ) (x y : Space) : B (root a b t x) (root a b t y) = B x y := by
  have hm : mate a ≠ b := axis_ne_of_pair_ne (by simpa only [pairedAxis_pairIndex] using hab)
  have hn : mate b ≠ a := axis_ne_of_pair_ne (by simpa only [pairedAxis_pairIndex] using hab.symm)
  simp only [root_apply, map_add, map_sub, map_smul, LinearMap.add_apply, LinearMap.sub_apply,
    LinearMap.smul_apply, metric_basis, metric_basis_right, basis_apply, if_neg (pairedAxis_ne a),
    if_neg (pairedAxis_ne b), if_neg hm, if_neg hn, smul_eq_mul]
  ring

private theorem root_det (a b : Axis) (hab : pairIndex a ≠ pairIndex b) (t : ℂ) :
    (root a b t).det = 1 := by
  have hm : mate a ≠ b := axis_ne_of_pair_ne (by simpa only [pairedAxis_pairIndex] using hab)
  have hn : mate b ≠ a := axis_ne_of_pair_ne (by simpa only [pairedAxis_pairIndex] using hab.symm)
  let T := LinearMap.transvection (e.coord (mate b)) (t • e a)
  let U := LinearMap.transvection (e.coord (mate a)) ((-t) • e b)
  have he : T * U = root a b t := by
    apply LinearMap.ext
    intro x
    funext j
    have hU : U x = x + e.coord (mate a) x • ((-t) • e b) := rfl
    change (T (U x)) j = root a b t x j
    change ((U x) + e.coord (mate b) (U x) • (t • e a)) j = _
    rw [hU, basis_coord, basis_coord, root_coord]
    simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul, basis_apply, if_neg (pairedAxis_ne b),
      mul_zero, add_zero, mul_ite, mul_one]
    simp only [mul_comm (x (mate b)) t]
    by_cases hb : j = b
    · simp only [if_pos hb, mul_neg, sub_eq_add_neg, mul_comm (x (mate a)) t]
      abel
    · simp only [if_neg hb, add_zero, sub_zero]
  rw [← he, map_mul]
  simp [T, U, hm, hn]

private abbrev Words := Submonoid.closure splitRootMaps

private theorem words_special : Words ≤ splitSpecialOrthogonal := by
  apply Submonoid.closure_le.mpr
  rintro _ ⟨a, b, t, hab, rfl⟩
  refine ⟨root_det a b hab t, fun x y => ?_⟩
  exact (D7Hodge.splitMetric_apply _ _).symm.trans
    ((root_preserves a b hab t x y).trans (D7Hodge.splitMetric_apply _ _))

private def fixesOutside (S : Finset Pair) (f : End) : Prop :=
  ∀ a, pairIndex a ∉ S → f (e a) = e a

private def localWords (S : Finset Pair) : Subgroup Endˣ where
  carrier := {u | (u : End) ∈ Words ∧ (↑u⁻¹ : End) ∈ Words ∧ fixesOutside S u}
  one_mem' := ⟨Words.one_mem, by rw [inv_one]; exact Words.one_mem, fun _ _ => rfl⟩
  mul_mem' {u v} hu hv := by
    refine ⟨Words.mul_mem hu.1 hv.1, ?_, fun a ha => ?_⟩
    · rw [mul_inv_rev, Units.val_mul]
      exact Words.mul_mem hv.2.1 hu.2.1
    · change (u : End) ((v : End) (e a)) = e a
      rw [hv.2.2 a ha, hu.2.2 a ha]
  inv_mem' {u} hu := by
    refine ⟨hu.2.1, by rw [inv_inv]; exact hu.1, fun a ha => ?_⟩
    have h := congrArg (fun x => (↑u⁻¹ : End) x) (hu.2.2 a ha)
    change (↑u⁻¹ : End) ((u : End) (e a)) = _ at h
    change ((↑u⁻¹ : End) * (u : End)) (e a) = _ at h
    rw [u.inv_mul] at h
    exact h.symm

private theorem rootUnit_mem_local (S : Finset Pair) (a b : Axis)
    (ha : pairIndex a ∈ S) (hb : pairIndex b ∈ S) (hab : pairIndex a ≠ pairIndex b) (t : ℂ) :
    rootUnit a b hab t ∈ localWords S := by
  refine ⟨root_mem a b hab t, root_mem a b hab (-t), fun j hj => ?_⟩
  change root a b t (e j) = e j
  have h₁ : mate a ≠ j := fun h => hj (by simpa only [← h, pairedAxis_pairIndex] using ha)
  have h₂ : mate b ≠ j := fun h => hj (by simpa only [← h, pairedAxis_pairIndex] using hb)
  simp only [root_apply, basis_apply, if_neg h₁, if_neg h₂, mul_zero, zero_smul, add_zero, sub_zero]

private theorem local_preserves {S : Finset Pair} (u : localWords S) (x y : Space) :
    B (u.val.val x) (u.val.val y) = B x y := by
  have hu := words_special u.prop.1
  exact (D7Hodge.splitMetric_apply _ _).trans (hu.2 x y |>.trans
    (D7Hodge.splitMetric_apply _ _).symm)

private abbrev act {S : Finset Pair} (u : localWords S) : End := u.val.val

private def localRoot {S : Finset Pair} (a b : Axis) (ha : pairIndex a ∈ S)
    (hb : pairIndex b ∈ S) (hab : pairIndex a ≠ pairIndex b) (t : ℂ) : localWords S :=
  ⟨rootUnit a b hab t, rootUnit_mem_local S a b ha hb hab t⟩

private theorem act_root {S : Finset Pair} (a b : Axis) (ha : pairIndex a ∈ S)
    (hb : pairIndex b ∈ S) (hab : pairIndex a ≠ pairIndex b) (t : ℂ) :
    act (localRoot a b ha hb hab t) = root a b t := rfl

private theorem act_mul {S : Finset Pair} (u v : localWords S) (x : Space) :
    act (u * v) x = act u (act v x) := rfl

private def supported (S : Finset Pair) (x : Space) : Prop :=
  ∀ j, pairIndex j ∉ S → x j = 0

private theorem supported_map {S : Finset Pair} {f : End}
    (hf : ∀ x y, B (f x) (f y) = B x y) (hfix : fixesOutside S f)
    {x : Space} (hx : supported S x) : supported S (f x) := by
  intro j hj
  have h := hf (e (mate j)) x
  rw [hfix (mate j) (by simpa only [pairedAxis_pairIndex] using hj),
    metric_basis, metric_basis, pairedAxis_pairedAxis, hx j hj] at h
  exact h

private theorem local_supported {S : Finset Pair} (u : localWords S)
    {x : Space} (hx : supported S x) : supported S (act u x) :=
  supported_map (local_preserves u) u.prop.2.2 hx

private theorem basis_supported {S : Finset Pair} {a : Axis} (ha : pairIndex a ∈ S) :
    supported S (e a) := by
  intro j hj
  rw [basis_apply, if_neg]
  exact fun he => hj (he ▸ ha)

private theorem axis_cases {p j : Axis} (h : pairIndex j = pairIndex p) :
    j = p ∨ j = mate p := by
  rcases null_axis_cases p with hp | hp <;> rcases null_axis_cases j with hj | hj
  · left
    rw [hj, h, ← hp]
  · right
    rw [hj, h, hp, pairedAxis_plus, pairIndex_plus]
  · right
    rw [hj, h, hp, pairedAxis_minus, pairIndex_minus]
  · left
    rw [hj, h, ← hp]

private theorem eq_two_axes {x : Space} (p : Axis)
    (h : ∀ j, pairIndex j ≠ pairIndex p → x j = 0) :
    x = x p • e p + x (mate p) • e (mate p) := by
  funext j
  by_cases hj : pairIndex j = pairIndex p
  · rcases axis_cases hj with h | h
    · simp [h, basis_apply, (pairedAxis_ne p).symm]
    · simp [h, basis_apply, pairedAxis_ne p]
  · rw [h j hj]
    have hp := axis_ne_of_pair_ne hj
    have hm : j ≠ mate p := axis_ne_of_pair_ne (by simpa only [pairedAxis_pairIndex] using hj)
    simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul, basis_apply, if_neg hp, if_neg hm,
      mul_zero, add_zero]

private theorem metric_two_axes (p : Axis) (a b c d : ℂ) :
    B (a • e p + b • e (mate p)) (c • e p + d • e (mate p)) = a * d + b * c := by
  simp [basis_apply, pairedAxis_ne p, (pairedAxis_ne p).symm]
private theorem isotropic_axis {x : Space} {p : Axis} (hx : B x x = 0) (hp : x p ≠ 0)
    (hzero : ∀ j, pairIndex j ≠ pairIndex p → x j = 0) : x = x p • e p := by
  have h := eq_two_axes p hzero
  have hh : B (x p • e p + x (mate p) • e (mate p))
      (x p • e p + x (mate p) • e (mate p)) = 0 := by rw [← h, hx]
  rw [metric_two_axes] at hh
  have hz : (2 : ℂ) * x p * x (mate p) = 0 := by linear_combination hh
  exact h.trans (by simp [(mul_eq_zero.mp hz).resolve_left (mul_ne_zero (by norm_num) hp)])

private theorem clear_coordinates {S : Finset Pair} {d : Axis} (hd : pairIndex d ∈ S)
    (x : Space) (hx : x d ≠ 0) (T : Finset Axis)
    (hT : ∀ q ∈ T, pairIndex q ∈ S ∧ pairIndex q ≠ pairIndex d) :
    ∃ u : localWords S, act u x d = x d ∧ act u (e (mate d)) = e (mate d) ∧
      ∀ q ∈ T, act u x q = 0 := by
  induction T using Finset.induction_on with
  | empty => exact ⟨1, rfl, rfl, by simp⟩
  | @insert q T hq ih =>
    have h := hT q (Finset.mem_insert_self q T)
    obtain ⟨u, hu, hfix, hz⟩ := ih (fun j hj => hT j (Finset.mem_insert_of_mem hj))
    let t := -(act u x q) / act u x d
    let v := localRoot q (mate d) h.1 (by simpa only [pairedAxis_pairIndex] using hd)
      (by simpa only [pairedAxis_pairIndex] using h.2) t
    have hv : act v = root q (mate d) t := rfl
    have hm : mate d ≠ q :=
      axis_ne_of_pair_ne (by simpa only [pairedAxis_pairIndex] using h.2.symm)
    refine ⟨v * u, ?_, ?_, ?_⟩
    · rw [act_mul, hv, root_coord, if_neg (axis_ne_of_pair_ne h.2.symm),
        if_neg (pairedAxis_ne d).symm, add_zero, sub_zero, hu]
    · rw [act_mul, hfix, hv, root_apply, pairedAxis_pairedAxis]
      have hmq : mate q ≠ mate d := axis_ne_of_pair_ne (by simpa only [pairedAxis_pairIndex] using h.2)
      simp only [basis_apply, if_neg (Ne.symm (pairedAxis_ne d)), if_neg hmq, mul_zero,
        zero_smul, add_zero, sub_zero]
    · intro j hj
      rw [act_mul, hv, root_coord]
      rcases Finset.mem_insert.mp hj with rfl | hj
      · simp [hm.symm, t, hu, hx]
      · have hjq : j ≠ q := fun he => hq (he ▸ hj)
        have hjm : j ≠ mate d := axis_ne_of_pair_ne (by
          simpa only [pairedAxis_pairIndex] using (hT j (Finset.mem_insert_of_mem hj)).2)
        simp only [if_neg hjq, if_neg hjm, add_zero, sub_zero, hz j hj]

private theorem clear_pair_complement {S : Finset Pair} {d : Axis} (hd : pairIndex d ∈ S)
    {x : Space} (hs : supported S x) (hi : B x x = 0) (hx : x d ≠ 0) :
    ∃ u : localWords S, act u x = x d • e d ∧ act u (e (mate d)) = e (mate d) := by
  let T := Finset.univ.filter fun q : Axis => pairIndex q ∈ S ∧ pairIndex q ≠ pairIndex d
  obtain ⟨u, hd', hf, hz⟩ := clear_coordinates hd x hx T (fun q hq => (Finset.mem_filter.mp hq).2)
  refine ⟨u, ?_, hf⟩
  rw [← hd']
  apply isotropic_axis (p := d) ((local_preserves u x x).trans hi) (fun h => hx (hd'.symm.trans h))
  intro j hj
  by_cases h : pairIndex j ∈ S
  · exact hz j (Finset.mem_filter.mpr ⟨Finset.mem_univ j, h, hj⟩)
  · exact local_supported u hs j h

private theorem obtain_pivot {S : Finset Pair} {p r : Axis}
    (hp : pairIndex p ∈ S) (hr : pairIndex r ∈ S) (hpr : pairIndex p ≠ pairIndex r)
    {x : Space} (hs : supported S x) (hx : x ≠ 0) :
    ∃ u : localWords S, act u x p ≠ 0 := by
  by_cases hxp : x p = 0
  · have use_other : ∀ y : Space, ∀ q : Axis, pairIndex q ∈ S → pairIndex p ≠ pairIndex q →
        y p = 0 → y q ≠ 0 → ∃ u : localWords S, act u y p ≠ 0 := by
      intro y q hq hpq hy hyq
      have hm : pairIndex (mate q) ∈ S := by rwa [pairedAxis_pairIndex]
      have hpm : pairIndex p ≠ pairIndex (mate q) := by rwa [pairedAxis_pairIndex]
      refine ⟨localRoot p (mate q) hp hm hpm 1, ?_⟩
      simp [act_root, root_coord, axis_ne_of_pair_ne hpm, hy, hyq]
    by_cases h : ∃ q, pairIndex p ≠ pairIndex q ∧ x q ≠ 0
    · obtain ⟨q, hpq, hq⟩ := h
      exact use_other x q (by by_contra hn; exact hq (hs q hn)) hpq hxp hq
    · have hz : ∀ q, pairIndex p ≠ pairIndex q → x q = 0 := by
        intro q hpq
        by_contra hn
        exact h ⟨q, hpq, hn⟩
      have hxm : x (mate p) ≠ 0 := by
        intro he
        apply hx
        rw [eq_two_axes p (fun j hj => hz j hj.symm), hxp, he, zero_smul, zero_smul, add_zero]
      let v := localRoot r p hr hp hpr.symm 1
      have hvr : act v x r = x (mate p) := by
        change root r p 1 x r = _
        simp [root_coord, axis_ne_of_pair_ne hpr.symm, hz r hpr]
      have hvp : act v x p = 0 := by
        change root r p 1 x p = _
        have hrm : pairIndex p ≠ pairIndex (mate r) := by rwa [pairedAxis_pairIndex]
        simp [root_coord, axis_ne_of_pair_ne hpr, hxp, hz (mate r) hrm]
      obtain ⟨u, hu⟩ := use_other (act v x) r hr hpr hvp (by rwa [hvr])
      exact ⟨u * v, hu⟩
  · exact ⟨1, hxp⟩

private theorem normalize_pivot {S : Finset Pair} {p r : Axis}
    (hp : pairIndex p ∈ S) (hr : pairIndex r ∈ S) (hpr : pairIndex p ≠ pairIndex r)
    {c : ℂ} (hc : c ≠ 0) : ∃ u : localWords S, act u (c • e p) = e p := by
  have hpm : pairIndex (mate p) ∈ S := by rwa [pairedAxis_pairIndex]
  have hrm : pairIndex (mate r) ∈ S := by rwa [pairedAxis_pairIndex]
  have h₁ : pairIndex r ≠ pairIndex (mate p) := by
    simpa only [pairedAxis_pairIndex] using hpr.symm
  have h₂ : pairIndex p ≠ pairIndex (mate r) := by rwa [pairedAxis_pairIndex]
  have hne := axis_ne_of_pair_ne hpr
  let u := localRoot r (mate p) hr hpm h₁ c⁻¹
  let v := localRoot p (mate r) hp hrm h₂ (1 - c)
  let w := localRoot r (mate p) hr hpm h₁ (-1)
  have hu : act u (c • e p) = c • e p + e r := by
    change root r (mate p) c⁻¹ (c • e p) = _
    simp [root_apply, basis_apply, (axis_ne_of_pair_ne h₂).symm, hc]
  have hv : act v (c • e p + e r) = e p + e r := by
    change root p (mate r) (1 - c) (c • e p + e r) = _
    simp [root_apply, basis_apply, hne.symm, pairedAxis_ne p, (axis_ne_of_pair_ne h₁).symm]
    rw [add_right_comm, ← add_smul, add_sub_cancel, one_smul]
  have hw : act w (e p + e r) = e p := by
    change root r (mate p) (-1) (e p + e r) = _
    simp [root_apply, basis_apply, hne, pairedAxis_ne r, (axis_ne_of_pair_ne h₂).symm]
  exact ⟨w * (v * u), by rw [act_mul, act_mul, hu, hv, hw]⟩

private theorem restore_pair {S : Finset Pair} {f : End} (hf : f ∈ splitSpecialOrthogonal)
    (hfix : fixesOutside S f) {p r : Axis}
    (hp : pairIndex p ∈ S) (hr : pairIndex r ∈ S) (hpr : pairIndex p ≠ pairIndex r) :
    ∃ u : localWords S, act u (f (e p)) = e p ∧ act u (f (e (mate p))) = e (mate p) := by
  have hB : ∀ x y, B (f x) (f y) = B x y := fun x y =>
    (D7Hodge.splitMetric_apply _ _).trans ((hf.2 x y).trans (D7Hodge.splitMetric_apply _ _).symm)
  have hpm : pairIndex (mate p) ∈ S := by rwa [pairedAxis_pairIndex]
  have hbp : B (e p) (e p) = 0 := by rw [metric_basis, basis_apply, if_neg (pairedAxis_ne p)]
  have hbm : B (e (mate p)) (e (mate p)) = 0 := by
    rw [metric_basis, basis_apply, pairedAxis_pairedAxis, if_neg (pairedAxis_ne p).symm]
  have hb : B (e p) (e (mate p)) = 1 := by rw [metric_basis, basis_apply, if_pos rfl]
  have hx : f (e p) ≠ 0 := by
    intro h
    have he := (hB (e p) (e (mate p))).trans hb
    simp only [h, map_zero, LinearMap.zero_apply, zero_ne_one] at he
  have hs := supported_map hB hfix (basis_supported hp)
  obtain ⟨u, hu⟩ := obtain_pivot hp hr hpr hs hx
  obtain ⟨v, hv, _⟩ := clear_pair_complement hp (local_supported u hs)
    ((local_preserves u _ _).trans ((hB _ _).trans hbp)) hu
  obtain ⟨w, hw⟩ := normalize_pivot hp hr hpr hu
  let g := w * (v * u)
  have hg : act g (f (e p)) = e p := by
    change act (w * (v * u)) (f (e p)) = _
    rw [act_mul, act_mul, hv, hw]
  let y := act g (f (e (mate p)))
  have hsy : supported S y := local_supported g (supported_map hB hfix (basis_supported hpm))
  have hy : B y y = 0 := (local_preserves g _ _).trans ((hB _ _).trans hbm)
  have hym : y (mate p) = 1 := by
    rw [← metric_basis p y, ← hg]
    exact (local_preserves g _ _).trans ((hB _ _).trans hb)
  obtain ⟨z, hz, hzp⟩ := clear_pair_complement hpm hsy hy (by rw [hym]; exact one_ne_zero)
  exact ⟨z * g, by rw [act_mul, hg]; simpa only [pairedAxis_pairedAxis] using hzp,
    by rw [act_mul]; change act z y = _; rw [hz, hym, one_smul]⟩

/-! Products of three roots exchange two disjoint null axes. Composing with
the exchange at parameter `-1` gives a diagonal map on the two pairs. -/

private def exchange (p r : Axis) (t : ℂ) : End :=
  root p (mate r) t * root r (mate p) (-t⁻¹) * root p (mate r) t

private theorem exchange_mem (p r : Axis) (h : pairIndex p ≠ pairIndex r) (t : ℂ) :
    exchange p r t ∈ Words :=
  Words.mul_mem (Words.mul_mem (root_mem _ _ (by simpa only [pairedAxis_pairIndex] using h) _)
    (root_mem _ _ (by simpa only [pairedAxis_pairIndex] using h.symm) _))
    (root_mem _ _ (by simpa only [pairedAxis_pairIndex] using h) _)

private theorem exchange_coord {p r : Axis} (h : pairIndex p ≠ pairIndex r)
    {t : ℂ} (ht : t ≠ 0) (x : Space) (j : Axis) :
    exchange p r t x j =
      if j = p then t * x r else
      if j = r then -t⁻¹ * x p else
      if j = mate p then t⁻¹ * x (mate r) else
      if j = mate r then -t * x (mate p) else x j := by
  change root p (mate r) t (root r (mate p) (-t⁻¹) (root p (mate r) t x)) j = _
  have hpr := axis_ne_of_pair_ne h
  have hpmr : p ≠ mate r := axis_ne_of_pair_ne (by simpa only [pairedAxis_pairIndex] using h)
  have hmpr : mate p ≠ r := axis_ne_of_pair_ne (by simpa only [pairedAxis_pairIndex] using h)
  have hm : mate p ≠ mate r := axis_ne_of_pair_ne (by simpa only [pairedAxis_pairIndex] using h)
  have h₁ := hpr.symm
  have h₂ := hpmr.symm
  have h₃ := hmpr.symm
  have h₄ := hm.symm
  have h₅ := pairedAxis_ne p
  have h₆ := pairedAxis_ne r
  have h₇ := h₅.symm
  have h₈ := h₆.symm
  rcases eq_or_ne j p with rfl | hp
  · simp_all [root_coord]
    field_simp
    ring
  rcases eq_or_ne j r with rfl | hr
  · simp_all [root_coord]
    field_simp
    ring
  rcases eq_or_ne j (mate p) with rfl | hp'
  · simp_all [root_coord]
    field_simp
    ring
  rcases eq_or_ne j (mate r) with rfl | hr'
  · simp_all [root_coord]
    field_simp
    ring
  · simp_all [root_coord]

private def diagonal (p r : Axis) (t : ℂ) : End :=
  exchange p r t * exchange p r (-1)

private theorem diagonal_mem (p r : Axis) (h : pairIndex p ≠ pairIndex r) (t : ℂ) :
    diagonal p r t ∈ Words :=
  Words.mul_mem (exchange_mem p r h t) (exchange_mem p r h (-1))

private theorem diagonal_coord {p r : Axis} (h : pairIndex p ≠ pairIndex r)
    {t : ℂ} (ht : t ≠ 0) (x : Space) (j : Axis) :
    diagonal p r t x j =
      (if j = p then t else
      if j = r then t⁻¹ else
      if j = mate p then t⁻¹ else
      if j = mate r then t else 1) * x j := by
  change exchange p r t (exchange p r (-1) x) j = _
  have hpr := axis_ne_of_pair_ne h
  have hrmp : r ≠ mate p := axis_ne_of_pair_ne (by simpa only [pairedAxis_pairIndex] using h.symm)
  have hmrp : mate r ≠ p := axis_ne_of_pair_ne (by simpa only [pairedAxis_pairIndex] using h.symm)
  have hm : mate r ≠ mate p := axis_ne_of_pair_ne (by simpa only [pairedAxis_pairIndex] using h.symm)
  simp only [exchange_coord h ht, exchange_coord h (neg_ne_zero.mpr one_ne_zero)]
  by_cases hp : j = p
  · simp [hp, hpr.symm]
  by_cases hr : j = r
  · simp [hr, hpr.symm]
  by_cases hp' : j = mate p
  · simp [hp', hmrp, hm, pairedAxis_ne r, pairedAxis_ne p, hrmp.symm]
  by_cases hr' : j = mate r
  · simp [hr', pairedAxis_ne p, hrmp.symm, hmrp, hm, pairedAxis_ne r]
  · simp [hp, hr, hp', hr']

private def singleTorus (i : Pair) (c : ℂˣ) : End :=
  torus fun j => if j = i then c else 1

private theorem singleTorus_coord (i : Pair) (c : ℂˣ) (x : Space) (j : Axis) :
    singleTorus i c x j =
      (if j = plusAxis i then (c : ℂ) else if j = minusAxis i then (c : ℂ)⁻¹ else 1) * x j := by
  change ((scale (fun k => if k = i then c else 1) j : ℂˣ) : ℂ) * x j = _
  by_cases hj : pairIndex j = i
  · have h : pairIndex j = pairIndex (plusAxis i) := hj.trans (pairIndex_plus i).symm
    rcases axis_cases h with rfl | h'
    · have hs : axisSign (plusAxis i) = 1 := by
        unfold axisSign
        change (if 2 * i.val % 2 = 0 then (1 : ℤ) else -1) = 1
        rw [if_pos (by omega)]
      simp [scale, pairIndex_plus, hs]
    · rw [h', pairedAxis_plus]
      have hs : axisSign (minusAxis i) = -1 := by
        unfold axisSign
        change (if (2 * i.val + 1) % 2 = 0 then (1 : ℤ) else -1) = -1
        rw [if_neg (by omega)]
      simp [scale, pairIndex_minus, hs, (plus_ne_minus i i).symm]
  · simp [scale, hj,
      show j ≠ plusAxis i from fun h => hj (by rw [h, pairIndex_plus]),
      show j ≠ minusAxis i from fun h => hj (by rw [h, pairIndex_minus])]

private theorem diagonal_cancel_aux {p r : Axis} (h : pairIndex p ≠ pairIndex r)
    {a : ℂ} (ha : a ≠ 0) (x : Space) (j : Axis) :
    diagonal p r a (diagonal p (mate r) a x) j =
      (if j = p then a * a else if j = mate p then a⁻¹ * a⁻¹ else 1) * x j := by
  have h' : pairIndex p ≠ pairIndex (mate r) := by rwa [pairedAxis_pairIndex]
  rw [diagonal_coord h ha, diagonal_coord h' ha, pairedAxis_pairedAxis]
  have hpr := (axis_ne_of_pair_ne h).symm
  have hpmr := (axis_ne_of_pair_ne h').symm
  have hrmp : r ≠ mate p := axis_ne_of_pair_ne (by simpa only [pairedAxis_pairIndex] using h.symm)
  have hm : mate r ≠ mate p := axis_ne_of_pair_ne (by simpa only [pairedAxis_pairIndex] using h.symm)
  by_cases hp : j = p
  · simp [hp, mul_assoc]
  by_cases hp' : j = mate p
  · simp [hp', pairedAxis_ne p, hrmp.symm, hm.symm, mul_assoc]
  by_cases hr : j = r
  · simp [hr, hpr, hrmp, (pairedAxis_ne r).symm, ha]
  by_cases hr' : j = mate r
  · simp [hr', hpmr, hm, pairedAxis_ne r, ha]
  · simp [hp, hp', hr, hr']

private theorem singleTorus_mem (i : Pair) (c : ℂˣ) : singleTorus i c ∈ Words := by
  obtain ⟨a, ha⟩ := IsAlgClosed.exists_pow_nat_eq (c : ℂ) (by decide : 0 < 2)
  rw [pow_two] at ha
  have han : a ≠ 0 := fun h => Units.ne_zero c (ha ▸ (h ▸ mul_zero (0 : ℂ)))
  have hai : a⁻¹ * a⁻¹ = (c : ℂ)⁻¹ := by rw [← ha, mul_inv_rev]
  obtain ⟨k, hk⟩ := exists_ne i
  have h : pairIndex (plusAxis i) ≠ pairIndex (plusAxis k) := by
    simpa only [pairIndex_plus] using hk.symm
  have h' : pairIndex (plusAxis i) ≠ pairIndex (mate (plusAxis k)) := by
    rwa [pairedAxis_pairIndex]
  have he : diagonal (plusAxis i) (plusAxis k) a *
      diagonal (plusAxis i) (mate (plusAxis k)) a = singleTorus i c := by
    apply LinearMap.ext
    intro x
    funext j
    rw [Module.End.mul_apply, diagonal_cancel_aux h han, singleTorus_coord,
      pairedAxis_plus, ha, hai]
  rw [← he]
  exact Words.mul_mem (diagonal_mem _ _ h a) (diagonal_mem _ _ h' a)

private theorem singleTorus_basis (i : Pair) (c : ℂˣ) (j : Axis) :
    singleTorus i c (e j) =
      (if j = plusAxis i then (c : ℂ) else if j = minusAxis i then (c : ℂ)⁻¹ else 1) • e j := by
  funext k
  rw [singleTorus_coord]
  by_cases h : k = j <;> simp [h, basis_apply]

private def swapAxes (p r : Axis) : End :=
  LinearMap.transvection (e.coord p - e.coord r) (e r - e p)

private theorem swap_det {p r : Axis} (h : p ≠ r) : (swapAxes p r).det = -1 := by
  rw [swapAxes, LinearMap.transvection.det]
  simp [h, h.symm]

private theorem swap_basis (p r j : Axis) (h : p ≠ r) :
    swapAxes p r (e j) = if j = p then e r else if j = r then e p else e j := by
  rw [swapAxes, LinearMap.transvection.apply]
  rcases eq_or_ne j p with rfl | hp
  · simp [h.symm]
  rcases eq_or_ne j r with rfl | hr
  · simp [hp, h]
  · simp [hp, hp.symm, hr, hr.symm]

private theorem singleton_generation (i : Pair) {f : End} (hf : f ∈ splitSpecialOrthogonal)
    (hfix : fixesOutside {i} f) : f ∈ Words := by
  let p := plusAxis i
  let q := mate p
  have hpi : pairIndex p = i := pairIndex_plus i
  have hqi : pairIndex q = i := (pairedAxis_pairIndex p).trans hpi
  have hpq : p ≠ q := (pairedAxis_ne p).symm
  have hq' : q = minusAxis i := pairedAxis_plus i
  have hB : ∀ x y, B (f x) (f y) = B x y := fun x y =>
    (D7Hodge.splitMetric_apply _ _).trans ((hf.2 x y).trans (D7Hodge.splitMetric_apply _ _).symm)
  let a := f (e p) p
  let b := f (e p) q
  let c := f (e q) p
  let d := f (e q) q
  have hs : ∀ k, pairIndex k = i → ∀ j, pairIndex j ≠ i → f (e k) j = 0 := by
    intro k hk j hj
    exact supported_map hB hfix (basis_supported (by simp [hk])) j (by simpa using hj)
  have hp : f (e p) = a • e p + b • e q :=
    eq_two_axes p (fun j hj => hs p hpi j (by simpa only [hpi] using hj))
  have hq : f (e q) = c • e p + d • e q :=
    eq_two_axes p (fun j hj => hs q hqi j (by simpa only [hpi] using hj))
  have hpp : B (e p) (e p) = 0 := by simp [basis_apply, pairedAxis_ne p]
  have hqq : B (e q) (e q) = 0 := by simp [basis_apply, q, hpq]
  have hpq' : B (e p) (e q) = 1 := by simp [basis_apply, q]
  have hab : a * b = 0 := by
    have h := (hB (e p) (e p)).trans hpp
    rw [hp, metric_two_axes] at h
    linear_combination h / 2
  have hcd : c * d = 0 := by
    have h := (hB (e q) (e q)).trans hqq
    rw [hq, metric_two_axes] at h
    linear_combination h / 2
  have hadbc : a * d + b * c = 1 := by
    have h := (hB (e p) (e q)).trans hpq'
    rwa [hp, hq, metric_two_axes] at h
  by_cases ha : a = 0
  · have hbc : b * c = 1 := by simpa [ha] using hadbc
    have hb : b ≠ 0 := left_ne_zero_of_mul_eq_one hbc
    have hc : c ≠ 0 := right_ne_zero_of_mul_eq_one hbc
    have hd : d = 0 := (mul_eq_zero.mp hcd).resolve_left hc
    have hcb : c = b⁻¹ := eq_inv_of_mul_eq_one_right hbc
    let u := Units.mk0 b hb
    have he : f = swapAxes p q * singleTorus i u := by
      apply e.ext
      intro j
      change f (e j) = swapAxes p q (singleTorus i u (e j))
      rw [singleTorus_basis, map_smul, swap_basis p q j hpq, ← hq']
      rcases eq_or_ne j p with rfl | hjp
      · simp [hp, ha, p, u]
      rcases eq_or_ne j q with rfl | hjq
      · simp [hq, hd, hcb, hjp, show q ≠ plusAxis i from hpq.symm, u]
      · have hj : pairIndex j ∉ ({i} : Finset Pair) := by
          intro hm
          have hm' : pairIndex j = pairIndex p := (Finset.mem_singleton.mp hm).trans hpi.symm
          exact (axis_cases hm').elim hjp hjq
        rw [hfix j hj]
        simp [show j ≠ plusAxis i from hjp, hjq, hjp]
    have hdet : f.det = 1 := hf.1
    rw [he, map_mul, swap_det hpq, singleTorus, torus_det, mul_one] at hdet
    norm_num at hdet
  · have hb : b = 0 := (mul_eq_zero.mp hab).resolve_left ha
    have had : a * d = 1 := by simpa [hb] using hadbc
    have hd : d ≠ 0 := right_ne_zero_of_mul_eq_one had
    have hc : c = 0 := (mul_eq_zero.mp hcd).resolve_right hd
    have hda : d = a⁻¹ := eq_inv_of_mul_eq_one_right had
    let u := Units.mk0 a ha
    have he : f = singleTorus i u := by
      apply e.ext
      intro j
      rw [singleTorus_basis, ← hq']
      rcases eq_or_ne j p with rfl | hjp
      · simp [hp, hb, p, u]
      rcases eq_or_ne j q with rfl | hjq
      · simp [hq, hc, hda, show q ≠ plusAxis i from hpq.symm, u]
      · have hj : pairIndex j ∉ ({i} : Finset Pair) := by
          intro hm
          have hm' : pairIndex j = pairIndex p := (Finset.mem_singleton.mp hm).trans hpi.symm
          exact (axis_cases hm').elim hjp hjq
        rw [hfix j hj]
        simp [show j ≠ plusAxis i from hjp, hjq]
    rw [he]
    exact singleTorus_mem i u

private theorem generation_supported (S : Finset Pair) (f : End)
    (hf : f ∈ splitSpecialOrthogonal) (hfix : fixesOutside S f) : f ∈ Words := by
  induction S using Finset.induction_on generalizing f with
  | empty =>
    have he : f = 1 := e.ext fun j => hfix j (Finset.notMem_empty _)
    rw [he]
    exact Words.one_mem
  | @insert i T hi ih =>
    by_cases hT : T.Nonempty
    · obtain ⟨k, hk⟩ := hT
      have hik : i ≠ k := fun h => hi (h ▸ hk)
      let p := plusAxis i
      let r := plusAxis k
      have hpi : pairIndex p = i := pairIndex_plus i
      have hri : pairIndex r = k := pairIndex_plus k
      obtain ⟨u, hp, hm⟩ := restore_pair hf hfix (p := p) (r := r)
        (hpi ▸ Finset.mem_insert_self i T) (hri ▸ Finset.mem_insert_of_mem hk)
        (by simpa only [hpi, hri] using hik)
      let g := act u * f
      have hg : g ∈ splitSpecialOrthogonal := splitSpecialOrthogonal.mul_mem (words_special u.prop.1) hf
      have hgf : fixesOutside T g := by
        intro j hj
        change act u (f (e j)) = e j
        by_cases hji : pairIndex j = i
        · rcases axis_cases (hji.trans hpi.symm) with he | he
          · rwa [he]
          · rwa [he]
        · have hnt : pairIndex j ∉ insert i T := by simp [hji, hj]
          rw [hfix j hnt]
          exact u.prop.2.2 j hnt
      have hmem := ih g hg hgf
      have he : (↑u.val⁻¹ : End) * g = f := by
        change (↑u.val⁻¹ : End) * ((u.val : End) * f) = f
        rw [← mul_assoc, u.val.inv_mul, one_mul]
      rw [← he]
      exact Words.mul_mem u.prop.2.1 hmem
    · rw [Finset.not_nonempty_iff_eq_empty.mp hT] at hfix
      exact singleton_generation i hf hfix

/-- The complex determinant-one split orthogonal group is generated by the
complex split root maps. -/
theorem splitSpecialOrthogonal_eq_rootClosure :
    splitSpecialOrthogonal = Submonoid.closure splitRootMaps :=
  le_antisymm (fun f hf => generation_supported Finset.univ f hf (by simp [fixesOutside]))
    words_special

/-- The action of every complex split special orthogonal transformation on a
pair of exterior tensors belongs to the complex linear span of real spin actions. -/
theorem splitSO_tensorActions_mem_spin_span (k l m n : ℕ) (f : splitSpecialOrthogonal) :
    (exteriorTensorMap k l f.val, exteriorTensorMap m n f.val) ∈
      Submodule.span ℂ (Set.range fun g : D7SpinAction.Spin =>
        (exteriorTensorMap k l (complexNullAction g),
          exteriorTensorMap m n (complexNullAction g))) :=
  rootClosure_tensorActions_mem_spin_span k l m n
    (splitSpecialOrthogonal_eq_rootClosure ▸ f.prop)

end

end GeometricUnity.D7RootGeneration
~~~

[Return to file index](#file-index)

## D7RealComparison.lean {#source-d7realcomparison-lean}

Identifies the complexified real coefficient, form, and covector tensor actions with the complex exterior-grade actions.

~~~lean
import D7CliffordAdjoint
import D7SpinNullFrame
import D7VectorTensor
import Mathlib.LinearAlgebra.BilinearForm.Properties
import Mathlib.LinearAlgebra.DirectSum.TensorProduct
import Mathlib.LinearAlgebra.QuadraticForm.Radical
import Mathlib.LinearAlgebra.TensorProduct.Pi

/-!
# Complexification of the real Spin coefficient representations

The real split quadratic space is complexified in the same null frame
used for the complex orthogonal action. The Clifford-to-exterior
identification then transports the conjugation action on the skew-adjoint
spinor matrices to the exterior grades.
-/

namespace GeometricUnity.D7RealComparison

open D7Exterior D7SpinAction D7SpinNullFrame D7CliffordAdjoint
open D7CliffordMatrix (spinorUnits ComplexMat)
open scoped TensorProduct DirectSum

noncomputable section

abbrev Coefficients := ↥(D7UnitaryRealForm.skewAdjoint complexSignature)
abbrev RealExterior (k : ℕ) := ⋀[ℝ]^k Vector
abbrev ComplexExterior (k : ℕ) := ⋀[ℂ]^k Space

/-- The complexification of the real vector space in the split null frame. -/
def vectorComplexEquiv : ℂ ⊗[ℝ] Vector ≃ₗ[ℂ] Space :=
  (nullFrame.baseChange ℝ ℂ).trans (TensorProduct.piScalarRight ℝ ℂ ℂ Axis)

private def vectorInclusion : Vector →ₗ[ℝ] Space :=
  (vectorComplexEquiv.toLinearMap.restrictScalars ℝ).comp (TensorProduct.mk ℝ ℂ Vector 1)

private theorem vectorComplexEquiv_tmul (z : ℂ) (v : Vector) :
    vectorComplexEquiv (z ⊗ₜ[ℝ] v) = z • vectorInclusion v := by
  change vectorComplexEquiv (z ⊗ₜ[ℝ] v) = z • vectorComplexEquiv (1 ⊗ₜ[ℝ] v)
  rw [← map_smul, TensorProduct.smul_tmul', smul_eq_mul, mul_one]

private theorem vectorInclusion_apply (v : Vector) :
    vectorInclusion v = fun j => (nullFrame v j : ℂ) := by
  funext j
  change vectorComplexEquiv (1 ⊗ₜ[ℝ] v) j = _
  simp [vectorComplexEquiv, Complex.real_smul]

private theorem vectorInclusion_intertwines (g : Spin) (v : Vector) :
    vectorInclusion (vectorRepresentation g v) = complexNullAction g (vectorInclusion v) := by
  rw [vectorInclusion_apply, vectorInclusion_apply]
  have h := complexNullAction_ofReal g (nullFrame v)
  change complexNullAction g (fun j => (nullFrame v j : ℂ)) =
    fun j => (realNullAction g (nullFrame v) j : ℂ) at h
  rw [h, realNullAction_apply, nullFrame.symm_apply_apply]

theorem vectorComplexEquiv_intertwines (g : Spin) :
    vectorComplexEquiv.toLinearMap.comp ((vectorRepresentation g).baseChange ℂ) =
      (complexNullAction g).comp vectorComplexEquiv.toLinearMap := by
  apply TensorProduct.AlgebraTensorModule.ext
  intro z v
  simp only [LinearMap.comp_apply, LinearMap.baseChange_tmul, LinearEquiv.coe_coe,
    vectorComplexEquiv_tmul, map_smul, vectorInclusion_intertwines]

private def realBasis : Module.Basis Axis ℝ Vector :=
  (Pi.basisFun ℝ Axis).map nullFrame.symm

private theorem vectorInclusion_basis (i : Axis) : vectorInclusion (realBasis i) = axisBasis i := by
  funext j
  simp only [vectorInclusion_apply, realBasis, Module.Basis.map_apply, nullFrame.apply_symm_apply,
    axisBasis, Pi.basisFun_apply, Pi.single_apply]
  split_ifs <;> simp

private def realExteriorInclusion : ExteriorAlgebra ℝ Vector →ₐ[ℝ] ExteriorAlgebra ℂ Space :=
  ExteriorAlgebra.lift ℝ
    ⟨((ExteriorAlgebra.ι ℂ).restrictScalars ℝ).comp vectorInclusion, fun v =>
      ExteriorAlgebra.ι_sq_zero (vectorInclusion v)⟩

private theorem realExteriorInclusion_ι (v : Vector) :
    realExteriorInclusion (ExteriorAlgebra.ι ℝ v) = ExteriorAlgebra.ι ℂ (vectorInclusion v) := by
  exact ExteriorAlgebra.lift_ι_apply (R := ℝ)
    (((ExteriorAlgebra.ι ℂ).restrictScalars ℝ).comp vectorInclusion)
    (fun x => ExteriorAlgebra.ι_sq_zero (vectorInclusion x)) v

private theorem realExteriorInclusion_ιMulti (k : ℕ) (v : Fin k → Vector) :
    realExteriorInclusion (ExteriorAlgebra.ιMulti ℝ k v) =
      ExteriorAlgebra.ιMulti ℂ k (vectorInclusion ∘ v) := by
  simp only [ExteriorAlgebra.ιMulti_apply, map_list_prod, List.map_ofFn, Function.comp_def,
    realExteriorInclusion_ι]

private def exteriorComplexMap :
    ℂ ⊗[ℝ] ExteriorAlgebra ℝ Vector →ₗ[ℂ] ExteriorAlgebra ℂ Space :=
  realExteriorInclusion.toLinearMap.liftBaseChange ℂ

private def exteriorComplexEquiv :
    ℂ ⊗[ℝ] ExteriorAlgebra ℝ Vector ≃ₗ[ℂ] ExteriorAlgebra ℂ Space :=
  (realBasis.ExteriorAlgebra.baseChange ℂ).equiv axisBasis.ExteriorAlgebra (Equiv.refl _)

private theorem exteriorComplexEquiv_toLinearMap :
    exteriorComplexEquiv.toLinearMap = exteriorComplexMap := by
  apply (realBasis.ExteriorAlgebra.baseChange ℂ).ext
  intro s
  change exteriorComplexEquiv ((realBasis.ExteriorAlgebra.baseChange ℂ) s) = _
  rw [show exteriorComplexEquiv ((realBasis.ExteriorAlgebra.baseChange ℂ) s) =
      axisBasis.ExteriorAlgebra s from Module.Basis.equiv_apply _ _ _ _]
  simp only [Module.Basis.baseChange_apply, exteriorComplexMap, LinearMap.liftBaseChange_tmul,
    AlgHom.toLinearMap_apply, one_smul, ExteriorAlgebra.basis_apply, ExteriorAlgebra.ιMulti_family,
    realExteriorInclusion_ιMulti, Function.comp_def, vectorInclusion_basis]

private theorem realExteriorInclusion_intertwines (g : Spin) (x : ExteriorAlgebra ℝ Vector) :
    realExteriorInclusion (ExteriorAlgebra.map (vectorRepresentation g) x) =
      ExteriorAlgebra.map (complexNullAction g) (realExteriorInclusion x) := by
  have h : realExteriorInclusion.comp (ExteriorAlgebra.map (vectorRepresentation g)) =
      ((ExteriorAlgebra.map (complexNullAction g)).restrictScalars ℝ).comp realExteriorInclusion := by
    apply ExteriorAlgebra.hom_ext
    ext v
    simp only [LinearMap.comp_apply, AlgHom.toLinearMap_apply, AlgHom.comp_apply,
      ExteriorAlgebra.map_apply_ι, realExteriorInclusion_ι, AlgHom.restrictScalars_apply,
      vectorInclusion_intertwines]
  exact DFunLike.congr_fun h x

private theorem exteriorComplexEquiv_intertwines (g : Spin) :
    exteriorComplexEquiv.toLinearMap.comp
        ((ExteriorAlgebra.map (vectorRepresentation g)).toLinearMap.baseChange ℂ) =
      (ExteriorAlgebra.map (complexNullAction g)).toLinearMap.comp exteriorComplexEquiv.toLinearMap := by
  rw [exteriorComplexEquiv_toLinearMap]
  apply TensorProduct.AlgebraTensorModule.ext
  intro z x
  simp only [LinearMap.comp_apply, LinearMap.baseChange_tmul, exteriorComplexMap,
    LinearMap.liftBaseChange_tmul, AlgHom.toLinearMap_apply, map_smul,
    realExteriorInclusion_intertwines]

/-- Complexification commutes with taking each exterior power. -/
def gradeComplexEquiv (k : ℕ) : ℂ ⊗[ℝ] RealExterior k ≃ₗ[ℂ] ComplexExterior k :=
  ((realBasis.exteriorPower k).baseChange ℂ).equiv (axisBasis.exteriorPower k) (Equiv.refl _)

private theorem gradeComplexEquiv_subtype (k : ℕ) :
    (Submodule.subtype (ComplexExterior k)).comp (gradeComplexEquiv k).toLinearMap =
      exteriorComplexEquiv.toLinearMap.comp ((Submodule.subtype (RealExterior k)).baseChange ℂ) := by
  apply ((realBasis.exteriorPower k).baseChange ℂ).ext
  intro s
  rw [LinearMap.comp_apply, LinearMap.comp_apply]
  change ((gradeComplexEquiv k (((realBasis.exteriorPower k).baseChange ℂ) s) :
    ComplexExterior k) : ExteriorAlgebra ℂ Space) = exteriorComplexEquiv _
  rw [show gradeComplexEquiv k (((realBasis.exteriorPower k).baseChange ℂ) s) =
      axisBasis.exteriorPower k s from Module.Basis.equiv_apply _ _ _ _,
    Module.Basis.baseChange_apply, LinearMap.baseChange_tmul, Submodule.subtype_apply,
    ← ExteriorAlgebra.basis_eq_coe_basis axisBasis s, ← ExteriorAlgebra.basis_eq_coe_basis realBasis s]
  symm
  simpa only [exteriorComplexEquiv, Module.Basis.baseChange_apply, Equiv.refl_apply] using
    Module.Basis.equiv_apply (realBasis.ExteriorAlgebra.baseChange ℂ) s.val
      axisBasis.ExteriorAlgebra (Equiv.refl _)

private theorem exteriorMap_subtype {K M N : Type} [Field K]
    [AddCommGroup M] [AddCommGroup N] [Module K M] [Module K N] (k : ℕ) (f : M →ₗ[K] N) :
    (Submodule.subtype (⋀[K]^k N)).comp (exteriorPower.map k f) =
      (ExteriorAlgebra.map f).toLinearMap.comp (Submodule.subtype (⋀[K]^k M)) := by
  apply exteriorPower.linearMap_ext
  apply AlternatingMap.ext
  intro v
  simp only [LinearMap.compAlternatingMap_apply, LinearMap.comp_apply, Submodule.subtype_apply,
    exteriorPower.map_apply_ιMulti, exteriorPower.ιMulti_apply_coe, AlgHom.toLinearMap_apply,
    ExteriorAlgebra.map_apply_ιMulti]

theorem gradeComplexEquiv_intertwines (g : Spin) (k : ℕ) :
    (gradeComplexEquiv k).toLinearMap.comp ((exteriorPower.map k (vectorRepresentation g)).baseChange ℂ) =
      (exteriorRepresentation k (spinToSO g)).comp (gradeComplexEquiv k).toLinearMap := by
  apply LinearMap.ext
  intro x
  apply Subtype.ext
  have hR := exteriorMap_subtype k (vectorRepresentation g)
  have hC := exteriorMap_subtype k (complexNullAction g)
  have h := DFunLike.congr_fun (gradeComplexEquiv_subtype k)
  have he := DFunLike.congr_fun (exteriorComplexEquiv_intertwines g)
  have hRb := congrArg (LinearMap.baseChange ℂ) hR
  rw [LinearMap.baseChange_comp, LinearMap.baseChange_comp] at hRb
  change ((gradeComplexEquiv k ((exteriorPower.map k (vectorRepresentation g)).baseChange ℂ x) :
      ComplexExterior k) : ExteriorAlgebra ℂ Space) =
    ((exteriorPower.map k (complexNullAction g) (gradeComplexEquiv k x) :
      ComplexExterior k) : ExteriorAlgebra ℂ Space)
  calc
    _ = exteriorComplexEquiv
          (((Submodule.subtype (RealExterior k)).baseChange ℂ)
            ((exteriorPower.map k (vectorRepresentation g)).baseChange ℂ x)) :=
      h _
    _ = exteriorComplexEquiv
          (((ExteriorAlgebra.map (vectorRepresentation g)).toLinearMap.baseChange ℂ)
            (((Submodule.subtype (RealExterior k)).baseChange ℂ) x)) :=
      congrArg exteriorComplexEquiv (DFunLike.congr_fun hRb x)
    _ = (ExteriorAlgebra.map (complexNullAction g))
          (exteriorComplexEquiv (((Submodule.subtype (RealExterior k)).baseChange ℂ) x)) :=
      he _
    _ = _ := by
      have hs := h x
      change ((gradeComplexEquiv k x : ComplexExterior k) : ExteriorAlgebra ℂ Space) =
        exteriorComplexEquiv (((Submodule.subtype (RealExterior k)).baseChange ℂ) x) at hs
      rw [← hs]
      exact (DFunLike.congr_fun hC (gradeComplexEquiv k x)).symm

abbrev CoefficientGrades := ⨁ k : Fin 15, ComplexExterior k.val

private def assembleGrades : CoefficientGrades →ₗ[ℂ] ExteriorAlgebra ℂ Space :=
  DirectSum.toModule ℂ (Fin 15) _ fun k => Submodule.subtype (ComplexExterior k.val)

private def restrictGrades : (⨁ k : ℕ, ComplexExterior k) →ₗ[ℂ] CoefficientGrades :=
  DirectSum.toModule ℂ ℕ _ fun k =>
    if h : k < 15 then DirectSum.lof ℂ (Fin 15) (fun i => ComplexExterior i.val) ⟨k, h⟩ else 0

private abbrev exteriorDecomposition :=
  DirectSum.decomposeLinearEquiv (fun k : ℕ => ComplexExterior k)

private theorem assembleGrades_injective : Function.Injective assembleGrades := by
  have h : restrictGrades.comp (exteriorDecomposition.toLinearMap.comp assembleGrades) =
      LinearMap.id := by
    apply DirectSum.linearMap_ext
    intro k
    apply LinearMap.ext
    intro x
    simp only [LinearMap.comp_apply, assembleGrades, DirectSum.toModule_lof,
      Submodule.subtype_apply, LinearEquiv.coe_coe, DirectSum.decomposeLinearEquiv_apply_coe,
      restrictGrades, dif_pos k.isLt, LinearMap.id_apply, Fin.eta]
  intro x y he
  have he' := congrArg (fun z => restrictGrades (exteriorDecomposition z)) he
  change (restrictGrades.comp (exteriorDecomposition.toLinearMap.comp assembleGrades)) x =
    (restrictGrades.comp (exteriorDecomposition.toLinearMap.comp assembleGrades)) y at he'
  rw [h] at he'
  exact he'

private theorem assembleGrades_surjective : Function.Surjective assembleGrades := by
  rw [← LinearMap.range_eq_top]
  apply top_unique
  rw [← axisBasis.ExteriorAlgebra.span_eq]
  apply Submodule.span_le.mpr
  rintro _ ⟨s, rfl⟩
  have hs := Finset.card_le_univ s
  rw [Fintype.card_fin] at hs
  let k : Fin 15 := ⟨s.card, Nat.lt_succ_of_le hs⟩
  let s' : D7Exterior.Index k.val := ⟨s, rfl⟩
  refine ⟨DirectSum.lof ℂ _ _ k (axisBasis.exteriorPower k.val s'), ?_⟩
  rw [assembleGrades, DirectSum.toModule_lof, Submodule.subtype_apply]
  exact (ExteriorAlgebra.basis_eq_coe_basis axisBasis s').symm

private def assembleGradesEquiv : CoefficientGrades ≃ₗ[ℂ] ExteriorAlgebra ℂ Space :=
  LinearEquiv.ofBijective assembleGrades ⟨assembleGrades_injective, assembleGrades_surjective⟩

/-- The actual conjugation action is a representation on the real coefficient space. -/
def coefficientAction : Representation ℝ Spin Coefficients where
  toFun := coefficientConjugation
  map_one' := by
    apply LinearMap.ext
    intro x
    apply Subtype.ext
    change (↑(spinorUnits 1) : ComplexMat) * x.val *
      (↑(spinorUnits 1)⁻¹ : ComplexMat) = x.val
    simp
  map_mul' g h := by
    apply LinearMap.ext
    intro x
    apply Subtype.ext
    change (↑(spinorUnits (g * h)) : ComplexMat) * x.val *
      (↑(spinorUnits (g * h))⁻¹ : ComplexMat) =
      (↑(spinorUnits g) : ComplexMat) *
        ((↑(spinorUnits h) : ComplexMat) * x.val * (↑(spinorUnits h)⁻¹ : ComplexMat)) *
        (↑(spinorUnits g)⁻¹ : ComplexMat)
    simp only [map_mul, Units.val_mul, mul_inv_rev, mul_assoc]

/-- The ambient action on all fifteen coefficient grades. -/
def coefficientGradeAction : Representation ℂ splitSpecialOrthogonal CoefficientGrades :=
  Representation.directSum fun k => exteriorRepresentation k.val

private theorem assembleGrades_intertwines (f : splitSpecialOrthogonal) :
    assembleGrades.comp (coefficientGradeAction f) =
      (ExteriorAlgebra.map f.val).toLinearMap.comp assembleGrades := by
  apply DirectSum.linearMap_ext
  intro k
  apply LinearMap.ext
  intro x
  have h := DFunLike.congr_fun (exteriorMap_subtype k.val f.val) x
  simpa [coefficientGradeAction, Representation.directSum_apply, assembleGrades,
    exteriorRepresentation] using h

private def coefficientExteriorEquiv :
    ℂ ⊗[ℝ] Coefficients ≃ₗ[ℂ] ExteriorAlgebra ℂ Space :=
  cliffordCoefficientEquiv.trans
    (((CliffordAlgebra.equivExterior WitnessW1.splitForm).baseChange ℝ ℂ).trans exteriorComplexEquiv)

private theorem coefficientExteriorEquiv_intertwines (g : Spin) :
    coefficientExteriorEquiv.toLinearMap.comp ((coefficientAction g).baseChange ℂ) =
      (ExteriorAlgebra.map (complexNullAction g)).toLinearMap.comp coefficientExteriorEquiv.toLinearMap := by
  let e := CliffordAlgebra.equivExterior WitnessW1.splitForm
  have h : e.toLinearMap.comp (cliffordConjugation g).toLinearMap =
      (ExteriorAlgebra.map (vectorRepresentation g)).toLinearMap.comp e.toLinearMap :=
    LinearMap.ext (equivExterior_intertwines g)
  have h' := congrArg (LinearMap.baseChange ℂ) h
  rw [LinearMap.baseChange_comp, LinearMap.baseChange_comp] at h'
  apply LinearMap.ext
  intro x
  have h₁ := DFunLike.congr_fun (cliffordCoefficientEquiv_intertwines g) x
  have h₂ := DFunLike.congr_fun h' (cliffordCoefficientEquiv x)
  have h₃ := DFunLike.congr_fun (exteriorComplexEquiv_intertwines g)
    ((e.toLinearMap.baseChange ℂ) (cliffordCoefficientEquiv x))
  simp only [LinearMap.comp_apply, LinearEquiv.coe_coe, AlgHom.toLinearMap_apply] at h₁ h₂ h₃
  change exteriorComplexEquiv
      ((e.toLinearMap.baseChange ℂ) (cliffordCoefficientEquiv ((coefficientConjugation g).baseChange ℂ x))) =
    ExteriorAlgebra.map (complexNullAction g)
      (exteriorComplexEquiv ((e.toLinearMap.baseChange ℂ) (cliffordCoefficientEquiv x)))
  rw [h₁, h₂, h₃]

/-- The complexified real unitary coefficient space, decomposed into exterior grades. -/
def coefficientComplexEquiv : ℂ ⊗[ℝ] Coefficients ≃ₗ[ℂ] CoefficientGrades :=
  coefficientExteriorEquiv.trans assembleGradesEquiv.symm

theorem coefficientComplexEquiv_intertwines (g : Spin) :
    coefficientComplexEquiv.toLinearMap.comp ((coefficientAction g).baseChange ℂ) =
      (coefficientGradeAction (spinToSO g)).comp coefficientComplexEquiv.toLinearMap := by
  apply LinearMap.ext
  intro x
  apply assembleGrades_injective
  have h (z : ℂ ⊗[ℝ] Coefficients) :
      assembleGrades (coefficientComplexEquiv z) = coefficientExteriorEquiv z :=
    assembleGradesEquiv.apply_symm_apply (coefficientExteriorEquiv z)
  change assembleGrades (coefficientComplexEquiv ((coefficientAction g).baseChange ℂ x)) =
    assembleGrades (coefficientGradeAction (spinToSO g) (coefficientComplexEquiv x))
  rw [h]
  have ha := DFunLike.congr_fun (assembleGrades_intertwines (spinToSO g)) (coefficientComplexEquiv x)
  change assembleGrades (coefficientGradeAction (spinToSO g) (coefficientComplexEquiv x)) =
    ExteriorAlgebra.map (complexNullAction g) (assembleGrades (coefficientComplexEquiv x)) at ha
  rw [ha, h]
  exact DFunLike.congr_fun (coefficientExteriorEquiv_intertwines g) x

/-- Scalar extension of a real representation to a complex representation. -/
def complexify {M : Type*} [AddCommGroup M] [Module ℝ M]
    (ρ : Representation ℝ Spin M) : Representation ℂ Spin (ℂ ⊗[ℝ] M) :=
  (Module.End.baseChangeHom ℝ ℂ M).toMonoidHom.comp ρ

@[simp] theorem complexify_apply {M : Type*} [AddCommGroup M] [Module ℝ M]
    (ρ : Representation ℝ Spin M) (g : Spin) :
    complexify ρ g = (ρ g).baseChange ℂ := rfl

private def exteriorAction {M : Type*} [AddCommGroup M] [Module ℝ M]
    (ρ : Representation ℝ Spin M) (k : ℕ) : Representation ℝ Spin (⋀[ℝ]^k M) where
  toFun g := exteriorPower.map k (ρ g)
  map_one' := by rw [map_one, Module.End.one_eq_id, exteriorPower.map_id]; rfl
  map_mul' g h := by rw [map_mul, Module.End.mul_eq_comp, exteriorPower.map_comp]; rfl

/-- The action on real exterior powers induced by the real Spin vector action. -/
def realExteriorAction (k : ℕ) : Representation ℝ Spin (RealExterior k) :=
  exteriorAction vectorRepresentation k

private abbrev splitMetric : LinearMap.BilinForm ℝ Vector := WitnessW1.splitForm.associated

private theorem splitAssociated_nondegenerate : splitMetric.Nondegenerate := by
  apply QuadraticMap.nondegenerate_associated_iff.mpr
  apply QuadraticMap.nondegenerate_iff_radical_eq_bot.mpr
  rw [WitnessW1.splitForm, QuadraticForm.radical_weightedSumSquares]
  apply (Submodule.eq_bot_iff _).mpr
  intro x hx
  funext i
  apply Pi.mem_spanSubset_iff.mp hx i
  change WitnessW1.metricSign i ≠ 0
  unfold WitnessW1.metricSign
  split_ifs <;> norm_num

/-- The real split metric identifies the vector and covector Spin representations. -/
def metricDualEquiv : vectorRepresentation.Equiv vectorRepresentation.dual := by
  let e := LinearMap.BilinForm.toDual splitMetric splitAssociated_nondegenerate
  refine Representation.Equiv.mk e fun g => ?_
  apply LinearMap.ext
  intro v
  apply LinearMap.ext
  intro w
  change e (vectorRepresentation g v) w = e v (vectorRepresentation g⁻¹ w)
  simp only [e, LinearMap.BilinForm.toDual_def]
  have h := associated_preserves g v (vectorRepresentation g⁻¹ w)
  have hw : vectorRepresentation g (vectorRepresentation g⁻¹ w) = w := by
    change (vectorRepresentation g * vectorRepresentation g⁻¹) w = w
    rw [← map_mul, mul_inv_cancel, map_one]
    rfl
  rwa [hw] at h

abbrev Covector := Module.Dual ℝ Vector

/-- The action on real differential form factors. -/
def formAction (k : ℕ) : Representation ℝ Spin (⋀[ℝ]^k Covector) :=
  exteriorAction vectorRepresentation.dual k

/-- Raising indices with the split metric identifies the covariant and contravariant exterior actions. -/
def formMetricEquiv (k : ℕ) : (formAction k).Equiv (realExteriorAction k) := by
  let e := metricDualEquiv.symm
  let E : (⋀[ℝ]^k Covector) ≃ₗ[ℝ] RealExterior k := LinearEquiv.ofLinearMap
    (exteriorPower.map k e.toLinearEquiv.toLinearMap)
    (exteriorPower.map k e.toLinearEquiv.symm.toLinearMap)
    (by rw [← exteriorPower.map_comp, LinearEquiv.comp_symm, exteriorPower.map_id])
    (by rw [← exteriorPower.map_comp, LinearEquiv.symm_comp, exteriorPower.map_id])
  refine Representation.Equiv.mk E fun g => ?_
  change exteriorPower.map k e.toLinearEquiv.toLinearMap ∘ₗ
      exteriorPower.map k (vectorRepresentation.dual g) =
    exteriorPower.map k (vectorRepresentation g) ∘ₗ exteriorPower.map k e.toLinearEquiv.toLinearMap
  rw [← exteriorPower.map_comp, ← exteriorPower.map_comp]
  exact congrArg (exteriorPower.map k) (e.isIntertwining' g)

private def complexifyEquiv {M N : Type*} [AddCommGroup M] [AddCommGroup N]
    [Module ℝ M] [Module ℝ N] {ρ : Representation ℝ Spin M} {σ : Representation ℝ Spin N}
    (e : ρ.Equiv σ) : (complexify ρ).Equiv (complexify σ) :=
  Representation.Equiv.mk (e.toLinearEquiv.baseChange ℝ ℂ) fun g => by
    simpa only [LinearEquiv.coe_baseChange, complexify_apply, LinearMap.baseChange_comp] using
      congrArg (LinearMap.baseChange ℂ) (e.isIntertwining' g)

/-- The complex ambient action with the same tensor factor attached to each coefficient grade. -/
def tensorGradeAction {U : Type*} [AddCommGroup U] [Module ℂ U]
    (σ : Representation ℂ splitSpecialOrthogonal U) :
    Representation ℂ splitSpecialOrthogonal (⨁ k : Fin 15, U ⊗[ℂ] ComplexExterior k.val) :=
  Representation.directSum fun k => σ.tprod (exteriorRepresentation k.val)

private def distributeGrades {U : Type*} [AddCommGroup U] [Module ℂ U]
    (σ : Representation ℂ splitSpecialOrthogonal U) :
    (σ.tprod coefficientGradeAction).Equiv (tensorGradeAction σ) := by
  let e := TensorProduct.directSumRight ℂ ℂ U (fun k : Fin 15 => ComplexExterior k.val)
  refine Representation.Equiv.mk e fun f => ?_
  apply TensorProduct.ext'
  intro u z
  let j := TensorProduct.mk ℂ U CoefficientGrades u
  suffices h : (e.toLinearMap.comp ((σ.tprod coefficientGradeAction) f)).comp j =
      ((tensorGradeAction σ f).comp e.toLinearMap).comp j from DFunLike.congr_fun h z
  apply DirectSum.linearMap_ext
  intro k
  apply LinearMap.ext
  intro x
  simp [j, e, Representation.tprod_apply, coefficientGradeAction, tensorGradeAction,
    Representation.directSum_apply]

private def tensorComplexEquiv {M U : Type*} [AddCommGroup M] [Module ℝ M]
    [AddCommGroup U] [Module ℂ U]
    (ρ : Representation ℝ Spin M) (σ : Representation ℂ splitSpecialOrthogonal U)
    (e : (complexify ρ).Equiv (σ.comp spinToSO)) :
    (complexify (ρ.tprod coefficientAction)).Equiv
      ((σ.tprod coefficientGradeAction).comp spinToSO) := by
  let E := (TensorProduct.AlgebraTensorModule.distribBaseChange ℝ ℂ M Coefficients).trans
    (TensorProduct.congr e.toLinearEquiv coefficientComplexEquiv)
  refine Representation.Equiv.mk E fun g => ?_
  apply TensorProduct.AlgebraTensorModule.ext
  intro c t
  let j := TensorProduct.mk ℝ ℂ (M ⊗[ℝ] Coefficients) c
  suffices h : (((E.toLinearMap.comp (complexify (ρ.tprod coefficientAction) g)).restrictScalars ℝ).comp j) =
      (((((σ.tprod coefficientGradeAction).comp spinToSO) g).comp E.toLinearMap).restrictScalars ℝ).comp j
      from DFunLike.congr_fun h t
  apply TensorProduct.ext'
  intro m x
  have hv := DFunLike.congr_fun (e.isIntertwining' g) (c ⊗ₜ[ℝ] m)
  change e.toLinearEquiv (complexify ρ g (c ⊗ₜ[ℝ] m)) =
    σ (spinToSO g) (e.toLinearEquiv (c ⊗ₜ[ℝ] m)) at hv
  have hx := DFunLike.congr_fun (coefficientComplexEquiv_intertwines g) (1 ⊗ₜ[ℝ] x)
  simp only [LinearMap.comp_apply, LinearEquiv.coe_coe, complexify_apply, LinearMap.baseChange_tmul] at hv hx
  simp only [LinearMap.comp_apply, LinearMap.restrictScalars_apply, j, TensorProduct.mk_apply,
    LinearEquiv.coe_coe, E, LinearEquiv.trans_apply, complexify_apply, LinearMap.baseChange_tmul,
    Representation.tprod_apply, MonoidHom.comp_apply, TensorProduct.map_tmul,
    TensorProduct.AlgebraTensorModule.distribBaseChange_tmul, TensorProduct.congr_tmul,
    hv, hx]

/-- Compare a tensor of a real Spin factor with the actual coefficient action to
the direct sum of the corresponding complex tensor grades. -/
def tensorComparison {M U : Type*} [AddCommGroup M] [Module ℝ M] [AddCommGroup U] [Module ℂ U]
    (ρ : Representation ℝ Spin M) (σ : Representation ℂ splitSpecialOrthogonal U)
    (e : (complexify ρ).Equiv (σ.comp spinToSO)) :
    (complexify (ρ.tprod coefficientAction)).Equiv ((tensorGradeAction σ).comp spinToSO) :=
  (tensorComplexEquiv ρ σ e).trans <|
    Representation.Equiv.mk (distributeGrades σ).toLinearEquiv
      (fun g => (distributeGrades σ).isIntertwining' (spinToSO g))

/-- The exterior-factor comparison, including the two-form source and the alternating channel. -/
def exteriorCoefficientComparison (k : ℕ) :
    (complexify (M := RealExterior k ⊗[ℝ] Coefficients)
      ((realExteriorAction k).tprod coefficientAction)).Equiv
      ((tensorGradeAction (exteriorRepresentation k)).comp spinToSO) :=
  tensorComparison (realExteriorAction k) (exteriorRepresentation k) <|
    Representation.Equiv.mk (gradeComplexEquiv k) (gradeComplexEquiv_intertwines · k)

/-- The vector-factor comparison for the target of the unrestricted contractions. -/
def vectorCoefficientComparison :
    (complexify (vectorRepresentation.tprod coefficientAction)).Equiv
      ((tensorGradeAction D7VectorTensor.vectorAction).comp spinToSO) :=
  tensorComparison vectorRepresentation D7VectorTensor.vectorAction <|
    Representation.Equiv.mk vectorComplexEquiv vectorComplexEquiv_intertwines

/-- The form-factor comparison on the real covariant source and alternating channel. -/
def formCoefficientComparison (k : ℕ) :
    (complexify (M := (⋀[ℝ]^k Covector) ⊗[ℝ] Coefficients)
      ((formAction k).tprod coefficientAction)).Equiv
      ((tensorGradeAction (exteriorRepresentation k)).comp spinToSO) :=
  tensorComparison (formAction k) (exteriorRepresentation k) <|
    (complexifyEquiv (formMetricEquiv k)).trans
      (Representation.Equiv.mk (gradeComplexEquiv k) (gradeComplexEquiv_intertwines · k))

/-- The one-form factor in the real codomain of Theorem 3.4. -/
def covectorCoefficientComparison :
    (complexify (M := Covector ⊗[ℝ] Coefficients)
      (vectorRepresentation.dual.tprod coefficientAction)).Equiv
      ((tensorGradeAction D7VectorTensor.vectorAction).comp spinToSO) :=
  tensorComparison vectorRepresentation.dual D7VectorTensor.vectorAction <|
    (complexifyEquiv metricDualEquiv.symm).trans
      (Representation.Equiv.mk vectorComplexEquiv vectorComplexEquiv_intertwines)

end

end GeometricUnity.D7RealComparison
~~~

[Return to file index](#file-index)

## D7RealJets.lean {#source-d7realjets-lean}

Constructs real coordinate first jets, wedge and trace projections, and their equivariant sections.

~~~lean
import D7RealComparison
import BianchiSymbol
import Mathlib.LinearAlgebra.Alternating.Uncurry.Fin

/-! # Real first jets, exterior alternation, and the split metric -/

namespace GeometricUnity.D7RealJets

open D7Exterior (Axis)
open D7RealComparison (Covector)
open scoped TensorProduct BigOperators

noncomputable section

set_option backward.isDefEq.respectTransparency false
set_option maxHeartbeats 1000000

abbrev Forms (k : ℕ) := ⋀[ℝ]^k Covector
abbrev FormJets := Covector ⊗[ℝ] Forms 2

def formBasis : Module.Basis Axis ℝ Covector := (Pi.basisFun ℝ Axis).dualBasis

def wedgeTwo (x y : Covector) : Forms 2 := exteriorPower.ιMulti ℝ 2 ![x, y]
def wedgeThree (x y z : Covector) : Forms 3 := exteriorPower.ιMulti ℝ 3 ![x, y, z]

theorem two_ext {W : Type*} [AddCommGroup W] [Module ℝ W] {f g : Forms 2 →ₗ[ℝ] W}
    (h : ∀ y z, f (wedgeTwo y z) = g (wedgeTwo y z)) : f = g := by
  apply exteriorPower.linearMap_ext
  apply AlternatingMap.ext
  intro v
  have hv : (![v 0, v 1] : Fin 2 → Covector) = v := by funext i; fin_cases i <;> rfl
  simpa only [LinearMap.compAlternatingMap_apply, wedgeTwo, hv] using h (v 0) (v 1)

theorem tensor_ext {W : Type*} [AddCommGroup W] [Module ℝ W] {f g : FormJets →ₗ[ℝ] W}
    (h : ∀ x y z, f (x ⊗ₜ[ℝ] wedgeTwo y z) = g (x ⊗ₜ[ℝ] wedgeTwo y z)) : f = g := by
  apply TensorProduct.ext'
  intro x u
  have he : f.comp (TensorProduct.mk ℝ Covector (Forms 2) x) =
      g.comp (TensorProduct.mk ℝ Covector (Forms 2) x) := two_ext (h x)
  exact DFunLike.congr_fun he u

private theorem three_ext {W : Type*} [AddCommGroup W] [Module ℝ W] {f g : Forms 3 →ₗ[ℝ] W}
    (h : ∀ x y z, f (wedgeThree x y z) = g (wedgeThree x y z)) : f = g := by
  apply exteriorPower.linearMap_ext
  apply AlternatingMap.ext
  intro v
  have hv : (![v 0, v 1, v 2] : Fin 3 → Covector) = v := by funext i; fin_cases i <;> rfl
  simpa only [LinearMap.compAlternatingMap_apply, wedgeThree, hv] using h (v 0) (v 1) (v 2)

private theorem coe_wedgeTwo (y z : Covector) :
    (wedgeTwo y z : ExteriorAlgebra ℝ Covector) = ExteriorAlgebra.ι ℝ y * ExteriorAlgebra.ι ℝ z := by
  simp [wedgeTwo, ExteriorAlgebra.ιMulti_apply]

private theorem coe_wedgeThree (x y z : Covector) :
    (wedgeThree x y z : ExteriorAlgebra ℝ Covector) =
      ExteriorAlgebra.ι ℝ x * (ExteriorAlgebra.ι ℝ y * ExteriorAlgebra.ι ℝ z) := by
  simp [wedgeThree, ExteriorAlgebra.ιMulti_apply]

theorem wedgeTwo_swap (x y : Covector) : wedgeTwo x y = -wedgeTwo y x := by
  apply Subtype.ext
  simp only [Submodule.coe_neg, coe_wedgeTwo]
  exact eq_neg_of_add_eq_zero_left (ExteriorAlgebra.ι_add_mul_swap (R := ℝ) x y)

private def wedgeLeft (x : Covector) (u : Forms 2) : Forms 3 :=
  ⟨ExteriorAlgebra.ι ℝ x * u.val, by
    change _ ∈ (LinearMap.range (ExteriorAlgebra.ι ℝ : Covector →ₗ[ℝ] _)) ^ (2 + 1)
    rw [Nat.add_comm 2 1, pow_add, pow_one]
    exact Submodule.mul_mem_mul (LinearMap.mem_range_self _ x) u.prop⟩

private def wedgeLeftLinear : Covector →ₗ[ℝ] Forms 2 →ₗ[ℝ] Forms 3 :=
  LinearMap.mk₂ ℝ wedgeLeft
    (fun x y u => by
      apply Subtype.ext
      change ExteriorAlgebra.ι ℝ (x + y) * u.val = _
      rw [map_add]
      exact add_mul _ _ _)
    (fun r x u => by
      apply Subtype.ext
      change ExteriorAlgebra.ι ℝ (r • x) * u.val = _
      rw [map_smul]
      exact smul_mul_assoc _ _ _)
    (fun x u v => by apply Subtype.ext; exact mul_add _ _ _)
    (fun r x u => by apply Subtype.ext; exact mul_smul_comm _ _ _)

/-- Wedge the derivative covector with the two form covectors. -/
def wedgeJet : FormJets →ₗ[ℝ] Forms 3 := TensorProduct.lift wedgeLeftLinear

@[simp] theorem wedgeJet_pure (x y z : Covector) :
    wedgeJet (x ⊗ₜ[ℝ] wedgeTwo y z) = wedgeThree x y z := by
  rw [wedgeJet, TensorProduct.lift.tmul]
  apply Subtype.ext
  change ExteriorAlgebra.ι ℝ x * (wedgeTwo y z).val = _
  rw [coe_wedgeTwo, coe_wedgeThree]

theorem map_wedgeTwo (f : Covector →ₗ[ℝ] Covector) (x y : Covector) :
    exteriorPower.map 2 f (wedgeTwo x y) = wedgeTwo (f x) (f y) := by
  rw [wedgeTwo, wedgeTwo, exteriorPower.map_apply_ιMulti]
  congr 1
  funext i
  fin_cases i <;> rfl

private theorem map_wedgeThree (f : Covector →ₗ[ℝ] Covector) (x y z : Covector) :
    exteriorPower.map 3 f (wedgeThree x y z) = wedgeThree (f x) (f y) (f z) := by
  rw [wedgeThree, wedgeThree, exteriorPower.map_apply_ιMulti]
  congr 1
  funext i
  fin_cases i <;> rfl

theorem wedgeJet_natural (f : Covector →ₗ[ℝ] Covector) :
    wedgeJet.comp (TensorProduct.map f (exteriorPower.map 2 f)) =
      (exteriorPower.map 3 f).comp wedgeJet := by
  apply tensor_ext
  intro x y z
  simp only [LinearMap.comp_apply, TensorProduct.map_tmul, map_wedgeTwo, wedgeJet_pure,
    map_wedgeThree]

private def insertionAlternating : Covector →ₗ[ℝ] (Covector [⋀^Fin 2]→ₗ[ℝ] FormJets) where
  toFun x := (TensorProduct.mk ℝ Covector (Forms 2) x).compAlternatingMap (exteriorPower.ιMulti ℝ 2)
  map_add' x y := by ext v; exact TensorProduct.add_tmul _ _ _
  map_smul' c x := by ext v; exact (TensorProduct.smul_tmul' c x _).symm

def includeThree : Forms 3 →ₗ[ℝ] FormJets :=
  (1 / 3 : ℝ) • exteriorPower.alternatingMapLinearEquiv (R := ℝ) (M := Covector) (N := FormJets) (n := 3)
    (AlternatingMap.alternatizeUncurryFin (R := ℝ) (M := Covector) (N := FormJets) insertionAlternating)

@[simp] theorem includeThree_pure (x y z : Covector) :
    includeThree (wedgeThree x y z) = (1 / 3 : ℝ) •
      (x ⊗ₜ[ℝ] wedgeTwo y z + y ⊗ₜ[ℝ] wedgeTwo z x + z ⊗ₜ[ℝ] wedgeTwo x y) := by
  simp only [includeThree, LinearMap.smul_apply, wedgeThree,
    exteriorPower.alternatingMapLinearEquiv_apply_ιMulti,
    AlternatingMap.alternatizeUncurryFin_apply, insertionAlternating,
    LinearMap.coe_mk, AddHom.coe_mk, LinearMap.compAlternatingMap_apply, TensorProduct.mk_apply]
  let F (i : Fin 3) := (-1 : ℤ) ^ i.val •
    (![x, y, z] i ⊗ₜ[ℝ] exteriorPower.ιMulti ℝ 2 (i.removeNth ![x, y, z]))
  change (1 / 3 : ℝ) • ∑ i : Fin 3, F i = _
  rw [Fin.sum_univ_three]
  have h₀ : F 0 = x ⊗ₜ[ℝ] wedgeTwo y z := by
    change (1 : ℤ) • (x ⊗ₜ[ℝ] wedgeTwo y z) = _
    exact one_zsmul _
  have h : (1 : Fin 3).removeNth ![x, y, z] = ![x, z] := by
    funext i
    fin_cases i <;> rfl
  have h₁ : F 1 = y ⊗ₜ[ℝ] wedgeTwo z x := by
    change (-1 : ℤ) • (y ⊗ₜ[ℝ] exteriorPower.ιMulti ℝ 2 ((1 : Fin 3).removeNth ![x, y, z])) = _
    rw [h]
    change (-1 : ℤ) • (y ⊗ₜ[ℝ] wedgeTwo x z) = _
    have hm : y ⊗ₜ[ℝ] wedgeTwo x z = -(y ⊗ₜ[ℝ] wedgeTwo z x) :=
      (congrArg (fun u : Forms 2 => y ⊗ₜ[ℝ] u) (wedgeTwo_swap x z)).trans
        (TensorProduct.tmul_neg y (wedgeTwo z x))
    rw [hm, neg_one_zsmul]
    exact neg_neg (y ⊗ₜ[ℝ] wedgeTwo z x : FormJets)
  have h₂ : F 2 = z ⊗ₜ[ℝ] wedgeTwo x y := by
    change (-1 : ℤ) ^ 2 • (z ⊗ₜ[ℝ] wedgeTwo x y) = _
    norm_num
  rw [h₀, h₁, h₂]

private theorem wedgeThree_rotate (x y z : Covector) : wedgeThree y z x = wedgeThree x y z := by
  let p : Equiv.Perm (Fin 3) := Equiv.swap 0 2 * Equiv.swap 0 1
  have hp : p.sign = 1 := by decide +kernel
  have he : (![y, z, x] : Fin 3 → Covector) = ![x, y, z] ∘ p := by
    funext i
    fin_cases i <;> rfl
  rw [wedgeThree, wedgeThree, he, AlternatingMap.map_perm, hp, one_smul]

theorem wedge_includeThree : wedgeJet.comp includeThree = LinearMap.id := by
  apply three_ext
  intro x y z
  simp only [LinearMap.comp_apply, includeThree_pure, map_smul, map_add, wedgeJet_pure,
    wedgeThree_rotate y z x, wedgeThree_rotate x y z, LinearMap.id_apply]
  module

theorem includeThree_natural (f : Covector →ₗ[ℝ] Covector) :
    includeThree.comp (exteriorPower.map 3 f) =
      (TensorProduct.map f (exteriorPower.map 2 f)).comp includeThree := by
  apply three_ext (W := FormJets)
  intro x y z
  simp only [LinearMap.comp_apply, map_wedgeThree, includeThree_pure, map_smul, map_add,
    TensorProduct.map_tmul, map_wedgeTwo]

private def pairCoordinate (b c : Axis) : (Forms 2) →ₗ[ℝ] ℝ :=
  exteriorPower.pairingDual ℝ Covector 2
    (exteriorPower.ιMulti ℝ 2 ![formBasis.coord b, formBasis.coord c])

private theorem pairCoordinate_wedge (b c : Axis) (y z : Covector) :
    pairCoordinate b c (wedgeTwo y z) =
      formBasis.coord b y * formBasis.coord c z - formBasis.coord c y * formBasis.coord b z := by
  simp [pairCoordinate, wedgeTwo, exteriorPower.pairingDual_ιMulti_ιMulti, Matrix.det_fin_two]

private theorem pairCoordinate_swap (b c : Axis) :
    pairCoordinate c b = -pairCoordinate b c := by
  apply two_ext
  intro x y
  simp only [LinearMap.neg_apply, pairCoordinate_wedge]
  ring

private def tripleCoordinate (a b c : Axis) : FormJets →ₗ[ℝ] ℝ :=
  TensorProduct.lift ((formBasis.coord a).smulRight (pairCoordinate b c))

@[simp] private theorem tripleCoordinate_tmul (a b c : Axis) (x : Covector) (u : Forms 2) :
    tripleCoordinate a b c (x ⊗ₜ[ℝ] u) = formBasis.coord a x * pairCoordinate b c u := rfl

private theorem tripleCoordinate_swap (a b c : Axis) :
    tripleCoordinate a c b = -tripleCoordinate a b c := by
  apply TensorProduct.ext'
  intro x u
  rw [tripleCoordinate_tmul, LinearMap.neg_apply, tripleCoordinate_tmul,
    pairCoordinate_swap b c, LinearMap.neg_apply, mul_neg]

private theorem tripleCoordinate_average (a b c : Axis) (s : FormJets) :
    tripleCoordinate a b c (includeThree (wedgeJet s)) =
      (1 / 3 : ℝ) * (tripleCoordinate a b c s + tripleCoordinate b c a s +
        tripleCoordinate c a b s) := by
  let f := (tripleCoordinate a b c).comp (includeThree.comp wedgeJet)
  let g := (1 / 3 : ℝ) • (tripleCoordinate a b c + tripleCoordinate b c a +
    tripleCoordinate c a b)
  have h : f = g := by
    apply TensorProduct.ext'
    intro x u
    let m := TensorProduct.mk ℝ Covector (Forms 2) x
    have hm : f.comp m = g.comp m := by
      apply two_ext
      intro y z
      simp only [f, g, m, LinearMap.comp_apply, TensorProduct.mk_apply, wedgeJet_pure,
        includeThree_pure, map_smul, map_add, LinearMap.smul_apply,
        LinearMap.add_apply, tripleCoordinate_tmul, pairCoordinate_wedge, smul_eq_mul]
      ring
    exact DFunLike.congr_fun hm u
  exact DFunLike.congr_fun h s

section Coefficients

variable {E : Type} [AddCommGroup E] [Module ℝ E]

private def coordinateEntry (a b c : Axis) : (FormJets ⊗[ℝ] E) →ₗ[ℝ] E :=
  (TensorProduct.lid ℝ E).toLinearMap.comp ((tripleCoordinate a b c).rTensor E)

@[simp] private theorem coordinateEntry_tmul (a b c : Axis) (s : FormJets) (x : E) :
    coordinateEntry a b c (s ⊗ₜ[ℝ] x) = tripleCoordinate a b c s • x := by
  simp [coordinateEntry]

private theorem coordinateEntry_swap (a b c : Axis) :
    (coordinateEntry a c b : (FormJets ⊗[ℝ] E) →ₗ[ℝ] E) = -coordinateEntry a b c := by
  apply TensorProduct.ext'
  intro s x
  rw [coordinateEntry_tmul, LinearMap.neg_apply, coordinateEntry_tmul,
    tripleCoordinate_swap a b c, LinearMap.neg_apply, neg_smul]

/-- The coordinates of a tensor with the derivative slot first and the
skew two-form slots second and third. -/
def tensorJet : (FormJets ⊗[ℝ] E) →ₗ[ℝ] BianchiSymbol.Jet Axis E where
  toFun s := ⟨fun a b c => coordinateEntry a b c s, by
    intro a b c
    change coordinateEntry a c b s = -coordinateEntry a b c s
    rw [coordinateEntry_swap, LinearMap.neg_apply]⟩
  map_add' s t := by
    apply Subtype.ext
    funext a b c
    exact map_add (coordinateEntry a b c) s t
  map_smul' r s := by
    apply Subtype.ext
    funext a b c
    exact (coordinateEntry a b c).map_smul r s

/-- Assemble the skew pair using all ordered coordinate pairs. -/
def assembleJet (J : BianchiSymbol.Jet Axis E) : FormJets ⊗[ℝ] E :=
  (2 : ℝ)⁻¹ • ∑ a : Axis, ∑ b : Axis, ∑ c : Axis,
    (formBasis a ⊗ₜ[ℝ] wedgeTwo (formBasis b) (formBasis c)) ⊗ₜ[ℝ] J.val a b c

private theorem axisCoordinate_basis (i j : Axis) :
    formBasis.coord i (formBasis j) = if i = j then 1 else 0 := by
  simp [Module.Basis.coord_apply, Finsupp.single_apply, eq_comm]

private theorem tensorJet_assemble (J : BianchiSymbol.Jet Axis E) :
    tensorJet (assembleJet J) = J := by
  apply Subtype.ext
  funext i j k
  change coordinateEntry i j k (assembleJet J) = J.val i j k
  simp only [assembleJet, map_smul, map_sum, coordinateEntry_tmul, tripleCoordinate_tmul,
    pairCoordinate_wedge, axisCoordinate_basis]
  have h (a b c : Axis) :
      ((if i = a then (1 : ℝ) else 0) *
        ((if j = b then 1 else 0) * (if k = c then 1 else 0) -
          (if k = b then 1 else 0) * (if j = c then 1 else 0))) • J.val a b c =
      (if k = c then if j = b then if i = a then J.val a b c else 0 else 0 else 0) -
      (if j = c then if k = b then if i = a then J.val a b c else 0 else 0 else 0) := by
    split_ifs <;> simp
  simp_rw [h, Finset.sum_sub_distrib]
  simp only [Finset.sum_ite_eq, Finset.mem_univ, if_true]
  rw [J.prop i j k]
  module

private def tensorBasis : Module.Basis (Axis × D7Exterior.Index 2) ℝ FormJets :=
  formBasis.tensorProduct (formBasis.exteriorPower 2)

private theorem pairCoordinate_basis (s : D7Exterior.Index 2) :
    let e := s.val.orderIsoOfFin s.prop
    pairCoordinate (e 0).val (e 1).val = (formBasis.exteriorPower 2).coord s := by
  let e := s.val.orderIsoOfFin s.prop
  have he : (![formBasis.coord (e 0).val, formBasis.coord (e 1).val] : Fin 2 → _) =
      fun j => formBasis.coord (e j).val := by
    funext j
    fin_cases j <;> rfl
  change pairCoordinate (e 0).val (e 1).val = _
  rw [pairCoordinate, he]
  exact (exteriorPower.basis_coord ℝ 2 formBasis s).symm

private theorem tripleCoordinate_basis (a : Axis) (s : D7Exterior.Index 2) :
    let e := s.val.orderIsoOfFin s.prop
    tripleCoordinate a (e 0).val (e 1).val = tensorBasis.coord (a, s) := by
  apply TensorProduct.ext'
  intro x u
  rw [tripleCoordinate_tmul, pairCoordinate_basis]
  simp only [Module.Basis.coord_apply, tensorBasis, Module.Basis.tensorProduct_repr_tmul_apply,
    smul_eq_mul]
  exact mul_comm _ _

private theorem tensorJet_injective :
    Function.Injective (tensorJet : (FormJets ⊗[ℝ] E) →ₗ[ℝ] BianchiSymbol.Jet Axis E) := by
  intro s t h
  apply (TensorProduct.equivFinsuppOfBasisLeft tensorBasis).injective
  ext ⟨a, ij⟩
  let e := ij.val.orderIsoOfFin ij.prop
  have hentry : coordinateEntry a (e 0).val (e 1).val s =
      coordinateEntry a (e 0).val (e 1).val t :=
    congrArg (fun J : BianchiSymbol.Jet Axis E => J.val a (e 0).val (e 1).val) h
  have hcoord : tripleCoordinate a (e 0).val (e 1).val = tensorBasis.coord (a, ij) :=
    tripleCoordinate_basis a ij
  simpa only [TensorProduct.equivFinsuppOfBasisLeft_apply, coordinateEntry, LinearMap.comp_apply,
    LinearEquiv.coe_coe, hcoord] using hentry

/-- Tensor and skew-array descriptions of a first jet. -/
def jetEquiv : (FormJets ⊗[ℝ] E) ≃ₗ[ℝ] BianchiSymbol.Jet Axis E where
  __ := tensorJet
  invFun := assembleJet
  left_inv s := tensorJet_injective (tensorJet_assemble (tensorJet s))
  right_inv := tensorJet_assemble

private theorem coordinateEntry_average (a b c : Axis) (s : FormJets ⊗[ℝ] E) :
    coordinateEntry a b c (includeThree.rTensor E (wedgeJet.rTensor E s)) =
      (1 / 3 : ℝ) • BianchiSymbol.cyclicSum (tensorJet s).val a b c := by
  let p := (includeThree.rTensor E).comp (wedgeJet.rTensor E)
  have h : (coordinateEntry a b c).comp p =
      (1 / 3 : ℝ) • ((coordinateEntry a b c) + coordinateEntry b c a + coordinateEntry c a b) := by
    apply TensorProduct.ext'
    intro t x
    simp only [p, LinearMap.comp_apply, LinearMap.rTensor_tmul, coordinateEntry_tmul,
      LinearMap.smul_apply, LinearMap.add_apply, tripleCoordinate_average, mul_smul, add_smul]
  exact DFunLike.congr_fun h s

/-- The cyclic mean in the coordinate model is the projection obtained
by exterior alternation followed by the normalized three-form inclusion. -/
theorem cyclic_average_eq_projection (s : FormJets ⊗[ℝ] E) (a b c : Axis) :
    (BianchiSymbol.alternation (tensorJet s)).val.val a b c =
      (tensorJet (includeThree.rTensor E (wedgeJet.rTensor E s))).val a b c := by
  rw [BianchiSymbol.alternation_apply]
  change _ = coordinateEntry a b c (includeThree.rTensor E (wedgeJet.rTensor E s))
  rw [coordinateEntry_average]

/-- The coordinate closed-jet condition is exactly the kernel of wedge
alternation on the derivative and form slots. -/
theorem closed_tensorJet_iff (s : FormJets ⊗[ℝ] E) :
    BianchiSymbol.ClosedJet (tensorJet s) ↔ wedgeJet.rTensor E s = 0 := by
  have hsection : (wedgeJet.rTensor E).comp (includeThree.rTensor E) =
      LinearMap.id := by
    apply TensorProduct.ext'
    intro u x
    have h := DFunLike.congr_fun wedge_includeThree u
    simp only [LinearMap.comp_apply, LinearMap.rTensor_tmul, LinearMap.id_apply]
    exact congrArg (fun v => v ⊗ₜ[ℝ] x) h
  rw [BianchiSymbol.closed_iff_alternation_eq_zero]
  constructor
  · intro h
    have hj : tensorJet (includeThree.rTensor E (wedgeJet.rTensor E s)) = 0 := by
      apply Subtype.ext
      funext a b c
      rw [← cyclic_average_eq_projection, h]
      rfl
    have hz := tensorJet_injective (hj.trans (map_zero tensorJet).symm)
    have hp := DFunLike.congr_fun hsection (wedgeJet.rTensor E s)
    change wedgeJet.rTensor E
        (includeThree.rTensor E (wedgeJet.rTensor E s)) = _ at hp
    rw [hz, map_zero] at hp
    exact hp.symm
  · intro h
    apply Subtype.ext
    apply Subtype.ext
    funext a b c
    rw [cyclic_average_eq_projection, h, map_zero, map_zero]
    rfl

end Coefficients

section Trace

open D7SpinAction D7RealComparison

private abbrev sharp := metricDualEquiv.symm.toLinearEquiv

private def metricIso : Covector ≃ₗ[ℝ] Module.Dual ℝ Covector :=
  sharp.trans (Module.evalEquiv ℝ Vector)

private def metric (a b : Covector) : ℝ := metricIso a b

private theorem metric_symm (a b : Covector) : metric a b = metric b a := by
  obtain ⟨x, rfl⟩ := metricDualEquiv.toLinearEquiv.surjective a
  obtain ⟨y, rfl⟩ := metricDualEquiv.toLinearEquiv.surjective b
  simp only [metric, metricIso, LinearEquiv.trans_apply,
    Module.evalEquiv_apply, Module.Dual.eval_apply]
  have hs (v : Vector) : sharp (metricDualEquiv.toLinearEquiv v) = v :=
    metricDualEquiv.symm_apply_apply v
  rw [hs, hs]
  change WitnessW1.splitForm.associated y x = WitnessW1.splitForm.associated x y
  rw [QuadraticMap.associated_apply, QuadraticMap.associated_apply, add_comm y x]
  congr 1
  ring

private theorem metric_invariant (g : Spin) (a b : Covector) :
    metric (vectorRepresentation.dual g a) (vectorRepresentation.dual g b) = metric a b := by
  have h := DFunLike.congr_fun (metricDualEquiv.symm.isIntertwining' g) a
  change sharp (vectorRepresentation.dual g a) = vectorRepresentation g (sharp a) at h
  have hx : vectorRepresentation g⁻¹ (vectorRepresentation g (sharp a)) = sharp a := by
    change (vectorRepresentation g⁻¹ * vectorRepresentation g) (sharp a) = sharp a
    rw [← map_mul, inv_mul_cancel, map_one]
    rfl
  change b (vectorRepresentation g⁻¹ (sharp (vectorRepresentation.dual g a))) = b (sharp a)
  rw [h, hx]

private def traceTerm (y z : Covector) : Covector →ₗ[ℝ] Covector :=
  (metricIso.toLinearMap.flip y).smulRight z - (metricIso.toLinearMap.flip z).smulRight y

private def traceAlt : Covector [⋀^Fin 2]→ₗ[ℝ] (Covector →ₗ[ℝ] Covector) where
  toFun w := traceTerm (w 0) (w 1)
  map_update_add' w i a b := by
    apply LinearMap.ext
    intro x
    fin_cases i <;> simp [traceTerm, Function.update, smul_add, add_smul] <;> module
  map_update_smul' w i c a := by
    apply LinearMap.ext
    intro x
    fin_cases i <;> simp [traceTerm, Function.update, smul_smul, smul_sub] <;> module
  map_eq_zero_of_eq' w i j h hij := by
    fin_cases i <;> fin_cases j <;> try exact (hij rfl).elim
    all_goals
      apply LinearMap.ext
      intro x
      have he : w 0 = w 1 := by first | exact h | exact h.symm
      simp [traceTerm, he]

/-- Contract the derivative slot against the form slots with the inverse split metric. -/
def traceJet : FormJets →ₗ[ℝ] Covector :=
  TensorProduct.lift (exteriorPower.alternatingMapLinearEquiv
    (R := ℝ) (M := Covector) (N := Covector →ₗ[ℝ] Covector) (n := 2) traceAlt).flip

@[simp] theorem traceJet_pure (x y z : Covector) :
    traceJet (x ⊗ₜ[ℝ] wedgeTwo y z) = metric x y • z - metric x z • y := by
  simp [traceJet, wedgeTwo, traceAlt, traceTerm, metric]

theorem traceJet_equivariant (g : Spin) :
    traceJet.comp (TensorProduct.map (vectorRepresentation.dual g)
      (exteriorPower.map 2 (vectorRepresentation.dual g))) =
      (vectorRepresentation.dual g).comp traceJet := by
  apply tensor_ext (W := Covector)
  intro x y z
  simp only [LinearMap.comp_apply, TensorProduct.map_tmul, map_wedgeTwo, traceJet_pure,
    metric_invariant, map_sub, map_smul]

theorem trace_includeThree : traceJet.comp includeThree = 0 := by
  apply three_ext (W := Covector)
  intro x y z
  simp only [LinearMap.comp_apply, includeThree_pure, map_smul, map_add, traceJet_pure,
    metric_symm y x, metric_symm z x, metric_symm z y, LinearMap.zero_apply]
  module

private def tensorEval : (Covector ⊗[ℝ] Covector) ≃ₗ[ℝ] (Covector →ₗ[ℝ] Covector) :=
  (TensorProduct.congr metricIso (LinearEquiv.refl ℝ Covector)).trans
    (dualTensorHomEquiv ℝ Covector Covector)

private theorem tensorEval_tmul (x y z : Covector) :
    tensorEval (x ⊗ₜ[ℝ] y) z = metric x z • y := by
  change dualTensorHom ℝ Covector Covector (metricIso x ⊗ₜ[ℝ] y) z = _
  rw [dualTensorHom_apply]
  rfl

private def metricBasis (i : Axis) : Covector := metricIso.symm (formBasis.coord i)

private theorem metricBasis_apply (i : Axis) (x : Covector) :
    metric (metricBasis i) x = formBasis.repr x i := by
  rw [metric, metricBasis, metricIso.apply_symm_apply, Module.Basis.coord_apply]

private theorem metricBasis_sum (x : Covector) :
    (∑ i : Axis, metric (metricBasis i) x • formBasis i) = x := by
  simpa only [metricBasis_apply] using formBasis.sum_repr x

private def metricTensor : Covector ⊗[ℝ] Covector :=
  ∑ i : Axis, metricBasis i ⊗ₜ[ℝ] formBasis i

private theorem metricTensor_invariant (g : Spin) :
    TensorProduct.map (vectorRepresentation.dual g) (vectorRepresentation.dual g) metricTensor =
      metricTensor := by
  apply tensorEval.injective
  apply LinearMap.ext
  intro v
  have hv : vectorRepresentation.dual g (vectorRepresentation.dual g⁻¹ v) = v := by
    change (vectorRepresentation.dual g * vectorRepresentation.dual g⁻¹) v = v
    rw [← map_mul, mul_inv_cancel, map_one]
    rfl
  obtain ⟨x, rfl⟩ : ∃ x, vectorRepresentation.dual g x = v := ⟨_, hv⟩
  simp only [metricTensor, map_sum, TensorProduct.map_tmul, LinearMap.sum_apply,
    tensorEval_tmul, metric_invariant, metricBasis_sum]
  simp_rw [← map_smul (vectorRepresentation.dual g)]
  rw [← map_sum, metricBasis_sum]

private theorem wedgeTwo_add_left (x y z : Covector) :
    wedgeTwo (x + y) z = wedgeTwo x z + wedgeTwo y z := by
  apply Subtype.ext
  simp [coe_wedgeTwo, add_mul]

private theorem wedgeTwo_add_right (x y z : Covector) :
    wedgeTwo x (y + z) = wedgeTwo x y + wedgeTwo x z := by
  apply Subtype.ext
  simp [coe_wedgeTwo, mul_add]

private theorem wedgeTwo_smul_left (c : ℝ) (x y : Covector) :
    wedgeTwo (c • x) y = c • wedgeTwo x y := by
  apply Subtype.ext
  simp [coe_wedgeTwo]

private theorem wedgeTwo_smul_right (c : ℝ) (x y : Covector) :
    wedgeTwo x (c • y) = c • wedgeTwo x y := by
  apply Subtype.ext
  simp [coe_wedgeTwo]

private def rawTraceSection : Covector →ₗ[ℝ] FormJets where
  toFun x := ∑ i : Axis, metricBasis i ⊗ₜ[ℝ] wedgeTwo (formBasis i) x
  map_add' x y := by simp [wedgeTwo_add_right, TensorProduct.tmul_add, Finset.sum_add_distrib]
  map_smul' c x := by simp [wedgeTwo_smul_right, TensorProduct.tmul_smul, Finset.smul_sum]

private theorem trace_rawSection (x : Covector) : traceJet (rawTraceSection x) = (13 : ℝ) • x := by
  change traceJet (∑ i : Axis, metricBasis i ⊗ₜ[ℝ] wedgeTwo (formBasis i) x) = _
  simp only [map_sum, traceJet_pure, metricBasis_apply, Module.Basis.repr_self, Finsupp.single_eq_same,
    one_smul, Finset.sum_sub_distrib, Finset.sum_const, Finset.card_univ, Fintype.card_fin,
    formBasis.sum_repr]
  module

private def insertVector (x : Covector) : (Covector ⊗[ℝ] Covector) →ₗ[ℝ] FormJets :=
  TensorProduct.map LinearMap.id
    { toFun := fun y => wedgeTwo y x
      map_add' := fun y z => wedgeTwo_add_left y z x
      map_smul' := fun c y => wedgeTwo_smul_left c y x }

private theorem insertVector_metricTensor (x : Covector) :
    insertVector x metricTensor = rawTraceSection x := by
  simp only [insertVector, metricTensor, map_sum, TensorProduct.map_tmul, LinearMap.id_apply]
  rfl

private theorem rawTraceSection_equivariant (g : Spin) :
    rawTraceSection.comp (vectorRepresentation.dual g) =
      (TensorProduct.map (vectorRepresentation.dual g)
        (exteriorPower.map 2 (vectorRepresentation.dual g))).comp rawTraceSection := by
  let f := vectorRepresentation.dual g
  apply LinearMap.ext
  intro x
  have h : (TensorProduct.map f (exteriorPower.map 2 f)).comp (insertVector x) =
      (insertVector (f x)).comp (TensorProduct.map f f) := by
    apply TensorProduct.ext'
    intro y z
    change TensorProduct.map f (exteriorPower.map 2 f) (y ⊗ₜ[ℝ] wedgeTwo z x) =
      (insertVector (f x)) (TensorProduct.map f f (y ⊗ₜ[ℝ] z))
    simp only [TensorProduct.map_tmul, map_wedgeTwo]
    rfl
  have ht := DFunLike.congr_fun h metricTensor
  change TensorProduct.map f (exteriorPower.map 2 f) (insertVector x metricTensor) =
    insertVector (f x) (TensorProduct.map f f metricTensor) at ht
  rw [show TensorProduct.map f f metricTensor = metricTensor from metricTensor_invariant g,
    insertVector_metricTensor, insertVector_metricTensor] at ht
  exact ht.symm

private def alternatingResidual : FormJets →ₗ[ℝ] FormJets where
  toFun x := x - includeThree (wedgeJet x)
  map_add' x y := by simp only [map_add]; abel
  map_smul' c x := by simp only [map_smul, smul_sub, RingHom.id_apply]

/-- A trace section with its alternating projection removed. -/
def includeVector : Covector →ₗ[ℝ] FormJets :=
  (1 / 13 : ℝ) • alternatingResidual.comp rawTraceSection

theorem wedge_includeVector : wedgeJet.comp includeVector = 0 := by
  apply LinearMap.ext
  intro x
  change wedgeJet ((1 / 13 : ℝ) • (rawTraceSection x - includeThree (wedgeJet (rawTraceSection x)))) = 0
  have h : wedgeJet (includeThree (wedgeJet (rawTraceSection x))) = wedgeJet (rawTraceSection x) :=
    DFunLike.congr_fun wedge_includeThree _
  rw [map_smul, map_sub, h, sub_self, smul_zero]

theorem trace_includeVector : traceJet.comp includeVector = LinearMap.id := by
  apply LinearMap.ext
  intro x
  change traceJet ((1 / 13 : ℝ) • (rawTraceSection x - includeThree (wedgeJet (rawTraceSection x)))) = x
  have h : traceJet (includeThree (wedgeJet (rawTraceSection x))) = 0 :=
    DFunLike.congr_fun trace_includeThree _
  rw [map_smul, map_sub, h, sub_zero, trace_rawSection, smul_smul]
  norm_num

theorem includeVector_equivariant (g : Spin) :
    includeVector.comp (vectorRepresentation.dual g) =
      (TensorProduct.map (vectorRepresentation.dual g)
        (exteriorPower.map 2 (vectorRepresentation.dual g))).comp includeVector := by
  let f := vectorRepresentation.dual g
  let F := TensorProduct.map f (exteriorPower.map 2 f)
  have hw : wedgeJet.comp F = (exteriorPower.map 3 f).comp wedgeJet := wedgeJet_natural f
  have hi : includeThree.comp (exteriorPower.map 3 f) = F.comp includeThree := includeThree_natural f
  have hr : rawTraceSection.comp f = F.comp rawTraceSection := rawTraceSection_equivariant g
  apply LinearMap.ext
  intro x
  have hr' : rawTraceSection (f x) = F (rawTraceSection x) := DFunLike.congr_fun hr x
  have hw' : wedgeJet (F (rawTraceSection x)) =
      exteriorPower.map 3 f (wedgeJet (rawTraceSection x)) := DFunLike.congr_fun hw (rawTraceSection x)
  have hi' : includeThree (exteriorPower.map 3 f (wedgeJet (rawTraceSection x))) =
      F (includeThree (wedgeJet (rawTraceSection x))) :=
    DFunLike.congr_fun hi (wedgeJet (rawTraceSection x))
  change (1 / 13 : ℝ) • (rawTraceSection (f x) - includeThree (wedgeJet (rawTraceSection (f x)))) =
    F ((1 / 13 : ℝ) • (rawTraceSection x - includeThree (wedgeJet (rawTraceSection x))))
  rw [hr', hw', hi', map_smul, map_sub]

end Trace

end
end GeometricUnity.D7RealJets
~~~

[Return to file index](#file-index)

## D7RealRanks.lean {#source-d7realranks-lean}

Transfers the complex intertwiner counts to the real operator and exterior-symbol spaces.

~~~lean
import D7Final
import D7RealComparison
import D7RootGeneration
import Mathlib.LinearAlgebra.Charpoly.BaseChange

/-! # Dimensions of real Spin(7,7)-equivariant maps -/

namespace GeometricUnity.D7RealTheorem

open D7Exterior D7VectorGrades D7VectorTensor D7SpinAction D7SpinNullFrame
open D7RealComparison D7RootInterpolation D7RootGeneration
open scoped DirectSum TensorProduct BigOperators

noncomputable section

set_option backward.isDefEq.respectTransparency false
set_option maxHeartbeats 1200000

def transportHom {K G M N U W : Type*} [CommSemiring K] [Monoid G]
    [AddCommMonoid M] [Module K M] [AddCommMonoid N] [Module K N]
    [AddCommMonoid U] [Module K U] [AddCommMonoid W] [Module K W]
    {ρ : Representation K G M} {τ : Representation K G N}
    {σ : Representation K G U} {π : Representation K G W}
    (e : ρ.Equiv σ) (f : τ.Equiv π) : ρ.IntertwiningMap τ ≃ₗ[K] σ.IntertwiningMap π where
  toFun T := f.toIntertwiningMap.comp (T.comp e.symm.toIntertwiningMap)
  invFun T := f.symm.toIntertwiningMap.comp (T.comp e.toIntertwiningMap)
  left_inv T := by ext x; simp
  right_inv T := by ext x; simp
  map_add' T S := by ext x; simp
  map_smul' c T := by ext x; simp

private theorem toMatrix_complexify {M ι : Type*} [AddCommGroup M] [Module ℝ M]
    [Fintype ι] [DecidableEq ι] (b : Module.Basis ι ℝ M) (f : Module.End ℝ M) :
    D7Classification.complexMatrices (LinearMap.toMatrix b b f) =
      LinearMap.toMatrix (b.baseChange ℂ) (b.baseChange ℂ) (f.baseChange ℂ) := by
  ext i j
  simp [D7Classification.complexMatrices, LinearMap.toMatrix_apply, ← Algebra.algebraMap_eq_smul_one]

private theorem finrank_complexify {U W : Type} [AddCommGroup U] [Module ℝ U]
    [AddCommGroup W] [Module ℝ W] [Module.Finite ℝ U] [Module.Finite ℝ W]
    (ρ : Representation ℝ Spin U) (τ : Representation ℝ Spin W) :
    Module.finrank ℝ (ρ.IntertwiningMap τ) =
      Module.finrank ℂ ((complexify ρ).IntertwiningMap (complexify τ)) := by
  let b := Module.Free.chooseBasis ℝ U
  let c := Module.Free.chooseBasis ℝ W
  let ρm := fun g => LinearMap.toMatrix b b (ρ g)
  let τm := fun g => LinearMap.toMatrix c c (τ g)
  let e := D7Final.intertwinerMatrices b c ρ τ
  have hρ : D7Classification.complexMatrices ∘ ρm =
      fun g => LinearMap.toMatrix (b.baseChange ℂ) (b.baseChange ℂ) (complexify ρ g) :=
    funext fun g => toMatrix_complexify b (ρ g)
  have hτ : D7Classification.complexMatrices ∘ τm =
      fun g => LinearMap.toMatrix (c.baseChange ℂ) (c.baseChange ℂ) (complexify τ g) :=
    funext fun g => toMatrix_complexify c (τ g)
  exact e.finrank_eq.trans (D7Final.real_dimension_of_comparison ρm τm (by
    change ↥(D7Classification.matrixIntertwiners (D7Classification.complexMatrices ∘ ρm)
      (D7Classification.complexMatrices ∘ τm)) ≃ₗ[ℂ] _
    rw [hρ, hτ]
    exact (D7Final.intertwinerMatrices (b.baseChange ℂ) (c.baseChange ℂ)
      (complexify ρ) (complexify τ)).symm))

section Blocks

variable {G I J : Type*} [Monoid G] [Fintype I] [Fintype J] [DecidableEq I] [DecidableEq J]
variable {U : I → Type*} {W : J → Type*}
variable [∀ i, AddCommGroup (U i)] [∀ j, AddCommGroup (W j)]
variable [∀ i, Module ℂ (U i)] [∀ j, Module ℂ (W j)]
variable (ρ : ∀ i, Representation ℂ G (U i)) (τ : ∀ j, Representation ℂ G (W j))

private def block (T : (⨁ i, U i) →ₗ[ℂ] ⨁ j, W j) (i : I) (j : J) : U i →ₗ[ℂ] W j :=
  (DirectSum.component ℂ J W j).comp (T.comp (DirectSum.lof ℂ I U i))

omit [Fintype I] [Fintype J] [DecidableEq J] in
private theorem directSum_comm_iff (T : (⨁ i, U i) →ₗ[ℂ] ⨁ j, W j) (g : G) :
    T.comp (Representation.directSum ρ g) = (Representation.directSum τ g).comp T ↔
      ∀ i j, (block T i j).comp (ρ i g) = (τ j g).comp (block T i j) := by
  constructor
  · intro h i j
    apply LinearMap.ext
    intro x
    have hx := DFunLike.congr_fun h (DirectSum.lof ℂ I U i x)
    have hj := congrArg (DirectSum.component ℂ J W j) hx
    simpa [block, Representation.directSum_apply, ← DirectSum.apply_eq_component] using hj
  · intro h
    apply DirectSum.linearMap_ext
    intro i
    apply LinearMap.ext
    intro x
    apply DirectSum.ext_component ℂ
    intro j
    simpa [block, Representation.directSum_apply, ← DirectSum.apply_eq_component]
      using DFunLike.congr_fun (h i j) x

private def assembleBlocks (B : ∀ i j, U i →ₗ[ℂ] W j) : (⨁ i, U i) →ₗ[ℂ] ⨁ j, W j :=
  DirectSum.toModule ℂ I _ fun i =>
    (DirectSum.linearEquivFunOnFintype ℂ J W).symm.toLinearMap.comp (LinearMap.pi (B i))

omit [Fintype I] [DecidableEq J] in
@[simp] private theorem block_assemble (B : ∀ i j, U i →ₗ[ℂ] W j) (i : I) (j : J) :
    block (assembleBlocks B) i j = B i j := by
  apply LinearMap.ext
  intro x
  simp [block, assembleBlocks, ← DirectSum.apply_eq_component]
  exact congrFun ((DirectSum.linearEquivFunOnFintype ℂ J W).apply_symm_apply ((LinearMap.pi (B i)) x)) j

omit [Fintype I] [Fintype J] [DecidableEq J] in
private theorem blocks_injective :
    Function.Injective (fun T : (⨁ i, U i) →ₗ[ℂ] ⨁ j, W j => fun i j => block T i j) := by
  intro T S h
  apply DirectSum.linearMap_ext
  intro i
  apply LinearMap.ext
  intro x
  apply DirectSum.ext_component ℂ
  intro j
  exact DFunLike.congr_fun (congrFun (congrFun h i) j) x

private def blockHom :
    (Representation.directSum ρ).IntertwiningMap (Representation.directSum τ) ≃ₗ[ℂ]
      (∀ i j, (ρ i).IntertwiningMap (τ j)) where
  toFun T i j := ⟨block T.toLinearMap i j, fun g =>
    (directSum_comm_iff ρ τ T.toLinearMap g).mp (T.isIntertwining' g) i j⟩
  invFun B := ⟨assembleBlocks (fun i j => (B i j).toLinearMap), fun g =>
    (directSum_comm_iff ρ τ _ g).mpr fun i j => by simpa using (B i j).isIntertwining' g⟩
  left_inv T := by
    apply Representation.IntertwiningMap.ext
    apply blocks_injective
    funext i j
    exact block_assemble _ i j
  right_inv B := by
    funext i j
    exact Representation.IntertwiningMap.ext (block_assemble _ i j)
  map_add' T S := by
    funext i j
    apply Representation.IntertwiningMap.ext
    apply LinearMap.ext
    intro x
    exact map_add (DirectSum.component ℂ J W j) _ _
  map_smul' a T := by
    funext i j
    apply Representation.IntertwiningMap.ext
    apply LinearMap.ext
    intro x
    exact map_smul (DirectSum.component ℂ J W j) _ _

end Blocks

private abbrev exteriorTensorAction (r k : ℕ) :
    Representation ℂ splitSpecialOrthogonal (Ext r ⊗[ℂ] Ext k) :=
  (exteriorRepresentation r).tprod (exteriorRepresentation k)

private def actionSpanEquiv (r k s l : ℕ) :
    (exteriorTensorAction r k).IntertwiningMap (exteriorTensorAction s l) ≃ₗ[ℂ]
    Representation.IntertwiningMap ((exteriorTensorAction r k).comp spinToSO)
      ((exteriorTensorAction s l).comp spinToSO) := by
  refine D7Final.restrictGroupEquiv (U := Ext r ⊗[ℂ] Ext k) (W := Ext s ⊗[ℂ] Ext l)
    spinToSO (exteriorTensorAction r k) (exteriorTensorAction s l) ?_
  intro g
  exact splitSO_tensorActions_mem_spin_span r k s l g

private def exteriorOne :
    (exteriorRepresentation 1).Equiv vectorAction :=
  Representation.Equiv.mk (exteriorPower.oneEquiv ℂ Space) fun f =>
    exteriorPower.oneEquiv_naturality f.val

def liftTensorEquiv {K G U W E : Type*} [CommSemiring K] [Monoid G]
    [AddCommMonoid U] [Module K U] [AddCommMonoid W] [Module K W]
    [AddCommMonoid E] [Module K E]
    {ρ : Representation K G U} {τ : Representation K G W}
    (e : ρ.Equiv τ) (σ : Representation K G E) :
    (ρ.tprod σ).Equiv (τ.tprod σ) := by
  refine Representation.Equiv.mk (TensorProduct.congr e.toLinearEquiv (LinearEquiv.refl K E))
    fun g => ?_
  apply TensorProduct.ext'
  intro x y
  have h := DFunLike.congr_fun (e.isIntertwining' g) x
  change e (ρ g x) = τ g (e x) at h
  simp [Representation.tprod_apply, h]

private def restrictRepEquiv {G H U W : Type*} [Monoid G] [Monoid H]
    [AddCommMonoid U] [Module ℂ U] [AddCommMonoid W] [Module ℂ W]
    {ρ : Representation ℂ G U} {τ : Representation ℂ G W}
    (φ : H →* G) (e : ρ.Equiv τ) : Representation.Equiv (ρ.comp φ) (τ.comp φ) :=
  Representation.Equiv.mk e.toLinearEquiv fun g => e.isIntertwining' (φ g)

private def exteriorUnit (l : ℕ) :
    (((exteriorRepresentation 0).tprod (exteriorRepresentation l))).Equiv
      (exteriorRepresentation l) := by
  let e := (TensorProduct.congr (exteriorPower.zeroEquiv ℂ Space) (LinearEquiv.refl ℂ (Ext l))).trans
    (TensorProduct.lid ℂ (Ext l))
  refine Representation.Equiv.mk e fun g => ?_
  apply TensorProduct.ext'
  intro x y
  have h := DFunLike.congr_fun (exteriorPower.zeroEquiv_naturality g.val) x
  change exteriorPower.zeroEquiv ℂ Space (exteriorPower.map 0 g.val x) =
    exteriorPower.zeroEquiv ℂ Space x at h
  simp [e, Representation.tprod_apply, exteriorRepresentation, h]

private def unrestrictedBlock (k l : Fin 15) :
    Representation.IntertwiningMap (((exteriorRepresentation 2).tprod
      (exteriorRepresentation k.val)).comp spinToSO)
      ((vectorAction.tprod (exteriorRepresentation l.val)).comp spinToSO) ≃ₗ[ℂ]
    D7Unrestricted.Intertwiners k.val l.val :=
  let e := liftTensorEquiv exteriorOne (exteriorRepresentation l.val)
  (transportHom (Representation.Equiv.refl ((exteriorTensorAction 2 k.val).comp spinToSO))
    (restrictRepEquiv spinToSO e.symm)).trans
    ((actionSpanEquiv 2 k.val 1 l.val).symm.trans
      (transportHom (Representation.Equiv.refl (exteriorTensorAction 2 k.val)) e))

private def exteriorBlock (r : ℕ) (k l : Fin 15) :
    Representation.IntertwiningMap (((exteriorRepresentation r).tprod
      (exteriorRepresentation k.val)).comp spinToSO)
      ((exteriorRepresentation l.val).comp spinToSO) ≃ₗ[ℂ]
    D7TripleInvariants.ExteriorIntertwiners r k.val l.val :=
  let e := exteriorUnit l.val
  (transportHom (Representation.Equiv.refl ((exteriorTensorAction r k.val).comp spinToSO))
    (restrictRepEquiv spinToSO e.symm)).trans
    ((actionSpanEquiv r k.val 0 l.val).symm.trans
      (transportHom (Representation.Equiv.refl (exteriorTensorAction r k.val)) e))

abbrev FormCoefficients (k : ℕ) := (⋀[ℝ]^k Covector) ⊗[ℝ] Coefficients
abbrev OneFormCoefficients := Covector ⊗[ℝ] Coefficients

abbrev formCoefficientsAction (k : ℕ) : Representation ℝ Spin (FormCoefficients k) :=
  (formAction k).tprod coefficientAction

abbrev oneFormCoefficientsAction : Representation ℝ Spin OneFormCoefficients :=
  vectorRepresentation.dual.tprod coefficientAction

abbrev Operators := (formCoefficientsAction 2).IntertwiningMap oneFormCoefficientsAction
abbrev ExteriorSymbols (r : ℕ) := (formCoefficientsAction r).IntertwiningMap coefficientAction

private theorem finiteIntertwiners {G U W I J : Type} [Monoid G]
    [AddCommGroup U] [Module ℂ U] [AddCommGroup W] [Module ℂ W]
    [Fintype I] [Fintype J] [DecidableEq I] [DecidableEq J]
    (b : Module.Basis I ℂ U) (c : Module.Basis J ℂ W)
    (ρ : Representation ℂ G U) (τ : Representation ℂ G W) :
    Module.Finite ℂ (ρ.IntertwiningMap τ) := by
  let e := D7Final.intertwinerMatrices b c ρ τ
  exact Module.Finite.of_injective (_root_.Submodule.subtype _ ∘ₗ e.toLinearMap)
    (Subtype.val_injective.comp e.injective)

private theorem finrank_blocks {M : Fin 15 → Fin 15 → Type}
    [∀ k l, AddCommGroup (M k l)] [∀ k l, Module ℂ (M k l)]
    [∀ k l, Module.Finite ℂ (M k l)] :
    Module.finrank ℂ (∀ k l, M k l) = ∑ k, ∑ l, Module.finrank ℂ (M k l) := by
  rw [Module.finrank_pi_fintype]
  exact Finset.sum_congr rfl fun k _ => Module.finrank_pi_fintype ℂ

theorem unrestricted_dimension : Module.finrank ℝ Operators = 200 := by
  let e := transportHom (formCoefficientComparison 2) covectorCoefficientComparison
  have h := finrank_complexify (U := FormCoefficients 2) (W := OneFormCoefficients)
    (formCoefficientsAction 2) oneFormCoefficientsAction
  refine h.trans (e.finrank_eq.trans ?_)
  let b := blockHom (U := fun k : Fin 15 => Ext 2 ⊗[ℂ] Ext k.val)
    (W := fun l : Fin 15 => Space ⊗[ℂ] Ext l.val) (fun k : Fin 15 =>
      ((exteriorRepresentation 2).tprod (exteriorRepresentation k.val)).comp spinToSO)
    (fun l : Fin 15 => (vectorAction.tprod (exteriorRepresentation l.val)).comp spinToSO)
  refine (b.trans (LinearEquiv.piCongrRight fun k => LinearEquiv.piCongrRight (unrestrictedBlock k))).finrank_eq.trans ?_
  have finite (k l : Fin 15) : Module.Finite ℂ (D7Unrestricted.Intertwiners k.val l.val) :=
    finiteIntertwiners (U := D7Unrestricted.Source k.val) (W := Product l.val)
      ((axisBasis.exteriorPower 2).tensorProduct (axisBasis.exteriorPower k.val))
      (axisBasis.tensorProduct (axisBasis.exteriorPower l.val))
      (D7Unrestricted.sourceAction k.val) (D7VectorGrades.action l.val)
  exact (@finrank_blocks (fun k l => D7Unrestricted.Intertwiners k.val l.val) _ _ finite).trans
    D7Unrestricted.unrestricted_total

private def coefficientComparison :
    (complexify coefficientAction).Equiv (coefficientGradeAction.comp spinToSO) :=
  Representation.Equiv.mk coefficientComplexEquiv coefficientComplexEquiv_intertwines

private theorem exterior_symbol_rank (r : ℕ) : Module.finrank ℝ (ExteriorSymbols r) =
      ∑ k : Fin 15, ∑ l : Fin 15,
        Module.finrank ℂ (D7TripleInvariants.ExteriorIntertwiners r k.val l.val) := by
  let e := transportHom (formCoefficientComparison r) coefficientComparison
  let : Module.Finite ℝ (⋀[ℝ]^r Covector) :=
    Module.Finite.of_basis ((Pi.basisFun ℝ Axis).dualBasis.exteriorPower r)
  have h := finrank_complexify (U := FormCoefficients r) (W := Coefficients)
    (formCoefficientsAction r) coefficientAction
  refine h.trans (e.finrank_eq.trans ?_)
  let b := blockHom (U := fun k : Fin 15 => Ext r ⊗[ℂ] Ext k.val)
    (W := fun l : Fin 15 => Ext l.val) (fun k : Fin 15 =>
      ((exteriorRepresentation r).tprod (exteriorRepresentation k.val)).comp spinToSO)
    (fun l : Fin 15 => (exteriorRepresentation l.val).comp spinToSO)
  refine (b.trans
    (LinearEquiv.piCongrRight fun k => LinearEquiv.piCongrRight (exteriorBlock r k))).finrank_eq.trans ?_
  have finite (k l : Fin 15) : Module.Finite ℂ (D7TripleInvariants.ExteriorIntertwiners r k.val l.val) :=
    finiteIntertwiners (U := Ext r ⊗[ℂ] Ext k.val) (W := Ext l.val)
      ((axisBasis.exteriorPower r).tensorProduct (axisBasis.exteriorPower k.val))
      (axisBasis.exteriorPower l.val) (exteriorTensorAction r k.val) (exteriorRepresentation l.val)
  exact @finrank_blocks (fun k l => D7TripleInvariants.ExteriorIntertwiners r k.val l.val) _ _ finite

theorem exterior_symbol_dimensions :
    Module.finrank ℝ (ExteriorSymbols 1) = 56 ∧ Module.finrank ℝ (ExteriorSymbols 3) = 96 :=
  ⟨(exterior_symbol_rank 1).trans D7TripleMultiplicity.vector_and_alternating_totals.1,
   (exterior_symbol_rank 3).trans D7TripleMultiplicity.vector_and_alternating_totals.2⟩

end
end GeometricUnity.D7RealTheorem
~~~

[Return to file index](#file-index)

## GU-test.py {#source-gu-test-py}

Runs the six groups of computational and numerical checks reported in the benchmark tables.

~~~python
#!/usr/bin/env python3
"""
Unified Computational & Symbolic Verification Suite for Geometric Unity
=======================================================================
The program runs six groups of verification checks using exact integer counts
and BLAS-accelerated matrix calculations. The final line reports the peak
allocation measured by tracemalloc for the current run.

  [V1] Cl(7,7) = End(C^128), J vs J' = i*J*Gamma_*, Eq. (3.27) Checkerboard,
       and u(64,64) Cartan / Killing Decomposition (8190 + 2 compact, 8192 coset).
  [V2] 6-Op to 3-Blade Reduction (Prop. 2), 4-Jet Proof Table, 8D Equivariant
       Space -> 4D Bianchi SVD, 3-Example Independence, 5th Trace Operator,
       and Exact D_7 = so(14,C) Klimyk Representation Count (200 -> 96).
  [V3] Non-Degenerate 14D Curved Riemann Normal Coordinates, Real Einstein
       Tensor Reconstruction (Prop. 1), Differential Bianchi Identity, and
       Finite U(64,64) Gauge Covariance (Bare vs Dressed across all 4 operators).
  [V4] Non-Abelian Bianchi Identity (D_A F_A = 0), Non-Circular Direct 3-Blade
       D_A-Divergence Formula, and D_{B_w} Torsion-Source Identity (Prop. 3).
  [V5] Typed Exterior Algebra on (R^{7,7}, eta), Hodge Star Involution ** = (-1)^{p+1},
       Eq. (9.3) Bracket Audit, Corrected 2-Bracket Realization, Exact Clifford
       Obstruction Witness (-8/3 gamma^{01234}), and Sparse Finite Differences.
  [V6] Full Derivative-Dependent 14D Periodic Action (Eq. 9.4) with F_B = 0,
       1D (N = 8, 10, 14) & Full 2D (N = 8, 10) Continuum Grid Convergence,
       -256 Dressed Kinetic Witness, Mixed-Harmonic Integration by Parts,
       Commutator-Sector Invisibility, Case A & Case B 4-Channel Variations,
       and True Fixed-A Coupled Dressing Variation (E_eps = D_{A,a} E_A^a).
"""

from functools import lru_cache
import gc
import hashlib
from itertools import combinations
from pathlib import Path
import platform
import sys
import time
import tracemalloc
import numpy as np

tracemalloc.start()
t0 = time.perf_counter()


class LiveProgress:
    """In-place live terminal progress bar with elapsed time & ETA (< 80 cols)."""
    def __init__(self, tag: str, total: int, desc: str, width: int = 18):
        self.tag = tag
        self.total = max(1, total)
        self.desc = desc
        self.width = width
        self.t_start = time.perf_counter()
        self.last_draw = 0.0
        self.update(0, force=True)

    def update(self, current: int, force: bool = False):
        now = time.perf_counter()
        if not force and (now - self.last_draw) < 0.04 and current < self.total:
            return
        self.last_draw = now
        frac = min(1.0, current / self.total)
        filled = int(self.width * frac)
        bar = "#" * filled + "-" * (self.width - filled)
        elapsed = now - self.t_start
        eta = (elapsed / frac - elapsed) if frac > 0.02 else 0.0
        line = (f"\r[{self.tag}] [{bar}] {int(frac * 100):3d}% ({current}/{self.total}) "
                f"{self.desc} | {elapsed:4.1f}s ETA {eta:3.1f}s")
        sys.stdout.write(f"{line[:79]:<79}")
        sys.stdout.flush()

    def finish(self, summary: str):
        total_elapsed = time.perf_counter() - t0
        line = f"\r[{self.tag} | {total_elapsed:5.2f}s] {summary}"
        sys.stdout.write(f"{line:<79}\n")
        sys.stdout.flush()


# ==============================================================================
# VERIFICATION GROUP 1: Cl_C(7,7) = End(C^128), Hermitian Forms J vs J' = i J Gamma_*,
#              Eq. (3.27) Checkerboard, and u(64,64) Signature Decomposition
# ==============================================================================
p1 = LiveProgress("V1", 18, "Cl(7,7), J vs J', Eq.(3.27)")

DIM = 14
ETA_REAL = np.array([1.0] * 7 + [-1.0] * 7, dtype=np.float64)
ETA_DIAG = ETA_REAL.astype(np.complex128)
ETA_MAT = np.diag(ETA_DIAG)
ALL_INDICES = tuple(range(DIM))

I2 = np.eye(2, dtype=np.complex128)
sx = np.array([[0, 1], [1, 0]], dtype=np.complex128)
sy = np.array([[0, -1j], [1j, 0]], dtype=np.complex128)
sz = np.array([[1, 0], [0, -1]], dtype=np.complex128)


def kron_list(mats):
    res = mats[0]
    for m in mats[1:]:
        res = np.kron(res, m)
    return res


gammas_eucl = []
for k in range(7):
    gammas_eucl.append(kron_list([sz] * k + [sx] + [I2] * (6 - k)))
    gammas_eucl.append(kron_list([sz] * k + [sy] + [I2] * (6 - k)))

gammas = np.array([gammas_eucl[a] if a < 7 else 1j * gammas_eucl[a] for a in range(DIM)])
I128 = np.eye(128, dtype=np.complex128)

cliff_err = max(
    np.max(np.abs(gammas[a] @ gammas[b] + gammas[b] @ gammas[a] - 2.0 * ETA_DIAG[a] * (a == b) * I128))
    for a in range(DIM) for b in range(DIM)
)
assert cliff_err < 1e-14, f"Clifford anticommutator failed: {cliff_err}"

J = I128.copy()
for a in range(7):
    J = J @ gammas[a]
if np.allclose(J @ J, -I128):
    J = 1j * J

Gamma_star = I128.copy()
for a in range(DIM):
    Gamma_star = Gamma_star @ gammas[a]
GSTAR_DIAG = np.diag(Gamma_star).copy()
assert np.max(np.abs(Gamma_star - np.diag(GSTAR_DIAG))) < 1e-15

J_prime = 1j * J @ Gamma_star
assert np.max(np.abs(J_prime.conj().T - J_prime)) < 1e-14
assert np.max(np.abs(J_prime @ J_prime - I128)) < 1e-14
assert np.isclose(np.trace(J_prime), 0.0)


def assert_in_u64(mat_batch, name: str = "tensor"):
    scale = max(1.0, float(np.max(np.abs(mat_batch))))
    err = float(np.max(np.abs(np.swapaxes(mat_batch.conj(), -1, -2) @ J_prime + J_prime @ mat_batch))) / scale
    assert err < 1e-12, f"{name} failed J'-skew-adjointness: rel err = {err}"


g_self_J_err = max(np.max(np.abs(gammas[a].conj().T @ J - J @ gammas[a])) for a in range(DIM))
g_skew_Jp_err = max(np.max(np.abs(gammas[a].conj().T @ J_prime + J_prime @ gammas[a])) for a in range(DIM))
p1.update(1, force=True)

rng = np.random.default_rng(42)
eq327_under_J_err = 0.0
rev_under_J_err = 0.0
eq327_under_Jp_err = 0.0

for k in range(DIM + 1):
    mat = np.zeros((128, 128), dtype=np.complex128)
    for _ in range(5):
        idx = sorted(rng.choice(DIM, size=k, replace=False))
        blade = I128.copy()
        for a in idx:
            blade = blade @ gammas[a]
        mat += rng.normal() * blade
    mat_eq327 = (1j * mat) if (k % 4 in (0, 3)) else mat
    mat_rev = (1j * mat) if (k % 4 in (0, 1)) else mat
    eq327_under_J_err = max(eq327_under_J_err, np.max(np.abs(mat_eq327.conj().T @ J + J @ mat_eq327)))
    rev_under_J_err = max(rev_under_J_err, np.max(np.abs(mat_rev.conj().T @ J + J @ mat_rev)))
    eq327_under_Jp_err = max(eq327_under_Jp_err, np.max(np.abs(mat_eq327.conj().T @ J_prime + J_prime @ mat_eq327)))
    p1.update(k + 2, force=True)

# Cartan decomposition of u(64,64): k = su(64) + su(64) + u(1)_center + u(1)_{J'} (8190 + 2) vs p (8192)
P_pos = 0.5 * (I128 + J_prime)
P_neg = 0.5 * (I128 - J_prime)
M_raw = rng.normal(size=(128, 128)) + 1j * rng.normal(size=(128, 128))
X_sample = J_prime @ (M_raw - M_raw.conj().T)
X_comp = P_pos @ X_sample @ P_pos + P_neg @ X_sample @ P_neg
X_noncomp = P_pos @ X_sample @ P_neg + P_neg @ X_sample @ P_pos
tr_comp_sq = float(np.trace(X_comp @ X_comp).real)
tr_noncomp_sq = float(np.trace(X_noncomp @ X_noncomp).real)

Z_center = 1j * I128
Z_rel_u1 = 1j * J_prime
assert_in_u64(Z_center, "Z_center")
assert_in_u64(Z_rel_u1, "Z_rel_u1")
killing_center = float((256.0 * np.trace(Z_center @ Z_center) - 2.0 * (np.trace(Z_center) ** 2)).real)
killing_rel_u1 = float((256.0 * np.trace(Z_rel_u1 @ Z_rel_u1) - 2.0 * (np.trace(Z_rel_u1) ** 2)).real)
dim_k_semisimple = 2 * (64 * 64 - 1)  # 8190
assert tr_comp_sq < 0.0 and tr_noncomp_sq > 0.0
assert abs(killing_center) < 1e-12 and np.isclose(killing_rel_u1, -32768.0) and dim_k_semisimple == 8190
p1.update(18, force=True)

p1.finish(f"Cl(7,7) err={cliff_err:.1e} | Eq.3.27(J)={eq327_under_J_err:.2f}, Eq.3.27(J')={eq327_under_Jp_err:.1e}")
print(f"    * Reversal J vs Conjugation J': ||g_a^dag J - J g_a|| = {g_self_J_err:.1e}, ||g_a^dag J' + J' g_a|| = {g_skew_Jp_err:.1e}")
print(f"    * Cartan Tr(X^2) in u(64,64):   Tr(X_comp^2) = {tr_comp_sq:+.4e} (<0), Tr(X_noncomp^2) = {tr_noncomp_sq:+.4e} (>0)")
print(f"    * Compact k = su(64)+su(64)+u(1)^2: [k,k]={dim_k_semisimple}, B(iI,iI)={killing_center:.1e}, B(iJ',iJ')={killing_rel_u1:.0f}, coset p=8192")


# ==============================================================================
# VERIFICATION GROUP 2: 2D-BLAS Shiab Operators, 6-Op -> 3-Blade Identity,
#              8 -> 4 Bianchi SVD, and Exact D_7 = so(14,C) Count (200 -> 96)
# ==============================================================================
p2 = LiveProgress("V2", 30, "6->2, 8->4 SVD & D_7 200->96")

gamma_up = gammas * ETA_DIAG[:, None, None]
g_up_star = gamma_up * GSTAR_DIAG[None, None, :]

G_up_row = gamma_up.transpose(1, 0, 2).reshape(128, 14 * 128)
G_up_col = gamma_up.reshape(14 * 128, 128)
G_dn_col = gammas.reshape(14 * 128, 128)
G_dn_row = gammas.transpose(1, 0, 2).reshape(128, 14 * 128)
G_ups_row = g_up_star.transpose(1, 0, 2).reshape(128, 14 * 128)
G_ups_col = g_up_star.reshape(14 * 128, 128)


def _L3_R3_from_L1_R1(L1, R1):
    S_L = -(G_up_row @ L1.reshape(14 * 128, 128))
    S_R = R1.transpose(1, 0, 2).reshape(128, 14 * 128) @ G_up_col
    L3 = (G_dn_col @ S_L).reshape(14, 128, 128) + 2.0 * L1
    R3 = (S_R @ G_dn_row).reshape(128, 14, 128).transpose(1, 0, 2) - 2.0 * R1
    return L3, R3


def theta_both_from_M(M):
    """Evaluates (Theta_Ein, Theta_Bianchi) directly from 2D layout M of shape (1792, 1792)."""
    L1 = (G_up_row @ M).reshape(128, 14, 128).transpose(1, 0, 2)
    R1 = -(M @ G_up_col).reshape(14, 128, 128)
    L3, R3 = _L3_R3_from_L1_R1(L1, R1)
    return 0.5 * (L3 + R3), 0.5j * (L3 - R3)


def theta_both_bare(F):
    return theta_both_from_M(F.transpose(0, 2, 1, 3).reshape(14 * 128, 14 * 128))


def theta_ein_bare(F):
    M = F.transpose(0, 2, 1, 3).reshape(14 * 128, 14 * 128)
    L1 = (G_up_row @ M).reshape(128, 14, 128).transpose(1, 0, 2)
    R1 = -(M @ G_up_col).reshape(14, 128, 128)
    L3, R3 = _L3_R3_from_L1_R1(L1, R1)
    return 0.5 * (L3 + R3)


def eval_6_and_8_ops(F):
    M = F.transpose(0, 2, 1, 3).reshape(14 * 128, 14 * 128)
    L1 = (G_up_row @ M).reshape(128, 14, 128).transpose(1, 0, 2)
    R1 = -(M @ G_up_col).reshape(14, 128, 128)
    O1_c = L1 - R1
    O1_a = 1j * (L1 + R1)

    S_L = -(G_up_row @ L1.reshape(14 * 128, 128))
    S_R = R1.transpose(1, 0, 2).reshape(128, 14 * 128) @ G_up_col
    S_c = S_L - S_R
    S_a = 1j * (S_L + S_R)

    O2_cc = (gammas @ S_c[None]) - (S_c[None] @ gammas)
    O2_ca = (gammas @ S_a[None]) - (S_a[None] @ gammas)
    O2_ac = 1j * ((gammas @ S_c[None]) + (S_c[None] @ gammas))
    O2_aa = 1j * ((gammas @ S_a[None]) + (S_a[None] @ gammas))

    L3 = (G_dn_col @ S_L).reshape(14, 128, 128) + 2.0 * L1
    R3 = (S_R @ G_dn_row).reshape(128, 14, 128).transpose(1, 0, 2) - 2.0 * R1
    T3_ein = 0.5 * (L3 + R3)
    T3_bia = 0.5j * (L3 - R3)

    L13 = (G_ups_row @ M).reshape(128, 14, 128).transpose(1, 0, 2)
    R13 = -(M @ G_ups_col).reshape(14, 128, 128)
    O13_c = L13 - R13
    O13_a = 1j * (L13 + R13)

    Sh_L = GSTAR_DIAG[:, None] * S_L
    Sh_R = S_R * GSTAR_DIAG[None, :]
    L11 = (G_dn_col @ Sh_L).reshape(14, 128, 128) + 2.0 * L13
    R11 = -(Sh_R @ G_dn_row).reshape(128, 14, 128).transpose(1, 0, 2) - 2.0 * R13
    T11_ein = 0.5 * (L11 + R11)
    T11_bia = 0.5j * (L11 - R11)

    ops6 = [O1_c, O1_a, O2_cc, O2_ca, O2_ac, O2_aa]
    ops8 = [O1_c, O1_a, O13_c, O13_a, T3_ein, T3_bia, T11_ein, T11_bia]
    return ops6, ops8


def trace_shiab(F):
    tr_F = np.trace(F, axis1=2, axis2=3)
    return theta_ein_bare(tr_F[:, :, None, None] * I128[None, None])


def random_u64(shape=()):
    M = rng.normal(size=shape + (128, 128)) + 1j * rng.normal(size=shape + (128, 128))
    return J_prime @ (M - np.swapaxes(M.conj(), -1, -2))


F_rand2 = random_u64((14, 14))
F_rand2 = 0.5 * (F_rand2 - np.swapaxes(F_rand2, 0, 1))
ops6_test, ops8_test = eval_6_and_8_ops(F_rand2)
tr_op_test = trace_shiab(F_rand2)

O1_c, O1_a, O2_cc, O2_ca, O2_ac, O2_aa = ops6_test
T3_ein, T3_bia = ops8_test[4], ops8_test[5]
prop2_ein_err = float(np.linalg.norm((O1_c + 0.25 * (O2_cc - O2_aa)) - T3_ein) / np.linalg.norm(T3_ein))
prop2_bia_err = float(np.linalg.norm((O1_a + 0.25 * (O2_ca + O2_ac)) - T3_bia) / np.linalg.norm(T3_bia))
assert prop2_ein_err < 1e-13 and prop2_bia_err < 1e-13

for idx, op in enumerate(ops8_test + [tr_op_test]):
    assert_in_u64(op, f"equivariant_op_{idx}")
p2.update(1, force=True)

d0F = np.zeros((14, 14, 128, 128), dtype=np.complex128)
names6 = ["O1_c", "O1_a", "O2_cc", "O2_ca", "O2_ac", "O2_aa"]
four_jet_results = {}
for label, M_jet in [
    ("i*I", 1j * I128),
    ("gamma^1", gamma_up[1]),
    ("gamma^0", gamma_up[0]),
    ("gamma^{01}", gamma_up[0] @ gamma_up[1]),
]:
    assert_in_u64(M_jet, label)
    d0F.fill(0.0)
    d0F[0, 1] = M_jet
    d0F[1, 0] = -M_jet
    o6, _ = eval_6_and_8_ops(d0F)
    four_jet_results[label] = [(n, round(float(np.linalg.norm(op[0])), 2)) for n, op in zip(names6, o6) if np.linalg.norm(op[0]) > 1e-10]

names_bia4 = ["T3_ein", "T3_bia", "T11_ein", "T11_bia"]
indep3_results = {}
for label, X_ind in [("i*I", 1j * I128), ("gamma^0", gamma_up[0]), ("gamma^3", gamma_up[3])]:
    F_ind = np.zeros((14, 14, 128, 128), dtype=np.complex128)
    F_ind[1, 2] = X_ind
    F_ind[2, 1] = -X_ind
    _, o8 = eval_6_and_8_ops(F_ind)
    indep3_results[label] = [n for n, op in zip(names_bia4, o8[4:]) if np.linalg.norm(op[0]) > 1e-10]
assert indep3_results["i*I"] == ["T3_ein", "T11_ein"]
assert indep3_results["gamma^0"] == ["T3_ein", "T11_bia"]
assert indep3_results["gamma^3"] == ["T3_bia", "T11_ein"]

# Low-memory factored closed 2-form jet SVD (28 MiB vs 686 MiB)
S_m2 = rng.normal(size=(8, 14, 14))
S_m2 = 0.5 * (S_m2 + np.swapaxes(S_m2, 1, 2))
W_m2 = random_u64((8, 14))
divs6 = [np.zeros((128, 128), dtype=np.complex128) for _ in range(6)]
divs8 = [np.zeros((128, 128), dtype=np.complex128) for _ in range(8)]
for a in range(DIM):
    Q_a = np.einsum('rb,rcjk->bcjk', S_m2[:, a, :], W_m2)
    F1_a = Q_a - np.swapaxes(Q_a, 0, 1)
    o6, o8 = eval_6_and_8_ops(F1_a)
    for k in range(6):
        divs6[k] += ETA_DIAG[a] * o6[k][a]
    for k in range(8):
        divs8[k] += ETA_DIAG[a] * o8[k][a]
    p2.update(a + 2, force=True)
del S_m2, W_m2, Q_a, F1_a

A6_mat = np.column_stack([np.concatenate([divs6[k].real.ravel(), divs6[k].imag.ravel()]) for k in range(6)])
_, s6, _ = np.linalg.svd(A6_mat, full_matrices=False)
null_6 = int(np.sum(s6 < 1e-7))

A8_mat = np.column_stack([np.concatenate([divs8[k].real.ravel(), divs8[k].imag.ravel()]) for k in range(8)])
_, s8, _ = np.linalg.svd(A8_mat, full_matrices=False)
null_8 = int(np.sum(s8 < 1e-7))

B5_mat = np.column_stack([np.concatenate([op.real.ravel(), op.imag.ravel()]) for op in (ops8_test[4:] + [tr_op_test])])
_, s5, _ = np.linalg.svd(B5_mat, full_matrices=False)
rank_5 = int(np.sum(s5 > 1e-7))
assert null_6 == 2 and null_8 == 4 and rank_5 == 5
del A6_mat, A8_mat, B5_mat, divs6, divs8, ops6_test, ops8_test, tr_op_test

weights_V = [(i, s) for i in range(7) for s in (1, -1)]


def wedge_weights(k: int):
    out = []
    for comb in combinations(weights_V, k):
        w = [0] * 7
        for i, s in comb:
            w[i] += s
        out.append(tuple(w))
    return tuple(out)


rho_D7 = (6, 5, 4, 3, 2, 1, 0)


def reflect_D7(v):
    if len({abs(x) for x in v}) < 7:
        return None
    arr = list(v)
    sgn = 1
    for i in range(7):
        for j in range(6 - i):
            if abs(arr[j]) < abs(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sgn = -sgn
    flips = 0
    for i in range(6):
        if arr[i] < 0:
            arr[i] = -arr[i]
            flips += 1
    if flips % 2 == 1:
        arr[6] = -arr[6]
    return tuple(arr), sgn


W_BY_DEG = {1: wedge_weights(1), 2: wedge_weights(2), 3: wedge_weights(3)}


@lru_cache(maxsize=None)
def klimyk_D7(deg: int, lam: tuple):
    mults = {}
    for nu in W_BY_DEG[deg]:
        res = reflect_D7([lam[i] + rho_D7[i] + nu[i] for i in range(7)])
        if res is not None:
            dom, sgn = res
            mu = tuple(dom[i] - rho_D7[i] for i in range(7))
            mults[mu] = mults.get(mu, 0) + sgn
    return {mu: m for mu, m in mults.items() if m != 0}


def irrep_Lambda_k(k: int):
    if k == 0 or k == 14:
        return [(0, 0, 0, 0, 0, 0, 0)]
    if k > 7:
        k = 14 - k
    if k < 7:
        return [tuple([1] * k + [0] * (7 - k))]
    return [(1, 1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1, -1)]


decomp_Cl = {}
decomp_L1_Cl = {}
for k in range(DIM + 1):
    for lam in irrep_Lambda_k(k):
        decomp_Cl[lam] = decomp_Cl.get(lam, 0) + 1
        for mu, m in klimyk_D7(1, lam).items():
            decomp_L1_Cl[mu] = decomp_L1_Cl.get(mu, 0) + m

tot_unres = 0
tot_bianchi = 0
tot_vec_channel = 0
for k in range(DIM + 1):
    for lam in irrep_Lambda_k(k):
        d1 = klimyk_D7(1, lam)
        d2 = klimyk_D7(2, lam)
        d3 = klimyk_D7(3, lam)
        tot_unres += sum(m * decomp_L1_Cl.get(mu, 0) for mu, m in d2.items())
        tot_bianchi += sum(m * decomp_Cl.get(mu, 0) for mu, m in d3.items())
        tot_vec_channel += sum(m * decomp_Cl.get(mu, 0) for mu, m in d1.items())
    p2.update(16 + k, force=True)

tot_hook_channel = tot_unres - tot_bianchi - tot_vec_channel
assert tot_unres == 200 and tot_bianchi == 96 and tot_vec_channel == 56 and tot_hook_channel == 48

p2.finish(f"Classifications verified: 6->{null_6}, 8->{null_8} (SVD), unrestricted D_7: {tot_unres}->{tot_bianchi}")
print(f"    * Prop 2(1) 3-blade identity:  ||O1_c+1/4(O2_cc-O2_aa) - T3_ein||/||T3|| = {prop2_ein_err:.1e}, T3_bia = {prop2_bia_err:.1e}")
print(f"    * 4-jet proof table (a=0):     iI->{four_jet_results['i*I']}, g^0->{four_jet_results['gamma^0']}")
print(f"    * 8D Bianchi SVD spectrum:     {[round(float(x), 1) for x in s8[:4]]} + 4 null modes (~{s8[4]:.1e})")
print(f"    * D_7 = so(14,C) channels:     Lambda^3 V = {tot_bianchi} (Bianchi), V = {tot_vec_channel}, Hook H_(2,1) = {tot_hook_channel} (Total = {tot_unres})")


# ==============================================================================
# VERIFICATION GROUP 3: Non-Degenerate Curved Riemann Normal Coordinates, Real Einstein
#              Reconstruction (Prop. 1), and Finite U(64,64) Gauge Covariance
# ==============================================================================
p3 = LiveProgress("V3", 4, "Curved 14D Einstein & U(64,64)")

H = rng.normal(size=(14, 14, 14, 14))
H = 0.25 * (H + np.swapaxes(H, 0, 1) + np.swapaxes(H, 2, 3) + np.swapaxes(np.swapaxes(H, 0, 1), 2, 3))

K = rng.normal(size=(14, 14, 14, 14, 14))
K = 0.5 * (K + np.swapaxes(K, 0, 1))
K = (K + np.einsum('abcde->abdec', K) + np.einsum('abcde->abecd', K)
     + np.swapaxes(K, 2, 3) + np.swapaxes(K, 2, 4) + np.swapaxes(K, 3, 4)) / 6.0

R0 = 0.5 * (np.einsum('adbc->abcd', H) + np.einsum('bcad->abcd', H)
            - np.einsum('bdac->abcd', H) - np.einsum('acbd->abcd', H))
dR = 0.5 * (np.einsum('adbce->eabcd', K) + np.einsum('bcade->eabcd', K)
            - np.einsum('bdace->eabcd', K) - np.einsum('acbde->eabcd', K))

norm_R0 = float(np.linalg.norm(R0))
norm_dR = float(np.linalg.norm(dR))
assert norm_R0 > 50.0 and norm_dR > 100.0
p3.update(1, force=True)

gamma_2up = gamma_up[:, None, :, :] @ gamma_up[None, :, :, :]
for b in range(DIM):
    gamma_2up[b, b] = 0.0

F_riem = 0.25 * np.tensordot(R0, gamma_2up, axes=([2, 3], [0, 1]))
p3.update(2, force=True)

_, ops8_riem = eval_6_and_8_ops(F_riem)
T3_ein_riem, T3_bia_riem, T11_ein_riem, T11_bia_riem = ops8_riem[4:]

Ric = np.einsum('cd,cadb->ab', ETA_MAT, R0)
R_scal = np.einsum('ab,ab->', ETA_MAT, Ric)
G_exact = np.tensordot(Ric - 0.5 * R_scal * ETA_MAT, gamma_up, axes=([1], [0]))
norm_G = float(np.linalg.norm(G_exact))

ein_rel_err = float(np.linalg.norm(T3_ein_riem - G_exact) / norm_G)
ein_dual_err = float(np.linalg.norm(T11_ein_riem - (G_exact * GSTAR_DIAG[None, None, :])) / norm_G)
bia_riem_rel = float((np.linalg.norm(T3_bia_riem) + np.linalg.norm(T11_bia_riem)) / norm_G)

div_G = np.zeros((128, 128), dtype=np.complex128)
for a in range(DIM):
    dF_riem_a = 0.25 * np.tensordot(dR[a], gamma_2up, axes=([2, 3], [0, 1]))
    div_G += ETA_DIAG[a] * theta_ein_bare(dF_riem_a)[a]
div_G_norm = float(np.linalg.norm(div_G))
div_G_rel = div_G_norm / norm_G
assert ein_rel_err < 1e-13 and ein_dual_err < 1e-13 and bia_riem_rel < 1e-13 and div_G_rel < 1e-12
del H, K, R0, dR, F_riem, dF_riem_a, gamma_2up, ops8_riem, G_exact
p3.update(3, force=True)


def cayley(X):
    return np.linalg.solve(I128 + X, I128 - X)


eps_g = cayley(0.01 * random_u64())
eps_g_inv = np.linalg.inv(eps_g)
h_g = cayley(0.01 * random_u64())
h_g_inv = np.linalg.inv(h_g)
unitarity_err = float(np.max(np.abs(h_g.conj().T @ J_prime @ h_g - J_prime)))


def eval_4_bianchi_dressed(F, eps_mat, einv_mat):
    F_bar = eps_mat[None, None] @ F @ einv_mat[None, None]
    _, o8 = eval_6_and_8_ops(F_bar)
    return [einv_mat[None] @ op @ eps_mat[None] for op in o8[4:]]


F_cov = random_u64((14, 14))
F_cov = 0.5 * (F_cov - np.swapaxes(F_cov, 0, 1))
F_cov_rot = h_g_inv[None, None] @ F_cov @ h_g[None, None]

bare_0 = theta_ein_bare(F_cov)
bare_rot = theta_ein_bare(F_cov_rot)
bare_cov_err = float(np.linalg.norm(bare_rot - (h_g_inv[None] @ bare_0 @ h_g[None])) / np.linalg.norm(bare_0))

dressed_0 = eval_4_bianchi_dressed(F_cov, eps_g, eps_g_inv)
dressed_rot = eval_4_bianchi_dressed(F_cov_rot, eps_g @ h_g, h_g_inv @ eps_g_inv)
dressed_cov_errs = [
    float(np.linalg.norm(dr - (h_g_inv[None] @ d0 @ h_g[None])) / np.linalg.norm(d0))
    for d0, dr in zip(dressed_0, dressed_rot)
]
assert bare_cov_err > 0.1 and max(dressed_cov_errs) < 1e-12
del F_cov, F_cov_rot, bare_0, bare_rot, dressed_0, dressed_rot
gc.collect()
p3.update(4, force=True)

p3.finish(f"14D Einstein err={ein_rel_err:.2e} (||R||={norm_R0:.1f}) | Bianchi div={div_G_norm:.2e} | Cov={max(dressed_cov_errs):.2e}")
print(f"    * Prop 1 on F_Riem:            ||T3_ein - G_ab g^b||/||G|| = {ein_rel_err:.2e}, dual = {ein_dual_err:.2e}, ||T_bia||/||G|| = {bia_riem_rel:.2e}")
print(f"    * U(64,64) gauge covariance:   ||h^dag J' h - J'|| = {unitarity_err:.2e} | Bare err = {bare_cov_err:.2f} vs Dressed max err = {max(dressed_cov_errs):.2e}")


# ==============================================================================
# VERIFICATION GROUP 4: Low-Memory Non-Abelian Bianchi Identity (D_A F_A = 0),
#              Non-Circular Direct 3-Blade D_A-Divergence, and Prop. 3
# ==============================================================================
p4 = LiveProgress("V4", 16, "Non-Abelian D_{B_w} & Torsion")

eps0 = cayley(0.01 * random_u64())
eps0_inv = np.linalg.inv(eps0)
X_a = random_u64((14,))
T0_jet = random_u64((14,))
A1 = random_u64((14, 14))
A0 = X_a + T0_jet

comm_A0 = (A0[:, None] @ A0[None, :]) - (A0[None, :] @ A0[:, None])
F_A0 = A1 - np.swapaxes(A1, 0, 1) + comm_A0

S_jet = rng.normal(size=(4, 14, 14))
S_jet = 0.5 * (S_jet + np.swapaxes(S_jet, 1, 2))
W_jet = random_u64((4, 14))

TRIPLES_364 = list(combinations(range(DIM), 3))
bianchi_triples = np.zeros((len(TRIPLES_364), 128, 128), dtype=np.complex128)
triples_by_c = [[] for _ in range(DIM)]
for t_idx, (c_t, a_t, b_t) in enumerate(TRIPLES_364):
    triples_by_c[c_t].append((t_idx, a_t, b_t))
    triples_by_c[a_t].append((t_idx, b_t, c_t))
    triples_by_c[b_t].append((t_idx, c_t, a_t))

div_DB_T1 = np.zeros((128, 128), dtype=np.complex128)
div_DB_T2 = np.zeros((128, 128), dtype=np.complex128)
rhs_T1 = np.zeros((128, 128), dtype=np.complex128)
rhs_T2 = np.zeros((128, 128), dtype=np.complex128)
max_DA_FA_scale = 0.0
p4.update(2, force=True)

for c in range(DIM):
    Q_c = np.einsum('ra,rbjk->abjk', S_jet[:, c, :], W_jet)
    c_A1_A0 = (A1[c, :, None] @ A0[None, :]) - (A0[None, :] @ A1[c, :, None])
    dF_A_c = (Q_c - np.swapaxes(Q_c, 0, 1)) + (c_A1_A0 - np.swapaxes(c_A1_A0, 0, 1))

    DA_FA_c = dF_A_c + (A0[c, None, None] @ F_A0 - F_A0 @ A0[c, None, None])
    max_DA_FA_scale = max(max_DA_FA_scale, float(np.max(np.abs(DA_FA_c))))
    for t_idx, idx1, idx2 in triples_by_c[c]:
        bianchi_triples[t_idx] += DA_FA_c[idx1, idx2]

    DB_FA_c = dF_A_c + (X_a[c, None, None] @ F_A0 - F_A0 @ X_a[c, None, None])

    F_bc = F_A0[:, c]
    F_ca = F_A0[c, :]
    comm_TF_c = ((T0_jet[c, None, None] @ F_A0 - F_A0 @ T0_jet[c, None, None])
                 + (T0_jet[:, None] @ F_bc[None, :] - F_bc[None, :] @ T0_jet[:, None])
                 + (T0_jet[None, :] @ F_ca[:, None] - F_ca[:, None] @ T0_jet[None, :]))

    db_bar = eps0[None, None] @ DB_FA_c @ eps0_inv[None, None]
    tf_bar = eps0[None, None] @ comm_TF_c @ eps0_inv[None, None]
    t1_db, t2_db = theta_both_bare(db_bar)
    t1_tf, t2_tf = theta_both_bare(tf_bar)
    div_DB_T1 += ETA_DIAG[c] * (eps0_inv @ t1_db[c] @ eps0)
    div_DB_T2 += ETA_DIAG[c] * (eps0_inv @ t2_db[c] @ eps0)
    rhs_T1 += ETA_DIAG[c] * (eps0_inv @ t1_tf[c] @ eps0)
    rhs_T2 += ETA_DIAG[c] * (eps0_inv @ t2_tf[c] @ eps0)
    p4.update(c + 3, force=True)

bianchi_nonab_err = float(np.max(np.abs(bianchi_triples)))
bianchi_nonab_rel = bianchi_nonab_err / max_DA_FA_scale
err_prop3_ein = float(np.linalg.norm(div_DB_T1 + (1.0 / 3.0) * rhs_T1) / np.linalg.norm(div_DB_T1))
err_prop3_bia = float(np.linalg.norm(div_DB_T2 + (1.0 / 3.0) * rhs_T2) / np.linalg.norm(div_DB_T2))

# Non-circular, direct 3-blade commutator verification of D_A^a Theta_{Ein,eps}(F_A)_a = 1/2 {[T^a, \tilde{\gamma}_a^{bc}], F_{A,bc}}
F_hat_m4 = eps0[None, None] @ F_A0 @ eps0_inv[None, None]
T_hat_m4 = eps0[None] @ T0_jet @ eps0_inv[None]
Theta_FA0_ein, _ = theta_both_bare(F_hat_m4)
Theta_FA0_ein = eps0_inv[None] @ Theta_FA0_ein @ eps0[None]
div_DA_T1 = div_DB_T1 + sum(ETA_DIAG[a] * (T0_jet[a] @ Theta_FA0_ein[a] - Theta_FA0_ein[a] @ T0_jet[a]) for a in range(DIM))

explicit_rhs_hat = np.zeros((128, 128), dtype=np.complex128)
for a in range(DIM):
    for b in range(DIM):
        for c in range(b + 1, DIM):
            if a == b or a == c:
                continue
            G_abc = gammas[a] @ gamma_up[b] @ gamma_up[c]  # \gamma_a^{bc} (a lowered, b<c raised)
            C_abc = T_hat_m4[a] @ G_abc - G_abc @ T_hat_m4[a]
            explicit_rhs_hat += ETA_DIAG[a] * (C_abc @ F_hat_m4[b, c] + F_hat_m4[b, c] @ C_abc)
explicit_rhs_DA = eps0_inv @ explicit_rhs_hat @ eps0
err_DA_formula = float(np.linalg.norm(div_DA_T1 - explicit_rhs_DA) / np.linalg.norm(div_DA_T1))

assert bianchi_nonab_err < 1e-9 and bianchi_nonab_rel < 1e-13 and err_prop3_ein < 1e-12 and err_prop3_bia < 1e-12 and err_DA_formula < 1e-12
del bianchi_triples, Q_c, c_A1_A0, dF_A_c, DA_FA_c, DB_FA_c, comm_TF_c, db_bar, tf_bar, F_A0, F_hat_m4, A1
gc.collect()

p4.finish(f"D_A F_A=0 ({bianchi_nonab_err:.2e}, rel={bianchi_nonab_rel:.2e}) | Prop 3 err: Ein={err_prop3_ein:.2e}, Bia={err_prop3_bia:.2e}")
print(f"    * Direct 3-blade D_A-div check: ||D_A^a Theta_Ein(F_A)_a|| = {np.linalg.norm(div_DA_T1):.4e} (explicit 1/2{{[T^a,g_a^bc],F_bc}} rel err = {err_DA_formula:.2e})")


# ==============================================================================
# VERIFICATION GROUP 5: Typed Exterior Algebra on (R^{7,7}, eta), Hodge Star Involution,
#              Eq. (9.3) Bracket Audit, and Sparse Blade Variational Check
# ==============================================================================
p5 = LiveProgress("V5", 10, "Typed Forms & Eq.(9.3) Audit")


def perm_sign(seq):
    arr = list(seq)
    swaps = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return -1 if (swaps % 2) else 1


HODGE_MAP = {}
for p in range(DIM + 1):
    for I in combinations(ALL_INDICES, p):
        Ic = tuple(x for x in ALL_INDICES if x not in I)
        sgn = perm_sign(I + Ic)
        metric_prod = float(np.prod([ETA_REAL[idx] for idx in I])) if p > 0 else 1.0
        HODGE_MAP[I] = (Ic, sgn * metric_prod)
p5.update(2, force=True)


class DifferentialForm:
    """Typed p-form on R^{7,7} valued in Mat(128, C)."""
    def __init__(self, degree: int, comps: dict):
        assert 0 <= degree <= DIM
        self.degree = degree
        self.comps = {I: np.asarray(M, dtype=np.complex128) for I, M in comps.items() if np.any(M != 0)}

    def __add__(self, other):
        assert self.degree == other.degree
        out = {I: M.copy() for I, M in self.comps.items()}
        for I, M in other.comps.items():
            out[I] = out[I] + M if I in out else M.copy()
        return DifferentialForm(self.degree, out)

    def __sub__(self, other):
        return self + (-1.0 * other)

    def __rmul__(self, scalar):
        if scalar == 0:
            return DifferentialForm(self.degree, {})
        return DifferentialForm(self.degree, {I: scalar * M for I, M in self.comps.items()})

    def norm(self):
        return float(np.sqrt(sum(np.sum(np.abs(M) ** 2) for M in self.comps.values()))) if self.comps else 0.0

    def hodge_star(self):
        return DifferentialForm(DIM - self.degree, {HODGE_MAP[I][0]: HODGE_MAP[I][1] * M for I, M in self.comps.items()})


def wedge(alpha: DifferentialForm, beta: DifferentialForm) -> DifferentialForm:
    new_deg = alpha.degree + beta.degree
    if new_deg > DIM:
        return DifferentialForm(DIM, {})
    out = {}
    for I, A in alpha.comps.items():
        setI = set(I)
        for J_idx, B in beta.comps.items():
            if setI.isdisjoint(J_idx):
                comb = I + J_idx
                K_idx = tuple(sorted(comb))
                term = perm_sign(comb) * (A @ B)
                out[K_idx] = out[K_idx] + term if K_idx in out else term
    return DifferentialForm(new_deg, out)


def graded_bracket_wedge(alpha: DifferentialForm, beta: DifferentialForm, mode: str) -> DifferentialForm:
    new_deg = alpha.degree + beta.degree
    assert new_deg <= DIM
    out = {}
    for I, A in alpha.comps.items():
        setI = set(I)
        for J_idx, B in beta.comps.items():
            if setI.isdisjoint(J_idx):
                comb = I + J_idx
                K_idx = tuple(sorted(comb))
                mat = (A @ B - B @ A) if mode == 'comm' else 1j * (A @ B + B @ A)
                term = perm_sign(comb) * mat
                out[K_idx] = out[K_idx] + term if K_idx in out else term
    return DifferentialForm(new_deg, out)


def trace_pairing(alpha: DifferentialForm, beta: DifferentialForm) -> complex:
    assert alpha.degree == beta.degree
    top = wedge(alpha, beta.hodge_star())
    if ALL_INDICES not in top.comps:
        return 0.0 + 0.0j
    return complex(np.trace(top.comps[ALL_INDICES]))


hodge_inv_err = 0.0
for p in range(DIM + 1):
    sample_I = tuple(range(p))
    f_p = DifferentialForm(p, {sample_I: I128})
    expected_sign = -1.0 if (p % 2 == 0) else 1.0
    hodge_inv_err = max(hodge_inv_err, (f_p.hodge_star().hodge_star() - expected_sign * f_p).norm())
assert hodge_inv_err < 1e-14
p5.update(4, force=True)

Phi1 = DifferentialForm(1, {(a,): gammas[a] for a in range(DIM)})
Phi2 = DifferentialForm(2, {
    (a, b): 0.5 * (gammas[a] @ gammas[b] - gammas[b] @ gammas[a])
    for a in range(DIM) for b in range(a + 1, DIM)
})


def eq93_single_pair(xi: DifferentialForm, m1: str, m2: str, w: float = 0.5) -> DifferentialForm:
    star_xi = xi.hodge_star()
    t1 = graded_bracket_wedge(Phi1, star_xi, m1)
    inner = graded_bracket_wedge(Phi2, star_xi, m2).hodge_star()
    t2 = graded_bracket_wedge(Phi1, inner, m1).hodge_star()
    return t1 - w * t2


def eq93_corrected_typed(xi: DifferentialForm) -> DifferentialForm:
    """Exact typed realization: *Theta_Ein(xi) = -C1 - 1/2 (C2c - C2a)."""
    star_xi = xi.hodge_star()
    C1 = graded_bracket_wedge(Phi1, star_xi, 'comm')
    C2c = graded_bracket_wedge(Phi1, graded_bracket_wedge(Phi2, star_xi, 'comm').hodge_star(), 'comm').hodge_star()
    C2a = graded_bracket_wedge(Phi1, graded_bracket_wedge(Phi2, star_xi, 'anticomm').hodge_star(), 'anticomm').hodge_star()
    return (-1.0) * C1 - 0.5 * (C2c - C2a)


xi_riem_const = DifferentialForm(2, {
    (a, b): 0.5 * (gammas[a] @ gammas[b])
    for a in range(DIM) for b in range(a + 1, DIM)
})
F_riem_const_arr = np.zeros((14, 14, 128, 128), dtype=np.complex128)
for (a, b), M in xi_riem_const.comps.items():
    F_riem_const_arr[a, b] = M
    F_riem_const_arr[b, a] = -M
target_13_riem = DifferentialForm(1, {(a,): theta_ein_bare(F_riem_const_arr)[a] for a in range(DIM)}).hodge_star()

out_cc_riem = eq93_single_pair(xi_riem_const, 'comm', 'comm', 0.5)
err_cc_riem = min((out_cc_riem - target_13_riem).norm(), (out_cc_riem + target_13_riem).norm()) / target_13_riem.norm()
out_aa_riem = eq93_single_pair(xi_riem_const, 'anticomm', 'anticomm', 0.5)
err_aa_riem = min((out_aa_riem - target_13_riem).norm(), (out_aa_riem + target_13_riem).norm()) / target_13_riem.norm()
p5.update(6, force=True)

xi_gen_typed = DifferentialForm(2, {(a, b): F_rand2[a, b] for a in range(DIM) for b in range(a + 1, DIM)})
target_13_gen = DifferentialForm(1, {(a,): theta_ein_bare(F_rand2)[a] for a in range(DIM)}).hodge_star()
corr_13_gen = eq93_corrected_typed(xi_gen_typed)
err_corr_typed = (corr_13_gen - target_13_gen).norm() / target_13_gen.norm()
assert abs(err_cc_riem - 5.0 / 6.0) < 1e-12 and abs(err_aa_riem - 1.0 / 6.0) < 1e-12 and err_corr_typed < 1e-14
del F_rand2, F_riem_const_arr
p5.update(8, force=True)


def theta_both_dBT_fast(row0, row7):
    """Exact O(14) evaluation of (Theta_Ein(d_B T), Theta_Bianchi(d_B T)) on active rows 0, 7."""
    U0 = row0.copy()
    U7 = row7.copy()
    U0[0] = 0.0
    U7[7] = 0.0

    L1 = gamma_up[0, None] @ U0 + gamma_up[7, None] @ U7
    L1[0] -= G_up_row @ U0.reshape(14 * 128, 128)
    L1[7] -= G_up_row @ U7.reshape(14 * 128, 128)

    R1 = U0 @ gamma_up[0, None] + U7 @ gamma_up[7, None]
    R1[0] -= U0.transpose(1, 0, 2).reshape(128, 14 * 128) @ G_up_col
    R1[7] -= U7.transpose(1, 0, 2).reshape(128, 14 * 128) @ G_up_col

    L3, R3 = _L3_R3_from_L1_R1(L1, R1)
    return 0.5 * (L3 + R3), 0.5j * (L3 - R3)


def theta_both_TT_fast(T_hat):
    """Computes (Theta_Ein(T^T), Theta_Bianchi(T^T)) via a single 2D BLAS outer product."""
    T_col = T_hat.reshape(14 * 128, 128)
    T_row = T_hat.transpose(1, 0, 2).reshape(128, 14 * 128)
    W_4d = (T_col @ T_row).reshape(14, 128, 14, 128)
    M_TT = (W_4d - W_4d.transpose(2, 1, 0, 3)).reshape(14 * 128, 14 * 128)
    return theta_both_from_M(M_TT)


def noncentral_delta_E_bare(T_site, ein_tt=None):
    """2D-BLAS evaluation of Delta E_a^{unit} = -sum_{b,c} {T_b, [T_c, gamma_a^{bc}]}."""
    if ein_tt is None:
        ein_tt, _ = theta_both_TT_fast(T_site)
    P_L = T_site.transpose(1, 0, 2).reshape(128, 14 * 128) @ G_up_col
    P_R = G_up_row @ T_site.reshape(14 * 128, 128)
    PgP = ((P_L @ G_dn_row).reshape(128 * 14, 128) @ P_R).reshape(128, 14, 128).transpose(1, 0, 2)
    diag_term = np.zeros_like(T_site)
    for b in range(DIM):
        Tb_g = (ETA_DIAG[b] * T_site[b]) @ G_dn_row
        diag_term += (Tb_g.reshape(128 * 14, 128) @ T_site[b]).reshape(128, 14, 128).transpose(1, 0, 2)
    mid_term = (T_site @ P_R[None]) + (P_L[None] @ T_site) - PgP - diag_term
    return 2.0 * mid_term - ein_tt


T_ce = np.zeros((14, 128, 128), dtype=np.complex128)
T_ce[1] = gamma_up[3]
T_ce[2] = gamma_up[4]
DE_ce0 = (1.0 / 3.0) * noncentral_delta_E_bare(T_ce)[0]
g01234 = gamma_up[0] @ gamma_up[1] @ gamma_up[2] @ gamma_up[3] @ gamma_up[4]
ce_err = float(np.linalg.norm(DE_ce0 - (-8.0 / 3.0) * g01234) / np.linalg.norm(g01234))
assert ce_err < 1e-13

T_sparse = DifferentialForm(1, {
    (1,): gammas[3],
    (2,): gammas[4],
    (5,): gammas[0] @ gammas[6],
    (8,): gammas[9],
})
FB_sparse = DifferentialForm(2, {
    (0, 1): gammas[2],
    (3, 4): 1j * I128,
})
alpha_sparse = DifferentialForm(1, {
    (0,): gammas[0] @ gammas[1] @ gammas[2] @ gammas[3] @ gammas[4],
    (1,): gammas[3] + gammas[9],
    (7,): gammas[1] @ gammas[2] @ gammas[5] @ gammas[6] @ gammas[7],
})
for f_sp in (T_sparse, FB_sparse, alpha_sparse):
    for M_sp in f_sp.comps.values():
        assert_in_u64(M_sp, "sparse_field")


def sparse_alg_action(T_f: DifferentialForm, kappa1: float = 1.5) -> float:
    K_f = FB_sparse + (1.0 / 3.0) * wedge(T_f, T_f)
    F_arr = np.zeros((14, 14, 128, 128), dtype=np.complex128)
    for (a, b), M in K_f.comps.items():
        F_arr[a, b] = M
        F_arr[b, a] = -M
    th_arr = theta_ein_bare(F_arr)
    th_form = DifferentialForm(1, {(a,): th_arr[a] for a in range(DIM)})
    return float((trace_pairing(T_f, th_form) + kappa1 * trace_pairing(T_f, T_f)).real)


eps_sp = 1e-6
fd_sparse = (sparse_alg_action(T_sparse + eps_sp * alpha_sparse)
             - sparse_alg_action(T_sparse - eps_sp * alpha_sparse)) / (2.0 * eps_sp)

T_sp_arr = np.zeros((14, 128, 128), dtype=np.complex128)
for (a,), M in T_sparse.comps.items():
    T_sp_arr[a] = M
F_sp_alg = FB_sparse + wedge(T_sparse, T_sparse)
F_sp_arr = np.zeros((14, 14, 128, 128), dtype=np.complex128)
for (a, b), M in F_sp_alg.comps.items():
    F_sp_arr[a, b] = M
    F_sp_arr[b, a] = -M

Th_sp_form = DifferentialForm(1, {(a,): theta_ein_bare(F_sp_arr)[a] for a in range(DIM)})
DE_sp_arr = (1.0 / 3.0) * noncentral_delta_E_bare(T_sp_arr)
DE_sp_form = DifferentialForm(1, {(a,): DE_sp_arr[a] for a in range(DIM)})

ana_sp_with = float(trace_pairing(alpha_sparse, Th_sp_form + DE_sp_form + 3.0 * T_sparse).real)
ana_sp_naive = float(trace_pairing(alpha_sparse, Th_sp_form + 3.0 * T_sparse).real)
sp_rel_err_with = abs(fd_sparse - ana_sp_with) / abs(fd_sparse)
sp_rel_err_naive = abs(fd_sparse - ana_sp_naive) / abs(fd_sparse)
assert sp_rel_err_with < 1e-7 and sp_rel_err_naive > 0.2
del F_sp_arr, T_sp_arr
gc.collect()
p5.update(10, force=True)

p5.finish(f"Typed **=(-1)^(p+1) err={hodge_inv_err:.1e} | Corrected Eq.9.3 err={err_corr_typed:.2e} | Sparse FD={sp_rel_err_with:.2e}")
print(f"    * Literal Eq.(9.3) on F_Riem:  (comm,comm) rel err = {err_cc_riem:.4f} (5/6), (anticomm,anticomm) = {err_aa_riem:.4f} (1/6)")
print(f"    * Noncentral blade witness:    ||Delta E_0 - (-8/3 g^01234)||/||g|| = {ce_err:.1e} (||Delta E_0|| = {np.linalg.norm(DE_ce0):.2f})")
print(f"    * Sparse blade FD variation:   FD = {fd_sparse:+.6f}, With Delta_E = {ana_sp_with:+.6f} ({sp_rel_err_with:.2e}), Without = {ana_sp_naive:+.6f} ({sp_rel_err_naive:.1%})")


# ==============================================================================
# VERIFICATION GROUP 6: Low-Memory Full 14D Periodic Action (Eq. 9.4, F_B = 0),
#              1D & 2D Continuum Grid Convergence, -256 Kinetic Witness,
#              Case A & B Variations, and True Fixed-A Coupled Noether Test
# ==============================================================================
p6 = LiveProgress("V6", 15, "Full 14D Action & Coupled Noether")

_, eigvecs = np.linalg.eigh(J_prime)
V_neg, V_pos = eigvecs[:, :64], eigvecs[:, 64:]


def random_nilpotent_u64():
    A = rng.normal(size=(64, 64)) + 1j * rng.normal(size=(64, 64))
    A_skew = 0.05 * (A - A.conj().T)
    return (V_pos + V_neg) @ A_skew @ (V_pos.conj().T - V_neg.conj().T)


X0_gen = random_nilpotent_u64()
X7_gen = random_nilpotent_u64()

T_harm = [random_u64((14,)) for _ in range(5)]
alpha_harm = [random_u64((14,)) for _ in range(5)]
eta_harm = [random_u64() for _ in range(3)]
for h_arr in T_harm + alpha_harm + eta_harm:
    assert_in_u64(h_arr, "harmonic_coeff")


def d_dx0_grid(field, freqs):
    N_g = len(freqs)
    shape = (N_g,) + (1,) * (field.ndim - 1)
    return np.fft.ifft(1j * freqs.reshape(shape) * np.fft.fft(field, axis=0), axis=0)


def d_dx7_grid(field, freqs):
    N_g = len(freqs)
    shape = (1, N_g) + (1,) * (field.ndim - 2)
    return np.fft.ifft(1j * freqs.reshape(shape) * np.fft.fft(field, axis=1), axis=1)


# Verify fast kernels against theta_both_bare using relative Frobenius error (< 1e-12)
_r0_chk = random_u64((14,))
_r7_chk = random_u64((14,))
_r0_chk[0] = 0.0
_r7_chk[7] = 0.0
_r7_chk[0] = -_r0_chk[7]
_F_dbt_chk = np.zeros((14, 14, 128, 128), dtype=np.complex128)
_F_dbt_chk[0, :] += _r0_chk
_F_dbt_chk[:, 0] -= _r0_chk
_F_dbt_chk[7, :] += _r7_chk
_F_dbt_chk[:, 7] -= _r7_chk
_e1, _b1 = theta_both_dBT_fast(_r0_chk, _r7_chk)
_e2, _b2 = theta_both_bare(_F_dbt_chk)
assert np.linalg.norm(_e1 - _e2) / np.linalg.norm(_e2) < 1e-12
assert np.linalg.norm(_b1 - _b2) / np.linalg.norm(_b2) < 1e-12

_F_tt_chk = (T_harm[0][:, None] @ T_harm[0][None, :]) - (T_harm[0][None, :] @ T_harm[0][:, None])
_et1, _bt1 = theta_both_TT_fast(T_harm[0])
_et2, _bt2 = theta_both_bare(_F_tt_chk)
assert np.linalg.norm(_et1 - _et2) / np.linalg.norm(_et2) < 1e-12
assert np.linalg.norm(_bt1 - _bt2) / np.linalg.norm(_bt2) < 1e-12
del _F_dbt_chk, _F_tt_chk, _e1, _b1, _e2, _b2, _et1, _bt1, _et2, _bt2


# 1. 1D Slice Continuum Convergence Check across N = 8, 10, 14
def eval_1d_slice_convergence(N_1d: int):
    g1 = np.linspace(0, 2 * np.pi, N_1d, endpoint=False)
    fr1 = np.fft.fftfreq(N_1d, d=1.0 / N_1d)
    s0_1 = np.sin(g1)[:, None, None]
    c0_1 = np.cos(g1)[:, None, None]
    eps_1 = I128[None] + s0_1 * X0_gen[None]
    einv_1 = I128[None] - s0_1 * X0_gen[None]
    d0_eps_1 = np.fft.ifft(1j * fr1[:, None, None] * np.fft.fft(eps_1, axis=0), axis=0)
    B0_1 = einv_1 @ d0_eps_1
    B0_hat_1 = d0_eps_1 @ einv_1

    EA0_1 = np.zeros((N_1d, 128, 128), dtype=np.complex128)
    comm_A_EA_1 = np.zeros((N_1d, 128, 128), dtype=np.complex128)
    act_1 = 0.0
    zero_row = np.zeros((14, 128, 128), dtype=np.complex128)

    for i in range(N_1d):
        s_i, c_i = float(np.sin(g1[i])), float(np.cos(g1[i]))
        T_i = T_harm[0] + s_i * T_harm[1] + c_i * T_harm[2]
        d0T_i = c_i * T_harm[1] - s_i * T_harm[2]
        ep, ei = eps_1[i], einv_1[i]
        T_h = ep[None] @ T_i @ ei[None]
        d0T_h = ep[None] @ d0T_i @ ei[None]
        row0 = d0T_h + (B0_hat_1[i][None] @ T_h - T_h @ B0_hat_1[i][None])

        ein_dbt, _ = theta_both_dBT_fast(row0, zero_row)
        ein_tt, _ = theta_both_TT_fast(T_h)
        de_h = noncentral_delta_E_bare(T_h, ein_tt)

        K_hat = 0.5 * ein_dbt + (1.0 / 3.0) * ein_tt + 0.75 * T_h
        act_1 += float(np.einsum('a,akm,amk->', ETA_DIAG, T_h, K_hat).real)

        EA_hat = ein_dbt + ein_tt + (1.0 / 3.0) * de_h + 1.5 * T_h
        EA_i = ei[None] @ EA_hat @ ep[None]
        A_i = T_i.copy()
        A_i[0] += B0_1[i]
        EA0_1[i] = EA_i[0]
        comm_A_EA_1[i] = (np.einsum('a,akm,amn->kn', ETA_DIAG, A_i, EA_i)
                          - np.einsum('a,akm,amn->kn', ETA_DIAG, EA_i, A_i))

    eta_1 = eta_harm[0][None] + s0_1 * eta_harm[1][None] + c0_1 * eta_harm[2][None]
    d0_EA0 = np.fft.ifft(1j * fr1[:, None, None] * np.fft.fft(EA0_1, axis=0), axis=0)
    DA_EA_1 = ETA_DIAG[0] * d0_EA0 + comm_A_EA_1
    noether_1 = float(np.mean(np.einsum('ikm,imk->i', eta_1, DA_EA_1)).real)
    return act_1 / N_1d, noether_1


act_1d_8, noe_1d_8 = eval_1d_slice_convergence(8)
act_1d_10, noe_1d_10 = eval_1d_slice_convergence(10)
act_1d_14, noe_1d_14 = eval_1d_slice_convergence(14)
quad_1d_err = max(abs(act_1d_8 - act_1d_14), abs(act_1d_10 - act_1d_14)) / abs(act_1d_14)
noe_1d_err = max(abs(noe_1d_8 - noe_1d_14), abs(noe_1d_10 - noe_1d_14)) / abs(noe_1d_14)
assert quad_1d_err < 1e-10 and noe_1d_err < 1e-10
p6.update(2, force=True)


# 2. Setup 2D Active Grid Helper & Run Full 2D Grid Convergence (N = 8 vs N = 10)
def build_2d_grid_context(N_g: int):
    g1 = np.linspace(0, 2 * np.pi, N_g, endpoint=False)
    x0_g, x7_g = np.meshgrid(g1, g1, indexing='ij')
    fr_g = np.fft.fftfreq(N_g, d=1.0 / N_g)
    s0_g = np.sin(x0_g).reshape(N_g, N_g, 1, 1)
    c0_g = np.cos(x0_g).reshape(N_g, N_g, 1, 1)
    s7_g = np.sin(x7_g).reshape(N_g, N_g, 1, 1)
    c7_g = np.cos(x7_g).reshape(N_g, N_g, 1, 1)
    eps_g = (I128[None, None] + s0_g * X0_gen[None, None]) @ (I128[None, None] + c7_g * X7_gen[None, None])
    einv_g = (I128[None, None] - c7_g * X7_gen[None, None]) @ (I128[None, None] - s0_g * X0_gen[None, None])
    d0_ep = d_dx0_grid(eps_g, fr_g)
    d7_ep = d_dx7_grid(eps_g, fr_g)
    B0_g = einv_g @ d0_ep
    B7_g = einv_g @ d7_ep
    B0_h_g = d0_ep @ einv_g
    B7_h_g = d7_ep @ einv_g
    eta_g = eta_harm[0][None, None] + s0_g * eta_harm[1][None, None] + c7_g * eta_harm[2][None, None]
    return (N_g, g1, fr_g, np.sin(g1), np.cos(g1), s0_g, c0_g, s7_g, c7_g,
            eps_g, einv_g, B0_g, B7_g, B0_h_g, B7_h_g, eta_g)


ctx8 = build_2d_grid_context(8)
ctx10 = build_2d_grid_context(10)
(N, grid_1d, freqs, SIN_1D, COS_1D, s0_4d, c0_4d, s7_4d, c7_4d,
 eps, eps_inv, B0_field, B7_field, B0_hat_base, B7_hat_base, eta_gauge) = ctx8

assert_in_u64(B0_field, "B0_field")
assert_in_u64(B7_field, "B7_field")
assert_in_u64(eta_gauge, "eta_gauge")

F07_actual = d_dx0_grid(B7_field, freqs) - d_dx7_grid(B0_field, freqs) + (B0_field @ B7_field - B7_field @ B0_field)
mc_flat_err = float(np.max(np.abs(F07_actual)))
assert mc_flat_err < 1e-11
p6.update(3, force=True)

# 3. Deterministic -256 Dressed Kinetic Witness
T_wit_1 = eps_inv @ (s0_4d * (gammas[0] @ gammas[1])[None, None]) @ eps
T_wit_2 = eps_inv @ (c0_4d * gammas[2][None, None]) @ eps
d0_Tw1 = d_dx0_grid(T_wit_1, freqs)
d7_Tw1 = d_dx7_grid(T_wit_1, freqs)
d0_Tw2 = d_dx0_grid(T_wit_2, freqs)
d7_Tw2 = d_dx7_grid(T_wit_2, freqs)

I_kin_wit_acc = 0.0
_r0_w = np.zeros((14, 128, 128), dtype=np.complex128)
_r7_w = np.zeros((14, 128, 128), dtype=np.complex128)
for i in range(N):
    for j in range(N):
        ep, ei = eps[i, j], eps_inv[i, j]
        B0_h, B7_h = B0_hat_base[i, j], B7_hat_base[i, j]
        T1_h = ep @ T_wit_1[i, j] @ ei
        T2_h = ep @ T_wit_2[i, j] @ ei
        _r0_w.fill(0.0)
        _r7_w.fill(0.0)
        _r0_w[1] = ep @ d0_Tw1[i, j] @ ei + (B0_h @ T1_h - T1_h @ B0_h)
        _r0_w[2] = ep @ d0_Tw2[i, j] @ ei + (B0_h @ T2_h - T2_h @ B0_h)
        _r7_w[1] = ep @ d7_Tw1[i, j] @ ei + (B7_h @ T1_h - T1_h @ B7_h)
        _r7_w[2] = ep @ d7_Tw2[i, j] @ ei + (B7_h @ T2_h - T2_h @ B7_h)

        ein_dbt, _ = theta_both_dBT_fast(_r0_w, _r7_w)
        val_ij = 0.5 * (ETA_DIAG[1] * np.trace(T1_h @ ein_dbt[1]) + ETA_DIAG[2] * np.trace(T2_h @ ein_dbt[2]))
        I_kin_wit_acc += float(val_ij.real)

I_kin_wit = I_kin_wit_acc / (N * N)
h_wit = 1e-6
dI_kin_wit = (((1.0 + h_wit) ** 2 - (1.0 - h_wit) ** 2) / (2.0 * h_wit)) * I_kin_wit
wit_err = abs(dI_kin_wit + 256.0) / 256.0
assert abs(I_kin_wit + 128.0) < 1e-9 and wit_err < 1e-7
del T_wit_1, T_wit_2, d0_Tw1, d7_Tw1, d0_Tw2, d7_Tw2, _r0_w, _r7_w
p6.update(5, force=True)

# 4. Site-Streaming Evaluator for Mixed-Harmonic Action, 2D Convergence, & Coupled Dressing Variations
KAPPA1 = 1.5


def eval_streaming_grid(s_alpha: float = 0.0, s_eta: float = 0.0, full_el_analysis: bool = False, ctx=ctx8):
    (N_c, _, fr_c, sin_c, cos_c, _, _, _, _,
     eps_c, einv_c, B0_c, B7_c, B0_hat_c, B7_hat_c, eta_c) = ctx
    H_T = [T_harm[k] + s_alpha * alpha_harm[k] for k in range(5)]

    if s_eta == 0.0:
        eps_g, einv_g = eps_c, einv_c
        B0_g, B7_g = B0_c, B7_c
        B0_hat_g, B7_hat_g = B0_hat_c, B7_hat_c
        has_delta_B = False
    else:
        half_s_eta = 0.5 * s_eta * eta_c
        h_s = np.linalg.solve(I128[None, None] - half_s_eta, I128[None, None] + half_s_eta)
        h_s_inv = np.linalg.solve(I128[None, None] + half_s_eta, I128[None, None] - half_s_eta)
        eps_g = eps_c @ h_s
        einv_g = h_s_inv @ einv_c
        d0_eps_s = d_dx0_grid(eps_g, fr_c)
        d7_eps_s = d_dx7_grid(eps_g, fr_c)
        B0_g = einv_g @ d0_eps_s
        B7_g = einv_g @ d7_eps_s
        B0_hat_g = d0_eps_s @ einv_g
        B7_hat_g = d7_eps_s @ einv_g
        Delta_B0 = B0_c - B0_g
        Delta_B7 = B7_c - B7_g
        d0_DB0 = d_dx0_grid(Delta_B0, fr_c)
        d7_DB0 = d_dx7_grid(Delta_B0, fr_c)
        d0_DB7 = d_dx0_grid(Delta_B7, fr_c)
        d7_DB7 = d_dx7_grid(Delta_B7, fr_c)
        has_delta_B = True

    act_kin = 0.0
    act_cub = 0.0
    act_mas = 0.0
    act_bia_kin = 0.0
    act_bia_cub = 0.0

    if full_el_analysis:
        c_kin = 0.0
        c_tt = 0.0
        c_de = 0.0
        c_mas = 0.0
        EA0_full = np.zeros((N_c, N_c, 128, 128), dtype=np.complex128)
        EA7_full = np.zeros((N_c, N_c, 128, 128), dtype=np.complex128)
        EA0_naive = np.zeros((N_c, N_c, 128, 128), dtype=np.complex128)
        EA7_naive = np.zeros((N_c, N_c, 128, 128), dtype=np.complex128)
        comm_A_EA_full = np.zeros((N_c, N_c, 128, 128), dtype=np.complex128)
        comm_A_EA_naive = np.zeros((N_c, N_c, 128, 128), dtype=np.complex128)
        ibp_fixed_eps_acc = 0.0
        d0_eta_grid = d_dx0_grid(eta_c, fr_c)
        d7_eta_grid = d_dx7_grid(eta_c, fr_c)

    for i in range(N_c):
        s0_i, c0_i = sin_c[i], cos_c[i]
        T_x0 = H_T[0] + s0_i * H_T[1] + c0_i * H_T[2]
        d0T_base = c0_i * H_T[1] - s0_i * H_T[2]
        for j in range(N_c):
            s7_j, c7_j = sin_c[j], cos_c[j]
            T_ij = T_x0 + s7_j * H_T[3] + c7_j * H_T[4]
            d0T_ij = d0T_base
            d7T_ij = c7_j * H_T[3] - s7_j * H_T[4]

            if has_delta_B:
                T_ij = T_ij.copy()
                d0T_ij = d0T_ij.copy()
                d7T_ij = d7T_ij.copy()
                T_ij[0] += Delta_B0[i, j]
                T_ij[7] += Delta_B7[i, j]
                d0T_ij[0] += d0_DB0[i, j]
                d0T_ij[7] += d0_DB7[i, j]
                d7T_ij[0] += d7_DB0[i, j]
                d7T_ij[7] += d7_DB7[i, j]

            ep, ei = eps_g[i, j], einv_g[i, j]
            T_hat = ep[None] @ T_ij @ ei[None]
            d0T_hat = ep[None] @ d0T_ij @ ei[None]
            d7T_hat = ep[None] @ d7T_ij @ ei[None]
            B0_h, B7_h = B0_hat_g[i, j], B7_hat_g[i, j]

            row0 = d0T_hat + (B0_h[None] @ T_hat - T_hat @ B0_h[None])
            row7 = d7T_hat + (B7_h[None] @ T_hat - T_hat @ B7_h[None])

            ein_dbt, bia_dbt = theta_both_dBT_fast(row0, row7)
            ein_tt, bia_tt = theta_both_TT_fast(T_hat)

            act_kin += float(np.einsum('a,akm,amk->', ETA_DIAG, T_hat, 0.5 * ein_dbt).real)
            act_cub += float(np.einsum('a,akm,amk->', ETA_DIAG, T_hat, ein_tt).real)
            act_mas += float(np.einsum('a,akm,amk->', ETA_DIAG, T_hat, T_hat).real)
            act_bia_kin += float(np.einsum('a,akm,amk->', ETA_DIAG, T_hat, 0.5 * bia_dbt).real)
            act_bia_cub += float(np.einsum('a,akm,amk->', ETA_DIAG, T_hat, (1.0 / 3.0) * bia_tt).real)

            if full_el_analysis:
                de_hat = noncentral_delta_E_bare(T_hat, ein_tt)
                al_ij = (alpha_harm[0] + s0_i * alpha_harm[1] + c0_i * alpha_harm[2]
                         + s7_j * alpha_harm[3] + c7_j * alpha_harm[4])
                al_hat = ep[None] @ al_ij @ ei[None]

                c_kin += float(np.einsum('a,akm,amk->', ETA_DIAG, al_hat, ein_dbt).real)
                c_tt += float(np.einsum('a,akm,amk->', ETA_DIAG, al_hat, ein_tt).real)
                c_de += float(np.einsum('a,akm,amk->', ETA_DIAG, al_hat, de_hat).real)
                c_mas += float(np.einsum('a,akm,amk->', ETA_DIAG, al_hat, T_hat).real)

                EA_hat_full = ein_dbt + ein_tt + (1.0 / 3.0) * de_hat + 1.5 * T_hat
                EA_hat_naive = ein_dbt + ein_tt + 1.5 * T_hat
                EA_ij_full = ei[None] @ EA_hat_full @ ep[None]
                EA_ij_naive = ei[None] @ EA_hat_naive @ ep[None]

                EA0_full[i, j] = EA_ij_full[0]
                EA7_full[i, j] = EA_ij_full[7]
                EA0_naive[i, j] = EA_ij_naive[0]
                EA7_naive[i, j] = EA_ij_naive[7]

                A_ij = T_ij.copy()
                A_ij[0] += B0_g[i, j]
                A_ij[7] += B7_g[i, j]
                comm_A_EA_full[i, j] = (np.einsum('a,akm,amn->kn', ETA_DIAG, A_ij, EA_ij_full)
                                        - np.einsum('a,akm,amn->kn', ETA_DIAG, EA_ij_full, A_ij))
                comm_A_EA_naive[i, j] = (np.einsum('a,akm,amn->kn', ETA_DIAG, A_ij, EA_ij_naive)
                                         - np.einsum('a,akm,amn->kn', ETA_DIAG, EA_ij_naive, A_ij))

                eta_ij = eta_c[i, j]
                dA_eta_ij = A_ij @ eta_ij[None] - eta_ij[None] @ A_ij
                dA_eta_ij[0] += d0_eta_grid[i, j]
                dA_eta_ij[7] += d7_eta_grid[i, j]
                ibp_fixed_eps_acc -= float(np.einsum('a,akm,amk->', ETA_DIAG, dA_eta_ij, EA_ij_full).real)

    inv_N2 = 1.0 / (N_c * N_c)
    actions = (act_kin * inv_N2, act_cub * inv_N2, act_mas * inv_N2,
               act_bia_kin * inv_N2, act_bia_cub * inv_N2)
    if not full_el_analysis:
        return actions

    DA_EA_full = (ETA_DIAG[0] * d_dx0_grid(EA0_full, fr_c)
                  + ETA_DIAG[7] * d_dx7_grid(EA7_full, fr_c)
                  + comm_A_EA_full)
    DA_EA_naive = (ETA_DIAG[0] * d_dx0_grid(EA0_naive, fr_c)
                   + ETA_DIAG[7] * d_dx7_grid(EA7_naive, fr_c)
                   + comm_A_EA_naive)
    ana_noether_full = float(np.mean(np.einsum('ijkm,ijmk->ij', eta_c, DA_EA_full)).real)
    ana_noether_naive = float(np.mean(np.einsum('ijkm,ijmk->ij', eta_c, DA_EA_naive)).real)
    ana_ibp_fixed_eps = ibp_fixed_eps_acc * inv_N2

    return actions, (c_kin * inv_N2, c_tt * inv_N2, c_de * inv_N2, c_mas * inv_N2,
                     ana_noether_full, ana_noether_naive, ana_ibp_fixed_eps)


# Full 2D Grid Continuum Convergence Check: N = 8 vs N = 10
act_base_10, (_, _, _, _, noe_2d_10, _, _) = eval_streaming_grid(0.0, 0.0, full_el_analysis=True, ctx=ctx10)
del ctx10
gc.collect()
p6.update(7, force=True)

act_base_8, (c_kin_base, c_tt_base, c_de_base, c_mas_base,
             ana_noether_full, ana_noether_naive, ana_ibp_fixed_eps) = eval_streaming_grid(0.0, 0.0, full_el_analysis=True, ctx=ctx8)
p6.update(9, force=True)

I_2d_8 = act_base_8[0] + (1.0 / 3.0) * act_base_8[1] + 0.75 * act_base_8[2]
I_2d_10 = act_base_10[0] + (1.0 / 3.0) * act_base_10[1] + 0.75 * act_base_10[2]
quad_2d_err = abs(I_2d_8 - I_2d_10) / abs(I_2d_10)
noe_2d_err = abs(ana_noether_full - noe_2d_10) / abs(noe_2d_10)
assert quad_2d_err < 1e-10 and noe_2d_err < 1e-10

eps_fd = 1e-6
act_p = eval_streaming_grid(+eps_fd, 0.0, full_el_analysis=False, ctx=ctx8)
p6.update(11, force=True)
act_m = eval_streaming_grid(-eps_fd, 0.0, full_el_analysis=False, ctx=ctx8)
p6.update(12, force=True)

fd_kin_only = (act_p[0] - act_m[0]) / (2.0 * eps_fd)
ana_kin_only = c_kin_base
kin_ibp_err = abs(fd_kin_only - ana_kin_only) / abs(fd_kin_only)
assert kin_ibp_err < 1e-7

fd_bia_kin = (act_p[3] - act_m[3]) / (2.0 * eps_fd)
fd_bia_cub = (act_p[4] - act_m[4]) / (2.0 * eps_fd)
rel_bia_kin = abs(fd_bia_kin) / abs(ana_kin_only)
rel_bia_cub = abs(fd_bia_cub) / abs(c_tt_base)
assert rel_bia_kin < 1e-7 and rel_bia_cub < 1e-7

var_results = {}
for label, lam, m_coeff in [
    ("Case A (lam=1/3, m=kappa1/2)", 1.0 / 3.0, 0.5 * KAPPA1),
    ("Case B (lam=2/3, m=kappa1)  ", 2.0 / 3.0, KAPPA1),
]:
    I_p = act_p[0] + lam * act_p[1] + m_coeff * act_p[2]
    I_m = act_m[0] + lam * act_m[1] + m_coeff * act_m[2]
    fd_tot = (I_p - I_m) / (2.0 * eps_fd)
    ck = c_kin_base
    cc = 3.0 * lam * c_tt_base
    cn = lam * c_de_base
    cm = 2.0 * m_coeff * c_mas_base
    ana_exact = ck + cc + cn + cm
    ana_naive = ck + c_tt_base + cm
    err_exact = abs(fd_tot - ana_exact) / abs(fd_tot)
    err_naive = abs(fd_tot - ana_naive) / abs(fd_tot)
    assert err_exact < 1e-7 and err_naive > 0.05
    var_results[label] = (fd_tot, ana_exact, ana_naive, err_exact, err_naive, ck, cc, cn, cm)

lam_A, m_A = 1.0 / 3.0, 0.5 * KAPPA1
act_eta_p = eval_streaming_grid(0.0, +eps_fd, full_el_analysis=False, ctx=ctx8)
p6.update(14, force=True)
act_eta_m = eval_streaming_grid(0.0, -eps_fd, full_el_analysis=False, ctx=ctx8)

I_coupled_p = act_eta_p[0] + lam_A * act_eta_p[1] + m_A * act_eta_p[2]
I_coupled_m = act_eta_m[0] + lam_A * act_eta_m[1] + m_A * act_eta_m[2]
fd_coupled_fixed_A = (I_coupled_p - I_coupled_m) / (2.0 * eps_fd)

noether_rel_err = abs(fd_coupled_fixed_A - ana_noether_full) / abs(fd_coupled_fixed_A)
noether_naive_err = abs(fd_coupled_fixed_A - ana_noether_naive) / abs(fd_coupled_fixed_A)
ibp_match_err = abs(ana_ibp_fixed_eps - ana_noether_full) / abs(ana_noether_full)
assert noether_rel_err < 1e-7 and ibp_match_err < 1e-10 and noether_naive_err > 0.05
p6.update(15, force=True)

p6.finish(f"Full 14D Action: Wit={wit_err:.2e}, Kin IBP={kin_ibp_err:.2e}, Case A={var_results['Case A (lam=1/3, m=kappa1/2)'][3]:.2e}, Coupled Noether={noether_rel_err:.2e}")
print(f"    * 1D & 2D grid convergence:     1D(8,10,14) I={quad_1d_err:.2e}, Noe={noe_1d_err:.2e} | 2D(8 vs 10) I={quad_2d_err:.2e}, Noe={noe_2d_err:.2e}")
print(f"    * Dressed -256 kinetic witness: I_kin = {I_kin_wit:+.6f} (-128), dI_kin[T] = {dI_kin_wit:+.6f} (-256, err = {wit_err:.2e})")
print(f"    * Commutator-sector bulk var:   rel_kin = {rel_bia_kin:.2e}, rel_cub = {rel_bia_cub:.2e} (invisible in bulk)")
for label, (fd_v, ex_v, nv_v, e_ex, e_nv, ck, cc, cn, cm) in var_results.items():
    print(f"    * {label}:")
    print(f"        Channels: kin={ck:+.1f}, cub={cc:+.1f}, noncentral={cn:+.1f}, mass={cm:+.1f}")
    print(f"        FD = {fd_v:+.4f} | Exact EL = {ex_v:+.4f} (err = {e_ex:.2e}) | Naive Eq.9.7 = {nv_v:+.4f} (err = {e_nv:.1%})")
print(f"    * True Fixed-A Coupled Noether: FD dI/ds|_A = {fd_coupled_fixed_A:+.4f} | <eta, D_A^a E_A> = {ana_noether_full:+.4f} (err = {noether_rel_err:.2e}, IBP diff = {ibp_match_err:.2e}) | Naive (no Delta_E) = {ana_noether_naive:+.4f} (err = {noether_naive_err:.1%})")

_, peak_bytes = tracemalloc.get_traced_memory()
tracemalloc.stop()
script_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:16] if "__file__" in globals() else "interactive"
print(f"\n[ALL 6 VERIFICATION GROUPS PASSED IN {time.perf_counter() - t0:.2f}s | Peak tracemalloc allocation: {peak_bytes / (1024**2):.1f} MiB | Python {platform.python_version()} / NumPy {np.__version__} | SHA256: {script_hash}]")
~~~

[Return to file index](#file-index)

## lakefile.toml {#source-lakefile-toml}

Declares the 39 Lean library targets and pins Mathlib to v4.33.1.

~~~toml
name = "geometric_unity"
defaultTargets = ["Theorem52", "WitnessW1", "D7Counts", "BianchiSymbol", "NoetherIdentity", "D7Classification", "D7Exterior", "D7Hodge", "D7Irreducible", "D7VectorTensor", "D7Hook", "D7VectorGrades", "D7MiddleTensor", "D7MiddleIrreducible", "D7TensorColumns", "D7TensorRotations", "D7GradeIrreducible", "D7ComplementaryGrades", "D7SignedDistinction", "D7TripleInvariants", "D7TripleMultiplicity", "D7QuadInvariants", "D7QuadMultiplicity", "D7Unrestricted", "D7Final", "D7BianchiFields", "D7UnitaryRealForm", "D7SpinAction", "D7CliffordMatrix", "D7CliffordAdjoint", "D7SpinNullFrame", "D7SpinRootLifts", "D7SpinOrientation", "D7RootInterpolation", "D7RootGeneration", "D7RealComparison", "D7RealJets", "D7RealRanks", "D7RealTheorem"]

[[require]]
name = "mathlib"
git = "https://github.com/leanprover-community/mathlib4.git"
rev = "v4.33.1"

[[lean_lib]]
name = "Theorem52"
srcDir = "."

[[lean_lib]]
name = "WitnessW1"
srcDir = "."

[[lean_lib]]
name = "D7Counts"
srcDir = "."

[[lean_lib]]
name = "BianchiSymbol"
srcDir = "."

[[lean_lib]]
name = "NoetherIdentity"
srcDir = "."

[[lean_lib]]
name = "D7Classification"
srcDir = "."

[[lean_lib]]
name = "D7Exterior"
srcDir = "."

[[lean_lib]]
name = "D7Hodge"
srcDir = "."

[[lean_lib]]
name = "D7Irreducible"
srcDir = "."

[[lean_lib]]
name = "D7VectorTensor"
srcDir = "."

[[lean_lib]]
name = "D7Hook"
srcDir = "."

[[lean_lib]]
name = "D7VectorGrades"
srcDir = "."

[[lean_lib]]
name = "D7MiddleTensor"
srcDir = "."

[[lean_lib]]
name = "D7MiddleIrreducible"
srcDir = "."

[[lean_lib]]
name = "D7TensorColumns"
srcDir = "."

[[lean_lib]]
name = "D7TensorRotations"
srcDir = "."

[[lean_lib]]
name = "D7GradeIrreducible"
srcDir = "."

[[lean_lib]]
name = "D7ComplementaryGrades"
srcDir = "."

[[lean_lib]]
name = "D7SignedDistinction"
srcDir = "."

[[lean_lib]]
name = "D7TripleInvariants"
srcDir = "."

[[lean_lib]]
name = "D7TripleMultiplicity"
srcDir = "."

[[lean_lib]]
name = "D7QuadInvariants"
srcDir = "."

[[lean_lib]]
name = "D7QuadMultiplicity"
srcDir = "."

[[lean_lib]]
name = "D7Unrestricted"
srcDir = "."

[[lean_lib]]
name = "D7Final"
srcDir = "."

[[lean_lib]]
name = "D7BianchiFields"
srcDir = "."

[[lean_lib]]
name = "D7UnitaryRealForm"
srcDir = "."

[[lean_lib]]
name = "D7SpinAction"
srcDir = "."

[[lean_lib]]
name = "D7CliffordMatrix"
srcDir = "."

[[lean_lib]]
name = "D7CliffordAdjoint"
srcDir = "."

[[lean_lib]]
name = "D7SpinNullFrame"
srcDir = "."

[[lean_lib]]
name = "D7SpinRootLifts"
srcDir = "."

[[lean_lib]]
name = "D7SpinOrientation"
srcDir = "."

[[lean_lib]]
name = "D7RootInterpolation"
srcDir = "."

[[lean_lib]]
name = "D7RootGeneration"
srcDir = "."

[[lean_lib]]
name = "D7RealComparison"
srcDir = "."

[[lean_lib]]
name = "D7RealTheorem"
srcDir = "."

[[lean_lib]]
name = "D7RealJets"
srcDir = "."

[[lean_lib]]
name = "D7RealRanks"
srcDir = "."
~~~

[Return to file index](#file-index)

## lake-manifest.json {#source-lake-manifest-json}

Records the exact Mathlib and transitive dependency revisions for the portable project.

~~~json
{
  "version": "1.2.0",
  "packagesDir": ".lake/packages",
  "packages": [
    {
      "url": "https://github.com/leanprover-community/mathlib4.git",
      "type": "git",
      "subDir": null,
      "scope": "",
      "rev": "0df444a360eaa60ab8c11dca51a86af692955474",
      "name": "mathlib",
      "manifestFile": "lake-manifest.json",
      "inputRev": "v4.33.1",
      "inherited": false,
      "configFile": "lakefile.lean"
    },
    {
      "url": "https://github.com/leanprover-community/plausible",
      "type": "git",
      "subDir": null,
      "scope": "leanprover-community",
      "rev": "b7eb3304aeae834b12dda98993a37f6a41f6f0bb",
      "name": "plausible",
      "manifestFile": "lake-manifest.json",
      "inputRev": "main",
      "inherited": true,
      "configFile": "lakefile.toml"
    },
    {
      "url": "https://github.com/leanprover-community/LeanSearchClient",
      "type": "git",
      "subDir": null,
      "scope": "leanprover-community",
      "rev": "5f4d51b81cbd3f6b32b156bfad9056621a040404",
      "name": "LeanSearchClient",
      "manifestFile": "lake-manifest.json",
      "inputRev": "main",
      "inherited": true,
      "configFile": "lakefile.toml"
    },
    {
      "url": "https://github.com/leanprover-community/import-graph",
      "type": "git",
      "subDir": null,
      "scope": "leanprover-community",
      "rev": "16f02aa7642864af59f1ff0e384a015994db9118",
      "name": "importGraph",
      "manifestFile": "lake-manifest.json",
      "inputRev": "main",
      "inherited": true,
      "configFile": "lakefile.toml"
    },
    {
      "url": "https://github.com/leanprover-community/ProofWidgets4",
      "type": "git",
      "subDir": null,
      "scope": "leanprover-community",
      "rev": "4be2e3d5087eeb272cf5a8853b8f9dd025ef5957",
      "name": "proofwidgets",
      "manifestFile": "lake-manifest.json",
      "inputRev": "main",
      "inherited": true,
      "configFile": "lakefile.lean"
    },
    {
      "url": "https://github.com/leanprover-community/aesop",
      "type": "git",
      "subDir": null,
      "scope": "leanprover-community",
      "rev": "3448c0bcc5ce01b2d1546e483ec3620e32df3d0e",
      "name": "aesop",
      "manifestFile": "lake-manifest.json",
      "inputRev": "master",
      "inherited": true,
      "configFile": "lakefile.toml"
    },
    {
      "url": "https://github.com/leanprover-community/quote4",
      "type": "git",
      "subDir": null,
      "scope": "leanprover-community",
      "rev": "92c15be17b7caf78c2ad767ec40f89052d908d81",
      "name": "Qq",
      "manifestFile": "lake-manifest.json",
      "inputRev": "master",
      "inherited": true,
      "configFile": "lakefile.toml"
    },
    {
      "url": "https://github.com/leanprover-community/batteries",
      "type": "git",
      "subDir": null,
      "scope": "leanprover-community",
      "rev": "4488d40d070b9700d4d5a6aa342f0d40c31b2a2d",
      "name": "batteries",
      "manifestFile": "lake-manifest.json",
      "inputRev": "main",
      "inherited": true,
      "configFile": "lakefile.toml"
    },
    {
      "url": "https://github.com/leanprover/lean4-cli",
      "type": "git",
      "subDir": null,
      "scope": "leanprover",
      "rev": "6130a47896ce867c6a4a55373441e59e565bad0f",
      "name": "Cli",
      "manifestFile": "lake-manifest.json",
      "inputRev": "v4.33.0",
      "inherited": true,
      "configFile": "lakefile.toml"
    }
  ],
  "name": "geometric_unity",
  "lakeDir": ".lake",
  "fixedToolchain": false
}
~~~

[Return to file index](#file-index)

## lean-toolchain {#source-lean-toolchain}

Pins Lean to leanprover/lean4:v4.33.1.

~~~text
leanprover/lean4:v4.33.1
~~~

[Return to file index](#file-index)

# Publication and license listings

These files accompany the source code in the archive and specify the publication identifier and license terms.

## README.md {#source-readme-md}

Records the publication DOI and citation, archive contents, and the scope of the text and software licenses.

~~~markdown
# Geometric Unity verification archive

*Clifford Contractions and the First-Order Bosonic Action in Geometric Unity*

R. Fisher · Braid Dynamics Applied Research Group

November 17, 2026

DOI: [10.5281/zenodo.24325062](https://doi.org/10.5281/zenodo.24325062)

## Contents and use

This archive contains 40 Lean files, the Python verification program `GU-test.py`, and three project configuration files. Extract `fisher-geometric-unity-2026-11-17-code.zip` to obtain the `gu-code` directory. The accompanying `fisher-geometric-unity-2026-11-17-code-guide.pdf` describes every source file, the assumptions of the formalizations, dependency installation, execution commands, and benchmark results. The accompanying `fisher-geometric-unity-2026-11-17-computational-supplement.md` contains the complete source listings in Markdown.

`SHA256SUMS` records the SHA-256 digest of every other file in this archive, including this README and both license files. Source files match their listings in the computational supplement, using UTF-8 text and Unix line endings.

## License scope

Copyright (c) 2026 R. Fisher.

- **Text and figures:** the technical note, the Code Guide, the prose and figures in the computational supplement, and this README are licensed under Creative Commons Attribution 4.0 International (CC BY 4.0). The full terms are included in `LICENSE-CC-BY-4.0.txt` and at <https://creativecommons.org/licenses/by/4.0/>.
- **Software:** all 40 Lean source files, `GU-test.py`, and the project configuration files `lakefile.toml`, `lake-manifest.json`, and `lean-toolchain` are licensed under the MIT License. This applies equally to their source listings embedded in the computational supplement. The full terms, including the copyright and permission notice, are included in `LICENSE-MIT.txt`.

These grants apply specifically to this Geometric Unity publication and its accompanying software, including copies obtained from Zenodo or the website. They take precedence for these materials over general website or repository notices. Third-party works and dependencies retain their own licenses; dependencies are downloaded separately and are not included in this archive. The reproduced license texts retain their own applicable terms.

## Citation

Fisher, R. (2026). *Clifford Contractions and the First-Order Bosonic Action in Geometric Unity*. https://doi.org/10.5281/zenodo.24325062
~~~

[Return to file index](#file-index)

## LICENSE-CC-BY-4.0.txt {#source-license-cc-by-4-0-txt}

Contains the full Creative Commons Attribution 4.0 International terms for the text and figures.

~~~text
Creative Commons Attribution 4.0 International

 Creative Commons Corporation (“Creative Commons”) is not a law firm and does not provide legal services or legal advice. Distribution of Creative Commons public licenses does not create a lawyer-client or other relationship. Creative Commons makes its licenses and related information available on an “as-is” basis. Creative Commons gives no warranties regarding its licenses, any material licensed under their terms and conditions, or any related information. Creative Commons disclaims all liability for damages resulting from their use to the fullest extent possible.

Using Creative Commons Public Licenses

Creative Commons public licenses provide a standard set of terms and conditions that creators and other rights holders may use to share original works of authorship and other material subject to copyright and certain other rights specified in the public license below. The following considerations are for informational purposes only, are not exhaustive, and do not form part of our licenses.

Considerations for licensors: Our public licenses are intended for use by those authorized to give the public permission to use material in ways otherwise restricted by copyright and certain other rights. Our licenses are irrevocable. Licensors should read and understand the terms and conditions of the license they choose before applying it. Licensors should also secure all rights necessary before applying our licenses so that the public can reuse the material as expected. Licensors should clearly mark any material not subject to the license. This includes other CC-licensed material, or material used under an exception or limitation to copyright. More considerations for licensors.

Considerations for the public: By using one of our public licenses, a licensor grants the public permission to use the licensed material under specified terms and conditions. If the licensor’s permission is not necessary for any reason–for example, because of any applicable exception or limitation to copyright–then that use is not regulated by the license. Our licenses grant only permissions under copyright and certain other rights that a licensor has authority to grant. Use of the licensed material may still be restricted for other reasons, including because others have copyright or other rights in the material. A licensor may make special requests, such as asking that all changes be marked or described. Although not required by our licenses, you are encouraged to respect those requests where reasonable. More considerations for the public.

Creative Commons Attribution 4.0 International Public License

By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution 4.0 International Public License ("Public License"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.

Section 1 – Definitions.

     a.	Adapted Material means material subject to Copyright and Similar Rights that is derived from or based upon the Licensed Material and in which the Licensed Material is translated, altered, arranged, transformed, or otherwise modified in a manner requiring permission under the Copyright and Similar Rights held by the Licensor. For purposes of this Public License, where the Licensed Material is a musical work, performance, or sound recording, Adapted Material is always produced where the Licensed Material is synched in timed relation with a moving image.

     b.	Adapter's License means the license You apply to Your Copyright and Similar Rights in Your contributions to Adapted Material in accordance with the terms and conditions of this Public License.

     c.	Copyright and Similar Rights means copyright and/or similar rights closely related to copyright including, without limitation, performance, broadcast, sound recording, and Sui Generis Database Rights, without regard to how the rights are labeled or categorized. For purposes of this Public License, the rights specified in Section 2(b)(1)-(2) are not Copyright and Similar Rights.

     d.	Effective Technological Measures means those measures that, in the absence of proper authority, may not be circumvented under laws fulfilling obligations under Article 11 of the WIPO Copyright Treaty adopted on December 20, 1996, and/or similar international agreements.

     e.	Exceptions and Limitations means fair use, fair dealing, and/or any other exception or limitation to Copyright and Similar Rights that applies to Your use of the Licensed Material.

     f.	Licensed Material means the artistic or literary work, database, or other material to which the Licensor applied this Public License.

     g.	Licensed Rights means the rights granted to You subject to the terms and conditions of this Public License, which are limited to all Copyright and Similar Rights that apply to Your use of the Licensed Material and that the Licensor has authority to license.

     h.	Licensor means the individual(s) or entity(ies) granting rights under this Public License.

     i.	Share means to provide material to the public by any means or process that requires permission under the Licensed Rights, such as reproduction, public display, public performance, distribution, dissemination, communication, or importation, and to make material available to the public including in ways that members of the public may access the material from a place and at a time individually chosen by them.

     j.	Sui Generis Database Rights means rights other than copyright resulting from Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, as amended and/or succeeded, as well as other essentially equivalent rights anywhere in the world.

     k.	You means the individual or entity exercising the Licensed Rights under this Public License. Your has a corresponding meaning.

Section 2 – Scope.

     a.	License grant.

          1. Subject to the terms and conditions of this Public License, the Licensor hereby grants You a worldwide, royalty-free, non-sublicensable, non-exclusive, irrevocable license to exercise the Licensed Rights in the Licensed Material to:

               A. reproduce and Share the Licensed Material, in whole or in part; and

               B. produce, reproduce, and Share Adapted Material.

          2. Exceptions and Limitations. For the avoidance of doubt, where Exceptions and Limitations apply to Your use, this Public License does not apply, and You do not need to comply with its terms and conditions.

          3. Term. The term of this Public License is specified in Section 6(a).

          4. Media and formats; technical modifications allowed. The Licensor authorizes You to exercise the Licensed Rights in all media and formats whether now known or hereafter created, and to make technical modifications necessary to do so. The Licensor waives and/or agrees not to assert any right or authority to forbid You from making technical modifications necessary to exercise the Licensed Rights, including technical modifications necessary to circumvent Effective Technological Measures. For purposes of this Public License, simply making modifications authorized by this Section 2(a)(4) never produces Adapted Material.

          5. Downstream recipients.

               A. Offer from the Licensor – Licensed Material. Every recipient of the Licensed Material automatically receives an offer from the Licensor to exercise the Licensed Rights under the terms and conditions of this Public License.

               B. No downstream restrictions. You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, the Licensed Material if doing so restricts exercise of the Licensed Rights by any recipient of the Licensed Material.

          6.  No endorsement. Nothing in this Public License constitutes or may be construed as permission to assert or imply that You are, or that Your use of the Licensed Material is, connected with, or sponsored, endorsed, or granted official status by, the Licensor or others designated to receive attribution as provided in Section 3(a)(1)(A)(i).

b. Other rights.

          1. Moral rights, such as the right of integrity, are not licensed under this Public License, nor are publicity, privacy, and/or other similar personality rights; however, to the extent possible, the Licensor waives and/or agrees not to assert any such rights held by the Licensor to the limited extent necessary to allow You to exercise the Licensed Rights, but not otherwise.

          2. Patent and trademark rights are not licensed under this Public License.

          3. To the extent possible, the Licensor waives any right to collect royalties from You for the exercise of the Licensed Rights, whether directly or through a collecting society under any voluntary or waivable statutory or compulsory licensing scheme. In all other cases the Licensor expressly reserves any right to collect such royalties.

Section 3 – License Conditions.

Your exercise of the Licensed Rights is expressly made subject to the following conditions.

     a.	Attribution.

          1. If You Share the Licensed Material (including in modified form), You must:

               A. retain the following if it is supplied by the Licensor with the Licensed Material:

                    i. identification of the creator(s) of the Licensed Material and any others designated to receive attribution, in any reasonable manner requested by the Licensor (including by pseudonym if designated);

                    ii. a copyright notice;

                    iii. a notice that refers to this Public License;

                    iv.	a notice that refers to the disclaimer of warranties;

                    v. a URI or hyperlink to the Licensed Material to the extent reasonably practicable;

               B. indicate if You modified the Licensed Material and retain an indication of any previous modifications; and

               C. indicate the Licensed Material is licensed under this Public License, and include the text of, or the URI or hyperlink to, this Public License.

          2. You may satisfy the conditions in Section 3(a)(1) in any reasonable manner based on the medium, means, and context in which You Share the Licensed Material. For example, it may be reasonable to satisfy the conditions by providing a URI or hyperlink to a resource that includes the required information.

          3. If requested by the Licensor, You must remove any of the information required by Section 3(a)(1)(A) to the extent reasonably practicable.

          4. If You Share Adapted Material You produce, the Adapter's License You apply must not prevent recipients of the Adapted Material from complying with this Public License.

Section 4 – Sui Generis Database Rights.

Where the Licensed Rights include Sui Generis Database Rights that apply to Your use of the Licensed Material:

     a.	for the avoidance of doubt, Section 2(a)(1) grants You the right to extract, reuse, reproduce, and Share all or a substantial portion of the contents of the database;

     b.	if You include all or a substantial portion of the database contents in a database in which You have Sui Generis Database Rights, then the database in which You have Sui Generis Database Rights (but not its individual contents) is Adapted Material; and

     c.	You must comply with the conditions in Section 3(a) if You Share all or a substantial portion of the contents of the database.
For the avoidance of doubt, this Section 4 supplements and does not replace Your obligations under this Public License where the Licensed Rights include other Copyright and Similar Rights.

Section 5 – Disclaimer of Warranties and Limitation of Liability.

     a.	Unless otherwise separately undertaken by the Licensor, to the extent possible, the Licensor offers the Licensed Material as-is and as-available, and makes no representations or warranties of any kind concerning the Licensed Material, whether express, implied, statutory, or other. This includes, without limitation, warranties of title, merchantability, fitness for a particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence or absence of errors, whether or not known or discoverable. Where disclaimers of warranties are not allowed in full or in part, this disclaimer may not apply to You.

     b.	To the extent possible, in no event will the Licensor be liable to You on any legal theory (including, without limitation, negligence) or otherwise for any direct, special, indirect, incidental, consequential, punitive, exemplary, or other losses, costs, expenses, or damages arising out of this Public License or use of the Licensed Material, even if the Licensor has been advised of the possibility of such losses, costs, expenses, or damages. Where a limitation of liability is not allowed in full or in part, this limitation may not apply to You.

     c.	The disclaimer of warranties and limitation of liability provided above shall be interpreted in a manner that, to the extent possible, most closely approximates an absolute disclaimer and waiver of all liability.

Section 6 – Term and Termination.

     a.	This Public License applies for the term of the Copyright and Similar Rights licensed here. However, if You fail to comply with this Public License, then Your rights under this Public License terminate automatically.

     b.	Where Your right to use the Licensed Material has terminated under Section 6(a), it reinstates:

          1. automatically as of the date the violation is cured, provided it is cured within 30 days of Your discovery of the violation; or

          2. upon express reinstatement by the Licensor.

     c.	For the avoidance of doubt, this Section 6(b) does not affect any right the Licensor may have to seek remedies for Your violations of this Public License.

     d.	For the avoidance of doubt, the Licensor may also offer the Licensed Material under separate terms or conditions or stop distributing the Licensed Material at any time; however, doing so will not terminate this Public License.

     e.	Sections 1, 5, 6, 7, and 8 survive termination of this Public License.

Section 7 – Other Terms and Conditions.

     a.	The Licensor shall not be bound by any additional or different terms or conditions communicated by You unless expressly agreed.

     b.	Any arrangements, understandings, or agreements regarding the Licensed Material not stated herein are separate from and independent of the terms and conditions of this Public License.

Section 8 – Interpretation.

     a.	For the avoidance of doubt, this Public License does not, and shall not be interpreted to, reduce, limit, restrict, or impose conditions on any use of the Licensed Material that could lawfully be made without permission under this Public License.

     b.	To the extent possible, if any provision of this Public License is deemed unenforceable, it shall be automatically reformed to the minimum extent necessary to make it enforceable. If the provision cannot be reformed, it shall be severed from this Public License without affecting the enforceability of the remaining terms and conditions.

     c.	No term or condition of this Public License will be waived and no failure to comply consented to unless expressly agreed to by the Licensor.

     d.	Nothing in this Public License constitutes or may be interpreted as a limitation upon, or waiver of, any privileges and immunities that apply to the Licensor or You, including from the legal processes of any jurisdiction or authority.

Creative Commons is not a party to its public licenses. Notwithstanding, Creative Commons may elect to apply one of its public licenses to material it publishes and in those instances will be considered the “Licensor.” Except for the limited purpose of indicating that material is shared under a Creative Commons public license or as otherwise permitted by the Creative Commons policies published at creativecommons.org/policies, Creative Commons does not authorize the use of the trademark “Creative Commons” or any other trademark or logo of Creative Commons without its prior written consent including, without limitation, in connection with any unauthorized modifications to any of its public licenses or any other arrangements, understandings, or agreements concerning use of licensed material. For the avoidance of doubt, this paragraph does not form part of the public licenses.

Creative Commons may be contacted at creativecommons.org.
~~~

[Return to file index](#file-index)

## LICENSE-MIT.txt {#source-license-mit-txt}

Contains the full MIT License and copyright notice for the software and project configuration files.

~~~text
MIT License

Copyright (c) 2026 R. Fisher

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
~~~

[Return to file index](#file-index)

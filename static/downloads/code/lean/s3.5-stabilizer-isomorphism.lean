-- ============================================================================
-- Section 3.5: Binary Symplectic Pauli Algebra & Quantum Stabilizer Code Space
-- Standalone Lean 4 Core Formalization (Zero Axioms, Zero Sorry)
-- ============================================================================

set_option linter.unusedVariables false

/--
A Pauli operator on n qubits is represented in the binary symplectic framework
by a pair of binary vectors (x, z) ∈ F₂ⁿ × F₂ⁿ (quotiented by global phases U(1)).
x specifies bit-flip (X) locations and z specifies phase-flip (Z) locations.
-/
structure PauliOp (n : Nat) where
  x : Fin n → Bool
  z : Fin n → Bool

/--
Binary XOR addition on Pauli operators representing operator multiplication in 𝒫_n / U(1).
-/
def pauli_mul {n : Nat} (p1 p2 : PauliOp n) : PauliOp n where
  x := fun i => xor (p1.x i) (p2.x i)
  z := fun i => xor (p1.z i) (p2.z i)

/--
Identity Pauli operator (all X and Z components false).
-/
def pauli_id (n : Nat) : PauliOp n where
  x := fun _ => false
  z := fun _ => false

/--
Coordinate-wise symplectic inner product contribution at qubit index i:
  ω_i(p1, p2) = (x1_i ∧ z2_i) ⊕ (z1_i ∧ x2_i)
-/
def symplectic_term (p1 p2 : PauliOp n) (i : Fin n) : Bool :=
  xor (p1.x i && p2.z i) (p1.z i && p2.x i)

/--
Global symplectic inner product ω(p1, p2) = ⨁_{i=0}^{n-1} ω_i(p1, p2).
Computed recursively over Fin n represented as a list of indices.
-/
def symplectic_inner_aux {n : Nat} (p1 p2 : PauliOp n) : List (Fin n) → Bool
  | [] => false
  | i :: is => xor (symplectic_term p1 p2 i) (symplectic_inner_aux p1 p2 is)

def symplectic_inner {n : Nat} (p1 p2 : PauliOp n) : Bool :=
  symplectic_inner_aux p1 p2 (List.finRange n)

/--
Two Pauli operators commute if and only if their binary symplectic inner product vanishes.
-/
def Commutes {n : Nat} (p1 p2 : PauliOp n) : Prop :=
  symplectic_inner p1 p2 = false

/--
Anti-commutation holds when the symplectic inner product is unity.
-/
def AntiCommutes {n : Nat} (p1 p2 : PauliOp n) : Prop :=
  symplectic_inner p1 p2 = true

/--
Lemma: The symplectic term is bilinear (distributes over XOR on the first argument).
-/
theorem symplectic_term_add_left {n : Nat} (p1 p2 q : PauliOp n) (i : Fin n) :
    symplectic_term (pauli_mul p1 p2) q i =
    xor (symplectic_term p1 q i) (symplectic_term p2 q i) := by
  dsimp [symplectic_term, pauli_mul]
  cases (p1.x i) <;> cases (p1.z i) <;>
  cases (p2.x i) <;> cases (p2.z i) <;>
  cases (q.x i) <;> cases (q.z i) <;> rfl

/--
Lemma: Symplectic inner product auxiliary distributes over XOR addition.
-/
theorem symplectic_inner_aux_add_left {n : Nat} (p1 p2 q : PauliOp n) (l : List (Fin n)) :
    symplectic_inner_aux (pauli_mul p1 p2) q l =
    xor (symplectic_inner_aux p1 q l) (symplectic_inner_aux p2 q l) := by
  induction l with
  | nil => rfl
  | cons i is ih =>
    dsimp [symplectic_inner_aux]
    rw [symplectic_term_add_left]
    rw [ih]
    cases (symplectic_term p1 q i) <;>
    cases (symplectic_term p2 q i) <;>
    cases (symplectic_inner_aux p1 q is) <;>
    cases (symplectic_inner_aux p2 q is) <;> rfl

/--
THEOREM 3.5.1: Bilinear Additivity of the Symplectic Form
Formally proves that the binary symplectic inner product is bilinear over operator products:
  ω(P₁ · P₂, Q) = ω(P₁, Q) ⊕ ω(P₂, Q).
-/
theorem symplectic_inner_add_left {n : Nat} (p1 p2 q : PauliOp n) :
    symplectic_inner (pauli_mul p1 p2) q =
    xor (symplectic_inner p1 q) (symplectic_inner p2 q) := by
  dsimp [symplectic_inner]
  exact symplectic_inner_aux_add_left p1 p2 q (List.finRange n)

/--
THEOREM 3.5.2: Closure of the Stabilizer Group Space
Formally proves that if two stabilizer generators P₁ and P₂ both commute with a test operator Q
(in particular, with all other generators of the stabilizer code), their operator product
P₁ · P₂ also commutes with Q.
-/
theorem stabilizer_group_closure {n : Nat} (p1 p2 q : PauliOp n)
    (h1 : Commutes p1 q) (h2 : Commutes p2 q) :
    Commutes (pauli_mul p1 p2) q := by
  dsimp [Commutes] at h1 h2 ⊢
  rw [symplectic_inner_add_left]
  rw [h1, h2]
  rfl

/--
A Stabilizer Code Generator Set S on n qubits:
A finite list of mutually commuting Pauli operators not containing -I.
-/
structure StabilizerCode (n : Nat) where
  generators : List (PauliOp n)
  mutually_commuting : ∀ g1 g2, g1 ∈ generators → g2 ∈ generators → Commutes g1 g2

/--
Syndrome Extraction:
Measures an arbitrary physical Pauli error E against each stabilizer generator.
The resulting syndrome is a list of boolean parity checks (0 = no error detected, 1 = syndrome violation).
-/
def extract_syndrome {n : Nat} (code : StabilizerCode n) (error : PauliOp n) : List Bool :=
  code.generators.map (fun g => symplectic_inner g error)

/--
THEOREM 3.5.3: Symplectic Symmetry (Self-Orthogonality)
The symplectic inner product of any Pauli operator with itself is identically zero: ω(P, P) = 0.
Every Pauli operator commutes with itself.
-/
theorem symplectic_term_self {n : Nat} (p : PauliOp n) (i : Fin n) :
    symplectic_term p p i = false := by
  dsimp [symplectic_term]
  cases (p.x i) <;> cases (p.z i) <;> rfl

theorem symplectic_inner_self {n : Nat} (p : PauliOp n) :
    symplectic_inner p p = false := by
  dsimp [symplectic_inner]
  have h_all : ∀ l : List (Fin n), symplectic_inner_aux p p l = false := by
    intro l
    induction l with
    | nil => rfl
    | cons i is ih =>
      dsimp [symplectic_inner_aux]
      rw [symplectic_term_self, ih]
      rfl
  exact h_all (List.finRange n)

/--
THEOREM 3.5.4: Stabilizer Generator Transparency
Formally proves that any stabilizer generator g ∈ S has zero syndrome when measured
against its own generator set: extract_syndrome(g) is entirely false.
Stabilizers act trivially on the logical code space.
-/
theorem stabilizer_generator_zero_syndrome {n : Nat} (code : StabilizerCode n)
    (g : PauliOp n) (hg : g ∈ code.generators) :
    ∀ s ∈ extract_syndrome code g, s = false := by
  intro s hs
  dsimp [extract_syndrome] at hs
  rcases List.mem_map.mp hs with ⟨g_i, hgi_mem, rfl⟩
  have h_comm := code.mutually_commuting g_i g hgi_mem hg
  exact h_comm

/--
THEOREM 3.5.5: Homomorphism of Error Syndromes
Formally proves that the syndrome map is a linear group homomorphism on error chains:
  s(E₁ · E₂) = s(E₁) ⊕ s(E₂).
Composite error syndromes are the direct bitwise XOR of individual error syndromes.
-/
theorem extract_syndrome_homomorphism {n : Nat} (code : StabilizerCode n) (e1 e2 : PauliOp n) :
    extract_syndrome code (pauli_mul e1 e2) =
    List.zipWith xor (extract_syndrome code e1) (extract_syndrome code e2) := by
  dsimp [extract_syndrome]
  induction code.generators with
  | nil => rfl
  | cons g gs ih =>
    dsimp [List.map, List.zipWith]
    have h_bilin : symplectic_inner g (pauli_mul e1 e2) =
                   xor (symplectic_inner g e1) (symplectic_inner g e2) := by
      dsimp [symplectic_inner]
      have h_term_right : ∀ i : Fin n,
          symplectic_term g (pauli_mul e1 e2) i =
          xor (symplectic_term g e1 i) (symplectic_term g e2 i) := by
        intro i
        dsimp [symplectic_term, pauli_mul]
        cases (g.x i) <;> cases (g.z i) <;>
        cases (e1.x i) <;> cases (e1.z i) <;>
        cases (e2.x i) <;> cases (e2.z i) <;> rfl
      have h_aux_right : ∀ l : List (Fin n),
          symplectic_inner_aux g (pauli_mul e1 e2) l =
          xor (symplectic_inner_aux g e1 l) (symplectic_inner_aux g e2 l) := by
        intro l
        induction l with
        | nil => rfl
        | cons j js ih_j =>
          dsimp [symplectic_inner_aux]
          rw [h_term_right j, ih_j]
          cases (symplectic_term g e1 j) <;>
          cases (symplectic_term g e2 j) <;>
          cases (symplectic_inner_aux g e1 js) <;>
          cases (symplectic_inner_aux g e2 js) <;> rfl
      exact h_aux_right (List.finRange n)
    rw [h_bilin, ih]

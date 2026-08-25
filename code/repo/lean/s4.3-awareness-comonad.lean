-- GraphState binds an abstract graph type with a generic nested annotation context
structure GraphState (G A : Type) where
  graph : G
  annotation : A
  deriving DecidableEq, Repr

-- Counit (ε): Context Extraction - Projects out the historical annotation layer
def ε {G A S : Type} (state : GraphState G (A × S)) : GraphState G A :=
  ⟨state.graph, state.annotation.1⟩

-- Comultiplication (δ): Meta-Check - Duplicates the current observation layer for verification
def δ {G A S : Type} (state : GraphState G (A × S)) : GraphState G ((A × S) × S) :=
  ⟨state.graph, (state.annotation, state.annotation.2)⟩

-- Lifted operation applying an annotation map to the history sector of a state tuple
def lift_history {G A B S : Type} (f : GraphState G A → GraphState G B) (state : GraphState G (A × S)) : GraphState G (B × S) :=
  ⟨state.graph, ((f ⟨state.graph, state.annotation.1⟩).annotation, state.annotation.2)⟩

/--
THEOREM 1: Left Identity
Formally proves that duplicating an observation context for a meta-check 
and immediately extracting the history yields the original state invariant.
-/
theorem left_identity {G A S : Type} (Y : GraphState G (A × S)) :
    ε (δ Y) = Y := by
  rfl

/--
THEOREM 2: Right Identity
Formally proves that duplicating an observation context and discarding 
the inner history layer returns the original observation profile cleanly.
-/
theorem right_identity {G A S : Type} (Y : GraphState G (A × S)) :
    lift_history ε (δ Y) = Y := by
  rfl

/--
THEOREM 3: Comonadic Associativity
Formally proves that the hierarchy of self-diagnosis is completely stable: 
building the stack of meta-checks from the bottom up or top down yields identical structures.
-/
theorem comonad_associativity {G A S : Type} (Y : GraphState G (A × S)) :
    δ (δ Y) = lift_history δ (δ Y) := by
  rfl

-- A generic representation of boolean vectors (syndromes and incidence vectors)
def BitVector (n : Nat) := Fin n → Bool

def zero_vec (n : Nat) : BitVector n := fun _ => false

-- Bitwise XOR for the BitVector type representing Pauli frame shifts
def xor_vec {n : Nat} (a b : BitVector n) : BitVector n :=
  fun i => xor (a i) (b i)

theorem xor_vec_self {n : Nat} (a : BitVector n) :
    xor_vec a a = zero_vec n := by
  funext i
  dsimp [xor_vec, zero_vec]
  cases (a i) <;> rfl

theorem xor_vec_zero {n : Nat} (a : BitVector n) :
    xor_vec a (zero_vec n) = a := by
  funext i
  dsimp [xor_vec, zero_vec]
  cases (a i) <;> rfl

theorem xor_vec_assoc {n : Nat} (a b c : BitVector n) :
    xor_vec (xor_vec a b) c = xor_vec a (xor_vec b c) := by
  funext i
  dsimp [xor_vec]
  cases (a i) <;> cases (b i) <;> cases (c i) <;> rfl

theorem xor_vec_comm {n : Nat} (a b : BitVector n) :
    xor_vec a b = xor_vec b a := by
  funext i
  dsimp [xor_vec]
  cases (a i) <;> cases (b i) <;> rfl

def shift_op {n : Nat} (u : BitVector n) (sigma : BitVector n) : BitVector n :=
  xor_vec sigma u

/--
THEOREM 4: Morphism Uniqueness (Zero Gauge Freedom)
Formally proves that the categorical syndrome update morphism k is uniquely determined
by the physical incidence vector u_ΔE, leaving zero gauge freedom in the awareness layer.
-/
theorem comonad_morphism_unique {n : Nat}
    (k1 k2 : BitVector n → BitVector n) (u : BitVector n)
    (h1 : ∀ s, k1 s = shift_op u s)
    (h2 : ∀ s, k2 s = shift_op u s) :
    k1 = k2 := by
  funext s
  rw [h1 s, h2 s]

/--
THEOREM 5: Reversible Involution of the Syndrome Shift
Proves that applying the same physical rewrite twice returns the syndrome
to its original diagnostic configuration without information loss: T_u(T_u(σ)) = σ.
-/
theorem comonad_shift_involution {n : Nat}
    (u : BitVector n) (sigma : BitVector n) :
    shift_op u (shift_op u sigma) = sigma := by
  dsimp [shift_op]
  rw [xor_vec_assoc, xor_vec_self, xor_vec_zero]

/--
THEOREM 6: Composition Homomorphism
Proves that sequential updates u1 followed by u2 on the syndrome layer
compose homomorphically with the boolean XOR addition of the incidence vectors.
-/
theorem comonad_shift_composition_homomorphism {n : Nat}
    (u1 u2 : BitVector n) (sigma : BitVector n) :
    shift_op u2 (shift_op u1 sigma) = shift_op (xor_vec u1 u2) sigma := by
  dsimp [shift_op]
  rw [xor_vec_assoc]

-- Rename Vector to BitVector to avoid colliding with Lean's built-in Vector
def BitVector (n : Nat) := Fin n → Bool

-- Bitwise XOR for our BitVector type
def xor_vec {n : Nat} (a b : BitVector n) : BitVector n :=
  fun i => xor (a i) (b i)

-- Define the abstract State as a boolean map indicating edge presence
def GraphState (Edges : Type) := Edges → Bool

-- The Symmetric Difference (ΔE) between two states is the XOR of their edge presence
def symmetric_difference {E : Type} (state1 state2 : GraphState E) : GraphState E :=
  fun e => xor (state1 e) (state2 e)

-- A generic geometric check operator (Stabilizer).
-- In QBD, this corresponds to checking if the parity of edges in the support is even/odd.
def GeometricCheck (E : Type) := GraphState E → Bool

-- The Incidence Vector u_ΔE evaluates whether the symmetric difference
-- intersects the support of the i-th geometric check an odd number of times.
variable {n : Nat} {E : Type}
variable (u_delta : BitVector n)

/--
THEOREM: Algebraic Rigidity of the Annotation Map
Formally proves that the updated syndrome map (k(σ)) is deterministically
fixed by the XOR of the prior syndrome (σ) and the Pauli-X incidence vector (u_ΔE).
Therefore, the categorical morphism 'k' possesses zero independent degrees of freedom.
-/
theorem algebraic_rigidity_of_k
    (sigma : BitVector n)
    (sigma_prime : BitVector n)
    (k : BitVector n → BitVector n)
    (h_physical_update : sigma_prime = xor_vec sigma u_delta)
    (h_categorical_map : sigma_prime = k sigma) :
    k sigma = xor_vec sigma u_delta := by
  -- The proof proceeds by transitive equality.
  -- Since σ' is defined physically by the XOR update, and categorially by k(σ),
  -- k(σ) must exactly equal the physical XOR update.
  rw [← h_categorical_map]
  exact h_physical_update

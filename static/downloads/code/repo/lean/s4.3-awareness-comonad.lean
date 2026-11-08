namespace QBD.Awareness

-- Fixed directed adjacency coordinates and global diagnostic fields.
abbrev Graph (V : Type) := (V × V) → Bool
abbrev Field (V : Type) := (V × V × V) → Fin 3 → Bool

-- Pointwise addition in the binary diagnostic field.
def add {V : Type} (a b : Field V) : Field V :=
  fun p i => xor (a p i) (b p i)

-- Pair-product check bits at every ordered triple, including inactive sites.
def observe {V : Type} (E : Graph V) : Field V :=
  fun p i => match i.val with
    | 0 => xor (E (p.1, p.2.1)) (E (p.2.1, p.2.2))
    | 1 => xor (E (p.2.1, p.2.2)) (E (p.2.2, p.1))
    | _ => xor (E (p.2.2, p.1)) (E (p.1, p.2.1))

-- The edge symmetric difference connecting two graph snapshots.
def edgeDifference {V : Type} (E F : Graph V) : Graph V :=
  fun e => xor (E e) (F e)

/-- The local incidence displacement equals the difference of observations. -/
theorem observation_difference {V : Type} (E F : Graph V) :
    observe (edgeDifference E F) = add (observe E) (observe F) := by
  funext p i
  rcases p with ⟨v, w, u⟩
  rcases i with ⟨i, hi⟩
  match i with
  | 0 => dsimp [observe, edgeDifference, add]; cases E (v,w) <;> cases E (w,u) <;> cases F (v,w) <;> cases F (w,u) <;> rfl
  | 1 => dsimp [observe, edgeDifference, add]; cases E (w,u) <;> cases E (u,v) <;> cases F (w,u) <;> cases F (u,v) <;> rfl
  | 2 => dsimp [observe, edgeDifference, add]; cases E (u,v) <;> cases E (v,w) <;> cases F (u,v) <;> cases F (v,w) <;> rfl
  | n+3 => omega

-- A graph transition transports every diagnostic field by its incidence shift.
def transport {V : Type} (E F : Graph V) (b : Field V) : Field V :=
  add b (add (observe E) (observe F))

/-- Identity graph transport fixes all field values. -/
theorem transport_identity {V : Type} (E : Graph V) (b : Field V) :
    transport E E b = b := by
  funext p i
  dsimp [transport, add]
  cases b p i <;> cases observe E p i <;> rfl

/-- Consecutive transports equal the endpoint transport. -/
theorem transport_composition {V : Type} (E F G : Graph V) (b : Field V) :
    transport F G (transport E F b) = transport E G b := by
  funext p i
  dsimp [transport, add]
  cases b p i <;> cases observe E p i <;> cases observe F p i <;> cases observe G p i <;> rfl

/-- Transport takes a faithful observation to the new faithful observation. -/
theorem transport_observation {V : Type} (E F : Graph V) :
    transport E F (observe E) = observe F := by
  funext p i
  dsimp [transport, add]
  cases observe E p i <;> cases observe F p i <;> rfl

-- Fiber maps on product annotations over the fixed vertex universe.
def lift {V A B : Type} (E F : Graph V) (k : A → B)
    (x : A × Field V) : B × Field V :=
  (k x.1, transport E F x.2)

-- Counit projection and comultiplication duplication.
def extract {A S : Type} (x : A × S) : A := x.1
def duplicate {A S : Type} (x : A × S) : (A × S) × S := (x, x.2)

/-- Identity annotation maps lift to identity product maps. -/
theorem lift_identity {V A : Type} (E : Graph V) (x : A × Field V) :
    lift E E id x = x := by
  rcases x with ⟨a,b⟩
  simp only [lift, id_eq, transport_identity]

/-- The graph-changing product lift preserves composition. -/
theorem lift_composition {V A B C : Type} (E F G : Graph V)
    (k : A → B) (l : B → C) (x : A × Field V) :
    lift F G l (lift E F k x) = lift E G (l ∘ k) x := by
  rcases x with ⟨a,b⟩
  simp only [lift, Function.comp_apply, transport_composition]

/-- Counit naturality includes changing graph snapshots. -/
theorem extract_natural {V A B : Type} (E F : Graph V)
    (k : A → B) (x : A × Field V) :
    extract (lift E F k x) = k (extract x) := by rfl

/-- Comultiplication naturality transports both copied context fields. -/
theorem duplicate_natural {V A B : Type} (E F : Graph V)
    (k : A → B) (x : A × Field V) :
    duplicate (lift E F k x) =
      lift E F (lift E F k) (duplicate x) := by rfl

/-- First counit law. -/
theorem counit_left {A S : Type} (x : A × S) : extract (duplicate x) = x := by rfl

/-- Second counit law, using identity base transport. -/
theorem counit_right {V A : Type} (E : Graph V) (x : A × Field V) :
    lift E E extract (duplicate x) = x := by
  rcases x with ⟨a,b⟩
  simp only [lift, extract, duplicate, transport_identity]

/-- Coassociativity duplicates the same observation field twice. -/
theorem coassociative {V A : Type} (E : Graph V) (x : A × Field V) :
    duplicate (duplicate x) = lift E E duplicate (duplicate x) := by
  rcases x with ⟨a,b⟩
  simp only [lift, duplicate, transport_identity]

end QBD.Awareness

#print axioms QBD.Awareness.observation_difference
#print axioms QBD.Awareness.lift_composition
#print axioms QBD.Awareness.duplicate_natural
#print axioms QBD.Awareness.coassociative

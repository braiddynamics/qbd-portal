structure TimestampedGraph (V : Type) [DecidableEq V] where
  E : V × V → Bool
  H : V × V → Nat

def T_add {V : Type} [DecidableEq V] (e : V × V) (h_rec : Nat) (G : TimestampedGraph V) :
    TimestampedGraph V :=
  { E := fun x => if x = e then true else G.E x
    H := fun x => if x = e then h_rec else G.H x }

def T_del {V : Type} [DecidableEq V] (e : V × V) (G : TimestampedGraph V) :
    TimestampedGraph V × Nat :=
  ( { E := fun x => if x = e then false else G.E x
      H := fun x => if x = e then 0 else G.H x },
    G.H e )

theorem del_then_recorded_add_pointwise {V : Type} [DecidableEq V]
    (G : TimestampedGraph V) (e x : V × V) (h_act : G.E e = true) :
    (T_add e (T_del e G).2 (T_del e G).1).E x = G.E x ∧
    (T_add e (T_del e G).2 (T_del e G).1).H x = G.H x := by
  dsimp [T_add, T_del]
  by_cases hx : x = e
  · subst hx
    constructor
    · rw [ite_eq_left rfl]
      exact h_act.symm
    · rw [ite_eq_left rfl]
  · constructor
    · rw [ite_eq_right hx, ite_eq_right hx]
    · rw [ite_eq_right hx, ite_eq_right hx]

theorem add_then_del_pointwise {V : Type} [DecidableEq V]
    (G : TimestampedGraph V) (e x : V × V) (h_rec : Nat)
    (h_abs : G.E e = false) (h_zero : G.H e = 0) :
    (T_del e (T_add e h_rec G)).1.E x = G.E x ∧
    (T_del e (T_add e h_rec G)).1.H x = G.H x := by
  dsimp [T_add, T_del]
  by_cases hx : x = e
  · subst hx
    constructor
    · rw [ite_eq_left rfl]
      exact h_abs.symm
    · rw [ite_eq_left rfl]
      exact h_zero.symm
  · constructor
    · rw [ite_eq_right hx, ite_eq_right hx]
    · rw [ite_eq_right hx, ite_eq_right hx]

#print axioms del_then_recorded_add_pointwise
#print axioms add_then_del_pointwise

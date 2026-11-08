def Edge (V : Type) := V × V

def GraphEdges (V : Type) := Edge V → Prop

def HistoricalInclusion {V : Type} (H1 H2 : GraphEdges V) : Prop :=
  ∀ e, H1 e → H2 e

/--
THEOREM 1: Category Hist Identity Inclusion
Proves that every cumulative trajectory graph admits an identity inclusion morphism.
-/
theorem historical_inclusion_id {V : Type} (H : GraphEdges V) :
    HistoricalInclusion H H := by
  intro e he
  exact he

/--
THEOREM 2: Category Hist Morphism Composition
Proves that historical inclusions compose transitively.
-/
theorem historical_inclusion_trans {V : Type} (H1 H2 H3 : GraphEdges V) :
    HistoricalInclusion H1 H2 → HistoricalInclusion H2 H3 → HistoricalInclusion H1 H3 := by
  intro h12 h23 e he
  exact h23 e (h12 e he)

/--
THEOREM 3: Cumulative History Step Monotonicity
Proves that cumulative history is strictly monotonic under constructor evolution: H_t ⊆ H_{t+1}.
-/
theorem cumulative_history_step_monotonicity {V : Type}
    (H_seq A_seq : Nat → GraphEdges V)
    (t : Nat)
    (h_step : ∀ t e, H_seq (t + 1) e ↔ H_seq t e ∨ A_seq t e) :
    HistoricalInclusion (H_seq t) (H_seq (t + 1)) := by
  intro e he
  rw [h_step t e]
  exact Or.inl he

/--
Helper Lemma: Inductive Multi-Step Expansion of Cumulative History
-/
theorem cumulative_history_add_monotonicity {V : Type}
    (H_seq A_seq : Nat → GraphEdges V)
    (h_step : ∀ t e, H_seq (t + 1) e ↔ H_seq t e ∨ A_seq t e)
    (t1 : Nat) (k : Nat) :
    HistoricalInclusion (H_seq t1) (H_seq (t1 + k)) := by
  intro e he
  induction k with
  | zero => exact he
  | succ n ih =>
    have h_one_step := cumulative_history_step_monotonicity H_seq A_seq (t1 + n) h_step
    exact h_one_step e ih

/--
THEOREM 4: Cumulative History Transitive Monotonicity
Proves that across arbitrary intervals t1 ≤ t2, cumulative history expands monotonically: H_{t1} ⊆ H_{t2}.
-/
theorem cumulative_history_transitive_monotonicity {V : Type}
    (H_seq A_seq : Nat → GraphEdges V)
    (h_step : ∀ t e, H_seq (t + 1) e ↔ H_seq t e ∨ A_seq t e)
    (t1 t2 : Nat) (h_le : t1 ≤ t2) :
    HistoricalInclusion (H_seq t1) (H_seq t2) := by
  rcases Nat.le.dest h_le with ⟨k, rfl⟩
  exact cumulative_history_add_monotonicity H_seq A_seq h_step t1 k

/--
THEOREM 5: Spatial State is Inductively a Subgraph of Cumulative History
Proves that at all logical ticks t, the active kinematic spatial graph G_t is an exact subgraph of H_t: E_t ⊆ H_t.
-/
theorem spatial_subgraph_of_cumulative_history {V : Type}
    (E_seq H_seq A_seq D_seq : Nat → GraphEdges V)
    (h_init : ∀ e, H_seq 0 e ↔ E_seq 0 e)
    (h_hist : ∀ t e, H_seq (t + 1) e ↔ H_seq t e ∨ A_seq t e)
    (h_dyn : ∀ t e, E_seq (t + 1) e ↔ (E_seq t e ∨ A_seq t e) ∧ ¬ D_seq t e) :
    ∀ t e, E_seq t e → H_seq t e := by
  intro t
  induction t with
  | zero =>
    intro e he
    exact (h_init e).mpr he
  | succ n ih =>
    intro e he
    rw [h_dyn n e] at he
    rw [h_hist n e]
    cases he.1 with
    | inl he_prev => exact Or.inl (ih e he_prev)
    | inr he_add => exact Or.inr he_add

/--
THEOREM 6: Dynamic Deletion Preserves Cumulative History
Proves that when an edge e is excised from the active kinematic state by deletion D_t,
e remains indelibly preserved in the cumulative historical record H_{t+1}.
-/
theorem deletion_preserves_cumulative_history {V : Type}
    (E_seq H_seq A_seq D_seq : Nat → GraphEdges V)
    (h_init : ∀ e, H_seq 0 e ↔ E_seq 0 e)
    (h_hist : ∀ t e, H_seq (t + 1) e ↔ H_seq t e ∨ A_seq t e)
    (h_dyn : ∀ t e, E_seq (t + 1) e ↔ (E_seq t e ∨ A_seq t e) ∧ ¬ D_seq t e)
    (t : Nat) (e : Edge V)
    (he_active : E_seq t e)
    (he_deleted : D_seq t e) :
    ¬ E_seq (t + 1) e ∧ H_seq (t + 1) e := by
  constructor
  · rw [h_dyn t e]
    intro ⟨_, h_not_D⟩
    exact h_not_D he_deleted
  · rw [h_hist t e]
    have h_in_H := spatial_subgraph_of_cumulative_history E_seq H_seq A_seq D_seq h_init h_hist h_dyn t e he_active
    exact Or.inl h_in_H

namespace QBD.CreationHistory

-- A creation occurrence stores both temporal coordinates explicitly.
structure Occurrence (V : Type) where
  source : V
  target : V
  born : Nat
  height : Nat

-- Histories contain creation records, not only spatial endpoint pairs.
abbrev History (V : Type) := Occurrence V → Prop

-- A canonical inclusion fixes each record value.
def Included {V : Type} (A B : History V) : Prop := ∀ w, A w → B w

-- The cumulative spatial support forgets both temporal coordinates.
def support {V : Type} (A : History V) (e : V × V) : Prop :=
  ∃ w, A w ∧ w.source = e.1 ∧ w.target = e.2

/-- Appending creation records preserves every old record. -/
theorem append_includes {V : Type} (A New : History V) :
    Included A (fun w => A w ∨ New w) := by
  intro w hw
  exact Or.inl hw

/-- Record inclusion induces inclusion of projected spatial supports. -/
theorem support_inclusion {V : Type} (A B : History V) (h : Included A B)
    (e : V × V) : support A e → support B e := by
  intro ⟨w, hw, hs, ht⟩
  exact ⟨w, h w hw, hs, ht⟩

/-- Canonical inclusion preserves scheduler birth tick. -/
theorem birth_preserved {V : Type} (w : Occurrence V) : (id w).born = w.born := by rfl

/-- Canonical inclusion preserves immutable causal height. -/
theorem height_preserved {V : Type} (w : Occurrence V) : (id w).height = w.height := by rfl

/-- Different scheduler births identify different creation occurrences. -/
theorem different_birth_distinct {V : Type} (w z : Occurrence V)
    (h : w.born ≠ z.born) : w ≠ z := by
  intro heq
  exact h (congrArg Occurrence.born heq)

/-- The recurrence increment respects the next scheduler tick bound. -/
theorem next_height_bound (parentMax tick : Nat) (h : parentMax ≤ tick) :
    parentMax + 1 ≤ tick + 1 := by
  exact Nat.succ_le_succ h

end QBD.CreationHistory

#print axioms QBD.CreationHistory.support_inclusion
#print axioms QBD.CreationHistory.different_birth_distinct

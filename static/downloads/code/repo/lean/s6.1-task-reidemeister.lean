-- §6.1.3 Task–Reidemeister realization (standalone Lean 4 core)
-- Mirrors the type-theoretic validation block in docs/02-players/06-fermions/6.1.md

-- Local vertex labels for pattern fragments
inductive V where
  | a | b | c
  deriving DecidableEq, Repr

-- Directed edge as an ordered pair
abbrev Edge := V × V

-- Finite graph fragment
abbrev Graph := List Edge

-- Edge membership in a fragment
def hasEdge : Graph → Edge → Bool
  | [], _ => false
  | h :: t, e => decide (h = e) || hasEdge t e

-- Local complexity = edge count
def complexity (G : Graph) : Nat := G.length

-- Delete the first matching directed edge
def applyDel : Graph → Edge → Graph
  | [], _ => []
  | h :: t, e => if h = e then t else h :: applyDel t e

-- Legal deletion: the edge is present
structure LegalDel (G : Graph) (e : Edge) : Prop where
  mem : hasEdge G e = true

-- Legal addition: irreflexive and absent (PUC freshness abstraction)
structure LegalAdd (G : Graph) (e : Edge) : Prop where
  not_loop : e.1 ≠ e.2
  fresh : hasEdge G e = false

-- Dependent elementary task space 𝔗(G)
inductive AllowedTask (G : Graph) where
  | del (e : Edge) (h : LegalDel G e)
  | add (e : Edge) (h : LegalAdd G e)

-- Reidemeister letters realized by the kinematic layer
inductive ReidLetter where
  | typeI_restorative
  | typeII_reducing
  | typeIII_slide

-- Task kind assigned by the realization map Φ
inductive TaskKind where
  | del
  | add
  | add_then_del

-- Realization map Φ on Reidemeister letters
def phi : ReidLetter → TaskKind
  | .typeI_restorative => .del
  | .typeII_reducing => .del
  | .typeIII_slide => .add_then_del

/-- Type I restorative patterns realize as deletion tasks. -/
theorem phi_typeI : phi .typeI_restorative = .del := rfl

/-- Type II reducing patterns realize as deletion tasks (one-sided). -/
theorem phi_typeII : phi .typeII_reducing = .del := rfl

/-- Type III slides realize as the composite add-then-delete word. -/
theorem phi_typeIII : phi .typeIII_slide = .add_then_del := rfl

/-- Deleting a present edge strictly decreases complexity. -/
theorem del_decreases_complexity
    (G : Graph) (e : Edge) (h : hasEdge G e = true) :
    complexity (applyDel G e) < complexity G := by
  induction G with
  | nil =>
      cases h
  | cons hd tl ih =>
      dsimp [applyDel, complexity, hasEdge] at h ⊢
      by_cases heq : hd = e
      · -- Head matches: result length is tl.length < tl.length + 1
        simpa [heq] using (Nat.lt_succ_self tl.length)
      · -- Head differs: membership forces the tail; cons adds one to both sides
        have hdec : decide (hd = e) = false := by simp [heq]
        have htl : hasEdge tl e = true := by
          rw [hdec, Bool.false_or] at h
          exact h
        have ih' : (applyDel tl e).length < tl.length := by
          simpa [complexity] using ih htl
        simpa [heq] using Nat.succ_lt_succ ih'

/-- A witnessed edge supplies LegalDel. -/
theorem legal_del_of_mem (G : Graph) (e : Edge)
    (h : hasEdge G e = true) : LegalDel G e :=
  ⟨h⟩

/-- Self-loops fail LegalAdd. -/
theorem legal_add_rejects_loop (G : Graph) (u : V)
    (h : LegalAdd G (u, u)) : False :=
  h.not_loop rfl

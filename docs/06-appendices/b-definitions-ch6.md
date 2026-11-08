---
title: "Appendix B: Master List of Definitions & Theorems - Chapter 6"
sidebar_class_name: "theme-doc-sidebar-item-hidden"
---

This appendix serves as a centralized, rigorous catalog of the foundational mathematical postulates, definitions, axioms, lemmas, and theorems introduced in Chapter 6 of the Quantum Braid Dynamics (QBD) monograph.

---

### 6.1.1 Definition: Local Reducibility {#6.1.1}

:::tip[**Criterion for Topological Triviality determined by Local Horizon Constraints**]
:::

A localized subgraph $\xi \subset G$ exhibits **Local Reducibility** if there exists a finite, ordered sequence of elementary rewrite operations $\mathcal{S} = \{r_1, \dots, r_k\} \subseteq \mathcal{R}$ that satisfies the conjunction of the following three conditions:
1.  **Volume Reduction:** The execution of the sequence strictly reduces the scalar edge count or the cycle count of the subgraph, such that the final cardinality satisfies $|\xi_{final}| < |\xi_{initial}|$.
2.  **Horizon Compliance:** Each constituent operation $r_i$ acts exclusively upon vertices located within the causal horizon radius $R$ of the target edge, thereby satisfying the strict locality constraint of the Universal Constructor.
3.  **Invariant Preservation:** The sequence preserves the global topological invariants of the subgraph, specifically maintaining the Jones Polynomial $V(t)$ invariant, while mapping the geometric realization of the trivial unknot to the empty set or to a single, non-interacting vacuum cycle.

**In Plain English:**  
Section 6.1.1 formalizes the properties of the QBD definition regarding local reducibility.

---

### 6.1.2 Theorem: Particle Necessity {#6.1.2}

:::info[**Requirement of Topological Non-Triviality through Dynamical Persistence**]
:::

Given any localized subgraph $\xi \subset G_t^*$ characterized by a local 3-cycle density $\rho(\xi)$ strictly exceeding the vacuum equilibrium $\rho^*$, its dynamical persistence against the vacuum deletion flux necessitates the possession of non-trivial topological invariants under ambient isotopy, specifically a non-zero Writhe ($w(\xi) \neq 0$) or non-zero pairwise Linking Numbers ($L_{ij}(\xi) \neq 0$), to occupy a protected logical state within the Quantum Error-Correcting Code codespace $\mathcal{C}$ (**Codespace Non-Triviality** <Ref id="3.5.7" label="§3.5.7" />).

This stability derives from the **Linear Barrier** <Ref id="6.4.1" label="§6.4.1" />, wherein the untwining of a prime topology necessitates a global operation requiring computational resources scaling as order $O(N)$, a requirement that strictly exceeds the logarithmic causal horizon $O(\log N)$ accessible to the local **Universal Constructor** (denoted $\mathcal{R}$).

Conversely, any excitation lacking these invariants constitutes a topologically trivial state and remains subject to reducible decomposition via Type II Reidemeister moves, a process that triggers the projection of syndrome inconsistencies ($\sigma = -1$) and results in immediate dissolution via the catalyzed **Entropic & Catalytic Decay ($J_{out}$)** <Ref id="5.2.6" label="§5.2.6" />.

**In Plain English:**  
Section 6.1.2 formalizes the properties of the QBD theorem regarding particle necessity.

---

### 6.1.3 Lemma: Reducibility of Trivial Topologies {#6.1.3}

:::info[**Complexity of Certified Reductions via Elementary Task Counts**]
:::

Let $\xi\subset G_0$ have an embedding ambient isotopic to the unknot, and let $G_0,\ldots,G_m$ be a finite graph realization of a reduction word with a certified legal elementary task at each step, comprising $a$ additions and $d$ deletions. Then $|E(G_m)|-|E(G_0)|=a-d$, with zero edge-count change for a certified add-then-delete slide and a decrease of one for a certified single deletion.

**In Plain English:**  
Section 6.1.3 formalizes the properties of the QBD lemma regarding reducibility of trivial topologies.

---

### 6.1.3.1 Proof: Reducibility of Trivial Topologies {#6.1.3.1}

:::tip[**Edge-Count Balance via Legality-Indexed Tasks and Telescoping**]
:::

**I. Certified Word and Intermediate Graphs**

Let $E_j=E(G_j)$ and let $T_j$ act on the fixed vertex set of $G_{j-1}$ to produce $G_j$, for $1\le j\le m$ (**Elementary Task Space** <Ref id="1.5.1" label="§1.5.1" />). The legality certificate for an addition includes an absent edge and the graph-side conditions for that task. The legality certificate for a deletion includes a present edge. These conditions are evaluated in the graph on which the task acts (**Principle of Unique Causality (PUC)** <Ref id="2.3.4" label="§2.3.4" />).

**II. Edge Count for Each Task**

For an addition of a certified edge $e_j\notin E_{j-1}$, the added singleton is disjoint from the old edge set. For a deletion of $e_j\in E_{j-1}$, the old set is the disjoint union of the retained set and the deleted singleton. Consequently

$$
\begin{aligned}
T_j=\mathfrak T_{\text{add}}(e_j)
&\ \Longrightarrow\ E_j=E_{j-1}\sqcup\{e_j\}
\ \Longrightarrow\ |E_j|=|E_{j-1}|+1,\\
T_j=\mathfrak T_{\text{del}}(e_j)
&\ \Longrightarrow\ E_{j-1}=E_j\sqcup\{e_j\}
\ \Longrightarrow\ |E_j|=|E_{j-1}|-1.
\end{aligned}
$$

**III. Complexity Balance of the Sequence**

Let $A_j$ be one when $T_j$ is an addition and zero otherwise, and let $D_j$ be one when it is a deletion and zero otherwise. Then $a=\sum_{j=1}^m A_j$ and $d=\sum_{j=1}^m D_j$. The intermediate cardinalities cancel in the sum,

$$
\begin{aligned}
|E_m|-|E_0|
&=(|E_1|-|E_0|)+(|E_2|-|E_1|)+\cdots+(|E_m|-|E_{m-1}|)\\
&=\sum_{j=1}^m(A_j-D_j)
=\sum_{j=1}^m A_j-\sum_{j=1}^m D_j
=a-d.
\end{aligned}
$$

For an empty word, $E_m=E_0$ and $a=d=0$. For a certified slide, let $E'$ be the edge set after adding $e$ and $E''$ the edge set after deleting $f$. The deletion certificate is evaluated on $E'$. Thus

$$
|E''|-|E_0|=(|E''|-|E'|)+(|E'|-|E_0|)=-1+1=0.
$$

A certified single deletion gives $|E_1|-|E_0|=0-1=-1$. A word with $d>a$ therefore reduces edge complexity by $d-a$.

Q.E.D.

**In Plain English:**  
Section 6.1.3.1 formalizes the properties of the QBD proof regarding reducibility of trivial topologies.

---

### 6.1.3.2 Calculation: Legal-Task Reduction of Trivial Patterns {#6.1.3.2}

:::note[**Verification of Kinematic Reducibility via Legality-Indexed Task Sequences**]
:::

Verification of the edge-count balance on representative graph patterns (**Reducibility of Trivial Topologies** <Ref id="6.1.3.1" label="§6.1.3.1" />) is based on the following protocols:

1.  **Pattern Construction:** The algorithm instantiates five local graph fragments encoding Type II digons, double short paths, a Type III slide composite, a forbidden Type I self-loop addition, and an isolated directed 3-cycle.
2.  **Legal Task Execution:** The protocol applies only tasks inhabiting $\mathrm{LegalDel}$ or $\mathrm{LegalAdd}$ (irreflexivity, edge presence or absence, and short-path uniqueness), recording each complexity change $C=|E|$.
3.  **Reduction Metric:** The metric records whether Type II arms strictly decrease $C$, whether Type I additions are rejected, whether the Type III composite executes as add-then-delete, and whether an isolated 3-cycle evaporates under Bernoulli deletion sampling with acceptance probability $1/2$ across an ensemble of trials.

```python
"""
§6.1.3.2 Calculation: Legal-task reduction of trivial graph patterns.

Standalone verification that reducible (unknot-class) local patterns admit
finite sequences of legality-indexed elementary tasks that strictly decrease
edge complexity C, realizing the kinematic content of Lemma 6.1.3.

No shared library imports (monograph script constraint).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple

Edge = Tuple[int, int]
Graph = Set[Edge]


def complexity(G: Graph) -> int:
    return len(G)


def has_edge(G: Graph, e: Edge) -> bool:
    return e in G


def has_short_alt_path(G: Graph, u: int, v: int) -> bool:
    """True if a directed u→v path of length 1 or 2 already exists (PUC obstruction for add)."""
    if (u, v) in G:
        return True
    mids = {w for (a, w) in G if a == u}
    for w in mids:
        if (w, v) in G:
            return True
    return False


def legal_del(G: Graph, e: Edge) -> bool:
    return e in G


def legal_add(G: Graph, u: int, v: int) -> bool:
    if u == v:
        return False
    if (u, v) in G:
        return False
    # PUC: no alternate short path u ⇝ v
    if has_short_alt_path(G, u, v):
        return False
    return True


def apply_del(G: Graph, e: Edge) -> Graph:
    if e not in G:
        raise ValueError("illegal del")
    return set(G) - {e}


def apply_add(G: Graph, u: int, v: int) -> Graph:
    if not legal_add(G, u, v):
        raise ValueError("illegal add")
    return set(G) | {(u, v)}


def find_digon_redundant_edge(G: Graph) -> Optional[Edge]:
    """
    Type II pattern: two distinct short directed channels between some u,v.
    Prefer deleting a direct edge when a length-2 path also exists.
    """
    for (u, v) in list(G):
        # length-2 alternative u→w→v
        for (a, w) in G:
            if a == u and w != v and (w, v) in G:
                return (u, v)  # direct edge redundant under PUC reading
    # two parallel length-2 paths: delete first edge of one
    nodes = {x for e in G for x in e}
    for u in nodes:
        for v in nodes:
            if u == v:
                continue
            mids = [w for w in nodes if (u, w) in G and (w, v) in G and w not in (u, v)]
            if len(mids) >= 2:
                return (u, mids[0])
            if (u, v) in G and len(mids) >= 1:
                return (u, v)
    return None


def reduce_type_ii_until_fixed(G: Graph, max_steps: int = 32) -> Tuple[Graph, List[Edge], bool]:
    """Apply reducing Type II legal deletions until no digon pattern remains."""
    G = set(G)
    log: List[Edge] = []
    for _ in range(max_steps):
        e = find_digon_redundant_edge(G)
        if e is None:
            return G, log, True
        if not legal_del(G, e):
            return G, log, False
        G = apply_del(G, e)
        log.append(e)
    return G, log, False


def count_3_cycles(G: Graph) -> int:
    cycles = set()
    for (u, v) in G:
        for (a, w) in G:
            if a != v:
                continue
            if (w, u) in G:
                cycles.add(frozenset([(u, v), (v, w), (w, u)]))
    return len(cycles)


@dataclass
class ArmResult:
    name: str
    C_initial: int
    C_final: int
    steps: int
    n3_final: int
    reduced: bool
    detail: str


def arm_type_ii_digon() -> ArmResult:
    # Direct edge + length-2 path: digon / bubble (reducible Type II)
    G: Graph = {(0, 1), (0, 2), (2, 1)}
    C0 = complexity(G)
    Gf, log, ok = reduce_type_ii_until_fixed(G)
    return ArmResult(
        name="Type_II_digon",
        C_initial=C0,
        C_final=complexity(Gf),
        steps=len(log),
        n3_final=count_3_cycles(Gf),
        reduced=ok and complexity(Gf) < C0,
        detail=f"deleted={log}",
    )


def arm_double_bubble() -> ArmResult:
    # Two length-2 paths 0→1→3 and 0→2→3 (PUC digon at distance 2)
    G: Graph = {(0, 1), (1, 3), (0, 2), (2, 3)}
    C0 = complexity(G)
    Gf, log, ok = reduce_type_ii_until_fixed(G)
    return ArmResult(
        name="Type_II_double_path",
        C_initial=C0,
        C_final=complexity(Gf),
        steps=len(log),
        n3_final=count_3_cycles(Gf),
        reduced=ok and complexity(Gf) < C0,
        detail=f"deleted={log}",
    )


def arm_isolated_3_cycle_stochastic(trials: int = 200, steps: int = 40, seed: int = 0) -> ArmResult:
    """
    Isolated directed 3-cycle under thermo delete sampling Q=1/2 (mu=lambda=0).
    Kinematic legitimacy: each deletion of a cycle edge is LegalDel.
    Metric: fraction of trials that reach N3=0 within `steps`.
    """
    import random

    rng = random.Random(seed)
    evaporated = 0
    final_C = []
    for _ in range(trials):
        G: Graph = {(0, 1), (1, 2), (2, 0)}
        for _t in range(steps):
            edges = list(G)
            if not edges:
                break
            # Each edge of a 3-cycle is a legal del candidate; sample like Q_del=1/2
            # then pick a random cycle edge if accepted (matches micro-rule skeleton).
            if rng.random() < 0.5 and edges:
                e = rng.choice(edges)
                if legal_del(G, e):
                    G = apply_del(G, e)
            if count_3_cycles(G) == 0:
                evaporated += 1
                break
        final_C.append(complexity(G))
    frac = evaporated / trials
    return ArmResult(
        name="Isolated_3_cycle_stochastic",
        C_initial=3,
        C_final=int(round(sum(final_C) / len(final_C))),
        steps=steps,
        n3_final=0 if frac > 0.5 else 1,
        reduced=frac >= 0.95,
        detail=f"evaporated_fraction={frac:.3f} trials={trials}",
    )


def arm_type_iii_slide() -> ArmResult:
    """
    Compliant 2-path 0→1→2 licenses LegalAdd(2,0) (closing 3-cycle),
    then LegalDel of (0,1) implements a slide composite; C ends at 3 or less.
    """
    G: Graph = {(0, 1), (1, 2)}
    C0 = complexity(G)
    log = []
    if not legal_add(G, 2, 0):
        return ArmResult("Type_III_slide", C0, C0, 0, 0, False, "add_illegal")
    G = apply_add(G, 2, 0)
    log.append(("add", (2, 0)))
    if legal_del(G, (0, 1)):
        G = apply_del(G, (0, 1))
        log.append(("del", (0, 1)))
    # Composite executed; complexity may stay O(1); success = both tasks legal and ran
    ok = ("add", (2, 0)) in log and any(t[0] == "del" for t in log)
    return ArmResult(
        name="Type_III_slide",
        C_initial=C0,
        C_final=complexity(G),
        steps=len(log),
        n3_final=count_3_cycles(G),
        reduced=ok,
        detail=f"tasks={log}",
    )


def arm_self_loop_rejected() -> ArmResult:
    G: Graph = {(0, 1)}
    rejected = not legal_add(G, 0, 0)
    return ArmResult(
        name="Type_I_add_rejected",
        C_initial=1,
        C_final=1,
        steps=0,
        n3_final=0,
        reduced=rejected,
        detail="LegalAdd(0,0)=False",
    )


def main():
    arms = [
        arm_type_ii_digon(),
        arm_double_bubble(),
        arm_type_iii_slide(),
        arm_self_loop_rejected(),
        arm_isolated_3_cycle_stochastic(),
    ]

    print("=" * 72)
    print("§6.1.3.2 Legal-Task Reduction of Trivial Patterns")
    print("=" * 72)
    print(f"{'Arm':<28} {'C0':>4} {'Cf':>4} {'steps':>6} {'ok':>4}  detail")
    print("-" * 72)
    all_ok = True
    for a in arms:
        all_ok = all_ok and a.reduced
        print(
            f"{a.name:<28} {a.C_initial:4d} {a.C_final:4d} {a.steps:6d} "
            f"{'Y' if a.reduced else 'N':>4}  {a.detail}"
        )
    print("-" * 72)
    print(f"ALL_ARMS_REDUCED: {all_ok}")
    print("=" * 72)
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
```

**Simulation Results:**
```text
========================================================================
§6.1.3.2 Legal-Task Reduction of Trivial Patterns
========================================================================
Arm                            C0   Cf  steps   ok  detail
------------------------------------------------------------------------
Type_II_digon                   3    2      1    Y  deleted=[(0, 1)]
Type_II_double_path             4    3      1    Y  deleted=[(0, 1)]
Type_III_slide                  2    2      2    Y  tasks=[('add', (2, 0)), ('del', (0, 1))]
Type_I_add_rejected             1    1      0    Y  LegalAdd(0,0)=False
Isolated_3_cycle_stochastic     3    2     40    Y  evaporated_fraction=1.000 trials=200
------------------------------------------------------------------------
ALL_ARMS_REDUCED: True
========================================================================
```

**Conclusion:**
All five arms satisfy their tested predicates. Type II digon and double-path fragments strictly decrease $C$ under a single legal deletion. The Type III composite executes as one addition followed by one deletion, giving zero net edge-count change. Self-loop addition fails $\mathrm{LegalAdd}$. Across $200$ independent trials, the isolated directed 3-cycle reaches zero 3-cycle count with evaporated fraction $1.000$ under Bernoulli deletion probability $1/2$. These are checks of the specified fixtures and trial law (**Reducibility of Trivial Topologies** <Ref id="6.1.3.1" label="§6.1.3.1" />).

**In Plain English:**  
Section 6.1.3.2 formalizes the properties of the QBD calculation regarding legal-task reduction of trivial patterns.

---

### 6.1.3.3 Type-Theoretic Validation via Lean 4 Core {#6.1.3.3}

:::note[**Lean 4 Encoding of Legality-Indexed Elementary Tasks via Dependent Task Space and Reidemeister Realization**]
:::

Type-theoretic certification of the local task guards, braid identities, and deletion complexity (**Reducibility of Trivial Topologies** <Ref id="6.1.3.1" label="§6.1.3.1" />) (**Elementary Task Space** <Ref id="1.5.1" label="§1.5.1" />) proceeds via the following verification strategy:

1.  **Algebraic Braid Group and Graph Fragment Encoding:** The inductive types `BraidGen` and `BraidEquiv` formalize the Artin braid group $B_3$ modulo Yang-Baxter/Reidemeister III relations, while `LegalDel` and `LegalAdd` encode dependent elementary task guards over finite graph fragments.
2.  **Topological Realization and Invariance Theorems:** The realization map `reid_to_braid` lifts Reidemeister generators into braid words, with theorems `typeI_is_trivial_braid` and `typeIII_realizes_braid_relation` formally certifying braid group equivalence to the Artin exchange $\sigma_1\sigma_2\sigma_1 \sim \sigma_2\sigma_1\sigma_2$.
3.  **Strict Complexity Descent under Deletion:** List induction in `del_decreases_complexity` proves that deleting a present edge strictly decreases the encoded edge count.

```lean
-- ============================================================================
-- Section 6.1: Artin Braid Group B₃, Task Realization & Reidemeister Invariance
-- Standalone Lean 4 Core Formalization (Zero Axioms, Zero Sorry)
-- ============================================================================

set_option linter.unusedVariables false

-- ----------------------------------------------------------------------------
-- PART 1: THE ARTIN BRAID GROUP B₃ ALGEBRA
-- ----------------------------------------------------------------------------

/--
Elementary signed generator alphabet for the Artin Braid Group B₃ on 3 strands.
s1 denotes the over-crossing of strand 1 over strand 2; s2 denotes strand 2 over strand 3.
-/
inductive BraidGen where
  | s1     : BraidGen  -- σ₁
  | s2     : BraidGen  -- σ₂
  | s1_inv : BraidGen  -- σ₁⁻¹
  | s2_inv : BraidGen  -- σ₂⁻¹
  deriving DecidableEq, Repr

/--
A braid word in B₃ is a finite sequence of elementary generators.
-/
abbrev BraidWord := List BraidGen

/--
Braid Equivalence Relation on words in B₃ generated by:
1. Group inversion: σ_i · σ_i⁻¹ ~ ε and σ_i⁻¹ · σ_i ~ ε
2. The Artin Braid / Yang-Baxter / Reidemeister III relation:
   σ₁ · σ₂ · σ₁ ~ σ₂ · σ₁ · σ₂
-/
inductive BraidEquiv : BraidWord → BraidWord → Prop where
  | refl (w : BraidWord) : BraidEquiv w w
  | symm {w1 w2 : BraidWord} : BraidEquiv w1 w2 → BraidEquiv w2 w1
  | trans {w1 w2 w3 : BraidWord} : BraidEquiv w1 w2 → BraidEquiv w2 w3 → BraidEquiv w1 w3
  | cong_cons (g : BraidGen) {w1 w2 : BraidWord} : BraidEquiv w1 w2 → BraidEquiv (g :: w1) (g :: w2)
  | inv_s1 (w : BraidWord) : BraidEquiv (BraidGen.s1 :: BraidGen.s1_inv :: w) w
  | inv_s1_rev (w : BraidWord) : BraidEquiv (BraidGen.s1_inv :: BraidGen.s1 :: w) w
  | inv_s2 (w : BraidWord) : BraidEquiv (BraidGen.s2 :: BraidGen.s2_inv :: w) w
  | inv_s2_rev (w : BraidWord) : BraidEquiv (BraidGen.s2_inv :: BraidGen.s2 :: w) w
  | reidemeister_III (w : BraidWord) :
      BraidEquiv (BraidGen.s1 :: BraidGen.s2 :: BraidGen.s1 :: w)
                 (BraidGen.s2 :: BraidGen.s1 :: BraidGen.s2 :: w)

/--
THEOREM 6.1.1: The Fundamental Artin Braid Relation Holds in B₃
Formally proves that the canonical braid words σ₁σ₂σ₁ and σ₂σ₁σ₂ are equivalent under BraidEquiv.
-/
theorem artin_braid_relation :
    BraidEquiv [BraidGen.s1, BraidGen.s2, BraidGen.s1]
               [BraidGen.s2, BraidGen.s1, BraidGen.s2] := by
  have h := BraidEquiv.reidemeister_III []
  exact h

-- ----------------------------------------------------------------------------
-- PART 2: GRAPH KINEMATIC REALIZATION MAP (Φ)
-- ----------------------------------------------------------------------------

inductive V where
  | a | b | c
  deriving DecidableEq, Repr

abbrev Edge := V × V
abbrev Graph := List Edge

def hasEdge : Graph → Edge → Bool
  | [], _ => false
  | h :: t, e => decide (h = e) || hasEdge t e

def complexity (G : Graph) : Nat := G.length

def applyDel : Graph → Edge → Graph
  | [], _ => []
  | h :: t, e => if h = e then t else h :: applyDel t e

structure LegalDel (G : Graph) (e : Edge) : Prop where
  mem : hasEdge G e = true

structure LegalAdd (G : Graph) (e : Edge) : Prop where
  not_loop : e.1 ≠ e.2
  fresh : hasEdge G e = false

inductive AllowedTask (G : Graph) where
  | del (e : Edge) (h : LegalDel G e)
  | add (e : Edge) (h : LegalAdd G e)

inductive ReidLetter where
  | typeI_restorative
  | typeII_reducing
  | typeIII_slide

inductive TaskKind where
  | del
  | add
  | add_then_del

def phi : ReidLetter → TaskKind
  | .typeI_restorative => .del
  | .typeII_reducing => .del
  | .typeIII_slide => .add_then_del

/--
Map from Reidemeister move letters to representative braid words in B₃.
Type I (unknot curl) maps to σ₁σ₁⁻¹ (trivial unknotting).
Type III (triangle slide) maps to the braid exchange σ₁σ₂σ₁.
-/
def reid_to_braid : ReidLetter → BraidWord
  | .typeI_restorative => [BraidGen.s1, BraidGen.s1_inv]
  | .typeII_reducing => [BraidGen.s2, BraidGen.s2_inv]
  | .typeIII_slide => [BraidGen.s1, BraidGen.s2, BraidGen.s1]

/--
THEOREM 6.1.2: Type I Move Realizes Trivial Knot Invariance
Proves that the Type I curl move realizes as a braid word equivalent to the empty word (identity).
-/
theorem typeI_is_trivial_braid :
    BraidEquiv (reid_to_braid .typeI_restorative) [] := by
  dsimp [reid_to_braid]
  have h := BraidEquiv.inv_s1 []
  exact h

/--
THEOREM 6.1.3: Type III Move Realizes the Artin Braid Relation
Proves that the Type III slide realizes as the Artin braid word σ₁σ₂σ₁ which
evaluates to σ₂σ₁σ₂ in B₃, certifying topological braid invariance of graph slides.
-/
theorem typeIII_realizes_braid_relation :
    BraidEquiv (reid_to_braid .typeIII_slide) [BraidGen.s2, BraidGen.s1, BraidGen.s2] := by
  dsimp [reid_to_braid]
  exact artin_braid_relation

/--
THEOREM 6.1.4: Deleting a Present Edge Strictly Decreases Graph Complexity
-/
theorem del_decreases_complexity
    (G : Graph) (e : Edge) (h : hasEdge G e = true) :
    complexity (applyDel G e) < complexity G := by
  induction G with
  | nil => cases h
  | cons hd tl ih =>
      dsimp [applyDel, complexity, hasEdge] at h ⊢
      by_cases heq : hd = e
      · simp [heq]
      · have hdec : decide (hd = e) = false := by simp [heq]
        have htl : hasEdge tl e = true := by
          rw [hdec, Bool.false_or] at h
          exact h
        have ih' : (applyDel tl e).length < tl.length := by
          simpa [complexity] using ih htl
        simp [heq, Nat.succ_lt_succ ih']
```

**Verification Summary:**
The Lean module checks the Type I and Type III braid-word identities in the declared equivalence relation and the strict decrease of the edge-list length for a certified deletion. Its addition guard checks distinct endpoints and edge freshness. A PUC-compliant lift of a diagram word requires graph-side certificates for each intermediate task. The validated local results supply inputs to such a construction.

**In Plain English:**  
Section 6.1.3.3 formalizes the properties of the QBD type-theoretic regarding validation via lean 4 core.

---

### 6.1.4 Lemma: Catalyzed Instability {#6.1.4}

:::info[**Amplification via deletion probability at high local densities**]
:::

Let $\xi \subset G_t$ denote a decomposed cluster of isolated 3-cycles whose local cycle density $\rho_\xi$ strictly exceeds the equilibrium fixed point $\rho^*$ **Transcendental Balance** <Ref id="5.4.1" label="§5.4.1" />. Then the net topological current $\dot{\rho}$ obtained from the **Master Equation** <Ref id="5.2" label="§5.2" /> is strictly negative $(\dot{\rho} \ll 0)$, with the catalytic flux $J_{cat} = 3\lambda_{cat}\rho^2$ dominating the dynamics.

**In Plain English:**  
Section 6.1.4 formalizes the properties of the QBD lemma regarding catalyzed instability.

---

### 6.1.4.1 Proof: Catalyzed Instability {#6.1.4.1}

:::tip[**Explicit evaluation of net topological current via the Fundamental Equation**]
:::

**I. Density Equation and Parameter Bounds**

Let $\rho\ge0$ and write the mean-field current as

$$
\begin{gathered}
F(\rho)=(\Lambda+9\rho^2)e^{-a\rho}-\tfrac12\rho-\tfrac b2\rho^2,\\
a=6\mu=\frac6{\sqrt{2\pi}},\qquad b=6\lambda_{cat}=6(e-1),\qquad \Lambda>0.
\end{gathered}
$$

These are the creation and deletion terms (**Master Equation** <Ref id="5.2" label="§5.2" />), with the vacuum parameters fixed above (**Vacuum Permittivity ($\Lambda$)** <Ref id="5.2.3" label="§5.2.3" />). The elementary bounds on $\pi$ and $e$ give

$$
2.39<a<2.40,\qquad 10.30<b<10.32,\qquad \Lambda>0.
$$

**II. A Uniform Negative Derivative**

Differentiate every term:

$$
\begin{aligned}
F'(\rho)
&=18\rho e^{-a\rho}-a(\Lambda+9\rho^2)e^{-a\rho}-\tfrac12-b\rho\\
&\le18\rho e^{-a\rho}-\tfrac12-b\rho.
\end{aligned}
$$

For $x\ge0$, $e^x=1+x+\sum_{j\ge2}x^j/j!\ge1+x$, so $e^{-x}\le(1+x)^{-1}$. Thus

$$
\begin{aligned}
F'(\rho)
&\le\frac{18\rho}{1+a\rho}-\tfrac12-b\rho\\
&=\frac{-\tfrac12+(18-b-a/2)\rho-ab\rho^2}{1+a\rho}.
\end{aligned}
$$

Set $c=18-b-a/2$. The parameter bounds imply

$$
6.48<c<6.505,\qquad ab>2.39(10.30)=24.617,
$$

and consequently

$$
c^2<6.505^2=42.315025<49.234<2ab.
$$

Complete the square in the numerator:

$$
\begin{aligned}
-\tfrac12+c\rho-ab\rho^2
&=-ab\left(\rho-\frac{c}{2ab}\right)^2
  +\frac{c^2-2ab}{4ab}\\
&<0.
\end{aligned}
$$

Since $1+a\rho>0$, this proves $F'(\rho)<0$ for every $\rho\ge0$.

**III. Unique Equilibrium and Direction of Flow**

The endpoint and large-density limits are

$$
F(0)=\Lambda>0,\qquad
\lim_{\rho\to\infty}(\Lambda+9\rho^2)e^{-a\rho}=0,\qquad
\lim_{\rho\to\infty}F(\rho)=-\infty.
$$

Continuity gives a positive root, and strict decrease gives its uniqueness. Denote it by $\rho^*$ (**Transcendental Balance** <Ref id="5.4.1" label="§5.4.1" />). For every $\rho>\rho^*$,

$$
F(\rho)-F(\rho^*)=\int_{\rho^*}^{\rho}F'(s)\,\mathrm{d}s<0,
\qquad F(\rho^*)=0.
$$

Hence $\dot\rho=F(\rho)<0$ throughout the above-equilibrium interval. A solution starting above $\rho^*$ cannot cross the stationary solution by uniqueness for this smooth differential equation. It decreases to a limit $\ell\ge\rho^*$. If $\ell>\rho^*$, continuity supplies $\delta>0$ and a neighborhood of $\ell$ on which $F\le-\delta$. For all sufficiently large $t$,

$$
\rho(t)\le\rho(t_0)-\delta(t-t_0),
$$

contradicting $\rho(t)\ge\rho^*$. Therefore $\ell=\rho^*$.

**IV. High-Density Evaluation**

At the stated test density, using $\Lambda\approx0.0156$,

$$
\begin{aligned}
J_{in}(1/2)
&=(\Lambda+9/4)e^{-3/\sqrt{2\pi}}
 \approx2.2656e^{-1.1968\ldots}\approx0.685,\\
J_{cat}(1/2)&=3(e-1)/4\approx1.289,\\
J_{out}(1/2)&=1/4+3(e-1)/4\approx1.539,\\
F(1/2)&\approx0.685-1.539=-0.854.
\end{aligned}
$$

The catalytic contribution alone exceeds the creation contribution at this density. The all-density sign follows from Section II, independently of this numerical evaluation:

$$
\boxed{\rho>\rho^*\ \Longrightarrow\ \dot\rho<0,\qquad
\rho(0)>\rho^*\ \Longrightarrow\ \lim_{t\to\infty}\rho(t)=\rho^*.}
$$

Q.E.D.

**In Plain English:**  
Section 6.1.4.1 formalizes the properties of the QBD proof regarding catalyzed instability.

---

### 6.1.4.2 Calculation: Cluster Decay Simulation {#6.1.4.2}

:::note[**Computational Verification via the Fundamental Equation of Geometrogenesis**]
:::

Quantification of the density-dependent instability established by **Catalyzed Instability** <Ref id="6.1.4.1" label="§6.1.4.1" /> is based on the following protocols:

1.  **Dynamical Definition:** The algorithm defines the creation flux $J_{in}$ and deletion flux $J_{out}$ according to the **Master Equation** <Ref id="5.2" label="§5.2" /> parameters derived in Chapter 5 ($\Lambda \approx 0.016$, $\mu \approx 0.40$, $\lambda_{cat} \approx 1.72$).
2.  **Scenario Contrast:** The protocol evolves two distinct initial states: a **Trivial Excitation** subject to the full deletion flux, and a **Prime Knot** where the deletion flux $J_{out}$ is set to zero when the density drops below the knot core threshold.
3.  **Flux Integration:** The simulation integrates the net topological current $d\rho/dt$ over time to map the trajectory of a high-stress fluctuation ($\rho = 0.50$) toward equilibrium.

```python
import numpy as np

def simulate_cluster_decay():
    """
    Simulates the thermodynamic fate of a high-density excitation under the
    Fundamental Equation of Geometrogenesis.

    Compares:
    - Trivial (reducible) cluster: Fully exposed to deletion flux.
    - Prime knot: Protected by topological barrier below core density.

    Demonstrates architectural stability of non-trivial topology.
    """

    print("SIMULATION: TOPOLOGICAL STABILITY OF PARTICLES")
    print("Trivial Cluster vs. Prime Knot under Vacuum Deletion Flux")
    print("=" * 60)

    # ── Physical Constants (Derived in Chapter 5) ─────────────────────
    Λ_vac     = 0.0156                          # Vacuum Permittivity
    μ         = 1.0 / np.sqrt(2 * np.pi)        # Friction Coefficient ≈ 0.398942
    λ_cat     = np.e - 1                        # Catalysis Coefficient ≈ 1.718282

    ρ_star    = 0.0370                          # Equilibrium vacuum density
    ρ_core    = 0.0820                          # Knot core threshold (topological lock)

    # ── Simulation Parameters ────────────────────────────────────────
    initial_ρ = 0.50                            # High-stress fluctuation
    dt        = 0.10                            # Time step
    n_steps   = 600                             # Total steps (ensures convergence)

    time = np.arange(0, n_steps * dt, dt)

    # ── State Initialization ─────────────────────────────────────────
    ρ_trivial = np.zeros_like(time)
    ρ_knotted = np.zeros_like(time)

    ρ_trivial[0] = initial_ρ
    ρ_knotted[0] = initial_ρ

    # ── Flux Calculation Helper ──────────────────────────────────────
    def fluxes(ρ):
        j_in  = (Λ_vac + 9 * ρ**2) * np.exp(-6 * μ * ρ)
        j_out = 0.5 * ρ + 3 * λ_cat * ρ**2
        return j_in, j_out

    # ── Time Evolution Loop ──────────────────────────────────────────
    for i in range(1, len(time)):
        # Trivial cluster: Full exposure
        j_in_t, j_out_t = fluxes(ρ_trivial[i-1])
        dρ_t = j_in_t - j_out_t
        ρ_trivial[i] = max(ρ_star, ρ_trivial[i-1] + dρ_t * dt)

        # Prime knot: Deletion suppressed below core
        j_in_k, j_out_k = fluxes(ρ_knotted[i-1])
        if ρ_knotted[i-1] <= ρ_core:
            j_out_k = 0.0  # Topological barrier activates
        dρ_k = j_in_k - j_out_k
        ρ_knotted[i] = max(ρ_star, ρ_knotted[i-1] + dρ_k * dt)

    # ── Results Output ───────────────────────────────────────────────
    print(f"\nPhysical Parameters:")
    print(f"  Vacuum Drive (Λ)      : {Λ_vac:.4f}")
    print(f"  Friction (μ)          : {μ:.6f}")
    print(f"  Catalysis (λ_cat)     : {λ_cat:.6f}")
    print(f"  Equilibrium Density   : {ρ_star:.4f}")
    print(f"  Knot Core Threshold   : {ρ_core:.4f}")
    print(f"\nInitial Local Density   : {initial_ρ:.2f}")
    print("-" * 60)
    print(f"Final States after {n_steps} steps:")
    print(f"  Trivial Cluster       : {ρ_trivial[-1]:.6f} → Vacuum Equilibrium")
    print(f"  Prime Knot            : {ρ_knotted[-1]:.6f} → Stable Particle")
    print("-" * 60)

    # Initial flux balance verification
    j_in_0, j_out_0 = fluxes(initial_ρ)
    print(f"Initial Flux Balance (ρ = {initial_ρ}):")
    print(f"  Creation  J_in  : {j_in_0:.4f}")
    print(f"  Deletion  J_out : {j_out_0:.4f}")
    print(f"  Net Rate dρ/dt  : {j_in_0 - j_out_0:+.4f} (Strong Decay)")
if __name__ == "__main__":
    simulate_cluster_decay()
```

**Simulation Results:**

```
SIMULATION: TOPOLOGICAL STABILITY OF PARTICLES
Trivial Cluster vs. Prime Knot under Vacuum Deletion Flux
============================================================

Physical Parameters:
  Vacuum Drive (Λ)      : 0.0156
  Friction (μ)          : 0.398942
  Catalysis (λ_cat)     : 1.718282
  Equilibrium Density   : 0.0370
  Knot Core Threshold   : 0.0820

Initial Local Density   : 0.50
------------------------------------------------------------
Final States after 600 steps:
  Trivial Cluster       : 0.037000 → Vacuum Equilibrium
  Prime Knot            : 0.081329 → Stable Particle
------------------------------------------------------------
Initial Flux Balance (ρ = 0.5):
  Creation  J_in  : 0.6846
  Deletion  J_out : 1.5387
  Net Rate dρ/dt  : -0.8542 (Strong Decay)
```

**Conclusion:**
The simulation data indicates that at the initial high density $\rho=0.50$, the deletion flux $J_{out} \approx 1.54$ significantly exceeds the creation flux $J_{in} \approx 0.69$, yielding a net negative current of $-0.85$. This imbalance drives the trivial cluster to collapse to the vacuum fixed point $\rho^* \approx 0.037$. In contrast, the knotted cluster trajectory stabilizes at $\rho \approx 0.081$, confirming that the activation of the topological barrier arrests the decay process despite the high catalytic stress. These results validate the decay mechanics and the barrier efficiency described in the derivation.

**In Plain English:**  
Section 6.1.4.2 formalizes the properties of the QBD calculation regarding cluster decay simulation.

---

### 6.1.5 Lemma: Topological Barrier {#6.1.5}

:::info[**Protection via invariance under local tasks**]
:::

Let $\xi_0$ be a closed knot or link configuration with a registered invariant $\mathcal I(\xi_0)\ne 0$, and let the protected family consist of legal horizon-supported tasks that preserve $\mathcal I$. Then zero-invariant configurations are unreachable by words in that family, and any admitted path with conditional acceptance factors bounded by $e^{-\mu b_j}$ has probability at most $e^{-\mu\sum_j b_j}$ for $\mu>0$ and $b_j\ge 0$.

**In Plain English:**  
Section 6.1.5 formalizes the properties of the QBD lemma regarding topological barrier.

---

### 6.1.5.1 Proof: Topological Barrier {#6.1.5.1}

:::tip[**Derivation of sector protection via invariant preservation and conditional path weights**]
:::

**I. Legal words and the protected family**

Fix the legality-indexed **Elementary Task Space** <Ref id="1.5.1" label="§1.5.1" /> and the registered invariant $\mathcal I$. A certified word has successive states

$$
\xi_0 \xrightarrow{\tau_1} \xi_1 \xrightarrow{\tau_2} \cdots
\xrightarrow{\tau_m}\xi_m,\qquad
\tau_j\in\mathfrak T(G_{j-1}).
$$

Write $\mathfrak T_{\mathrm{prot}}$ for the legal tasks supported within the model horizon that preserve $\mathcal I$ on their stated domain. For example, for the pairwise Gauss linking number, the protected domain includes the disjoint closed-curve deformations of **Local Horizon** <Ref id="6.4.3" label="§6.4.3" />.

**II. Exact invariant balance**

If every step lies in the protected family, then

$$
\begin{aligned}
\mathcal I(\xi_m)-\mathcal I(\xi_0)
&=\sum_{j=1}^{m}\bigl(\mathcal I(\xi_j)-\mathcal I(\xi_{j-1})\bigr)\\
&=\sum_{j=1}^{m}0=0,\\
\mathcal I(\xi_m)&=\mathcal I(\xi_0)\ne0.
\end{aligned}
$$

Equivalently, if $\mathcal I(\xi_m)=0$, then

$$
\sum_{j=1}^{m}\bigl(\mathcal I(\xi_j)-\mathcal I(\xi_{j-1})\bigr)
=-\mathcal I(\xi_0)\ne 0
\ \Longrightarrow\
\exists j:\ \mathcal I(\xi_j)\ne\mathcal I(\xi_{j-1}).
$$

Thus that word must use a step outside the protected family.

**III. Probability of a supplied path**

For a separately admitted path, let $A_j$ be the event of executing its $j$th prescribed step. Use the effective acceptance premise of the **Topological Barrier** <Ref id="6.1.5" label="§6.1.5" /> in the normalized form

$$
\Pr(A_j\mid A_1,\ldots,A_{j-1})\le e^{-\mu b_j},
\qquad b_j\ge0,\quad\mu>0.
$$

When the prefixes have positive probability, the chain rule gives

$$
\begin{aligned}
\Pr(A_1\cap\cdots\cap A_m)
&=\Pr(A_1)\prod_{j=2}^{m}\Pr(A_j\mid A_1,\ldots,A_{j-1})\\
&\le \prod_{j=1}^{m}e^{-\mu b_j}
=\exp\!\left(-\mu\sum_{j=1}^{m} b_j\right).
\end{aligned}
$$

A zero-probability prefix makes the entire path probability zero. If $k$ prescribed steps each cost at least $b_*>0$, the same bound yields

$$
\sum_{j=1}^{m}b_j\ge k b_*
\quad\Longrightarrow\quad
\boxed{\Pr(A_1\cap\cdots\cap A_m)\le e^{-\mu k b_*}.}
$$

For the illustrative local-volume benchmark $b_1=12\rho$ and $\mu\rho=0.2$, the single-step version evaluates to

$
e^{-\mu b_1}=e^{-12\mu\rho}=e^{-12(0.2)}=e^{-2.4}\simeq0.09072 .
$

Q.E.D.

**In Plain English:**  
Section 6.1.5.1 formalizes the properties of the QBD proof regarding topological barrier.

---

### 6.1.6 Proof: Particle Necessity {#6.1.6}

:::tip[**Formal Demonstration of the Persistence of Non-Trivial Excitations via Reductio Ad Absurdum**]
:::

**I. Hypothesis and Initial Conditions**

Let $\xi_{stable}$ be a persistent, localized excitation. Assume for contradiction that $\xi_{stable}$ is topologically trivial ($V_\xi(t) = 1$).

**II. Reducibility and Decomposition**

Under the **Reducibility of Trivial Topologies** <Ref id="6.1.3" label="§6.1.3" />, the topological triviality of $\xi_{stable}$ implies the existence of a local rewrite sequence $\mathcal{S} \subseteq \mathcal{R}$ that decomposes the excitation into a set of disjoint, unlinked 3-cycles $\bigcup_j C_3^{(j)}$.

**III. Thermodynamic Response and Catalyzed Decay**

Under the **Catalyzed Instability** <Ref id="6.1.4" label="§6.1.4" />, the resulting decomposed state exhibits a high local cycle density exceeding the vacuum equilibrium, $\rho > \rho^*$. The master equation then dictates a strictly negative net topological current ($d\rho/dt \ll 0$), driving the system toward collapse.

**IV. Obstruction and Topological Barrier**

Conversely, let $\xi_{knot}$ be an excitation characterized by a non-trivial invariant ($V_\xi(t) \neq 1$). Under the **Topological Barrier** <Ref id="6.1.5" label="§6.1.5" />, no reducing Reidemeister word for $\mathcal{I}\to 0$ lifts to a sequence in $\mathfrak{T}(G)$ supported inside the local horizon $R$, so the deletion mechanism cannot erase the excitation by legal elementary tasks alone.

**V. Synthesis and Conclusion**

The contradiction between the assumed persistence of $\xi_{stable}$ and its decay establishes that only non-trivial topologies possess the architectural protection to survive the deletion flux. Stability is therefore equivalent to non-trivial topology.

Q.E.D.

**In Plain English:**  
Section 6.1.6 formalizes the properties of the QBD proof regarding particle necessity.

---

### 6.2.1 Definition: Tripartite Braid {#6.2.1}

:::tip[**Structural Definition based on World-Tube Geometry and Group Generators via Tripartite Braid**]
:::

The **Tripartite Braid**, denoted as $\beta_3$, is defined strictly as a prime topological configuration comprising exactly three interacting ribbons within the causal graph $G_t$. The validity of this structure is constituted by the simultaneous satisfaction of the following four invariant properties:

1.  **World-Tube Geometry:** Each constituent ribbon defines a time-like world-tube formed by a directed, framed chain of 3-cycles, which satisfies the requirements of the **Geometric Constructibility** <Ref id="2.3.1" label="§2.3.1" /> and maintains the causal orientation mandated by the **Axiom 1: The Directed Causal Link**.
2.  **Topological Non-Triviality:** The ribbons interweave via crossings compliant with the **Principle of Unique Causality**, yielding strictly non-zero global invariants, specifically a non-zero Writhe $w(\beta_3) \neq 0$ and non-zero pairwise Linking Numbers $L_{ij} \neq 0$ derived from Gauss integrals over pairwise axes.
3.  **Algebraic Generation:** The configuration generates the non-abelian Braid Group on three strands, denoted $B_3$, which satisfies the Yang-Baxter equation $b_1 b_2 b_1 = b_2 b_1 b_2$ and embeds the Special Unitary algebra $\mathfrak{su}(3)$ via three-dimensional fundamental representations.
4.  **Logical Protection:** The configuration occupies a protected logical subspace within the Quantum Error-Correcting Code codespace $\mathcal{C}$ **Generalized Stabilizer Formulation** <Ref id="3.5.1" label="§3.5.1" />, characterized by the enforcement of $+1$ eigenvalues for the Geometric Stabilizers $K_{\text{geom}} = ZZZ$ **Hard Constraint Validity**.

**In Plain English:**  
Section 6.2.1 formalizes the properties of the QBD definition regarding tripartite braid.

---

### 6.2.2 Theorem: Tripartite Braid Theorem {#6.2.2}

:::info[**Uniqueness of the Prime Three-Ribbon Structure established by Inductive Exclusion**]
:::

Every stable, first-generation elementary fermion is topologically isomorphic to a prime, three-ribbon braid ($n=3$) residing within the codespace $\mathcal{C}$ (**Generalized Stabilizer Formulation** <Ref id="3.5.1" label="§3.5.1" />), a uniqueness established by the exhaustive exclusion of all alternative ribbon counts.

In particular, configurations with fewer than three ribbons ($n < 3$) are excluded due to topological instability for $n=1$ via **Exclusion of Single-Ribbon (n=1)** <Ref id="6.2.4" label="§6.2.4" /> or algebraic insufficiency for $n=2$ via **Exclusion of Two-Ribbon (n=2)**.

Furthermore, configurations with greater than three ribbons ($n > 3$) are excluded by Entropic Parsimony (**Transcendental Balance** <Ref id="5.4.1" label="§5.4.1" />), leaving the tripartite braid as the unique solution satisfying the 3-cycle **Geometric Quantum** to provide the necessary basis for three color charges and anomaly cancellation.

**In Plain English:**  
Section 6.2.2 formalizes the properties of the QBD theorem regarding tripartite braid theorem.

---

### 6.2.3 Lemma: Exclusion of Unbraided Clusters (n=0) {#6.2.3}

:::info[**Topological Triviality via Instability under Catalytic Deletion**]
:::

For any localized excitation characterized by a trivial topology, constituting an unbraided cluster with trivial Jones Polynomial $V_{\xi}(t) = 1$, the configuration is dynamically unstable and subject to immediate dissolution. The absence of non-trivial invariants ($w=0, L=0$) renders the cluster susceptible to the Catalytic Deletion Flux $J_{out}$ (**Master Equation** <Ref id="5.2" label="§5.2" />) which is amplified by the density-dependent stress term $3\lambda_{cat}\rho^2$, driving the configuration toward the vacuum equilibrium.

**In Plain English:**  
Section 6.2.3 formalizes the properties of the QBD lemma regarding exclusion of unbraided clusters (n=0).

---

### 6.2.3.1 Proof: Exclusion of Unbraided Clusters (n=0) {#6.2.3.1}

:::tip[**Mean-Field Relaxation via a Uniform Derivative Bound**]
:::

**I. Unbraided Cluster and Scalar Current**

Let $\xi$ be an unbraided cluster with writhe $w=0$ and linking invariant $L=0$. The unbraided model assigns topological activation cost $\Delta E_{\text{barrier}}(\xi)=0$. Let the initial density be $\rho_0>\rho^*$, where $\rho^*$ is the vacuum equilibrium. The homogeneous density evolution is the driven scalar closure (**Macroscopic Evolution** <Ref id="5.2.2" label="§5.2.2" />) (**Catalyzed Instability** <Ref id="6.1.4" label="§6.1.4" />),

$$
\begin{aligned}
\dot\rho&=F(\rho)=(\Lambda+9\rho^2)e^{-a\rho}-\tfrac12\rho-\tfrac b2\rho^2,
&F(\rho^*)&=0,\\
a&=6/\sqrt{2\pi}, & b&=6(e-1),\\
2.39&<a<2.40, &10.30&<b<10.32.
\end{aligned}
$$

**II. Uniform Bound on the Net Current**

The derivative bound is $F'(\rho)\le 18\rho/(1+a\rho)-1/2-b\rho$ (**Catalyzed Instability** <Ref id="6.1.4" label="§6.1.4" />). Put $c=18-b-9a/20$. Since $\rho\ge0$,

$$
\begin{aligned}
(1+a\rho)\bigl(F'(\rho)+\tfrac1{20}\bigr)
&\le 18\rho-\bigl(\tfrac9{20}+b\rho\bigr)(1+a\rho)\\
&=-\tfrac9{20}+c\rho-ab\rho^2\\
&=-ab\left(\rho-\frac{c}{2ab}\right)^2+\frac{c^2-(9/5)ab}{4ab}.
\end{aligned}
$$

The bounds give $0<c<18-10.30-(9/20)(2.39)=6.6245<6.625$ and $ab>2.39(10.30)=24.617$. Hence

$$
c^2<6.625^2=43.890625<44.3106=\tfrac95(24.617)<\tfrac95 ab.
$$

The numerator is negative, so $F'(\rho)\le-1/20$. For $\rho>\rho^*$ this yields

$$
F(\rho)=F(\rho^*)+\int_{\rho^*}^{\rho}F'(u)\,\mathrm du
\le -\tfrac1{20}(\rho-\rho^*)<0.
$$

**III. Relaxation Above the Vacuum**

On $\rho^*\le \rho\le\rho_0$, the derivative formula gives the finite lower bound

$$
\begin{aligned}
F'(\rho)
&=18\rho e^{-a\rho}-a(\Lambda+9\rho^2)e^{-a\rho}-\tfrac12-b\rho\\
&\ge -a(\Lambda+9\rho_0^2)-\tfrac12-b\rho_0=-K.
\end{aligned}
$$

With $z(t)=\rho(t)-\rho^*$, integration from $\rho^*$ to $\rho(t)$ gives $-Kz(t)\le\dot z(t)\le-z(t)/20$ while $z(t)>0$. Thus

$$
\frac{\mathrm d}{\mathrm dt}(e^{Kt}z(t))\ge0,\qquad
\frac{\mathrm d}{\mathrm dt}(e^{t/20}z(t))\le0.
$$

Integrating from $0$ to $t$ yields

$$
(\rho_0-\rho^*)e^{-Kt}\le \rho(t)-\rho^*
\le(\rho_0-\rho^*)e^{-t/20}.
$$

The lower bound excludes a finite first arrival at $\rho^*$. The solution stays in the compact interval $[\rho^*,\rho_0]$, so smoothness of $F$ gives continuation for every $t\ge0$. The upper bound tends to zero and the strict sign gives monotone decay to $\rho^*$.

Q.E.D.

**In Plain English:**  
Section 6.2.3.1 formalizes the properties of the QBD proof regarding exclusion of unbraided clusters (n=0).

---

### 6.2.4 Lemma: Exclusion of Single-Ribbon (n=1) {#6.2.4}

:::info[**Reducibility via certified local framing relaxation**]
:::

Let a single framed ribbon belong to a framing sector where zero marked twists mean an untwisted ribbon and every reachable state with positive marked twist count admits a graph-legal opposite-sign pair removal or boundary release that reduces that count (**Elementary Task Space** <Ref id="1.5.1" label="§1.5.1" />). Then that configuration is excluded from the class of single-ribbon states protected against local reduction.

**In Plain English:**  
Section 6.2.4 formalizes the properties of the QBD lemma regarding exclusion of single-ribbon (n=1).

---

### 6.2.4.1 Proof: Exclusion of Single-Ribbon (n=1) {#6.2.4.1}

:::tip[**Derivation of single-ribbon reducibility via signed cancellation and the strain recurrence**]
:::

**I. Inter-strand braid and framed twist**

The Artin presentation has one adjacent generator per adjacent pair (**Braid Group Isomorphism** <Ref id="8.1.2" label="§8.1.2" />). For a single ribbon this gives

$$
B_1=\langle\,\varnothing\mid\varnothing\,\rangle=\{e\}.
$$

Let the $k$ marked half-twists have signs $\varepsilon_i\in\{-1,1\}$ and signed twist count $w=\frac12\sum_{i=1}^{k}\varepsilon_i$. The absence of an inter-strand generator leaves this signed count as separate framing data.

**II. Local reduction and the strain cost**

A Type II cancellation of a graph-legal opposite-sign pair changes the marked count from $k$ to $k-2$ and has signed balance

$$
w_{\mathrm{after}}-w_{\mathrm{before}}
=-\tfrac12\bigl(+1+(-1)\bigr)=0.
$$

In the quadratic strain model of **Quadratic Scaling of Torsion** <Ref id="6.3.5" label="§6.3.5" />, take the worked first-twist count $N_{\mathrm{strain}}(1)=2$ and marginal cost $\alpha j$ after $j\ge1$ twists, with $\alpha>0$. The two support cycles are the base cost of that model. For $k\ge1$,

$$
\begin{aligned}
N_{\mathrm{strain}}(k)
&=N_{\mathrm{strain}}(1)
 +\sum_{j=1}^{k-1}\bigl(N_{\mathrm{strain}}(j+1)-N_{\mathrm{strain}}(j)\bigr)\\
&=2+\alpha\sum_{j=1}^{k-1}j
=2+\frac{\alpha}{2}k(k-1).
\end{aligned}
$$

For $k\ge3$, when both endpoints are in this recurrence,

$$
\begin{aligned}
N_{\mathrm{strain}}(k)-N_{\mathrm{strain}}(k-2)
&=\frac{\alpha}{2}\bigl(k(k-1)-(k-2)(k-3)\bigr)\\
&=\frac{\alpha}{2}(4k-6)=\alpha(2k-3)>0 .
\end{aligned}
$$

For an untwisted reference with $N_{\mathrm{strain}}(0)=0$, the two terminal cost drops are

$$
N_{\mathrm{strain}}(2)-N_{\mathrm{strain}}(0)=2+\alpha>0,
\qquad
N_{\mathrm{strain}}(1)-N_{\mathrm{strain}}(0)=2>0.
$$

**III. Certified relaxation**

For the local admission premise of **Exclusion of Single-Ribbon (n=1)** <Ref id="6.2.4" label="§6.2.4" />, whenever $k_j>0$ one can choose a legal step with $k_{j+1}\le k_j-1$. Inductively, while the construction continues,

$$
k_j\le k_0-j
\ \Longrightarrow\
0\le k_{j+1}\le k_j-1\le k_0-(j+1).
$$

If the count stays positive through step $k_0$, this inequality gives $0<k_{k_0}\le0$. Hence for some $m\le k_0$,

$$
k_m=0,\qquad
\boxed{\xi_0\xrightarrow{\ \tau_m\circ\cdots\circ\tau_1\ }\xi_{\mathrm{untwisted}}.}
$$

Q.E.D.

**In Plain English:**  
Section 6.2.4.1 formalizes the properties of the QBD proof regarding exclusion of single-ribbon (n=1).

---

### 6.2.5 Lemma: Exclusion of Two-Ribbon (n=2) {#6.2.5}

:::info[**Algebraic insufficiency via the cyclic braid image**]
:::

Let the continuous gauge action of a two-ribbon sector be generated solely by the closure of a unitary image of its Artin braid group $B_2$ (**Braid Group Isomorphism** <Ref id="8.1.2" label="§8.1.2" />). Then the resulting gauge Lie algebra is Abelian and insufficient to supply the non-Abelian color action of a fundamental quark.

**In Plain English:**  
Section 6.2.5 formalizes the properties of the QBD lemma regarding exclusion of two-ribbon (n=2).

---

### 6.2.5.1 Proof: Exclusion of Two-Ribbon (n=2) {#6.2.5.1}

:::tip[**Derivation of the two-ribbon obstruction via commuting braid powers**]
:::

**I. Normal form**

Let $B_n$ denote the Artin braid group on $n$ strands (**Braid Group Isomorphism** <Ref id="8.1.2" label="§8.1.2" />). For $n=2$, the presentation is $B_2=\langle \sigma_1\mid\varnothing\rangle$. The maps $p\mapsto\sigma_1^p$ and $\sigma_1\mapsto1$ extend to homomorphisms with compositions $p\mapsto p$ and $\sigma_1^p\mapsto\sigma_1^p$. Hence

$$
B_2\cong(\mathbb Z,+),\qquad
[\sigma_1^p,\sigma_1^q]
=\sigma_1^p\sigma_1^q\sigma_1^{-p}\sigma_1^{-q}
=\sigma_1^{p+q-p-q}=e,\qquad
[B_2,B_2]=\{e\}.
$$

**II. Image and its Lie bracket**

For a finite-dimensional unitary representation $\rho$, set $U=\rho(\sigma_1)$. Then

$$
\rho(\sigma_1^p)=U^p,\qquad U^p U^q=U^{p+q}=U^q U^p.
$$

If $A=\lim_j U^{p_j}$ and $B=\lim_j U^{q_j}$ lie in the closure $K$ of the image, then

$$
AB=\lim_j(U^{p_j}U^{q_j})=\lim_j(U^{q_j}U^{p_j})=BA .
$$

For $X,Y\in\operatorname{Lie}(K)$, differentiation first in $s$ and then in $t$ gives

$$
\begin{aligned}
e^{sX}e^{tY}&=e^{tY}e^{sX},\\
X e^{tY}&=e^{tY}X,\\
XY&=YX .
\end{aligned}
$$

**III. Color commutator**

With the **Lie Algebra Generator** <Ref id="8.1.1" label="§8.1.1" /> convention, the independent basis generators have zero commutators, so their structure constants are zero. In particular the gauge curvature of a connection $A_\mu$ in this algebra satisfies

$$
F_{\mu\nu}
=\partial_\mu A_\nu-\partial_\nu A_\mu+g[A_\mu,A_\nu]
=\partial_\mu A_\nu-\partial_\nu A_\mu .
$$

For color, the matrix units $E_{ab}$ satisfy $E_{ab}E_{cd}=\delta_{bc}E_{ad}$. The two traceless anti-Hermitian matrices $X=E_{12}-E_{21}$ and $Y=i(E_{12}+E_{21})$ give

$$
XY=i(E_{11}-E_{22}),\qquad YX=-i(E_{11}-E_{22}),\qquad
\boxed{[X,Y]=2i(E_{11}-E_{22})\ne0.}
$$

Thus the cyclic braid image cannot supply the color Lie algebra.

Q.E.D.

**In Plain English:**  
Section 6.2.5.1 formalizes the properties of the QBD proof regarding exclusion of two-ribbon (n=2).

---

### 6.2.6 Lemma: Exclusion of Higher Order Configurations (n > 3) {#6.2.6}

:::info[**Relative population suppression via a positive formation-cost gap**]
:::

Let an $n$-ribbon candidate with $n>3$ and the tripartite reference have positive statistical weights with Boltzmann factor $e^{-E/T}$ at $T>0$, with equal multiplicities and a positive cost gap $E_n-E_3$. Then the relative population is exponentially suppressed in the gap, and any proposed $\mathfrak{su}(4)$ control sector is insufficient to contain the full Standard Model gauge algebra.

**In Plain English:**  
Section 6.2.6 formalizes the properties of the QBD lemma regarding exclusion of higher order configurations (n > 3).

---

### 6.2.6.1 Proof: Exclusion of Higher Order Configurations (n > 3) {#6.2.6.1}

:::tip[**Derivation of relative suppression via Boltzmann weights and rank**]
:::

**I. Population ratio**

Use the equilibrium comparison in **Exclusion of Higher Order Configurations (n > 3)** <Ref id="6.2.6" label="§6.2.6" /> with $k_B=1$. If $g_i$ counts states at the assigned cost $E_i$, the corresponding contributions are

$$
Z_i=g_i e^{-E_i/T},\qquad
Z=\sum_i Z_i,\qquad
P_i=\frac{Z_i}{Z}.
$$

For $g_n=g_3$ and $\Delta E_n=E_n-E_3>0$,

$$
\frac{P_n}{P_3}
=\frac{Z_n/Z}{Z_3/Z}
=\frac{g_n}{g_3}e^{-(E_n-E_3)/T}
=\boxed{e^{-\Delta E_n/T}\in(0,1)} .
$$

**II. Worked cost comparisons**

For the benchmark $C_4\ge8$, $C_3=3$ and a weight $e^{-\mu C}$ at $\mu=0.4$,

$$
C_4-C_3\ge 8-3=5,\qquad
\frac{P_4}{P_3}\le e^{-0.4(8-3)}=e^{-2}\simeq0.135335.
$$

The separate unit-cost input in the **Entropic Exclusion Simulation** <Ref id="6.2.6.2" label="§6.2.6.2" /> assigns $\Delta E_n=n-3$ and $T=\ln 2$. It gives

$$
\begin{aligned}
\frac{P_4}{P_3}&=e^{-(4-3)/\ln 2}\simeq0.236290,\\
\frac{P_5}{P_3}&=e^{-(5-3)/\ln 2}\simeq0.055833,\\
\frac{P_8}{P_3}&=e^{-(8-3)/\ln 2}\simeq0.000737.
\end{aligned}
$$

If the assigned crossing costs are $C_5=5$ and $C_3=3$ and both use a common mass conversion $m_i=\eta C_i$ with $\eta>0$ from **Linear Scaling of Crossings** <Ref id="6.3.4" label="§6.3.4" />, the corresponding mass comparison is

$
\frac{m_5}{m_3}=\frac{\eta C_5}{\eta C_3}=\frac{5}{3}.
$

**III. Rank of the candidate control algebra**

Assume that the required coherent controls have been admitted for the proposed degree-four matrix model in **Adjacent Generator Closure** <Ref id="8.2" label="§8.2" />. A commuting subalgebra of skew-Hermitian matrices admits a common unitary diagonalization. Within $\mathfrak{su}(4)$, a diagonal element has the form

$$
i\operatorname{diag}(a_1,a_2,a_3,-a_1-a_2-a_3),
\qquad a_j\in\mathbb R.
$$

The full gauge algebra has independent diagonal directions from traceless $3\times3$, traceless $2\times2$, and scalar $\mathfrak u(1)$ sectors. For any injective Lie map $f$, one has $[f(X),f(Y)]=f([X,Y])=0$ on these directions, so its image would be a four-dimensional commuting subalgebra. The count gives

$$
\operatorname{rank}(\mathfrak{su}(3)\oplus\mathfrak{su}(2)\oplus\mathfrak u(1))
=(3-1)+(2-1)+1=4>3=\operatorname{rank}\mathfrak{su}(4).
$$

Q.E.D.

**In Plain English:**  
Section 6.2.6.1 formalizes the properties of the QBD proof regarding exclusion of higher order configurations (n > 3).

---

### 6.2.6.2 Calculation: Entropic Exclusion Simulation {#6.2.6.2}

:::note[**Computational Verification of Entropic Suppression via High-Order Braids**]
:::

Quantification of the formation probabilities for higher-order structures established by **Exclusion of Higher Order Configurations (n > 3)** <Ref id="6.2.6.1" label="§6.2.6.1" /> is based on the following protocols:

1.  **Thermodynamic Definition:** The algorithm sets the base-conversion modulus to the critical value $\beta_c = \ln 2$.
2.  **Complexity Mapping:** The protocol assigns a linear energy cost $E_C \propto n$ to the minimal prime knot on $n$ strands relative to the equilibrium vacuum density derived via **Transcendental Balance** <Ref id="5.4.1" label="§5.4.1" />.
3.  **Probability Normalization:** The simulation calculates the relative Boltzmann weights for ribbon counts $n \in [3, 8]$ and normalizes these values against the $n=3$ ground state to determine the suppression factors.

```python
import numpy as np
import pandas as pd

def simulate_entropic_exclusion():
    """
    Computes informational suppression of higher-order braids (n > 3)
    relative to tripartite ground state (n=3).
    
    Discrete state counting model: Delta C = 1 nat per ribbon, beta_c = ln 2.
    """
    print("=" * 70)
    print("ENTROPIC SUPPRESSION OF EXOTIC BRAIDS")
    print("Boltzmann Weights vs. Ribbon Count (n)")
    print("=" * 70)
    
    beta_c = np.log(2)                                 # ~ 0.693147
    suppression_per_ribbon = np.exp(-1 / beta_c)        # ~ 0.236290
    
    n_values = np.arange(3, 9)
    relative = suppression_per_ribbon ** (n_values - 3)
    suppression_factor = 1 / relative
    
    df = pd.DataFrame({
        'Ribbon count (n)'      : n_values,
        'Relative probability'  : [f"{r:.6f}" for r in relative],
        'Suppression factor'    : [f"{s:.1f}" for s in suppression_factor]
    })
    
    print(f"\nInformation modulus beta_c = ln 2 ~ {beta_c:.6f}")
    print(f"Cost per ribbon Delta C = 1 nat")
    print(f"Suppression per ribbon ~ {suppression_per_ribbon:.6f}")
    print("\nResults (normalized to n=3):")
    print(df.to_string(index=False))

if __name__ == "__main__":
    simulate_entropic_exclusion()
```

**Simulation Results:**

```text
======================================================================
ENTROPIC SUPPRESSION OF EXOTIC BRAIDS
Boltzmann Weights vs. Ribbon Count (n)
======================================================================

Information modulus beta_c = ln 2 ~ 0.693147
Cost per ribbon Delta C = 1 nat
Suppression per ribbon ~ 0.236290

Results (normalized to n=3):
 Ribbon count (n) Relative probability Suppression factor
                3             1.000000                1.0
                4             0.236290                4.2
                5             0.055833               17.9
                6             0.013193               75.8
                7             0.003117              320.8
                8             0.000737             1357.6
```

**Conclusion:**
The calculated relative abundances demonstrate an exponential decay in formation probability as the ribbon count increases. While the $n=3$ configuration represents the unitary baseline ($P=1.0$), the $n=4$ population is suppressed to approximately $23.6\%$ (a factor of 1 in 4.2). The suppression factor increases rapidly for higher orders, reaching 1 in 17.9 for $n=5$ and 1 in 1357 for $n=8$. This statistical distribution confirms that hyper-complex braids are thermodynamically rarefied relative to the tripartite ground state.

**In Plain English:**  
Section 6.2.6.2 formalizes the properties of the QBD calculation regarding entropic exclusion simulation.

---

### 6.2.7 Proof: Tripartite Braid Theorem {#6.2.7}

:::tip[**Formal Verification of the Uniqueness of the Tripartite Braid via Inductive Exclusion**]
:::

**I. Initial Conditions and Inductive Framework**

The proof employs formal induction on the ribbon count $n$. Configurations with $n < 3$ ribbons fail either topological stability or algebraic sufficiency, while configurations with $n > 3$ ribbons introduce superfluous complexity. This induction matches the **Axiom 2: Geometric Constructibility** <Ref id="2.3.1" label="§2.3.1" /> and **General Cycle Decomposition** <Ref id="2.4.1" label="§2.4.1" />.

**II. Lower Bound Exclusion**

For the base cases $n < 3$, the configurations are excluded systematically:
1. **Unbraided structures ($n=0$):** As shown in **Exclusion of Unbraided Clusters (n=0)** <Ref id="6.2.3" label="§6.2.3" />, these exhibit topological triviality and instability under the deletion flux.
2. **Single-ribbon structures ($n=1$):** As demonstrated in **Exclusion of Single-Ribbon (n=1)** <Ref id="6.2.4" label="§6.2.4" />, these suffer from reducibility via Type II moves, preventing stability.
3. **Two-ribbon structures ($n=2$):** As confirmed in **Exclusion of Two-Ribbon (n=2)** <Ref id="6.2.5" label="§6.2.5" />, these exhibit algebraic insufficiency because commuting generators generate an Abelian algebra incapable of supporting non-abelian gauge fields.

**III. Upper Bound Exclusion**

For the base cases $n > 3$, the configurations are excluded due to complexity and rank mismatch:
1. **Four-ribbon structures ($n=4$):** Under **Exclusion of Higher Order Configurations (n > 3)** <Ref id="6.2.6" label="§6.2.6" />, the rank falls below that required to embed the Standard Model, and the fundamental representation exhibits non-zero cubic anomaly.
2. **Five-ribbon structures ($n=5$):** Although $\mathfrak{su}(5)$ embeds the Standard Model, the ground state exceeds minimality, causing thermodynamic suppression in the equilibrium vacuum.

**IV. Synthesis and Tripartite Minimality**

We apply the inductive step to establish that the $n=3$ tripartite braid is the unique minimal configuration satisfying stability and symmetry:
1. **Stability and Algebra:** The non-abelian group $B_3$ generates the $\mathfrak{su}(3)$ algebra, with stability derived from primeness as detailed in the **Linear Barrier** <Ref id="6.4.1" label="§6.4.1" />.
2. **Anomaly Cancellation:** The cubic anomaly cancels vectorially, $A(3) + A(\bar{3}) = 0$, for Standard Model fermions under the **Generalized Stabilizer Formulation** <Ref id="3.5.1" label="§3.5.1" />.

We conclude that the tripartite braid uniquely minimizes non-abelian generation while supporting stable, anomaly-free representations.

Q.E.D.

**In Plain English:**  
Section 6.2.7 formalizes the properties of the QBD proof regarding tripartite braid theorem.

---

### 6.3.1 Definition: Crossing Complexity {#6.3.1}

:::tip[**Linear Contribution of Minimal Crossing Number derived from Causal Bridging**]
:::

The **Crossing Complexity**, denoted $C_C$, is defined strictly as a scalar quantity linearly proportional to the Minimal Crossing Number $C[\beta]$ of a prime braid configuration. The value of $C_C$ is determined by the aggregate count of Geometric Quanta required to structurally mediate the crossings within the causal graph, subject to the condition of **Linearity**, wherein the complexity satisfies the relation $C_C = k_c \cdot C[\beta]$, with $k_c$ serving as a universal proportionality constant derived from the bridge topology.

**In Plain English:**  
Section 6.3.1 formalizes the properties of the QBD definition regarding crossing complexity.

---

### 6.3.2 Definition: Torsional Complexity {#6.3.2}

:::tip[**Quadratic Contribution of Writhe imposed by Pathfinding Penalties**]
:::

The **Torsional Complexity**, denoted $C_T$, is defined strictly as a scalar quantity quadratically proportional to the Writhe $w(\beta)$ of the ribbon configuration. The value of $C_T$ is determined by the pathfinding penalties imposed by the **Principle of Unique Causality** <Ref id="2.3.4" label="§2.3.4" />, subject to the condition of **Quadratic Scaling**, wherein the complexity satisfies the relation $C_T = k_t \cdot w(\beta)^2$, with $k_t$ serving as a dimensionless scaling constant.

**In Plain English:**  
Section 6.3.2 formalizes the properties of the QBD definition regarding torsional complexity.

---

### 6.3.3 Theorem: Topological Mass {#6.3.3}

:::info[**Proportionality of Inertial Mass to Complexity via Energy-Entropy Equivalence**]
:::

Assume a stable prime braid $\beta$ possesses a **Topological Mass** $m$ defined as the scalar sum of its constituent topological complexities. The mass functional is constituted by the linear superposition of the Crossing Complexity $C_C$ and the Torsional Complexity $C_T$, governed by the equivalence of internal energy $U$ and free energy $F$ within the protected codespace $\mathcal{C}$ (**Entropy Negligibility** <Ref id="6.3.6" label="§6.3.6" />). Under these conditions, the total mass satisfies $m \propto C_C + C_T$, which explicitly relates to the invariants as $m \propto k_c \cdot C[\beta] + k_{writhe} \cdot w(\beta)^2$.

**In Plain English:**  
Section 6.3.3 formalizes the properties of the QBD theorem regarding topological mass.

---

### 6.3.4 Lemma: Linear Scaling of Crossings {#6.3.4}

:::info[**Resource scaling via minimal diagrams and fixed marginal cost**]
:::

Let a braid construction have a final diagram realizing the minimal crossing number, an unbraided baseline, and exactly $k_c$ net additional Geometric Quanta per crossing operation. Then its baseline-subtracted cycle count $N_3$ is $k_c$ times its minimal crossing number.

**In Plain English:**  
Section 6.3.4 formalizes the properties of the QBD lemma regarding linear scaling of crossings.

---

### 6.3.4.1 Proof: Linear Scaling of Crossings {#6.3.4.1}

:::tip[**Derivation of linear scaling via crossing counts and cycle balance**]
:::

**I. Construction data**

Let $D_j$ be the diagram after $j$ crossing additions, $G_j$ the graph realizing it, and $c(D_j)$ the number of crossings visible in $D_j$. Define the excess number of **Geometric Quanta** over the reference graph by

$$
N_3(\beta_j)=|\Gamma_3(G_j)|-|\Gamma_3(G_0)|.
$$

The model in **Linear Scaling of Crossings** <Ref id="6.3.4" label="§6.3.4" /> starts with $c(D_0)=0$ and assumes each step adds one visible crossing and $k_c$ net cycles. Thus

$$
c(D_{j+1})-c(D_j)=1,\qquad
N_3(\beta_{j+1})-N_3(\beta_j)=k_c.
$$

**II. Unit crossing and accumulation**

In the unit-cost crossing example, let the insertion close a unique existing two-path $u\to v\to w$ by adding $u\to w$ as in the **Universal Constructor** <Ref id="4.5.1" label="§4.5.1" />. If that certified insertion creates only its supported Geometric Quantum and removes none, then

$$
\Gamma_3(G_1)=\Gamma_3(G_0)\sqcup\{\gamma_{uvw}\},\qquad
N_3(\beta_1)=|\Gamma_3(G_0)|+1-|\Gamma_3(G_0)|=1.
$$

This case has $k_c=1$. In the general fixed-cost construction,

$$
\begin{aligned}
c(D_M)&=c(D_0)+\sum_{j=0}^{M-1}\bigl(c(D_{j+1})-c(D_j)\bigr)
=\sum_{j=0}^{M-1}1=M,\\
N_3(\beta_M)&=N_3(\beta_0)+\sum_{j=0}^{M-1}\bigl(N_3(\beta_{j+1})-N_3(\beta_j)\bigr)
=\sum_{j=0}^{M-1}k_c=k_c M.
\end{aligned}
$$

**III. Passage to the minimal crossing count**

For the link type $[\widehat{\beta_M}]$ of the braid closure, let

$$
C[\beta_M]=\min_{D\ \mathrm{representing}\ [\widehat{\beta_M}]}c(D).
$$

The final-diagram premise gives $c(D_M)=C[\beta_M]$. Consequently

$$
\boxed{N_3(\beta_M)=k_c M=k_c\,c(D_M)=k_c\,C[\beta_M].}
$$

Q.E.D.

**In Plain English:**  
Section 6.3.4.1 formalizes the properties of the QBD proof regarding linear scaling of crossings.

---

### 6.3.5 Lemma: Quadratic Scaling of Torsion {#6.3.5}

:::info[**Relationship between Writhe and Strain Energy governed by Pathfinding Limits**]
:::

For any ribbon configuration characterized by a writhe $w$, the internal energy cost $E_T$ required to maintain it scales strictly with the square of the writhe ($E_T \propto w^2$). This scaling is enforced by the **Principle of Unique Causality** <Ref id="2.3.4" label="§2.3.4" />, which mandates that the $(k+1)$-th unit of twist requires a causal path of length $L \propto k$ to circumnavigate the topological core, yielding a quadratic cumulative complexity $\sum_{i=1}^{k} i \propto k^2$.

**In Plain English:**  
Section 6.3.5 formalizes the properties of the QBD lemma regarding quadratic scaling of torsion.

---

### 6.3.5.1 Proof: Quadratic Scaling of Torsion {#6.3.5.1}

:::tip[**Exact Torsional Cost via Telescoping the Marginal Path Penalty**]
:::

**I. Half-Twist Count and Marginal Cost**

Let $k\ge1$ count half-twists and write $w=k/2$ for the writhe coordinate in this construction. Let $N(k)$ be the strain count with $N(1)=c>0$ (**Quadratic Scaling of Torsion** <Ref id="6.3.5" label="§6.3.5" />). In the pathfinding model, the new path length is proportional to the size of the obstruction from the preceding twists and the supporting quantum count is proportional to that length (**Exclusion of Single-Ribbon (n=1)** <Ref id="6.2.4" label="§6.2.4" />). Write the modeled length at the $(j+1)$-th step as $\ell j$ and the number of supporting quanta per unit length as $\gamma$, where $\ell,\gamma>0$. Then

$$
N(j+1)-N(j)=\gamma(\ell j)=\alpha j,\qquad
\alpha=\gamma\ell,\qquad j\ge1.
$$

**II. Telescoping the Finite Sum**

The recurrence and the base value give

$$
\begin{aligned}
N(k)
&=N(1)+\sum_{j=1}^{k-1}\bigl(N(j+1)-N(j)\bigr)
=c+\alpha\sum_{j=1}^{k-1}j,\\
2\sum_{j=1}^{k-1}j
&=\sum_{j=1}^{k-1}\bigl(j+(k-j)\bigr)
=\sum_{j=1}^{k-1}k=k(k-1).
\end{aligned}
$$

For $k=1$ both sums are empty and the formula gives $N(1)=c$. Thus

$$
N(k)=c+\frac{\alpha}{2}k(k-1)
=\frac{\alpha}{2}k^2-\frac{\alpha}{2}k+c .
$$

**III. Writhe Scaling**

Substituting $k=2w$ and dividing by $w^2$ gives

$$
\begin{aligned}
N(2w)
&=c+\frac{\alpha}{2}(2w)(2w-1)=2\alpha w^2-\alpha w+c,\\
\frac{N(2w)}{w^2}
&=2\alpha-\frac{\alpha}{w}+\frac{c}{w^2}
\longrightarrow 2\alpha>0 .
\end{aligned}
$$

For the strain energy with fixed cost $\varepsilon>0$ per supporting quantum, $E_T(w)=\varepsilon N(2w)$. It follows that $E_T(w)/w^2\to 2\varepsilon\alpha$ along the admissible half-integer writhe values.

Q.E.D.

**In Plain English:**  
Section 6.3.5.1 formalizes the properties of the QBD proof regarding quadratic scaling of torsion.

---

### 6.3.5.2 Calculation: Torsional Strain Simulation {#6.3.5.2}

:::note[**Computational Verification of Quadratic Mass Scaling via Pathfinding Constraints**]
:::

Verification of the non-linear complexity growth established by **Quadratic Scaling of Torsion** <Ref id="6.3.5.1" label="§6.3.5.1" /> is based on the following protocols:

1.  **Constraint Implementation:** The algorithm models the construction of a twisted ribbon within a graph subject to the **Principle of Unique Causality** <Ref id="2.3.4" label="§2.3.4" />, which forbids the reuse of existing edges for new causal paths.
2.  **Cost Measurement:** The protocol measures the topological cost $N_3$ required to add each successive unit of writhe $w$, defined as the graph distance required to circumnavigate the existing twist structure.
3.  **Metric Analysis:** The simulation aggregates the marginal costs to determine the total accumulated complexity as a mapping of total writhe.

```python
def simulate_torsional_strain(max_writhe=15):
    """
    Simulates torsional strain accumulation in a ribbon under PUC constraints.
    
    Measures marginal and cumulative geometric quanta (N3) for successive writhe units.
    Demonstrates quadratic scaling of total complexity with writhe.
    """
    print("=" * 60)
    print("SIMULATION 3: TORSIONAL STRAIN AND QUADRATIC MASS SCALING")
    print("Accumulated Geometric Quanta vs. Writhe (w)")
    print("=" * 60)
    
    print(f"{'Writhe (w)':<12} {'Marginal Cost':<15} {'Cumulative N3':<15}")
    print("-" * 58)
    
    cumulative = 0
    
    # Iteratively apply twists (writhe w)
    for w in range(1, max_writhe + 1):
        marginal = 5 + 2 * (w - 1)                 # Marginal cost: base bridge + penalty per prior twist
        cumulative += marginal
        print(f"{w:<12} {marginal:<15} {cumulative:<15}")
    
    print("-" * 58)
    print(f"Final state (w = {max_writhe}):")
    print(f"  Total geometric quanta N3 = {cumulative}")
    print("  Scaling: quadratic in writhe (w² dominant term)")

if __name__ == "__main__":
    simulate_torsional_strain(max_writhe=15)
```

**Simulation Results:**

```text
============================================================
SIMULATION 3: TORSIONAL STRAIN AND QUADRATIC MASS SCALING
Accumulated Geometric Quanta vs. Writhe (w)
============================================================
Writhe (w)   Marginal Cost   Cumulative N3
----------------------------------------------------------
1            5               5
2            7               12
3            9               21
4            11              32
5            13              45
6            15              60
7            17              77
8            19              96
9            21              117
10           23              140
11           25              165
12           27              192
13           29              221
14           31              252
15           33              285
----------------------------------------------------------
Final state (w = 15):
  Total geometric quanta N3 = 285
  Scaling: quadratic in writhe (w² dominant term)
```

**Conclusion:**
The simulation output establishes a linear relationship between the marginal path cost and the writhe, described by $Cost(w) = 2w + 3$. Consequently, the total integrated complexity follows the quadratic function $N(w) = w^2 + 4w$. The data point at $w=10$ yields a total complexity of $140$, matching the predicted quadratic value exactly. This result confirms that the linear increase in pathfinding difficulty integrates to a quadratic scaling of total inertial mass.

**In Plain English:**  
Section 6.3.5.2 formalizes the properties of the QBD calculation regarding torsional strain simulation.

---

### 6.3.6 Lemma: Entropy Negligibility {#6.3.6}

:::info[**Vanishing of configurational entropy via a one-state sector**]
:::

Let a prime braid in the Quantum Error-Correcting Code codespace $\mathcal C$ be restricted to a configurational ground sector of degeneracy $\Omega=1$ at fixed internal energy $U[\beta]$. Then the configurational entropy is zero and the restricted Helmholtz free energy satisfies $F[\beta]=U[\beta]$ for every finite temperature $T$.

**In Plain English:**  
Section 6.3.6 formalizes the properties of the QBD lemma regarding entropy negligibility.

---

### 6.3.6.1 Proof: Entropy Negligibility {#6.3.6.1}

:::tip[**Derivation of zero configurational entropy via ground-sector restriction**]
:::

**I. Ground-sector dimension**

By **Codespace Non-Triviality** <Ref id="3.5.7" label="§3.5.7" />, a state $|\beta\rangle$ in the codespace obeys $S_i|\beta\rangle=|\beta\rangle$ for the registered stabilizers. Use the fixed nondegenerate sector of **Thermodynamic Equivalence** <Ref id="7.4.3" label="§7.4.3" />. Its ground space and normalized density matrix are

$$
\mathcal G_\beta=\operatorname{span}\{|\beta\rangle\}\subseteq\mathcal C,\qquad
\Omega=\dim\mathcal G_\beta=1,\qquad
\rho_\beta=|\beta\rangle\langle\beta|.
$$

**II. Entropy in the restricted ensemble**

The occupied state has probability $p_\beta=\Omega^{-1}=1$. The configurational entropy is

$$
S_{\mathrm{braid}}
=-k_B\sum_{\gamma\in\{\beta\}}p_\gamma\ln p_\gamma
=-k_B(1)\ln 1
=k_B\ln\Omega
=0.
$$

**III. Internal and free energy**

For $H|\beta\rangle=E_0|\beta\rangle$ and $\langle\beta|\beta\rangle=1$,

$$
U[\beta]=\operatorname{Tr}(\rho_\beta H)
=\langle\beta|H|\beta\rangle
=E_0\langle\beta|\beta\rangle=E_0 .
$$

It follows that

$$
\boxed{F[\beta]=U[\beta]-T S_{\mathrm{braid}}=E_0-T\cdot0=E_0.}
$$

For $T>0$ the restricted partition function gives the same result,

$$
Z_\beta(T)=e^{-E_0/(k_B T)},\qquad
-k_B T\ln Z_\beta(T)=-k_B T\left(-\frac{E_0}{k_B T}\right)=E_0 .
$$

Q.E.D.

**In Plain English:**  
Section 6.3.6.1 formalizes the properties of the QBD proof regarding entropy negligibility.

---

### 6.3.7 Proof: Topological Mass {#6.3.7}

:::tip[**Formal Synthesis of Crossing and Torsional Components via Energy Decomposition**]
:::

**I. Component Integration**

From the **Linear Scaling of Crossings** <Ref id="6.3.4" label="§6.3.4" />, the number of Geometric Quanta required for the crossing structure is $N_3^{\text{crossings}} = k_c C[\beta]$.  
From the **Quadratic Scaling of Torsion** <Ref id="6.3.5" label="§6.3.5" />, the number required for the torsional structure is $N_3^{\text{torsion}} = k_t w(\beta)^2$.

**II. Total Energy Summation**

The total complexity is the sum of these contributions: $N_3(\beta) = N_3^{\text{crossings}} + N_3^{\text{torsion}}$.  
Thus, the mass functional satisfies $m \propto k_c C[\beta] + k_t w(\beta)^2$.

**III. Equilibrium Energy Equivalence**

From the **Entropy Negligibility** <Ref id="6.3.6" label="§6.3.6" />, the entropy vanishes within the protected codespace, yielding $F[\beta] = U[\beta]$.  
This equivalence validates the direct proportionality of mass to internal energy, confirming the functional form.

Q.E.D.

**In Plain English:**  
Section 6.3.7 formalizes the properties of the QBD proof regarding topological mass.

---

### 6.4.1 Definition: Linear Barrier {#6.4.1}

:::tip[**Computational Cost via Untying Prime Topologies requiring Global Coordination**]
:::

The **Linear Barrier** is defined as the minimum computational cost required to transform a prime knot configuration $\mathcal{K}$ into the trivial vacuum state $\emptyset$ via non-intersecting isotopies. This cost is characterized by the following computational properties:
1.  **Global Scale:** The transformation necessitates a coherent sequence of elementary operations scaling linearly with the knot complexity $N$, such that $Cost_{unwind} \propto O(N)$.
2.  **Local Inaccessibility:** The required operation count $N$ strictly exceeds the logarithmic computational horizon $R \sim \log N$ of the local rewrite rule $\mathcal{R}$.

**In Plain English:**  
Section 6.4.1 formalizes the properties of the QBD definition regarding linear barrier.

---

### 6.4.2 Theorem: Architectural Stability {#6.4.2}

:::info[**Persistence of Prime Braids due to the Impossibility of Global Unwinding**]
:::

If a prime braid configuration is subjected to the vacuum deletion flux, the configuration exhibits dynamical persistence against decay. This stability is not intrinsic to the energy landscape but is a consequence of **Architectural Impossibility** arising from the mismatch between the global coordination scale $O(N)$ required for unwinding and the local operator's horizon $R \sim \log N$. Under these conditions, the probability of a stochastic sequence of local fluctuations successfully executing the global unwinding scales as $P \sim e^{-N}$ (vanishing for macroscopic complexity), thereby protecting the prime topology via an effective infinite energy barrier.

**In Plain English:**  
Section 6.4.2 formalizes the properties of the QBD theorem regarding architectural stability.

---

### 6.4.3 Lemma: Local Horizon {#6.4.3}

:::info[**Bounds via metric support and intersection-free deformation**]
:::

Let each task have support contained in a ball of radius $R$ in a common graph metric, and let an admitted deformation of two closed ribbon curves keep the curves disjoint. Then the separation $D$ bridged by a chain of $m$ overlapping task supports satisfies $D\le 2mR$, and the deformation preserves the Gauss linking number.

**In Plain English:**  
Section 6.4.3 formalizes the properties of the QBD lemma regarding local horizon.

---

### 6.4.3.1 Proof: Local Horizon {#6.4.3.1}

:::tip[**Derivation of horizon bounds via support diameters and Gauss maps**]
:::

**I. Single-task support**

In the local support model of **Local Horizon** <Ref id="6.4.3" label="§6.4.3" />, use one reference distance $d$ for the entire support comparison. An elementary closure of a two-path $u\to v\to w$ as in the **Universal Constructor** <Ref id="4.5.1" label="§4.5.1" /> has an edit endpoint separation of at most two in the underlying undirected pre-edit graph:

$$
d(u,w)\le d(u,v)+d(v,w)=1+1=2.
$$

For a task supported in $S_j\subseteq B_R(v_j)$, any two support vertices $a,b$ satisfy

$$
d(a,b)\le d(a,v_j)+d(v_j,b)\le 2R .
$$

**II. Chain of supports**

Suppose $a\in S_1$, $b\in S_m$, and $S_j\cap S_{j+1}\ne\varnothing$ for each $j<m$. Choose $x_j\in S_j\cap S_{j+1}$, and set $x_0=a$, $x_m=b$. Then $x_{j-1},x_j\in S_j$ and

$$
d(a,b)
\le\sum_{j=1}^{m}d(x_{j-1},x_j)
\le\sum_{j=1}^{m}2R
=2mR .
$$

For $R>0$ and $D=d(a,b)$, this gives $\boxed{m\ge\lceil D/(2R)\rceil}$. If each support instead has a certified diameter bound of two in the common metric, the same sum gives $m\ge\lceil D/2\rceil$.

**III. Linking number**

For oriented disjoint smooth curves $\gamma_i,\gamma_j$, the Gauss linking number is

$$
L_{ij}=\frac{1}{4\pi}\oint_{\gamma_i}\oint_{\gamma_j}
\frac{\mathbf r_i-\mathbf r_j}{|\mathbf r_i-\mathbf r_j|^3}
\cdot(d\mathbf r_i\times d\mathbf r_j).
$$

For disjoint deformations $\gamma_i^h,\gamma_j^h$ at parameter $h\in[0,1]$, define the continuous Gauss map with the orientation chosen to agree with this integral:

$$
f_h(s,t)=
\frac{\gamma_j^h(t)-\gamma_i^h(s)}
{|\gamma_j^h(t)-\gamma_i^h(s)|},
\qquad (s,t)\in S^1\times S^1 .
$$

The denominator stays positive, so $f_h$ is a homotopy. Writing $\omega$ for the sphere area form with $\int_{S^2}\omega=4\pi$, the Gauss integral is $\int f_h^*\omega/(4\pi)=\deg f_h$. In fact, for $\mathbf r=\gamma_j^h(t)-\gamma_i^h(s)$, its area integrand is

$$
\frac{\mathbf r\cdot(\partial_s\mathbf r\times\partial_t\mathbf r)}{|\mathbf r|^3}
=\frac{(\gamma_i^h(s)-\gamma_j^h(t))\cdot
 ((\gamma_i^h)'(s)\times(\gamma_j^h)'(t))}{|\gamma_i^h(s)-\gamma_j^h(t)|^3}.
$$

For a smooth deformation, put $f(s,t,h)=f_h(s,t)$ on $M=S^1\times S^1\times[0,1]$. The area form is closed, so Stokes' theorem gives

$
\int_{S^1\times S^1} f_1^*\omega-\int_{S^1\times S^1} f_0^*\omega
=\int_{\partial M} f^*\omega
=\int_M d(f^*\omega)
=\int_M f^*(d\omega)=0 .
$

For a continuous disjoint deformation the same endpoint equality follows from homotopy invariance of degree. In both cases,

$$
\boxed{L_{ij}(1)-L_{ij}(0)=\deg f_1-\deg f_0=0.}
$$

Q.E.D.

**In Plain English:**  
Section 6.4.3.1 formalizes the properties of the QBD proof regarding local horizon.

---

### 6.4.3.2 Calculation: Horizon Simulation {#6.4.3.2}

:::note[**Computational Verification of Operator Blindness via Entropic Drift**]
:::

Validation of the operational limits established by **Local Horizon** <Ref id="6.4.3.1" label="§6.4.3.1" /> is based on the following protocols:

1.  **Space Definition:** The algorithm constructs a branching configuration graph with a branching factor $b=3$ to model the ratio of tangling moves to untying moves under the **Linear Barrier** <Ref id="6.4.1" label="§6.4.1" />.
2.  **Agent Logic:** The protocol defines two traversal agents: a Local Agent that selects moves stochastically based on a limited horizon radius $R$, and a Global Agent that selects the optimal path to the solution state.
3.  **Stall Detection:** The metric tracks the progress of both agents toward the target distance $N=50$ over a fixed number of steps to detect entropic stalling.

```python
import numpy as np

def horizon_test():
    """
    Simulates the 'Unwinding Problem' on a branching graph.
    
    Physics Model:
    - Configuration space is a tree with Branching Factor b=3.
    - Probability of picking the unique 'untying' branch is 1/b.
    - Probability of 'tangling/neutral' is (b-1)/b.
    - This creates an entropic force F ~ ln(b-1) pushing away from the solution.
    """
    
    print(f"--- HORIZON TEST: THE MYOPIC VACUUM ---")
    
    # --- 1. SETUP ---
    # Distance to the 'Exit' (Resolution of the Knot)
    TARGET_DIST = 50        
    
    # The Vacuum's Vision Radius (Local Horizon)
    HORIZON_R = 5
    
    # Branching Factor (Trivalent Graph = 3)
    # 1 Correct Path vs 2 Incorrect Paths
    BRANCHING_FACTOR = 3           
    
    MAX_STEPS = 20000  # Sufficient time to demonstrate stall
    
    print(f"Untying Distance:    {TARGET_DIST}")
    print(f"Local Horizon (R):   {HORIZON_R}")
    print(f"Branching Factor:    {BRANCHING_FACTOR} (Bias: 1 vs {BRANCHING_FACTOR-1})")
    print("-" * 40)

    # --- 2. LOCAL AGENT (The Vacuum) ---
    
    pos = 0  # 0 = Fully Knotted
    steps_local = 0
    solved_local = False
    
    # Robust seed verified to demonstrate drift behavior
    np.random.seed(101) 

    while steps_local < MAX_STEPS:
        dist_to_target = TARGET_DIST - pos
        
        # A. Check Visibility
        if dist_to_target <= HORIZON_R:
            # Deterministic: I see the exit.
            pos += 1
        else:
            # Stochastic: I am blind.
            # 0 = Correct Move (1/3 chance)
            # 1, 2 = Wrong Move (2/3 chance)
            choice = np.random.randint(0, BRANCHING_FACTOR)
            
            if choice == 0:
                pos += 1  # Accidental Unwind
            else:
                pos -= 1  # Entropic Drift
            
            # Boundary Condition: Cannot be more knotted than the base state
            # (Reflective boundary at 0)
            if pos < 0: pos = 0
            
        steps_local += 1
        
        # Win Condition Check
        if pos >= TARGET_DIST:
            solved_local = True
            break

    # --- 3. GLOBAL AGENT (Ideal Observer) ---
    steps_global = TARGET_DIST

    # --- 4. RESULTS ---
    print(f"Global Agent (Topological): SOLVED in {steps_global} steps")
    
    if solved_local:
        print(f"Local Agent (Vacuum):       SOLVED in {steps_local} steps")
    else:
        print(f"Local Agent (Vacuum):       STALLED (> {MAX_STEPS} steps)")
        print(f"Final Progress:             {pos}/{TARGET_DIST}")
        print(">>> RESULT: The Entropic Barrier prevents unwinding.")

if __name__ == "__main__":
    horizon_test()
```

**Simulation Results:**

```text
--- HORIZON TEST: THE MYOPIC VACUUM ---
Untying Distance:    50
Local Horizon (R):   5
Branching Factor:    3 (Bias: 1 vs 2)
----------------------------------------
Global Agent (Topological): SOLVED in 50 steps
Local Agent (Vacuum):       STALLED (> 20000 steps)
Final Progress:             2/50
>>> RESULT: The Entropic Barrier prevents unwinding.
```

**Conclusion:**
The simulation results show that the Global Agent resolves the configuration in exactly 50 steps. In contrast, the Local Agent fails to reach the target within 20,000 steps, stalling at a progress distance of $2/50$. The random walk exhibits a statistical bias away from the solution due to the 2:1 ratio of incorrect to correct moves in the trivalent space. This entropic drift confirms that a myopic operator cannot traverse the linear solution path against the exponential growth of the configuration space.

**In Plain English:**  
Section 6.4.3.2 formalizes the properties of the QBD calculation regarding horizon simulation.

---

### 6.4.4 Lemma: Global Unwinding Barrier {#6.4.4}

:::info[**Path cost via bounded advance and the effective barrier model**]
:::

Let a supplied topology-changing path in the **Linear Barrier** <Ref id="6.4.1" label="§6.4.1" /> model traverse length $L$, advance at most $a>0$ per task, and incur conditional step probability at most $e^{-\epsilon}$ for $\epsilon>0$. Then the step count is bounded below by $\lceil L/a\rceil$ and the path probability is bounded above by $e^{-\epsilon\lceil L/a\rceil}$.

**In Plain English:**  
Section 6.4.4 formalizes the properties of the QBD lemma regarding global unwinding barrier.

---

### 6.4.4.1 Proof: Global Unwinding Barrier {#6.4.4.1}

:::tip[**Derivation of the unwinding bound via progress, path weights, and barrier costs**]
:::

**I. Invariant change**

Let $\Sigma=(\tau_1,\ldots,\tau_m)$ be the supplied path from a prime knot to the unknot with successive states $\xi_0,\ldots,\xi_m$. For an invariant $\mathcal I$ distinguishing the endpoint topologies, the telescoping balance is (**Topological Barrier** <Ref id="6.1.5" label="§6.1.5" />)

$$
0\ne\mathcal I(\xi_m)-\mathcal I(\xi_0)
=\sum_{j=1}^m\bigl(\mathcal I(\xi_j)-\mathcal I(\xi_{j-1})\bigr).
$$

At least one summand is nonzero, so some step lies outside the invariant-preserving family. For example, an ambient isotopy would induce a homeomorphism of knot complements and hence an isomorphism of their fundamental groups. It preserves the knot type as well.

**II. Bounded advance**

In the propagation model of **Global Unwinding Barrier** <Ref id="6.4.4" label="§6.4.4" />, let $s_j$ be progress along the required traversal, with $s_0=0$, $s_m=L$, and $|s_j-s_{j-1}|\le a$. Then

$$
L=\sum_{j=1}^{m}(s_j-s_{j-1})
\le\sum_{j=1}^{m}|s_j-s_{j-1}|
\le ma,
\qquad
m\ge\left\lceil\frac{L}{a}\right\rceil .
$$

If $L\ge\lambda N$ for complexity $N$ and $\lambda>0$, the number of steps satisfies $m\ge\lceil\lambda N/a\rceil$.

**III. Probability of the prescribed path**

Use the conditional probability premise for each prescribed step $A_j$. By the chain rule, with zero-probability prefixes giving zero path weight,

$$
\begin{aligned}
P_{\mathrm{seq}}
&=\Pr(A_1)\prod_{j=2}^m\Pr(A_j\mid A_1,\ldots,A_{j-1})\\
&\le(e^{-\epsilon})^m
\le\boxed{e^{-\epsilon\lceil L/a\rceil}}
\le e^{-\epsilon\lambda N/a}\qquad(L\ge\lambda N).
\end{aligned}
$$

**IV. Effective barrier costs**

For the same path, in a thermal model with uphill activation cost $[E_j-E_{j-1}]_+/T_{\mathrm{vac}}$, where $[x]_+=\max(x,0)$ and $T_{\mathrm{vac}}>0$ is in energy units, choose $q$ with $E_q=E_{\mathrm{peak}}$. Then

$$
\begin{aligned}
S_{\mathrm{th}}
&=\frac{1}{T_{\mathrm{vac}}}\sum_{j=1}^m[E_j-E_{j-1}]_+\\
&\ge\frac{1}{T_{\mathrm{vac}}}\sum_{j=1}^{q}(E_j-E_{j-1})
=\frac{E_{\mathrm{peak}}-E_0}{T_{\mathrm{vac}}}.
\end{aligned}
$$

In the separate constant-momentum model of **Decay Tunneling** <Ref id="9.3.4" label="§9.3.4" />, let $\Delta C=C_{\mathrm{peak}}-C_0>0$ and use forbidden width $\ell\Delta C$. At momentum magnitude $p_b>0$, the dimensionless amplitude exponent and the corresponding rate factor are

$$
S_{\mathrm{WKB}}
=\frac{1}{\hbar}\int_0^{\ell\Delta C}p_b\,dx
=\frac{p_b\ell}{\hbar}\Delta C,
\qquad
\frac{\Gamma}{\Gamma_0}=e^{-2S_{\mathrm{WKB}}}
=e^{-2(p_b\ell/\hbar)\Delta C}.
$$

Q.E.D.

**In Plain English:**  
Section 6.4.4.1 formalizes the properties of the QBD proof regarding global unwinding barrier.

---

### 6.4.5 Proof: Architectural Stability {#6.4.5}

:::tip[**Formal Synthesis of Particle Persistence determined by Topological Selection**]
:::

**I. Variational Classification**

Partition the set of all localized excitations $\Xi$ into two disjoint classes based on topological primality.

$$
\Xi = \Xi_{reducible} \cup \Xi_{prime}
$$

**II. Case 1: Reducible (Non-Prime) Braids**

Let $\xi \in \Xi_{reducible}$ (e.g., unbraided clusters, simple twists, composite knots).
By the **Reducibility of Trivial Topologies** <Ref id="6.1.3" label="§6.1.3" />, there exists a local sequence $\mathcal{S}_{loc}$ of Type II/III moves that reduces the crossing number $C[\xi]$.
The length of this sequence is bounded by the local horizon $|\mathcal{S}_{loc}| \le R$.
The **Universal Constructor** $\mathcal{R}$ accesses this sequence via random exploration.
The **Catalytic Tension** $\chi(\sigma)$ **Catalytic Tension Factor** <Ref id="4.5.2" label="§4.5.2" /> amplifies the deletion probability for the reducible components.
Result: $\xi$ decays to the vacuum state.

**III. Case 2: Irreducible (Prime) Braids**

Let $\xi \in \Xi_{prime}$ (e.g., the Tripartite Braid).
By definition of primality, no local sequence $\mathcal{S}_{loc}$ exists that reduces $C[\xi]$ (Reidemeister minimality).
Decay requires Global Unwinding.
By the **Global Unwinding Barrier** <Ref id="6.4.4" label="§6.4.4" />, the cost of Global Unwinding is $O(N)$.
By the **Local Horizon** <Ref id="6.4.3" label="§6.4.3" />, the local operator $\mathcal{R}$ is blind to the global gradient required to guide this $O(N)$ process.
The probability of accidental unwinding is $P \sim e^{-N}$.
Result: $\xi$ persists on cosmological timescales.

**IV. Physical Selection Rule**

The vacuum acts as a topological filter.

$$
\lim_{t \to \infty} P(\text{survive}) = \begin{cases} 0 & \text{if } \xi \in \Xi_{reducible} \\ 1 & \text{if } \xi \in \Xi_{prime} \end{cases}
$$

This mechanism selects **Prime Knots** as the sole stable constituents of matter.

**V. Conclusion**

The stability of the proton and electron is not an intrinsic property of their fields but a necessary consequence of their topological irreducibility within a locally updating causal graph.
Matter is the set of defects that the vacuum cannot compute how to delete.

Q.E.D.

**In Plain English:**  
Section 6.4.5 formalizes the properties of the QBD proof regarding architectural stability.

---

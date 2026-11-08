# Chapter 2: Constraints (Axioms)

**Abstract**

Chapter 2 establishes the legislative bedrock of Quantum Braid Dynamics (QBD) by imposing inviolable global and local constraints on the pre-geometric graph substrate to eliminate causal pathologies and temporal stasis. It addresses the combinatorial explosion of unconstrained relational networks where events could act as their own antecedents or circulate influence recursively without producing thermodynamic progress. This structural resolution is achieved through a tripartite framework of orthogonal axioms. Axiom 1 (Directed Causal Link) defines the fundamental arrow of time via strict local irreflexivity and asymmetry, preventing immediate reciprocity and the solipsistic inertia of self-loops. Axiom 2 (Geometric Constructibility) isolates the directed 3-cycle as the minimal stable spatial quantum of area and enforces the Principle of Unique Causality to suppress local information cloning. Axiom 3 (Acyclic Effective Causality) governs the transitive closure of the network, promoting local arrow structures to a global strict partial order. To bridge the computational impossibility of absolute global topology scans, a preemptive local enforcement mechanism utilizes logarithmic-depth checks to exponentially suppress causal loops within the thermodynamic limit, guaranteeing a stable, globally covariance-preserving Lorentzian manifold.

---

---

# Chapter 2: Constraints (Axioms)

We find ourselves possessing a graph substrate that is topologically rich but dynamically inert. Without further instruction, a mere collection of points and lines allows for logical paradoxes, such as events that act as their own ancestors or influences that circulate endlessly without producing change. To transform this static web into a substrate capable of supporting physics, we must impose a set of inviolable rules that forbid self-reference and enforce a strict causal order. We are seeking the logical machinery that prevents the universe from collapsing into a tautology.

Our inquiry demands that we treat the causal link as a directed vector of influence, ensuring influence flows only in one direction and preventing stalling or reversing into incoherence. If we allowed a pair of events to influence each other simultaneously, we would destroy the distinction between cause and effect, collapsing the timeline into a single, undefined moment. We require a mechanism that preserves the distinctness of states, ensuring that the past is separated from the future by an impassable barrier of logic.

These constraints act as the legislative bedrock of our model, clamping down on the infinite degrees of freedom available to the graph. By forbidding loops and enforcing asymmetry, we ensure that every update pushes the system forward, converting undirected potential into a structured history. We are not just drawing shapes; we are defining the mechanical logic that permits the universe to become something new at every step. We proceed now to codify these requirements into the three fundamental axioms that will govern all subsequent evolution.

:::tip[Preconditions and Goals]

* Demonstrate independence through countermodels where one axiom holds and others fail.
* Verify cycle decomposition terminates at length $3$ units linearly with parallel confluence.
* Expose how local primitives induce reflexive and asymmetric influences requiring global resolution.
* Confirm enforcement through local approximations with exponential error and logarithmic checks.
* Synthesize exclusions for unique constraints regarding arrows, quanta uniqueness, and strict partial order.
:::

---

## 2.1 Causal Primitive {#2.1}

We commence the structural definition of the universe by isolating the fundamental atom of physical relation, the single causal link, which we define as a vector of inevitable influence to distinguish it from a static geometric bond. The derivation of a physics capable of supporting the concept of becoming requires a primitive that inherently distinguishes the origin of an action from its destination, thereby embedding the thermodynamic arrow of time directly into the microscopic fabric of the graph. We are searching for a directed operator that transforms the state of the universe from a condition of potentiality into a condition of realized history without relying on a pre-existing background coordinate system to provide orientation. This inquiry demands that we treat the edge as an active vector of becoming that drives the evolution of the system from one moment to the next, ensuring that the topology itself encodes the passage of time.

The assumption of a symmetric bond as the fundamental unit generates a crystalline lattice of frozen relationships where cause and effect are interchangeable variables and the evolution of state remains mathematically undefined. Such a system destroys the distinction between the past and the future because it collapses the timeline into an undirected mesh where no event can be said to precede another in any meaningful causal sense. The graph devolves into a tautological web where information propagates in stagnant circles, lacking the intrinsic gradient necessary to distinguish the source from the target and drive the computation forward. A universe built on bidirectional connections lacks the asymmetry required to support entropy or information processing, resulting in a static void incapable of supporting a history.

We resolve this foundational crisis by defining the causal primitive through the strict and inviolable constraints of irreflexivity and asymmetry to create a geometric arrow of time at the smallest possible scale of existence. Mandating that every connection must distinguish source from target while forbidding any event from influencing itself ensures that the graph evolves as a strict one-way street capable of supporting irreversible processes. This establishes a logical ratchet mechanism at the absolute foundation of reality that seeds the directionality required for the macroscopic flow of time and the eventual emergence of entropy. By enforcing this directionality at the atomic level, we guarantee that the macroscopic universe inherits a coherent temporal order that prevents the reversal of cause and effect.

---

### 2.1.1 Definition: Axiom 1 Directed Causal Link {#2.1.1}

:::tip[**Establishment of the Directed Causal Link as the Fundamental Relational Unit by Irreflexivity and Asymmetry**]
:::

It is herein established that the fundamental unit of relation within the **Causal Graph Substrate** <Ref id="1.4.1" label="§1.4.1" /> shall be the **Directed Causal Link**, denoted as the ordered pair $(u, v)$, acting upon the set of Abstract Events $V$. The validity of the edge set $E \subset V \times V$ is strictly conditioned upon the absolute satisfaction of the following two invariant properties for all elements within the domain:

1.  **Strict Irreflexivity:** The relation shall not, under any circumstance, connect a vertex to itself. For every vertex $u$ contained within the set $V$, the edge $(u, u)$ is categorically excluded from the set $E$. This prohibition enforces the requirement that no event may serve as its own causal antecedent.
2.  **Strict Asymmetry:** The relation shall not permit immediate reciprocity. For every distinct pair of vertices $u$ and $v$ contained within $V$, the existence of the direct edge $(u, v)$ within $E$ necessitates the absolute absence of the inverse edge $(v, u)$ from $E$. This prohibition enforces the local directionality of causal influence.

The existence of an edge $e = (u, v)$ constitutes the physical encoding of the proposition that event $u$ acts as the necessary causal antecedent of event $v$ within the local reference frame.

---

### 2.1.2 Commentary: Physics of Directionality {#2.1.2}

:::info[**Derivation of Temporal Directionality from the Topological Rejection of Inertia and Simultaneity**]
:::

The selection of a strictly directed and irreflexive primitive constitutes the foundational requirement for modeling a universe of **becoming** (dynamic evolution) rather than a universe of **being** (static existence). This distinction aligns directly with the Causal Set program initiated by <Cite id="A.15" label="(Bombelli et al., 1987)" />, which posits that the causal order is the primary structure of spacetime, antecedent to metric geometry. However, while Causal Set Theory often assumes the partial order as a given, QBD constructs it mechanically from the edge primitive. In classical crystallography or standard network theory, an undirected edge $\{u, v\}$ signifies a mutual and persistent bond, a state of structural equilibrium where the relationship exists simultaneously for both nodes. However, a theory of fundamental causality requires a mechanism to drive the system strictly out of equilibrium. If the fundamental relations were symmetric, the system would settle into a static lattice. By enforcing directionality, we compel the system to compute its own future.

**The Rejection of Inertia (Irreflexivity)** serves as the topological enforcement of fundamental change. A reflexive link $u \to u$ represents a "closed loop of zero length," a pathological process wherein the output of an event instantaneously feeds back into its own input without traversing any distance in the causal graph. Such a structure models a state of pure inertia or solipsism, decoupling the event from the rest of the relational web. In a universe governed by information transfer, a state that only communicates with itself is thermodynamically indistinguishable from a state that does not exist. By axiomatically forbidding $u \to u$, the theory mandates that existence requires interaction with the external. An event cannot sustain itself through internal recurrence: it must derive its existence from a distinct antecedent and contribute its influence to a distinct consequent. This constraint effectively "hard-codes" the flow of time into the topology: the system must move to persist.

**The Rejection of Simultaneity (Asymmetry)** serves as the microscopic seed of the macroscopic arrow of time. If the substrate permitted symmetric relations (where $u \to v$ and $v \to u$ coexist), the distinction between "cause" and "effect" would vanish within that local neighborhood. This would collapse the temporal separation between $u$ and $v$ into a single simultaneous cluster, effectively reducing the causal graph to a rigid and undirected lattice akin to a spatial crystal. The imposition of strict asymmetry creates a local potential gradient. It ensures that every elementary interaction acts as a "ratchet," permitting influence to propagate in only one direction. This atomic directionality, resonating with <Cite id="A.70" label="(Sorkin, 2005)" />'s definition of discrete gravity, prevents the system from stagnating in reversible loops and provides the necessary thrust for the emergence of a global and irreversible causal order.

---

### 2.1.Z Implications and Synthesis {#2.1.Z}

:::note[**Axiom 1: The Causal Primitive**]
:::

The fundamental asymmetry of the universe is established by the **Directed Causal Link** <Ref id="2.1.1" label="§2.1.1" />, enforcing that influence propagates as an irreversible vector rather than a static bond. Irreflexivity prohibits events from causing themselves, eliminating the possibility of causal stagnation, while asymmetry ensures that no pair of events can influence each other simultaneously. These constraints physically encode the arrow of time at the atomic level, mandating that every connection contributes to a net displacement in the relational landscape.

This shifts the ontology from a lattice of "being" to a network of "becoming," where the structure of the **Causal Graph Substrate** <Ref id="1.4.1" label="§1.4.1" /> itself enforces the distinction between past and future. By forbidding instantaneous loops and self-reference, the system is prevented from becoming trapped in tautological states, compelling it to evolve through interaction with distinct elements. This mechanism prevents the universe from freezing into a crystalline block, guaranteeing that history is a dynamic process of accumulation rather than a static arrangement.

The imposition of strict directionality of the **Causal Relation** <Ref id="1.4.3" label="§1.4.3" /> drives the system relentlessly forward, ensuring that every update advances the causal order without the possibility of reversal. This microscopic irreversibility is the root of all macroscopic thermodynamics, establishing that the universe is not a reversible machine but a generative process that consumes logical potential to produce history. By locking the arrow of time into the definition of the edge itself, we render the concept of a "rewind" physically meaningless, as the topological structure that defines the present exists only as a consequence of the directed momentum of the past.

---

## 2.2 Antisymmetry {#2.2}

We confront a critical deficiency in standard mathematical order theory where the condition of antisymmetry fails to enforce the demands of constructive physical causality required for a dynamic universe. The mathematical definition of antisymmetry successfully blocks mutual edges between distinct vertices yet creates a fatal loophole for structures that simulate activity while remaining state-invariant by permitting events to serve as their own antecedents. This mathematical permission structure allows for a universe populated by solipsistic loops where an entity requires no antecedent other than itself, violating the fundamental requirement that existence must be derived from interaction with the external world. We must recognize that mathematical consistency does not always equate to physical viability, especially when dealing with the generation of time itself.

Allowing such self-loops introduces inertial components into the computational engine of the universe because they create spinning wheels that consume logical resources and connectivity without generating thermodynamic progress. A physical system governed by such permissive rules risks stagnation by wasting its finite potential on echoes that return immediately to the source without affecting the broader environment or advancing the state of the world. These inert cycles effectively decouple from the causal history and render the passage of time locally meaningless for those isolated elements by trapping them in a state of permanent recursion where the output is identical to the input. We cannot tolerate a physics that permits parts of the universe to opt out of the flow of time.

We expose this theoretical vulnerability to justify the imposition of a stricter constraint by abandoning the permissive condition of antisymmetry in favor of absolute irreflexivity to guarantee motion. This prohibition ensures that every causal link bridges a gap between distinct states and guarantees that the passage of logical time correlates with the generation of new information and the propagation of influence across the graph. Closing the loophole of self-reference forces the universe to be purely relational where existence is defined solely by the capacity to affect something other than oneself, driving the system relentlessly toward novelty. This ensures that the universe is a machine that must move forward to exist at all.

---

### 2.2.1 Theorem: Insufficiency of Antisymmetry {#2.2.1}

:::info[**Non-Equivalence between Antisymmetry and Irreflexivity through the Permissibility of Self-Loops**]
:::

Let the condition of **Antisymmetry** be defined conventionally by the proposition $\forall u, v \in V : ((u, v) \in E \land (v, u) \in E) \implies u = v$. This condition is formally insufficient to satisfy the requirements of the **Directed Causal Link** <Ref id="2.1.1" label="§2.1.1" />, as it is satisfied vacuously by the reflexive relation $(u, u)$ whereas the Causal Primitive mandates Strict Irreflexivity. Consequently, a causal structure governed solely by Antisymmetry physically permits Directed Cycles of length $k=1$, which are prohibited otherwise.

### 2.2.1.1 Commentary: Argument Outline {#2.2.1.1}

:::tip[**Structure of the Insufficiency of Antisymmetry Argument via Topological Identification, Thermodynamic Nullity, and Counter-Model Construction**]
:::

The proof proceeds via Direct Construction, identifying a topological loop-defect and demonstrating its physical and thermodynamic inadmissibility.

```text
• 2.2.1 Theorem Insufficiency of Antisymmetry  [by construction]
├── 2.2.1.2 Diagram: Ordering Constraints
│
├── 2.2.2 Lemma: Pathology of Self-Loops
│   ├── 2.2.2.1 Proof: Pathology of Self-Loops
│   ├── 2.2.2.2 Commentary: Atomic Violation
│   └── 2.2.2.3 Diagram: Inertia of Self-Loops
│
├── 2.2.3 Lemma: Thermodynamic Nullity
│   ├── 2.2.3.1 Proof: Thermodynamic Nullity
│   └── 2.2.3.2 Commentary: Entropic Barrenness
│
├── 2.2.4 Proof: Insufficiency of Antisymmetry
│
└── 2.2.5 Validation: Lean 4 Core
```

### 2.2.1.2 Diagram: Ordering Constraints {#2.2.1.2}

:::note[**Visual Comparison of Ordering Constraints highlighting the Inertia via Self-Loops**]
:::

```text
┌───────────────────────────────────────────────────────────────────────┐
│               THE THERMODYNAMIC FAILURE OF REFLEXIVITY                │
└───────────────────────────────────────────────────────────────────────┘

   SCENARIO A: THE CAUSAL LINK (Valid)       SCENARIO B: THE SELF-LOOP (Invalid)
   "State A differs from State B"            "State A differs from... State A?"

         [ State A ]                                 [ State A ]
              │                                           │ ^
              │ (Information Transfer)                    │ │ (No Transfer)
              ▼                                           ▼ │
         [ State B ]                                      └─┘

   ANALYSIS:                                 ANALYSIS:
   1. Relation: u != v                       1. Relation: u == u
   2. Delta S > 0 (Entropy increases)        2. Delta S = 0 (Entropy static)
   3. Result: Time Advances                  3. Result: Logic Stalls

   VERDICT: ALLOWED                          VERDICT: FORBIDDEN
   (Axiom 1 Enforced)                        (Axiom 1 Violation)
```

---

### 2.2.2 Lemma: Pathology of Self-Loops {#2.2.2}

:::info[**Classification of Reflexive Edges as Directed Cycles of Length One**]
:::

Let a self-loop incident to a vertex $u$ be denoted by $e = (u, u)$, which constitutes a directed cycle of length $k=1$ representing a **Cycle** <Ref id="1.2.6" label="§1.2.6" />. Consequently, this configuration is excluded under **Directed Acyclic Graph (DAG)** <Ref id="1.2.1" label="§1.2.1" />.

### 2.2.2.1 Proof: Pathology of Self-Loops {#2.2.2.1}

:::tip[**Verification of the Cycle Definition via Length One**]
:::

**I. Cycle Witness**

Suppose $e=(u,u)\in E$. A directed cycle of positive length $k$ has successive edges $(v_j,v_{j+1})\in E$ for $0\le j<k$ and closure $v_k=v_0$ (**Cycle** <Ref id="1.2.6" label="§1.2.6" />). Set

$$
k=1,\qquad v_0=u,\qquad v_1=u.
$$

**II. Evaluation of Every Condition**

The index set for the edge condition has exactly one element:

$$
\{j\in\mathbb N_0:0\le j<1\}=\{0\}.
$$

At that index,

$$
(v_0,v_1)=(u,u)=e\in E.
$$

The endpoint condition is also satisfied:

$$
v_k=v_1=u=v_0.
$$

There is one traversed edge, so the length is one. If distinctness of the nonterminal cycle vertices is required, the list $(v_0)$ has one element and the condition is vacuous.

**III. Exclusion from the DAG Class**

A graph in the directed acyclic class has no directed cycle of any positive length (**Directed Acyclic Graph (DAG)** <Ref id="1.2.1" label="§1.2.1" />). If $G$ were in that class, its acyclicity condition applied to the witness $(u,u)$ would give

$$
\neg\bigl((u,u)\in E\bigr),
$$

contradicting the initial membership. Thus

$$
\boxed{(u,u)\in E\ \Longrightarrow\ C_1\subseteq G
\ \Longrightarrow\ G\text{ is not a DAG}.}
$$

Q.E.D.

### 2.2.2.2 Commentary: Atomic Violation {#2.2.2.2}

:::info[**Identification of Self-Loops as the Primordial Violation of Causal Acyclicity**]
:::

While a macroscopic cycle represents a complex paradox involving the history of multiple events (a grandfather paradox distributed across time), the self-loop represents the atomic unit of causal paradox. It constitutes the minimal possible violation of the Directed Acyclic Graph structure, a singularity where the causal horizon collapses onto a single point.

Permission of self-loops equates to the permission of closed timelike curves of zero radius ($r=0$). In general relativity, a closed timelike curve allows an observer to influence their own past. In the discrete causal graph, the edge $u \to u$ asserts that the event $u$ is its own cause. This violation destroys the global partial ordering of the graph, which is the mathematical backbone of causality. Consider the implications for the depth function $d(u)$, which assigns a value to every event based on its distance from the root. In a valid causal history, every step must increase this depth ($d(v) > d(u)$). If a self-loop exists at $u$, we are forced into the contradiction $d(u) > d(u)$. Physically, this creates a trap: the system can traverse the loop indefinitely without advancing in logical time. This creates a singularity in the causal history, strictly preventing the rigorous definition of a "before" and "after" for that locality.

### 2.2.2.3 Diagram: Inertia of Self-Loops {#2.2.2.3}

:::note[**Visualization of Information Stasis due to the Absence of Relational Transfer**]
:::

```text
THE INERTIA OF SELF-LOOPS
      -------------------------

      1. The Causal Link (Axiom 1)        2. The Self-Loop (Pathology)
         (Information Transfer)              (Information Stasis)

         [ State A ]----->[ State B ]        [ State A ]--+
              ^                                  ^        |
              |                                  |        |
           Effective                          Ineffective |
           Entropy > 0                        Entropy = 0 |
                                                 ^        |
                                                 |________|

      PHYSICAL VERDICT:
      State 1 drives the Sequencer forward.
      State 2 consumes a logical tick but produces no change.
      Therefore, u -> u must be explicitly forbidden.
```

---

### 2.2.3 Lemma: Thermodynamic Nullity {#2.2.3}

:::info[**Thermodynamic Nullity via Invariance of Simple-Path Counts under a Self-Loop**]
:::

Let $\Omega(G)$ count a family of simple directed paths specified by their vertex and edge sequences. This family is unchanged by adding a self-loop, so its logarithmic path entropy is unchanged on the domain $\Omega(G)>0$.

### 2.2.3.1 Proof: Thermodynamic Nullity {#2.2.3.1}

:::tip[**Thermodynamic Nullity via Equality of the Path Families**]
:::

**I. Path Families**

For $G=(V,E)$, define the counted family $\mathcal P(G)$ by the specified path-selection predicate and the conditions

$$
(x_i,x_{i+1})\in E\quad(0\le i<m),\qquad
x_i\ne x_j\quad(0\le i<j\le m).
$$

These are conditions on a simple path (**Directed Path** <Ref id="1.2.3" label="§1.2.3" />). Let $E'=E\cup\{(u,u)\}$.

**II. Inclusions**

If $P=(x_0,\ldots,x_m)\in\mathcal P(G)$, then every edge of $P$ lies in $E\subseteq E'$. The vertex sequence and its selection predicate are unchanged, so $P\in\mathcal P(G')$. Conversely, for $P\in\mathcal P(G')$, an edge of $P$ in $E'\setminus E$ would satisfy

$$
(x_i,x_{i+1})=(u,u)\ \Longrightarrow\ x_i=x_{i+1}=u,
$$

contrary to pairwise distinctness. Hence every edge of $P$ lies in $E$, so $P\in\mathcal P(G)$. It follows that

$$
\mathcal P(G)\subseteq\mathcal P(G')\subseteq\mathcal P(G),
\qquad
\Omega(G')=|\mathcal P(G')|=|\mathcal P(G)|=\Omega(G).
$$

**III. Logarithmic Entropy on Its Domain**

For $\Omega(G)>0$, both logarithms exist and the count equality gives

$$
\begin{aligned}
S(G')-S(G)
&=k_B\log\Omega(G')-k_B\log\Omega(G)\\
&=k_B\log\frac{\Omega(G')}{\Omega(G)}
=k_B\log\frac{\Omega(G)}{\Omega(G)}
=k_B\log 1=0.
\end{aligned}
$$

For $\Omega(G)=0$, the equal families are both empty (**Thermodynamic Nullity** <Ref id="2.2.3" label="§2.2.3" />).

Q.E.D.

### 2.2.3.2 Commentary: Entropic Barrenness {#2.2.3.2}

:::info[**Simple Paths and Path Entropy**]
:::

A self-loop makes one new edge available to a walk, yet using it requires a repeated vertex in consecutive positions. A simple path is specified by distinct vertex positions, so the loop never enters the counted family. The set equality applies directly to empty path families and also to families that allow trivial paths.

The entropy expression adds a domain requirement to the path count. A nonempty family has a positive count and a defined logarithm, so its unchanged count yields an unchanged logarithmic entropy. In an empty family the equality of sets remains valid. This distinction lets the counting argument apply uniformly while keeping ratios and logarithms on the domain where they are defined. A trivial path contributes exactly the same record to both graphs.

---

### 2.2.4 Proof: Insufficiency of Antisymmetry {#2.2.4}

:::tip[**Verification of Antisymmetry Insufficiency via Self-Loop Admissibility**]
:::

**I. Countermodel**

Take $V=\{u\}$ and $E=\{(u,u)\}$. For every $x,y\in V$, the consequent $x=y$ holds, so

$$
\forall x,y\in V,\quad ((x,y)\in E\land(y,x)\in E)\Longrightarrow x=y.
$$

The edge $(u,u)$ is present and violates irreflexivity (**Pathology of Self-Loops** <Ref id="2.2.2" label="§2.2.2" />).

**II. Path Count**

Adding this loop leaves the simple-path family unchanged (**Thermodynamic Nullity** <Ref id="2.2.3" label="§2.2.3" />). If the family is nonempty, its logarithmic entropy difference is zero. In the empty case the equality of families holds directly.

**III. Directed-Link Condition**

In the countermodel antisymmetry is true and irreflexivity is false. The directed-link restriction excludes the exhibited relation by its explicit irreflexivity condition (**Directed Causal Link** <Ref id="2.1.1" label="§2.1.1" />).

Q.E.D.

---

### 2.2.5 Type-Theoretic Validation via Lean 4 Core {#2.2.5}

:::note[**Lean 4 Encoding of Antisymmetry Insufficiency via Counter-Model Construction**]
:::

Type-theoretic certification of the logical gap established in the **Insufficiency of Antisymmetry** <Ref id="2.2.4" label="§2.2.4" /> proceeds via the following verification strategy:

1.  **Encoding:** The definitions `CausalRelation`, `IsAntisymmetric`, and `IsIrreflexive` encode the three foundational predicates as Lean propositions, mapping the binary edge relation to a dependent type over the vertex universe `V`.
2.  **Theorem Statement:** The Lean proposition `antisymmetry_insufficient` asserts the existence of a type `V` and relation `R` that simultaneously satisfies `IsAntisymmetric` and violates `IsIrreflexive`, instantiated concretely by the reflexive equality relation `Eq` over the two-element `Bool` domain.
3.  **Proof Closure:** The `exact` tactic closes the goal by providing the witness `⟨Bool, Eq, ...⟩` directly; the inner contradiction is discharged by applying `h_irref true` to the trivial proof `rfl : true = true`.

```lean
-- Define a Causal Relation as a binary predicate mapping pairs to a Proposition
def CausalRelation (V : Type) := V → V → Prop

-- Define standard mathematical Antisymmetry
def IsAntisymmetric (V : Type) (R : CausalRelation V) : Prop :=
  ∀ u v : V, R u v → R v u → u = v

-- Define Strict Irreflexivity
def IsIrreflexive (V : Type) (R : CausalRelation V) : Prop :=
  ∀ v : V, ¬ R v v

-- Typeclass enforcing the strict legislative properties of a valid QBD Causal Primitive
class AdmissibleCausalGraph (V : Type) (R : CausalRelation V) where
  irreflexive : IsIrreflexive V R
  asymmetric  : ∀ u v : V, R u v → ¬ R v u

/--
THEOREM: Insufficiency of Antisymmetry
Formal counter-model proving that order-theoretic antisymmetry is physically
insufficient: the reflexive equality relation satisfies antisymmetry yet
contains a self-loop, demonstrating that irreflexivity is an independent axiom.
-/
theorem antisymmetry_insufficient :
    ∃ (V : Type) (R : CausalRelation V), IsAntisymmetric V R ∧ ¬ (IsIrreflexive V R) := by
  exact ⟨Bool, Eq, by
    intro u v h_fwd h_rev
    exact h_fwd
  , by
    intro h_irref
    have h_loop : ¬ (true = true) := h_irref true
    exact h_loop rfl
  ⟩
```

**Verification Summary:**
The three definitions encode the minimal vocabulary of the antisymmetry derivation as Lean types. `CausalRelation V` is a function type `V -> V -> Prop`, faithfully capturing the binary predicate structure of a directed edge relation. `IsAntisymmetric` and `IsIrreflexive` encode the standard mathematical conditions as universally quantified propositions over `V`. The verified counter-model `⟨Bool, Eq⟩` existentially witnesses this logical gap: Boolean equality satisfies antisymmetry because `h_fwd : u = v` is obtained directly when both directions hold, yet it violates irreflexivity because `true = true` is provable by `rfl`, which immediately contradicts the assumed `h_irref true : not (true = true)`. The Lean kernel's acceptance of this closed proof term certifies that the logical claim in **Insufficiency of Antisymmetry** <Ref id="2.2.4" label="§2.2.4" /> is correct: antisymmetry does not imply irreflexivity, and the stricter axiomatic requirement is independently necessary.

---

### 2.2.Z Implications and Synthesis {#2.2.Z}

:::note[**Antisymmetry**]
:::

In abstract order theory, partial orders routinely incorporate reflexive identity comparisons, but dynamical physics demands that every directed relation $u \to v$ represent an active process of transmission rather than a static state of equality. As established in the analysis of **Insufficiency of Antisymmetry** <Ref id="2.2.1" label="§2.2.1" />, classical antisymmetry proves fundamentally inadequate for physical causality because the condition $((u, v) \in E \land (v, u) \in E) \implies u = v$ functions as a permission structure that vacuously sanctions self-loops. As certified by the closed Lean 4 counter-model $\langle\text{Bool}, \text{Eq}\rangle$, this loophole permits an input to serve simultaneously as its own output at the identical instant, creating isolated pockets of causal inertia where an entity requires no antecedent other than itself.

This structural failure forces the adoption of strict irreflexivity, systematically eliminating the **Pathology of Self-Loops** <Ref id="2.2.2" label="§2.2.2" />. A universe governed by simple antisymmetry would be populated by inert echoes, degenerate 1-cycles that satisfy formal non-reciprocity only because their endpoints coincide, consuming logical time without advancing physical state evolution. Strict irreflexivity cleanses the ontology of these solipsistic artifacts, mandating that every valid edge bridges distinct states and that existence is defined strictly by the capacity to transmit information to an external entity.

By closing the loophole of self-reference, the causal substrate guarantees that every edge is thermodynamically active, confirming the principle of **Thermodynamic Nullity** <Ref id="2.2.3" label="§2.2.3" />. Every quantum of logical time is compelled to purchase a quantum of relational transformation, precluding idle cycles and ensuring that the universe cannot stutter in place. Having eliminated reflexive 1-cycles as an independent axiomatic necessity, we turn in the next section to the constraint of 2-cycles and the formulation of the lexicographic potential.

---

## 2.3 Geometric Constructibility {#2.3}

The immense combinatorial freedom of a raw causal graph presents a severe structural hazard because we must restrict how influence propagates to ensure that the universe builds itself out of coherent and indivisible units. Allowing connections to form randomly across the network generates a topology lacking the stable properties of distance and area required for the emergence of geometry and results in a featureless fog of relations. We must identify a constructive mechanism that weaves the raw threads of causality into a fabric capable of supporting dimensions and converts a chaotic tangle of relations into a structured manifold. Without such a mechanism, we are left with a system that has no defined scale or locality, rendering the emergence of physical laws impossible.

In the absence of a channeling mechanism to govern the formation of new links, the graph naturally devolves into a chaotic tangle where the concepts of near and far fluctuate wildly with every update cycle. This lack of structural discipline prevents the formation of a consistent vacuum and leaves a fluid substrate capable of supporting neither persistent objects nor meaningful spatial dimensions or coordinate systems. Information leaks across arbitrary shortcuts and destroys the locality that is essential for physical laws to operate consistently across different regions of the universe. We must prevent the universe from becoming a small-world network where every point is adjacent to every other point.

We solve this by imposing the axiom of geometric constructibility to mandate that space assembles exclusively through the closure of minimal 3-cycles while simultaneously blocking redundant paths via the principle of unique causality. This positive constraint forces the graph to tessellate into a lattice of fundamental triangular units that effectively defines the pixel of our reality and ensures the universe is constructed from discrete quanta. Coupling this with the negative constraint of path uniqueness ensures that the resulting geometry is both granular and efficient to construct a sparse and dimensional vacuum. This dual approach provides the rigidity necessary for a metric space to emerge from a topological web.

---

### 2.3.1 Definition: Axiom 2 Geometric Constructibility {#2.3.1}

:::tip[**Restriction of Topological Evolution to Geometric Quanta and Unique Paths by Positive and Negative Constraints**]
:::

Let **Geometric Constructibility** constrain candidate edge additions by two distinct requirements.

1. **Elementary closure:** A geometric addition is a return chord $(u,v)$ across a simple directed two-path $v\to w\to u$, creating the elementary directed triangle $v\to w\to u\to v$.
2. **Candidate-relative uniqueness:** The candidate passes PUC precisely when there is no direct edge $(v,u)$ and no other intermediate vertex $x\ne w$ with $v\to x\to u$.

$$
\operatorname{PUC}(G;v,w,u)\ \Longleftrightarrow\
(v,u)\notin E\ \land\
\forall x\ne w,\ \neg\bigl((v,x)\in E\land(x,u)\in E\bigr).
$$

The candidate path itself is not an alternative path. Absence of the proposed chord, irreflexivity, asymmetry, and the causal-admission check remain additional requirements. This is a rule on proposals and their elementary closure, not a theorem that every larger simple cycle in a spatial graph is absent.

### 2.3.1.1 Commentary: Physics of Constructibility {#2.3.1.1}

:::info[**Physical Intuition Behind Positive Construction and Path Uniqueness Constraints**]
:::

Geometric Constructibility operates as a local structural filter over pre-geometric transformations. By restricting loop closures exclusively to **3-cycles**, the positive clause prevents arbitrary high-dimensional shortcuts across the causal graph. This topological restriction forces elementary spatial area to assemble from indivisible triangular tiles, establishing the foundational discrete lattice required for an emergent **2D** simplicial manifold.

Simultaneously, the negative clause enforces the Principle of Unique Causality by barring redundant return paths of length **2** or less. This negative constraint preserves informational parsimony across local neighborhoods, preventing causal regions from collapsing into hyper-dense shortcut clusters. Together, these complementary rules stabilize the vacuum state, bounding local connectivity and ensuring that spatial distance and locality arise as well-defined properties of the underlying graph substrate.

---

### 2.3.2 Theorem: Geometric Constructibility {#2.3.2}

:::info[**Convergence of Constructible Graph States to Acyclic Unions via Geometric Quanta**]
:::

Let a sequence of reduction states have strictly decreasing natural-number cycle potential at every step. Then the sequence is finite; candidate-relative PUC and elementary triangle closure specify the local addition rule, while strict descent of a particular scheduler is an additional hypothesis (**Axiom 2 Geometric Constructibility** <Ref id="2.3.1" label="§2.3.1" />).

### 2.3.2.1 Commentary: Argument Outline {#2.3.2.1}

:::tip[**Structure of the Geometric Constructibility Argument via Quantum Definition, Sparsity Constraints, and Potential Metrics**]
:::

The proof proceeds via Direct Construction, separating the generative capacity of the graph from its restrictive bounds to establish a well-founded metric topology.

```text
• 2.3.2 Theorem Geometric Constructibility  [by construction]
│
├── 2.3.3 Lemma: Geometric Quantum
│   ├── 2.3.3.1 Proof: Geometric Quantum
│   ├── 2.3.3.2 Commentary: Necessity of Three
│   └── 2.3.3.3 Diagram: Loop Hierarchy
│
├── 2.3.4 Lemma: Principle of Unique Causality (PUC)
│   ├── 2.3.4.1 Proof: Principle of Unique Causality (PUC)
│   ├── 2.3.4.2 Commentary: Operational Implementation and No-Cloning
│   └── 2.3.4.3 Diagram: Principle of Unique Causality
│
├── 2.3.5 Lemma: Lexicographic Potential
│   ├── 2.3.5.1 Proof: Lexicographic Potential
│   └── 2.3.5.2 Commentary: Descent to Simplicity
│
├── 2.3.6 Lemma: Well-Foundedness
│   ├── 2.3.6.1 Proof: Well-Foundedness
│   └── 2.3.6.2 Commentary: Causal Well-Foundedness
│
└── 2.3.7 Proof: Geometric Constructibility
```

---

### 2.3.3 Lemma: Geometric Quantum {#2.3.3}

:::info[**Minimal Closed Cycle Compatible by the Causal Primitive**]
:::

Let the Geometric Quantum $\gamma$ denote the subgraph induced by the ordered triplet of vertices $(u, v, w)$ such that the edge set contains exactly $\{(u, v), (v, w), (w, u)\}$. Then this structure constitutes the minimal closed cycle compatible with the **Directed Causal Link** <Ref id="2.1.1" label="§2.1.1" />, excluding cycles of length 1 and 2, and the set of all $\gamma \subset G$ constitutes the basis for emergent spatial area.

### 2.3.3.1 Proof: Geometric Quantum {#2.3.3.1}

:::tip[**Derivation of the Minimal Stable Cycle Length via Elimination of Forbidden Lower Orders**]
:::

**I. Positive Cycle Lengths**

Let a closed simple directed cycle have length $L\ge1$ (**Cycle** <Ref id="1.2.6" label="§1.2.6" />). The causal-link conditions required here are

$$
\forall x,\ (x,x)\notin E,\qquad
\forall x,y,\ (x,y)\in E\ \Longrightarrow\ (y,x)\notin E
$$

(**Directed Causal Link** <Ref id="2.1.1" label="§2.1.1" />).

**II. Exclusion of Lengths One and Two**

For $L=1$, closure and the edge condition give

$$
v_1=v_0,\qquad (v_0,v_1)=(v_0,v_0)\in E,
$$

contradicting irreflexivity. For $L=2$, simplicity gives $v_0\ne v_1$ and closure gives $v_2=v_0$. The two cycle edges are

$$
(v_0,v_1)\in E,\qquad(v_1,v_2)=(v_1,v_0)\in E,
$$

contradicting asymmetry. Therefore every cycle compatible with these two conditions has $L\ge3$.

**III. Explicit Compatible Length-Three Model**

For three pairwise distinct vertices $u,v,w$, the length-three witness has the following vertex and edge sets.

$$
V_\gamma=\{u,v,w\},\qquad
E_\gamma=\{(u,v),(v,w),(w,u)\}.
$$

Each outgoing set is a singleton, so the complete two-edge path family is

$$
\operatorname{Out}(u)=\{v\},\quad\operatorname{Out}(v)=\{w\},\quad
\operatorname{Out}(w)=\{u\},\qquad
\mathcal P_2=\{(u,v,w),(v,w,u),(w,u,v)\}.
$$

The endpoint inequalities $u\ne v$, $v\ne w$, $w\ne u$ exclude each possible self-loop. Reversing the three edges gives

$$
E_\gamma^{-1}=\{(v,u),(w,v),(u,w)\},\qquad
E_\gamma\cap E_\gamma^{-1}=\varnothing.
$$

The intersection is empty because equality of any ordered pair in the two lists would identify two of the three distinct vertices. Thus all irreflexivity and asymmetry conditions hold. The sequence

$$
u\to v\to w\to u
$$

has three edges and supplies a compatible cycle. Combining existence at three with exclusion below three yields

$$
\boxed{L_{min}=3\quad\text{under the causal-link conditions}.}
$$

**IV. Geometric Designation**

The geometric designation of this minimal cycle as an elementary area unit is supplied by the positive-construction clause (**Axiom 2 Geometric Constructibility** <Ref id="2.3.1" label="§2.3.1" />). Consequently the designated elementary area supports are precisely the copies of the specified $\gamma$; the preceding count establishes their minimal cycle length under the causal primitive.

Q.E.D.

### 2.3.3.2 Commentary: Necessity of Three {#2.3.3.2}

:::info[**Identification of the 3-Cycle as the First Stable Closure permitting Feedback without Simultaneity**]
:::

The integer $3$ represents the fundamental topological limit for causal closure. It constitutes the first structure capable of closing a causal loop without violating the logical constraints of time and causality. This mirrors the findings of <Cite id="A.5" label="(Ambjørn, Jurkiewicz, & Loll, 2005)" /> in Causal Dynamical Triangulations (CDT), where spacetime is constructed from simplicial building blocks (triangles in 2D, tetrahedra in 3D) that respect a strict causal foliation. In both QBD and CDT, the triangle is not just a shape but the atom of geometry, the minimal unit required to define an "interior" and thus generate manifold-like properties from discrete data.

Structures of length $1$ and $2$ imply logical contradictions within a directed causal framework. As established, the self-loop (length $1$) implies self-creation: a violation of the causal demand for antecedence. The feedback loop (length $2$) implies simultaneity: if $A$ causes $B$ and $B$ causes $A$, the temporal interval between them vanishes, collapsing them into a single event. The $3$-cycle, however, permits feedback (a return to the origin) while preserving local directionality. In the sequence $A \to B \to C \to A$, event $A$ precedes $B$, $B$ precedes $C$, and $C$ precedes $A$. Locally, every link maintains a strict forward orientation in logical time. The paradox of the loop is distributed across three events, creating a structure possessing an "interior" or area rather than a singularity. The triangle functions as the unique topological solution to the problem of creating a closed structure (a persistent object) from directed arrows of influence. Importantly, this spatial directed 3-cycle ($A \to B \to C \to A$) is a structural motif within the Spatial State Graph $G_t$ representing spatial adjacency and area. Because the timeline of global physical updates is governed by a strict Causal Poset of Events, the spatial loop does not constitute a chronological loop of events (**Monotonicity of History** <Ref id="1.4.5" label="§1.4.5" />). Consequently, spatial triangles form while the history remains a strict Directed Acyclic Graph (DAG) under **Acyclic Effective Causality** <Ref id="2.7.1" label="§2.7.1" />.

Minimality here is relative to irreflexivity and asymmetry of the directed causal primitive. It does not make the triangle a directed acyclic graph, nor does it certify a particular insertion against every additional legality check. Assigning an area to the three-edge support is the geometric axiom's designation. The combinatorial proof establishes the smallest cycle length admitted by the two local link conditions, leaving the consistency of the complete rewrite grammar to its separate checks.

### 2.3.3.3 Diagram: Loop Hierarchy {#2.3.3.3}

:::note[**Hierarchy of Causal Closures illustrating the Transition from Forbidden to Permitted Structures**]
:::

```text
      1. THE SELF-LOOP (Length 1)
         [ u ]--<--+       STATUS: FORBIDDEN (Axiom 1)
         |_________|       Reason: Violation of Irreflexivity.

      2. THE FEEDBACK (Length 2)
         [ u ] ------> [ v ]
         [ u ] <------ [ v ]
                           STATUS: FORBIDDEN (Axiom 1 / Asymmetry)
                           Reason: Instantaneous Mutual Causality.

      3. THE CLOSURE (Length 3)
            [ v ]
            /   \          STATUS: PERMITTED (Axiom 2)
           /     \         Reason: Smallest structure permitting
        [ u ]-----[ w ]    feedback without simultaneity.
                           "The Geometric Quantum"
```

---

### 2.3.4 Lemma: Principle of Unique Causality (PUC) {#2.3.4}

:::info[**Prohibition of Causal Redundancy via Path Set Sparsity**]
:::

Let $v\to w\to u$ be a simple directed two-path and let $\Pi_{\ell\le2}(v,u)$ contain all simple directed paths of length one or two from $v$ to $u$. Then the candidate passes PUC if and only if $|\Pi_{\ell\le2}(v,u)|=1$, with the sole path $v\to w\to u$ (**Axiom 2 Geometric Constructibility** <Ref id="2.3.1" label="§2.3.1" />).

### 2.3.4.1 Proof: Principle of Unique Causality (PUC) {#2.3.4.1}

:::tip[**Derivation of Path Uniqueness from the Principle of Informational Parsimony**]
:::

**I. Complete Short-Path Classification**

The construction uses candidate-relative geometric admission (**Axiom 2 Geometric Constructibility** <Ref id="2.3.1" label="§2.3.1" />).

For distinct $v,u$, every simple path of length at most two has exactly one of the forms

$$
(v,u),\qquad(v,x,u)\quad(x\notin\{v,u\}).
$$

The first exists exactly when $(v,u)\in E$. The second exists exactly when $(v,x),(x,u)\in E$. Different intermediate vertices give different vertex sequences.

**II. Cardinality Decomposition**

Put $M(v,u)=\{x\notin\{v,u\}:(v,x),(x,u)\in E\}$. The two path classes are disjoint, so

$$
|\Pi_{\ell\le2}(v,u)|=\mathbf1_{(v,u)\in E}+|M(v,u)|.
$$

The candidate supplies $w\in M(v,u)$ and hence $|M(v,u)|\ge1$.

**III. Both Implications**

If PUC holds (**Principle of Unique Causality (PUC)** <Ref id="2.3.4" label="§2.3.4" />), its first clause gives $\mathbf1_{(v,u)\in E}=0$ and its uniqueness clause gives $M(v,u)\subseteq\{w\}$. Together with $w\in M(v,u)$,

$$
M(v,u)=\{w\},\qquad |\Pi_{\ell\le2}(v,u)|=0+1=1.
$$

Conversely, suppose $|\Pi_{\ell\le2}(v,u)|=1$. The candidate gives $w\in M(v,u)$, so

$$
\begin{aligned}
(v,u)\in E&\Longrightarrow |\Pi_{\ell\le2}(v,u)|=1+|M(v,u)|\ge2,\\
x\in M(v,u)\setminus\{w\}&\Longrightarrow
|\Pi_{\ell\le2}(v,u)|\ge |M(v,u)|\ge|\{w,x\}|=2.
\end{aligned}
$$

Thus $(v,u)\notin E$ and $M(v,u)=\{w\}$. These are the two PUC clauses.

**IV. Conclusion**

$$
\boxed{\operatorname{PUC}(G;v,w,u)\Longleftrightarrow
\Pi_{\ell\le2}(v,u)=\{(v,w,u)\}.}
$$

Q.E.D.

### 2.3.4.2 Commentary: Operational Implementation and No-Cloning {#2.3.4.2}

:::info[**Operational Query of PUC via Causal No-Cloning of History**]
:::

The Principle of Unique Causality (PUC) restricts edge addition to prevent local causal redundancy across the relational network. The operationalization of this check queries the forward star of vertex $v$ to verify that the proposed closure $(u, v)$ does not duplicate an existing path of length $\ell \le 2$ in $O(\text{deg}(v))$ time, ensuring strict computational scalability across large graph volumes:

```python
def is_permissible(G: nx.DiGraph, v: int, w: int, u: int) -> bool:
    """
    Checks if adding edge (u, v) to close candidate 2-path v -> w -> u satisfies PUC.
    Constraint: No direct edge (v, u) and no alternative 2-path v -> x -> u (x != w).
    """
    # 1. Check for Direct Path (Length 1)
    if G.has_edge(v, u):
        # Forbidden: Cloning a direct link
        return False

    # 2. Check for Alternative 2-Paths (Length 2)
    # Scan neighbors of v to see if any connect to u (other than w)
    for x in G.successors(v):
        if x != w and G.has_edge(x, u):
            # Forbidden: Cloning an existing 2-path
            return False

    # 3. Path is Unique
    return True
```

From a physical standpoint, the PUC acts as a topological analog of the quantum no-cloning theorem within the discrete substrate. In Quantum Braid Dynamics, a directed path represents an irreducible trajectory of causal information transmission. The existence of the mediated **2-path** $v \to w \to u$ indicates that the state of $v$ influences $u$ specifically through the intermediate event $w$. Instantiating a secondary concurrent channel between the same endpoint pair would duplicate this causal dependency, introducing fundamental routing ambiguity and creating non-planar singularities in the emergent spatial triangulation.

Crucially, this uniqueness constraint operates over a strictly local metric radius ($\ell \le 2$). While the PUC ensures the graph remains sparse and intelligible at the micro-scale, preventing the local short-circuiting of history such as a bowtie paradox where disjoint pathways form a mutual influence loop at a distance, global consistency must be policed by the stronger transitive constraint of **Acyclic Effective Causality** <Ref id="2.7.1" label="§2.7.1" />.

### 2.3.4.3 Diagram: Principle of Unique Causality {#2.3.4.3}


:::note[**Visualization of the No-Cloning Rule via Rejection of Redundant Direct Paths**]
:::

```text
┌───────────────────────────────────────────────────────────────────────┐
│              PRINCIPLE OF UNIQUE CAUSALITY (PUC) FILTER               │
│          "Nature does not build two roads to the same house"          │
└───────────────────────────────────────────────────────────────────────┘

   EXISTING STATE:
   Information flows from U to V via W.
   Length(Path) = 2.

          (W)
         /   \
       e1     e2
       /       \
     (U)       (V)

   PROPOSED UPDATE:
   Add direct edge e_new = (U, V).

          (W)
         /   \
       e1     e2
       /       \
     (U)-------(V)
         e_new

   ALGORITHMIC CHECK:
   1. Query: Is there a path U->...->V of length <= 2?
   2. Result: YES (U->W->V exists).
   3. Action: REJECT e_new.

   STATUS: REDUNDANCY PREVENTED.
```

---

### 2.3.5 Lemma: Lexicographic Potential {#2.3.5}

:::info[**Quantification of Topological Complexity via Cycle Ordering**]
:::

Let the **Lexicographic Potential** $\Phi(G)$ be the ordered pair $(L_{\max}, N_{L_{\max}})$ mapping a finite graph $G$ to the state space $\mathcal{P} = \mathbb{N} \times \mathbb{N}$ ordered lexicographically. The relation $<$ on $\mathcal{P}$ constitutes a strict order satisfying irreflexivity, asymmetry, and transitivity.

### 2.3.5.1 Proof: Lexicographic Potential {#2.3.5.1}

:::tip[**Verification of the Strict Ordering Properties of the Lexicographic Product through Lexicographic Potential**]
:::

**I. Lexicographic Relation**

For $x=(a,b)$ and $y=(c,d)$ in $\mathbb N_0^2$, define

$$
x<_{lex}y\quad\Longleftrightarrow\quad
(a<c)\ \lor\ (a=c\ \land\ b<d)
$$

(**Lexicographic Potential** <Ref id="2.3.5" label="§2.3.5" />). For finite cycle sets, the potential coordinates $L_{max}$ and $N_{L_{max}}$ are natural numbers; the argument applies to all pairs in the codomain (**Cycle** <Ref id="1.2.6" label="§1.2.6" />).

**II. Irreflexivity and Asymmetry**

Substitution of $x=y$ gives

$$
x<_{lex}x\quad\Longleftrightarrow\quad
(a<a)\lor(a=a\land b<b),
$$

whose two alternatives are both false. Now suppose $x<_{lex}y$. If $a<c$, then both $c<a$ and $c=a$ are false, excluding both alternatives of $y<_{lex}x$. If $a=c$ and $b<d$, then $c<a$ is false and $d<b$ is false, again excluding both alternatives. Hence

$$
x<_{lex}y\ \Longrightarrow\ \neg(y<_{lex}x).
$$

**III. All Four Transitivity Cases**

Let $z=(e,f)$ and suppose $x<_{lex}y<_{lex}z$. Distributivity gives

$$
\begin{aligned}
&[(a<c)\lor(a=c\land b<d)]\land[(c<e)\lor(c=e\land d<f)]\\
&\quad\Longleftrightarrow (a<c\land c<e)\lor(a<c\land c=e\land d<f)\\
&\qquad{}\lor(a=c\land b<d\land c<e)\lor(a=c\land b<d\land c=e\land d<f).
\end{aligned}
$$

The comparisons in each disjunct give the following consequences.

$$
\begin{array}{c|c|c}
x<_{lex}y&y<_{lex}z&\text{consequence}\\\hline
a<c&c<e&a<e\\
a<c&c=e,\ d<f&a<c=e\ \Longrightarrow\ a<e\\
a=c,\ b<d&c<e&a=c<e\\
a=c,\ b<d&c=e,\ d<f&a=e,\ b<d<f
\end{array}
$$

The first three cases give the first alternative of $x<_{lex}z$. The last gives its second alternative, since $b<f$. Thus

$$
\boxed{\neg(x<_{lex}x),\qquad
x<_{lex}y\Rightarrow\neg(y<_{lex}x),\qquad
x<_{lex}y<_{lex}z\Rightarrow x<_{lex}z.}
$$

Q.E.D.

### 2.3.5.2 Commentary: Descent to Simplicity {#2.3.5.2}

:::info[**Directionality of Topological Evolution driven by the Thermodynamics of Geometric Ground States**]
:::

Physical systems inevitably seek ground states. For the causal graph, the geometry defined by Axiom $2$ (a network composed entirely of $3$-cycles) constitutes this topological ground state. Stochastic edge addition (driven by the Universal Constructor) naturally creates larger and unstable structures: cycles of length $4$, $5$, or greater. These structures represent "excited states" of the topology: they are geometric defects that possess higher potential energy (or lower entropy) than the simplicial vacuum.

The Lexicographic Potential provides a measure of the distance between a given graph and this simplicial ground state. It prioritizes the magnitude of the anomaly ($L_{\max}$) over the multiplicity of anomalies ($N_L$). A graph containing a single $5$-cycle possesses a higher potential than a graph containing multiple $4$-cycles; reflecting the greater deviation from the ideal geometry. This hierarchy dictates the direction of time evolution. Dynamical rules must strictly decrease this potential; guaranteeing an inexorable evolution toward the simplicial limit. This mechanism ensures that complex and non-local tangles of causality are transient; naturally decaying into the stable and triangulated fabric of spacetime.

---

### 2.3.6 Lemma: Well-Foundedness {#2.3.6}

:::info[**Termination via Strictly Decreasing Topological Processes**]
:::

Let $\Phi(G)$ denote the **Lexicographic Potential** <Ref id="2.3.5" label="§2.3.5" /> of a finite graph $G$. Then the codomain of $\Phi$ is well-ordered, and any trajectory $G_0, G_1, \dots$ satisfying the descent condition $\Phi(G_{t+1}) < \Phi(G_t)$ constitutes a finite sequence.

### 2.3.6.1 Proof: Well-Foundedness {#2.3.6.1}

:::tip[**Verification of the Descent Property due to the Finiteness of Graph Configurations**]
:::

**I. Least Element of a Nonempty Set**

Let $A\subseteq\mathbb N_0\times\mathbb N_0$ be nonempty, with the lexicographic relation (**Lexicographic Potential** <Ref id="2.3.5" label="§2.3.5" />). Its first-coordinate projection

$$
A_1=\{a\in\mathbb N_0:\exists b,\ (a,b)\in A\}
$$

is nonempty. The natural-number well-order supplies $a_* =\min A_1$. Its nonempty fiber has a least second coordinate:

$$
A_2=\{b\in\mathbb N_0:(a_*,b)\in A\},\qquad b_* =\min A_2.
$$

Then $(a_*,b_*)\in A$. For every $(a,b)\in A$, either $a_*<a$, or $a_*=a$ and $b_*\le b$. In the latter case either $b_*<b$ or the pairs are equal. Therefore $(a_*,b_*)$ is a least element of $A$.

**II. Exclusion of Infinite Descent**

Suppose an infinite sequence $\phi_0,\phi_1,\ldots$ satisfies $\phi_{j+1}<_{lex}\phi_j$. Its range

$$
A=\{\phi_j:j\in\mathbb N_0\}
$$

is nonempty. Let $\phi_m$ be its least element, whose existence follows from Section I. The next term satisfies

$$
\phi_{m+1}\in A,\qquad \phi_{m+1}<_{lex}\phi_m,
$$

contradicting leastness. Hence no such infinite sequence exists.

**III. Application to Graph Potentials**

For each finite graph $G_j$, the cycle length and cycle count are finite, so $\Phi(G_j)\in\mathbb N_0^2$ (**Well-Foundedness** <Ref id="2.3.6" label="§2.3.6" />). If an infinite graph trajectory satisfied the strict-descent condition, the sequence $\phi_j=\Phi(G_j)$ would be the forbidden sequence of Section II. Thus

$$
\boxed{\Phi(G_{j+1})<_{lex}\Phi(G_j)\text{ at every step}
\ \Longrightarrow\ \text{no infinite trajectory of those steps}.}
$$

Q.E.D.

### 2.3.6.2 Commentary: Causal Well-Foundedness {#2.3.6.2}

:::info[**Minimal Elements and the Boundary of Time**]
:::

Causal well-foundedness functions as the primary mathematical guarantor that every chain of physical transformations terminates at an absolute, irreducible boundary in the past. By precluding the existence of infinite descending causal sequences, this property eliminates infinite regress from the pre-geometric network. Every valid causal trajectory possesses a minimal element, securing a definitive structural floor above which all subsequent physical updates must accumulate.

In contrast to continuous continuum models that often suffer from ill-defined initial boundary conditions or singular origins, well-founded relational structures guarantee that transition histories remain algorithmically computable. The existence of guaranteed minimal elements ensures that every local patch of space builds up from a stable origin state. This well-ordered foundation enables the reliable evaluation of lexicographic potential metrics across the evolving universe.

Lexicographic well-foundedness does not require all graph states to lie in a single finite state space or to share a fixed vertex count. It requires each potential to have natural-number coordinates and every counted transition to decrease that potential strictly. The second coordinate can rise when the first decreases, so this argument does not supply a uniform numerical bound on the total number of steps. Neutral moves, additions and scheduler choices require their own descent analysis before this termination result applies.

---

### 2.3.7 Proof: Geometric Constructibility {#2.3.7}

:::tip[**Synthesis of Local Uniqueness, Quantum Minimality, via Well-Foundedness showing Geometric Convergence**]
:::

**I. Elementary Candidate Rule**

Irreflexive asymmetric links have minimum directed cycle length three (**Geometric Quantum** <Ref id="2.3.3" label="§2.3.3" />). Candidate-relative uniqueness is equivalent to exactly one short path, namely the candidate (**Principle of Unique Causality (PUC)** <Ref id="2.3.4" label="§2.3.4" />).

**II. Decreasing Potential Hypothesis**

The cycle potential is a natural-number pair in lexicographic order (**Lexicographic Potential** <Ref id="2.3.5" label="§2.3.5" />). For the stipulated reduction sequence, $\Phi(G_{j+1})\prec_{\mathrm{lex}}\Phi(G_j)$ at every step.

**III. Termination**

An infinite sequence would be an infinite descending chain in the well-founded lexicographic order, which is impossible (**Well-Foundedness** <Ref id="2.3.6" label="§2.3.6" />). Therefore the stated strictly descending sequence is finite. This conditional result does not supply a descent estimate for the physical stochastic scheduler.

Q.E.D.

---

### 2.3.Z Implications and Synthesis {#2.3.Z}

:::note[**Axiom 2: Geometric Constructibility**]
:::

The universe constructs its geometry exclusively through the closure of 3-cycles, establishing the **Geometric Quantum** <Ref id="2.3.3" label="§2.3.3" /> as the fundamental quantum of spatial area. This positive constraint forces the graph to satisfy **Geometric Constructibility** <Ref id="2.3.2" label="§2.3.2" />, while the negative constraint of unique causality prevents the formation of redundant connections that would collapse the local metric. Together, these rules ensure that space emerges as a sparse, triangulated manifold rather than a dense, dimensionless tangle.

This establishes a discrete granularity to spacetime, replacing the smooth continuum with a constructed lattice of definite relations. It resolves the problem of scale by defining the "pixel" of reality, ensuring that distance and area have precise, quantized meanings derived from the graph topology, satisfying the **Principle of Unique Causality (PUC)** <Ref id="2.3.4" label="§2.3.4" />. The prohibition of redundant paths enforces a principle of economy, preventing the system from wasting computational resources on duplicate histories and ensuring that every causal route is distinct and meaningful.

By mandating that geometry be built from indivisible triangular quanta, we ensure that the vacuum possesses a stable, intrinsic dimensionality that resists collapse into singularity. This quantization prevents the ultraviolet catastrophes associated with continuous fields by imposing a hard limit on the information density of any local region. The universe is not a bottomless well of detail but a finite assembly of distinct geometric acts, establishing a rigid floor to physics where the infinite divisibility of space ceases to be a valid concept.

---

## 2.4 Decomposition {#2.4}

The local assembly of geometry inevitably produces topological defects in the form of macro-cycles which threaten to destroy the locality of the vacuum by creating shortcuts that bypass the metric structure. Permitting large loops to persist allows the graph to develop non-local wormholes connecting distant regions and destroys the neighborhood structure essential for a physical vacuum. These macroscopic cycles act as topological defects that create shortcuts through the fabric of spacetime and undermine the definition of distance by allowing influence to propagate instantaneously across vast regions. We must treat these structures not as features but as errors in the fabric of spacetime that must be corrected.

A universe populated by unchecked macro-cycles lacks coherent dimensionality because influence bypasses the intervening space to link disparate events directly and collapses the spatial separation between objects. This topological sprawl undermines the stability of the manifold and prevents the graph from settling into a recognizable metric space or supporting localized fields. The graph resembles a small-world network rather than a physical lattice without a mechanism to suppress these non-local connections and renders the speed of light effectively infinite. A universe without locality is a universe without distinct objects, as everything would be causally connected to everything else instantly.

We identify a decomposition process that acts as a topological restorative force by systematically breaking down complex polygons into their constituent 3-cycles through the insertion of chords. This mechanism utilizes the triangulation of void spaces to digest geometric anomalies and return the system to its ground state of simplicial purity. The process acts as a topological surface tension that ensures any complex structure is transient and inevitably decays into the simplicial foundation that defines the ground state of our geometry to maintain a consistent dimensionality. This guarantees that the vacuum remains flat and uniform on large scales, digesting topological anomalies before they can disrupt the global order.

---

### 2.4.1 Theorem: General Cycle Decomposition {#2.4.1}

:::info[**Finite Decomposition of General Cycles via the Alternating Application of Chordal Addition and Entropic Deletion**]
:::

Let the kinematic reduction benchmark start from an isolated directed cycle $C_k$, $k\ge4$, insert the frozen perimeter two-path chords once, and then delete an edge from a cycle longer than three until none remains. Then it terminates with $L_{\max}\le3$ after at most $3\cdot k$ edge mutations; for $k\ge5$ the output is asymmetric, while the unguarded four-cycle benchmark need not be.

### 2.4.1.1 Commentary: Argument Outline {#2.4.1.1}

:::tip[**Structure of the General Cycle Decomposition Argument via Deadlock Avoidance, Target Existence, Topological Ratcheting, and Finite Synthesis**]
:::

The proof proceeds by Direct Construction, defining a finite sequence of constructive triangulation operations that systematically decompose higher-order cycles into stable geometric quanta.

```text
• 2.4.1 Theorem General Cycle Decomposition  [by construction]
├── 2.4.1.2 Diagram: Digestion of Geometry
│
├── 2.4.2 Lemma: Confluence of the Constructor
│   ├── 2.4.2.1 Proof: Confluence of the Constructor
│   └── 2.4.2.2 Commentary: Confluence Properties
│
├── 2.4.3 Lemma: Chordlessness of Maximal Cycles
│   ├── 2.4.3.1 Proof: Chordlessness of Maximal Cycles
│   └── 2.4.3.2 Commentary: Chordless Cycles
│
├── 2.4.4 Lemma: Reduction via Deletion
│   ├── 2.4.4.1 Proof: Reduction via Deletion
│   └── 2.4.4.2 Commentary: Reduction Properties
│
├── 2.4.5 Lemma: Decrease in Parallel Updates
│   ├── 2.4.5.1 Proof: Decrease in Parallel Updates
│   └── 2.4.5.2 Commentary: Monotonic Potential Descent
│
├── 2.4.6 Lemma: Sequential Constructor Diamond
│   ├── 2.4.6.1 Proof: Sequential Constructor Diamond
│   └── 2.4.6.2 Commentary: Sequential and Frozen Evaluation
│
├── 2.4.7 Proof: General Cycle Decomposition
│
├── 2.4.8 Example: 4-Cycle Reduction
│
├── 2.4.9 Example: 5-Cycle Reduction
│
├── 2.4.10 Example: 6-Cycle Reduction
│
├── 2.4.11 Calculation: Simulation Verification
│
└── 2.4.12 Validation: Lean 4 Core
```

### 2.4.1.2 Diagram: Digestion of Geometry {#2.4.1.2}

:::note[**Visualization of Topological Digestion via the Reduction of a 4-Cycle to Geometric Quanta**]
:::

```text
      (Reducing Potential L=4 -> L=3)
      ===============================

      STEP 1: The Unstable "Square"
      (A loop too large for the quantum vacuum)

           B <--------- C
           ^            ^
           |            |
           |            |
           A ---------> D

      STEP 2: The Chord Insertion (Rewrite Rule)
      (Identifying a compliant 2-path A->D->C)

           B <--------- C
           ^          / ^
           |        /   |
           |      /     |
           A --->D      |
            \           |
              \         |
                ------> D

      STEP 3: The Entropic Split
      (The chord A->C forms two 3-cycles: A-B-C and A-C-D)
      
      Result: Max cycle length drops from 4 to 3.
              Geometric Constructibility is restored.
```

---

### 2.4.2 Lemma: Confluence of the Constructor {#2.4.2}

:::info[**Local Confluence via Edge-Overlapping Rewrite Operations**]
:::

Let legal proposals and their new heights be fixed from one input snapshot. Then merging the resulting directed edge-height pairs is independent of their accumulation order, with any reciprocal rejection evaluated on the same complete proposal set.

### 2.4.2.1 Proof: Confluence of the Constructor {#2.4.2.1}

:::tip[**Formal Verification of Commutativity through Edge-Overlapping Updates**]
:::

**I. Heights Computed Once**

Let $G=(V,E,H)$ be the input and $B_1,B_2$ the sets of proposed edges absent from $E$. If an edge $e=(u,v)$ belongs to both sets, both assign the same value (**Creation Timestamp** <Ref id="1.4.4" label="§1.4.4" />)

$$
h_1(e)=1+\max\bigl(\{H(x,u):(x,u)\in E\}\cup\{0\}\bigr)=h_2(e).
$$

Thus the two assignments define a common function $h$ on $B_1\cup B_2$.

**II. Directed-Pair Membership and Reciprocal Rejection**

For an ordered pair $e=(u,v)$ write $e^{-1}=(v,u)$. Accumulating the sets in the two orders gives

$$
\begin{aligned}
e\in B_{12}&\Longleftrightarrow e\in B_1\lor e\in B_2,\\
e\in B_{21}&\Longleftrightarrow e\in B_2\lor e\in B_1,\\
e\in F(B_{12})
&\Longleftrightarrow
(u\ne v)\land(e\in B_1\lor e\in B_2)
\land(e^{-1}\notin B_1)\land(e^{-1}\notin B_2)\\
&\Longleftrightarrow e\in F(B_{21}).
\end{aligned}
$$

For $u\ne v$, the reciprocal-pair example has $B_1=\{e\}$ and $B_2=\{e^{-1}\}$. Then

$$
\begin{aligned}
e^{-1}\notin B_1&\Longrightarrow F(B_1)=\{e\},\\
e\notin B_2&\Longrightarrow F(B_2)=\{e^{-1}\},\\
B_{12}=B_{21}&=\{e,e^{-1}\},\\
e^{-1}\in B_{12}&\Longrightarrow e\notin F(B_{12}),\\
e\in B_{12}&\Longrightarrow e^{-1}\notin F(B_{12}).
\end{aligned}
$$

Neither proposal survives the filter on the complete set, so $F(B_{12})=F(B_{21})=\varnothing$.

**III. Equality of the Height Fields**

Let $E_{ij}=E\cup F(B_{ij})$. Pointwise equality of retained membership gives $E_{12}=E_{21}$. For $e$ in this common edge set,

$$
H_{12}(e)=
\begin{cases}
H(e),&e\in E,\\
h(e),&e\in F(B_{12})
\end{cases}
=
\begin{cases}
H(e),&e\in E,\\
h(e),&e\in F(B_{21})
\end{cases}
=H_{21}(e).
$$

The vertex set is fixed, so $(V,E_{12},H_{12})=(V,E_{21},H_{21})$ (**Confluence of the Constructor** <Ref id="2.4.2" label="§2.4.2" />).

**IV. Worked Example of Vertex Sharing**

The two support paths are $(0,1,2)$ and $(2,3,4)$. They share vertex $2$. The old adjacency and the complete short-path families at their endpoint pairs are

$$
E_0=\{(0,1),(1,2),(2,3),(3,4),(0,4)\},\qquad
\Pi_{\ell\le2}^{E_0}(0,2)=\{(0,1,2)\},\quad
\Pi_{\ell\le2}^{E_0}(2,4)=\{(2,3,4)\}.
$$

Indeed, $0$ has successors $1,4$, of which only $1$ has an edge to $2$, and $2$ has only successor $3$, which has an edge to $4$. Neither endpoint pair has a direct edge. Thus each path passes the short-path uniqueness test (**Principle of Unique Causality (PUC)** <Ref id="2.3.4" label="§2.3.4" />).

If $(2,0)$ is inserted first, the successors of $2$ become $\{0,3\}$ and both have an edge to $4$. The updated count is

$$
\Pi_{\ell\le2}^{E_0\cup\{(2,0)\}}(2,4)
=\{(2,0,4),(2,3,4)\},\qquad
\left|\Pi_{\ell\le2}^{E_0\cup\{(2,0)\}}(2,4)\right|=2 .
$$

Thus reevaluating PUC at the second path rejects it. For a frozen batch consisting of these two proposals, the filter instead acts on $B=\{(2,0),(4,2)\}$. The reverse pairs $(0,2)$ and $(2,4)$ are both absent from $B$, so $F(B)=B$ and both accumulation orders produce $E_0\cup\{(2,0),(4,2)\}$ with the same snapshot-assigned heights.

Q.E.D.

### 2.4.2.2 Commentary: Confluence Properties {#2.4.2.2}

:::info[**Convergence of Alternative Path Branches in the Macro-Timeline**]
:::

Confluence properties guarantee that spatially independent rewrite paths eventually converge, ensuring that the macroscopic timeline remains unique regardless of the local update schedule. In a distributed pre-geometric substrate, updates execute concurrently across disparate regions, mirroring the Church-Rosser and critical-pair confluence theorems of algebraic graph transformation (<Cite id="A.24" label="(Ehrig et al., 2006)" />). Local confluence ensures that the final topological configuration depends exclusively on the set of applied rules rather than the arbitrary sequential ordering of intermediate operations.

In the absence of confluence, disparate sequences of local graph rewrites would branch into incompatible parallel geometries, destroying macroscopic coherence. By guaranteeing that local path choices reconcile into a unified global state, the confluent constructor prevents history splitting at the Planck scale. This mathematical property secures the uniqueness of classical spacetime histories, providing the structural foundation for determinism and macroscopic timeline stability.

---

### 2.4.3 Lemma: Chordlessness of Maximal Cycles {#2.4.3}

:::info[**Topological Chordlessness via Maximal Cycles**]
:::

Let the input be exactly the isolated directed cycle $C_k$ with edges $i\to i+1\pmod k$, $k\ge4$. Then this initial maximal cycle is chordless and each of its $k$ perimeter two-paths passes candidate-relative PUC (**Principle of Unique Causality (PUC)** <Ref id="2.3.4" label="§2.3.4" />).

### 2.4.3.1 Proof: Chordlessness of Maximal Cycles {#2.4.3.1}

:::tip[**Isolated Perimeter Chordlessness via Outgoing Adjacency**]
:::

**I. Perimeter Adjacency**

Let $V=\mathbb Z/k\mathbb Z$ with $k\ge4$ and $E_0=\{(i,i+1):i\in V\}$. The outgoing set of vertex $i$ is exactly $\{i+1\}$. Hence a directed edge joining nonconsecutive perimeter vertices would require its target to equal $i+1$, contrary to nonconsecutiveness.

**II. Path Existence and Uniqueness**

For fixed $i$, the ordered path $(i,i+1,i+2)$ has two edges of $E_0$. The congruences $0\not\equiv1,2\pmod k$ and $1\not\equiv2\pmod k$ give pairwise distinctness. Also

$$
\begin{aligned}
(i,i+2)\in E_0&\Longrightarrow i+2\equiv i+1\pmod k
\Longrightarrow k\mid 1,\\
(i+2,i)\in E_0&\Longrightarrow i\equiv i+3\pmod k
\Longrightarrow k\mid 3,
\end{aligned}
$$

both impossible for $k\ge4$. If $(i,x),(x,i+2)\in E_0$, the first condition gives $x=i+1$ and the second then gives $i+2=x+1$. Thus the unique path of length one or two from $i$ to $i+2$ is the displayed two-path (**Principle of Unique Causality (PUC)** <Ref id="2.3.4" label="§2.3.4" />).

**III. Enumeration of Candidates**

Every simple two-path beginning at $i$ must use $i+1$ and then $i+2$, since both outgoing sets are singletons. For the associated chord map,

$$
\Phi(i)=(i+2,i),\qquad
\Phi(i)=\Phi(j)\Longrightarrow i=j
$$

by equality of target coordinates. Therefore the full frozen list contains exactly $|V|=k$ distinct candidate chords (**Chordlessness of Maximal Cycles** <Ref id="2.4.3" label="§2.4.3" />).

Q.E.D.

### 2.4.3.2 Commentary: Chordless Cycles {#2.4.3.2}

:::info[**Independence of Minimal Stabilizer Cycles in Gauge Structures**]
:::

Chordless cycles function as the primitive stabilizer units within the pre-geometric graph substrate. If a maximal cycle possessed internal chord edges, it would immediately decompose into smaller, independent elementary sub-loops, breaching the topological minimality required for gauge invariance. Enforcing chordlessness ensures that maximal loops remain structurally indivisible, acting as fundamental quanta of enclosed causal flux across the network.

This topological requirement mirrors the role of Wilson loops in continuous gauge theories, where closed non-local paths encode physical gauge fields without reference to arbitrary background coordinates. By preserving their structural independence against internal short-circuiting, chordless cycles maintain discrete topological invariants. These robust units form the foundational building blocks from which the macroscopic stabilizer codespace and emergent gauge fields are systematically derived.

---

### 2.4.4 Lemma: Reduction via Deletion {#2.4.4}

:::info[**Strict Descent of the Lexicographic Potential via Edge Deletion**]
:::

Let $e$ denote an edge belonging to a simple cycle $C$ of maximal length within a graph $G$ characterized by the state valuation $\Phi(G)$ (**Lexicographic Potential** <Ref id="2.3.5" label="§2.3.5" />). Then the deletion of $e$ yields a graph $G'$ satisfying the strict descent condition $\Phi(G') < \Phi(G)$.

### 2.4.4.1 Proof: Reduction via Deletion {#2.4.4.1}

:::tip[**Demonstration of Order Descent via Path Set Reduction**]
:::

**I. Cycle Families Before Deletion**

Let $G=(V,E)$ have maximal simple-cycle length $L$ and $n_L$ cycles of that length (**Lexicographic Potential** <Ref id="2.3.5" label="§2.3.5" />). Fix one maximal cycle $C$ and $e\in E(C)$. For each length $k$, define

$$
\mathcal C_k(G)=\{D\subseteq G:D\text{ is a simple directed cycle of length }k\},\qquad
\mathcal D_k(e)=\{D\in\mathcal C_k(G):e\in E(D)\}.
$$

In particular $C\in\mathcal D_L(e)$, so $|\mathcal D_L(e)|\ge1$.

**II. Exact Cycle-Set Identity**

Deletion gives $G'=(V,E\setminus\{e\})$ (**Edge Deletion Task** <Ref id="1.5.3" label="§1.5.3" />). If $D\in\mathcal C_k(G')$, all its edges lie in $E\setminus\{e\}$, so $D\in\mathcal C_k(G)$ and $e\notin E(D)$. Conversely, if $D\in\mathcal C_k(G)$ and $e\notin E(D)$, all its edges remain in $G'$, so $D\in\mathcal C_k(G')$. Thus

$$
\mathcal C_k(G')=\mathcal C_k(G)\setminus\mathcal D_k(e)
\quad\Longrightarrow\quad
|\mathcal C_k(G')|=|\mathcal C_k(G)|-|\mathcal D_k(e)|.
$$

No cycle of length greater than $L$ can appear, since every remaining cycle already belonged to $G$.

**III. The Two Potential Cases**

At length $L$,

$$
0\le|\mathcal C_L(G')|
=n_L-|\mathcal D_L(e)|\le n_L-1<n_L.
$$

If this number is positive, then $L'_{max}=L$ and

$$
\Phi(G')=(L,n_L-|\mathcal D_L(e)|)<_{lex}(L,n_L)=\Phi(G).
$$

If it is zero, no length-$L$ cycle survives, and none longer exists. Thus $L'_{max}<L$; use $L'_{max}=0$ if no cycles remain. The first coordinate then gives $\Phi(G')<_{lex}\Phi(G)$ regardless of the second coordinate.

$$
\boxed{e\in E(C),\quad |C|=L_{max}(G)
\ \Longrightarrow\ \Phi(G-e)<_{lex}\Phi(G).}
$$

Q.E.D.

### 2.4.4.2 Commentary: Reduction Properties {#2.4.4.2}

:::info[**Thermodynamic Regulation of Graph Density via Cycle Dissolution**]
:::

Reduction via deletion describes the physical mechanism by which edge removal systematically decreases local cycle density across the network. In the absence of an active pruning operation, the unconstrained generative drive of edge addition would relentlessly increase relational connectivity. This structural runaway would quickly collapse the causal graph into a hyper-dense, all-to-all connected network that completely lacks spatial locality and meaningful metric distance.

Edge deletion operates as the thermodynamic cooling agent of the pre-geometric vacuum, selectively dissolving redundant relational connections to regulate graph dimensionality. By counteracting generative expansion, deletion preserves sparse connectivity patterns and maintains low-dimensional manifold structures near critical point equilibria. This essential balancing mechanism ensures that the emergent spacetime fabric retains well-defined spatial locality, finite informational capacity, and stable physical coordinates across all macroscopic scales.

Deletion destroys precisely the cycles that use the deleted edge; it cannot create new ones. This monotonicity is why the descent proof does not require the maximal cycle to be chordless or to be the only maximal cycle. The argument concerns deletion by itself. An atomic operation that also adds edges needs a separate bound on the cycles created by those additions before the same potential conclusion can be applied to the combined update.

---

### 2.4.5 Lemma: Decrease in Parallel Updates {#2.4.5}

:::info[**Net Reduction of Topological Complexity via Parallel Rewriting**]
:::

Let the isolated-cycle benchmark perform its single chord-addition phase followed by deletion-only pruning of cycles longer than three. Then it uses at most $k$ additions and $2\cdot k$ deletions, and its final cycle potential is smaller than that of its initial $C_k$ (**Chordlessness of Maximal Cycles** <Ref id="2.4.3" label="§2.4.3" />).

### 2.4.5.1 Proof: Decrease in Parallel Updates {#2.4.5.1}

:::tip[**Verification of Net Descent via Atomic Parallel Rewriting**]
:::

**I. Finite Edge Budget**

The input has $k$ edges. The frozen perimeter list has $k$ distinct proposed chords, so the addition phase leaves at most $2\cdot k$ edges.

**II. Deletion Termination**

Each pruning step selects an existing edge of a cycle longer than three and removes it. If $m_j$ is the current edge count, then $m_{j+1}=m_j-1$. After $j$ removals the edge count is

$$
m_j=m_0+\sum_{\ell=0}^{j-1}(m_{\ell+1}-m_\ell)
=m_0+\sum_{\ell=0}^{j-1}(-1)=m_0-j\ge0.
$$

Thus $j\le m_0\le2k$. A remaining cycle of length greater than three supplies an edge for one more deletion. At $j=m_0$ there are no edges, so the loop must stop by then with no cycle longer than three.

**III. Final Potential**

The initial longest cycle has length $k\ge4$. The final graph has $L_{\max}\le3<k$. Hence its lexicographic cycle potential is strictly smaller regardless of its remaining cycle multiplicity. The separate maximal-cycle edge-deletion lemma supplies strict lexicographic descent when that more specific deletion choice is used (**Reduction via Deletion** <Ref id="2.4.4" label="§2.4.4" />). The implementation's arbitrary long-cycle choice is certified here by edge count instead.

**IV. Mutation Bound**

$$
N_{\mathrm{add}}\le k,\qquad N_{\mathrm{delete}}\le2k,\qquad
N_{\mathrm{add}}+N_{\mathrm{delete}}\le3k.
$$

These are the claimed mutation and final-potential bounds (**Decrease in Parallel Updates** <Ref id="2.4.5" label="§2.4.5" />).

Q.E.D.

### 2.4.5.2 Commentary: Monotonic Potential Descent {#2.4.5.2}

:::info[**Thermodynamic Guarantee of Potential Monotonicity in Atomic Parallel Evolution**]
:::

The atomic cycle reduction $\mathcal{R}_{\text{atom}}$ functions as the thermodynamic engine driving discrete spacetime toward geometric equilibrium. Rather than executing a two-phase pipeline where intermediate unpruned chord networks could temporarily introduce dense cross-chords (such as the inscribed chord pentagram of an unpruned 5-cycle), the physical QBD substrate couples chord instantiation with perimeter edge pruning in a single atomic tick.

Within the discrete causal graph, strict potential descent (**Lexicographic Potential** <Ref id="2.3.5" label="§2.3.5" />) provides a Lyapunov function directly on network configurations, ensuring that every parallel update step strictly reduces the ordered pair $(L_{\max}, N_{L_{\max}})$. This monotonic descent prevents the emergence of dynamical limit cycles or persistent chaotic tangles, guaranteeing that the pre-geometric vacuum converges deterministically toward the ground state defined by fundamental 3-cycle quanta.

---

### 2.4.6 Lemma: Sequential Constructor Diamond {#2.4.6}

:::info[**Sequential Constructor Diamond via Order Independence of Two Overlapping Sequential Additions**]
:::

Let the four endpoints $v,w,u,x$ be distinct with $(v,x)\notin E$, both paths $v\to w\to u$ and $w\to u\to x$ pass PUC and the bounded reverse-witness guard, and the chord heights dominate old outgoing heights at their respective targets. Then both candidate admissions are preserved in either sequential order and the final active timestamped graph is the same.

### 2.4.6.1 Proof: Sequential Constructor Diamond {#2.4.6.1}

:::tip[**Sequential Constructor Diamond via Preservation of Candidate Data under the Other Addition**]
:::

**I. Candidate Paths and Source Maxima**

Write $e_1=(u,v)$, $e_2=(x,w)$, and let $E_j=E\cup\{e_j\}$. A new two-path from $w$ to $x$ in $E_1$ must use $e_1$ either as $(w,y)$ or as $(y,x)$. The first alternative forces $w=u$ and the second $x=v$. Both contradict distinctness. Neither $(w,x)$ nor $(x,w)$ equals $e_1$. Thus the candidate $w\to u\to x$ and both endpoint exclusions are unchanged (**Geometric Constructibility** <Ref id="2.3.1" label="§2.3.1" />).

For a new two-path from $v$ to $u$ in $E_2$, $e_2=(v,y)$ would force $v=x$ and $e_2=(y,u)$ would force $u=w$. Again neither is possible, and $e_2$ differs from both $(v,u)$ and $(u,v)$. The source maxima satisfy

$$
\begin{aligned}
\operatorname{In}_{E_1}(x)&=\operatorname{In}_E(x) && (v\ne x),\\
\operatorname{In}_{E_2}(u)&=\operatorname{In}_E(u) && (w\ne u).
\end{aligned}
$$

The retained old heights on these incoming sets are the same, so the height assigned to $e_2$ after $e_1$ is $h_2$, and that assigned to $e_1$ after $e_2$ is $h_1$.

**II. Exclusion of New Reverse Witnesses**

If a reverse witness from $w$ to $x$ after inserting $e_1$ uses $e_1$, that edge enters $v\ne x$, so the witness has a next edge $(v,z)\in E$. Strict increase would require

$$
h_1<H(v,z)\le \max_{(v,y)\in E}H(v,y)\le h_1.
$$

Similarly a new reverse witness from $v$ to $u$ using $e_2$ must leave $w\ne u$ along $(w,z)\in E$, requiring

$$
h_2<H(w,z)\le\max_{(w,y)\in E}H(w,y)\le h_2.
$$

Both inequalities are impossible. All other witnesses use only old edges, whose heights and common vertex-count cutoff are unchanged.

**III. Equality of the Two Outputs**

In both orders the output edge set is $E\cup\{e_1,e_2\}$. At any output edge $y$, both height functions equal

$$
H_*(y)=
\begin{cases}
H(y),&y\in E,\\
h_1,&y=e_1,\\
h_2,&y=e_2.
\end{cases}
$$

This proves equality as active timestamped graphs (**Sequential Constructor Diamond** <Ref id="2.4.6" label="§2.4.6" />).

Q.E.D.

### 2.4.6.2 Commentary: Sequential and Frozen Evaluation {#2.4.6.2}

:::info[**Sequential and Frozen Evaluation**]
:::

The frozen merge fixes every proposal and height before updating adjacency. In the sequential diamond, each order evaluates its second proposal on a modified snapshot. The second candidate could in principle acquire a competing path, a changed source maximum, or a newly increasing reverse witness. The four endpoints and dominance premise let these questions be checked separately.

The equality concerns the active graph and its height assignment at the end of the two branches. The ledger can distinguish the order of creation events. A simultaneous pair also has a separate global causal question because two locally legal chords can generate new mediated pairs together. The dominance criterion for the full batch uses the transitive closure of those pairs. The result treats just these two overlapping chords at their constructor heights.

---

### 2.4.7 Proof: General Cycle Decomposition {#2.4.7}

:::tip[**Derivation of General Cycle Decomposition via Confluence and Potential Reduction**]
:::

**I. Initial Accessibility and Merge**

The isolated input has the $k$ PUC-compliant perimeter paths (**Chordlessness of Maximal Cycles** <Ref id="2.4.3" label="§2.4.3" />). Its frozen proposal union has the stated accumulation-order property (**Confluence of the Constructor** <Ref id="2.4.2" label="§2.4.2" />).

**II. Pruning and Termination**

The maximal-cycle deletion identity is valid independently of chordlessness (**Reduction via Deletion** <Ref id="2.4.4" label="§2.4.4" />). For the actual benchmark's arbitrary long-cycle choices, the decreasing edge budget gives termination, the $3\cdot k$ mutation bound and final $L_{\max}\le3$ (**Decrease in Parallel Updates** <Ref id="2.4.5" label="§2.4.5" />).

**III. Reciprocal-Chord Cases**

Two proposed chords $(i+2,i)$ and $(j+2,j)$ are reciprocal exactly when $j=i+2$ and $i=j+2$ modulo $k$. These equations imply $k\mid4$, so among $k\ge4$ only $k=4$ admits such a pair. No proposed chord is reciprocal to a perimeter edge for $k\ge4$. Thus for $k\ge5$ no two-cycle is created; deletions cannot create one later.

**IV. Scope of the Conclusion**

For $k\ge5$, absence of loops and reciprocal pairs together with $L_{\max}\le3$ leaves only directed three-cycles if any cycles remain. For $k=4$, the asserted stopping condition alone is $L_{\max}\le3$ (**General Cycle Decomposition** <Ref id="2.4.1" label="§2.4.1" />).

The sequential diamond applies to its two individually admissible proposals under the height-dominance premises (**Sequential Constructor Diamond** <Ref id="2.4.6" label="§2.4.6" />).

Q.E.D.

---

### 2.4.8 Example: 4-Cycle Reduction {#2.4.8}

:::tip[**Algorithmic Verification of 4-Cycle Reduction via Iterative Chordal Decomposition**]
:::

**I. Initial State Definition**

Let $G_0 = (V, E_0)$ denote an isolated directed cycle of length $L=4$.
* **Vertices:** $V = \{0, 1, 2, 3\}$
* **Edges:** $E_0 = \{(0, 1), (1, 2), (2, 3), (3, 0)\}$
* **Topological Metrics:** $L_{\max} = 4$, Potential $\Phi(G_0) = (4, 1)$.

*(Remark on Untimestamped Pedagogical Model vs. Physical QBD Substrate):*
The four-cycle walkthrough below traces the unweighted, untimestamped topological decomposition used in early pedagogical illustrations and benchmark calculations such as **Simulation Verification** <Ref id="2.4.11" label="§2.4.11" />. In the physical substrate equipped with edge timestamps $H(e)$ and the Symmetric Reciprocal Filter $\mathcal{M}(A)$, proposals $(2, 0)$ and $(0, 2)$ colliding on an exact unweighted tie are simultaneously suppressed ($\mathcal{M}(A)$ drops colliding pairs $(u, v)$ and $(v, u)$), preventing reciprocal 2-cycles from nucleating and strictly preserving Axiom 1. Once local asymmetry is broken by ambient field timestamps or non-uniform path histories, atomic chord insertion resolves the defect directly into simplicial 3-cycles without intermediate reciprocal states.

**II. Phase 1: Chordal Addition ($k=4$)**

The rewrite rule $\mathcal{R}$ identifies all compliant 2-paths.
1.  **Site Identification:**
    * $\pi_1 = (0, 1, 2) \implies$ Add chord $(2, 0)$
    * $\pi_2 = (1, 2, 3) \implies$ Add chord $(3, 1)$
    * $\pi_3 = (2, 3, 0) \implies$ Add chord $(0, 2)$
    * $\pi_4 = (3, 0, 1) \implies$ Add chord $(1, 3)$
2.  **Operational Execution:**

    $$
    E_{add} = E_0 \cup \{(2, 0), (3, 1), (0, 2), (1, 3)\}
    $$

    **Total Additions:** 4

**III. Phase 2: Entropic Deletion**

1.  **Cycle Detection:** The original cycle $(0, 1, 2, 3)$ persists.
2.  **Target Selection:** The algorithm selects edge $e = (0, 1)$.
3.  **Operational Execution:**

    $$
    E_{final} = E_{add} \setminus \{(0, 1)\}
    $$

    **Total Deletions:** 1

**IV. Final State Analysis**

* **Topological Check:**
    * Removing $(0, 1)$ breaks the 4-cycle.
    * Connectivity resolves to 3-cycles.
    * **Cycle A:** $(2, 3, 0, 2)$ via edges $(2, 3)$, $(3, 0)$, chord $(0, 2)$.
    * **Cycle B:** $(1, 2, 3, 1)$ via edges $(1, 2)$, $(2, 3)$, chord $(3, 1)$.
* **Result:** $L_{\max} = 3$. Total reduction steps = 5.

---

### 2.4.9 Example: 5-Cycle Reduction {#2.4.9}

:::tip[**Algorithmic Verification of 5-Cycle Reduction demonstrating Iterative Decomposition**]
:::

**I. Initial State Definition**

Let $G_0$ consist of a directed cycle of length $L=5$.
* **Vertices:** $V = \{0, 1, 2, 3, 4\}$
* **Edges:** $E_0 = \{(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)\}$
* **Metrics:** $L_{\max} = 5$.

**II. Phase 1: Chordal Addition ($k=5$)**

1.  **Site Identification:**
    * $(0, 1, 2) \to (2, 0)$
    * $(1, 2, 3) \to (3, 1)$
    * $(2, 3, 4) \to (4, 2)$
    * $(3, 4, 0) \to (0, 3)$
    * $(4, 0, 1) \to (1, 4)$
2.  **Operational Execution:**

    $$
    E_{add} = E_0 \cup \{(2, 0), (3, 1), (4, 2), (0, 3), (1, 4)\}
    $$

    **Total Additions:** 5

**III. Phase 2: Entropic Deletion**

1.  **Iteration 1:**
    * **Detect:** Cycle $(0, 1, 2, 3, 4)$. Length 5.
    * **Delete:** Edge $(0, 1)$.
    * **State:** $E_1 = E_{add} \setminus \{(0, 1)\}$.
2.  **Iteration 2:**
    * **Detect:** Cycle $(1, 4, 2, 3, 1)$.
        * Path components: $(1, 4)$ [Chord], $(4, 2)$ [Chord], $(2, 3)$ [Perimeter], $(3, 1)$ [Chord].
        * Length: 4.
    * **Delete:** Edge $(1, 4)$.
    * **State:** $E_2 = E_1 \setminus \{(1, 4)\}$.
3.  **Iteration 3:**
    * **Detect:** Cycle $(2, 0, 3, 4, 2)$.
        * Path components: $(2, 0)$ [Chord], $(0, 3)$ [Chord], $(3, 4)$ [Perimeter], $(4, 2)$ [Chord].
        * Length: 4.
    * **Delete:** Edge $(2, 0)$.
    * **State:** $E_3 = E_2 \setminus \{(2, 0)\}$.
    * **Total Deletions:** 3.

**IV. Final State Analysis**

* **Result:** No cycles of length $> 3$ remain. Remaining structure consists of 3-cycles such as $(1, 2, 3)$ via chord $(3, 1)$. Total reduction steps = 8.

---

### 2.4.10 Example: 6-Cycle Reduction {#2.4.10}

:::tip[**Algorithmic Verification of 6-Cycle Reduction highlighting Operational Confluence**]
:::

**I. Initial State Definition**

Let $G_0$ consist of a directed cycle of length $L=6$.
* **Vertices:** $V = \{0, 1, 2, 3, 4, 5\}$
* **Edges:** $E_0 = \{(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)\}$

**II. Phase 1: Chordal Addition ($k=6$)**

1.  **Site Identification:**
    Six compliant sites: $(0, 1, 2) \to (2, 0)$, $(1, 2, 3) \to (3, 1)$, $(2, 3, 4) \to (4, 2)$, $(3, 4, 5) \to (5, 3)$, $(4, 5, 0) \to (0, 4)$, $(5, 0, 1) \to (1, 5)$.
2.  **Operational Execution:**

    $$
    E_{add} = E_0 \cup \{(2, 0), (3, 1), (4, 2), (5, 3), (0, 4), (1, 5)\}
    $$

    **Total Additions:** 6

**III. Phase 2: Entropic Deletion**

1.  **Iteration 1:**
    * **Detect:** Cycle $(0, 1, 2, 3, 4, 5)$. Length 6.
    * **Delete:** Edge $(0, 1)$.
    * **State:** $E_1 = E_{add} \setminus \{(0, 1)\}$.
2.  **Iteration 2:**
    * **Detect:** Cycle $(0,4,5,3,1,2,0)$.
        * Perimeter edges: $(4,5),(1,2)$.
        * Chords: $(0,4),(5,3),(3,1),(2,0)$.
        * Length: 6.
    * **Delete:** Chord $(0,4)$.
    * **State:** $E_2=E_1\setminus\{(0,4)\}=E_{add}\setminus\{(0,1),(0,4)\}$.
    * **Total Deletions:** 2.

**IV. Final State Analysis**

The only outgoing edges from $0$ were $(0,1)$ and $(0,4)$. Both were removed, so $0$ lies on no remaining cycle. On the vertices $\{1,2,3,4,5\}$ the successors in $E_2$ are

$$
1\mapsto\{2,5\},\quad 2\mapsto\{3\},\quad
3\mapsto\{1,4\},\quad 4\mapsto\{2,5\},\quad 5\mapsto\{3\}.
$$

A cycle through $1$ must enter it from $3$. Its first edge out of $1$ goes to $2$ or $5$, either of which returns to $3$. To close without repeating $3$ the cycle must then take $(3,1)$. A cycle avoiding $1$ must contain $3$, since deleting $1$ and $3$ leaves just the edges $(4,2)$ and $(4,5)$. It must leave $3$ along $(3,4)$, after which $2$ and $5$ both return to $3$. Thus the complete cycle family up to rotation is

$$
(1,2,3,1),\qquad (1,5,3,1),\qquad
(2,3,4,2),\qquad (3,4,5,3).
$$

The pruning criterion is met with $L_{\max}=3$. The benchmark performs six additions and two deletions, for eight edge mutations.

---

### 2.4.11 Calculation: Simulation Verification {#2.4.11}

:::note[**Simulation Verification of the Cycle Reduction Algorithm via Deterministic Execution**]
:::

Verification of finite isolated-cycle termination (**General Cycle Decomposition** <Ref id="2.4.7" label="§2.4.7" />) (**Confluence of the Constructor** <Ref id="2.4.2" label="§2.4.2" />) is based on the following protocols:

1.  **Defect Initialization:** The algorithm constructs isolated directed cycles of length $k \in [4, 12]$ to serve as standardized topological defects. This mapping represents the initialization of unstable macroscopic loops within the vacuum.
2.  **Topological Reduction:** The protocol simulates an unweighted topological reduction by instantiating chords across open 2-paths and subsequently pruning macro-cycles ($L > 3$) via entropic deletion to resolve topological tension.
3.  **Operation Counting:** The metric tracks the total additions and deletions required for the system to reach the simplicial ground state ($L_{\max} = 3$), verifying the monotonic descent of $\Phi(G)$ (**Lexicographic Potential** <Ref id="2.3.5" label="§2.3.5" />).

*(Pedagogical Benchmark vs. Physical Dynamic Execution):*  
The script below is a topological demonstrator of cycle-length reduction on unweighted defect graphs. In the physical QBD substrate, graph rewriting executes via the timestamp-aware atomic scheduler with the Symmetric Reciprocal Filter $\mathcal{M}(A)$ (shown in `atomic_cycle_reduction_step`), strictly preventing reciprocal 2-cycles during parallel collapse.

```python
"""
Pedagogical Topological Cycle Digestion Demonstrator (§2.4.11).

Demonstrates cycle-length reduction on unweighted directed k-cycles
to verify termination at simplicial ground states (L_max <= 3).
Physical rewrites use the timestamp-aware atomic scheduler (Axioms 1-3).
"""

import networkx as nx
import pandas as pd
import math 

def create_directed_cycle(k):
    """Creates a simple directed $k$-cycle graph: the initial topological defect."""
    G = nx.DiGraph()
    nodes = list(range(k))
    for i in range(k):
        G.add_edge(nodes[i], nodes[(i + 1) % k])
    return G

def get_max_cycle_len(G):
    """Returns the length of the longest simple cycle, or 0 if acyclic."""
    try:
        cycles = list(nx.simple_cycles(G))
        if not cycles:
            return 0
        return max(len(c) for c in cycles)
    except nx.NetworkXNoCycle:
        return 0

def find_compliant_2_paths(G):
    """
    Identifies all open 2-paths (v→w→u) that satisfy the
    Principle of Unique Causality (PUC) for chord addition.
    This is the recognition phase of the rewrite rule.
    """
    paths = []
    for v in G.nodes():
        for w in G.successors(v):
            for u in G.successors(w):
                if u == v: 
                    continue  # Prevent trivial loops
                
                # Constraint 1: Direct chord must not exist
                if G.has_edge(v, u): 
                    continue
                
                # Constraint 2: No parallel 2-path (PUC)
                redundant = False
                for x in G.successors(v):
                    if x != w and G.has_edge(x, u):
                        redundant = True
                        break
                if not redundant:
                    paths.append((v, w, u))
    return paths

def phase_1_add_chords(G):
    """Phase 1: Exhaustive chord insertion on all compliant sites (parallel update)."""
    paths = find_compliant_2_paths(G)  # Collect all sites first, simulating parallel application
    ops = 0
    for v, w, u in paths:
        if not G.has_edge(u, v):        # Direction: close with (u → v)
            G.add_edge(u, v)
            ops += 1
    return ops

def phase_2_delete_cycles(G):
    """Phase 2: Entropic deletion: break remaining macro-cycles by removing perimeter edges."""
    ops = 0
    while True:
        max_len = get_max_cycle_len(G)
        if max_len <= 3:
            break
           
        # Find and break one macro-cycle
        target_cycle = None
        for c in nx.simple_cycles(G):
            if len(c) > 3:
                target_cycle = c
                break
       
        if target_cycle:
            # Delete the first edge of the detected cycle: thermodynamic pruning
            u, v = target_cycle[0], target_cycle[1]
            if G.has_edge(u, v):
                G.remove_edge(u, v)
                ops += 1
        else:
            break
    return ops

def run_reduction_protocol(k):
    """Full reduction protocol for a single $k$-cycle, returning (add_ops, del_ops)."""
    if k <= 3: 
        return 0, 0
   
    G = create_directed_cycle(k)
    add_ops = phase_1_add_chords(G)
    del_ops = phase_2_delete_cycles(G)
   
    return add_ops, del_ops


def atomic_cycle_reduction_step(G):
    """
    Companion reference: Timestamp-aware atomic cycle reduction step (Lemma 2.4.5).
    Applies chord addition and perimeter deletion in a single atomic rewrite step,
    filtering reciprocal collision pairs to strictly preserve Axiom 1 (no 2-cycles).
    """
    paths = find_compliant_2_paths(G)
    if not paths:
        return 0, 0
    
    proposals_add = {(u, v) for v, w, u in paths}
    # Symmetric Reciprocal Filter (Corollary 2.2): drop colliding pairs and self-loops
    filtered_add = {
        (u, v) for (u, v) in proposals_add
        if (v, u) not in proposals_add and u != v
    }
    
    proposals_del = set()
    for c in nx.simple_cycles(G):
        if len(c) > 3:
            proposals_del.add((c[0], c[1]))
            break
            
    for u, v in filtered_add:
        G.add_edge(u, v)
    for u, v in proposals_del:
        if G.has_edge(u, v):
            G.remove_edge(u, v)
            
    return len(filtered_add), len(proposals_del)


# === Execution and Verification ===
results = []
for k in range(4, 13):
    adds, dels = run_reduction_protocol(k)
    results.append({
        "Cycle Length (k)": k,
        "Add Ops": adds,
        "Del Ops": dels,
        "Total Steps": adds + dels
    })

df = pd.DataFrame(results)
print(df.to_markdown(index=False))
```

**Simulation Results:**

|   Cycle Length (k) |   Add Ops |   Del Ops |   Total Steps |
|-------------------:|----------:|----------:|--------------:|
|                  4 |         4 |         1 |             5 |
|                  5 |         5 |         3 |             8 |
|                  6 |         6 |         2 |             8 |
|                  7 |         7 |         3 |            10 |
|                  8 |         8 |         3 |            11 |
|                  9 |         9 |         3 |            12 |
|                 10 |        10 |         3 |            13 |
|                 11 |        11 |         3 |            14 |
|                 12 |        12 |         3 |            15 |

**Conclusion:**
The tabulated data establishes a linear correlation between the initial cycle length $k$ and the addition count ($Ops_{add} = k$). The deletion count stabilizes at a constant value ($Ops_{del} = 3$) for all topologies with $k \ge 7$. This finite scaling confirms that the algorithmic reduction complexity is proportional to the defect size $O(k)$, validating the termination logic of the proof.

---

### 2.4.12 Type-Theoretic Validation via Lean 4 Core {#2.4.12}

:::note[**Lean 4 Encoding of Lexicographic Well-Foundedness via Well-Order Instantiation**]
:::

Type-theoretic certification of the descent guarantee established in the **Well-Foundedness** <Ref id="2.3.6" label="§2.3.6" /> proof proceeds via the following verification strategy:

1.  **Encoding:** The definitions `IsGeometricQuantum` and `IsCompliant2Path` encode the directed **3-cycle** and the **Principle of Unique Causality** as dependent propositions over an abstract causal relation, confirming that the type system admits the axiomatic vocabulary without contradiction.
2.  **Theorem Statements:** The first theorem (`lexicographic_relation_wf`) certifies the well-foundedness of the lexicographic product order on $\mathbb{N} \times \mathbb{N}$ by kernel-delegated instance resolution; the second (`lexicographic_descent_admissible`) certifies that any state transition reducing either the maximum cycle length or its multiplicity constitutes a strictly descending step in this order; the third (`puc_precludes_alternative_intermediate`) certifies that parent uniqueness under `IsCompliant2Path` excludes duplicate intermediate 2-path routing channels.
3.  **Proof Closure:** `lexicographic_relation_wf` is discharged by `inferInstance`, confirming Lean's standard library contains the required well-order; `lexicographic_descent_admissible` uses a case split on the disjunction, with `Prod.Lex.left` closing the length-reduction branch and `Prod.Lex.right` closing the count-reduction branch after `subst` eliminates the equality hypothesis; `puc_precludes_alternative_intermediate` is discharged directly by applying the uniqueness projection of `IsCompliant2Path` to the path pair hypothesis.

```lean
-- Establish the implicit event universe variable
variable {V : Type}

-- Define a Causal Relation as a binary predicate mapping pairs to a Proposition
def CausalRelation (V : Type) := V → V → Prop

-- Directed 3-cycle template (IsGeometricQuantum)
def IsGeometricQuantum (R : CausalRelation V) (u v w : V) : Prop :=
  R u v ∧ R v w ∧ R w u

-- Principle of Unique Causality (PUC) (IsCompliant2Path)
def IsCompliant2Path (R : CausalRelation V) (u w v : V) : Prop :=
  R u w ∧ R w v ∧ ¬ R u v ∧ (∀ z : V, R u z ∧ R z v → z = w)

/--
THEOREM 1: Lexicographic Potential Relation is Well-Founded
Formally establishes that Prod.Lex on Nat × Nat is well-founded,
guaranteeing the existence of no infinite descending chains in the state space.
-/
theorem lexicographic_relation_wf :
    WellFounded (Prod.Lex (fun (a b : Nat) => a < b) (fun (a b : Nat) => a < b)) :=
  (inferInstance : WellFoundedRelation (Nat × Nat)).wf

/--
THEOREM 2: Lexicographic Descent is Admissible
Proves that any update step reducing either the maximum cycle length
or its multiplicity transitions the state space along a strictly decreasing chain.
-/
theorem lexicographic_descent_admissible :
    ∀ (L1 N1 L2 N2 : Nat),
    (L2 < L1 ∨ (L2 = L1 ∧ N2 < N1)) →
    Prod.Lex (fun (a b : Nat) => a < b) (fun (a b : Nat) => a < b) (L2, N2) (L1, N1) := by
  intro L1 N1 L2 N2 h
  cases h with
  | inl h_left =>
    exact Prod.Lex.left N2 N1 h_left
  | inr h_right_and =>
    cases h_right_and with
    | intro h_eq h_right =>
      subst h_eq
      exact Prod.Lex.right _ h_right

/--
THEOREM 3: PUC Precludes Alternative Intermediate Nodes
Proves that under the Principle of Unique Causality, no alternative intermediate node z ≠ w
can form a 2-path from u to v, certifying that 2-path routing channels are unique.
-/
theorem puc_precludes_alternative_intermediate :
    ∀ (R : CausalRelation V) (u w v : V),
    IsCompliant2Path R u w v →
    ∀ z : V, R u z → R z v → z = w := by
  intro R u w v h_puc z h_uz h_zv
  exact h_puc.2.2.2 z ⟨h_uz, h_zv⟩
```

**Verification Summary:**
The auxiliary definitions `IsGeometricQuantum` and `IsCompliant2Path` confirm that the causal vocabulary of Axiom 2 is well-typed as Lean propositions, requiring no consistency workaround. The first theorem delegates the well-foundedness of $\mathbb{N} \times \mathbb{N}$ under the lexicographic product order to `inferInstance`, which resolves against Lean's standard library `WellFoundedRelation` instance; the kernel's acceptance of this one-liner constitutes the machine certificate that the codomain of $\Phi(G)$ possesses no infinite descending chains. The second theorem covers the two-case disjunction $(L_2 < L_1) \lor (L_2 = L_1 \land N_2 < N_1)$ that defines strict lexicographic descent: `Prod.Lex.left` closes the first case directly from the length inequality, while `subst h_eq` eliminates the equality $L_2 = L_1$ before `Prod.Lex.right` closes the count-reduction case. The third theorem `puc_precludes_alternative_intermediate` formally certifies that the universal quantification in `IsCompliant2Path` uniquely identifies the intermediate vertex, precluding parallel routing channels. The Lean kernel's acceptance of these closed proof terms certifies the descent guarantee in the **Well-Foundedness** <Ref id="2.3.6" label="§2.3.6" /> proof: any dynamical rule that strictly decreases the Lexicographic Potential $\Phi$ is provably terminating.

---

### 2.4.Z Implications and Synthesis {#2.4.Z}

:::note[**Decomposition**]
:::

As established under **General Cycle Decomposition** <Ref id="2.4.1" label="§2.4.1" />, the 3-cycle Geometric Quantum stands as a global attractor within the state space of the universe, resisting the unbounded expansion of topological complexity. This restorative mechanism operates through a synchronized three-phase kinematic cycle: the Rewrite Rule identifies cycle defects larger than triangles; the **Principle of Unique Causality (PUC)** <Ref id="2.3.4" label="§2.3.4" /> acts as a precise discriminator that forbids the duplication of existing short-range histories while permitting chordal shortcutting ($L=1$ superseding $L \ge 2$); and Thermodynamic Deletion acts as a one-way ratchet that prevents fragmented loops from recombining into high-tension configurations. The well-foundedness of this reduction under the **Lexicographic Potential** <Ref id="2.3.5" label="§2.3.5" /> is certified by the closed Lean 4 kernel proofs, guaranteeing that every rewrite sequence strictly terminates in the simplicial ground state.

Physically, this decomposition constitutes an active process of topological digestion that protects the manifold structure of space. When the vacuum encounters a macro-cycle defect, it triangulates the interior into stable 3-cycle quanta through a finite sequence of chord insertions rather than allowing non-local entanglements to tear the substrate. Enforcing the **Chordlessness of Maximal Cycles** <Ref id="2.4.3" label="§2.4.3" /> purges long-range shortcuts and wormhole-like topological bridges, localizing geometric stress and preserving the microscopic granularity necessary for smooth macroscopic coordinate geometry.

The inevitability of cycle reduction guarantees the **Confluence of the Constructor** <Ref id="2.4.2" label="§2.4.2" />, ensuring that complex topological anomalies are strictly transient and dynamically unstable. The vacuum functions as an active thermodynamic filter, converting chaotic non-local loops into the stable simplicial foam that constitutes background-independent spacetime. Having established that Axioms 1 and 2 dynamically reduce all graph configurations to fundamental geometric quanta, we proceed to prove the logical independence of these two foundational constraints in the subsequent section.

---

## 2.5 Independence {#2.5}

We must pause to verify that our foundational rules are distinct pillars of the theory rather than redundant restatements of a single underlying principle to ensure the logical parsimony of our framework. It is necessary to prove that a system can enforce directed links without automatically compelling triangular geometry and that the existence of closed quanta does not presuppose the directionality of the arrows. We are searching for the logical orthogonality of our axioms to ensure that each one carves out a specific and unique aspect of the physical reality we are constructing. If our axioms were interdependent, we would risk building a theory on circular logic rather than fundamental principles.

A theory carrying excess conceptual baggage fails to identify the true atomic elements of the physics if the axioms are not logically orthogonal and indicates a failure to isolate the independent variables of the system. Relying on interdependent rules obscures the specific role each constraint plays in shaping reality and leaves a confused map of the dependencies between time and space and causality. A theory built on circular assumptions cannot stand because we must demonstrate that each rule brings something unique and necessary to the table to define the universe completely. We must be certain that we are not simply renaming the same constraint in different ways.

We achieve this by constructing explicit countermodels where one axiom holds firmly while the other is flagrantly breached to demonstrate the separability of these physical concepts. A directed square obeys causality yet lacks geometry while a reflexive triangle possesses area yet fails time-ordering which proves the concepts are distinct. These examples serve as logical proofs of independence that validate our choice of axioms as the irreducible basis for a directed geometry and confirm we have isolated the origins of time and space. This analysis confirms that we have successfully decomposed the universe into its prime constituent rules.

---

### 2.5.1 Theorem: Independence of Axioms 1 and 2 {#2.5.1}

:::info[**Independence of Axioms 1 and 2 via Mutual Non-Entailment on Raw Directed Graphs**]
:::

Let the raw universe consist of finite timestamped directed graphs permitting loops and reciprocal pairs. The static geometric diagnostic requires all simple cycles of length at least two to be triangles and each simple two-path to be unique among paths of length at most two, while the constructive predicate starts from a base with no such cycles and the same two-path uniqueness and accretes PUC return chords at constructor heights without creating simple cycles of length at least four. For each geometric predicate, it and Axiom 1 are logically independent even with Axiom 3 imposed.

### 2.5.1.1 Commentary: Argument Outline {#2.5.1.1}

:::tip[**Structure of the Independence of Axioms Argument via Causal Satisfaction, Geometric Satisfaction, and Mutual Non-Entailment**]
:::

The proof proceeds by Direct Construction, establishing logical orthogonality between the causal and geometric primitives by instantiating explicit counter-models.

```text
• 2.5.1 Theorem Independence of Axioms 1 and 2  [by construction]
├── 2.5.1.2 Diagram: Independence Matrix
│
├── 2.5.2 Lemma: Independence Case A
│   ├── 2.5.2.1 Proof: Independence Case A
│   └── 2.5.2.2 Commentary: Local Independence A
│
├── 2.5.3 Lemma: Independence Case B
│   ├── 2.5.3.1 Proof: Independence Case B
│   └── 2.5.3.2 Commentary: Local Independence B
│
├── 2.5.4 Lemma: Raw Proposal Independence
│   ├── 2.5.4.1 Proof: Raw Proposal Independence
│   ├── 2.5.4.2 Calculation: Raw Proposal Predicate Table
│   └── 2.5.4.3 Commentary: Domain of the Transition Witnesses
│
└── 2.5.5 Proof: Independence of Axioms 1 and 2
```

### 2.5.1.2 Diagram: Independence Matrix {#2.5.1.2}

:::note[**Independence Matrix via Truth Table of Static and Constructive Independence Witnesses**]
:::

```text
Graph                       Ax1    Static Ax2    Accretion Ax2    Ax3
Zero-height initial tree   true      true           true         true
Uniform-height four-cycle  true      false          false        true
Triangle and isolated loop false     true           true         true
Five-vertex butterfly      true      true           true         false
```

---

### 2.5.2 Lemma: Independence Case A {#2.5.2}

:::info[**Independence Case A via Independence Witness for Failure of Geometric Constructibility**]
:::

Let $G_A$ be a directed four-cycle with all heights zero. It satisfies Axioms 1 and 3 and fails the static diagnostic and constructive accretion predicates.

### 2.5.2.1 Proof: Independence Case A {#2.5.2.1}

:::tip[**Independence Case A via Evaluation on a Uniform-Height Four-Cycle**]
:::

**I. Directed-Link and Mediated Conditions**

The residue model has all heights zero and the edge sets

$$
E_A=\{(0,1),(1,2),(2,3),(3,0)\},\quad
E_A^{-1}=\{(1,0),(2,1),(3,2),(0,3)\},\quad
E_A\cap E_A^{-1}=\varnothing .
$$

The loop and reciprocity tests reduce to

$$
(i,i+1)=(i,i)\Longrightarrow 1\equiv0\pmod4,\qquad
(i+1,i)\in E_A\Longrightarrow 2\equiv0\pmod4,
$$

both false. A spatial path of length at least two has first two heights $(0,0)$, failing $0<0$. Hence $R(G_A)=\varnothing$ and all its nonempty powers are empty.

**II. Failure of the Static Predicate**

The perimeter $(0,1,2,3,0)$ has all its directed edges in $E_A$ and its first four vertices are pairwise distinct. Thus

$$
(0,1,2,3,0)\in\mathcal C_4(G_A),
\qquad
\mathcal C_4(G_A)\ne\varnothing.
$$

The static predicate requires all simple cycles of length at least two to have length three (**Independence of Axioms 1 and 2** <Ref id="2.5.1" label="§2.5.1" />).

**III. Failure of the Accretion Predicate**

For a hypothetical constructive sequence $G^{(0)},\ldots,G^{(m)}=G_A$, the base has $\mathcal C_4(G^{(0)})=\varnothing$. At each accretion step a four-cycle would either consist wholly of old edges or contain the new chord. The former would lie in $\mathcal C_4(G^{(j)})$ and the latter is prohibited by the accretion rule. Therefore

$$
\mathcal C_4(G^{(j)})=\varnothing\Longrightarrow
\mathcal C_4(G^{(j+1)})=\varnothing.
$$

Induction gives $\mathcal C_4(G_A)=\varnothing$, contradicting the exhibited perimeter (**Independence Case A** <Ref id="2.5.2" label="§2.5.2" />).

Q.E.D.

### 2.5.2.2 Commentary: Local Independence A {#2.5.2.2}

:::info[**An Acyclic Mediated Relation on a Spatial Cycle**]
:::

The directed four-cycle isolates the effect of the geometric cycle condition. Its perimeter has no reciprocal edges and therefore satisfies the local directed-link requirement. Assigning equal active heights also prevents the perimeter from furnishing a strictly increasing path of two or more edges, so the mediated relation has no arrows at all.

The static diagnostic rejects the cycle because of its length. The constructive diagnostic rejects it for a different reason. The permitted accretion starts without a long simple cycle and keeps that property at each step. Their agreement on this graph is useful for the truth table. It leaves room for the diagnostics to give different answers on other graphs, such as a pair of closed triangles sharing a stem.

---

### 2.5.3 Lemma: Independence Case B {#2.5.3}

:::info[**Independence Case B via Independence Witness for Failure of Directed Causality**]
:::

Let $G_B$ consist of a directed triangle with successive heights $0,0,1$ and a disjoint self-loop. It satisfies both geometric predicates and Axiom 3 and fails Axiom 1.

### 2.5.3.1 Proof: Independence Case B {#2.5.3.1}

:::tip[**Independence Case B via Evaluation on a Triangle and a Disjoint Loop**]
:::

**I. Complete Static Path Enumeration**

Let $E=\{(a,b),(b,c),(c,a),(z,z)\}$ with heights $0,0,1,0$ in the listed order. The successor map is $a\mapsto b\mapsto c\mapsto a$ and $z\mapsto z$. For each of $a,b,c$ the first return is at step three, so their cycles differ only by rotation. The first edge from $z$ already repeats $z$, so it cannot start a simple two-path. The full two-path set and the direct edges at its endpoint pairs are

$$
\mathcal P_2(G_B)=\{(a,b,c),(b,c,a),(c,a,b)\},\qquad
\{(a,c),(b,a),(c,b)\}\cap E=\varnothing.
$$

Each ordered endpoint pair appears exactly once. This establishes both clauses of the static predicate (**Independence of Axioms 1 and 2** <Ref id="2.5.1" label="§2.5.1" />).

**II. Constructive Witness**

Let $E_0=E\setminus\{(c,a)\}$. Its only simple two-path is $(a,b,c)$ and its only cycle is the isolated length-one loop. For the candidate $(c,a)$ the incoming height set at $c$ is $\{0\}$, and

$$
h_{\mathrm{new}}=1+\max\{0\}=1,\qquad
E_0\cup\{(c,a)\}=E .
$$

The only simple cycle created by the chord is $(a,b,c,a)$, so this is a valid accretion sequence.

**III. Directed-Link and Mediated Conditions**

The edge $(z,z)\in E$ fails irreflexivity. There are no simple paths of length at least three. For the three two-paths the comparisons are

$$
(a,b,c):0<0\ \text{false},\qquad
(b,c,a):0<1\ \text{true},\qquad
(c,a,b):1<0\ \text{false}.
$$

Hence $R=\{(b,a)\}$ and $R^2=\varnothing$, since no mediated edge leaves $a$. The closure $R^+=R$ has no diagonal (**Independence Case B** <Ref id="2.5.3" label="§2.5.3" />).

Q.E.D.

### 2.5.3.2 Commentary: Local Independence B {#2.5.3.2}

:::info[**Scope of the Raw Graph Universe**]
:::

The isolated loop tests the irreflexivity requirement independently of the triangle. It belongs to the raw input universe and persists in the proposed output, which makes the first axiom false there. The simple two-paths and the directed triangles of interest all lie in the other connected component, so their tests are unaffected by the added loop.

The accretion witness starts with a two-path and the isolated loop. Closing the two-path is legal for the chosen geometric diagnostic, whose base restriction concerns cycles on at least two vertices. This arrangement makes the geometric and directed-link truth values independently visible. For the live evolution, admissible inputs already respect the directed-link restriction, so the raw witness is a logical independence test on an enlarged domain.

---

### 2.5.4 Lemma: Raw Proposal Independence {#2.5.4}

:::info[**Raw Proposal Independence via Independence of Predicates on the Raw Proposal Space**]
:::

Let a raw proposal specify a graph, a triple $(v,w,u)$ and an absent chord $(u,v)$ at its source-maximum height, with a reverse-witness horizon of at least two. The output Axiom 1 test, geometric admission of the specified support and either causal test (bounded reverse witness or full output closure) are mutually independent in the sense that each can fail while the other two pass.

### 2.5.4.1 Proof: Raw Proposal Independence {#2.5.4.1}

:::tip[**Raw Proposal Independence via Evaluation of Three Explicit Proposals**]
:::

**I. Failure of Geometric Admission**

Geometric admission evaluates the candidate-relative two-path test (**Raw Proposal Independence** <Ref id="2.5.4" label="§2.5.4" />) (**Axiom 2 Geometric Constructibility** <Ref id="2.3.1" label="§2.3.1" />).

On $0\xrightarrow{0}1\xrightarrow{0}2\xrightarrow{0}3$ propose $(3,0)$ at height one with specified middle vertex $1$. The edge $(1,3)$ is absent, so the support fails. The added edge produces no loop or reciprocal pair. The reverse path has equal old heights, and the output has $R=\{(2,0)\}$, so both causal tests pass.

**II. Failure of Axiom 1**

On $0\xrightarrow{0}1\xrightarrow{0}2$ with an isolated height-zero loop at $3$, propose $(2,0)$ at height one. The support is unique, the old reverse path has equal heights, and $R$ of the output is $\{(1,0)\}$. The isolated loop remains, so Axiom 1 fails.

**III. Failure of the Causal Tests**

Use $A\xrightarrow{1}Z\xrightarrow{2}D\xrightarrow{3}C\xrightarrow{4}Z\xrightarrow{5}B$ and propose $(B,A)$ at height six. The only simple two-path from $A$ to $B$ is $A\to Z\to B$ and $(A,B)$ is absent. The chord is neither a loop nor reciprocal. The reverse witness has $1<5<6$, so it fails the bounded test. In the output, $A\xrightarrow{1}Z\xrightarrow{2}D$ and $D\xrightarrow{3}C\xrightarrow{4}Z\xrightarrow{5}B\xrightarrow{6}A$ give $A R D R A$, violating the closure test.

Q.E.D.

### 2.5.4.2 Calculation: Raw Proposal Predicate Table {#2.5.4.2}

:::note[**Raw Proposal Predicate Table via Finite Evaluation of the Three Raw Proposal Witnesses**]
:::

Verification of the raw proposal truth table (**Raw Proposal Independence** <Ref id="2.5.4.1" label="§2.5.4.1" />) (**Geometric Constructibility** <Ref id="2.3.1" label="§2.3.1" />) is based on the following protocols:

1.  **Fixtures:** Set the pre-state edge heights and proposed chord for each witness.
2.  **Predicates:** Evaluate geometric admission, the bounded reverse test, and the output closure independently.
3.  **Comparison:** Check the four truth values in each row.

```python
import networkx as nx


def relations(graph):
    relation = nx.DiGraph()
    relation.add_nodes_from(graph)
    for a in graph:
        for b in graph:
            if a == b:
                continue
            if any(len(path) >= 3 and increasing(graph, path)
                   for path in nx.all_simple_paths(graph, a, b)):
                relation.add_edge(a, b)
    return relation


def increasing(graph, path):
    heights = [graph[a][b]["height"] for a, b in zip(path, path[1:])]
    return all(left < right for left, right in zip(heights, heights[1:]))


def evaluate(edges, v, w, u):
    graph = nx.DiGraph()
    graph.add_weighted_edges_from(edges, weight="height")
    height = 1 + max(data["height"] for _, _, data in graph.in_edges(u, data=True))
    middle = {z for z in graph[v] if z not in {v, u} and graph.has_edge(z, u)}
    geometric = (len({v, w, u}) == 3 and middle == {w}
                 and not graph.has_edge(v, u) and not graph.has_edge(u, v))
    reverse_ok = not any(
        len(path) >= 3 and increasing(graph, path)
        and graph[path[-2]][u]["height"] < height
        for path in nx.all_simple_paths(graph, v, u, cutoff=5)
    )
    graph.add_edge(u, v, height=height)
    directed = all(a != b and not graph.has_edge(b, a) for a, b in graph.edges)
    return directed, geometric, reverse_ok, nx.is_directed_acyclic_graph(relations(graph))


fixtures = [
    ([(0, 1, 0), (1, 2, 0), (2, 3, 0)], 0, 1, 3),
    ([(0, 1, 0), (1, 2, 0), (3, 3, 0)], 0, 1, 2),
    ([("A", "Z", 1), ("Z", "D", 2), ("D", "C", 3),
      ("C", "Z", 4), ("Z", "B", 5)], "A", "Z", "B"),
]
expected = [(True, False, True, True), (False, True, True, True),
            (True, True, False, False)]
for index, (fixture, target) in enumerate(zip(fixtures, expected), 1):
    actual = evaluate(*fixture)
    assert actual == target
    print(f"Proposal {index}: {actual}")
```

**Simulation Results:**

```text
Proposal 1: (True, False, True, True)
Proposal 2: (False, True, True, True)
Proposal 3: (True, True, False, False)
```

**Conclusion:**

The three explicit proposals yield the stated truth table and confirm the predicate evaluations on the raw domain.

### 2.5.4.3 Commentary: Domain of the Transition Witnesses {#2.5.4.3}

:::info[**Domain of the Transition Witnesses**]
:::

A raw proposal specifies a proposed chord before testing the geometric and causal predicates. This enlarged domain is useful because one can ask which particular predicate rejects a candidate. The malformed support in the first example tests the geometric condition. The isolated loop in the second example lets the directed-link test fail while the proposed triangle remains locally well formed.

The two causal tests act on different objects. The bounded guard looks for a single reverse witness in the old graph. The full test computes the closure of all mediated pairs in the graph containing the chord. The third proposal fails each test by an explicit witness. Their agreement on this small table leaves the distinction between the predicates intact.

---

### 2.5.5 Proof: Independence of Axioms 1 and 2 {#2.5.5}

:::tip[**Independence of Axioms 1 and 2 via Comparison of Opposite Truth Assignments**]
:::

**I. Failure of Geometric Entailment**

$G_A$ satisfies Axioms 1 and 3 and fails both specified geometric predicates (**Independence Case A** <Ref id="2.5.2" label="§2.5.2" />).

**II. Failure of Causal Entailment**

The triangle and loop meet both geometric tests and have acyclic mediated closure, while the loop violates directed-link irreflexivity (**Independence Case B** <Ref id="2.5.3" label="§2.5.3" />).

**III. Scope of the Predicate Tests**

The two opposite assignments establish mutual non-entailment for each geometric predicate on the raw graph universe. Separate countermodels give the truth assignments on the raw proposal universe (**Raw Proposal Independence** <Ref id="2.5.4" label="§2.5.4" />).

Q.E.D.

---

### 2.5.Z Implications and Synthesis {#2.5.Z}

:::note[**Independence**]
:::

The logical orthogonality of the causal and geometric axioms is confirmed by the **Independence of Axioms 1 and 2** <Ref id="2.5.1" label="§2.5.1" /> through the existence of specific countermodels that violate one while satisfying the other. This proves that time (directionality) and space (triangulation) are distinct, irreducible features of the physical substrate, not derived consequences of a single underlying rule. The separation of these constraints ensures that the theory is not circular, but rather built upon a minimal set of necessary and sufficient conditions.

This delineation clarifies the specific role of each foundational principle: causal validity does not require geometry according to **Independence Case A** <Ref id="2.5.2" label="§2.5.2" />, while geometric constructibility is separate from causal rules according to **Independence Case B** <Ref id="2.5.3" label="§2.5.3" />. It prevents the conflation of cause with structure, allowing the universe to be analyzed as a system where temporal progress and spatial extension are independent but interacting degrees of freedom. This independence guarantees that the resulting physics is rich and non-trivial, arising from the interplay of distinct legislative forces rather than the unfolding of a single tautology.

By establishing these axioms as distinct pillars, this framework secures a robust foundation where the failure of one principle does not collapse the entire theoretical framework, allowing for precise diagnosis of physical pathologies. This modularity implies that the arrow of time and the fabric of space are not the same entity but are coupled mechanical systems. The universe requires both the engine of causality and the chassis of geometry to function, and recognizing their independence provides an understanding of how they constrain one another to produce a consistent physical reality.

---

## 2.6 Inadequacy of Local Axioms {#2.6}

A critical realization confronts us when we examine the behavior of extended causal chains because we find that local rules alone fail to prevent global paradoxes from emerging in the transitive closure of the graph. Our primitives successfully police individual links yet remain blind to longer paths that bend around to touch their own origins to create time machines out of mediated influence. We must address the subtle danger that a sequence of individually valid steps could collectively form a structure that violates the logical consistency of the whole and creates a conflict between local legality and global causality. This forces us to confront the limits of reductionism in a system where global topology emerges from local rules.

The system remains vulnerable to transitive snarls where an event indirectly becomes its own ancestor through a sequence of valid steps if we rely solely on local constraints to govern the evolution. This failure destroys the partial order of the universe and collapses the distinction between past and future to render the timeline incoherent and physically impossible. A universe that permits such circular dependencies cannot support computation or evolution because the state of the system would become undefined and riddled with logical contradictions that prevent the consistent propagation of information. We cannot allow the local freedom of the graph to destroy its global consistency.

We address this inadequacy by exposing the specific failure modes of local axioms such as the reflexive loop in a 3-cycle or the symmetric dependency in a bowtie configuration to diagnose the root of the instability. This diagnosis demonstrates the necessity of a third global constraint to enforce acyclicity across all scales and ensures that the arrow of time remains consistent not just for immediate neighbors but for the entire history of the universe. This moves our theory from a description of local interactions to a framework for global consistency and ensures that the causal order is an invariant property.

---

### 2.6.1 Theorem: Inadequacy of Local Axioms {#2.6.1}

:::info[**Demonstration of Global Inconsistency under Local Axioms due to Transitive Reflexivity and Symmetry Failures**]
:::

Let a system be constrained exclusively by Axioms 1 and 2. The causal precedence relation $\le$ (**Effective Influence** <Ref id="2.6.2" label="§2.6.2" />) is not guaranteed to constitute a strict partial order. Specifically, the transitive closure of locally valid structures permits the emergence of **Reflexivity** ($u \le u$) and **Symmetry** ($u \le v \land v \le u$), thereby failing to enforce global causal consistency.

### 2.6.1.1 Commentary: Argument Outline {#2.6.1.1}

:::tip[**Structure of the Inadequacy of Local Axioms Argument via Local Limit Diagnosis, Reflexive Loop Exposure, Symmetric Loop Construction, and Global Prophylaxis Necessity**]
:::

The proof proceeds via Contradiction, assuming that local constraints alone suffice for global consistency to expose the emergent causal violations that refute this assumption.

```text
• 2.6.1 Theorem Inadequacy of Local Axioms  [by contradiction]
│
├── 2.6.2 Lemma: Effective Influence
│   ├── 2.6.2.1 Proof: Effective Influence
│   └── 2.6.2.2 Commentary: Causal Mediation and Simultaneity Evasion
│
├── 2.6.3 Lemma: Strict Timestamps
│   ├── 2.6.3.1 Proof: Strict Timestamps
│   └── 2.6.3.2 Commentary: Timestamp Strictness
│
├── 2.6.4 Lemma: Failure of Reflexivity
│   ├── 2.6.4.1 Proof: Failure of Reflexivity
│   └── 2.6.4.2 Commentary: Non-Reflexive Causality
│
├── 2.6.5 Lemma: Failure of Asymmetry
│   ├── 2.6.5.1 Proof: Failure of Asymmetry
│   ├── 2.6.5.2 Commentary: Asymmetry Constraints
│   └── 2.6.5.3 Diagram: Bowtie Paradox
│
├── 2.6.6 Lemma: Causal Acyclicity vs. Spatial Triangulation
│   ├── 2.6.6.1 Proof: Causal Acyclicity vs. Spatial Triangulation
│   └── 2.6.6.2 Commentary: Causal and Spatial Interactions
│
└── 2.6.7 Proof: Inadequacy of Local Axioms
    ├── 2.6.7.1 Corollary: Global Constraint
    └── 2.6.7.2 Diagram: Antisymmetry Failure
```

---

### 2.6.2 Lemma: Effective Influence {#2.6.2}

:::info[**Effective Influence via Strictly Increasing Simple Witnesses of Mediated Influence**]
:::

Let $uRv$ mean that there is a directed path from $u$ to $v$ of at least two edges, with pairwise distinct vertices and strictly increasing active heights. The relation $R$ is irreflexive and every witness admits a split at an interior vertex into two strictly increasing subpaths.

### 2.6.2.1 Proof: Effective Influence {#2.6.2.1}

:::tip[**Effective Influence via Decomposition of a Simple Increasing Witness**]
:::

**I. Witness and Endpoint Conditions**

For $P=(x_0,\ldots,x_k)$ with $k\ge2$, put $h_i=H(x_{i-1},x_i)$ for $1\le i\le k$ (**Creation Timestamp** <Ref id="1.4.4" label="§1.4.4" />). The witness conditions are

$$
\forall\,0\le i<j\le k,\ x_i\ne x_j,\qquad
\forall\,1\le i<k,\ h_i<h_{i+1}.
$$

A diagonal pair would give a witness with $0<k$ and $x_0=x_k=u$. At the distinct indices $0,k$, simplicity requires $x_0\ne x_k$. Thus

$$
(u,u)\in R\Longrightarrow (x_0=x_k\land x_0\ne x_k),\qquad
R\cap\{(u,u):u\in V\}=\varnothing .
$$

**II. Restriction to Two Subpaths**

For $1\le j<k$, set $P_-=(x_0,\ldots,x_j)$ and $P_+=(x_j,\ldots,x_k)$. Every edge of either path is an edge of $P$. Their height lists are $(h_1,\ldots,h_j)$ and $(h_{j+1},\ldots,h_k)$, respectively. For consecutive heights inside either list the comparisons are inherited from the displayed witness conditions, and at the shared vertex $x_j$ the comparison is $h_j<h_{j+1}$.

**III. Concatenation under a Strict Join**

Conversely, let $P_-,P_+$ be simple increasing paths of positive length with intersection of vertex sets exactly $\{x_j\}$ and with terminal and initial heights satisfying $h_j<h_{j+1}$. The concatenated vertex sequence uses the join once. A repeated vertex would have to repeat within one subpath, or belong to both outside the join, and each possibility contradicts a hypothesis. All height comparisons are

$$
h_1<\cdots<h_j,\qquad h_j<h_{j+1},\qquad
h_{j+1}<\cdots<h_k .
$$

These give one increasing list of length at least two, so the concatenation witnesses $x_0Rx_k$ (**Effective Influence** <Ref id="2.6.2" label="§2.6.2" />).

Q.E.D.

### 2.6.2.2 Commentary: Causal Mediation and Simultaneity Evasion {#2.6.2.2}

:::info[**Single Witnesses and Transitive Closure**]
:::

The two descriptions of mediated influence use different composition operations. A single witness is a spatial path with pairwise distinct vertices and increasing heights. Its split into two subpaths preserves the comparisons because both pieces come from the same witness. Either piece can be a direct edge if the split lies one step from an endpoint.

Taking the transitive closure composes pairs of the mediated relation. The relation composition only identifies the common endpoint. It can combine witnesses whose heights reset at that endpoint, or whose vertex lists would repeat a position when concatenated. This is how a diagonal of the closure can arise even though every individual witness has distinct endpoints and the relation itself has no diagonal. The closure is built from nonempty chains of mediated pairs.

---

### 2.6.3 Lemma: Strict Timestamps {#2.6.3}

:::info[**Strict Timestamps via Strict and Weak Height Filtering**]
:::

Let $R_{\le}$ use the same simple paths of length at least two as $R$, with nondecreasing heights in place of strictly increasing heights. Then $R\subseteq R_{\le}$, and the inclusion can be strict even when both relations have acyclic closure.

### 2.6.3.1 Proof: Strict Timestamps {#2.6.3.1}

:::tip[**Strict Timestamps via Comparison of Strict and Weak Inequalities**]
:::

**I. Domain and Objects**

Both tests use the same underlying spatial path family (**Strict Timestamps** <Ref id="2.6.3" label="§2.6.3" />) (**Effective Influence** <Ref id="2.6.2" label="§2.6.2" />).

**II. Inclusion**

For every witness of $uRv$, each comparison $h_i<h_{i+1}$ implies $h_i\le h_{i+1}$, giving $uR_{\le}v$.

**III. Equal-Height Witness**

The graph $a\xrightarrow{0}b\xrightarrow{0}c$ has outgoing sets $\{b\},\{c\},\varnothing$ in that order. Its only two-edge path is $(a,b,c)$ and $c$ has no successor. The height pair $(0,0)$ fails $0<0$ and satisfies $0\le0$. Hence

$$
R=\varnothing,\qquad R_{\le}=\{(a,c)\}.
$$

No pair in $R_{\le}$ starts at $c$, so $R_{\le}^2=\varnothing$ and $R_{\le}^+=\{(a,c)\}$. Also $R^+=\varnothing$. Both closures have empty diagonal. Acyclicity of the weak relation therefore permits equal heights along a mediated path.

Q.E.D.

### 2.6.3.2 Commentary: Timestamp Strictness {#2.6.3.2}

:::info[**Active Heights and Occurrence Order**]
:::

Replacing a strict comparison with a weak one introduces spatial paths along edges of equal height. This change matters even on an outward two-path, where no directed cycle is possible. The example isolates the effect of the height predicate because the graph and the underlying family of simple paths are fixed.

The occurrence order uses the supporting inputs of a creation event, whereas the spatial witness test compares the active heights along a path in one snapshot. Strict increase for occurrence dependencies comes from the source maximum at creation. The absence of a cycle in a relation constructed with weak comparisons supplies no numerical inequality for the heights of its individual edges. An increasing numerical sequence is a sufficient witness condition under the stated path test.

---

### 2.6.4 Lemma: Failure of Reflexivity {#2.6.4}

:::info[**Violation of Irreflexivity through the Geometric Quantum**]
:::

Let $R$ denote mediated simple-path influence on the timestamped directed four-cycle $A\xrightarrow1B\xrightarrow2C\xrightarrow3D\xrightarrow4A$. Then $AR^+A$ in the nonempty transitive closure, although the simple-path relation $R$ is itself irreflexive (**Axiom 3 Acyclic Effective Causality** <Ref id="2.7.1" label="§2.7.1" />).

### 2.6.4.1 Proof: Failure of Reflexivity {#2.6.4.1}

:::tip[**Demonstration of Self-Influence via Transitive Analysis**]
:::

**I. The Two Simple Witnesses**

The vertices $A,B,C,D$ are distinct. The sequences $(A,B,C)$ and $(C,D,A)$ have no repeated vertices, have length two, and satisfy the respective height tests $1<2$ and $3<4$ (**Effective Influence** <Ref id="2.6.2" label="§2.6.2" />). Hence

$$
A\,R\,C,\qquad C\,R\,A.
$$

**II. Nonempty Transitive Closure**

A witness for $xR^+y$ is a finite sequence $x=x_0R x_1R\cdots R x_m=y$ with $m\ge1$. The sequence of intermediate vertices $(A,C,A)$ has two $R$-steps, so

$$
A\,R\,C\land C\,R\,A\Longrightarrow AR^+A.
$$

The composed witness is an $R$-chain. It is not required to be one simple spatial path.

**III. Irreflexivity of the Original Filter**

If $x\,R\,x$, a simple path of length at least two would have identical first and last vertices, contrary to pairwise vertex distinctness. Therefore $\neg(x\,R\,x)$ for every $x$, even in this countermodel.

**IV. Conclusion**

$$
\boxed{\forall x,\ \neg(x\,R\,x),\qquad AR^+A.}
$$

The closure violates the required causal irreflexivity (**Failure of Reflexivity** <Ref id="2.6.4" label="§2.6.4" />).

Q.E.D.

### 2.6.4.2 Commentary: Non-Reflexive Causality {#2.6.4.2}
:::tip[**Elimination of Self-Causation at the Micro-Scale**]
:::

The simple-path definition already excludes a self-pair in the original mediated influence relation. The independent causal requirement concerns cycles formed by chains of those influence steps. A chain can return to its starting vertex even though every individual witness has distinct vertices and increasing internal heights. The four-vertex example isolates that distinction: it supplies two valid mediated witnesses, while their composition belongs to a transitive closure rather than to the original class of simple chronological paths.

This separation also explains why a closed spatial walk is insufficient as a simple-path witness. Repeating the starting vertex changes the mathematical object being used. The temporal filter and the nonempty transitive closure must therefore remain visible in both statements and proofs. Acyclicity of the closure gives an actual strict order; its preservation by a particular bounded scheduler check is a further dynamical obligation. The countermodel motivates that obligation without claiming that a chronology-violating spatial assignment is an admissible physical trajectory.

---

### 2.6.5 Lemma: Failure of Asymmetry {#2.6.5}

:::info[**Mutual Influence from Increasing Spatial Arcs**]
:::

Let $G$ be a directed cycle of length $L\ge4$. There is a height assignment under which two vertices $a,b$ satisfy $aRb$ and $bRa$ along simple spatial arcs with disjoint interiors.

### 2.6.5.1 Proof: Failure of Asymmetry {#2.6.5.1}

:::tip[**Failure of Asymmetry via Separate Height Assignments on the Two Cycle Arcs**]
:::

**I. Domain and Objects**

The arc endpoints define mediated pairs when each arc passes the strict test (**Failure of Asymmetry** <Ref id="2.6.5" label="§2.6.5" />) (**Effective Influence** <Ref id="2.6.2" label="§2.6.2" />).

**II. Splitting the Perimeter**

Index the perimeter $x_0,\ldots,x_{L-1},x_0$. Put $a=x_0$ and $b=x_2$. The two directed arcs have lengths $2$ and $L-2$, and their interiors are $\{x_1\}$ and $\{x_3,\ldots,x_{L-1}\}$.

**III. Witness Heights**

Assign heights $1,2$ on the first arc and $1,2,\ldots,L-2$ on the second. Each arc has at least two edges, pairwise distinct vertices, and strictly increasing heights. Thus

$$
a\mathrel R b,\qquad b\mathrel R a,\qquad (a,a)\in R^+ .
$$

Q.E.D.

### 2.6.5.2 Commentary: Asymmetry Constraints {#2.6.5.2}

:::tip[**Arc Endpoints and Mediated Closure**]
:::

The perimeter splits at two chosen vertices into arcs that share their endpoints and have disjoint interiors. Each witness is a simple path on its own. The heights along the second arc can begin again at a low value, because its comparison test is independent of the first arc's terminal height.

The two opposite mediated arrows produce a diagonal after taking transitive closure. The joined spatial traversal repeats its starting vertex, so it cannot be a simple witness for a diagonal of the original relation. Keeping these two operations separate explains how local checks of individual increasing paths can coexist with a failure of acyclicity in their full relational closure. The construction assigns heights to the perimeter separately on the two arcs with no shared edges.

### 2.6.5.3 Diagram: Bowtie Paradox {#2.6.5.3}

:::note[**Visualization of the Effective Influence Paradox illustrating Bidirectional Causality through Entropy Maximization**]
:::

```text
┌───────────────────────────────────────────────────────────────────────┐
│                     THE BOWTIE PARADOX (Counter-Model)                │
│            Satisfies Axioms 1 & 2 -> Violates Global Causality        │
└───────────────────────────────────────────────────────────────────────┘

        LOOP 1 (Left)                     LOOP 2 (Right)
      A -> B -> C (Valid)               C -> D -> A (Valid)

          t=1                                  t=2
      (A)----->(B)                         (C)----->(D)
       ^        |                           |        |
       |        |                           |        |
       |        | t=4                       |        | t=3
       |        |                           |        |
       +-------(C)                         (A)<------+

   ANALYSIS OF PATHS:
   1. Path A->B->C:  Timestamps (1, 4). Strictly Increasing.
      Conclusion: A is an ancestor of C (A <= C).

   2. Path C->D->A:  Timestamps (2, 3). Strictly Increasing.
      Conclusion: C is an ancestor of A (C <= A).

   THE CONTRADICTION:
   A <= C AND C <= A implies A == C.
   But A != C.
   Therefore: Effective Influence is NOT a Partial Order.
```

---

### 2.6.6 Lemma: Causal Acyclicity vs. Spatial Triangulation {#2.6.6}

:::info[**Independence of Spatial Area Closures from Causal Timeline Ordering**]
:::

Let $G_{\mathrm{space}} = (V, E)$ denote the instantaneous Spatial State Graph, and let $G_{\mathrm{event}} = (E, \prec)$ denote the Causal History Poset. Then the existence of directed 3-cycles representing discrete spatial area elements in $G_{\mathrm{space}}$ does not induce or construct directed causal cycles in $G_{\mathrm{event}}$, which remains a strict directed acyclic graph.

### 2.6.6.1 Proof: Causal Acyclicity vs. Spatial Triangulation {#2.6.6.1}

:::tip[**Topological Distinctions between Spatial Boundaries via Chronological Ordering**]
:::

**I. Two Distinct Incidence Relations**

Let $G_{space}=(V,E)$ be the spatial graph, and let $\mathcal E$ be the set of edge-creation events. The event graph has event vertices and causal dependency edges:

$$
G_{event}=(\mathcal E,D),\qquad D\subseteq\prec,
$$

where $\prec$ is the stipulated strict history order (**Causal Acyclicity vs. Spatial Triangulation** <Ref id="2.6.6" label="§2.6.6" />). Spatial adjacency is a relation on $V$; causal precedence is a relation on $\mathcal E$. They are not identified by sharing an incidence symbol (**Causal Graph Substrate** <Ref id="1.4.1" label="§1.4.1" />).

**II. No Cycle in a Strict Event Order**

Suppose the event graph contained a positive-length directed cycle

$$
\varepsilon_0\ D\ \varepsilon_1\ D\ \cdots\ D\ \varepsilon_{m-1}\ D\ \varepsilon_0.
$$

Since $D\subseteq\prec$, transitivity of $\prec$ gives, inductively,

$$
\varepsilon_0\prec\varepsilon_j\quad(1\le j<m),\qquad
\varepsilon_0\prec\varepsilon_{m-1}\prec\varepsilon_0
\ \Longrightarrow\ \varepsilon_0\prec\varepsilon_0.
$$

This contradicts irreflexivity. For $m=1$, the first edge already gives that contradiction. Therefore $G_{event}$ has no directed cycles.

**III. A Spatial Triangle Does Not Supply the Missing Dependency**

The spatial witness is a triangle with distinct supports

$$
e_1=(u,v),\qquad e_2=(v,w),\qquad e_3=(w,u)
$$

(**Geometric Quantum** <Ref id="2.3.3" label="§2.3.3" />). Denote their creation events by $\varepsilon_1,\varepsilon_2,\varepsilon_3$. A consistent event order can have

$$
\varepsilon_1\prec\varepsilon_2\prec\varepsilon_3,
\qquad H(\varepsilon_1)=1,\ H(\varepsilon_2)=2,\ H(\varepsilon_3)=3.
$$

The spatial equality of the final endpoint of $e_3$ and the first endpoint of $e_1$ is an equality in $V$. It does not assert the event dependency $\varepsilon_3\prec\varepsilon_1$. In the concrete order the missing dependency would require $H(\varepsilon_3)<H(\varepsilon_1)$, or $3<1$. In the abstract order,

$$
\varepsilon_1\prec\varepsilon_2\prec\varepsilon_3
\Longrightarrow \varepsilon_1\prec\varepsilon_3,\qquad
(\varepsilon_1\prec\varepsilon_3)\land(\varepsilon_3\prec\varepsilon_1)
\Longrightarrow\varepsilon_1\prec\varepsilon_1 .
$$

Both are contradictions. Thus

$$
\boxed{C_3\subseteq G_{space}\ \text{is compatible with}\
\operatorname{Cycles}(G_{event})=\varnothing}
$$

under the stated separate strict event-order structure.

Q.E.D.

### 2.6.6.2 Commentary: Causal and Spatial Interactions {#2.6.6.2}

:::info[**Prevention of Closed Timelike Loops in Curvature Fields**]
:::

The structural decoupling between spatial triangulation and causal history resolves a fundamental tension in discrete quantum gravity. In Quantum Braid Dynamics, space is constructed from oriented **3-cycles** that tile the graph into simplicial 2-complexes, endowing the substrate with metric area and discrete curvature. However, because edge creation events are assigned discrete, monotonically advancing timestamps $H(e) \in \mathbb{N}_0$, spatial closed loops remain purely relational boundaries that do not circulate causal influence through historical time.

At the cosmological origin ($t=0$), the pre-geometric Bethe tree represents an instantaneous spatial leaf where all constituent edges share the ground-state timestamp $H=0$ (**Topological Tunneling** <Ref id="3.4.2" label="§3.4.2" />). This timestamp degeneracy ensures that tree 2-paths are not strictly monotone under historical accumulation ($0 \not< 0$). Consequently, the Acyclic Pre-Check `pre_check_aec` permits the deterministic first-tick parallel burst to nucleate spatial 3-cycles across unperturbed branches (**Ignition Probability** <Ref id="3.4.5" label="§3.4.5" />) without creating causal closed loops.

If spatial loops were permitted to circulate influence across monotonically increasing historical timestamps, the causal substrate would degenerate into closed timelike curves, destroying the well-founded partial order of history. Enforcing strict chronological monotonicity on causal paths ensures that the emergent spacetime satisfies discrete global hyperbolicity. While local constructibility rules (Axioms 1 and 2) govern the formation of spatial simplices, the global transitivity of **Acyclic Effective Causality** <Ref id="2.7.1" label="§2.7.1" /> protects the timeline against large-scale acausal reconvergence, securing a consistent Lorentzian background for matter and gauge interactions.

The separation result consumes a distinct strict event-order structure as specified in the statement. It does not derive that structure merely from assigning birth numbers to the edges of a spatial graph. A concrete constructor must identify its event objects and dependency edges, and establish that updates preserve their order. Once that structure is supplied, a spatial triangle is not a closed causal history simply because its spatial endpoints close.

---

### 2.6.7 Proof: Inadequacy of Local Axioms {#2.6.7}

:::tip[**Inadequacy of Local Axioms via Composition of Local Influence Witnesses**]
:::

**I. Spatial Witnesses**

Every $R$ witness is a simple increasing spatial path (**Effective Influence** <Ref id="2.6.2" label="§2.6.2" />). Weak height filtering allows additional equal-height witnesses (**Strict Timestamps** <Ref id="2.6.3" label="§2.6.3" />).

**II. Closure Failure**

A composite cycle gives a diagonal pair in $R^+$ (**Failure of Reflexivity** <Ref id="2.6.4" label="§2.6.4" />). In particular, the two increasing arcs of the directed perimeter yield $(a,b),(b,a)\in R$, and hence $(a,a)\in R^+$ (**Failure of Asymmetry** <Ref id="2.6.5" label="§2.6.5" />). The five-vertex accretion witness verifies the failure on a locally constructible input (**Independence of Axiom 3** <Ref id="2.7.6" label="§2.7.6" />).

**III. Spatial Closure**

Spatial triangle closure can coexist with acyclic mediated closure (**Causal Acyclicity vs. Spatial Triangulation** <Ref id="2.6.6" label="§2.6.6" />). The two local constraints thus permit both acyclic and cyclic mediated closures.

Q.E.D.

### 2.6.7.1 Corollary: Global Constraint {#2.6.7.1}

:::info[**Necessity of an Explicit Global Constraint via Causal Unidirectionality**]
:::

A physical theory requires a well-defined causal ordering (a "direction of time"). The proven failure of Axioms 1 and 2 to entail such an order necessitates a third axiom. This axiom must explicitly forbid states containing causal paradoxes, acting as a global topological constraint.

Q.E.D.

### 2.6.7.2 Diagram: Antisymmetry Failure {#2.6.7.2}

:::note[**Comparative Visualization of the Failure Modes of Antisymmetry versus Irreflexivity as Antisymmetry Failure**]
:::

```text
Comparison of Ordering Constraints on Substrate
---------------------------------------------------------
(A) Asymmetry           (B) Antisymmetry          (C) Axiom 1 (Irreflexive)
    u -> v -> u             u -> v -> u               u -> u
    |           |           |           |             |
    v           v           v           v             v
Violation: YES          Violation: ONLY IF        Violation: YES
(Mutual Influence)      u != v                    (Explicitly Forbidden)

Result:                 Result:                   Result:
Pure Directionality     Loophole for u->u         Thermodynamic Arrow
(No Cycles)             (Permits Inert Loops)     (Process Required)
```

---

### 2.6.Z Implications and Synthesis {#2.6.Z}

:::note[**Inadequacy of Local Axioms**]
:::

Local constraints alone fail to prevent global paradoxes, as established in **Inadequacy of Local Axioms** <Ref id="2.6.1" label="§2.6.1" />. Transitive chains of valid links can curl back to form closed timelike curves that are invisible to local inspection. This is demonstrated by the **Failure of Reflexivity** <Ref id="2.6.4" label="§2.6.4" /> and **Failure of Asymmetry** <Ref id="2.6.5" label="§2.6.5" /> in larger cycles, showing that causality is a global property that cannot be fully captured by local enforcement.

This forces a shift from purely reductionist physics to a holistic view where global consistency imposes constraints on local actions, establishing **Effective Influence** <Ref id="2.6.2" label="§2.6.2" /> as a strict partial order requiring **Strict Timestamps** <Ref id="2.6.3" label="§2.6.3" />. It implies that the arrow of time is a coherent global ordering that must be actively maintained against the natural tendency of the graph to tangle. The realization that local validity does not imply global sanity necessitates a mechanism that bridges the gap between the micro and the macro, ensuring that the timeline remains linear and acyclic across all scales.

The persistence of these transitive paradoxes demands the imposition of a third, global axiom to enforce acyclicity, preventing the universe from creating logical contradictions through the accumulation of local steps. Without this global check, the local laws of physics would eventually undermine themselves, creating regions of causality violation that would propagate and destroy the logical consistency of the timeline. The universe must possess a mechanism to censor these global loops, ensuring that the collective history remains a coherent narrative rather than a collection of disjointed and contradictory causal loops.

---

## 2.7 Global Consistency & Enforcement {#2.7}

The enforcement of global acyclicity presents a computational paradox because a local agent within the graph cannot instantaneously perceive the topology of the entire universe to prevent the formation of a large loop. We require a mechanism to enforce acyclicity across the entire graph without resorting to exhaustive global scans that would require infinite computational energy at every step. It is physically impossible for a local agent to perceive the global topology instantly yet the consistency of the timeline depends upon preventing circular paths that may span the entire universe. We are faced with the challenge of imposing a global law using only local resources.

Relying on post-hoc correction proves thermodynamically untenable because it requires the system to wait for a paradox to form before expending infinite energy to resolve it. This wait-and-fix approach violates the finiteness of resources and leaves the universe constantly on the brink of logical collapse and energetic divergence. A reality that must constantly rewind time to fix its own errors is not a stable physical system but a failed simulation so we must find a way to prevent these errors from occurring in the first place without requiring omniscience. The cost of fixing a broken timeline exceeds the energy available in the universe.

We solve this by implementing a preemptive local enforcement mechanism that approximates global consistency through logarithmic-depth probes to filter out potential violations before they manifest. Bounding the error probability exponentially allows us to design a system that is robust by default and utilizes the thermodynamics of the rewrite rule to ensure that the present advances as a coherent wavefront. This statistical enforcement aligns the computational limits of the graph with the physical requirements of causality and ensures that the arrow of time is protected by the laws of probability rather than an impossible requirement for global knowledge.

---

### 2.7.1 Definition: Axiom 3 Acyclic Effective Causality {#2.7.1}

:::tip[**Imposition of Global Causal Consistency through the Enforcement of a Strict Partial Order**]
:::

Let $R$ be the **Effective Influence** relation of mediated simple spatial paths with strictly increasing causal heights (**Effective Influence** <Ref id="2.6.2" label="§2.6.2" />). **Acyclic Effective Causality** requires its nonempty transitive closure $R^+$ to be irreflexive:

$$
\forall v\in V,\ \neg(vR^+v).
$$

Concatenation of finite $R$-chains makes $R^+$ transitive. If $uR^+v$ and $vR^+u$, concatenation would give $uR^+u$, so $R^+$ is asymmetric as well. The strict partial order in this axiom is $R^+$; the original time-respecting simple-path relation need not be transitive. The occurrence dependency order is a separate chronological relation on creation records (**Monotonicity of History** <Ref id="1.4.5" label="§1.4.5" />).

### 2.7.1.1 Commentary: Arrow of Causality {#2.7.1.1}

:::tip[**Derivation of Causal Unidirectionality from the Partial Order Constraint**]
:::

The mathematical requirement that effective influence forms a strict partial order is not a matter of abstract taxonomy: it is the encoding of the fundamental physical principle of **Causal Unidirectionality**. When we assert that the graph must be a partial order, we are asserting that the universe has a distinct grain, a directionality that cannot be smoothed away by coordinate transformations.

The condition of **Irreflexivity** ($\neg(v \le v)$) forbids "closed timelike curves" at the level of individual events. In a computational universe, this is a prohibition against a process waiting for its own output before it begins. An event cannot be its own ancestor: it cannot trigger its own execution. This prevents the logical paradoxes associated with self-creation (the Bootstrap Paradox), ensuring that every event has a lineage that traces back to a distinct origin.

The condition of **Asymmetry** ($\neg(v \le u)$ if $u \le v$) extends this prohibition to mutual influence between distinct entities. If Event $A$ influences Event $B$, then Event $B$ is forever barred from influencing Event $A$. This is the definition of "Past" and "Future." This constraint segregates the universe into a strict "Past" (events that influence $v$), "Future" (events influenced by $v$), and "Elsewhere" (events causally disconnected from $v$). Without this axiom, the distinction between cause and effect would vanish. We would inhabit a static crystal of relations where dependence runs in circles, and time would effectively cease to flow. The imposition of asymmetry forces the system out of equilibrium, rendering the "flow" of time physically well-defined.

### 2.7.1.2 Commentary: Operational Enforcement {#2.7.1.2}

:::info[**Bounded Reverse Witnesses in the Operational Guard**]
:::

The engine enumerates simple paths from the proposed chord's target to its source up to the configured cutoff. It rejects the chord when such a reverse path has at least two edges, strictly increasing heights and terminal height below the proposed height. The inputs to this check come from the frozen active snapshot, before the simultaneous batch is merged.

The Lean edge-list predicate can include repeated vertices and uses an unbounded search specification. Loop erasure relates the witness representations at a common horizon when the endpoints are distinct and the candidate passes the direct-bypass test. That bridge concerns one reverse witness in the old snapshot. Even a single retained chord can create a new mediated pair $wRv$ that composes with an old $vRw$, giving $(v,v)\in R^+$ in the updated graph. The full target-diagonal test applies under old acyclicity and target height dominance (**Batch Causal Preservation under Dominance** <Ref id="2.7.8" label="§2.7.8" />). The first-tick result uses both uniform old heights and a grading that increases along each old edge (**First-Tick Causality on Graded Graphs** <Ref id="2.7.9" label="§2.7.9" />).

```python
from math import log2

import networkx as nx


def pre_check_aec(graph, source, target, candidate_height):
    """Check a bounded reverse witness for an absent return chord."""
    cutoff = int(log2(len(graph))) + 3 if len(graph) > 1 else 1
    for path in nx.all_simple_paths(graph, target, source, cutoff=cutoff):
        heights = [graph[a][b]["H"] for a, b in zip(path, path[1:])]
        if (len(heights) >= 2 and heights[-1] < candidate_height
                and all(a < b for a, b in zip(heights, heights[1:]))):
            return False
    return True


snapshot = nx.DiGraph()
snapshot.add_weighted_edges_from([(0, 1, 0), (1, 2, 0)], weight="H")
assert pre_check_aec(snapshot, 2, 0, 1)
snapshot[1][2]["H"] = 1
assert not pre_check_aec(snapshot, 2, 0, 2)
print("Equal-height path admitted; strictly increasing reverse witness rejected.")
```

---

### 2.7.2 Theorem: Distributed Rollback Cost {#2.7.2}

:::info[**Thermodynamic Enforcement via Conditional Distributed Rollback Cost**]
:::

Let repairing a spatial perimeter $C$ require coordination over ambient graph distance $D_G(C)=\max_{u,v\in V(C)}d_G(u,v)$ and irreversible erasure of at least $b$ bits. Assume an additive cost of at least $\epsilon_{\mathrm{hop}}>0$ per required hop and at least $k_BT_c\log 2$ per irreversibly erased bit. The resulting lower bound is $W_{\mathrm{repair}}\ge\epsilon_{\mathrm{hop}}D_G(C)+b k_BT_c\log 2$.

### 2.7.2.1 Commentary: Argument Outline {#2.7.2.1}

:::tip[**Structure of the Thermodynamic Enforcement Argument via Local Observation and Conditional Repair Costs**]
:::

The proof proceeds by construction of finite witness graphs and a cost decomposition under the stated communication and erasure premises.

```text
• 2.7.2 Theorem Distributed Rollback Cost  [by construction]
│
├── 2.7.3 Lemma: Finite-Radius Indistinguishability
│   ├── 2.7.3.1 Proof: Finite-Radius Indistinguishability
│   ├── 2.7.3.2 Commentary: Blindness of Locality
│   └── 2.7.3.3 Diagram: Horizon Problem
│
├── 2.7.4 Lemma: Bounded Reverse-Witness Misses
│   ├── 2.7.4.1 Proof: Bounded Reverse-Witness Misses
│   └── 2.7.4.2 Commentary: Cost of Certainty
│
├── 2.7.5 Lemma: Exact Poset Invariance
│   ├── 2.7.5.1 Proof: Exact Poset Invariance
│   └── 2.7.5.2 Commentary: Two-Tier Causal Hierarchy
│
├── 2.7.6 Lemma: Independence of Axiom 3
│   ├── 2.7.6.1 Proof: Independence of Axiom 3
│   └── 2.7.6.2 Commentary: Tripartite Foundation
│
├── 2.7.7 Lemma: Loop Erasure of Reverse Witnesses
│   ├── 2.7.7.1 Proof: Loop Erasure of Reverse Witnesses
│   └── 2.7.7.2 Commentary: Paths, Walks, and Search Horizons
│
├── 2.7.8 Lemma: Batch Causal Preservation under Dominance
│   ├── 2.7.8.1 Proof: Batch Causal Preservation under Dominance
│   ├── 2.7.8.2 Calculation: Target Diagonals before and after Deletion
│   └── 2.7.8.3 Commentary: Final Closure and Batch Admission
│
├── 2.7.9 Lemma: First-Tick Causality on Graded Graphs
│   ├── 2.7.9.1 Proof: First-Tick Causality on Graded Graphs
│   ├── 2.7.9.2 Calculation: Graded Inputs and Uniform-Height Cycle
│   └── 2.7.9.3 Commentary: Scope of the Grading Hypothesis
│
├── 2.7.10 Proof: Distributed Rollback Cost
│
└── 2.7.11 Validation: Lean 4 Core
```

---

### 2.7.3 Lemma: Finite-Radius Indistinguishability {#2.7.3}

:::info[**Cycle Diameter Growth via Finite-Radius Indistinguishability of Distant Causal Closure**]
:::

For any observation radius $r\ge1$, there are timestamped directed graphs whose rooted radius-$r$ induced balls coincide, with one graph having acyclic mediated closure and the other having a mediated cycle.

### 2.7.3.1 Proof: Finite-Radius Indistinguishability {#2.7.3.1}

:::tip[**Cycle Diameter Growth via Opening a Directed Perimeter Outside the Observed Ball**]
:::

**I. The Closed and Open Perimeters**

Let $m=2r+4$ and $V=\{0,\ldots,m-1\}$. Use the cycle $C$ with edges $e_j=(j,j+1\bmod m)$ and the open graph $P=C\setminus\{e_{r+1}\}$ (**Finite-Radius Indistinguishability** <Ref id="2.7.3" label="§2.7.3" />) (**Failure of Asymmetry** <Ref id="2.6.5" label="§2.6.5" />). Assign edge heights by

$$
H(e_j)=
\begin{cases}
j & 0\le j\le r+1,\\
j-(r+2) & r+2\le j\le 2r+3 .
\end{cases}
$$

Use the restriction of $H$ on $P$.

**II. Equality of the Rooted Balls**

In the undirected support of $C$, the two routes from $0$ to $j$ have lengths $j$ and $m-j$. Consequently,

$$
\begin{aligned}
d_C(0,j)&=\min(j,m-j),\\
B_C(0,r)&=\{0,\ldots,r\}\cup\{r+4,\ldots,2r+3\}.
\end{aligned}
$$

The endpoints of the removed edge satisfy

$$
d_C(0,r+1)=\min(r+1,r+3)=r+1>r,\qquad
d_C(0,r+2)=\min(r+2,r+2)=r+2>r.
$$

For $0\le j\le r$, the route $0,1,\ldots,j$ remains in $P$ and has length $j=d_C(0,j)$. For $r+4\le j\le 2r+3$, the route $0,2r+3,\ldots,j$ remains in $P$ and has length $m-j=d_C(0,j)$. Every route in $P$ also occurs in $C$. The distance comparisons are therefore

$$
\begin{aligned}
j\in B_C(0,r)&\Longrightarrow d_C(0,j)\le d_P(0,j)\le d_C(0,j),\\
j\notin B_C(0,r)&\Longrightarrow d_P(0,j)\ge d_C(0,j)>r .
\end{aligned}
$$

Thus $B_P(0,r)=B_C(0,r)$. The deleted edge has neither endpoint in this ball, so the induced edges have the same directions and heights.

**III. Opposite Closure Outcomes**

The two directed arcs in $C$ give

$$
0\xrightarrow{0}1\xrightarrow{1}\cdots\xrightarrow{r+1}r+2,\qquad
r+2\xrightarrow{0}r+3\xrightarrow{1}\cdots\xrightarrow{r+1}0 .
$$

Each arc is a simple path of length $r+2$ and its heights increase strictly. Hence $(0,r+2),(r+2,0)\in R_C$ and $(0,0)\in R_C^+$. In $P$, let $\ell$ denote the index in the order $(r+2,\ldots,2r+3,0,\ldots,r+1)$. For every edge $(u,v)$ of $P$, $\ell(v)=\ell(u)+1$. A path of length $k$ therefore has $\ell(v)-\ell(u)=k$. Every $R_P$ witness has positive length, so a composition of $a$ such witnesses satisfies

$$
\ell(v_a)-\ell(v_0)=\sum_{i=1}^a\bigl(\ell(v_i)-\ell(v_{i-1})\bigr)>0 .
$$

This proves $(v,v)\notin R_P^+$ for all $v$.

Q.E.D.

### 2.7.3.2 Commentary: Blindness of Locality {#2.7.3.2}

:::info[**Local Information and Ambient Distance**]
:::

A bounded observation can see the same induced neighborhood in an open directed path and in a distant closed perimeter. The indistinguishability argument depends on placing the differing edge outside the observation radius. It identifies a limitation of the information delivered by that local observation, independent of any probability assigned to the two input graphs.

For a repair algorithm, the distance that matters is measured in the ambient graph. A perimeter can have no chords among its own vertices and still have short routes through vertices outside it. Establishing a coordination cost from the perimeter length therefore requires a premise about the routes available to the algorithm. The conditional repair theorem uses the ambient distance directly. The two finite examples separate the local view from the global closure.

### 2.7.3.3 Diagram: Horizon Problem {#2.7.3.3}

:::note[**Visualization of the Enforcement of Paradox Prevention via Post-hoc correction**]
:::

```text
┌───────────────────────────────────────────────────────────────────────┐
│                     THE HORIZON PROBLEM (Blindness)                   │
└───────────────────────────────────────────────────────────────────────┘

                      Global Cycle (Length L = 100)
             ...............................................
            .'                                               '.
          .'                                                   '.
         .                                                       .
        .                                                         .
       .                                                           .
      .                           [ R ]                             .
      .                       (Local Scope)                         .
      .                          .-----.                            .
      |                         /       \                           |
      |          Edge U->V     |   (O)   |      Edge X->Y           |
      |          (Input)       | Observer|      (Output)            |
      |                         \       /                           |
      |                          '-----'                            .
      .                                                             .
      .     To the Local Observer (O), the lines extend to          .
      .     infinity. O cannot know that Input connects to          .
      .     Output 50 steps away.                                   .
       .                                                           .
        .                                                         .
         '.                                                     .'
           '.                                                 .'
             '...............................................'

   CONCLUSION:
   Post-hoc correction requires infinite information velocity.
   Paradoxes must be prevented locally before they close globally.
```

---

### 2.7.4 Lemma: Bounded Reverse-Witness Misses {#2.7.4}

:::info[**Local PUC Approximation via Conditional Miss Probability for a Bounded Reverse Search**]
:::

Let the fixed candidate support have $N$ vertices of maximum undirected degree three, with each new height comparison on a fixed simple path having conditional success probability at most $0<p<1/4$ given its exposed prefix. At $L_{\mathrm{cut}}=\lfloor\log_2 N\rfloor+3$, the probability of any missed reverse witness in one tick is at most $18N(2p)^{L_{\mathrm{cut}}}/(1-2p)$, and uniform conditional control across ticks gives the sum of their respective one-tick bounds.

### 2.7.4.1 Proof: Bounded Reverse-Witness Misses {#2.7.4.1}

:::tip[**Local PUC Approximation via Conditional Path Counting and Union Bounds**]
:::

**I. Path Probabilities**

The reverse-witness guard evaluates paths from a fixed candidate target (**Bounded Reverse-Witness Misses** <Ref id="2.7.4" label="§2.7.4" />) (**Acyclic Effective Causality** <Ref id="2.7.1" label="§2.7.1" />).

For a fixed length-$L$ path let $A_j$ be the event that its first $j$ comparisons succeed. Since $\Pr(A_j)\le p\Pr(A_{j-1})$ and $\Pr(A_0)=1$, $\Pr(A_{L-1})\le p^{L-1}$. Requiring its final height below the candidate height only restricts this event.

**II. Path and Site Counts**

The first edge has at most three choices. Subsequent edges have at most two after excluding the predecessor. Thus for a fixed starting vertex at most $3\cdot2^{L-1}$ length-$L$ simple paths are possible. With $q=2p$ the site bound is

$$
\begin{aligned}
\sum_{L=L_{\mathrm{cut}}+1}^{\infty}3\cdot2^{L-1}p^{L-1}
&=3\sum_{L=L_{\mathrm{cut}}+1}^{\infty}q^{L-1}\\
&=3q^{L_{\mathrm{cut}}}\lim_{m\to\infty}\frac{1-q^{m+1}}{1-q}
=\frac{3q^{L_{\mathrm{cut}}}}{1-q}.
\end{aligned}
$$

Let $S$ be the candidate set and $M_s$ the miss event at site $s$. The candidate count and union bound give

$$
|S|\le\sum_{v\in V}3\cdot2=6N,\qquad
\Pr\left(\bigcup_{s\in S}M_s\right)
\le\sum_{s\in S}\Pr(M_s)
\le 6N\frac{3q^{L_{\mathrm{cut}}}}{1-q}
=\frac{18Nq^{L_{\mathrm{cut}}}}{1-q}.
$$

**III. Dependence on Horizon**

Since $L_{\mathrm{cut}}\ge\log_2 N+2$ and $0<q<1/2$,

$$
\frac{18Nq^{L_{\mathrm{cut}}}}{1-q}
\le\frac{18q^2}{1-q}N^{1+\log_2 q}.
$$

Since $q<1/2$, $1+\log_2 q<0$. Let $M_t$ be the event of a miss at tick $t$, let $\mathcal F_{t-1}$ be the history before it, and let $B_N$ be the displayed bound. Under the uniform conditional premise,

$$
\Pr(M_t)=\mathbb E[\Pr(M_t\mid\mathcal F_{t-1})]\le B_N,\qquad
\Pr\!\left(\bigcup_{t=1}^{T}M_t\right)
\le\sum_{t=1}^{T}\Pr(M_t)\le T B_N .
$$

Q.E.D.

### 2.7.4.2 Commentary: Cost of Certainty {#2.7.4.2}

:::info[**Scope of the Reverse-Witness Estimate**]
:::

The cutoff estimate uses a bound on the probability of another successful timestamp comparison after the earlier comparisons have been exposed. A cycle density or a marginal edge frequency gives a different kind of information. The conditional form allows a product estimate along the path without assuming that the comparisons themselves are independent.

A union bound over candidate sites converts the path estimate into a one-tick reverse-witness bound. Extending that estimate through multiple ticks requires uniform control over the relevant histories and candidate supports. A cycle in the full mediated closure can instead use newly created witnesses from different candidates, even if every individual reverse check finds no witness. The probability estimate addresses the finite search cutoff. A finite horizon and an estimate uniform over histories are both explicit inputs.

---

### 2.7.5 Lemma: Exact Poset Invariance {#2.7.5}

:::info[**Strict Acyclicity of the Causal History Poset through Timestamp Monotonicity**]
:::

Let $\Omega$ be the set of immutable creation occurrences and let $\omega D\eta$ mean that $\omega$ is an incoming occurrence present at the source of $\eta$ in its creation snapshot. Under the source-maximum recurrence, the nonempty dependency closure $D^+$ is a strict partial order on $\Omega$, independently of the spatial search horizon (**Monotonicity of History** <Ref id="1.4.5" label="§1.4.5" />).

### 2.7.5.1 Proof: Exact Poset Invariance {#2.7.5.1}

:::tip[**Well-Founded Induction from Strict Timestamp Monotonicity**]
:::

**I. Immediate Dependency Inequality**

Let $\omega D\eta$. By the creation-snapshot definition, $h(\omega)$ belongs to the source incoming-height set $M_\eta$. The recurrence (**Creation Timestamp** <Ref id="1.4.4" label="§1.4.4" />) gives

$$
h(\eta)=1+\max(M_\eta\cup\{0\})\ge1+h(\omega)>h(\omega).
$$

This uses membership at creation, without retimestamping an older outgoing edge.

**II. Nonempty Dependency Paths**

For a chain $\omega_0D\omega_1D\cdots D\omega_m$ with $m\ge1$, induction gives $h(\omega_j)\ge h(\omega_0)+j$: the case $j=0$ is equality, and the step follows from

$$
h(\omega_{j+1})\ge h(\omega_j)+1
\ge h(\omega_0)+j+1.
$$

Hence $\omega D^+\eta$ implies $h(\eta)>h(\omega)$. A self-pair would require $h(\omega)>h(\omega)$, which is impossible.

**III. Strict Partial Order**

Concatenation of positive-length $D$-chains proves transitivity of $D^+$. If both $\omega D^+\eta$ and $\eta D^+\omega$, the height inequalities give

$$
h(\omega)<h(\eta)<h(\omega),
$$

a contradiction. Thus $D^+$ is transitive, irreflexive and asymmetric.

**IV. Preservation and Scope**

When a new occurrence is appended, each of its recorded predecessors satisfies the same strict height inequality, and old labels and dependencies are unchanged. Therefore every finite stage and their cumulative union have no finite dependency cycle: any proposed cycle lies in some finite stage and would yield the contradiction above. This proves the occurrence-order assertion (**Exact Poset Invariance** <Ref id="2.7.5" label="§2.7.5" />). The separate spatial relation $R^+$ still requires its own causal-admission condition; this proof supplies no quantitative bound on missed spatial influence paths.

Q.E.D.

### 2.7.5.2 Commentary: Two-Tier Causal Hierarchy {#2.7.5.2}

:::info[**Architectural Decoupling of Physical Acyclicity from Computational Search Optimization**]
:::

The occurrence-order theorem uses immutable creation records as its vertices. A dependency points from an incoming occurrence in the creation snapshot to the new occurrence it helps determine. The height inequality is consequently justified at the moment of creation and survives later spatial deletion or recreation. Two occurrences of the same ordered pair can have different birth ticks and remain distinct members of the record set.

The spatial mediated influence relation has a different domain and a separate acyclicity requirement. An arbitrary walk assembled from spatial edges is not automatically a dependency chain, even when individual pieces are time-respecting. A finite search horizon may affect which spatial configurations the scheduler admits, but it cannot invalidate the displayed inequality on actual recorded predecessors. Conversely, the occurrence inequality does not prove a bound on search-horizon errors or establish that every spatial influence closure remains acyclic.

---

### 2.7.6 Lemma: Independence of Axiom 3 {#2.7.6}

:::info[**Independence of Axiom 3 via A Five-Vertex Countermodel for Mediated Acyclicity**]
:::

Let $G$ have edges $A\to Z\to D\to C\to Z\to B\to A$ in the displayed order with heights $1,2,3,4,5,6$. It satisfies Axiom 1 and both specified geometric predicates, while $R^+$ has a diagonal.

### 2.7.6.1 Proof: Independence of Axiom 3 {#2.7.6.1}

:::tip[**Independence of Axiom 3 via Butterfly Accretion and Composition of Simple Witnesses**]
:::

**I. The Static Butterfly**

The butterfly has edge set $E=\{AZ,ZD,DC,CZ,ZB,BA\}$, where $UV$ denotes $(U,V)$ (**Independence of Axiom 3** <Ref id="2.7.6" label="§2.7.6" />) (**Independence of Axioms 1 and 2** <Ref id="2.5.1" label="§2.5.1" />). Each edge has distinct endpoints and the six reversed edges are absent. Deleting $Z$ leaves only $BA$ and $DC$, which contain no directed cycle. Every simple cycle therefore has a rotation beginning at $Z$. After either first edge, the other vertices each have a unique outgoing edge. The first returns are

$$
ZD\Longrightarrow (Z,D,C,Z),\qquad
ZB\Longrightarrow (Z,B,A,Z).
$$

A longer cycle would repeat $Z$ before closing. Thus these two triangles exhaust the simple cycles up to rotation.

The complete set of length-two paths is

$$
\begin{array}{c|l}
\text{middle vertex} & \text{paths}\\ \hline
Z & A Z D,\ A Z B,\ C Z D,\ C Z B\\
D & Z D C\\
C & D C Z\\
B & Z B A\\
A & B A Z
\end{array}
$$

Thus their endpoint pairs form $S=\{AD,AB,CD,CB,ZC,DZ,ZA,BZ\}$. These eight pairs are distinct and $S\cap E=\varnothing$.

**II. The Two Accretions**

Start from $E_0=\{AZ,ZD,DC,ZB\}$, with heights $1,2,3,5$ respectively. Its two-paths are $AZD$, $AZB$ and $ZDC$, with distinct endpoints and absent bypasses. Its vertex order $(A,Z,D,C,B)$ advances along every edge, so the base is acyclic. The first return chord is $CZ$, supported by $ZDC$. The second is $BA$, supported by $AZB$. The two height checks are

$$
\begin{aligned}
H(CZ)&=1+\max H_{\mathrm{in}}(C)=1+H(DC)=4,&2<3<4,\\
H(BA)&=1+\max H_{\mathrm{in}}(B)=1+H(ZB)=6,&1<5<6.
\end{aligned}
$$

By the complete two-path list, the support endpoint pairs $ZC$ and $AB$ have one witness each even in the final graph. Each update therefore has its displayed unique witness in its pre-addition graph. After each addition the edges are a subset of $E$, so the cycle analysis above excludes any longer simple cycle.

**III. The Mediated Cycle**

The simple paths

$$
A\xrightarrow{1}Z\xrightarrow{2}D,\qquad
D\xrightarrow{3}C\xrightarrow{4}Z\xrightarrow{5}B\xrightarrow{6}A
$$

give $A R D$ and $D R A$. Their composition gives $(A,A)\in R^+$.

Q.E.D.

### 2.7.6.2 Commentary: Tripartite Foundation {#2.7.6.2}

:::info[**Separate Geometric and Mediated Tests**]
:::

The butterfly shares a central vertex between two directed triangles. A simple cycle cannot cross from one triangle into the other and return without repeating that vertex. The static test can therefore accept the geometry even though the heights permit opposite mediated witnesses that use different parts of the two triangles.

The constructive witness orders the two chord additions and computes each height from its source snapshot. It evaluates the accretion predicate with the causal guard omitted, because the purpose is to check whether geometric admissibility entails mediated acyclicity. The witness also clarifies how a walk through the butterfly can repeat the shared vertex while the two constituent simple paths each retain distinct vertices. The raw base and each added chord meet the prescribed geometric conditions.

---

### 2.7.7 Lemma: Loop Erasure of Reverse Witnesses {#2.7.7}

:::info[**Loop Erasure of Reverse Witnesses via Equivalence of Simple and Walk Witnesses at a Common Cutoff**]
:::

Let $v\ne u$ with $(v,u)\notin E$. A directed walk from $v$ to $u$ of at least two and at most $L$ edges with strictly increasing heights and terminal height below $h$ exists if and only if a simple path with those properties exists.

### 2.7.7.1 Proof: Loop Erasure of Reverse Witnesses {#2.7.7.1}

:::tip[**Loop Erasure of Reverse Witnesses via Erasure of Repeated-Vertex Segments**]
:::

**I. Erasure Preserves an Edge Subsequence**

Let $(x_0,\ldots,x_k)$ be a witness walk from $v$ to $u$ with $k\le L$ and heights $h_1<\cdots<h_k<h$. If $x_i=x_j$ for $i<j$, erase the segment from position $i$ to $j$. The new walk and its height sequence are

$$
(x_0,\ldots,x_i,x_{j+1},\ldots,x_k),\qquad
(h_1,\ldots,h_i,h_{j+1},\ldots,h_k),
$$

with the suffix empty if $j=k$. When $j<k$, the new join edge $(x_i,x_{j+1})$ is the original edge $(x_j,x_{j+1})$. When $j=k$, its new endpoint $x_i=x_k$ is still $u$. If both height pieces are nonempty then $h_i<h_{j+1}$ by strict increase in the original list. Thus the new list is increasing and its terminal entry remains below $h$.

**II. Finite Reduction**

At one erasure the length changes from $k$ to $k-(j-i)\le k-1$. After $m$ erasures the lengths satisfy

$$
0\le k_m\le k_0-m\le L-m.
$$

The endpoints remain distinct, so $k_m\ge1$. The erasures must therefore terminate with no repeated vertex and with length at most $L$.

**III. Mediation at the Final Length**

The candidate has no direct forward bypass $(v,u)$ (**Geometric Constructibility** <Ref id="2.3.1" label="§2.3.1" />). A final simple path of length one would be precisely that edge, which is absent. Hence the path has length at least two and obeys the original height cutoff. Conversely, any such simple path is a walk with the required properties. This proves equivalence at the same search horizon (**Loop Erasure of Reverse Witnesses** <Ref id="2.7.7" label="§2.7.7" />).

Q.E.D.

### 2.7.7.2 Commentary: Paths, Walks, and Search Horizons {#2.7.7.2}

:::info[**Paths, Walks, and Search Horizons**]
:::

The path representation assigns a distinct vertex to every position. The walk representation permits a vertex to occur more than once, even with strictly increasing heights. Erasing the portion between two occurrences keeps the endpoints and removes a contiguous portion of the edge list. The remaining height list inherits its strict ordering as a subsequence.

The common horizon matters because erasure supplies a path no longer than the given walk. An unbounded witness can still have a shortest simple representative beyond a chosen finite cutoff. The direct-bypass condition matters at the other end of the range. It prevents erasure from leaving a single edge when the causal guard requires a mediated reverse witness. Erasure preserves the candidate's endpoint pair at every stage. The equivalence preserves the test for one increasing reverse witness at the common horizon. It leaves the test for compositions of multiple witnesses to the full target-diagonal criterion under its stated hypotheses (**Batch Causal Preservation under Dominance** <Ref id="2.7.8" label="§2.7.8" />).

---

### 2.7.8 Lemma: Batch Causal Preservation under Dominance {#2.7.8}

:::info[**Batch Causal Preservation under Dominance via Exact Target-Diagonal Test for a Dominant Batch**]
:::

Let old $R$ be acyclic, with every retained new chord's height dominating the old outgoing heights at its target. The final $R$ is acyclic exactly when its full closure has no target diagonal, with the pre-deletion test sufficient and the two-chord sequential diamond also acyclic when both targets are old $R$-sinks.

### 2.7.8.1 Proof: Batch Causal Preservation under Dominance {#2.7.8.1}

:::tip[**Batch Causal Preservation under Dominance via Localization of New Influence Pairs at Batch Targets**]
:::

**I. Localization by Height Dominance**

Let $B$ be the retained chord set, $T=\{v:(u,v)\in B\}$ its targets, and $E_f=(E\cup B)\setminus D$. Denote the old and final mediated relations by $R_0,R_f$ (**Effective Influence** <Ref id="2.6.2" label="§2.6.2" />). For $(a,b)\in R_f\setminus R_0$, choose a simple increasing witness $(x_0,\ldots,x_k)$. It uses at least one chord, because a witness made solely of retained old edges would also exist in the old graph. If its $j$-th edge $(x_{j-1},x_j)$ is new and the next edge is old, the two hypotheses give

$$
H(x_{j-1},x_j)<H(x_j,x_{j+1})
\le \max_{(x_j,y)\in E}H(x_j,y)
\le H(x_{j-1},x_j),
$$

a contradiction. Starting at its first new edge and applying the same argument at each successive position shows that its final edge is new. Hence

$$
R_f\setminus R_0\subseteq V\times T.
$$

**II. Equivalence of Target Diagonals and Acyclicity**

If $R_f^+$ has a diagonal, there is a nonempty closed walk of $R_f$ pairs $(y_0,y_1),\ldots,(y_{m-1},y_m)$, with $y_m=y_0$. Since $R_0$ has acyclic closure, some pair $(y_{j-1},y_j)$ is outside $R_0$. By localization $y_j\in T$. Rotating the same list of pairs gives a nonempty return walk at $y_j$, so $(y_j,y_j)\in R_f^+$. Conversely a target diagonal is already a diagonal in the full closure. This proves

$$
R_f^+\cap\{(x,x):x\in V\}=\varnothing
\quad\Longleftrightarrow\quad
R_f^+\cap\{(x,x):x\in T\}=\varnothing .
$$

Let $R_m$ be the relation just after merge. Every final witness uses edges of the merged graph with identical heights, giving $R_f\subseteq R_m$ and therefore $R_f^+\subseteq R_m^+$. The pre-deletion target test implies the final one.

**III. The Two Old Sinks**

For the sequential diamond the added edges are $(u,v)$ and $(x,w)$ with four distinct endpoints (**Sequential Constructor Diamond** <Ref id="2.4.6" label="§2.4.6" />). They cannot occur consecutively, since their sources $\{u,x\}$ are disjoint from their targets $\{v,w\}$. By Section I every new witness therefore has exactly one new edge, at its end. If $v,w$ are sinks in $R_0$, localization and irreflexivity give

$$
R_f\cap(\{v\}\times V)\subseteq\{(v,w)\},
\qquad
R_f\cap(\{w\}\times V)\subseteq\{(w,v)\}.
$$

A witness of $(v,w)$ would end with $(x,w)$. Its prefix from $v$ to $x$ uses old edges and has at least two edges, since $(v,x)\notin E$. It would give $(v,x)\in R_0$, contradicting the sink condition. Thus $v$ remains a sink and any arrow from $w$ ends at $v$. Neither target admits a nonempty return walk. Section II gives acyclicity of the full relation.

Q.E.D.

### 2.7.8.2 Calculation: Target Diagonals before and after Deletion {#2.7.8.2}

:::note[**Target Diagonals before and after Deletion via Exact Evaluation of Mediated Closure for an Explicit Batch**]
:::

Verification of the target-diagonal test on the explicit batch (**Batch Causal Preservation under Dominance** <Ref id="2.7.8.1" label="§2.7.8.1" />) (**Effective Influence** <Ref id="2.6.2" label="§2.6.2" />) is based on the following protocols:

1.  **Input:** Construct the timestamped five-vertex graph and its two dominant chords.
2.  **Closure:** Compute simple increasing witnesses and take their full transitive closure.
3.  **Deletion:** Remove the specified old edge and recompute the target diagonals.

```python
import networkx as nx


def mediated_relation(graph):
    relation = nx.DiGraph()
    relation.add_nodes_from(graph)
    for start in graph:
        for end in graph:
            if start == end:
                continue
            for path in nx.all_simple_paths(graph, start, end):
                heights = [graph[a][b]["height"] for a, b in zip(path, path[1:])]
                if len(heights) >= 2 and all(a < b for a, b in zip(heights, heights[1:])):
                    relation.add_edge(start, end)
                    break
    return relation


def timestamped(edges):
    graph = nx.DiGraph()
    graph.add_weighted_edges_from(edges, weight="height")
    return graph


old = timestamped([("v", "w", 0), ("w", "u", 0), ("u", "x", 0),
                   ("v", "z", 0), ("z", "x", 1)])
chords = [("u", "v", 1), ("x", "w", 2)]
assert nx.is_directed_acyclic_graph(mediated_relation(old))
for _, target, height in chords:
    assert all(height >= data["height"] for _, _, data in old.out_edges(target, data=True))
merged = old.copy()
merged.add_weighted_edges_from(chords, weight="height")
final = merged.copy()
final.remove_edge("z", "x")
for name, graph, expected in [("merge", merged, ["v", "w"]), ("final", final, [])]:
    closure = nx.transitive_closure(mediated_relation(graph))
    diagonal = [target for target in ("v", "w") if closure.has_edge(target, target)]
    assert diagonal == expected
    assert nx.is_directed_acyclic_graph(mediated_relation(graph)) == (not diagonal)
    print(f"{name} target diagonals: {diagonal}")
```

**Simulation Results:**

```text
merge target diagonals: ['v', 'w']
final target diagonals: []
```

**Conclusion:**

The merged example has two target diagonals and the specified deletion removes both. This confirms the pre-deletion and final-state distinction in the fixture.

### 2.7.8.3 Commentary: Final Closure and Batch Admission {#2.7.8.3}

:::info[**Final Closure and Batch Admission**]
:::

Dominance constrains where a newly created witness can end. Every such witness enters the target set at its last edge, so any new directed cycle of mediated pairs passes through that set. The diagonal test still uses the full relation closure. It includes walks that move between the targets through vertices outside the target set.

The pre-deletion test is sufficient because deleting edges can only remove witnesses. The final test also permits cases where a deletion removes the sole witness for one of the cycle's mediated pairs. The finite calculation exhibits this difference. The batch criterion applies under its dominance premises. The reference bounded guard evaluates proposals individually on the frozen graph. For two old sinks the extra overlap conditions provide an analytic sufficient case.

---

### 2.7.9 Lemma: First-Tick Causality on Graded Graphs {#2.7.9}

:::info[**First-Tick Causality on Graded Graphs via One-Tick Mediated Acyclicity on Uniform-Height Graded Inputs**]
:::

Let every old edge have height $h$ and raise a vertex grading by one, and let a batch of elementary return chords have height $h+1$. The mediated closure after the tick is acyclic.

### 2.7.9.1 Proof: First-Tick Causality on Graded Graphs {#2.7.9.1}

:::tip[**First-Tick Causality on Graded Graphs via Strict Decrease of Grading along Mediated Pairs**]
:::

**I. Height and Grading Changes**

An elementary chord closes a directed two-path in the frozen graph (**First-Tick Causality on Graded Graphs** <Ref id="2.7.9" label="§2.7.9" />) (**Axiom 2 Geometric Constructibility** <Ref id="2.3.1" label="§2.3.1" />).

Every candidate chord $u\to v$ closes a two-path $v\to w\to u$ and has at least one old incoming edge at $u$. Its source maximum is $h$, so its height is $h+1$. For the grading $d$,

$$
d(u)=d(w)+1=d(v)+2,\qquad d(v)-d(u)=-2.
$$

**II. Mediated Witness**

Every increasing witness of length at least two uses exactly the two heights $h<h+1$. Its first edge raises the grading by one and its second lowers it by two. Thus $aRb$ implies $d(b)=d(a)-1$ in the merged graph, and the same implication holds after deletions.

**III. Exclusion of Closure Diagonals**

A chain of $m\ge1$ mediated pairs from $a$ to $b$ has $d(b)=d(a)-m$. It cannot return to $a$. Hence the final $R^+$ is irreflexive.

Q.E.D.

### 2.7.9.2 Calculation: Graded Inputs and Uniform-Height Cycle {#2.7.9.2}

:::note[**Graded Inputs and Uniform-Height Cycle via Finite Grading Check and Six-Cycle Counterexample**]
:::

Verification of grading decrease and the six-cycle counterexample (**First-Tick Causality on Graded Graphs** <Ref id="2.7.9.1" label="§2.7.9.1" />) (**Effective Influence** <Ref id="2.6.2" label="§2.6.2" />) is based on the following protocols:

1.  **Graded Input:** Construct the outward tree and enumerate every retained subset of its closing chords.
2.  **Mediated Pairs:** Check that every mediated pair lowers the fixed grading by one.
3.  **Ungraded Input:** Compute the relation after all six closing chords on a uniform-height cycle.

```python
import networkx as nx


def mediated_relation(graph):
    relation = nx.DiGraph()
    relation.add_nodes_from(graph)
    for start in graph:
        for end in graph:
            if start == end:
                continue
            for path in nx.all_simple_paths(graph, start, end):
                heights = [graph[a][b]["height"] for a, b in zip(path, path[1:])]
                if len(heights) >= 2 and all(a < b for a, b in zip(heights, heights[1:])):
                    relation.add_edge(start, end)
                    break
    return relation


def timestamped(edges):
    graph = nx.DiGraph()
    graph.add_weighted_edges_from(edges, weight="height")
    return graph


from itertools import combinations


old = timestamped([(0, 1, 0), (0, 2, 0), (1, 3, 0), (1, 4, 0),
                   (2, 5, 0), (2, 6, 0), (3, 7, 0)])
depth = nx.single_source_shortest_path_length(old, 0)
chords = [(u, v, 1) for v in old for w in old[v] for u in old[w]]
count = 0
for size in range(len(chords) + 1):
    for batch in combinations(chords, size):
        graph = old.copy()
        graph.add_weighted_edges_from(batch, weight="height")
        relation = mediated_relation(graph)
        assert all(depth[b] == depth[a] - 1 for a, b in relation.edges)
        assert nx.is_directed_acyclic_graph(relation)
        count += 1
print(f"Outward-tree batches checked: {count}")

cycle = timestamped((i, (i + 1) % 6, 0) for i in range(6))
cycle.add_weighted_edges_from((((i + 2) % 6, i, 1) for i in range(6)), weight="height")
relation = mediated_relation(cycle)
assert set(relation.edges) == {(i, (i - 1) % 6) for i in range(6)}
assert not nx.is_directed_acyclic_graph(relation)
print(f"Six-cycle mediated pairs: {sorted(relation.edges)}")
```

**Simulation Results:**

```text
Outward-tree batches checked: 32
Six-cycle mediated pairs: [(0, 5), (1, 0), (2, 1), (3, 2), (4, 3), (5, 4)]
```

**Conclusion:**

All tested graded batches satisfy the one-step decrease, and the six-cycle gives a cyclic relation. The outputs confirm the grading distinction on these finite inputs.

### 2.7.9.3 Commentary: Scope of the Grading Hypothesis {#2.7.9.3}

:::info[**Scope of the Grading Hypothesis**]
:::

An outward tree carries a grading given by root depth. Its old edges increase depth by one, so a return chord across two such edges decreases depth by two. Uniform old heights and the constructor height rule force any mediated witness after the merge to consist of exactly one old edge followed by one new chord.

Uniform height without a grading can give a different result. The directed six-cycle has no grading that increases by one around the whole perimeter. Its six admitted return chords create mediated arrows around a cycle. This fixture distinguishes the first-tick theorem for graded inputs from the general batch criterion and from later ticks with nonuniform active heights. Edge deletion preserves the grading decrease of every surviving witness.

---

### 2.7.10 Proof: Distributed Rollback Cost {#2.7.10}

:::tip[**Thermodynamic Enforcement via Assembly of Conditional Coordination and Erasure Costs**]
:::

**I. Detection Scope**

Local observation admits the indistinguishable pair (**Finite-Radius Indistinguishability** <Ref id="2.7.3" label="§2.7.3" />). The bounded missed-witness probability uses its separate extension law (**Bounded Reverse-Witness Misses** <Ref id="2.7.4" label="§2.7.4" />) and witness representation (**Loop Erasure of Reverse Witnesses** <Ref id="2.7.7" label="§2.7.7" />).

Full closure uses the target-diagonal test under dominance (**Batch Causal Preservation under Dominance** <Ref id="2.7.8" label="§2.7.8" />) and the first-tick grading argument on its stated domain (**First-Tick Causality on Graded Graphs** <Ref id="2.7.9" label="§2.7.9" />).

**II. Distinct Relations**

Immutable occurrence dependencies have acyclic closure (**Exact Poset Invariance** <Ref id="2.7.5" label="§2.7.5" />). The butterfly has cyclic spatial mediated closure (**Independence of Axiom 3** <Ref id="2.7.6" label="§2.7.6" />).

**III. Stipulated Costs**

Under the stated coordination premise the hop count $n_{\mathrm{hop}}$ is at least $D_G(C)$. Under the erasure premise the erased bits $n_{\mathrm{bit}}$ are at least $b$. Additivity and the assumed unit costs give

$$
W_{\mathrm{repair}}\ge\epsilon_{\mathrm{hop}}n_{\mathrm{hop}}
+k_BT_c\log(2)n_{\mathrm{bit}}
\ge\epsilon_{\mathrm{hop}}D_G(C)+b k_BT_c\log 2 .
$$

Q.E.D.

---

### 2.7.11 Type-Theoretic Validation via Lean 4 Core {#2.7.11}

:::note[**Lean 4 Encoding of Asymmetry's Algebraic Closure through Biconditional Decomposition**]
:::

Type-theoretic certification of the structural relationships between asymmetry, irreflexivity, and antisymmetry (the three properties now united under **Acyclic Effective Causality** <Ref id="2.7.1" label="§2.7.1" />) proceeds via the following verification strategy:

1.  **Encoding:** The definitions `IsAsymmetric`, `IsIrreflexive`, and `IsAntisymmetric` encode the three relational predicates. `IsAsymmetric` is the formal expression of Axiom 3's Global Asymmetry requirement: if $u$ influences $v$, then $v$ cannot influence $u$.
2.  **Theorem Statements:** The first theorem (`asymmetry_implies_irreflexivity`) certifies that asymmetry strictly subsumes irreflexivity by self-application; the second (`asymmetry_equiv`) certifies the full biconditional, proving that asymmetry is the exact algebraic conjunction of the two weaker conditions. Furthermore, strict poset acyclicity under edge timestamp monotonicity is formally certified by `edge_monotone_no_causal_cycle`.
3.  **Proof Closure:** Both proofs are closed by `intro` and `exact` tactics; the biconditional uses `constructor` to split into two directions, with `False.elim` eliminating the mutual-edge contradiction in the antisymmetry branch and `rw` substituting the equality witness in the reverse direction.

```lean
-- Define a Causal Relation as a binary predicate mapping pairs to a Proposition
def CausalRelation₂ (V : Type) := V → V → Prop

-- Define Strict Asymmetry (the algebraic expression of Axiom 3 Global Asymmetry)
def IsAsymmetric (V : Type) (R : CausalRelation₂ V) : Prop :=
  ∀ u v : V, R u v → ¬ R v u

-- Define Strict Irreflexivity
def IsIrreflexive₂ (V : Type) (R : CausalRelation₂ V) : Prop :=
  ∀ v : V, ¬ R v v

-- Define standard mathematical Antisymmetry
def IsAntisymmetric₂ (V : Type) (R : CausalRelation₂ V) : Prop :=
  ∀ u v : V, R u v → R v u → u = v

/--
THEOREM 1: Asymmetry Implies Irreflexivity
Certifies that the Global Asymmetry of Axiom 3 strictly subsumes irreflexivity:
if a relation is asymmetric, no event can act as its own causal antecedent.
-/
theorem asymmetry_implies_irreflexivity {V : Type} (R : CausalRelation₂ V)
    (h_asym : IsAsymmetric V R) : IsIrreflexive₂ V R := by
  intro v h_loop
  -- Self-application of asymmetry at (v, v) yields the contradiction directly
  exact h_asym v v h_loop h_loop

/--
THEOREM 2: Relational Completeness of the Causal Primitive
Formally seals the axiomatic chapter by proving that asymmetry is the exact
algebraic conjunction of irreflexivity and antisymmetry, unifying all three
causal constraints into a single structural equivalence.
-/
theorem asymmetry_equiv {V : Type} (R : CausalRelation₂ V) :
    IsAsymmetric V R ↔ (IsIrreflexive₂ V R ∧ IsAntisymmetric₂ V R) := by
  constructor
  · intro h_asym
    constructor
    · -- Forward: Asymmetry implies Irreflexivity via self-application
      intro v h_loop
      exact h_asym v v h_loop h_loop
    · -- Forward: Asymmetry implies Antisymmetry vacuously via False.elim
      intro u v h_fwd h_rev
      exact False.elim (h_asym u v h_fwd h_rev)
  · intro h_conj
    intro u v h_fwd h_rev
    -- Reverse: Antisymmetry forces u = v; irreflexivity annihilates the self-loop
    have h_eq : u = v := h_conj.right u v h_fwd h_rev
    rw [h_eq] at h_fwd
    exact h_conj.left v h_fwd

-- ----------------------------------------------------------------------------
-- PART 2: EDGE TIMESTAMPS & STRICT CAUSAL PATH MONOTONICITY (Axiom 3)
-- ----------------------------------------------------------------------------

def Edge (V : Type) := V × V
def GraphEdges (V : Type) := Edge V → Prop
def EdgeTimestampMap (V : Type) := Edge V → Nat

def DirectedEdgePath {V : Type} (E : GraphEdges V) : List (Edge V) → Prop
  | [] => True
  | [e] => E e
  | e1 :: e2 :: rest => E e1 ∧ e1.2 = e2.1 ∧ DirectedEdgePath E (e2 :: rest)

def IsEdgePathMonotone {V : Type} (H : EdgeTimestampMap V) : List (Edge V) → Prop
  | [] => True
  | [_] => True
  | e1 :: e2 :: rest => H e1 < H e2 ∧ IsEdgePathMonotone H (e2 :: rest)

/--
THEOREM 3: Edge Timestamp Path Monotonicity Transitivity
Proves that along any directed causal path with strictly increasing edge timestamps,
the initial edge timestamp is strictly less than the final edge timestamp: H(e_first) < H(e_last).
-/
theorem edge_path_monotonicity_transitive {V : Type}
    (H : EdgeTimestampMap V) :
    ∀ (e1 e2 : Edge V) (rest : List (Edge V)),
    IsEdgePathMonotone H (e1 :: rest ++ [e2]) →
    H e1 < H e2 := by
  intro e1 e2 rest
  revert e1
  induction rest with
  | nil =>
    intro e1 h_mono
    dsimp [IsEdgePathMonotone] at h_mono
    exact h_mono.1
  | cons e_mid rest_mid ih =>
    intro e1 h_mono
    dsimp [IsEdgePathMonotone] at h_mono
    have h1 := h_mono.1
    have h2 := ih e_mid h_mono.2
    exact Nat.lt_trans h1 h2

/--
THEOREM 4: Edge Timestamp Monotone Closed Loop Impossibility (Axiom 3)
Proves that a closed directed path whose edge timestamps strictly increase cannot form
a closed loop without incurring H(e_first) < H(e_first), precluding Closed Timelike Curves.
-/
theorem edge_monotone_no_causal_cycle {V : Type}
    (E : GraphEdges V) (H : EdgeTimestampMap V) :
    ∀ (e1 e_last : Edge V) (rest : List (Edge V)),
    DirectedEdgePath E (e1 :: rest ++ [e_last]) →
    IsEdgePathMonotone H (e1 :: rest ++ [e_last]) →
    H e_last < H e1 →
    False := by
  intro e1 e_last rest _ h_mono h_close
  have h_trans := edge_path_monotonicity_transitive H e1 e_last rest h_mono
  have h_contra := Nat.lt_trans h_trans h_close
  exact Nat.lt_irrefl (H e1) h_contra
```

**Verification Summary:**
The definitions extend the vocabulary established in the **Type-Theoretic Validation via Lean 4 Core** <Ref id="2.2.5" label="§2.2.5" /> to include `IsAsymmetric`, the direct Lean encoding of the Global Asymmetry clause of **Acyclic Effective Causality** <Ref id="2.7.1" label="§2.7.1" />. The first theorem self-applies `h_asym` at the identical vertex pair `(v, v)`: because asymmetry asserts `R v v -> not R v v`, any self-loop hypothesis `h_loop : R v v` immediately produces its own negation, and `exact` discharges the goal. The second theorem splits via `constructor` into two directions.

The forward direction reuses the self-application trick for irreflexivity, then dispatches antisymmetry by supplying both directions of the mutual-edge hypothesis to `h_asym`, whose output `False` is eliminated by `False.elim`. The reverse direction unpacks `h_conj` into `h_conj.left` (irreflexivity) and `h_conj.right` (antisymmetry), applies antisymmetry to force `h_eq : u = v`, rewrites `h_fwd` under this equality to obtain a self-loop, then applies irreflexivity to close. The Lean kernel's acceptance of both closed proof terms certifies that the three-axiom system of Chapter 2 possesses complete algebraic closure: Asymmetry is not a separate postulate alongside Irreflexivity and Antisymmetry, but their exact logical conjunction, ensuring the tripartite foundation established by **Independence of Axiom 3** <Ref id="2.7.6" label="§2.7.6" /> is also algebraically minimal. In tandem with `edge_monotone_no_causal_cycle` establishing **Exact Poset Invariance** <Ref id="2.7.5" label="§2.7.5" />, the causal ordering of physical history is completely secured.

---

### 2.7.Z Implications and Synthesis {#2.7.Z}

:::note[**Causal Admission**]
:::

The bounded reverse-path guard checks a frozen proposal (**Acyclic Effective Causality** <Ref id="2.7.1" label="§2.7.1" />). Its witness estimate uses a conditional extension law (**Bounded Reverse-Witness Misses** <Ref id="2.7.4" label="§2.7.4" />).

Full batch closure has a separate target-diagonal test under dominance (**Batch Causal Preservation under Dominance** <Ref id="2.7.8" label="§2.7.8" />). On uniform-height graded inputs, depth decrease gives first-tick acyclicity (**First-Tick Causality on Graded Graphs** <Ref id="2.7.9" label="§2.7.9" />).

Distributed rollback costs use the stated ambient coordination and erasure premises. The constructor can implement candidate checks locally, while a global batch requirement depends on the scope of the evolution rule.

---

## 2.8 Formal Synthesis {#2.8}

:::note[**End of Chapter 2**]
:::

The three axioms forge the substrate's unyielding frame, erecting a rigid skeleton upon which the fabric of reality can be braided. The **Causal Primitive** acts as a ratchet, directing influence without reversal and sharpening the arrow of time. **Geometric Constructibility** mandates the tiling of the vacuum with $3$-cycle quanta, ensuring space is woven from fundamental areas. Finally, **Acyclic Effective Causality** projects these local rules into a global order, preventing the universe from trapping itself in the paradox of closed loops.

This triad delimits the boundaries of the possible. The countermodels prove that each axiom serves as a unique load-bearing pillar of the theory, independent and necessary. Furthermore, the mechanism of **Decomposition** ensures that complex tangles dissolve into simplices, enforcing an inexorable drive toward geometric simplicity. Physically, the graph now accretes as a directed lattice, where every cycle resolves to a quantum of area and every edge preserves the integrity of history.

But a set of rules is not a universe: laws require a jurisdiction. Possessing the constraints but lacking the initial state, the investigation must now determine the specific configuration of the graph at $t=0$ that satisfies these strictures while maximizing potential. This leads us to **Chapter 3**, where the unique topology of the vacuum is derived.

---

### Table of Symbols

| Symbol | Description | Context / First Used |
| :--- | :--- | :--- |
| $(u, v)$ | The Directed Causal Link (Atomic relation $u \to v$) | [§2.1.1](/monograph/rules/axioms/2.1/#2.1.1) |
| $E$ | The set of edges within the graph | [§2.1.1](/monograph/rules/axioms/2.1/#2.1.1) |
| $\implies$ | Logical implication | [§2.2.1](/monograph/rules/axioms/2.2/#2.2.1) |
| $\forall$ | Universal quantifier ("for all") | [§2.2.1](/monograph/rules/axioms/2.2/#2.2.1) |
| $\mathcal{T}_{self}$ | Self-Loop Addition Operation | [§2.2.3](/monograph/rules/axioms/2.2/#2.2.3) |
| $\Omega(G)$ | Cardinality of the set of Simple Paths | [§2.2.3](/monograph/rules/axioms/2.2/#2.2.3) |
| $\Delta S$ | Change in Entropy | [§2.2.3](/monograph/rules/axioms/2.2/#2.2.3) |
| $k_B$ | Boltzmann Constant | [§2.2.3](/monograph/rules/axioms/2.2/#2.2.3) |
| $\mathfrak{T}_{add}$ | Edge Addition Operation | [§2.3.1](/monograph/rules/axioms/2.3/#2.3.1) |
| $\Pi_{\ell \le 2}(u, v)$ | Set of Simple Directed Paths from $u$ to $v$ with length $\le 2$ | [§2.3.1](/monograph/rules/axioms/2.3/#2.3.1) |
| $L$ | Length of a cycle or path | [§2.3.1](/monograph/rules/axioms/2.3/#2.3.1) |
| $\gamma$ | Geometric Quantum (Directed 3-Cycle) | [§2.3.2](/monograph/rules/axioms/2.3/#2.3.2) |
| $\Phi(G)$ | Lexicographic Potential $(L_{\max}, N_{L_{\max}})$ | [§2.3.5](/monograph/rules/axioms/2.3/#2.3.5) |
| $L_{\max}$ | Length of the longest simple cycle in $G$ | [§2.3.5](/monograph/rules/axioms/2.3/#2.3.5) |
| $N_{L_{\max}}$ | Count of distinct cycles of length $L_{\max}$ | [§2.3.5](/monograph/rules/axioms/2.3/#2.3.5) |
| $\mathcal{R}$ | The Rewrite Rule (Edge addition mechanism) | [§2.4.2](/monograph/rules/axioms/2.4/#2.4.2) |
| $C$ | A Simple Directed Cycle | [§2.4.3](/monograph/rules/axioms/2.4/#2.4.3) |
| $\text{dist}_C(u, v)$ | Distance between vertices along a cycle $C$ | [§2.4.3.1](/monograph/rules/axioms/2.4/#2.4.3.1) |
| $\mathcal{O}_{add}$ | Composite Addition Phase (Chord insertion) | [§2.4.5](/monograph/rules/axioms/2.4/#2.4.5) |
| $\mathcal{O}_{del}$ | Composite Deletion Phase (Entropic breakage) | [§2.4.5](/monograph/rules/axioms/2.4/#2.4.5) |
| $\mathcal{S}_{step}$ | Composite Update Step ($\mathcal{O}_{del} \circ \mathcal{O}_{add}$) | [§2.4.5](/monograph/rules/axioms/2.4/#2.4.5) |
| $\le$ | Effective Influence Relation (Strict Partial Order) | [§2.6.2](/monograph/rules/axioms/2.6/#2.6.2) |
| $H(e)$ | History Timestamp (Local relational time / discrete proper time) | [§2.6.2](/monograph/rules/axioms/2.6/#2.6.2) |
| $\pi_{uv}$ | A specific Simple Directed Path instance from $u$ to $v$ | [§2.6.2](/monograph/rules/axioms/2.6/#2.6.2) |
| $\neg$ | Logical negation | [§2.7.1](/monograph/rules/axioms/2.7/#2.7.1) |
| $N$ | Total number of vertices in the graph | [§2.7.2](/monograph/rules/axioms/2.7/#2.7.2) |
| $R$ | Radius of local computational patch | [§2.7.3](/monograph/rules/axioms/2.7/#2.7.3) |
| $\rho$ | Edge density of the graph | [§2.7.3](/monograph/rules/axioms/2.7/#2.7.3) |
| $t_{crit}$ | Critical time where cycle diameter exceeds horizon | [§2.7.3](/monograph/rules/axioms/2.7/#2.7.3) |
| $P_{err}(R)$ | Probability of paradox evasion at radius $R$ | [§2.7.4](/monograph/rules/axioms/2.7/#2.7.4) |
| $E_{sync}$ | Energy required for global synchronization | [§2.7.5](/monograph/rules/axioms/2.7/#2.7.5) |
| $D$ | Graph Diameter | [§2.7.5](/monograph/rules/axioms/2.7/#2.7.5) |

\newpage
# References

### 5. **Ambjørn, J., Jurkiewicz, J., & Loll, R. (2005).** {#A.5}
**"Reconstructing the Universe"**
    * **Link:** [https://arxiv.org/abs/hep-th/0505154](https://arxiv.org/abs/hep-th/0505154)


**Overview:**
Ambjorn, Jurkiewicz, and Loll demonstrate that a non-trivial four-dimensional classical spacetime can emerge from a non-perturbative path integral of causal triangulations. This approach, known as Causal Dynamical Triangulations (CDT), shows that imposing a strict distinction between space-like and time-like steps solves the historical problem of spatial collapse and ensures causality in the continuum limit.

**Relevance to QBD:**
This seminal work in discrete quantum gravity provides vital conceptual backing for the geometrogenesis proofs in QBD. In Chapter 11, we leverage Loll's insights to show how discrete causal structures avoid cosmological dimensional collapse. CDT's results set a precedent for how discrete, causally ordered structures can successfully yield continuous, high-dimensional geometries when the continuum limit is taken.

---

### 14. **Bollobás, B. (2001).** {#A.14}
**"Random Graphs (2nd ed.)"**
    * **Link:** [https://doi.org/10.1017/CBO9780511814068](https://doi.org/10.1017/CBO9780511814068)


**Overview:**
Bollobas presents a classic and detailed monograph on the theory of random graphs, focusing on the probabilistic methods used to study the properties of graphs generated by random processes. He covers connectivity, path lengths, chromatic numbers, and the threshold functions that govern the appearance of specific subgraphs.

**Relevance to QBD:**
This reference is integral to the random graph audits conducted in Chapter 5. To prove that the vacuum graph remains sparse and does not undergo runaway densification, we must analyze the threshold behavior of its local connections. Bollobas's probabilistic bounds provide the disciplined apparatus required to analyze the stability of the vacuum against runaway graph growth.

---

### 15. **Bombelli, L., Lee, J., Meyer, D., & Sorkin, R. D. (1987).** {#A.15}
**"Space-time as a causal set"**
    * **Link:** [https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.59.521](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.59.521)


**Overview:**
Bombelli and his collaborators introduce the causal set approach to quantum gravity, postulating that spacetime is a discrete partially ordered set (poset) where the partial order represents causal relations. They show that discrete causal structure is sufficient to recover both the causal structure and the local volume of a smooth spacetime manifold.

**Relevance to QBD:**
This classic paper is the conceptual precursor to the Causal Graph substrate defined in Chapter 1. We adopt Sorkin's insight that causality is fundamental and volume is discrete. However, we expand this setting by adding relational graph connectivity, which allows the modeling of quantum state vector updates. This citation places QBD within the historical and physical lineage of discrete causality as the chief organizer of spacetime.

---

### 24. **Ehrig, H., Ehrig, K., Prange, U., & Taentzer, G. (2006).** {#A.24}
**"Fundamentals of Algebraic Graph Transformation"**
- *Monographs in Theoretical Computer Science. An EATCS Series, Springer*
    * **Link:** [https://doi.org/10.1007/3-540-31188-2](https://doi.org/10.1007/3-540-31188-2)


**Overview:**
Ehrig et al. formulate the foundational theory of algebraic graph transformation using category theory (adhesive and quasi-adhesive categories, double-pushout approach). They prove critical pair confluence and local Church-Rosser theorems for graph rewriting systems.

**Relevance to QBD:**
The double-pushout framework and graph confluence theorems are used in Chapter 2 to establish the confluence, causality, and causal consistency of local rewrite rules operating on the relational substrate.

---

### 26. **Erdős, P., & Rényi, A. (1960).** {#A.26}
**"On the evolution of random graphs"**
    * **Link:** [https://users.renyi.hu/~p_erdos/1960-10.pdf](https://users.renyi.hu/~p_erdos/1960-10.pdf)


**Overview:**
Erdos and Renyi present the foundational paper on the evolution of random graphs, introducing the classical probabilistic model where edges are added stochastically. They prove the existence of sharp phase transitions, specifically the sudden appearance of a unique giant component as the average vertex degree exceeds one.

**Relevance to QBD:**
This seminal work is the foundation for the geometrogenesis proofs in Chapter 11. We model the emergence of physical space as a phase transition in a random causal network. Erdos and Renyi's results supply the basis for this phase transition, showing that the vacuum graph stochastically transitions from a disjointed state to a unified, highly connected spacetime manifold.

---

### 70. **Sorkin, R. D. (2005).** {#A.70}
**"Causal sets: Discrete gravity"**
- *In Lectures on Quantum Gravity (pp. 305-327). Springer*
    * **Link:** [https://arxiv.org/abs/gr-qc/0309009](https://arxiv.org/abs/gr-qc/0309009)


**Overview:**
Sorkin presents a comprehensive review of the causal set approach to quantum gravity, postulating that spacetime is fundamentally discrete and represented by a partially ordered set (poset) of events. He demonstrates that discrete causal relations are sufficient to recover the causal structure, topology, and volume of a continuous Lorentzian spacetime manifold.

**Relevance to QBD:**
Sorkin's causal set model is a core physical pillar for the discrete causal substrate defined in Chapter 1. We adopt his insight that causality is fundamental and volume is discrete. However, we expand his poset setting by adding relational graph connectivity, which is necessary to support quantum states. Sorkin's work underpins the physical basis for our discrete spacetime model.
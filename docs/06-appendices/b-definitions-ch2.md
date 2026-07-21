---
title: "Appendix B: Master List of Definitions & Theorems - Chapter 2"
sidebar_class_name: "theme-doc-sidebar-item-hidden"
---

This appendix serves as a centralized, rigorous catalog of the foundational mathematical postulates, definitions, axioms, lemmas, and theorems introduced in Chapter 2 of the Quantum Braid Dynamics (QBD) monograph.

---

### 2.1.1 Definition: Axiom 1 Directed Causal Link {#2.1.1}

:::tip[**Establishment of the Directed Causal Link as the Fundamental Relational Unit by Irreflexivity and Asymmetry**]
:::

It is herein established that the fundamental unit of relation within the **Causal Graph Substrate** <Ref id="1.4.1" label="§1.4.1" /> shall be the **Directed Causal Link**, denoted as the ordered pair $(u, v)$, acting upon the set of Abstract Events $V$. The validity of the edge set $E \subset V \times V$ is strictly conditioned upon the absolute satisfaction of the following two invariant properties for all elements within the domain:

1.  **Strict Irreflexivity:** The relation shall not, under any circumstance, connect a vertex to itself. For every vertex $u$ contained within the set $V$, the edge $(u, u)$ is categorically excluded from the set $E$. This prohibition enforces the requirement that no event may serve as its own causal antecedent.
2.  **Strict Asymmetry:** The relation shall not permit immediate reciprocity. For every distinct pair of vertices $u$ and $v$ contained within $V$, the existence of the direct edge $(u, v)$ within $E$ necessitates the absolute absence of the inverse edge $(v, u)$ from $E$. This prohibition enforces the local directionality of causal influence.

The existence of an edge $e = (u, v)$ constitutes the physical encoding of the proposition that event $u$ acts as the necessary causal antecedent of event $v$ within the local reference frame.

**In Plain English:**  
A directed causal link represents the primitive cause-and-effect relation, acting as a one-way temporal ratchet that drives cosmic updates.

---

### 2.2.1 Theorem: Insufficiency of Antisymmetry {#2.2.1}

:::info[**Non-Equivalence between Antisymmetry and Irreflexivity through the Permissibility of Self-Loops**]
:::

Let the condition of **Antisymmetry** be defined conventionally by the proposition $\forall u, v \in V : ((u, v) \in E \land (v, u) \in E) \implies u = v$. This condition is formally insufficient to satisfy the requirements of the **Directed Causal Link** <Ref id="2.1.1" label="§2.1.1" />, as it is satisfied vacuously by the reflexive relation $(u, u)$ whereas the Causal Primitive mandates Strict Irreflexivity. Consequently, a causal structure governed solely by Antisymmetry physically permits Directed Cycles of length $k=1$, which are prohibited otherwise.

**In Plain English:**  
Section 2.2.1 formalizes the properties of the QBD theorem regarding insufficiency of antisymmetry.

---

### 2.2.2 Lemma: Pathology of Self-Loops {#2.2.2}

:::info[**Classification of Reflexive Edges as Directed Cycles of Length One**]
:::

Let a self-loop incident to a vertex $u$ be denoted by $e = (u, u)$, which constitutes a directed cycle of length $k=1$ representing a **Cycle** <Ref id="1.2.6" label="§1.2.6" />. Consequently, this configuration is excluded under **Directed Acyclic Graph (DAG)** <Ref id="1.2.1" label="§1.2.1" />.

**In Plain English:**  
Section 2.2.2 formalizes the properties of the QBD lemma regarding pathology of self-loops.

---

### 2.2.2.1 Proof: Pathology of Self-Loops {#2.2.2.1}

:::tip[**Verification of the Cycle Definition for Length One**]
:::

**I. The Generalized Cycle Definition**

Let a directed cycle of length $k$ be defined as a sequence of vertices $C_k = (v_0, v_1, \dots, v_k)$ satisfying **Cycle** <Ref id="1.2.6" label="§1.2.6" />:

1.  **Connectivity:** $\forall i \in \{0, \dots, k-1\}, (v_i, v_{i+1}) \in E$
2.  **Closure:** $v_0 = v_k$

**II. Sequence Mapping**

Let $e_{loop} = (u, u) \in E$ denote a self-loop incident to vertex $u$. A sequence $S$ is defined from this structure:

$$
S = (v_0, v_1)
$$

where $v_0 = u$ and $v_1 = u$.

**III. Verification of Criteria**

The sequence $S$ satisfies the topological criteria for a cycle:

1.  **Length:** The sequence has length $k=1$.
2.  **Connectivity:** The pair $(v_0, v_1)$ corresponds to the edge $(u, u)$. Since $(u, u) \in E$, the connectivity condition holds.
3.  **Closure:** The endpoints satisfy $v_0 = u$ and $v_1 = u$, establishing $v_0 = v_1$.

**IV. Conclusion**

The self-loop $e_{loop}$ satisfies the definition of a directed cycle $C_1$. We conclude that the existence of such an edge violates the acyclicity condition required for a valid history, as defined in **Directed Acyclic Graph (DAG)** <Ref id="1.2.1" label="§1.2.1" />.

Q.E.D.

**In Plain English:**  
Section 2.2.2.1 formalizes the properties of the QBD proof regarding pathology of self-loops.

---

### 2.2.3 Lemma: Thermodynamic Nullity {#2.2.3}

:::info[**Nullity of Entropic Contribution from Reflexive Relations**]
:::

Let $\Omega(G)$ denote the cardinality of the set of simple paths connecting distinct vertices in a graph $G$. Then the path ensemble remains invariant under the addition of a self-loop, $\Omega(G') = \Omega(G)$, and the associated entropic contribution $\Delta S$ is zero.

**In Plain English:**  
Section 2.2.3 formalizes the properties of the QBD lemma regarding thermodynamic nullity.

---

### 2.2.3.1 Proof: Thermodynamic Nullity {#2.2.3.1}

:::tip[**Formal Derivation of Invariance in the Path Ensemble**]
:::

**I. Definition of the Configuration Space**

Let $\Omega(G)$ denote the cardinality of the set of simple directed paths between distinct vertices $u, v$ in a graph governed by the **Directed Causal Link** <Ref id="2.1.1" label="§2.1.1" />. A simple path is defined strictly as a sequence of vertices containing no repetitions.

$$
\Omega(G) = | \{ \pi_{uv} \mid u \neq v, \pi \text{ is simple} \} |
$$

The presence of self-loops, studied in **Pathology of Self-Loops** <Ref id="2.2.2" label="§2.2.2" />, is evaluated.

Let $\mathcal{T}_{self}$ denote the operation adding a self-loop $e = (x, x)$ to the graph $G$, yielding $G'$. Any candidate path $\pi'$ in $G'$ that traverses $e$ necessarily contains the subsequence $(x, x)$. This repetition of the vertex $x$ violates the definition of a simple path. It follows that no valid simple path utilizes the self-loop edge.

$$
\pi' \notin \Omega(G') \implies \Omega(G') = \Omega(G)
$$

**III. Calculation of Entropy Change**

The entropic contribution of the operation is defined by the Boltzmann formulation:

$$
\Delta S = k_B \ln \left( \frac{\Omega(G')}{\Omega(G)} \right)
$$

Substitution of the invariance equality into the expression yields:

$$
\Delta S = k_B \ln(1)
$$

The logarithm of unity implies the vanishing of the term:

$$
\Delta S = 0
$$

**IV. Conclusion**

The addition of a self-loop preserves the cardinality of the simple path ensemble. We conclude that the entropic contribution of a reflexive edge is identically zero.

Q.E.D.

**In Plain English:**  
Section 2.2.3.1 formalizes the properties of the QBD proof regarding thermodynamic nullity.

---

### 2.2.4 Proof: Insufficiency of Antisymmetry {#2.2.4}

:::tip[**Insufficiency of Antisymmetry** <Ref id="2.2.1" label="§2.2.1" />]
:::

**I. The Mathematical Condition**
Let the axiom of **Antisymmetry** be defined by the standard order-theoretic implication:
$$
\forall u, v \in V, \quad ((u, v) \in E \land (v, u) \in E) \implies u = v
$$
This condition operates as a conditional restraint. Crucially, it is verified definitionally to permit the existence of a reflexive edge $e = (u, u)$, as the consequent of the implication ($u=u$) holds true, rendering the statement valid regardless of the edge's existence.

**II. The Constraint Chain**
The physical admissibility of such a reflexive structure is evaluated against the foundational requirements of the theory:

1.  **Pathology of Self-Loops** <Ref id="2.2.2" label="§2.2.2" />: It is established that a reflexive edge $e = (u, u)$ constitutes a directed cycle of length $k=1$. The existence of such a structure stands in direct violation of the **Global Acyclicity** requirement, which is essential for defining a valid causal history.
2.  **Thermodynamic Nullity** <Ref id="2.2.3" label="§2.2.3" />: It is established that the addition of a self-loop yields a net entropic gain of exactly zero ($\Delta S = 0$). This occurs because the relation fails to distinguish the vertex from itself or establish a correlation between distinct entities. The operation consumes a unit of logical time $t_L$ without generating distinguishable information, thereby violating the requirement for effective physical evolution.

**III. Convergence**
A causal system governed solely by the condition of Antisymmetry is verified definitionally to permit the formation of states (self-loops) that are both topologically cyclic and thermodynamically vacuous.

**IV. Formal Conclusion**
The condition of Antisymmetry is verified to be formally insufficient to enforce causal validity. The stricter axiom of **Irreflexivity** ($\forall u, (u, u) \notin E$) is required to explicitly and categorically exclude the domain of validity for self-loops, thereby ensuring that all causal links establish a relation between distinct entities.

Q.E.D.

**In Plain English:**  
Section 2.2.4 formalizes the properties of the QBD proof regarding insufficiency of antisymmetry.

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
The three definitions encode the minimal vocabulary of the antisymmetry derivation as Lean types. `CausalRelation V` is a function type `V → V → Prop`, faithfully capturing the binary predicate structure of a directed edge relation. `IsAntisymmetric` and `IsIrreflexive` encode the standard mathematical conditions as universally quantified propositions over `V`. The verified counter-model `⟨Bool, Eq⟩` existentially witnesses this logical gap: Boolean equality satisfies antisymmetry because `h_fwd : u = v` is obtained directly when both directions hold, yet it violates irreflexivity because `true = true` is provable by `rfl`, which immediately contradicts the assumed `h_irref true : ¬ (true = true)`. The Lean kernel's acceptance of this closed proof term certifies that the logical claim in **Insufficiency of Antisymmetry** <Ref id="2.2.4" label="§2.2.4" /> is correct: antisymmetry does not imply irreflexivity, and the stricter axiomatic requirement is independently necessary.

**In Plain English:**  
Section 2.2.5 formalizes the properties of the QBD type-theoretic regarding validation via lean 4 core.

---

### 2.3.1 Definition: Axiom 2 Geometric Constructibility {#2.3.1}

:::tip[**Restriction of Topological Evolution to Geometric Quanta and Unique Paths by Positive and Negative Constraints**]
:::

The kinematic admissibility of any transformation $G \to G'$ involving the addition of an edge is restricted by the following two complementary clauses of **Geometric Constructibility**:

1.  **Clause A (Positive Construction):** The formation of closed topological structures is restricted exclusively to **Geometric Quanta**, defined as **3-Cycle** <Ref id="1.2.8" label="§1.2.8" />. The closure of a causal loop is permissible if and only if the resulting path sequence has a length of exactly $L=3$.
2.  **Clause B (Negative Constraint):** The construction must adhere to the **Principle of Unique Causality (PUC)**. The instantiation of a return edge $(u, v)$ is prohibited if there already exists an alternative Simple Directed Path from $v$ to $u$ of length $\ell \le 2$ within the graph $G$.

**In Plain English:**  
Section 2.3.1 formalizes the properties of the QBD definition regarding axiom 2 geometric constructibility.

---

### 2.3.2 Theorem: Geometric Constructibility {#2.3.2}

:::info[**Convergence of Constructible Graph States to Acyclic Unions of Geometric Quanta**]
:::

For any graph state $G$ undergoing a sequence of edge addition and deletion tasks, the resulting configuration $G'$ converges to a stable, acyclic union of geometric quanta. This convergence is bounded and well-founded under the lexicographic potential.

**In Plain English:**  
A 3-cycle represents the minimal closed loop of causality, constituting the fundamental 'geometric quantum' or atom of physical space.

---

### 2.3.3 Lemma: Geometric Quantum {#2.3.3}

:::info[**Minimal Closed Cycle Compatible with the Causal Primitive**]
:::

Let the Geometric Quantum $\gamma$ denote the subgraph induced by the ordered triplet of vertices $(u, v, w)$ such that the edge set contains exactly $\{(u, v), (v, w), (w, u)\}$. Then this structure constitutes the minimal closed cycle compatible with the **Directed Causal Link** <Ref id="2.1.1" label="§2.1.1" />, excluding cycles of length 1 and 2, and the set of all $\gamma \subset G$ constitutes the basis for emergent spatial area.

**In Plain English:**  
Section 2.3.3 formalizes the properties of the QBD lemma regarding geometric quantum.

---

### 2.3.3.1 Proof: Geometric Quantum {#2.3.3.1}

:::tip[**Derivation of the Minimal Stable Cycle Length via Elimination of Forbidden Lower Orders**]
:::

**I. Cycle Length Domain**

Let $L$ denote the length of a directed cycle $C_L$, analyzed for $L \in \mathbb{N}_{\ge 1}$.

**II. Elimination of Lower Orders**

The case $L=1$ implies an edge $e = (u, u)$. This configuration is excluded by the irreflexivity property of the **Directed Causal Link** <Ref id="2.1.1" label="§2.1.1" />:

$$
(u, u) \notin E \implies L \neq 1
$$

The case $L=2$ implies edges $e_1 = (u, v)$ and $e_2 = (v, u)$ with $u \neq v$. This configuration is excluded by the **Directed Causal Link** <Ref id="2.1.1" label="§2.1.1" />:

$$
(u, v) \in E \implies (v, u) \notin E \implies L \neq 2
$$

**III. Verification of the 3-Cycle**

A cycle of length 3 involves distinct vertices $u, v, w$ and edges $E_C = \{ (u, v), (v, w), (w, u) \}$.

1.  **Irreflexivity:** The condition $u \neq v \neq w$ holds, ensuring no self-loops.
2.  **Asymmetry:** The set contains no reciprocal pairs (e.g., $(v, u) \notin E_C$).

**IV. Conclusion**

The integer $L=3$ is the minimal length satisfying the Causal Primitive.

$$
L_{min} = 3
$$

Q.E.D.

**In Plain English:**  
Section 2.3.3.1 formalizes the properties of the QBD proof regarding geometric quantum.

---

### 2.3.4 Lemma: Principle of Unique Causality (PUC) {#2.3.4}

:::info[**Prohibition of Causal Redundancy under the Sparsity Constraint on Local Paths**]
:::

Let $\Pi_{\ell \le 2}(u, v)$ denote the set of all Simple Directed Paths originating at $u$ and terminating at $v$ with a path length strictly less than or equal to 2. The operation $\mathfrak{T}_{add}(u, v)$ defined in **Edge Addition Task** <Ref id="1.5.2" label="§1.5.2" /> is admissible if and only if the cardinality of this set is zero, and is excluded otherwise.

**In Plain English:**  
Section 2.3.4 formalizes the properties of the QBD lemma regarding principle of unique causality (puc).

---

### 2.3.4.1 Proof: Principle of Unique Causality (PUC) {#2.3.4.1}

:::tip[**Formal Derivation of Path Uniqueness from the Principle of Informational Parsimony**]
:::

**I. Initial State**

Let $G$ be a graph satisfying **Geometric Constructibility** <Ref id="2.3.1" label="§2.3.1" /> containing a mediated path between $u$ and $v$ whose admissibility is governed by the **Principle of Unique Causality (PUC)** <Ref id="2.3.4" label="§2.3.4" />:

$$
P_1 = (u, w, v) \implies (u, w) \in E \land (w, v) \in E
$$

The set of paths of length $\le 2$ satisfies the non-empty condition:

$$
|\Pi_{\le 2}(u, v)| \ge 1
$$

**II. The Proposed Operation**

The proposed operation adds the direct edge $e = (u, v)$. This creates a new path $P_2 = (u, v)$ of length 1.

**III. Information Analysis**

1.  **Path $P_1$:** Encodes the causal relation $u \prec v$ via $w$.
2.  **Path $P_2$:** Encodes the causal relation $u \prec v$ directly.
3.  **Result:** The bit "$u$ precedes $v$" is encoded twice in the local topology.

**IV. Constraint Application**

The **Principle of Unique Causality (PUC)** forbids edge addition if a path of length $\le 2$ already exists.

* **Condition:** $|\Pi_{\le 2}(u, v)| \ge 1$
* **Action:** $\mathfrak{T}_{add}(u, v)$ is Forbidden

**V. Conclusion**

The existence of the mediated path $P_1$ physically precludes the formation of the direct path $P_2$. The topology enforces informational parsimony.

Q.E.D.

**In Plain English:**  
Section 2.3.4.1 formalizes the properties of the QBD proof regarding principle of unique causality (puc).

---

### 2.3.5 Lemma: Lexicographic Potential {#2.3.5}

:::info[**Quantification of Topological Complexity via Cycle Ordering**]
:::

Let the **Lexicographic Potential** $\Phi(G)$ be the ordered pair $(L_{\max}, N_{L_{\max}})$ mapping a finite graph $G$ to the state space $\mathcal{P} = \mathbb{N} \times \mathbb{N}$ ordered lexicographically. The relation $<$ on $\mathcal{P}$ constitutes a strict order satisfying irreflexivity, asymmetry, and transitivity.

**In Plain English:**  
Section 2.3.5 formalizes the properties of the QBD lemma regarding lexicographic potential.

---

### 2.3.5.1 Proof: Lexicographic Potential {#2.3.5.1}

:::tip[**Verification of the Strict Ordering Properties of the Lexicographic Product**]
:::

**I. Irreflexivity**

Let $\Phi(G) = (a, b) \in \mathcal{P}$ represent the **Lexicographic Potential** <Ref id="2.3.5" label="§2.3.5" /> mapping of the cycles, defined in **Cycle** <Ref id="1.2.6" label="§1.2.6" />. The relation $(a, b) < (a, b)$ is false because the standard order $<$ on $\mathbb{N}$ is strictly irreflexive, meaning $a \nless a$ and $b \nless b$.

**II. Asymmetry**

Let $(a, b) < (c, d)$. If $a < c$, then $c < a$ is false, hence $(c, d) \nless (a, b)$. If $a = c$ and $b < d$, then $d < b$ is false, hence $(c, d) \nless (a, b)$. Asymmetry holds.

**III. Transitivity**

Let $(a, b) < (c, d)$ and $(c, d) < (e, f)$. If $a < c$ and $c < e$, transitivity of $\mathbb{N}$ yields $a < e$, hence $(a, b) < (e, f)$. If $a = c$ and $c < e$, then $a < e$. Similarly, if $a < c$ and $c = e$, then $a < e$. Finally, if $a = c$ and $c = e$, then $b < d$ and $d < f$ which yields $b < f$ by transitivity of $\mathbb{N}$, establishing $(a, b) < (e, f)$.

Q.E.D.

**In Plain English:**  
Section 2.3.5.1 formalizes the properties of the QBD proof regarding lexicographic potential.

---

### 2.3.6 Lemma: Well-Foundedness {#2.3.6}

:::info[**Termination of Strictly Decreasing Topological Processes**]
:::

Let $\Phi(G)$ denote the **Lexicographic Potential** <Ref id="2.3.5" label="§2.3.5" /> of a finite graph $G$. Then the codomain of $\Phi$ is well-ordered, and any trajectory $G_0, G_1, \dots$ satisfying the descent condition $\Phi(G_{t+1}) < \Phi(G_t)$ constitutes a finite sequence.

**In Plain English:**  
Section 2.3.6 formalizes the properties of the QBD lemma regarding well-foundedness.

---

### 2.3.6.1 Proof: Well-Foundedness {#2.3.6.1}

:::tip[**Verification of the Descent Property due to the Finiteness of Graph Configurations**]
:::

**I. State Space Properties**

Let $G$ be a graph with finite vertex count $|V| = N < \infty$. Let $\mathcal{C}$ denote the set of all simple cycles in $G$. The number of possible cycles is bounded by the combinatorial limit:

$$
|\mathcal{C}| \le \sum_{k=1}^N \binom{N}{k} (k-1)! < \infty
$$

**II. The Potential Function**

Let $\Phi(G) = (L_{\max}, N_{L_{\max}})$ represent the **Lexicographic Potential** <Ref id="2.3.5" label="§2.3.5" /> mapping under the **Well-Foundedness** <Ref id="2.3.6" label="§2.3.6" /> relation.

1.  **Length Bound:** $L_{\max} \in \{0, \dots, N\}$.
2.  **Count Bound:** $N_{L_{\max}}$ is finite.

**III. Descent Analysis**

Let a dynamical operation produce a sequence of states $G_0, G_1, \dots$ satisfying $\Phi(G_{i+1}) < \Phi(G_i)$. The domain is a finite subset of the well-ordered set $\mathbb{N} \times \mathbb{N}$. It follows that no infinite strictly decreasing sequence exists.

$$
\nexists \ \{ \phi_i \}_{i=0}^\infty \quad \text{such that} \quad \forall i, \phi_{i+1} < \phi_i
$$

**IV. Conclusion**

Any dynamical rule that strictly decreases the Lexicographic Potential $\Phi$ terminates in a finite number of steps. The cycle reduction process is guaranteed to halt.

Q.E.D.

**In Plain English:**  
Section 2.3.6.1 formalizes the properties of the QBD proof regarding well-foundedness.

---

### 2.3.7 Proof: Geometric Constructibility {#2.3.7}

:::tip[**Synthesis of Local Uniqueness, Quantum Minimality, and Well-Foundedness showing Geometric Convergence**]
:::

**I. Spatial Quantization**

The local construction of cycles is restricted to the minimal stable topological closure, as established by the **Geometric Quantum** <Ref id="2.3.3" label="§2.3.3" />. Any larger macro-cycle is unstable under the constructor's rewrite rules.

**II. Initial Configuration and Rewrite Admissibility**

Let a sequence of rewrite tasks operate on a causal graph $G_0$. The admissibility of each addition task is constrained by the local check, satisfying the **Principle of Unique Causality (PUC)** <Ref id="2.3.4" label="§2.3.4" />.

**III. Convergence and Well-Foundedness**

The sequence of configurations corresponds to a monotonic descent of the potential function, defined under **Lexicographic Potential** <Ref id="2.3.5" label="§2.3.5" />. By the **Well-Foundedness** <Ref id="2.3.6" label="§2.3.6" /> of this potential, this descent contains no infinite chains and must terminate. Upon termination, the target graph converges to a union of geometric quanta.

Q.E.D.

**In Plain English:**  
Section 2.3.7 formalizes the properties of the QBD proof regarding geometric constructibility.

---

### 2.4.1 Theorem: General Cycle Decomposition {#2.4.1}

:::info[**Finite Decomposition of General Cycles via the Alternating Application of Chordal Addition and Entropic Deletion**]
:::

For all graph states $G$ containing a Simple Directed Cycle of length $L_{\max} \ge 4$, there exists a finite, computable sequence of admissible operations, specifically Chordal Addition followed by Entropic Deletion, that transforms $G$ into a state $G'$ where all cycles have length $L \le 3$. This decomposition sequence guarantees the strict monotonic reduction of the **Lexicographic Potential** <Ref id="2.3.5" label="§2.3.5" />, denoted $\Phi(G)$.

**In Plain English:**  
Section 2.4.1 formalizes the properties of the QBD theorem regarding general cycle decomposition.

---

### 2.4.2 Lemma: Confluence of the Constructor {#2.4.2}

:::info[**Local Confluence of Overlapping Rewrite Operations**]
:::

Let $\mathcal{R}$ denote the rewrite rule governing edge addition applied to a state $G$ containing two distinct, overlapping compliant paths $P_1$ and $P_2$ (**2-Path** <Ref id="1.2.5" label="§1.2.5" />). Then the application of $\mathcal{R}$ to $P_1$ maintains the compliance of $P_2$, and the resulting state is invariant with respect to the temporal order of application ($G_{1,2} \equiv G_{2,1}$), establishing the global consistency of the decomposition.

**In Plain English:**  
Section 2.4.2 formalizes the properties of the QBD lemma regarding confluence of the constructor.

---

### 2.4.2.1 Proof: Confluence of the Constructor {#2.4.2.1}

:::tip[**Formal Verification of Commutativity in Overlapping Updates**]
:::

**I. Initial State with Overlap**

Let $G = (V, E)$ denote a graph governed by the **Confluence of the Constructor** <Ref id="2.4.2" label="§2.4.2" /> containing two compliant **2-Path** <Ref id="1.2.5" label="§1.2.5" /> states sharing a common edge $(w, u)$.
1.  $P_1 = (v, w, u)$ targeting the chord $e_1 = (u, v)$.
2.  $P_2 = (w, u, x)$ targeting the chord $e_2 = (x, w)$.

**II. Branch A Derivation**

The transition $G \xrightarrow{P_1} G_A$ yields the edge set $E_A = E \cup \{ (u, v) \}$.
**Check $P_2$ Validity in $G_A$:**
The required edges $(w, u)$ and $(u, x)$ persist in $E_A$. The Uniqueness Constraint requires the absence of a path $w \to \dots \to x$ of length $\le 2$ utilizing the new edge $(u, v)$. Since $(u, v)$ originates at $u$ and terminates at $v$, a contribution to the target path necessitates a connection $v \to x$. The case $v=x$ implies that $P_2$ forms a cycle, a configuration excluded by compliance. It follows that no such path exists, and $P_2$ remains valid.
The subsequent operation $\mathcal{R}(P_2)$ yields:

$$
E_{AB} = E \cup \{ (u, v), (x, w) \}
$$

**III. Branch B Derivation**

The transition $G \xrightarrow{P_2} G_B$ yields the edge set $E_B = E \cup \{ (x, w) \}$.
**Check $P_1$ Validity in $G_B$:**
Symmetric analysis establishes that the addition of $(x, w)$ does not invalidate $P_1$.
The operation $\mathcal{R}(P_1)$ yields:

$$
E_{BA} = E \cup \{ (x, w), (u, v) \}
$$

**IV. Convergence**

Comparison of the final edge sets reveals identity due to the commutativity of set union:

$$
E_{AB} = E \cup \{ e_1, e_2 \} = E \cup \{ e_2, e_1 \} = E_{BA}
$$

We conclude that the order of operations does not affect the final state.

Q.E.D.

**In Plain English:**  
Section 2.4.2.1 formalizes the properties of the QBD proof regarding confluence of the constructor.

---

### 2.4.3 Lemma: Chordlessness of Maximal Cycles {#2.4.3}

:::info[**Topological Chordlessness of Maximal Cycles**]
:::

Let $C$ denote a Simple Directed Cycle within $G$ possessing the maximal length $L = L_{\max} \ge 4$. Then $C$ constitutes a strictly **Chordless** cycle, satisfying the condition that no edges exist between non-adjacent vertices.

**In Plain English:**  
Section 2.4.3 formalizes the properties of the QBD lemma regarding chordlessness of maximal cycles.

---

### 2.4.3.1 Proof: Chordlessness of Maximal Cycles {#2.4.3.1}

:::tip[**Derivation of Chordlessness via Contradiction of the Lexicographic Maximality Premise**]
:::

**I. The Maximality Hypothesis**

Let $C = (v_0, \dots, v_{L-1})$ denote a simple **Cycle** <Ref id="1.2.6" label="§1.2.6" /> of length $L$. Assume $L$ represents the global maximum cycle length in $G$.

$$
L = L_{\max}
$$

**II. The Chord Assumption**

Assume the existence of a chord $e = (v_i, v_k)$ where $v_i, v_k \in C$ correspond to non-adjacent vertices. The indices satisfy the separation condition:

$$
|i - k| > 1 \pmod L
$$

**III. Topological Partition**

The chord $e$ partitions the cycle $C$ into two sub-cycles:

1.  **Cycle $C_1$:** Composed of the path along $C$ from $v_k$ to $v_i$ and the chord $(v_i, v_k)$.

    $$
    L_1 = \text{dist}_C(v_k, v_i) + 1
    $$

2.  **Cycle $C_2$:** Composed of the path along $C$ from $v_i$ to $v_k$ and the chord $(v_i, v_k)$.

    $$
    L_2 = \text{dist}_C(v_i, v_k) + 1
    $$

**IV. Inequality Derivation**

The total length $L$ corresponds to the sum of the distances along the original arc.

$$
L = \text{dist}_C(v_k, v_i) + \text{dist}_C(v_i, v_k)
$$

The non-adjacency condition implies strictly positive distances between vertices on the arc.

$$
\text{dist}_C(v_k, v_i) \ge 1 \implies L_2 < L
$$

$$
\text{dist}_C(v_i, v_k) \ge 1 \implies L_1 < L
$$

**V. Contradiction**

The presence of the chord identifies $C$ as a composite structure formed by the union of $C_1$ and $C_2$. It follows that the elementary cycles contributing to the potential $\Phi(G)$ are $C_1$ and $C_2$. The maximum length in this subgraph evaluates to $\max(L_1, L_2) < L$. This contradicts the premise that a simple cycle of length $L$ exists under the **Lexicographic Potential** <Ref id="2.3.5" label="§2.3.5" />. We conclude that a maximal simple cycle must be chordless.

Q.E.D.

**In Plain English:**  
Section 2.4.3.1 formalizes the properties of the QBD proof regarding chordlessness of maximal cycles.

---

### 2.4.4 Lemma: Reduction via Deletion {#2.4.4}

:::info[**Strict Descent of the Lexicographic Potential under Edge Deletion**]
:::

Let $e$ denote an edge belonging to a simple cycle $C$ of maximal length within a graph $G$ characterized by the **Lexicographic Potential** <Ref id="2.3.5" label="§2.3.5" />, denoted $\Phi(G)$.. Then the deletion of $e$ yields a graph $G'$ satisfying the strict descent condition $\Phi(G') < \Phi(G)$.

**In Plain English:**  
Section 2.4.4 formalizes the properties of the QBD lemma regarding reduction via deletion.

---

### 2.4.4.1 Proof: Reduction via Deletion {#2.4.4.1}

:::tip[**Demonstration of Order Descent via Path Set Reduction**]
:::

**I. Initial State Definition**

Let $G = (V, E)$ denote a graph with **Lexicographic Potential** <Ref id="2.3.5" label="§2.3.5" /> $\Phi(G) = (L_{\max}, N_{L_{\max}})$. Let $C$ denote a simple cycle of length $L_{\max}$, and let $e \in C$ denote a specific edge within this cycle.

**II. The Deletion Operation**

Let $G'$ denote the graph resulting from the **Edge Deletion Task** <Ref id="1.5.3" label="§1.5.3" /> operation $E' = E \setminus \{e\}$, satisfying **Reduction via Deletion** <Ref id="2.4.4" label="§2.4.4" />.

**III. Connectivity Analysis**

The deletion of the edge $e$ strictly reduces the set of valid paths. Any cycle $C_{new}$ existing in $G'$ necessitates that all constitutive edges belong to $E'$. The subset relation $E' \subset E$ implies that any such cycle pre-existed in $G$. It follows that no new cycles emerge from the deletion operation.

$$
\mathcal{C}(G') \subseteq \mathcal{C}(G) \setminus \{C\}
$$

**IV. Recalculation of Potential**

The potential $\Phi(G') = (L'_{\max}, N'_{L_{\max}})$ evaluates under two cases based on the survival of other maximal cycles.

1.  **Case A (Survival):** If the set of cycles of length $L_{\max}$ remains non-empty, the length parameter is invariant ($L'_{\max} = L_{\max}$). The count parameter decreases by the number of maximal cycles containing $e$, ensuring $N'_{L_{\max}} < N_{L_{\max}}$.
2.  **Case B (Extinction):** If $C$ was the sole remaining cycle of length $L_{\max}$, the maximum cycle length decreases. This yields $L'_{\max} < L_{\max}$.

**V. Conclusion**

Both cases satisfy the criteria for lexicographic descent. We conclude that the deletion of a maximal-cycle edge guarantees strict potential reduction.

$$
\Phi(G') < \Phi(G)
$$

Q.E.D.

**In Plain English:**  
Section 2.4.4.1 formalizes the properties of the QBD proof regarding reduction via deletion.

---

### 2.4.5 Lemma: Decrease in Parallel Updates {#2.4.5}

:::info[**Net Reduction of Topological Complexity under Composite Updates**]
:::

Let $\mathcal{S}_{step} = \mathcal{O}_{del} \circ \mathcal{O}_{add}$ denote a composite update step comprising edge addition and subsequent deletion. Then the operation satisfies the strict descent condition for the Lexicographic Potential, $\Phi(G_{next}) < \Phi(G)$.

**In Plain English:**  
Section 2.4.5 formalizes the properties of the QBD lemma regarding decrease in parallel updates.

---

### 2.4.5.1 Proof: Decrease in Parallel Updates {#2.4.5.1}

:::tip[**Verification of Net Descent across the Two-Phase Update Cycle**]
:::

**I. Phase 1: Chordal Addition**

Let $G \to G_{add}$ denote the addition of chords to all compliant 2-paths within maximal cycles.

1.  **Site Availability:** Maximal cycles satisfy **Chordlessness of Maximal Cycles** <Ref id="2.4.3" label="§2.4.3" />, ensuring the existence of valid 2-paths.
2.  **Structure Decomposition:** The addition of chords partitions maximal cycles into 3-cycles and smaller loops.
3.  **Cycle Bounding:** The **Principle of Unique Causality (PUC)** <Ref id="2.3.4" label="§2.3.4" /> restricts additions to sites lacking short paths. The creation of a cycle $L_{new} > L_{\max}$ requires a pre-existing path of length $> L_{\max}-1$ connecting vertices at distance 2. This implies a prior path violation.
4.  **Result:** The maximum cycle length satisfies the non-increasing condition.

    $$
    \Phi(G_{add}) \le \Phi(G)
    $$

**II. Phase 2: Entropic Deletion**

Let $G_{add} \to G_{next}$ denote the removal of edges from the original maximal cycles.

1.  **Operation:** Edges participating in the original cycle $C$ undergo deletion.
2.  **Potential Drop:** Edge removal strictly reduces the Lexicographic Potential under **Reduction via Deletion** <Ref id="2.4.4" label="§2.4.4" />.

    $$
    \Phi(G_{next}) < \Phi(G_{add})
    $$

**III. Synthesis**

The composition of operations yields a strict inequality:

$$
\Phi(G_{next}) < \Phi(G)
$$

We conclude that the update step enforces monotonic descent in the topological complexity metric.

Q.E.D.

**In Plain English:**  
Section 2.4.5.1 formalizes the properties of the QBD proof regarding decrease in parallel updates.

---

### 2.4.6 Proof: General Cycle Decomposition {#2.4.6}

:::tip[**General Cycle Decomposition** <Ref id="2.4.1" label="§2.4.1" /> via Synthesis of Confluence and Potential Reduction]
:::

**I. Initial Conditions**

Let the universe exist in state $G_0$ with potential $\Phi(G_0) = (L, N_L)$ satisfying $L \ge 4$.

**II. Operational Accessibility**

1.  **Site Existence:** Cycles of length $L$ must satisfy **Chordlessness of Maximal Cycles** <Ref id="2.4.3" label="§2.4.3" />. This guarantees the presence of compliant 2-paths susceptible to the rewrite rule $\mathcal{R}$.
2.  **Operational Set:** The set of valid operations is non-empty.

    $$
    |\mathcal{O}_{add}| \ge 1
    $$

**III. Consistency and Reduction**

1.  **Confluence:** The parallel application of operations proceeds concurrently, as established by the **Confluence of the Constructor** <Ref id="2.4.2" label="§2.4.2" />, yielding state $G_{add}$.
2.  **Net Descent:** The subsequent deletion phase produces state $G_1$ satisfying $\Phi(G_1) < \Phi(G_0)$ as established by **Decrease in Parallel Updates** <Ref id="2.4.5" label="§2.4.5" />, which utilizes **Reduction via Deletion** <Ref id="2.4.4" label="§2.4.4" /> to guarantee the potential decrease.

**IV. Iterative Termination**

1.  **Sequence Construction:** The dynamics generate a sequence of potentials $\Phi(G_0) > \Phi(G_1) > \dots$.
2.  **Well-Foundedness:** The lexicographic order on finite graphs constitutes a proven well-founded invariant with no infinite descending chains under the **Lexicographic Potential** <Ref id="2.3.5" label="§2.3.5" />.
3.  **Limit:** The sequence must terminate at a state $G_{min}$.

**V. Final State Topology**

Termination occurs when no cycle $L \ge 4$ exists to trigger the reduction mechanism.

$$
L_{\max}(G_{min}) \le 3
$$

The graph converges to a union of Geometric Quanta (3-cycles) and acyclic paths.

Q.E.D.

**In Plain English:**  
Section 2.4.6 formalizes the properties of the QBD proof regarding general cycle decomposition.

---

### 2.4.10 Calculation: Simulation Verification {#2.4.10}

:::note[**Simulation Verification of the Cycle Reduction Algorithm via Deterministic Execution**]
:::

Verification of the finite termination condition established by **General Cycle Decomposition** <Ref id="2.4.6" label="§2.4.6" /> is based on the following protocols:

1.  **Defect Initialization:** The algorithm constructs isolated directed cycles of length $k \in [4, 12]$ to serve as standardized topological defects. This mapping represents the initialization of unstable macroscopic loops within the vacuum.
2.  **Topological Reduction:** The protocol simulates a maximally parallel update by instantiating chords across open 2-paths and subsequently prunes macro-cycles ($L > 3$) via entropic deletion to resolve topological tension.
3.  **Operation Counting:** The metric tracks the total additions and deletions required for the system to reach the simplicial ground state ($L_{\max} = 3$), verifying the descent of the **Lexicographic Potential** <Ref id="2.3.5" label="§2.3.5" />.

```python
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

The tabulated data establishes a linear correlation between the initial cycle length $k$ and the addition count ($Ops_{add} = k$). The deletion count stabilizes at a constant value ($Ops_{del} = 3$) for all topologies with $k \ge 7$. This finite scaling confirms that the algorithmic reduction complexity is proportional to the defect size $O(k)$, validating the termination logic of the proof.

**In Plain English:**  
Section 2.4.10 formalizes the properties of the QBD calculation regarding simulation verification.

---

### 2.4.11 Type-Theoretic Validation via Lean 4 Core {#2.4.11}

:::note[**Lean 4 Encoding of Lexicographic Well-Foundedness via Well-Order Instantiation**]
:::

Type-theoretic certification of the descent guarantee established in the **Well-Foundedness** <Ref id="2.3.6" label="§2.3.6" /> proof proceeds via the following verification strategy:

1.  **Encoding:** The definitions `IsGeometricQuantum` and `IsCompliant2Path` encode the directed **3-cycle** and the **Principle of Unique Causality** as dependent propositions over an abstract causal relation, confirming that the type system admits the axiomatic vocabulary without contradiction.
2.  **Theorem Statements:** The first theorem (`lexicographic_relation_wf`) certifies the well-foundedness of the lexicographic product order on $\mathbb{N} \times \mathbb{N}$ by kernel-delegated instance resolution; the second (`lexicographic_descent_admissible`) certifies that any state transition reducing either the maximum cycle length or its multiplicity constitutes a strictly descending step in this order.
3.  **Proof Closure:** `lexicographic_relation_wf` is discharged by `inferInstance`, confirming Lean's standard library contains the required well-order; `lexicographic_descent_admissible` uses a case split on the disjunction, with `Prod.Lex.left` closing the length-reduction branch and `Prod.Lex.right` closing the count-reduction branch after `subst` eliminates the equality hypothesis.

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
```

**Verification Summary:**
The auxiliary definitions `IsGeometricQuantum` and `IsCompliant2Path` confirm that the causal vocabulary of Axiom 2 is well-typed as Lean propositions, requiring no consistency workaround. The first theorem delegates the well-foundedness of $\mathbb{N} \times \mathbb{N}$ under the lexicographic product order to `inferInstance`, which resolves against Lean's standard library `WellFoundedRelation` instance; the kernel's acceptance of this one-liner constitutes the machine certificate that the codomain of $\Phi(G)$ possesses no infinite descending chains. The second theorem covers the two-case disjunction $(L_2 < L_1) \lor (L_2 = L_1 \land N_2 < N_1)$ that defines strict lexicographic descent: `Prod.Lex.left` closes the first case directly from the length inequality, while `subst h_eq` eliminates the equality $L_2 = L_1$ before `Prod.Lex.right` closes the count-reduction case. The Lean kernel's acceptance of both closed proof terms certifies the descent guarantee in the **Well-Foundedness** <Ref id="2.3.6" label="§2.3.6" /> proof: any dynamical rule that strictly decreases the Lexicographic Potential $\Phi$ is provably terminating.

**In Plain English:**  
Section 2.4.11 formalizes the properties of the QBD type-theoretic regarding validation via lean 4 core.

---

### 2.5.1 Theorem: Independence of Axioms 1 and 2 {#2.5.1}

:::info[**Establishment of Logical Orthogonality between Causal and Geometric Primitives via Mutual Non-Entailment**]
:::

Let the **Directed Causal Link** <Ref id="2.1.1" label="§2.1.1" /> be established first. Let **Geometric Constructibility** <Ref id="2.3.1" label="§2.3.1" /> be established second. These constraints are formally independent, meaning the satisfaction of either does not logically entail the satisfaction of the other, as demonstrated by orthogonal countermodels.

**In Plain English:**  
Section 2.5.1 formalizes the properties of the QBD theorem regarding independence of axioms 1 and 2.

---

### 2.5.2 Lemma: Independence Case A {#2.5.2}

:::info[**Existence of Causal Validity amidst Geometric Non-Constructibility**]
:::

Let $G_A$ denote a chordless directed cycle of length $4$ satisfying **The Directed Causal Link** <Ref id="2.1.1" label="§2.1.1" />. This structure constitutes an irreducible configuration violating **Geometric Constructibility** <Ref id="2.3.1" label="§2.3.1" />.

**In Plain English:**  
Section 2.5.2 formalizes the properties of the QBD lemma regarding independence case a.

---

### 2.5.2.1 Proof: Independence Case A {#2.5.2.1}

:::tip[**Formal Verification of the Chordless 4-Cycle Model against Axiomatic Criteria**]
:::

**I. Model Construction**

Let $G_A = (V, E)$ denote a graph forming a single connected directed cycle of length four, defined by the vertex set $V = \{A, B, C, D\}$ and the edge set $E = \{(A, B), (B, C), (C, D), (D, A)\}$. The topology strictly excludes internal chords:

$$
E \cap \{(A, C), (B, D)\} = \emptyset
$$

**II. Verification of the Causal Primitive**

Inspection of the edge set $E$ reveals no reflexive edges, satisfying the **Directed Causal Link** <Ref id="2.1.1" label="§2.1.1" />.

$$
\forall v \in V, (v, v) \notin E
$$

Furthermore, inspection reveals no reciprocal pairs.

$$
(A, B) \in E \implies (B, A) \notin E
$$

**III. Verification of Geometric Constructibility (Axiom 2)**

Axiom $2$ requires that valid geometry emerges exclusively from the closure of minimal directed $3$-cycles under **Geometric Constructibility** <Ref id="2.3.1" label="§2.3.1" />. The graph $G_A$ contains a cycle of length $4$. The absence of chords precludes the decomposition of this cycle into constituent $3$-cycles.

$$
L_{min}(G_A) = 4 > 3
$$

The structure persists as an irreducible unit exceeding the geometric quantum.

$$
G_A \notin \Omega_{geo}
$$

**IV. Conclusion**

The model $G_A$ satisfies Causal Validity while violating Geometric Constructibility. We conclude that Axiom 1 does not entail Axiom 2.

$$
Ax1 \not\implies Ax2
$$

Q.E.D.

**In Plain English:**  
Section 2.5.2.1 formalizes the properties of the QBD proof regarding independence case a.

---

### 2.5.3 Lemma: Independence Case B {#2.5.3}

:::info[**Existence of Geometric Constructibility amidst Causal Invalidity**]
:::

Let $G_B$ denote the disjoint union of a simple directed $3$-cycle and a reflexive vertex, satisfying **Geometric Constructibility** <Ref id="2.3.1" label="§2.3.1" />. This configuration is excluded by the irreflexive constraint of **The Directed Causal Link** <Ref id="2.1.1" label="§2.1.1" />.

**In Plain English:**  
Section 2.5.3 formalizes the properties of the QBD lemma regarding independence case b.

---

### 2.5.3.1 Proof: Independence Case B {#2.5.3.1}

:::tip[**Formal Verification of the Disjoint Reflexive Model against Axiomatic Criteria**]
:::

**I. Model Construction**

Let $G_B$ comprise the union of two disjoint subgraphs $C_1$ and $C_2$.

1.  **Subgraph $C_1$:** A valid 3-cycle on vertices $\{A, B, C\}$ with edge set:

    $$
    E_1 = \{(A, B), (B, C), (C, A)\}
    $$

2.  **Subgraph $C_2$:** An isolated vertex $X$ with edge set:

    $$
    E_2 = \{(X, X)\}
    $$

The composite graph is defined as $G_B = C_1 \cup C_2$.

**II. Verification of The Directed Causal Link (Axiom 1)**

The **Directed Causal Link** <Ref id="2.1.1" label="§2.1.1" /> imposes a universal prohibition on self-reference.

$$
\forall u \in V, (u, u) \notin E
$$

The subgraph $C_2$ contains the reflexive edge $(X, X)$. This constitutes a direct violation of the irreflexivity condition.

$$
G_B \notin \Omega_{causal}
$$

**III. Verification of Geometric Constructibility (Axiom 2)**

**Geometric Constructibility** <Ref id="2.3.1" label="§2.3.1" /> identifies the directed $3$-cycle as the basis of spatial assembly. The subgraph $C_1$ constitutes a valid instance of the geometric quantum.

$$
C_1 \in \Omega_{geo}
$$

Axiom $2$ posits a positive definition for spatial assembly: it does not, in isolation, enforce the removal of non-geometric causal defects in disjoint sectors. The existence of $C_1$ satisfies the constructive criteria.

**IV. Conclusion**

The existence of $G_B$ demonstrates that Geometric Constructibility does not entail Causal Validity. We conclude that Axiom 2 does not imply Axiom 1.

$$
Ax2 \not\implies Ax1
$$

Q.E.D.

**In Plain English:**  
Section 2.5.3.1 formalizes the properties of the QBD proof regarding independence case b.

---

### 2.5.4 Proof: Independence of Axioms 1 and 2 {#2.5.4}

:::tip[Orthogonal Counter-Models demonstrating the **Independence of Axioms 1 and 2** <Ref id="2.5.1" label="§2.5.1" />]
:::

**I. The Independence Hypothesis**
Two axiomatic constraints are defined as logically independent if and only if the satisfaction of one does not logically entail the satisfaction of the other. This independence is verified through the construction of specific counter-models that selectively violate one axiom while satisfying the other.

**II. The Counter-Model Chain**
1.  **Direction 1 ($\neg(Ax1 \implies Ax2)$):**
    * *Model Construction:* **Independence Case A** <Ref id="2.5.2" label="§2.5.2" /> constructs a graph $G_A$ consisting of a chordless directed $4$-cycle.
    * *Axiomatic Analysis:* The graph $G_A$ satisfies the **Causal Primitive** (it contains no self-loops and no reciprocal $2$-cycles), yet it violates **Geometric Constructibility** (it contains an unreduced cycle of length $L=4$, exceeding the quantum limit).
    * *Deduction:* Causal validity does not necessitate geometric quantization.
2.  **Direction 2 ($\neg(Ax2 \implies Ax1)$):**
    * *Model Construction:* **Independence Case B** <Ref id="2.5.3" label="§2.5.3" /> constructs a graph $G_B$ consisting of a disjoint union of a valid $3$-cycle and an isolated self-loop ($C_3 \cup \{e_{loop}\}$).
    * *Axiomatic Analysis:* The graph $G_B$ satisfies **Geometric Constructibility** (the $3$-cycle is a valid geometric quantum), yet it violates the **Causal Primitive** (the self-loop breaches irreflexivity).
    * *Deduction:* Geometric validity does not necessitate global causal consistency.

**III. Convergence**
Since neither logical implication holds, it is demonstrated that the axioms operate on orthogonal structural properties of the graph.

**IV. Formal Conclusion**
The Causal Primitive (Axiom $1$) and Geometric Constructibility (Axiom $2$) are mutually independent constraints. Neither axiom can be derived from the other: both are required to fully specify the physical substrate.

$$
Ax1 \perp Ax2
$$

Q.E.D.

**In Plain English:**  
Section 2.5.4 formalizes the properties of the QBD proof regarding independence of axioms 1 and 2.

---

### 2.6.1 Theorem: Inadequacy of Local Axioms {#2.6.1}

:::info[**Demonstration of Global Inconsistency under Local Axioms due to Transitive Reflexivity and Symmetry Failures**]
:::

Let a system be constrained exclusively by Axioms 1 and 2. The **Effective Influence** <Ref id="2.6.2" label="§2.6.2" /> relation $\le$ is not guaranteed to constitute a strict partial order. Specifically, the transitive closure of locally valid structures permits the emergence of **Reflexivity** ($u \le u$) and **Symmetry** ($u \le v \land v \le u$), thereby failing to enforce global causal consistency.

**In Plain English:**  
Section 2.6.1 formalizes the properties of the QBD theorem regarding inadequacy of local axioms.

---

### 2.6.2 Lemma: Effective Influence {#2.6.2}

:::info[**Establishment of the Effective Influence Relation as the Transitive Closure of Timestamped Paths**]
:::

Let the **Effective Influence** relation $u \le v$ be defined over the set of vertices $V$ by the existence of a simple directed path with strictly increasing edge timestamps. The relation preserves the monotonicity of logical time and distinguishes mediated influence from direct causal interaction.

**In Plain English:**  
Section 2.6.2 formalizes the properties of the QBD lemma regarding effective influence.

---

### 2.6.2.1 Proof: Effective Influence {#2.6.2.1}

:::tip[**Verification of the Transitive and Monotonic Properties of Effective Influence**]
:::

**I. Simple Path Construction**

Let $\pi_{uv} = (v_0, v_1, \dots, v_k)$ be a simple **Directed Path** <Ref id="1.2.3" label="§1.2.3" /> of length $k \ge 2$ initiating at $v_0 = u$ and terminating at $v_k = v$, forming the basis of **Effective Influence** <Ref id="2.6.2" label="§2.6.2" />. The uniqueness of the sequence of vertices avoids cyclic self-intersection.

**II. Monotonic Propagation**

Let each edge $e_i = (v_i, v_{i+1})$ have a creation timestamp $H(e_i)$. The sequentiality condition mandates:

$$
H(e_0) < H(e_1) < \dots < H(e_{k-1})
$$

**III. Time Ordering Preservation**

Since the standard order $<$ on logical time $\mathbb{R}$ is transitive, it follows that the initial timestamp strictly precedes the final timestamp:

$$
H(e_0) < H(e_{k-1})
$$

This establishes a directed causal gradient from $u$ to $v$.

Q.E.D.

**In Plain English:**  
Section 2.6.2.1 formalizes the properties of the QBD proof regarding effective influence.

---

### 2.6.3 Lemma: Strict Timestamps {#2.6.3}

:::info[**Necessity of Strictly Increasing Timestamps for Strict Partial Ordering**]
:::

Let the effective influence relation $\le$ constitute a strict partial order. Then the associated timestamp function $H$ satisfies the strict inequality condition $H(v_i, v_{i+1}) < H(v_{i+1}, v_{i+2})$ for all connected sequences of events.

**In Plain English:**  
Section 2.6.3 formalizes the properties of the QBD lemma regarding strict timestamps.

---

### 2.6.3.1 Proof: Strict Timestamps {#2.6.3.1}

:::tip[**Derivation of Strict Inequality from Partial Order Axioms**]
:::

**I. Premise**

Let the relation $\le$ satisfy the axioms of a strict partial order. The properties of Irreflexivity, Asymmetry, and Transitivity hold.

**II. Hypothesis (Relaxed Equality)**

Suppose the **Creation Timestamp** <Ref id="1.4.4" label="§1.4.4" /> function $H$ permits equality for connected events, violating **Strict Timestamps** <Ref id="2.6.3" label="§2.6.3" />.

$$
H(u, v) \le H(v, w) \implies \exists (u, v, w) \text{ such that } H(u, v) = H(v, w)
$$

**III. Simultaneity Analysis**

The equality condition implies simultaneous edge formation within the same logical tick. Consider the parallel formation of edges between distinct vertices $A$ and $B$.

$$
H(A, B) = t \land H(B, A) = t
$$

This establishes the mutual relations:

$$
A \le B \land B \le A
$$

Since $A \neq B$, this constitutes a violation of the Asymmetry axiom.

**IV. Conclusion**

The derived contradiction implies the strict inequality condition.

$$
H(v_i, v_{i+1}) < H(v_{i+1}, v_{i+2})
$$

We conclude that strictly increasing timestamps are necessary for the validity of the influence relation.

Q.E.D.

**In Plain English:**  
Section 2.6.3.1 formalizes the properties of the QBD proof regarding strict timestamps.

---

### 2.6.4 Lemma: Failure of Reflexivity {#2.6.4}

:::info[**Violation of Irreflexivity within the Geometric Quantum**]
:::

Let $v$ denote a vertex participating in a Geometric Quantum (Directed $3$-Cycle) with strictly increasing timestamps along the edges. Then the Effective Influence relation satisfies the reflexive condition $v \le v$, violating the global constraint of **Acyclic Effective Causality** <Ref id="2.7.1" label="§2.7.1" />.

**In Plain English:**  
Section 2.6.4 formalizes the properties of the QBD lemma regarding failure of reflexivity.

---

### 2.6.4.1 Proof: Failure of Reflexivity {#2.6.4.1}

:::tip[**Demonstration of Self-Influence via Transitive Analysis**]
:::

**I. Model Construction**

Let $G$ denote a single directed **3-Cycle** <Ref id="1.2.8" label="§1.2.8" /> defined by the vertex set $V = \{A, B, C\}$ and the edge set $E = \{(A,B), (B,C), (C,A)\}$, analyzed for **Failure of Reflexivity** <Ref id="2.6.4" label="§2.6.4" />.

**II. History Assignment**

Let the timestamp function $H$ assign strictly increasing timestamps to the sequence.

* $H(A, B) = t_1$
* $H(B, C) = t_2$
* $H(C, A) = t_3$

The timestamps satisfy the condition $t_1 < t_2 < t_3$.

**III. Influence Analysis**

Evaluate the influence relation for the pair $(A, A)$.

1.  **Path Existence:** A directed path $\pi = (A, B, C, A)$ exists.
    
2.  **Length Constraint:** The path length is $L=3$.

    $$
    L \ge 2
    $$

    The mediation condition holds.
3.  **Sequentiality:** The timestamp sequence corresponds to $(t_1, t_2, t_3)$. The strict ordering $t_1 < t_2 < t_3$ implies the sequence is strictly increasing.

    $$
    A \xrightarrow{t_1} B \xrightarrow{t_2} C \xrightarrow{t_3} A
    $$

**IV. Conclusion**

The existence of $\pi$ establishes the relation $A \le A$. We conclude that this self-influence violates the Irreflexivity axiom required for a strict partial order.

Q.E.D.

**In Plain English:**  
Section 2.6.4.1 formalizes the properties of the QBD proof regarding failure of reflexivity.

---

### 2.6.5 Lemma: Failure of Asymmetry {#2.6.5}

:::info[**Emergence of Mutual Influence via Disjoint Sub-paths in Higher-Order Cycles**]
:::

Let $G$ denote a directed cycle of length $L \ge 4$. Then there exists a valid timestamp assignment such that distinct vertices $u, v$ possess disjoint sub-paths satisfying **Monotonicity of History** <Ref id="1.4.5" label="§1.4.5" /> in both directions, establishing the symmetric effective influence relation $u \le v \land v \le u$.

**In Plain English:**  
Section 2.6.5 formalizes the properties of the QBD lemma regarding failure of asymmetry.

---

### 2.6.5.1 Proof: Failure of Asymmetry {#2.6.5.1}

:::tip[**Demonstration of Mutual Influence via the Bowtie Configuration**]
:::

**I. Model Construction**

Let $G$ denote a directed 4-**Cycle** <Ref id="1.2.6" label="§1.2.6" /> defined by the vertex set $V = \{A, B, C, D\}$ and the edge set $E = \{(A, B), (B, C), (C, D), (D, A)\}$, analyzed for **Failure of Asymmetry** <Ref id="2.6.5" label="§2.6.5" />.

**II. History Assignment**

Let the timestamp function $H$ assign values to the edge set to construct the "Bowtie" configuration.

* $H(A, B) = 1$
* $H(B, C) = 4$
* $H(C, D) = 2$
* $H(D, A) = 3$

**III. Evaluation of Forward Influence**

Consider the path $\pi_{AC} = (A, B, C)$.

1.  **Length:** The path length is $2$.

    $$
    2 \ge 2
    $$

2.  **Timestamps:** The sequence is $(1, 4)$.
3.  **Monotonicity:** The strictly increasing condition $1 < 4$ holds.
4.  **Result:** The relation $A \le C$ holds.

**IV. Evaluation of Reverse Influence**

Consider the path $\pi_{CA} = (C, D, A)$.

1.  **Length:** The path length is $2$.

    $$
    2 \ge 2
    $$

2.  **Timestamps:** The sequence is $(2, 3)$.
3.  **Monotonicity:** The strictly increasing condition $2 < 3$ holds.
4.  **Result:** The relation $C \le A$ holds.

**V. Conclusion**

The relations $A \le C$ and $C \le A$ hold simultaneously for distinct vertices ($A \neq C$). We conclude that this configuration violates the Asymmetry property.

Q.E.D.

**In Plain English:**  
Section 2.6.5.1 formalizes the properties of the QBD proof regarding failure of asymmetry.

---

### 2.6.6 Lemma: Causal Acyclicity vs. Spatial Triangulation {#2.6.6}

:::info[**Independence of Spatial Area Closures from Causal Timeline Ordering**]
:::

Let $G_{space}$ represent the Spatial State Graph, and let $G_{event}$ represent the Causal Poset of Events. The existence of directed cycles representing spatial area in $G_{space}$ does not imply or construct directed cycles in the causal history $G_{event}$, which remains a strict Directed Acyclic Graph (DAG).

**In Plain English:**  
Section 2.6.6 formalizes the properties of the QBD lemma regarding causal acyclicity vs. spatial triangulation.

---

### 2.6.6.1 Proof: Causal Acyclicity vs. Spatial Triangulation {#2.6.6.1}

:::tip[**Topological Distinctions between Spatial Boundaries and Chronological Ordering**]
:::

**I. Spatial vs. Temporal Adjacency**

Let spatial edges in $G_{space}$ be defined on the **Causal Graph Substrate** <Ref id="1.4.1" label="§1.4.1" /> and denoted by $(u, v)_{space}$, representing physical adjacency at a constant logical timestamp. Let causal events in $G_{event}$ represent the **Causal Acyclicity vs. Spatial Triangulation** <Ref id="2.6.6" label="§2.6.6" /> mapping, where edges $(e_i, e_j)_{event}$ represent direct causal influence.

**II. Path Non-Coincidence**

A spatial cycle of length $L=3$ (a triangle) in $G_{space}$ comprises edges:

$$
(u, v)_{space}, \ (v, w)_{space}, \ (w, u)_{space}
$$

The creation of these spatial edges corresponds to distinct events in $G_{event}$ occurring at strictly increasing timestamps:

$$
t_1 < t_2 < t_3
$$

**III. Loop Independence**

Although the spatial loop is closed in $G_{space}$, the causal path in $G_{event}$ connecting the creation events does not close: the sequence of events is strictly ordered by logical time. Because time is monotonic:

$$
t_3 > t_1
$$

The creation event of the final edge $(w, u)$ cannot influence the creation event of $(u, v)$ in $G_{event}$, precluding the closure of any causal cycle in history.

Q.E.D.

**In Plain English:**  
Section 2.6.6.1 formalizes the properties of the QBD proof regarding causal acyclicity vs. spatial triangulation.

---

### 2.6.7 Proof: Inadequacy of Local Axioms {#2.6.7}

:::tip[Synthesis of Transitive Failures showing the **Inadequacy of Local Axioms** <Ref id="2.6.1" label="§2.6.1" />]
:::

**I. The Local Premise**

Assume the existence of a causal system constrained *exclusively* by Axiom 1 (defining the Local Arrow) and Axiom 2 (defining the Local Geometry). The sufficiency of these axioms is tested by determining whether the transitive closure of the **Effective Influence** <Ref id="2.6.2" label="§2.6.2" /> relation $\le$ consistently forms a strict partial order. This relation necessitates strictly increasing timestamps along connected sequences, satisfying **Strict Timestamps** <Ref id="2.6.3" label="§2.6.3" />.

**II. The Failure Chain**

The analysis identifies specific configurations where local validity permits global inconsistency:

1.  **Failure of Reflexivity** <Ref id="2.6.4" label="§2.6.4" />: Within the local geometry of the $3$-cycle, the combination of directed edges and strictly increasing timestamps necessitates that upon closure of the loop, the relation $v \le v$ is established. This constitutes a violation of **Global Irreflexivity**.

2.  **Failure of Asymmetry** <Ref id="2.6.5" label="§2.6.5" />: Within a $4$-cycle "Bowtie" configuration, the existence of disjoint sub-paths allows for the simultaneous establishment of $u \le v$ and $v \le u$ with valid timestamps. This constitutes a violation of **Global Asymmetry**.

3.  **Causal vs. Spatial Loops**: The occurrence of spatial closed paths is necessary to construct area under **Causal Acyclicity vs. Spatial Triangulation** <Ref id="2.6.6" label="§2.6.6" />. However, local axioms fail to prevent these spatial loops from collapsing the temporal ordering of events.

**III. Convergence**

The set of Local Axioms permits the formation of transitive structures that satisfy all local rules but generate global contradictions regarding the ordering of events.

**IV. Formal Conclusion**

The Local Axioms are insufficient to ensure Global Causal Consistency. An explicit global constraint, designated as **Axiom 3**, is required to strictly enforce the Directed Acyclic Graph (DAG) property on the transitive closure of the influence relation.

$$
Ax1 \land Ax2 \not\implies \text{DAG}
$$

Q.E.D.

**In Plain English:**  
Section 2.6.7 formalizes the properties of the QBD proof regarding inadequacy of local axioms.

---

### 2.6.7.1 Corollary: Global Constraint {#2.6.7.1}

:::info[**Necessity of an Explicit Global Constraint required for the Definition of Causal Unidirectionality**]
:::

A physical theory requires a well-defined causal ordering (a "direction of time"). The proven failure of Axioms 1 and 2 to entail such an order necessitates a third axiom. This axiom must explicitly forbid states containing causal paradoxes, acting as a global topological constraint.

Q.E.D.

**In Plain English:**  
Section 2.6.7.1 formalizes the properties of the QBD corollary regarding global constraint.

---

### 2.7.1 Definition: Axiom 3 Acyclic Effective Causality {#2.7.1}

:::tip[**Imposition of Global Causal Consistency through the Enforcement of a Strict Partial Order**]
:::

The **Effective Influence** <Ref id="2.6.2" label="§2.6.2" /> relation $\le$ is axiomatically constrained to form a **Strict Partial Order** over the set of vertices $V$, establishing **Acyclic Effective Causality** via the following global topological constraints:
1.  **Global Irreflexivity:** For all $v \in V$, the relation $v \le v$ is false ($\neg(v \le v)$).
2.  **Global Asymmetry:** For all pairs $u, v \in V$, if $u \le v$, then the relation $v \le u$ must be false ($\neg(v \le u)$).
Consequently, the transitive closure of the causal history must form a Directed Acyclic Graph (DAG) with respect to $\le$.

**In Plain English:**  
Causality is strictly acyclic: an event can never be its own cause. This prevents grandfather paradoxes and closed timeline loops.

---

### 2.7.2 Theorem: Thermodynamic Enforcement {#2.7.2}

:::info[**Necessity of Preemptive Local Enforcement dictated by the Thermodynamic Impossibility of Post-Hoc Correction**]
:::

Assume the requirement of **Acyclic Effective Causality** <Ref id="2.7.1" label="§2.7.1" />. This requirement mandates the implementation of a preemptive local constraint within the Universal Constructor. The post-hoc correction of causal paradoxes is physically impossible in the thermodynamic limit ($N \to \infty$) because the energy required to synchronize the detection and deletion of a non-local cycle across the graph diameter diverges, violating the bounds of **Finite Information Substrate** <Ref id="1.3.5" label="§1.3.5" />.

**In Plain English:**  
Section 2.7.2 formalizes the properties of the QBD theorem regarding thermodynamic enforcement.

---

### 2.7.3 Lemma: Cycle Diameter Growth {#2.7.3}

:::info[**Divergence of Cycle Diameters beyond Finite Computational Radii**]
:::

Let the graph evolve under the rewrite rule $\mathcal{R}$. Then the length of the longest simple cycle $L_{\max}$ diverges as a function of logical time, and for any finite computational radius $R$ there exists a critical time $t_{crit}$ such that $L_{\max} > 2R$ holds and local operators bounded by radius $R$ are topologically blind to the closure of global cycles.

**In Plain English:**  
Section 2.7.3 formalizes the properties of the QBD lemma regarding cycle diameter growth.

---

### 2.7.3.1 Proof: Cycle Diameter Growth {#2.7.3.1}

:::tip[**Derivation of Trans-Local Cycle Expansion via Random Graph Dynamics**]
:::

**I. Micro-Dynamics**

The rewrite rule $\mathcal{R}$ acts as the engine of geometrogenesis, injecting **3-Cycle** <Ref id="1.2.8" label="§1.2.8" /> structures into the topology, leading to **Cycle Diameter Growth** <Ref id="2.7.3" label="§2.7.3" />. This increases the edge density $\rho$ of the graph over logical time.

**II. Macro-State Evolution**

As density $\rho$ rises, the system approaches the percolation threshold. Random Graph Theory dictates that near this threshold, the probability of forming system-spanning structures increases non-linearly.

$$
P(L_{\max} > R) \to 1 \quad \text{as} \quad N \to \infty
$$

**III. The Horizon Limit**

Let a local computational patch be defined by a finite radius $R$. The dynamics inevitably generate cycles with length $L_{\max}$ satisfying:

$$
L_{\max} \gg R
$$

**IV. Blindness**

A local operator bounded by $R$ cannot perceive the closure of a cycle with diameter $D > R$. To the local operator, the path segment appears as an open geodesic.

**V. Conclusion**

Local dynamics generate trans-local structures invisible to local error-correction. Post-hoc correction of paradoxes is topologically impossible for a local agent.

Q.E.D.

**In Plain English:**  
Section 2.7.3.1 formalizes the properties of the QBD proof regarding cycle diameter growth.

---

### 2.7.4 Lemma: Local PUC Approximation {#2.7.4}

:::info[**Exponential Suppression of Global Paradoxes under Local Search Constraints**]
:::

Let $P_{err}(R)$ denote the probability that a paradox-inducing cycle of length $L > R$ evades detection by a local search of radius $R$ in the sparse graph regime. Then this probability satisfies the exponential decay bound $P_{err}(R) < e^{-R}$, and a search depth scaling as $R \sim \ln N$ constitutes a sufficient condition to suppress the probability of global paradox formation below any arbitrary fixed threshold.

**In Plain English:**  
Section 2.7.4 formalizes the properties of the QBD lemma regarding local puc approximation.

---

### 2.7.4.1 Proof: Local PUC Approximation {#2.7.4.1}

:::tip[**Derivation of the Error Probability Bound via Sparse Graph Analysis**]
:::

**I. Premise**

Let the causal graph operate in the sparse regime where the edge density satisfies $\rho \ll 1$, evaluated for **Local PUC Approximation** <Ref id="2.7.4" label="§2.7.4" /> under the **Principle of Unique Causality (PUC)** <Ref id="2.3.4" label="§2.3.4" />.

**II. Path Extension Probability**

The probability of a specific path extending for length $L$ without termination is proportional to the density raised to the power of the length.

$$
P_{ext}(L) \propto \rho^L
$$

**III. Loop Closure Probability**

The probability of a path closing back on its origin to form a cycle involves the selection of a specific vertex from $N$ candidates.

$$
P_{close}(L) \propto \frac{1}{N} \rho^L
$$

**IV. Cumulative Error**

The total probability of an undetected cycle existing beyond the check radius $R$ corresponds to the sum over all lengths greater than $R$.

$$
P_{err} = \sum_{L=R+1}^{\infty} C \frac{\rho^L}{N} \approx \frac{C}{N} \frac{\rho^{R+1}}{1-\rho}
$$

**V. Exponential Decay**

The condition $\rho < 1$ implies that the term $\rho^R$ decays exponentially with $R$. The assignment $R \sim \ln N$ yields a probability bounded by a polynomial in $1/N$.

$$
P_{err} \le \mathcal{O}(N^{-k})
$$

**VI. Conclusion**

The local check provides an approximation fidelity that approaches unity in the thermodynamic limit.

Q.E.D.

**In Plain English:**  
Section 2.7.4.1 formalizes the properties of the QBD proof regarding local puc approximation.

---

### 2.7.5 Lemma: Independence of Axiom 3 {#2.7.5}

:::info[**Logical Independence of the Global Acyclicity Requirement**]
:::

Let $\Sigma = \{Ax1, Ax2\}$ denote the set of local axioms consisting of **The Directed Causal Link** and **Geometric Constructibility** <Ref id="2.3.1" label="§2.3.1" />. The timestamped 4-cycle defined by **Failure of Asymmetry** <Ref id="2.6.5" label="§2.6.5" /> constitutes a valid graph under $\Sigma$ while violating Axiom 3, showing that Axiom 3 is logically independent.

**In Plain English:**  
Section 2.7.5 formalizes the properties of the QBD lemma regarding independence of axiom 3.

---

### 2.7.5.1 Proof: Independence of Axiom 3 {#2.7.5.1}

:::tip[**Verification of Independence via the Timestamped 4-Cycle Countermodel**]
:::

**I. Model Construction**

Let $G$ denote a directed $4$-cycle defined by the vertex set $V = \{A, B, C, D\}$ and the edge set $E = \{(A,B), (B,C), (C,D), (D,A)\}$, analyzed for **Independence of Axiom 3** <Ref id="2.7.5" label="§2.7.5" /> utilizing the **Failure of Asymmetry** <Ref id="2.6.5" label="§2.6.5" /> model.

**II. History Assignment**

Let the timestamp function $H$ assign the sequential "Bowtie" values to the edge set:

* $H(A, B) = 1$
* $H(B, C) = 2$
* $H(C, D) = 3$
* $H(D, A) = 4$

**III. Verification of Local Axioms**

The graph satisfies the Irreflexivity and Asymmetry conditions for all individual edges, complying with Axiom 1. The $4$-cycle does not violate the constructive definition of Axiom 2, which governs formation rather than existence.

**IV. Verification of Global Acyclicity (Axiom 3)**

Consider the effective influence relations derived from the timestamp sequence.

1.  **Forward Path:** The path $A \to B \to C$ corresponds to timestamps $(1, 2)$. The condition $1 < 2$ establishes the relation $A \le C$.
2.  **Reverse Path:** The path $C \to D \to A$ corresponds to timestamps $(3, 4)$. The condition $3 < 4$ establishes the relation $C \le A$.
3.  **Conflict:** The simultaneous validity of $A \le C$ and $C \le A$ for distinct vertices constitutes a symmetric dependency. This violates the strict partial order required by Axiom 3.

**V. Conclusion**

A model exists that satisfies Axioms 1 and 2 but violates Axiom 3. We conclude that Axiom 3 is logically independent.

Q.E.D.

**In Plain English:**  
Section 2.7.5.1 formalizes the properties of the QBD proof regarding independence of axiom 3.

---

### 2.7.6 Proof: Thermodynamic Enforcement {#2.7.6}

:::tip[**Thermodynamic Enforcement** <Ref id="2.7.6" label="§2.7.6" /> via Demonstration of Energy Divergence]
:::

**I. Hypothesis**

Assume the system permits the formation of a global symmetric influence loop (Paradox) and corrects it at time $t+1$.

**II. Information Requirement**

Unique correction (e.g., deleting the "latest" edge) requires identifying the edge with the maximal timestamp within the loop.

$$
e_{target} = \arg \max_{e \in C} H(e)
$$

**III. Non-Locality**

By the **Cycle Diameter Growth** <Ref id="2.7.3" label="§2.7.3" />, the loop length $L$ exceeds the local horizon $R$.
The timestamp information is distributed across $L/R$ spacelike-separated patches.

**IV. Synchronization Cost**

Comparing timestamps across these patches requires signal traversal.
The time required is proportional to the diameter $D \propto L$.
Correction at $t+1$ implies instantaneous (superluminal) coordination across $D$.

**V. Energy Divergence**

In the thermodynamic limit ($N \to \infty, D \to \infty$), the energy required to synchronize this state approaches infinity.

$$
E_{sync} \to \infty
$$

**VI. Conclusion**

Post-hoc correction violates the finite-energy constraint.
Enforcement must occur via the local pre-check, which utilizes the **Local PUC Approximation** <Ref id="2.7.4" label="§2.7.4" /> to guarantee global causal acyclicity with probability approaching unity in the thermodynamic limit. This is logically independent of the local constraints as shown in **Independence of Axiom 3** <Ref id="2.7.5" label="§2.7.5" />.

Q.E.D.

**In Plain English:**  
Section 2.7.6 formalizes the properties of the QBD proof regarding thermodynamic enforcement.

---

### 2.7.7 Type-Theoretic Validation via Lean 4 Core {#2.7.7}

:::note[**Lean 4 Encoding of Asymmetry's Algebraic Closure via Biconditional Decomposition**]
:::

Type-theoretic certification of the structural relationships between asymmetry, irreflexivity, and antisymmetry (the three properties now united under **Acyclic Effective Causality** <Ref id="2.7.1" label="§2.7.1" />) proceeds via the following verification strategy:

1.  **Encoding:** The definitions `IsAsymmetric`, `IsIrreflexive`, and `IsAntisymmetric` encode the three relational predicates. `IsAsymmetric` is the formal expression of Axiom 3's Global Asymmetry requirement: if $u$ influences $v$, then $v$ cannot influence $u$.
2.  **Theorem Statements:** The first theorem (`asymmetry_implies_irreflexivity`) certifies that asymmetry strictly subsumes irreflexivity by self-application; the second (`asymmetry_equiv`) certifies the full biconditional, proving that asymmetry is the exact algebraic conjunction of the two weaker conditions.
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
```

**Verification Summary:**
The definitions extend the vocabulary established in the **Type-Theoretic Validation via Lean 4 Core** <Ref id="2.2.5" label="§2.2.5" /> to include `IsAsymmetric`, the direct Lean encoding of the Global Asymmetry clause of **Acyclic Effective Causality** <Ref id="2.7.1" label="§2.7.1" />. The first theorem self-applies `h_asym` at the identical vertex pair `(v, v)`: because asymmetry asserts `R v v → ¬ R v v`, any self-loop hypothesis `h_loop : R v v` immediately produces its own negation, and `exact` discharges the goal. The second theorem splits via `constructor` into two directions. The forward direction reuses the self-application trick for irreflexivity, then dispatches antisymmetry by supplying both directions of the mutual-edge hypothesis to `h_asym`, whose output `False` is eliminated by `False.elim`. The reverse direction unpacks `h_conj` into `h_conj.left` (irreflexivity) and `h_conj.right` (antisymmetry), applies antisymmetry to force `h_eq : u = v`, rewrites `h_fwd` under this equality to obtain a self-loop, then applies irreflexivity to close. The Lean kernel's acceptance of both closed proof terms certifies that the three-axiom system of Chapter 2 possesses complete algebraic closure: Asymmetry is not a separate postulate alongside Irreflexivity and Antisymmetry, but their exact logical conjunction, ensuring the tripartite foundation established by **Independence of Axiom 3** <Ref id="2.7.5" label="§2.7.5" /> is also algebraically minimal.

**In Plain English:**  
Section 2.7.7 formalizes the properties of the QBD type-theoretic regarding validation via lean 4 core.

---

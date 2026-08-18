---
title: "Appendix B: Master List of Definitions & Theorems - Chapter 1"
sidebar_class_name: "theme-doc-sidebar-item-hidden"
---

This appendix serves as a centralized, rigorous catalog of the foundational mathematical postulates, definitions, axioms, lemmas, and theorems introduced in Chapter 1 of the Quantum Braid Dynamics (QBD) monograph.

---

### 1.1.5 Axiom of Choice {#1.1.5}

:::info[**Acceptance of Non-Constructive Principles based on Systemic Fertility**]
:::

If the debate over the parallel postulate marked the birth of a new view on axioms, the controversy surrounding the Axiom of Choice represents its full maturation. Here, the justification for adopting a foundational principle is almost entirely divorced from physical intuition or self-evidence, resting instead on the internal coherence and sheer utility of the mathematical system it enables.

**Introducing the Axiom of Choice**

First formulated by Ernst Zermelo in 1904, the Axiom of Choice states that for any collection of non-empty sets, there exists a function (a "choice function") that selects exactly one element from each set. For a finite collection, this is provable from more basic axioms. The power and controversy of AC arise when dealing with infinite collections. Bertrand Russell's famous analogy clarifies its nature:

  * Given an infinite collection of pairs of shoes, one can define a choice function ("for each pair, choose the left shoe").
  * But for an infinite collection of pairs of socks, where the two members of a pair are indistinguishable, no such defining rule exists.

AC asserts that a choice function nevertheless exists, even if it cannot be constructed or explicitly defined.

**Controversy and Counterintuitive Consequences**

This non-constructive character is the primary source of objection to AC, particularly from mathematicians of the constructivist and intuitionist schools, for whom "to exist" means "to be constructible". The axiom's acceptance leads to a number of deeply counterintuitive results that challenge physical understanding. The most famous of these is the Banach-Tarski paradox, which demonstrates that a solid sphere can be decomposed into a finite number of non-overlapping pieces, which can then be reassembled by rigid motions to form two solid spheres, each identical in size to the original. This result appears to violate the conservation of volume, but the paradox is resolved by noting that the "pieces" involved are so complex that they are non-measurable, as they cannot be assigned a well-defined volume.

**Justification through Systemic Utility and Equivalence**

Despite these paradoxes, the Axiom of Choice is a standard and indispensable component of modern mathematics, forming the C in ZFC (Zermelo-Fraenkel set theory with Choice), the most common foundation for the field. Its justification is almost entirely pragmatic, stemming from its immense power and the elegance of the theories it facilitates. Within the context of the other ZF axioms, AC is logically equivalent to several other powerful and widely used principles, most notably:

  * Zorn's Lemma: This principle states that a partially ordered set in which every chain (totally ordered subset) has an upper bound must contain at least one maximal element.
  * The Well-Ordering Principle: This principle asserts that any set can be "well-ordered," meaning its elements can be arranged in an order such that every non-empty subset has a least element.
    These equivalent forms, particularly Zorn's Lemma, are essential tools in numerous branches of mathematics. Their use is critical in proving fundamental theorems such as:
  * Every vector space has a basis.
  * Every commutative ring with a unit element contains a maximal ideal (Krull's Theorem).
  * The product of any collection of compact topological spaces is compact (Tychonoff's Theorem).

The mathematical community has largely accepted AC because rejecting it would mean abandoning these and countless other foundational results, effectively crippling vast areas of modern algebra, analysis, and topology. The justification is not its intuitive plausibility, but its mathematical fertility. The matter was settled formally when Kurt Gödel (1938) and Paul Cohen (1963) proved that AC is independent of the other axioms of ZF set theory; it can be neither proved nor disproved from them. Its inclusion is a genuine choice, and that choice has been made in favor of systemic power over intuitive comfort.

**In Plain English:**  
Section 1.1.5 formalizes the properties of the QBD axiom regarding axiom of choice.

---

### 1.1.6 Principle: Coherentist Justification {#1.1.6}

:::info[**Justification of Unprovable Postulates by Coherentist Criteria**]
:::

The historical evolution of axiomatic justification, epitomized by the independence of Euclid's parallel postulate and the pragmatic acceptance of the Axiom of Choice, demonstrates that when foundational postulates cannot be syntactically derived or intuitively verified as "self-evident," their legitimacy rests upon **Coherentist Justification**. Rather than seeking validation from an impossible chain of antecedent proofs, the axiomatic basis $\mathcal{A}$ of a formal deductive system $\mathfrak{D} = (\mathcal{L}, \mathcal{A}, \mathcal{I})$ is justified holistically by the emergent properties of the global structure it generates.

The adoption of an Axiomatic Basis $\mathcal{A}$ is governed exclusively by the satisfaction of four **Coherence Criteria**:

1. **Consistency:** The absolute guarantee of formal non-contradiction, ensuring $\mathcal{A} \nvdash \perp$.
2. **Independence:** The minimality of the basis, such that for every $a \in \mathcal{A}$, $\mathcal{A} \setminus \{a\} \nvdash a$, ensuring no redundant assumptions are codified as axioms.
3. **Parsimony:** The minimization of the cardinality $|\mathcal{A}|$ and structural complexity of postulates relative to the explanatory scope of the system (Occam's razor).
4. **Fertility (Systemic Utility):** The capacity of $(\mathcal{L}, \mathcal{A}, \mathcal{I})$ to generate a rich, non-trivial body of theorems ($\mathcal{A} \vdash \theta$) that unifies disparate structures, resolves foundational paradoxes, and, in the construction of a physical theory, maps isomorphically to observable phenomena.

**Holistic Support vs. Linear Circularity**

Coherentist justification replaces the classical foundationalist model, which envisions knowledge as a hierarchical tower resting upon "self-evident" bedrock, with a relational model (analogous to Otto Neurath's ship), wherein foundational postulates and derived theorems exist in a web of mutual support.

Crucially, this mode of justification does not commit the fallacy of circular reasoning (*petitio principii*). A circular argument operates linearly ($P \vdash P$), providing no new explanatory content. Coherentist validation operates non-linearly: the axiomatic basis $\mathcal{A}$ is not proved by its consequences, but rather justified by the global stability, parsimony, and mathematical and empirical fertility of the complete deductive edifice.

:::note[**Summary Table: Epistemological Approaches**]
:::

| Dimension | Foundationalist View (Classical) | Coherentist View (Formalist / Constructive) |
| :--- | :--- | :--- |
| **Nature of Axioms** | Self-evident truths; direct descriptions of an absolute, pre-existing reality. | Foundational assumptions; formal rules defining a generative system. |
| **Source of Justification** | Direct intuition, self-evidence, or linear antecedent derivation. | Systemic properties: consistency ($\nvdash \perp$), parsimony ($|\mathcal{A}|$), and generative fertility. |
| **Structure of Knowledge** | Hierarchical pyramid resting on basic, unshakeable beliefs. | Holistic web of mutual logical and structural coherence. |
| **Status of Alternatives** | Categorically false if non-corresponding to intuitive reality. | Valid alternative formal systems; selection is adjudicated pragmatically by systemic fertility and coherence. |

**In Plain English:**  
Section 1.1.6 formalizes the properties of the QBD principle regarding coherentist justification.

---

### 1.2.1 Definition: Directed Acyclic Graph (DAG) {#1.2.1}

:::tip[**Directed Acyclic Graph (DAG) as the Relational Foundation of Causal Order**]
:::

A **Directed Acyclic Graph (DAG)** is a directed graph $G = (V, E)$ containing no directed cycles. Formally, there exists no sequence of vertices $(v_0, v_1, \dots, v_k)$ in $V$ of length $k \ge 1$ such that $v_0 = v_k$ and $(v_i, v_{i+1}) \in E$ for all $0 \le i < k$.

**In Plain English:**  
Space is built from simple discrete connections: single links represent precedence, 2-paths represent transitive mediation, and 3-cycles represent spatial area.

---

### 1.2.2 Definition: Bipartite Graph {#1.2.2}

:::tip[**Bipartite Graph as the Partitioned Architecture of State Transitions**]
:::

A **Bipartite Graph** is a directed graph $G = (V, E)$ whose vertex set $V$ can be partitioned into two disjoint sets, $V_A$ and $V_B$ (where $V_A \cup V_B = V$ and $V_A \cap V_B = \emptyset$), such that every directed edge connects a vertex in $V_A$ to a vertex in $V_B$ or vice versa. Formally, the edge set satisfies $E \subseteq (V_A \times V_B) \cup (V_B \times V_A)$.

**In Plain English:**  
Section 1.2.2 formalizes the properties of the QBD definition regarding bipartite graph.

---

### 1.2.3 Definition: Directed Path {#1.2.3}

:::tip[**Directed Path as the Sequence of Relational Causality**]
:::

A **Directed Path** in a directed graph $G = (V, E)$ is a sequence of vertices $(v_0, v_1, \dots, v_n)$ of length $n \ge 0$ such that for all $0 \le i < n$, the directed edge $(v_i, v_{i+1}) \in E$.

**In Plain English:**  
Section 1.2.3 formalizes the properties of the QBD definition regarding directed path.

---

### 1.2.4 Definition: Simple Path {#1.2.4}

:::tip[**Simple Path as the Acyclic Trajectory of Influence**]
:::

A **Simple Path** is a Directed Path $(v_0, v_1, \dots, v_n)$ containing no repeated vertices. Formally, $v_i \neq v_j$ for all $0 \le i < j \le n$.

**In Plain English:**  
Section 1.2.4 formalizes the properties of the QBD definition regarding simple path.

---

### 1.2.5 Definition: 2-Path {#1.2.5}

:::tip[**2-Path as the Minimal Unit of Transitive Mediation**]
:::

A **2-Path** is a simple Directed Path of length exactly $2$. Formally, it is denoted as an ordered triplet of distinct vertices $(v, w, u)$ such that $(v, w) \in E$ and $(w, u) \in E$.

**In Plain English:**  
A 2-path consists of three events connected in sequence (A causes B, B causes C), constituting the minimal pathway for causal influence to propagate.

---

### 1.2.6 Definition: Cycle {#1.2.6}

:::tip[**Cycle as the General Topological Expression of Causal Closure**]
:::

A **Cycle** (or directed cycle) is a non-trivial Directed Path $(v_0, v_1, \dots, v_k)$ of length $k \ge 1$ such that $v_0 = v_k$.

**In Plain English:**  
Section 1.2.6 formalizes the properties of the QBD definition regarding cycle.

---

### 1.2.7 Definition: 2-Cycle {#1.2.7}

:::tip[**2-Cycle as the Minimal Unit of Reciprocal Causality**]
:::

A **2-Cycle** is a Cycle of length exactly $k=2$. Formally, it consists of a pair of distinct vertices $\{u, v\}$ such that $(u, v) \in E$ and $(v, u) \in E$.

**In Plain English:**  
Section 1.2.7 formalizes the properties of the QBD definition regarding 2-cycle.

---

### 1.2.8 Definition: 3-Cycle {#1.2.8}

:::tip[**3-Cycle as the Minimal Closed Loop Enclosing a Topological Area**]
:::

A **3-Cycle** is a Cycle of length exactly $k=3$. Formally, it consists of a triplet of distinct vertices $(A, B, C)$ such that $(A, B) \in E$, $(B, C) \in E$, and $(C, A) \in E$.

**In Plain English:**  
Section 1.2.8 formalizes the properties of the QBD definition regarding 3-cycle.

---

### 1.3.1 Definition: Dual Time Architecture {#1.3.1}

:::tip[**Mathematical Characterization of the Dual Temporal Scales as a Formal Architecture**]
:::

The temporal structure of the physical theory is defined as a **Dual Time Architecture** constituted by the pair $(t_{phys}, t_L)$, consisting of an emergent Physical Time ($t_{phys}$) and a fundamental Global Logical Time ($t_L$).

**In Plain English:**  
Time in QBD operates in a dual fashion: physical time (the relativistic, continuous time experienced by observers inside the universe) and global logical time (a step counter for the universe's evolution engine).

---

### 1.3.2 Definition: Emergent Physical Time {#1.3.2}

:::tip[**Mathematical Characterization as Relational Physical Duration**]
:::

Let $G = (V, E, H)$ be a causal graph. For any directed causal path $\pi = (v_0, v_1, \dots, v_k)$ in $G$ representing an observer's trajectory, the **Emergent Physical Time** interval $\Delta t_{phys}$ along the path is defined as:

$$
\Delta t_{phys} = \tau(\pi) = f\left(k, \{H(e) \mid e \in \pi\}\right)
$$

where $k$ is the topological path length and $f$ is a scaling function mapping discrete edge creation timestamps to proper time, emerging as continuous physical time in the macroscopic limit.

**In Plain English:**  
Physical time is relationally defined as proper time computed along causal paths of the graph, emerging as continuous coordinate duration in the macroscopic limit.

---

### 1.3.3 Definition: Global Logical Time {#1.3.3}

:::tip[**Global Sequencer ($t_L$) as the Fundamental Iterator of State Evolution**]
:::

Let $\mathcal{U}$ denote the Universal Evolution Operator. The **Global Logical Time**, denoted $t_L \in \mathbb{N}_0$, is the discrete, non-negative integer parameter indexing the sequence of global states of the universe under the repeated action of $\mathcal{U}$:

$$
U_0 \xrightarrow{\mathcal{U}} U_1 \xrightarrow{\mathcal{U}} U_2 \xrightarrow{\mathcal{U}} \dots \xrightarrow{\mathcal{U}} U_{t_L}
$$

where each application of $\mathcal{U}$ maps state $U_{t_L}$ to $U_{t_L+1}$, establishing a strict total order on the history of the universe.

**In Plain English:**  
Logical time is a discrete sequence of integer steps tracking the repeated application of the universal update operator, ensuring an absolute causal order.

---

### 1.3.4 Theorem: Temporal Finitude {#1.3.4}

:::info[**Necessity of a Finite Temporal Origin demanded by the Logical Exclusion of Infinite Regress**]
:::

The following holds: the domain of Global Logical Time $t_L$ is strictly lower-bounded. There exists a unique initial state, designated $U_0$, which possesses no causal predecessor. The domain of $t_L$ is isomorphic to the set of non-negative integers $\mathbb{N}_0$, establishing a definite moment of genesis for the computational process.

**In Plain English:**  
The universe must have had a beginning (a logical step zero) because an infinite past would require infinite information capacity, resulting in thermodynamic collapse.

---

### 1.3.5 Lemma: Finite Information Substrate {#1.3.5}

:::info[**Finiteness via Quadratic Boundedness of the Information Substrate**]
:::

Let $t_L$ denote a finite logical time. Then the information content $S(U_{t_L})$ is strictly finite, and the growth of this content is bounded by a quadratic function of logical time, $S(U_{t_L}) \le \mathcal{O}(t_L^2)$.

**In Plain English:**  
The amount of information needed to describe the universe's state cannot grow faster than a quadratic curve, preventing informational overload and keeping the system stable.

---

### 1.3.5.1 Proof: Finite Information Substrate {#1.3.5.1}

:::tip[**Derivation of the Quadratic Entropy Bound via Inductive Branching**]
:::

**I. Setup and Assumptions**

Let $\Omega_{t}$ denote the set of admissible physical states at logical time $t$, as governed by the **Global Logical Time** <Ref id="1.3.3" label="§1.3.3" /> coordinate. Let $S(U_{t}) = \log_2 |\Omega_{t}|$ quantify the information content of the **Dual Time Architecture** <Ref id="1.3.1" label="§1.3.1" /> state.

The physical postulates impose the following growth constraints:

1. **Finite Local Branching ($b$):** The **Finite Nature Hypothesis** limits the update capacity of the substrate. The number of physically distinct successor states for any state $U$ is bounded by the local branching factor $b$ raised to the number of active sites.

$$
\forall U \in \Omega, \quad | \{ U' \mid U \xrightarrow{\mathcal{U}} U' \} | \le b^{s_t}
$$

2. **Causal Horizon Scaling ($\delta_{\text{holo}}$):** The number of active degrees of freedom is restricted to the cardinality of the growth front, defined as the set of maximal elements within the poset. In a causally expanding discrete graph, this boundary cardinality $s_t$ is bounded by a linear function of the poset height:

$$
s_{t} \le \delta_{\text{holo}} \cdot t \quad \text{where } \delta_{\text{holo}} > 0
$$

**II. Derivation**

The cardinality of the state space at step $t+1$ is bounded by the product of the previous cardinality and the successor count defined by the branching factor and active sites.

$$
|\Omega_{t+1}| \le |\Omega_t| \cdot b^{s_t}
$$

We apply a logarithmic transformation to convert this product into a summation for the entropy calculation:

$$
\log_2 |\Omega_{t+1}| \le \log_2 |\Omega_t| + \log_2(b^{s_t})
$$

Simplifying the expression yields the relational entropy formula:

$$
S(U_{t+1}) \le S(U_t) + s_t \log_2 b
$$

Let $\Delta S_t = S(U_{t+1}) - S(U_t)$ define the incremental entropy change. We substitute the **Holographic Surface Scaling** constraint to yield the explicit upper bound:

$$
\Delta S_t \le (\delta_{\text{holo}} t) \log_2 b
$$

**III. Accumulation**

The total entropy at time $T$ constitutes the sum of the initial entropy and all incremental changes.

$$
S(U_T) = S(U_0) + \sum_{t=0}^{T-1} \Delta S_t
$$

The unique primordial vacuum at $t=0$ establishes the **Base Case**:

$$
|\Omega_0| = 1 \implies S(U_0) = 0
$$

We substitute the derived bound for $\Delta S_t$ into the cumulative sum:

$$
S(U_T) \le 0 + \sum_{t=0}^{T-1} (\delta_{\text{holo}} t \log_2 b)
$$

Factoring out the time-independent constants by defining $C = \delta_{\text{holo}} \log_2 b$ isolates the arithmetic series:

$$
S(U_T) \le C \sum_{t=0}^{T-1} t
$$

**IV. Resolution and Conclusion**

We evaluate the arithmetic series via the standard summation formula with $n = T-1$:

$$
\sum_{t=0}^{T-1} t = \frac{(T-1)((T-1)+1)}{2}
$$

Simplifying the terms sequentially yields the explicit polynomial components:

$$
\sum_{t=0}^{T-1} t = \frac{(T-1)T}{2}
$$

$$
\sum_{t=0}^{T-1} t = \frac{T^2 - T}{2}
$$

We substitute this result back into the entropy inequality:

$$
S(U_T) \le C \cdot \left( \frac{T^2 - T}{2} \right)
$$

Expanding the expression restores the explicit physical constants:

$$
S(U_T) \le \frac{\delta_{\text{holo}} \log_2 b}{2} (T^2 - T)
$$

For $T > 1$, the quadratic term strictly dominates the linear term, establishing the inequality $T^2 - T < T^2$. This dominance relation yields the strict upper bound:

$$
S(U_T) < \frac{\delta_{\text{holo}} \log_2 b}{2} T^2
$$

We conclude that the information content growth is bounded by a quadratic function of logical time:

$$
S(U_{t_L}) \le \mathcal{O}(t_L^2)
$$

This scaling holds universally for any locally finite, causally expanding graph.

Q.E.D.

**In Plain English:**  
Section 1.3.5.1 formalizes the properties of the QBD proof regarding finite information substrate.

---

### 1.3.6 Lemma: Backward Accumulation {#1.3.6}

:::info[**Exclusion of Unbounded Past Direction due to Backward Accumulation**]
:::

Assume the domain of the global logical time parameter $T$ extends to the infinite past. Therefore, this unbounded configuration is excluded by the **Finite Information Substrate** <Ref id="1.3.5" label="§1.3.5" />.

**In Plain English:**  
Section 1.3.6 formalizes the properties of the QBD lemma regarding backward accumulation.

---

### 1.3.6.1 Proof: Backward Accumulation {#1.3.6.1}

:::tip[**Derivation of Contradiction via Entropy and Capacity Divergence**]
:::

**I. Setup and Assumptions**

Let the temporal domain be unbounded in the past direction, denoted $T = \mathbb{Z}_{\le 0}$. Let the history of the universe be the infinite sequence of states $\mathcal{H} = \{ \dots, U_{-n}, \dots, U_{-1}, U_0 \}$.

**II. Case A: Irreversible Dynamics**

Let $\mathcal{U}$ be a dissipative operator satisfying the Second Law of Thermodynamics. Let $\Delta S_k = S(U_{k+1}) - S(U_k)$ denote the entropy production at step $k$.

1. **Thermodynamic Positivity:**
   For non-equilibrium evolution involving coarse-graining or erasure, the expected entropy production is strictly positive:

   $$
   \mathbb{E}[\Delta S_k] = \mu > 0
   $$

   The fluctuations are bounded by the **Finite Information Substrate** <Ref id="1.3.5" label="§1.3.5" />:

   $$
   \text{Var}(\Delta S_k) = \sigma^2 < \infty
   $$

2. **Cumulative Summation:**
   The total entropy at the present $t=0$ is the accumulation of all prior productions. Let $S_n$ denote the sum over the past $n$ steps:

   $$
   S_n = \sum_{k=-n}^{-1} \Delta S_k
   $$

3. **Probabilistic Divergence:**
   Chebyshev's Inequality bounds the deviation of the time-averaged entropy production from the mean $\mu$:

   $$
   \mathbb{P}\left( \left| \frac{S_n}{n} - \mu \right| > \epsilon \right) \le \frac{\sigma^2}{n \epsilon^2}
   $$

   The limit $n \to \infty$ drives the probability of deviation to zero:

   $$
   \lim_{n \to \infty} \mathbb{P}\left( \left| \frac{S_n}{n} - \mu \right| > \epsilon \right) = 0
   $$

   This implies almost sure convergence of the sum to the linear growth trend:

   $$
   S(U_0) \approx \lim_{n \to \infty} n\mu = \infty
   $$

4. **Contradiction:**
   The divergence $S(U_0) \to \infty$ is excluded by the **Finite Information Substrate** <Ref id="1.3.5" label="§1.3.5" />.

**III. Case B: Reversible Dynamics**

Let $\mathcal{U}$ be a strictly unitary (bijective) operator.

$$
U_{t+1} = \mathcal{U}(U_t) \iff U_t = \mathcal{U}^{-1}(U_{t+1})
$$

1. **Injectivity of History:**
   The requirement of a non-cyclic history implies injectivity of the mapping from time to state:

   $$
   \forall t_a, t_b \in T, \quad t_a \neq t_b \implies U_{t_a} \neq U_{t_b}
   $$

2. **Information Preservation:**
   In a deterministic reversible system, unitarity requires that the present state $U_0$ encode the unique trajectory of the past. Let $\Delta I_k$ denote the unique information bit distinguishing state $U_{-k}$ from any other state in the sequence:

   **1 bit** is the minimal bound.

3. **Capacity Aggregation:**
   The total information capacity required for $U_0$ to distinguish an infinite set of unique predecessors is the sum of these contributions:

   $$
   I(U_0) \ge \sum_{k=1}^{\infty} \Delta I_{-k}
   $$

   Evaluating the sum yields:

   $$
   I(U_0) \ge \sum_{k=1}^{\infty} 1 = \infty
   $$

4. **Contradiction:**
   An infinite information capacity $I(U_0) = \infty$ is excluded by the **Finite Information Substrate** <Ref id="1.3.5" label="§1.3.5" />.

**IV. Conclusion**

Both dynamical regimes necessitate an infinite information content in the present state $U_0$ given an infinite past. We conclude that the temporal domain is bounded by a finite origin.

Q.E.D.

**In Plain English:**  
Section 1.3.6.1 formalizes the properties of the QBD proof regarding backward accumulation.

---

### 1.3.7 Lemma: Finite State Recurrence {#1.3.7}

:::info[**Incompatibility of Infinite Past Duration due to Strictly Finite Configuration Spaces**]
:::

Given a universal configuration space $\Omega$ characterized by a strictly finite cardinality $|\Omega| = N < \infty$, let the historical trajectory be indexed by an unbounded sequence of non-positive temporal increments. Therefore, a state recurrence forming a closed causal loop arises, violating **Acyclic Effective Causality** <Ref id="2.7.1" label="§2.7.1" />.

**In Plain English:**  
Section 1.3.7 formalizes the properties of the QBD lemma regarding finite state recurrence.

---

### 1.3.7.1 Proof: Finite State Recurrence {#1.3.7.1}

:::tip[**Combinatorial Contradiction via the Dirichlet Pigeonhole Principle and Mathematical Induction**]
:::

**I. Boundary Conditions and State Space Setup**

Let $\Omega$ denote the universal configuration space of admissible states, whose finite cardinality is established in the **Finite Information Substrate** <Ref id="1.3.5" label="§1.3.5" />. Assume the cardinality of this state space is strictly finite:

$$
|\Omega| = N < \infty
$$

Let the global logical timeline be hypothesized as unbounded in the past direction, generating an infinite sequence of states $\mathcal{T}$ indexed by non-positive logical time integers in the **Global Logical Time** <Ref id="1.3.3" label="§1.3.3" /> poset:

$$
\mathcal{T = (\dots, U_{-2}, U_{-1}, U_0)}
$$

**II. Cardinality and Subsequence Mapping**

Consider a finite subsequence $\mathcal{T}_{\text{sub}}$ extracted from the historical trajectory $\mathcal{T}$ containing exactly $N + 1$ elements:

$$
\mathcal{T}_{\text{sub}} = (U_{-N}, \dots, U_0)
$$

Let $T = \{-N, \dots, 0\}$ denote the finite set of temporal indices enumerating this subsequence, establishing the cardinality constraint:

$$
|T| = N + 1
$$

Define the mapping $f: T \to \Omega$ by the state assignment evaluation:

$$
f(t) = U_t
$$

**III. Inductive Cycle Construction**

Comparing the domain cardinality $|T| = N + 1$ with the codomain cardinality $|\Omega| = N$ implies that the mapping $f$ cannot be injective. The Dirichlet Pigeonhole Principle establishes the existence of at least two distinct temporal indices $t_a, t_b \in T$ satisfying the strict ordering $t_a < t_b$ such that the associated states are identical:

$$
U_{t_a} = U_{t_b}
$$

Let $\mathcal{U}$ denote the deterministic evolution operator mapping each state snapshot to its unique successor, satisfying $U_{t+1} = \mathcal{U}(U_t)$. The topological identity of $U_{t_a}$ and $U_{t_b}$ yields the structural identity of their respective immediate consequences:

$$
\mathcal{U}(U_{t_a}) = \mathcal{U}(U_{t_b}) \implies U_{t_a+1} = U_{t_b+1}
$$

Mathematical induction establishes this state identity for all subsequent increments $k \in \mathbb{N}_0$, yielding the general recurrence translation:

$$
U_{t_a+k} = U_{t_b+k}
$$

The deterministic trajectory is thereby bound to enter a periodic closed cycle $C$ of length $P = t_b - t_a$:

$$
C = (U_{t_a}, U_{t_a+1}, \dots, U_{t_b-1})
$$

The return relation at the boundary maps the terminal cycle element directly back to the initial locus:

$$
U_{t_b-1} \to U_{t_b} \equiv U_{t_a}
$$

This recurrence establishes the following closed causal structure:

$$
U_{t_a} \to U_{t_a+1} \to \dots \to U_{t_b-1} \to U_{t_a}
$$

**IV. Formal Conclusion**

The formation of the periodic cycle $C$ establishes that state $U_{t_a}$ constitutes a causal ancestor of itself ($U_{t_a} \prec U_{t_a}$), establishing a transitive relation within the causal network. This localized self-influence is incompatible with the global property of irreflexivity mandated by the strict partial order of the timeline. We conclude that an infinite past trajectory within a strictly finite configuration space is incompatible with the structural requirements of **Acyclic Effective Causality** <Ref id="2.7.1" label="§2.7.1" />.

Q.E.D.

**In Plain English:**  
Section 1.3.7.1 formalizes the properties of the QBD proof regarding finite state recurrence.

---

### 1.3.8 Lemma: Supertask Impossibility {#1.3.8}

:::info[**Impossibility of Infinite Operation Sequences from Logical and Physical Non-Termination**]
:::

Given an infinite sequence of discrete computational steps required to generate a present state $U_0$, the execution of this sequence constitutes a **Supertask**. Therefore, the completion of this **Supertask** is physically excluded within the dynamical constraints of the theory, as the realization of $\aleph_0$ operations within a finite proper time interval implies a completed infinity, which is impermissible in a constructive ontology **Temporal Finitude** <Ref id="1.3.4" label="§1.3.4" />.

**In Plain English:**  
Section 1.3.8 formalizes the properties of the QBD lemma regarding supertask impossibility.

---

### 1.3.8.1 Proof: Supertask Impossibility {#1.3.8.1}

:::tip[**Order-Theoretic Non-Well-Foundedness through Thermodynamic Entropy Divergence Proof**]
:::

**I. Initial Conditions and History Definition**

Let $\mathcal{H}$ denote the ordered set of computational operations $\mathcal{U}_i$ required to generate the present state $U_0$ from a precedent state. Under the hypothesis of an infinite past, the index set of the **Global Logical Time** <Ref id="1.3.3" label="§1.3.3" /> is the negative integers, violating the well-foundedness required for physical causation outlined in **Temporal Finitude** <Ref id="1.3.4" label="§1.3.4" />:

$$
\mathcal{H} = \{ \dots, \mathcal{U}_{-3}, \mathcal{U}_{-2}, \mathcal{U}_{-1} \}
$$

This set possesses the order type $\omega^*$ (the order of the negative integers), which is characterized by having a last element $\mathcal{U}_{-1}$ but no first element.

**II. The Supertask Constraint**

For the state $U_0$ to be physically realized (to exist as the output of a computation), the entire sequence of operations in $\mathcal{H}$ must have been executed to completion. This implies the performance of a **Supertask**, defined as an infinite number of discrete steps completed within the timeline prior to $t=0$.

**III. Computational Non-Initialization Analysis**

Let $M = (S, \Sigma, \delta, s_0)$ denote a state machine modeling the physical universe, where $s_0$ is the initial state. A valid computational history mapping an execution trace must be isomorphic to a well-ordered set, establishing the requirement that every non-empty subset of events contains a $\le$-minimal element. Define a well-founded history as a configuration where every non-empty subset $X \subseteq \mathcal{H}$ contains a $\le$-minimal element $m$ such that $\nexists x \in X : x < m$. The infinite sequence $\mathcal{H}$ possesses the non-well-founded order type $\omega^*$ (the order of the negative integers), which lacks a minimal element because the subset $\mathcal{H}$ itself possesses no minimal element. For any computation to proceed, the machine must be initialized in state $s_0$ at some time $t_{start}$. In the sequence $\mathcal{H}$, for any hypothesized starting time $t_k$, there exists a prior operation $\mathcal{U}_{t_k-1}$ that was required to generate the input for $\mathcal{U}_{t_k}$:

$$
\forall k \in \mathbb{Z}, \quad \exists (k-1) \in \mathbb{Z} \quad \text{such that} \quad k-1 < k
$$

There is no time $t$ at which the machine $M$ could have been initialized. The initialization domain satisfies the intersection boundary:

$$
\text{Domain}(\mathcal{H}) \cap \{ t_{start} \} = \emptyset
$$

The absence of a valid initial state implies that a computation with no initial state is mathematically undefined.

**IV. Resource and Energy Divergence Analysis**

Let $\epsilon(op)$ denote the energy cost of a single logical operation. By Landauer's Principle and the Margolus-Levitin theorem, any state transition takes a non-zero amount of energy and time:

$$
\epsilon(op) \ge \epsilon_{min} > 0
$$

The total energy $E_{total}$ dissipated to reach state $U_0$ is the sum over the infinite history:

$$
E_{total} = \sum_{k \in \mathcal{H}} \epsilon(\mathcal{U}_k)
$$

We substitute the lower bound constraint into the summation to evaluate the total energy divergence:

$$
E_{total} \ge \sum_{k=1}^{\infty} \epsilon_{min} = \lim_{n \to \infty} (n \cdot \epsilon_{min}) = \infty
$$

An infinite energy dissipation implies that the universe must have exhausted all free energy (reached thermodynamic equilibrium) infinitely long ago. This unbounded dissipation implies that the accumulated entropy diverges to infinity ($S \to \infty$), satisfying the divergence expression:

$$
S(U_0) = \infty \quad \not\le \quad \mathcal{O}(t_L^2) < \infty
$$

However, the information content of any valid state step is bounded by the quadratic scaling function $S(U_t) \le \mathcal{O}(t^2)$ due to the holographic property of the substrate, as established by **Finite Information Substrate** <Ref id="1.3.5" label="§1.3.5" />. The divergence $S(U_0) = \infty$ establishes a contradiction with this extensive information bound, contradicting the existence of the low-entropy, ordered state $U_0$ observed at the present.

**V. Formal Conclusion**

We conclude that the joint requirements of structural well-foundedness and holographic information capacity limits exclude the completion of an unbounded historical sequence, establishing that the temporal domain possesses a finite origin.

Q.E.D.

**In Plain English:**  
Section 1.3.8.1 formalizes the properties of the QBD proof regarding supertask impossibility.

---

### 1.3.9 Proof: Temporal Finitude {#1.3.9}

:::tip[**Temporal Finitude** due to Entropy Limits <Ref id="1.3.4" label="§1.3.4" />]
:::

**I. The Infinite Hypothesis**
 Let it be assumed, for the explicit purpose of demonstrating a contradiction, that the domain of Global Logical Time $t_L$ is unbounded in the past direction. This assumption implies that the set of temporal indices is isomorphic to the non-positive integers ($T_L \cong \mathbb{Z}_{\le 0}$), thereby asserting the existence of an infinite sequence of distinct antecedent states $\{\dots, U_{-2}, U_{-1}, U_0\}$.
 
 **II. Information and Thermodynamic Constraints**
 The validity of this hypothesis is interrogated against the established information-theoretic lemmas of the theory:
 
 1.  **Finite Information Substrate** <Ref id="1.3.5" label="§1.3.5" />: The system enforces a strict holographic bound on the information content of any state within the sequence. It is established that $S(U_t)$ must remain finite for all finite $t$. The assumption of an infinite past requires the current state to encode a history of infinite depth, which necessitates an information capacity that exceeds this finite bound.
 2.  **Backward Accumulation** <Ref id="1.3.6" label="§1.3.6" />: Under the condition of irreversible dynamics, an infinite past necessitates an unbounded accumulation of entropy production ($\Sigma \Delta S \to \infty$). This accumulation would result in a present state $U_0$ characterized by maximal entropy (Thermodynamic Equilibrium or Heat Death), a condition that stands in direct contradiction to the observed low-entropy configuration of the physical universe.
 
 **III. Recurrence and Computability Constraints**
 The hypothesis is further constrained by topological and computational limits:
 
 1.  **Finite State Recurrence** <Ref id="1.3.7" label="§1.3.7" />: Under the condition of reversible dynamics within a state space of finite cardinality, an infinite temporal duration necessitates the occurrence of Poincaré recurrence ($U_t = U_{t+k}$). Such recurrence establishes closed causal loops, which constitute a direct violation of the **Acyclicity** axiom governing the causal graph.
 2.  **Supertask Impossibility** <Ref id="1.3.8" label="§1.3.8" />: The logical traversal of an infinite sequence of operations to arrive at the present state $U_0$ constitutes a Supertask. The completion of such a task is computationally undefined, as it lacks a valid initialization condition, rendering the existence of $U_0$ logically impossible under constructive dynamical rules.
 
 **IV. Convergence**
 The assumption of an unbounded past generates inescapable contradictions under both thermodynamic and computational constraints. Whether the dynamics are reversible or irreversible, the hypothesis fails to yield a consistent physical model.
 
 **V. Formal Conclusion**
 Consequently, the temporal domain cannot be unbounded. There must exist a unique initial state $U_0$ such that for all integers $t < 0$, the state $U_t$ is undefined. The domain of Global Logical Time is isomorphic to the set of non-negative integers $\mathbb{N}_0$, thereby establishing a definite and absolute moment of genesis.

Q.E.D.

**In Plain English:**  
Section 1.3.9 formalizes the properties of the QBD proof regarding temporal finitude.

---

### 1.4.1 Definition: Causal Graph Substrate {#1.4.1}

:::tip[**Mathematical Characterization of the Relational Configuration Space as a Formal Architecture**]
:::

Let $\Omega$ denote the universal configuration space of all valid states of the **Causal Graph Substrate**. A specific causal graph configuration is a triplet $G = (V, E, H)$ where:
1.  **Event Set**: $V$ is a finite set of vertices representing abstract events.
2.  **Causal Link Set**: $E \subseteq V \times V$ is a binary relation represented as a set of directed edges.
3.  **Timestamp Mapping**: $H: E \to \mathbb{N}$ is a mapping assigning a creation timestamp to each edge.

The graph $G$ must be a finite directed acyclic graph.

**In Plain English:**  
Causal Graph Substrate defines the universal configuration space of all valid states as finite directed graphs represented by the triplet (V, E, H).

---

### 1.4.2 Definition: Abstract Event {#1.4.2}

:::tip[**Formal Characterization of Event Vertices as Pre-Geometric Nodes**]
:::

Let $V = \{ v_1, v_2, \ldots, v_N \}$ be a finite set of vertices, where each element $v \in V$ is an **Abstract Event**. An abstract event is a structureless point representing the intersection of causal influences. It possesses no intrinsic coordinates, spatial volume, or physical attributes independent of its incidence relations within the edge set $E$.

**In Plain English:**  
Abstract Event defines the vertex set V where each element represents a structureless pre-geometric event whose identity is determined purely by relations.

---

### 1.4.3 Definition: Causal Relation {#1.4.3}

:::tip[**Formal Characterization of Causal Links as Directed Poset Edges**]
:::

Let $E \subseteq V \times V$ be a set of directed edges, where each ordered pair $e = (u, v) \in E$ is a **Causal Relation**. An edge $e$ represents an irreducible causal link denoting the direct, unmediated logical proposition that event $u$ precedes and causally influences event $v$. The relation is strictly asymmetric, satisfying:

$$
(u, v) \in E \implies (v, u) \notin E.
$$

**In Plain English:**  
Causal Relation defines the edge set E of directed links representing irreducible, asymmetric causal influence between events.

---

### 1.4.4 Definition: Creation Timestamp {#1.4.4}

:::tip[**Formal Characterization of the Historical Edge Timestamp Mapping as a Formal Architecture**]
:::

Let $H: E \to \mathbb{N}$ be a mapping that assigns to each edge $e \in E$ a **Creation Timestamp** $H(e) = t_L$, where $t_L$ is the global logical time of its creation. The mapping $H$ assigns a unique, immutable integer index to each edge upon its formation, establishing a discrete proper time step for relational connections.

**In Plain English:**  
Creation Timestamp defines the mapping H assigning to each edge a discrete, immutable creation index tracking its chronological order of genesis.

---

### 1.4.5 Theorem: Monotonicity of History {#1.4.5}

:::info[**Strict Monotonicity via Well-Foundedness of Causal Timestamp Sequences**]
:::

Let $G = (V, E, H)$ be a causal graph. For any newly created edge $e = (u, v)$, the timestamp assignment satisfies the local recurrence relation:

$$
H(e) = 1 + \max\left( \lbrace H(e') \mid e' = (w, u) \in E \rbrace \cup \lbrace0\rbrace \right)
$$

where the maximum is taken over all edges $e'$ incoming to the source vertex $u$. The timestamp function $H$ induces a well-founded partial order on $E$ and enforces that $G$ is a directed acyclic graph, preserving the forward arrow of logical time.

**In Plain English:**  
The Monotonicity of History Theorem states that the creation timestamp assignment mapping H induces a well-founded partial order, enforcing that the causal graph is a directed acyclic graph.

---

### 1.4.6 Lemma: Irreflexivity of Timestamps {#1.4.6}

:::info[**Unsatisfiability of Recursive Timestamp Assignment via Self-Loops**]
:::

Let $e_{self} = (u, u)$ be a self-loop incident to a vertex $u$ in a graph $G$. The recursive timestamp assignment $H(e_{self}) = 1 + \max \left( \{H(e') \mid e' \in \text{In}(u)\} \cup \{0\} \right)$ is inconsistent and admits no stable timestamp assignment.

**In Plain English:**  
The Irreflexivity of Timestamps Lemma proves that no self-loop can satisfy the recursive timestamp assignment, logically excluding closed timelike curves of zero radius.

---

### 1.4.6.1 Proof: Irreflexivity of Timestamps {#1.4.6.1}

:::tip[**Formal Stability Analysis via Self-Loop Timestamps**]
:::

**I. Pre-computation of the Source History**

Let the proposed self-loop $e_{self} = (u, u)$ be defined on the **Causal Graph Substrate** <Ref id="1.4.1" label="§1.4.1" />. Its calculated **Creation Timestamp** <Ref id="1.4.4" label="§1.4.4" /> is governed by the recurrence relation defined in the **Monotonicity of History** <Ref id="1.4.5" label="§1.4.5" />. Let the constructor function query the pre-existing history of vertex $u$.  Let $T_{max}$ represent the maximum timestamp among all pre-existing incoming edges:

$$
T_{max} = \max \left( \{ H(e') \mid e' \in \text{In}(u)_{\text{pre}} \} \cup \{0\} \right)
$$

The calculated timestamp for the proposed self-loop $e_{self} = (u, u)$ is:

$$
H(e_{self}) = T_{max} + 1
$$

**II. State Update and Post-Creation Evaluation**

Let the edge $e_{self}$ be added to the edge set, updating the set of incoming edges:

$$
\text{In}(u)_{\text{post}} = \text{In}(u)_{\text{pre}} \cup \{ e_{self} \}
$$

For the timestamp assignment to remain stable, the recursive rule must satisfy the inequality:

$$
H(e_{self}) > \max_{k \in \text{In}(u)_{\text{post}}} H(k)
$$

**III. Contradiction Derivation**

Since $e_{self} \in \text{In}(u)_{\text{post}}$, the maximum of the updated set includes $H(e_{self})$:

$$
\max_{k \in \text{In}(u)_{\text{post}}} H(k) = \max(T_{max}, H(e_{self}))
$$

By construction, $H(e_{self}) = T_{max} + 1$, yielding:

$$
\max_{k \in \text{In}(u)_{\text{post}}} H(k) = H(e_{self})
$$

Substituting this value back into the stability inequality results in:

$$
H(e_{self}) > H(e_{self})
$$

The inequality $x > x$ is false for all real numbers.  Therefore, no stable timestamp can be assigned to a self-loop, and the configuration is rejected by the constructor.

Q.E.D.

**In Plain English:**  
Section 1.4.6.1 formalizes the properties of the QBD proof regarding irreflexivity of timestamps.

---

### 1.4.7 Lemma: Transitive Causal Monotonicity {#1.4.7}

:::info[**Monotonic Timestamp Progression along Directed Causal Chains by Inductive Path Extension**]
:::

Let $\pi = (v_0, v_1, \dots, v_k)$ be a directed path in a causal graph $G$, where $e_i = (v_{i-1}, v_i) \in E$ for each $i \in \{1, \dots, k\}$. Then the sequence of edge timestamps $H(e_i)$ is strictly monotonically increasing:

$$
H(e_1) < H(e_2) < \dots < H(e_k).
$$

**In Plain English:**  
The Transitive Causal Monotonicity Lemma proves that timestamps along any causal path are strictly monotonically increasing, establishing a well-founded topological progression.

---

### 1.4.7.1 Proof: Transitive Causal Monotonicity {#1.4.7.1}

:::tip[**Inductive Demonstration via Strict Timestamp Increase**]
:::

**I. Inductive Base Case**
 
Let $e_1 = (v_0, v_1)$ and $e_2 = (v_1, v_2)$ be adjacent directed edges along the path $\pi$. By incidence definition, the edge $e_1$ terminates at vertex $v_1$, establishing the membership $e_1 \in \text{In}(v_1)$.
 
The creation timestamp $H(e_2)$ of the outgoing edge $e_2$ is assigned by the recursive relation governing edge creation (**Creation Timestamp** <Ref id="1.4.4" label="§1.4.4" />), satisfying the historical ordering (**Monotonicity of History** <Ref id="1.4.5" label="§1.4.5" />):
 
$$
H(e_2) = 1 + \max \left( \{ H(k) \mid k \in \text{In}(v_1) \} \cup \{0\} \right)
$$
 
The incidence condition $e_1 \in \text{In}(v_1)$ yields the bound on the maximum incoming timestamp:
 
$$
\max \left( \{ H(k) \mid k \in \text{In}(v_1) \} \right) \ge H(e_1)
$$
 
Evaluating the inequality yields:
 
$$
H(e_2) \ge 1 + H(e_1) > H(e_1)
$$
 
establishing the base inequality $H(e_1) < H(e_2)$.
 
**II. Inductive Hypothesis**
 
Assume that strict timestamp monotonicity holds for any directed subpath of length $n \ge 1$:
 
$$
H(e_1) < H(e_2) < \dots < H(e_n)
$$
 
where the terminal edge $e_n$ in this subpath terminates at vertex $v_n$.
 
**III. Inductive Step**
 
Consider the adjacent outgoing edge $e_{n+1} = (v_n, v_{n+1})$ originating at $v_n$. The incoming incidence $e_n \in \text{In}(v_n)$ yields the recursive assignment inequality for $H(e_{n+1})$:
 
$$
H(e_{n+1}) = 1 + \max \left( \{ H(k) \mid k \in \text{In}(v_n) \} \cup \{0\} \right) \ge 1 + H(e_n) > H(e_n)
$$
 
Applying this single-step inequality to the inductive hypothesis yields the strict monotonicity condition:
 
$$
H(e_1) < H(e_2) < \dots < H(e_n) < H(e_{n+1})
$$
 
establishing the extended monotonicity chain to path length $n+1$.
 
**IV. Transitive Conclusion**
 
We conclude that edge timestamps strictly increase monotonically along every directed causal path ($H(e_1) < H(e_2) < \dots < H(e_k)$), which establishes that $H(e_1) < H(e_k)$ for all $k \ge 2$ and induces a well-founded causal partial order on history.
 
Q.E.D.

**In Plain English:**  
Section 1.4.7.1 formalizes the properties of the QBD proof regarding transitive causal monotonicity.

---

### 1.4.8 Proof: Monotonicity of History {#1.4.8}

:::tip[**Synthesis of Irreflexivity via Transitivity to Establish Global Acyclicity**]
:::

**I. Assumption of a Causal Cycle**

Let $G = (V, E, H)$ be a causal graph, and assume $G$ contains a directed cycle $C = (v_0, v_1, \dots, v_k)$ of length $k \ge 1$ where $v_0 = v_k$.

**II. Evaluation of Cycle Categories**

1.  **Length $k=1$**: Under this condition, the cycle is a self-loop $e = (v_0, v_0)$. The recursive assignment admits no stable timestamp for a self-loop (**Irreflexivity of Timestamps** <Ref id="1.4.6" label="§1.4.6" />), establishing a contradiction.
2.  **Length $k \ge 2$**: Under this condition, the cycle forms a directed path from $v_0$ to $v_k$. The sequence of edge timestamps is strictly monotonically increasing (**Transitive Causal Monotonicity** <Ref id="1.4.7" label="§1.4.7" />), satisfying:

$$
H(e_1) < H(e_2) < \dots < H(e_k)
$$

which establishes the inequality $H(e_1) < H(e_k)$. The boundary identification $v_0 = v_k$ establishes that the terminal edge $e_k = (v_{k-1}, v_0)$ belongs to the incoming set $\text{In}(v_0)$. The recursive creation timestamp assignment for the initial outgoing edge $e_1 = (v_0, v_1)$ yields:

$$
H(e_1) = 1 + \max \left( \{ H(k) \mid k \in \text{In}(v_0) \} \cup \{0\} \right) \ge 1 + H(e_k) > H(e_k)
$$

Combining the inequality $H(e_1) > H(e_k)$ with the transitive inequality $H(e_1) < H(e_k)$ yields the contradiction:

$$
H(e_1) < H(e_1)
$$

**III. Conclusion**

Both cases establish a contradiction. Therefore, the assumption of a causal cycle is false, and the causal graph $G = (V, E, H)$ is a directed acyclic graph.

Q.E.D.

**In Plain English:**  
Section 1.4.8 formalizes the properties of the QBD proof regarding monotonicity of history.

---

### 1.5.1 Definition: Elementary Task Space {#1.5.1}

:::tip[**Mathematical Characterization of the Admissible Transformation Space as a Formal Architecture**]
:::

Let $\mathcal{G}$ denote the universe of all causal graphs $G = (V, E, H)$. The **Elementary Task Space** $\mathfrak{T}$ is the set of all graph transformations $T: G \to G'$ where $G' = (V', E', H')$ such that:
1.  **Acyclicity**: $G'$ is a directed acyclic graph.
2.  **Monotonicity of History**: The local sequence of timestamps $H'$ satisfies temporal monotonicity under any edge modification.
3.  **Finite Growth**: There exists a constant $k \in \mathbb{N}$ such that $|V'| \leq |V| + k$ and $|E'| \leq |E| + k$.

Formally:

$$
\mathfrak{T} = \lbrace T: \mathcal{G} \to \mathcal{G} \mid T(G) \text{ preserves acyclicity, monotonicity of } H, \text{ and finite growth} \rbrace.
$$

**In Plain English:**  
Elementary Task Space defines the set of all structurally possible graph transformations that preserve causality, timestamp monotonicity, and finite growth.

---

### 1.5.2 Definition: Edge Addition Task {#1.5.2}

:::tip[**Formal Specification of the Primitive Edge Insertion Operator via Edge Addition Task**]
:::

Let $G = (V, E, H)$ be a causal graph. For any pair of vertices $u, v \in V$ such that $u \neq v$ and $(u, v) \notin E$, the **Edge Addition Task** $\mathfrak{T}_{add}(u, v)$ is the mapping:

$$
\mathfrak{T}_{add}(u, v): G \mapsto G' = (V', E', H')
$$

where the target components are defined by:
1.  **Vertex Set**: $V' = V$.
2.  **Edge Set**: $E' = E \cup \{(u, v)\}$.
3.  **Timestamp Assignment**: $H'(e) = H(e)$ for all $e \in E$, and $H'(u, v) = t_L$, where $t_L$ is the emergent timestamp satisfying:

$$
t_L > \max \left( \{ H(x, y) \in E \mid y = u \lor y = v \} \cup \{ 0 \} \right).
$$

The operation is defined if and only if $G'$ is a directed acyclic graph.

**In Plain English:**  
Edge Addition Task defines the primitive operator that creates a directed causal link between two existing vertices with a new, monotonically increasing timestamp.

---

### 1.5.3 Definition: Edge Deletion Task {#1.5.3}

:::tip[**Formal Specification of the Primitive Edge Excision Operator via Edge Deletion Task**]
:::

Let $G = (V, E, H)$ be a causal graph. For any edge $e = (u, v) \in E$, the **Edge Deletion Task** $\mathfrak{T}_{del}(u, v)$ is the mapping:

$$
\mathfrak{T}_{del}(u, v): G \mapsto G' = (V', E', H')
$$

where the target components are defined by:
1.  **Vertex Set**: $V' = V$.
2.  **Edge Set**: $E' = E \setminus \{(u, v)\}$.
3.  **Timestamp Assignment**: $H'$ is the restriction of $H$ to $E'$, satisfying $H'(e') = H(e')$ for all $e' \in E'$.

**In Plain English:**  
Edge Deletion Task defines the primitive operator that removes an active directed causal link while preserving its historical timestamp in the sequence log.

---

### 1.5.4 Theorem: Vacuum Repertoire {#1.5.4}

:::info[**Sufficiency via Completeness of Primitive Edge Operators**]
:::

Let $\mathfrak{T}_{vac} = \{ \mathfrak{T}_{add}(u, v), \mathfrak{T}_{del}(u, v) \mid u, v \in V \}$ denote the set of primitive tasks. The fundamental mutability of any causal graph $G = (V, E, H)$ is exhaustively generated by the set of primitive tasks $\mathfrak{T}_{vac}$. These operations are mutually inverse, conserve state distinguishability, and dynamically govern the active vertex set $V$ purely through relational incidence.

**In Plain English:**  
The Vacuum Repertoire Theorem proves that edge addition and deletion are sufficient to generate all valid graph transitions, are mutually inverse, and conserve state distinguishability.

---

### 1.5.5 Lemma: Relational Vertex Emergence {#1.5.5}

:::info[**Subordination via Vertex Existence to Edge Topology**]
:::

Let $G = (V, E, H)$ be a causal graph, and let $V_{act} = \{ v \in V \mid \exists u \in V \text{ such that } (u, v) \in E \lor (v, u) \in E \}$ be the active vertex set. The creation or destruction of a vertex is strictly subordinate to edge operations, with no primitive task in $\mathfrak{T}_{vac}$ directly mutating the vertex set $V$.

**In Plain English:**  
The Relational Vertex Emergence Lemma states that vertices cannot be directly created or destroyed by primitive tasks; they emerge and vanish solely as endpoints of active relations.

---

### 1.5.5.1 Proof: Relational Vertex Emergence {#1.5.5.1}

:::tip[**Verification of Vertex Subordination through Primitive Operations**]
:::

**I. Definition of the Vertex Modification Operator**

Let $T \in \mathfrak{T}_{vac}$ be a primitive task. By **Edge Addition Task** <Ref id="1.5.2" label="§1.5.2" /> and **Edge Deletion Task** <Ref id="1.5.3" label="§1.5.3" />, the mapping $T: G \mapsto G'$ satisfies:

$$
V' = V
$$

for both $\mathfrak{T}_{add}(u, v)$ and $\mathfrak{T}_{del}(u, v)$.

**II. Relation to the Active Vertex Set**

Let the active vertex set $V_{act} \subseteq V$ be defined as the set of all vertices with non-zero degree:

$$
V_{act}(G) = \{ v \in V \mid \deg(v) > 0 \}
$$

where $\deg(v) = \deg_{in}(v) + \deg_{out}(v)$.

1.  **Addition case**: Let $T = \mathfrak{T}_{add}(u, v)$.  The edge set becomes $E' = E \cup \{(u, v)\}$.  The degrees of $u$ and $v$ increase by 1, while other degrees remain constant.  Thus, if $u, v \notin V_{act}(G)$, they transition to $V_{act}(G')$.  No vertex is added to $V$.
2.  **Deletion case**: Let $T = \mathfrak{T}_{del}(u, v)$.  The edge set becomes $E' = E \setminus \{(u, v)\}$.  The degrees of $u$ and $v$ decrease by 1.  If their degree becomes 0, they cease to be in $V_{act}(G')$.  No vertex is removed from $V$.

**III. Conclusion**

Since $V' = V$ under all primitive operators, the vertex set $V$ itself is invariant under $\mathfrak{T}_{vac}$.  All changes in active vertex status are strictly determined by edge incidence.

Q.E.D.

**In Plain English:**  
Section 1.5.5.1 formalizes the properties of the QBD proof regarding relational vertex emergence.

---

### 1.5.6 Lemma: Reversibility of Primitives {#1.5.6}

:::info[**Kinematic Reversibility via Edge Operations**]
:::

For all primitive tasks $T \in \mathfrak{T}_{vac}$ acting on a causal graph $G$, there exists a unique inverse primitive task $T^{-1} \in \mathfrak{T}_{vac}$ such that $T^{-1}(T(G)) = G$, conserving state distinguishability.

**In Plain English:**  
The Reversibility of Primitives Lemma proves that every primitive edge addition or deletion has a unique inverse operation, ensuring that the substrate's transitions are completely reversible.

---

### 1.5.6.1 Proof: Reversibility of Primitives {#1.5.6.1}

:::tip[**Verification of the Inverse Relations of Primitive Operators through Reversibility of Primitives**]
:::

**I. Evaluation of the Edge Addition Inverse**

Let $G = (V, E, H)$ be a causal graph, and let $T = \mathfrak{T}_{add}(u, v)$ be the **Edge Addition Task** <Ref id="1.5.2" label="§1.5.2" /> defined on $G$.  The resulting graph is $G' = (V, E \cup \{(u, v)\}, H')$, where $H'$ assigns $t_L$ to the new edge.

We apply the primitive task $T^{-1} = \mathfrak{T}_{del}(u, v)$ (the **Edge Deletion Task** <Ref id="1.5.3" label="§1.5.3" />) to $G'$:

1.  **Vertex Set**: $V'' = V' = V$.
2.  **Edge Set**: $E'' = E' \setminus \{(u, v)\} = (E \cup \{(u, v)\}) \setminus \{(u, v)\} = E$.
3.  **Timestamp Assignment**: $H''$ is the restriction of $H'$ to $E''$.  Since $E'' = E$, and $H'$ preserves $H$ on all edges in $E$, it follows that $H''(e) = H(e)$ for all $e \in E$.

Thus, $T^{-1}(T(G)) = G$.

**II. Evaluation of the Edge Deletion Inverse**

Let $G = (V, E, H)$ be a causal graph containing the edge $(u, v)$, and let $T = \mathfrak{T}_{del}(u, v)$ be defined on $G$.  The resulting graph is $G' = (V, E \setminus \{(u, v)\}, H')$.

We apply the primitive task $T^{-1} = \mathfrak{T}_{add}(u, v)$ with the historical timestamp $t_L = H(u, v)$:

1.  **Vertex Set**: $V'' = V' = V$.
2.  **Edge Set**: $E'' = E' \cup \{(u, v)\} = (E \setminus \{(u, v)\}) \cup \{(u, v)\} = E$.
3.  **Timestamp Assignment**: $H''$ assigns $H(u, v)$ to the restored edge.  Since the rest of the timestamps are unchanged, $H'' = H$.

Thus, $T^{-1}(T(G)) = G$.

**III. Conclusion**

Both operations possess unique inverses within the primitive set, demonstrating that state distinguishability is conserved across transitions.

Q.E.D.

**In Plain English:**  
Section 1.5.6.1 formalizes the properties of the QBD proof regarding reversibility of primitives.

---

### 1.5.7 Proof: Vacuum Repertoire {#1.5.7}

:::tip[**Completeness of the Primitive Operators via Vacuum Repertoire**]
:::

**I. Characterization of the Target Space**

Let $T: G \mapsto G'$ be any valid transformation in the Elementary Task Space $\mathfrak{T}$, where $G = (V, E, H)$ and $G' = (V', E', H')$.  By definition, the change in the edge set is finite, and the vertex set undergoes no independent modifications.

**II. Decomposition into Primitive Operations**

Let the symmetric difference of the edge sets be:

$$
\Delta E = E' \triangle E = (E' \setminus E) \cup (E \setminus E')
$$

Since both $E$ and $E'$ are finite, the cardinality $|\Delta E| = m$ is finite.  The elements of $\Delta E$ are ordered as a sequence of single-edge operations:

1.  For each edge $e_i \in E \setminus E'$: Apply the primitive task $\mathfrak{T}_{del}(e_i)$.
2.  For each edge $e_j \in E' \setminus E$: Apply the primitive task $\mathfrak{T}_{add}(e_j)$ with its assigned timestamp.

Let the sequence of operations be $T_1, T_2, \dots, T_m$.  Each intermediate graph $G_i$ preserves acyclicity by the definition of the path trajectory in the Task Space.

**III. Synthesis of Vertex Consistency**

By **Relational Vertex Emergence** <Ref id="1.5.5" label="§1.5.5" />, the vertex set is invariant under each primitive operation ($V_{i+1} = V_i$).  Thus:

$$
V' = V_m = V_{m-1} = \dots = V_0 = V
$$

which matches the requirement that all vertex transformations are subordinate to edge mutations.

**IV. Uniqueness and Reversibility**

By **Reversibility of Primitives** <Ref id="1.5.6" label="§1.5.6" />, each step $T_i$ possesses a unique inverse task $T_i^{-1}$.  Therefore, the entire sequence $T_m \circ \dots \circ T_1$ is invertible, preserving state distinguishability:

$$
(T_m \circ \dots \circ T_1)^{-1} = T_1^{-1} \circ \dots \circ T_m^{-1}
$$

This demonstrates that any admissible transformation in $\mathfrak{T}$ can be decomposed into, and is generated by, a finite sequence of primitive tasks from $\mathfrak{T}_{vac}$.

Q.E.D.

**In Plain English:**  
Section 1.5.7 formalizes the properties of the QBD proof regarding vacuum repertoire.

---

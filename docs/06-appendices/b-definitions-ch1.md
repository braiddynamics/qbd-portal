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

Let $U_0$ be the specified input of a forward trajectory of the Universal Evolution Operator $\mathcal U$. **Global Logical Time** $t_L\in\mathbb N_0$ indexes that trajectory by labeling the input zero and incrementing the index by one for every update.

$$
U_0 \xrightarrow{\mathcal U} U_1 \xrightarrow{\mathcal U} U_2
\xrightarrow{\mathcal U}\cdots\xrightarrow{\mathcal U}U_{t_L}.
$$

The indices have their usual strict total order, including when distinct ticks have the same active configuration.

**In Plain English:**

Logical time labels the specified initial snapshot zero and counts subsequent updates. The ordered indices distinguish observations even when adjacency repeats.

---

### 1.3.4 Theorem: Temporal Finitude {#1.3.4}

:::info[**Temporal Finitude via Finite Capacity of Distinguishable Histories**]
:::

Let the histories distinguished at observation admit an injective encoding into $M<\infty$ possible present states. Their cardinality is at most $M$, and the comb with distinct retained terminal alternatives and the full continuing binary prefix tree give, respectively,

$$
K\le M-1,\qquad K\le\lfloor\log_2 M\rfloor.
$$

These are tick bounds when $K$ bounds the number of past ticks.

**In Plain English:**  
A finite state space bounds the number of histories that can be recovered from it. A time bound additionally depends on how the histories branch.

---

### 1.3.5 Lemma: Finite Information Substrate {#1.3.5}

:::info[**Finite Information Substrate via Entropy of Finite Update Choices**]
:::

Let $A_t$ and $C_t$ count binary addition trials and old triangles with at most four deletion outcomes each in a frozen snapshot. The conditional realization entropy is at most $A_t+2C_t$ bits, and under fixed initialization, uniform degree, one trial per candidate edge and at most linear vertex growth, both the accumulated conditional choice entropy and induced graph trajectory entropy are $O(T^2)$ through $T$ ticks.

**In Plain English:**  
The number of choices in a frozen tick bounds its conditional Shannon entropy. With bounded degree and at most linear vertex growth, the cumulative bound is quadratic in the tick count.

---

### 1.3.5.1 Proof: Finite Information Substrate {#1.3.5.1}

:::tip[**Finite Information Substrate via Support Counting and the Entropy Chain Rule**]
:::

**I. Single-Tick Support**

The frozen tick supplies the choice list and deterministic successor (**Finite Information Substrate** <Ref id="1.3.5" label="§1.3.5" />) (**Evolution Operator** <Ref id="4.6.1" label="§4.6.1" />).

Let $\Xi_t$ denote the realization and fix the input snapshot $G_t=g$. Its choices occupy at most $2^{A_t(g)}4^{C_t(g)}$ outcomes. The entropy of a law on $n$ outcomes is at most $\log_2 n$. Thus

$$
H(\Xi_t\mid G_t=g)\le\log_2(2^{A_t(g)}4^{C_t(g)})=A_t(g)+2C_t(g).
$$

**II. Counting with a Degree Bound**

Let $N_t\le a+bt$ and let $\Delta$ bound the total degree. The number of directed two-paths through a vertex is at most $\Delta^2$. Each candidate and each triangle have a supporting two-path, with distinct candidates and distinct triangles separately giving distinct paths. Hence

$$
A_t\le N_t\Delta^2,\qquad C_t\le N_t\Delta^2,\qquad A_t+2C_t\le3\Delta^2(a+bt).
$$

**III. Accumulated Entropy**

For fixed $G_0$, a realization prefix determines its final snapshot, and the full realization list determines the graph trajectory. Applying the support bound after fixing each prefix gives

$$
\begin{aligned}
H(G_1,\ldots,G_T)
&\le H(\Xi_0,\ldots,\Xi_{T-1})\\
&=\sum_{t=0}^{T-1}H(\Xi_t\mid\Xi_0,\ldots,\Xi_{t-1})\\
&\le3\Delta^2\sum_{t=0}^{T-1}(a+bt)
=3\Delta^2\bigl(aT+bT(T-1)/2\bigr).
\end{aligned}
$$

Q.E.D.

**In Plain English:**  
Section 1.3.5.1 formalizes the properties of the QBD proof regarding finite information substrate.

---

### 1.3.6 Lemma: Backward Accumulation {#1.3.6}

:::info[**Backward Accumulation via Occurrence Accumulation and Conditional Entropy**]
:::

Let $\mathcal E_t$ be the cumulative occurrence set through tick $t$, initially finite. Across $K$ ticks each with a new record its cardinality increases by at least $K$, and if the trajectory's finite conditional entropy at each counted tick is at least $\epsilon>0$, its joint trajectory entropy increases by at least $\epsilon K$ bits.

**In Plain English:**  
Section 1.3.6 formalizes the properties of the QBD lemma regarding backward accumulation.

---

### 1.3.6.1 Proof: Backward Accumulation {#1.3.6.1}

:::tip[**Backward Accumulation via Disjoint Increments and Conditional Entropy**]
:::

**I. Domain and Objects**

Creation occurrences are retained in the historical record (**Backward Accumulation** <Ref id="1.3.6" label="§1.3.6" />) (**Monotonicity of History** <Ref id="1.4.5" label="§1.4.5" />).

**II. Occurrence Counting**

Put $B_t=\mathcal E_{t+1}\setminus\mathcal E_t$. For $s<t$, $B_s\subseteq\mathcal E_t$ and $B_t\cap\mathcal E_t=\varnothing$. Thus for an interval $[a,b]$,

$$
\mathcal E_b=\mathcal E_a\sqcup\bigsqcup_{t=a}^{b-1}B_t,\qquad
|\mathcal E_b|-|\mathcal E_a|=\sum_{t=a}^{b-1}|B_t|\ge K.
$$

**III. Entropy Summation**

For trajectory variables $X_a,\ldots,X_b$ and the specified set $J$ of $K$ ticks, nonnegativity of conditional entropy gives

$$
\begin{aligned}
H(X_a,\ldots,X_b)-H(X_a)
&=\sum_{t=a}^{b-1}H(X_{t+1}\mid X_a,\ldots,X_t)\\
&\ge \sum_{t\in J}H(X_{t+1}\mid X_a,\ldots,X_t)\ge \epsilon K.
\end{aligned}
$$

Q.E.D.

**In Plain English:**  
Section 1.3.6.1 formalizes the properties of the QBD proof regarding backward accumulation.

---

### 1.3.7 Lemma: Finite State Recurrence {#1.3.7}

:::info[**Finite State Recurrence via Recurrence of Directed Adjacency**]
:::

Let $V$ be a fixed finite vertex set of size $N$ and $E_t$ the loop-free directed adjacency. Among $2^{N(N-1)}+1$ observations there are two with equal adjacency, and their cumulative occurrence sets differ if a record is added between the two snapshots.

**In Plain English:**  
Section 1.3.7 formalizes the properties of the QBD lemma regarding finite state recurrence.

---

### 1.3.7.1 Proof: Finite State Recurrence {#1.3.7.1}

:::tip[**Finite State Recurrence via Pigeonhole Counting on the Adjacency Projection**]
:::

**I. Domain and Objects**

The active snapshot has a directed adjacency field (**Finite State Recurrence** <Ref id="1.3.7" label="§1.3.7" />) (**Causal Graph Substrate** <Ref id="1.4.1" label="§1.4.1" />).

**II. Finite Projection**

The directed pair domain $P=\{(u,v)\in V^2:u\ne v\}$ has size $N(N-1)$. Each $E_t\subseteq P$, so the adjacency map takes at most $2^{N(N-1)}$ values. For $2^{N(N-1)}+1$ observation ticks this gives $E_s=E_t$ for some $s<t$.

**III. Historical Records**

If occurrence $\omega$ is recorded between the snapshots, then

$$
\omega\notin\mathcal E_s,\qquad \omega\in\mathcal E_t,\qquad
\mathcal E_s\subsetneq\mathcal E_t .
$$

Q.E.D.

**In Plain English:**

Section 1.3.7.1 formalizes the properties of the QBD proof regarding finite state recurrence.

---

### 1.3.8 Lemma: Supertask Impossibility {#1.3.8}

:::info[**Supertask Impossibility via Bound on Sequential Execution in Finite Duration**]
:::

Let sequential steps have nonoverlapping physical durations of at least $\tau_0>0$. The number of complete steps in a physical interval of length $T_{\mathrm{phys}}$ is bounded by $\lfloor T_{\mathrm{phys}}/\tau_0\rfloor$.

**In Plain English:**

Section 1.3.8 formalizes the properties of the QBD lemma regarding supertask impossibility.

---

### 1.3.8.1 Proof: Supertask Impossibility {#1.3.8.1}

:::tip[**Supertask Impossibility via Summation of Minimum Step Durations**]
:::

**I. Domain and Objects**

Logical steps are the sequentially indexed updates (**Supertask Impossibility** <Ref id="1.3.8" label="§1.3.8" />) (**Global Logical Time** <Ref id="1.3.3" label="§1.3.3" />).

**II. Disjoint Step Intervals**

For $m$ complete steps with physical intervals $[a_i,b_i]$, sequentiality gives $b_i\le a_{i+1}$. Thus

$$
m\tau_0\le\sum_{i=1}^m(b_i-a_i)\le T_{\mathrm{phys}} .
$$

**III. Integer Bound**

Dividing by $\tau_0$ and taking the integer floor gives $m\le\lfloor T_{\mathrm{phys}}/\tau_0\rfloor$. An infinite execution inside the interval would contain a finite subset exceeding that bound.

Q.E.D.

**In Plain English:**  
Section 1.3.8.1 formalizes the properties of the QBD proof regarding supertask impossibility.

---

### 1.3.9 Lemma: Finite Capacity of History Encodings {#1.3.9}

:::info[**Finite Capacity of History Encodings via Injective Encoding of Occurrence Histories**]
:::

Let $f:\mathcal H\to S$ inject a family of distinguishable histories into a finite set of $M$ states, so $|\mathcal H|\le M$. For a comb with its $K$ terminating alternatives and final continuing history included in $\mathcal H$, and for a binary continuing-prefix tree with all depth-$K$ histories included in $\mathcal H$, the respective bounds are

$$
K+1\le M,\qquad 2^K\le M.
$$

**In Plain English:**

Section 1.3.9 formalizes the properties of the QBD lemma regarding finite capacity of history encodings.

---

### 1.3.9.1 Proof: Finite Capacity of History Encodings {#1.3.9.1}

:::tip[**Finite Capacity of History Encodings via Pigeonhole Counting and Prefix Induction**]
:::

**I. Encoding**

The histories counted here are distinct records of occurrences (**Finite Capacity of History Encodings** <Ref id="1.3.9" label="§1.3.9" />) (**Backward Accumulation** <Ref id="1.3.6" label="§1.3.6" />).

The image is a subset of the state set, so $|\mathcal H|=|f(\mathcal H)|\le |S|=M$.

**II. Comb**

Two alternatives that terminate at different branch points differ at the earlier point, where one continues and the other terminates. The final continuing history also differs from every terminated alternative at its branch point. Hence $K+1\le|\mathcal H|\le M$.

**III. Full Continuing Branches**

Let $n_j$ count depth-$j$ continuing prefixes. There is one root. Each prefix contributes at least two children with distinct parent histories, so

$$
n_0=1,\qquad n_{j+1}\ge2n_j,\qquad n_j\ge2^j\quad (0\le j\le K)
$$

by induction. Thus $2^K\le n_K\le|\mathcal H|\le M$.

Q.E.D.

**In Plain English:**

Section 1.3.9.1 formalizes the properties of the QBD proof regarding finite capacity of history encodings.

---

### 1.3.10 Proof: Temporal Finitude {#1.3.10}

:::tip[**Temporal Finitude via Assembly of Conditional History Bounds**]
:::

**I. Identification of the Count**

A finite choice list has bounded conditional entropy (**Finite Information Substrate** <Ref id="1.3.5" label="§1.3.5" />). A new creation grows the occurrence set (**Backward Accumulation** <Ref id="1.3.6" label="§1.3.6" />). A repeated adjacency can occur at distinct snapshots (**Finite State Recurrence** <Ref id="1.3.7" label="§1.3.7" />). The encoding premise applies to the specified histories.

**II. Branch Depth**

The two counting cases give (**Finite Capacity of History Encodings** <Ref id="1.3.9" label="§1.3.9" />)

$$
K+1\le M\ \Longrightarrow\ K\le M-1,\qquad
2^K\le M\ \Longrightarrow\ K\le\lfloor\log_2 M\rfloor .
$$

If unbounded candidate past length forces unbounded $K$, the uniform bound on $K$ excludes unbounded candidate past length.

**III. Physical Execution**

For an execution of $L$ complete sequential steps in a finite physical interval the separate duration premise gives (**Supertask Impossibility** <Ref id="1.3.8" label="§1.3.8" />)

$$
L\tau_0\le T_{\mathrm{phys}}.
$$

Q.E.D.

**In Plain English:**

Section 1.3.10 formalizes the properties of the QBD proof regarding temporal finitude.

---

### 1.4.1 Definition: Causal Graph Substrate {#1.4.1}

:::tip[**Mathematical Characterization of the Relational Configuration Space as a Formal Architecture**]
:::

Let the **Causal Graph Substrate** at logical tick $t$ be the active spatial configuration $G_t=(V,E_t,H_t)$, where $V$ is a fixed finite vertex set, $E_t\subseteq V\times V$ is irreflexive and asymmetric, and $H_t:E_t\to\mathbb N_0$ records immutable causal heights of the active edge occurrences. Directed spatial cycles are permitted; the chronological order belongs to the distinct creation-event structure.

A creation occurrence is a record $\omega=(u,v,b,h)$ with birth tick $b\in\mathbb N_0$ and causal height $h\in\mathbb N_0$. At most one occurrence of a given ordered pair is created per tick. The active-occurrence map $\alpha_t:E_t\to\mathcal E_t$ identifies the current record and satisfies $H_t(u,v)=h(\alpha_t(u,v))$. The cumulative creation record $\mathcal E_t$ retains past occurrences after active deletion (**Historical Category** <Ref id="4.1.2" label="§4.1.2" />).

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

Let the **Creation Timestamp** $H_t(e)$ denote the causal height of the active occurrence of $e$, distinct from its scheduler birth tick $b(e)$. For a new edge $e=(u,v)$ inserted during the transition from tick $t$ to tick $t+1$, its height is

$$
h_{\mathrm{new}}(u,v)=1+\max\bigl(\{H_t(x,u):(x,u)\in E_t\}\cup\{0\}\bigr),
\qquad \omega=(u,v,t+1,h_{\mathrm{new}}(u,v)).
$$

Existing occurrences retain their assigned heights. The initial substrate has $H_0(e)=0$. A deleted pair recreated later receives a new occurrence identifier even if its newly computed height equals an earlier height. The birth tick and height are both immutable coordinates of an occurrence; neither is a replacement for the other.

**In Plain English:**  
Creation Timestamp defines the mapping H assigning to each edge a discrete, immutable creation index tracking its chronological order of genesis.

---

### 1.4.5 Theorem: Monotonicity of History {#1.4.5}

:::info[**Strict Monotonicity via Well-Foundedness of Causal Timestamp Sequences**]
:::

Let creation heights satisfy the source-side recurrence and let $\omega\mathrel D\eta$ mean that the edge occurrence $\omega$ is an incoming edge of the source of $\eta$ in the snapshot used to create $\eta$. Then $D^+$ is an irreflexive transitive relation on creation occurrences and every $D$-chain has strictly increasing heights; active spatial walks need not have increasing heights (**Creation Timestamp** <Ref id="1.4.4" label="§1.4.4" />).

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

**I. Fixed-Point Equation for a Self-Loop**

Let $e_*=(u,u)$ and suppose a stable timestamp $h=H(e_*)\in\mathbb N_0$ satisfies the stated recurrence (**Irreflexivity of Timestamps** <Ref id="1.4.6" label="§1.4.6" />). Put

$$
A=\{H(e'):e'\in\operatorname{In}(u)\}\cup\{0\},\qquad
m=\max A,\qquad h=1+m
$$

with the timestamp rule fixed above (**Creation Timestamp** <Ref id="1.4.4" label="§1.4.4" />). The self-loop is incoming to $u$, because its target is $u$:

$$
e_*=(u,u)\in\operatorname{In}(u)\quad\Longrightarrow\quad h\in A.
$$

**II. Maximum Bound and Contradiction**

Membership in $A$ gives $h\le m$. Substituting $m=h-1$ from the recurrence gives

$$
h\le m=h-1\quad\Longrightarrow\quad 0\le-1,
$$

which is false. Equivalently,

$$
h=1+m\ge1+h\quad\Longrightarrow\quad h-h\ge1\quad\Longrightarrow\quad0\ge1.
$$

The contradiction applies to every candidate finite value $h$.

**III. Pre-Insertion Value and Re-Evaluation**

Let $m_0$ be the maximum on the incoming edges before insertion. A provisional assignment $h_0=m_0+1$ gives the new incoming maximum

$$
m_1=\max\{m_0,h_0\}=h_0,
$$

because $h_0>m_0$. Re-evaluation of the same recurrence then requires

$$
h_1=1+m_1=h_0+1\ne h_0.
$$

More generally, if $h_j=m_0+j+1$, then

$$
\max\{m_0,h_j\}=h_j,\qquad h_{j+1}=1+h_j=m_0+(j+1)+1.
$$

Thus no finite provisional value is a fixed point:

$$
\boxed{e_*\in\operatorname{In}(u)\ \Longrightarrow\
\nexists h\in\mathbb N_0:\ h=1+\max\bigl(\{H(e'):e'\in\operatorname{In}(u),\ e'\ne e_*\}\cup\{0,h\}\bigr).}
$$

Q.E.D.

**In Plain English:**  
Section 1.4.6.1 formalizes the properties of the QBD proof regarding irreflexivity of timestamps.

---

### 1.4.7 Lemma: Transitive Causal Monotonicity {#1.4.7}

:::info[**Monotonic Timestamp Progression along Directed Causal Chains by Inductive Path Extension**]
:::

Let $e_1,\ldots,e_k$ be a sequentially instantiated causal chain whose occurrence of $e_i$ remains incoming to the source when $e_{i+1}$ is created, for each $i<k$. Then $H(e_1)<\cdots<H(e_k)$, and for $k\ge2$ the endpoint bound is $H(e_k)\ge H(e_1)+k-1$ (**Creation Timestamp** <Ref id="1.4.4" label="§1.4.4" />).

**In Plain English:**  
The Transitive Causal Monotonicity Lemma proves that timestamps along any causal path are strictly monotonically increasing, establishing a well-founded topological progression.

---

### 1.4.7.1 Proof: Transitive Causal Monotonicity {#1.4.7.1}

:::tip[**Inductive Demonstration via Strict Timestamp Increase**]
:::

**I. Predecessor Membership at Creation**

Let $\omega_i$ be the occurrence of $e_i$ and put $h_i=h(\omega_i)$. The sequential-chain hypothesis means that, when $e_{i+1}$ is created from a snapshot $G_{t_i}$, its source is the target of $e_i$ and $e_i$ is still present there. Consequently

$$
h_i\in\{H_{t_i}(x,s(e_{i+1})):(x,s(e_{i+1}))\in E_{t_i}\}.
$$

**II. Consecutive Inequality**

The source-side recurrence (**Creation Timestamp** <Ref id="1.4.4" label="§1.4.4" />) therefore gives

$$
\begin{aligned}
h_{i+1}
&=1+\max\bigl(\{H_{t_i}(x,s(e_{i+1}))\}\cup\{0\}\bigr)\\
&\ge1+h_i>h_i.
\end{aligned}
$$

Here the set in the maximum ranges over the incoming edges of that source in the creation snapshot. Both the membership and the maximum refer to that same snapshot.

**III. Induction on the Chain**

For $j=1$, $h_j=h_1=h_1+j-1$. If $h_j\ge h_1+j-1$, then

$$
h_{j+1}\ge h_j+1\ge h_1+j=h_1+(j+1)-1.
$$

Induction proves $h_j\ge h_1+j-1$ for all $j\le k$. The consecutive strict inequalities concatenate by transitivity of the natural-number order. This establishes the sequential-chain claim (**Transitive Causal Monotonicity** <Ref id="1.4.7" label="§1.4.7" />).

**IV. Conclusion**

$$
\boxed{h_1<\cdots<h_k,\qquad h_k\ge h_1+k-1.}
$$

Q.E.D.

**In Plain English:**  
Section 1.4.7.1 formalizes the properties of the QBD proof regarding transitive causal monotonicity.

---

### 1.4.8 Proof: Monotonicity of History {#1.4.8}

:::tip[**Synthesis of Irreflexivity via Transitivity to Establish Global Acyclicity**]
:::

**I. Direct Event Dependencies**

Let $\omega D\eta$ be a dependency with the stipulated creation-snapshot meaning (**Monotonicity of History** <Ref id="1.4.5" label="§1.4.5" />). The preceding incoming occurrence belongs to the creation snapshot of $\eta$. The source-side maximum therefore gives

$$
\omega D\eta\ \Longrightarrow\ h(\eta)\ge h(\omega)+1.
$$

Stable self-loop assignment also has the independent obstruction $h\ge h+1$ (**Irreflexivity of Timestamps** <Ref id="1.4.6" label="§1.4.6" />). Physical self-loops are excluded directly by the irreflexive edge constraint.

**II. Finite Dependency Paths**

A witness for $\omega D^+\eta$ is a chain $\omega=\omega_0D\omega_1D\cdots D\omega_m=\eta$ with $m\ge1$. The sequential inequality (**Transitive Causal Monotonicity** <Ref id="1.4.7" label="§1.4.7" />) gives

$$
h(\eta)\ge h(\omega)+m>h(\omega).
$$

**III. Irreflexivity and Transitivity**

If $\omega D^+\omega$, the endpoint inequality becomes $h(\omega)>h(\omega)$, a contradiction. If $\omega D^+\eta$ and $\eta D^+\zeta$, concatenation of the two finite dependency chains is a nonempty dependency chain from $\omega$ to $\zeta$. Thus

$$
\neg(\omega D^+\omega),\qquad
(\omega D^+\eta\land\eta D^+\zeta)\Longrightarrow\omega D^+\zeta.
$$

**IV. Well-Founded Height Descent**

A reversed dependency chain $\omega_{j+1}D^+\omega_j$ satisfies $h(\omega_{j+1})\le h(\omega_j)-1$. Induction gives $h(\omega_j)+j\le h(\omega_0)$. Taking $j=h(\omega_0)+1$ contradicts nonnegativity. Therefore no infinite descending dependency chain exists, and $D^+$ is a well-founded strict partial order on creation occurrences.

Q.E.D.

**In Plain English:**  
Section 1.4.8 formalizes the properties of the QBD proof regarding monotonicity of history.

---

### 1.5.1 Definition: Elementary Task Space {#1.5.1}

:::tip[**Mathematical Characterization of the Admissible Transformation Space as a Formal Architecture**]
:::

Let the **Elementary Task Space** $\mathfrak T(G)$ consist of guarded additions and deletions on a fixed spatial vertex set $V$. An addition changes one absent directed pair to present, preserves irreflexivity and asymmetry, assigns the source-side causal height, and satisfies the applicable candidate-relative PUC and causal-admission predicates; a deletion removes one present edge without erasing its historical occurrence (**Creation Timestamp** <Ref id="1.4.4" label="§1.4.4" />). The uniqueness predicate is candidate-relative (**Principle of Unique Causality (PUC)** <Ref id="2.3.4" label="§2.3.4" />).

Each primitive preserves $V$, changes at most one active edge, and leaves all surviving occurrence heights unchanged. Spatial triangle creation is permitted. The event dependency order, rather than all active spatial adjacency, is the chronological structure. A fixed-snapshot parallel merge and a sequential re-evaluation of guards are different task schedules.

**In Plain English:**  
Elementary Task Space defines the set of all structurally possible graph transformations that preserve causality, timestamp monotonicity, and finite growth.

---

### 1.5.2 Definition: Edge Addition Task {#1.5.2}

:::tip[**Formal Specification of the Primitive Edge Insertion Operator via Edge Addition Task**]
:::

Let the **Edge Addition Task** $\mathfrak T_{add}(u,v)$ act on $G_t=(V,E_t,H_t)$ for an absent pair $(u,v)$ with $u\ne v$ and $(v,u)\notin E_t$. Its admitted candidate includes the required geometric and causal guard evidence. The updated components are

$$
V'=V,\qquad E'=E_t\cup\{(u,v)\},\qquad
H'|_{E_t}=H_t,\qquad
H'(u,v)=1+\max\bigl(\{H_t(x,u):(x,u)\in E_t\}\cup\{0\}\bigr).
$$

The transition from tick $t$ records the new occurrence $(u,v,t+1,H'(u,v))$. For a return chord across $v\to w\to u$, PUC is evaluated relative to that candidate (**Principle of Unique Causality (PUC)** <Ref id="2.3.4" label="§2.3.4" />). Passing PUC is one guard, not an assertion that every other guard holds. The target spatial graph can contain the newly closed triangle.

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

:::info[**Vacuum Repertoire via Finite Composition and Recorded Rollback of Edge Tasks**]
:::

Let $\mathfrak T$ be the space of tasks witnessed by finite admissible sequences of guarded edge additions and deletions on a fixed vertex set $V$. Each task is a finite composition of the primitives, with active incidence determined by the edge set and rollback of each active update specified by the edited pair and its previous height.

**In Plain English:**  
A finite admissible task is composed of primitive edge updates. A record of the edited pair and height enables rollback on the active snapshot.

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

**I. Primitive State Components**

Let $G=(V,E,H)$ and $e=(u,v)$ with $u\ne v$. The two primitive definitions give

$$
\begin{array}{c|c|c}
\text{primitive}&V'&E'\\\hline
\mathfrak T_{add}(u,v)&V&E\cup\{e\}\\
\mathfrak T_{del}(u,v)&V&E\setminus\{e\}
\end{array}
$$

(**Edge Addition Task** <Ref id="1.5.2" label="§1.5.2" />), (**Edge Deletion Task** <Ref id="1.5.3" label="§1.5.3" />). Hence $V'=V$ in both cases.

**II. Incidence Change Under Addition**

Define $d_G(x)=d_{in,G}(x)+d_{\mathrm{out},G}(x)$ and $V_{act}(G)=\{x:d_G(x)>0\}$. For a legal addition, $e\notin E$, so

$$
\begin{aligned}
d_{\mathrm{out},G'}(x)&=d_{\mathrm{out},G}(x)+\mathbf1_{\{u\}}(x),\\
d_{in,G'}(x)&=d_{in,G}(x)+\mathbf1_{\{v\}}(x),\\
d_{G'}(x)&=d_G(x)+\mathbf1_{\{u\}}(x)+\mathbf1_{\{v\}}(x).
\end{aligned}
$$

Every previously positive degree remains positive. Each endpoint gains one, and every other degree is unchanged. Therefore

$$
V_{act}(G')=V_{act}(G)\cup\{u,v\}.
$$

The formula allows either endpoint already to be active; set union adds no duplicate element.

**III. Incidence Change Under Deletion**

For a legal deletion, $e\in E$, so both endpoints have degree at least one. The corresponding equations are

$$
\begin{aligned}
d_{\mathrm{out},G'}(x)&=d_{\mathrm{out},G}(x)-\mathbf1_{\{u\}}(x),\\
d_{in,G'}(x)&=d_{in,G}(x)-\mathbf1_{\{v\}}(x),\\
d_{G'}(x)&=d_G(x)-\mathbf1_{\{u\}}(x)-\mathbf1_{\{v\}}(x).
\end{aligned}
$$

Since $u\ne v$, each endpoint loses exactly one. An endpoint leaves the active set exactly when its old total degree was one:

$$
V_{act}(G')=V_{act}(G)\setminus
\{x\in\{u,v\}:d_G(x)=1\}.
$$

**IV. Finite Primitive Sequences**

For $G_{j+1}=T_j(G_j)$ with $T_j\in\mathfrak T_{vac}$, the base equality is $V(G_0)=V$. The single-step identity gives

$$
V(G_j)=V\quad\Longrightarrow\quad
V(G_{j+1})=V(G_j)=V.
$$

Induction establishes $V(G_m)=V$ for every finite $m$. The active set is recalculated from the displayed incidence equations at each step, which proves the stated subordination (**Relational Vertex Emergence** <Ref id="1.5.5" label="§1.5.5" />).

$$
\boxed{V(G_m)=V(G_0),\qquad
V_{act}(G_j)=\{x\in V:d_{G_j}(x)>0\}.}
$$

Q.E.D.

**In Plain English:**  
Section 1.5.5.1 formalizes the properties of the QBD proof regarding relational vertex emergence.

---

### 1.5.6 Lemma: Reversibility of Primitives {#1.5.6}

:::info[**Reversibility of Primitives via Partial Inverses on Active Adjacency and Heights**]
:::

Let a snapshot have adjacency $E(x)\in\{0,1\}$ and height $H(x)\in\mathbb N$ at every directed pair $x$, with height zero when absent. Both fields are restored by adding an absent pair and then deleting it, or by deleting an active pair and then restoring it at its saved height.

**In Plain English:**  
Deleting a newly added edge restores an absent pair. A deleted active pair can be restored at its saved height.

---

### 1.5.6.1 Proof: Reversibility of Primitives {#1.5.6.1}

:::tip[**Reversibility of Primitives via Pointwise Inversion of Edge Updates**]
:::

**I. Single-Pair Updates**

The height field belongs to the active edge snapshot (**Reversibility of Primitives** <Ref id="1.5.6" label="§1.5.6" />) (**Creation Timestamp** <Ref id="1.4.4" label="§1.4.4" />).

Write $A_{e,h}$ for setting $(E(e),H(e))=(1,h)$ and $D_e$ for setting $(E(e),H(e))=(0,0)$. Both operations preserve $(E(x),H(x))$ for every $x\ne e$.

**II. Rollback of Addition**

At an absent $e$, the forward and backward updates are

$$
(0,0)\xrightarrow{A_{e,h}}(1,h)\xrightarrow{D_e}(0,0).
$$

At all other pairs both operations preserve both fields. Hence $D_e(A_{e,h}(G))=G$ on the active snapshot.

**III. Rollback of Deletion**

At an active $e$, save $h=H_G(e)$. The two updates at $e$ are

$$
(1,h)\xrightarrow{D_e}(0,0)\xrightarrow{A_{e,h}}(1,h).
$$

Again the other pairs are unchanged, so $A_{e,h}(D_e(G))=G$ on the active snapshot.

Q.E.D.

**In Plain English:**  
Section 1.5.6.1 formalizes the properties of the QBD proof regarding reversibility of primitives.

---

### 1.5.7 Proof: Vacuum Repertoire {#1.5.7}

:::tip[**Vacuum Repertoire via Composition of Pointwise Rollbacks**]
:::

**I. Domain and Objects**

A task in the space specifies an admissible trajectory of active snapshots (**Vacuum Repertoire** <Ref id="1.5.4" label="§1.5.4" />) (**Elementary Task Space** <Ref id="1.5.1" label="§1.5.1" />).

**II. Finite Task Composition**

An admissible task has a witness sequence $G_0\xrightarrow{T_1}G_1\to\cdots\xrightarrow{T_m}G_m$, with each $T_j$ a guarded primitive in its input snapshot. Thus $G_m=(T_m\circ\cdots\circ T_1)(G_0)$. Each step preserves $V$, and at index $j$ the active vertex set is $\{v\in V:\deg_{G_j}(v)>0\}$ (**Relational Vertex Emergence** <Ref id="1.5.5" label="§1.5.5" />).

**III. Recorded Rollback**

Let $R_j$ be the restoration determined by the record for step $j$. The pointwise identities give $R_j(G_j)=G_{j-1}$ (**Reversibility of Primitives** <Ref id="1.5.6" label="§1.5.6" />). Substitution from the last index to the first gives

$$
(R_1\circ\cdots\circ R_m)(G_m)=
(R_1\circ\cdots\circ R_{m-1})(G_{m-1})=\cdots=G_0 .
$$

Q.E.D.

**In Plain English:**

Section 1.5.7 formalizes the properties of the QBD proof regarding vacuum repertoire.

---

### 1.5.8 Type-Theoretic Validation via Lean 4 Core {#1.5.8}

:::note[**Lean 4 Encoding of Recorded Edge Rollback via Pointwise Equality**]
:::

Type-theoretic certification of the active-field rollback identities (**Reversibility of Primitives** <Ref id="1.5.6" label="§1.5.6" />) and their pointwise derivation (**Reversibility of Primitives** <Ref id="1.5.6.1" label="§1.5.6.1" />) proceeds via the following verification strategy.

1.  **Encoding:** A timestamped graph stores a Boolean adjacency and a natural height at each directed pair.
2.  **Theorem Statements:** The two compositions preserve both fields at every pair in their stated domains.
3.  **Proof Closure:** The proof splits on equality with the edited pair and rewrites the corresponding conditionals.

```lean
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
```

**Verification Summary:**

The two closed terms certify the active-field identities. Deletion rollback reads the saved height, and addition rollback uses the absent-pair zero-height premise. The Lean kernel accepts both pointwise results.

**In Plain English:**

Section 1.5.8 formalizes the properties of the QBD type-theoretic regarding validation via lean 4 core.

---

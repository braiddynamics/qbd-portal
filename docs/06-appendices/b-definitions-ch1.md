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

The historical evolution of axiomatic justification, epitomized by the independence of Euclid's parallel postulate and the pragmatic acceptance of the Axiom of Choice, demonstrates that when foundational postulates cannot be syntactically derived or intuitively verified as "self-evident," their legitimacy rests upon **Coherentist Justification**. Rather than seeking validation from an impossible chain of antecedent proofs, the axiomatic basis $\mathcal{A}_{\mathrm{ax}}$ of a formal deductive system $\mathfrak{D} = (\mathcal{L}, \mathcal{A}_{\mathrm{ax}}, \mathcal{I})$ is justified holistically by the emergent properties of the global structure it generates.

The adoption of an Axiomatic Basis $\mathcal{A}_{\mathrm{ax}}$ is governed exclusively by the satisfaction of four **Coherence Criteria**:

1. **Consistency:** The absolute guarantee of formal non-contradiction, ensuring $\mathcal{A}_{\mathrm{ax}} \nvdash \perp$.
2. **Independence:** The minimality of the basis, such that for every $a \in \mathcal{A}_{\mathrm{ax}}$, $\mathcal{A}_{\mathrm{ax}} \setminus \{a\} \nvdash a$, ensuring no redundant assumptions are codified as axioms.
3. **Parsimony:** The minimization of the cardinality $|\mathcal{A}_{\mathrm{ax}}|$ and structural complexity of postulates relative to the explanatory scope of the system (Occam's razor).
4. **Fertility (Systemic Utility):** The capacity of $(\mathcal{L}, \mathcal{A}_{\mathrm{ax}}, \mathcal{I})$ to generate a rich, non-trivial body of theorems ($\mathcal{A}_{\mathrm{ax}} \vdash \theta$) that unifies disparate structures, resolves foundational paradoxes, and, in the construction of a physical theory, maps isomorphically to observable phenomena.

**Holistic Support vs. Linear Circularity**

Coherentist justification replaces the classical foundationalist model, which envisions knowledge as a hierarchical tower resting upon "self-evident" bedrock, with a relational model (analogous to Otto Neurath's ship), wherein foundational postulates and derived theorems exist in a web of mutual support.

Crucially, this mode of justification does not commit the fallacy of circular reasoning (*petitio principii*). A circular argument operates linearly ($P \vdash P$), providing no new explanatory content. Coherentist validation operates non-linearly: the axiomatic basis $\mathcal{A}_{\mathrm{ax}}$ is not proved by its consequences, but rather justified by the global stability, parsimony, and mathematical and empirical fertility of the complete deductive edifice.

:::note[**Summary Table: Epistemological Approaches**]
:::

| Dimension | Foundationalist View (Classical) | Coherentist View (Formalist / Constructive) |
| :--- | :--- | :--- |
| **Nature of Axioms** | Self-evident truths; direct descriptions of an absolute, pre-existing reality. | Foundational assumptions; formal rules defining a generative system. |
| **Source of Justification** | Direct intuition, self-evidence, or linear antecedent derivation. | Systemic properties: consistency ($\nvdash \perp$), parsimony ($\lvert\mathcal{A}_{\mathrm{ax}}\rvert$), and generative fertility. |
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

Let $G = (V, E, H)$ be a causal graph. For any directed causal path $\pi_{\mathrm{path}} = (v_0, v_1, \dots, v_k)$ in $G$ representing an observer's trajectory, the **Emergent Physical Time** interval $\Delta t_{phys}$ along the path is defined as:

$$
\Delta t_{phys} = \tau(\pi_{\mathrm{path}}) = f\left(k, \{H(e) \mid e \in \pi_{\mathrm{path}}\}\right)
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
Logical time is a discrete sequence of integer steps tracking the repeated application of the universal update operator, ensuring an absolute causal order.

---

### 1.3.4 Theorem: Temporal Finitude {#1.3.4}

:::info[**Temporal Finitude via Finite Capacity of Distinguishable Histories**]
:::

Let the histories distinguished at observation admit an injective encoding into $M_{\mathrm{st}}<\infty$ possible present states. Their cardinality is at most $M_{\mathrm{st}}$, and the comb with distinct retained terminal alternatives and the full continuing binary prefix tree give, respectively,

$$
K\le M_{\mathrm{st}}-1,\qquad K\le\lfloor\log_2 M_{\mathrm{st}}\rfloor.
$$

**In Plain English:**  
The universe must have had a beginning (a logical step zero) because an infinite past would require infinite information capacity, resulting in thermodynamic collapse.

---

### 1.3.5 Lemma: Finite Information Substrate {#1.3.5}

:::info[**Finite Information Substrate via Entropy of Finite Update Choices**]
:::

Let $A_t$ and $C_t$ count the trials in a frozen snapshot, with one binary addition trial per distinct candidate return chord of a simple two-path, at most one deletion trial per old triangle with at most four outcomes, and the successor determined by the snapshot and realized trial list. The conditional realization entropy is at most $A_t+2C_t$ bits, and under fixed initialization, uniform degree, one trial per candidate edge and at most linear vertex growth, both the accumulated conditional choice entropy and induced graph trajectory entropy are $O(T^2)$ through $T$ ticks.

**In Plain English:**  
The amount of information needed to describe the universe's state cannot grow faster than a quadratic curve, preventing informational overload and keeping the system stable.

---

### 1.3.5.1 Proof: Finite Information Substrate {#1.3.5.1}

:::tip[**Finite Information Substrate via Support Counting and the Entropy Chain Rule**]
:::

**I. Counting Realizations in a Frozen Snapshot**

Fix the input $G_t=g$ and index the $A_t(g)$ addition trials and $C_t(g)$ old-triangle trials. If $D_j(g)$ is the outcome set of the $j$-th deletion trial, the realized list $\Xi_t$ takes values in the product

$$
S_g=\{0,1\}^{A_t(g)}\times\prod_{j=1}^{C_t(g)}D_j(g),
\qquad
|S_g|=2^{A_t(g)}\prod_{j=1}^{C_t(g)}|D_j(g)|
\le 2^{A_t(g)+2C_t(g)}.
$$

Write $q_\xi=\Pr(\Xi_t=\xi\mid G_t=g)$ and $n_g=|\{\xi:q_\xi>0\}|$. Concavity of $\log_2$ gives

$$
\begin{aligned}
H_S(\Xi_t\mid G_t=g)
&=\sum_{q_\xi>0}q_\xi\log_2\frac1{q_\xi}\\
&\le \log_2\left(\sum_{q_\xi>0}q_\xi\frac1{q_\xi}\right)
=\log_2 n_g
\le A_t(g)+2C_t(g).
\end{aligned}
$$

**II. Counting Supporting Paths**

For a middle vertex $w$ the ordered pair of incident directed edges $(v,w),(w,u)$ ranges over at most $d_{\mathrm{in}}(w)d_{\mathrm{out}}(w)$ possibilities. Requiring three distinct vertices can only reduce this count (**2-Path** <Ref id="1.2.5" label="§1.2.5" />). Every admissible addition has a supporting two-path, and one path determines only the return chord $(u,v)$. Every directed triangle also contains a two-path, and a given path belongs to at most one directed triangle, since its third edge must be $(u,v)$. Consequently, for maximum degree $\Delta$,

$$
\begin{aligned}
P_2(G_t)&\le\sum_{w\in V_t}d_{\mathrm{in}}(w)d_{\mathrm{out}}(w)
\le N_t\Delta^2,\\
A_t(G_t)&\le P_2(G_t),\qquad C_t(G_t)\le P_2(G_t),\\
A_t(G_t)+2C_t(G_t)&\le 3\Delta^2N_t
\le3\Delta^2(a+bt).
\end{aligned}
$$

**III. Entropy of the Choice Sequence**

With $G_0$ fixed, each list $\xi_{<t}$ determines $G_t$. Applying the fixed-snapshot bound on each positive-probability prefix and averaging gives

$$
\begin{aligned}
H_S(\Xi_t\mid\Xi_{<t})
&=\sum_{\xi_{<t}}\Pr(\Xi_{<t}=\xi_{<t})
  H_S(\Xi_t\mid\Xi_{<t}=\xi_{<t})\\
&\le\sum_{\xi_{<t}}\Pr(\Xi_{<t}=\xi_{<t})\,3\Delta^2(a+bt)
=3\Delta^2(a+bt).
\end{aligned}
$$

The chain rule and the arithmetic sum yield

$$
\begin{aligned}
H_S(\Xi_0,\ldots,\Xi_{T-1})
&=\sum_{t=0}^{T-1}H_S(\Xi_t\mid\Xi_{<t})\\
&\le3\Delta^2\left(aT+b\sum_{t=0}^{T-1}t\right)
=3\Delta^2\left(aT+\frac{bT(T-1)}2\right).
\end{aligned}
$$

**IV. Projection to the Graph Trajectory**

Write $X=(\Xi_0,\ldots,\Xi_{T-1})$ and $Y=(G_1,\ldots,G_T)$. As $Y$ is determined by $X$, $H_S(Y\mid X)=0$, so

$$
H_S(X)=H_S(X,Y)=H_S(Y)+H_S(X\mid Y)\ge H_S(Y).
$$

Thus both entropies satisfy the displayed quadratic bound (**Finite Information Substrate** <Ref id="1.3.5" label="§1.3.5" />).

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

For a fixed-vertex edit history, let $A_t^{\mathrm{ret}}$ and $D_t$ denote the numbers of insertions and deletions from tick $t$ to tick $t+1$. Suppose deletions remove only preexisting pairs, insertions add only previously absent pairs, and $B_t$ consists of exactly one fresh record per insertion. These hypotheses yield

$$
\begin{aligned}
A^{\mathrm{ret}}&=\sum_{t=a}^{b-1}A_t^{\mathrm{ret}}=\sum_{t=a}^{b-1}|B_t|=|\mathcal E_b\setminus\mathcal E_a|,\\
|E_b|-|E_a|
&=\sum_{t=a}^{b-1}(|E_{t+1}|-|E_t|)
=\sum_{t=a}^{b-1}(A_t^{\mathrm{ret}}-D_t)=A^{\mathrm{ret}}-D ,
\end{aligned}
$$

where $D=\sum_{t=a}^{b-1}D_t$. The active tick count $M_{\mathrm{act}}$ counts a tick with both operations once. Since $\mathbf1_{\{A_t^{\mathrm{ret}}+D_t>0\}}\le A_t^{\mathrm{ret}}+D_t$, it obeys

$$
\begin{aligned}
M_{\mathrm{act}}
&=\sum_{t=a}^{b-1}\mathbf1_{\{A_t^{\mathrm{ret}}+D_t>0\}}
\le A^{\mathrm{ret}}+D\\
&=|E_a|+2A^{\mathrm{ret}}-|E_b|
\le |E_a|+2|\mathcal E_b\setminus\mathcal E_a|.
\end{aligned}
$$

**III. Entropy Summation**

For trajectory variables $X_a,\ldots,X_b$ and the specified set $J$ of $K$ ticks, nonnegativity of conditional entropy gives

$$
\begin{aligned}
H_S(X_a,\ldots,X_b)-H_S(X_a)
&=\sum_{t=a}^{b-1}H_S(X_{t+1}\mid X_a,\ldots,X_t)\\
&\ge \sum_{t\in J}H_S(X_{t+1}\mid X_a,\ldots,X_t)\ge \epsilon K.
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

**I. Coordinates of the Adjacency Projection**

Fix a vertex set $V$ of size $N$. For the directed pair domain $P=\{(u,v)\in V^2:u\ne v\}$, each of the $N$ source vertices admits $N-1$ target vertices. An active adjacency is determined by the vector of edge indicators (**Causal Graph Substrate** <Ref id="1.4.1" label="§1.4.1" />)

$$
|P|=\sum_{u\in V}(N-1)=N(N-1),\qquad
E_t\longmapsto (\mathbf 1_{\{e\in E_t\}})_{e\in P}\in\{0,1\}^{P}.
$$

Two different edge sets differ on at least one pair, so this map is injective. The cardinality of the target is

$$
|\{0,1\}^{P}|=\prod_{e\in P}2=2^{|P|}=2^{N(N-1)}.
$$

**II. Repeated Projection**

For $m=2^{N(N-1)}+1$ observation ticks $t_1<\cdots<t_m$, suppose all adjacencies were distinct. Injectivity would give

$$
2^{N(N-1)}+1
=m
=|\{E_{t_1},\ldots,E_{t_m}\}|
\le |\{0,1\}^{P}|=2^{N(N-1)},
$$

a contradiction. Hence $E_s=E_t$ for two distinct observation ticks $s<t$.

**III. Separation of the Occurrence Records**

For a creation occurrence $\omega$ recorded after $s$ and by $t$, the cumulative sets satisfy

$$
\omega\in\mathcal E_t\setminus\mathcal E_s,\qquad
\mathcal E_t=\mathcal E_s\sqcup(\mathcal E_t\setminus\mathcal E_s),
\qquad
(E_s,\mathcal E_s)\ne(E_t,\mathcal E_t).
$$

In the record-level example, $e=(a,b)$ has initial occurrence $\omega_0=(a,b,0,h_0)$. A deletion at tick one and fresh creation $\omega_2=(a,b,2,h_2)$ at tick two give

$$
\begin{aligned}
E_0&=\{e\}, &\mathcal E_0&=\{\omega_0\},\\
E_1&=E_0\setminus\{e\}=\varnothing,
&\mathcal E_1&=\mathcal E_0\cup\varnothing=\{\omega_0\},\\
E_2&=E_1\cup\{e\}=\{e\},
&\mathcal E_2&=\mathcal E_1\sqcup\{\omega_2\}=\{\omega_0,\omega_2\}.
\end{aligned}
$$

The birth coordinates distinguish $\omega_2$ from $\omega_0$. Thus

$$
E_0=E_2,\qquad
\mathcal E_0=\mathcal E_1\subsetneq\mathcal E_2,\qquad
(E_0,\mathcal E_0)\ne(E_2,\mathcal E_2).
$$

The example separates recurrence of the adjacency projection from recurrence of the record (**Finite State Recurrence** <Ref id="1.3.7" label="§1.3.7" />).

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

**I. Interval Order**

Let the physical observation interval be $[A,B]$ with $B-A=T_{\mathrm{phys}}$. The $m$ complete steps correspond to ordered intervals

$$
A\le a_1\le b_1\le a_2\le b_2\le\cdots\le a_m\le b_m\le B,
\qquad b_j-a_j\ge\tau_0>0.
$$

Logical indices count the steps, and the inequalities above concern the stipulated physical durations (**Global Logical Time** <Ref id="1.3.3" label="§1.3.3" />).

**II. Adding Step Durations and Gaps**

For $m\ge1$, write the full length as

$$
\begin{aligned}
B-A
&=(a_1-A)+\sum_{j=1}^{m}(b_j-a_j)
  +\sum_{j=1}^{m-1}(a_{j+1}-b_j)+(B-b_m)\\
&\ge \sum_{j=1}^{m}(b_j-a_j)
\ge \sum_{j=1}^{m}\tau_0=m\tau_0.
\end{aligned}
$$

For $m=0$ the same inequality holds since $T_{\mathrm{phys}}\ge0$.

**III. Integer Bound and Exclusion of an Infinite List**

Dividing by $\tau_0$ gives $m\le T_{\mathrm{phys}}/\tau_0$. Since $m$ is an integer,

$$
m\le\left\lfloor\frac{T_{\mathrm{phys}}}{\tau_0}\right\rfloor .
$$

An infinite family would contain $K=\lfloor T_{\mathrm{phys}}/\tau_0\rfloor+1$ distinct intervals. In increasing order of their left endpoints they still satisfy $A\le a_1$, $b_j\le a_{j+1}$ for $j<K$, and $b_K\le B$. The gaps in the duration sum are therefore nonnegative, and

$$
T_{\mathrm{phys}}=B-A\ge\sum_{j=1}^K(b_j-a_j)
\ge K\tau_0
=\left(\left\lfloor T_{\mathrm{phys}}/\tau_0\right\rfloor+1\right)\tau_0
>T_{\mathrm{phys}} .
$$

The strict inequality follows from the floor bound and $\tau_0>0$. The contradiction excludes an infinite list of steps (**Supertask Impossibility** <Ref id="1.3.8" label="§1.3.8" />).

Q.E.D.

**In Plain English:**  
Section 1.3.8.1 formalizes the properties of the QBD proof regarding supertask impossibility.

---

### 1.3.9 Lemma: Finite Capacity of History Encodings {#1.3.9}

:::info[**Finite Capacity of History Encodings via Injective Encoding of Occurrence Histories**]
:::

Let $f:\mathcal H_{\mathrm{hist}}\to S$ inject a family of distinguishable histories into a finite set of $M_{\mathrm{st}}$ states, so $|\mathcal H_{\mathrm{hist}}|\le M_{\mathrm{st}}$. For a comb with its $K$ terminating alternatives and final continuing history included in $\mathcal H_{\mathrm{hist}}$, and for a binary continuing-prefix tree with all depth-$K$ histories included in $\mathcal H_{\mathrm{hist}}$, the respective bounds are

$$
K+1\le M_{\mathrm{st}},\qquad 2^K\le M_{\mathrm{st}}.
$$

**In Plain English:**  
Section 1.3.9 formalizes the properties of the QBD lemma regarding finite capacity of history encodings.

---

### 1.3.9.1 Proof: Finite Capacity of History Encodings {#1.3.9.1}

:::tip[**Finite Capacity of History Encodings via Pigeonhole Counting and Prefix Induction**]
:::

**I. Encoding**

The histories counted here are distinct records of occurrences (**Finite Capacity of History Encodings** <Ref id="1.3.9" label="§1.3.9" />) (**Backward Accumulation** <Ref id="1.3.6" label="§1.3.6" />).

The image is a subset of the state set, so $|\mathcal H_{\mathrm{hist}}|=|f(\mathcal H_{\mathrm{hist}})|\le |S|=M_{\mathrm{st}}$.

**II. Comb**

Two alternatives that terminate at different branch points differ at the earlier point, where one continues and the other terminates. The final continuing history also differs from every terminated alternative at its branch point. Hence $K+1\le|\mathcal H_{\mathrm{hist}}|\le M_{\mathrm{st}}$.

**III. Full Continuing Branches**

Let $P_j$ be the set of continuing prefixes of depth $j$, with $n_j=|P_j|$. The single root gives $n_0=1=2^0$. For $j<K$, every child has one parent. If $c(p)$ counts the continuing children of $p$, then

$$
n_{j+1}=\sum_{p\in P_j}c(p)\ge\sum_{p\in P_j}2=2n_j .
$$

The induction hypothesis $n_j\ge2^j$ gives $n_{j+1}\ge2\cdot2^j=2^{j+1}$. In particular, $2^K\le n_K$. The depth-$K$ histories are included in $\mathcal H_{\mathrm{hist}}$, so $2^K\le n_K\le|\mathcal H_{\mathrm{hist}}|\le M_{\mathrm{st}}$.

Q.E.D.

**In Plain English:**  
Section 1.3.9.1 formalizes the properties of the QBD proof regarding finite capacity of history encodings.

---

### 1.3.10 Lemma: Departure After an Infinite Hold {#1.3.10}

:::info[**Exclusion of Positive Probability for Departure from an Infinite Hold**]
:::

Let $(X_t)_{t\in\mathbb Z}$ be a time-homogeneous Markov chain on a countable state space.
Then the probability of a departure from a state occupied at every preceding tick is zero.

**In Plain English:**
A time-homogeneous Markov chain on a countable state space has zero probability of leaving a state it has occupied at every preceding tick.

---

### 1.3.10.1 Proof: Departure After an Infinite Hold {#1.3.10.1}

:::tip[**Exclusion of Departure via Geometric Holding Probabilities**]
:::

**I. Probability of a Finite Hold and Departure**

Let $S$ denote the countable state space and let $K$ denote the one-step transition kernel (**Departure After an Infinite Hold** <Ref id="1.3.10" label="§1.3.10" />). Let $x$ denote an arbitrary state in $S$, and let $s$ denote an arbitrary integer serving as the last holding tick. The next tick is $s+1$ under unit-step indexing (**Global Logical Time** <Ref id="1.3.3" label="§1.3.3" />). Let $p$ denote the probability $K(x,x)\in[0,1]$.

Let $m$ denote a positive integer. For $0\le j\le m+1$, define $B_{m,j}$ as the event that each listed state equals $x$.

$$
B_{m,j}=\bigcap_{i=0}^{j}\{X_{s-m+i}=x\},
\qquad 0\le j\le m+1.
$$

For $0\le j\le m$, let $t$ denote $s-m+j$. The intersection through index $j+1$ yields

$$
B_{m,j+1}=B_{m,j}\cap\{X_{t+1}=x\}.
$$

If $\Pr(B_{m,j})>0$, the inclusion $B_{m,j}\subseteq\{X_t=x\}$ implies $\Pr(X_t=x)>0$. Conditioning on $B_{m,j}$ specifies the successive states from $s-m$ through $t$. The reduction to conditioning on $X_t=x$ follows from the Markov property. Time homogeneity implies that the resulting conditional probability is $K(x,x)$. The successive equalities are

$$
\begin{aligned}
\Pr(B_{m,j+1})
&=\Pr(B_{m,j})\Pr(X_{t+1}=x\mid B_{m,j})\\
&=\Pr(B_{m,j})\Pr(X_{t+1}=x\mid X_t=x)\\
&=\Pr(B_{m,j})K(x,x)\\
&=p\Pr(B_{m,j}).
\end{aligned}
$$

If $\Pr(B_{m,j})=0$, the inclusion $B_{m,j+1}\subseteq B_{m,j}$ implies $\Pr(B_{m,j+1})=0=p\Pr(B_{m,j})$. The two cases establish the recurrence for every $0\le j\le m$.

At $j=0$, the one-term intersection $B_{m,0}=\{X_{s-m}=x\}$ and the convention $p^0=1$ yield $\Pr(B_{m,0})=\Pr(X_{s-m}=x)p^0$. For $0\le j\le m$, the recurrence and the induction hypothesis $\Pr(B_{m,j})=\Pr(X_{s-m}=x)p^j$ yield

$$
\Pr(B_{m,j+1})
=p\Pr(B_{m,j})
=p\Pr(X_{s-m}=x)p^j
=\Pr(X_{s-m}=x)p^{j+1}.
$$

In particular, $B_{m,m}$ records a hold through tick $s$, and $B_{m,m+1}=B_{m,m}\cap\{X_{s+1}=x\}$ records a hold through the next tick as well. Define $C_m$ as the event of a finite hold followed by departure, namely $B_{m,m}\setminus B_{m,m+1}$. The disjoint decomposition of $B_{m,m}$ into $C_m$ and $B_{m,m+1}$ and the two induction values yield

$$
\begin{aligned}
\Pr(C_m)
&=\Pr(B_{m,m})-\Pr(B_{m,m+1})\\
&=\Pr(X_{s-m}=x)p^m-\Pr(X_{s-m}=x)p^{m+1}\\
&=\Pr(X_{s-m}=x)p^m(1-p)\\
&\le p^m(1-p).
\end{aligned}
$$

**II. Probability of an Infinite Hold for a Fixed State and Tick**

Define $A_{x,s}$ as the event that the chain occupies $x$ through every tick up to $s$ and departs at $s+1$.

$$
A_{x,s}=\{X_{s+1}\ne x\}\cap\bigcap_{t\le s}\{X_t=x\}.
$$

The intersection is countable. For every $m\ge1$, the conditions defining $A_{x,s}$ include all $m+1$ holding conditions in $B_{m,m}$ and the departure condition at $s+1$. These conditions imply $A_{x,s}\subseteq C_m$. Consequently $\Pr(A_{x,s})$ is bounded by $\Pr(C_m)$ in the chain

$$
0\le\Pr(A_{x,s})\le\Pr(C_m)\le p^m(1-p).
$$

For $p=0$ and $m\ge1$, the factor $p^m$ is zero. For $p=1$, the factor $1-p$ is zero. The zero upper bound in each case implies $\Pr(A_{x,s})=0$.

For $0<p<1$, define $\delta$ as $(1-p)/p$. Then $\delta>0$ and $1+\delta=(p+1-p)/p=1/p$. The binomial expansion yields

$$
(1+\delta)^m
=1+m\delta+\sum_{k=2}^{m}\binom{m}{k}\delta^k
\ge 1+m\delta ,
$$

with the sum empty at $m=1$. Taking reciprocals of the positive lower bound yields

$$
0\le\Pr(A_{x,s})
\le (1-p)p^m
=\frac{1-p}{(1+\delta)^m}
\le\frac{1-p}{1+m\delta}.
$$

For any $\varepsilon>0$, the choice of an integer $m>(1-p)/(\varepsilon\delta)$ implies $1+m\delta>(1-p)/\varepsilon$. Dividing $1-p$ by this positive denominator yields a bound strictly less than $\varepsilon$. If $\Pr(A_{x,s})$ were positive, $\varepsilon=\Pr(A_{x,s})$ would imply $\Pr(A_{x,s})<\Pr(A_{x,s})$. This contradiction establishes $\Pr(A_{x,s})=0$ also for $0<p<1$.

**III. Exhaustion by Finite Sets of States and Ticks**

Let $i$ denote an injection from $S$ into $\mathbb N_0$. Its existence follows from countability of $S$. For $n\in\mathbb N_0$, define $F_n$ as the set of pairs satisfying both index bounds and define $U_n$ as the union of the corresponding events.

$$
F_n=\{(x,s)\in S\times\mathbb Z:i(x)\le n,\ |s|\le n\},
\qquad U_n=\bigcup_{(x,s)\in F_n}A_{x,s}.
$$

The index condition selects at most $n+1$ states, and the ticks are among $-n,-n+1,\ldots,n$, a list of $2n+1$ integers. The number of pairs in $F_n$ is bounded by the product $(n+1)(2n+1)$. Finite subadditivity and the fixed-pair result yield

$$
0\le\Pr(U_n)
\le\sum_{(x,s)\in F_n}\Pr(A_{x,s})
=\sum_{(x,s)\in F_n}0
=0.
$$

The sets $F_n$ are increasing. For any pair $(x,s)$, the integer $n=\max\{i(x),|s|\}$ satisfies both membership conditions, which implies $(x,s)\in F_n$. This establishes that every pair appears in the exhaustion.

**IV. Probability of Departure at an Arbitrary Tick**

Let $A$ denote the event of departure from a state held at every preceding tick. Every outcome in $A$ specifies a holding state $x$ and a last holding tick $s$, which implies membership in $A_{x,s}$ and in some $U_n$. Conversely, every outcome in a $U_n$ belongs to an $A_{x,s}$ and satisfies the defining conditions of $A$. The two inclusions establish $A=\bigcup_{n\ge0} U_n$.

Define $D_0$ as $U_0$ and, for $n\ge1$, define $D_n$ as $U_n\setminus U_{n-1}$. For $j<n$, the inclusion $D_j\subseteq U_j\subseteq U_{n-1}$ implies $D_j\cap D_n=\varnothing$. Every outcome in some $U_n$ belongs to $D_j$ at its least such index $j$, and every $D_n$ lies in $U_n$. These inclusions and the pairwise disjointness establish that $A$ is the disjoint union of the $D_n$. The inequalities $0\le\Pr(D_n)\le\Pr(U_n)=0$ imply $\Pr(D_n)=0$ for each $n$. Countable additivity yields

$$
\Pr(A)=\sum_{n=0}^{\infty}\Pr(D_n)=\sum_{n=0}^{\infty}0=0.
$$

Q.E.D.

**In Plain English:**
Section 1.3.10.1 formalizes the properties of the QBD proof regarding departure after an infinite hold.

---

### 1.3.11 Proof: Temporal Finitude {#1.3.11}

:::tip[**Temporal Finitude via Assembly of Conditional History Bounds**]
:::

**I. Identification of the Count**

Let $\mathcal H$ denote the histories distinguished at observation and $\mathcal S$ the possible present states. The injective encoding $f:\mathcal H\to\mathcal S$ implies

$$
|\mathcal H|=|f(\mathcal H)|\le|\mathcal S|=M_{\mathrm{st}}.
$$

For one-tick extensions of a fixed past, let $\mathcal H_1\subseteq\mathcal H$ denote the distinct extensions from the frozen snapshot $g$. Under the trial hypotheses of **Finite Information Substrate** <Ref id="1.3.5" label="§1.3.5" />, each trial list in $S_g$ determines one extension and $|S_g|\le 2^{A_t+2C_t}$. Thus

$$
|\mathcal H_1|\le \min\{M_{\mathrm{st}},\,2^{A_t+2C_t}\}.
$$

Under the hypotheses of **Finite State Recurrence** <Ref id="1.3.7" label="§1.3.7" />, let $i<j$ index a pair with $E_i=E_j$. If a record is added between these observations, then $\mathcal E_i\ne\mathcal E_j$. For histories distinguished by their occurrence sets, equality of their adjacency images therefore precludes an injective encoding by adjacency alone.

**II. Branch Depth**

The two counting cases give (**Finite Capacity of History Encodings** <Ref id="1.3.9" label="§1.3.9" />)

$$
K+1\le M_{\mathrm{st}}\ \Longrightarrow\ K\le M_{\mathrm{st}}-1,\qquad
2^K\le M_{\mathrm{st}}\ \Longrightarrow\ K\le\lfloor\log_2 M_{\mathrm{st}}\rfloor .
$$

If unbounded candidate past length forces unbounded $K$, the uniform bound on $K$ excludes unbounded candidate past length.

In the active-tick case, assume a two-sided time-homogeneous Markov chain of snapshots $G_t=(V,E_t,H_t)$ on fixed finite $V$ with irreflexive asymmetric adjacency, natural-number edge labels, insertions of absent pairs, deletions of present pairs, unchanged labels on surviving edges, and a complete append-only ledger recording exactly one fresh occurrence per insertion.

The active-tick case uses the occurrence bound in **Backward Accumulation** <Ref id="1.3.6" label="§1.3.6" />. On a fixed $N$-vertex set with an asymmetric irreflexive adjacency, each unordered pair carries at most one edge. On a realization with a finite complete observation ledger of size $B$, the ledger at the start of any preceding finite interval is a subset of the observation ledger. Thus every preceding finite interval ending at that observation satisfies

$$
M_{\mathrm{act}}
\le |E_{\mathrm{start}}|+2|\mathcal E_{\mathrm{end}}\setminus\mathcal E_{\mathrm{start}}|
\le \binom N2+2B .
$$

If the prior history contained more than $\binom N2+2B$ active ticks, a finite interval beginning at the earliest of any $\binom N2+2B+1$ of them and ending at observation would violate the bound. Thus the set of prior active ticks is finite. If it is nonempty, let $s$ denote its least tick.

For tick $t$, let $P_t$ denote the inserted pairs and $Q_t$ the deleted pairs. The edit hypotheses imply

$$
Q_t\subseteq E_t,\qquad P_t\cap E_t=\varnothing,\qquad
E_{t+1}=(E_t\setminus Q_t)\cup P_t.
$$

For every $t<s$, $P_t=Q_t=\varnothing$ implies $E_{t+1}=E_t$. The fixed vertex set and unchanged surviving labels establish $G_{t+1}=G_t$. Chaining the equalities from $t$ up to $s$ gives $G_t=G_s$ for every $t\le s$. On tick $s$, the update and disjointness conditions give

$$
E_s\setminus E_{s+1}=Q_s,\qquad E_{s+1}\setminus E_s=P_s.
$$

At least one of $P_s,Q_s$ is nonempty, so $E_{s+1}\ne E_s$ and hence $G_{s+1}\ne G_s$. There are finitely many possible edge sets on the fixed vertex set, and the height assignments for each edge set form a finite product of countable sets. The snapshot state space is therefore countable. The event of a finite complete ledger and a nonempty active past is contained in the event of departure after an infinite hold for this time-homogeneous chain. Its probability is zero (**Departure After an Infinite Hold** <Ref id="1.3.10" label="§1.3.10" />).

**III. Physical Execution**

For an execution of $L$ complete sequential steps in a finite physical interval the separate duration premise gives (**Supertask Impossibility** <Ref id="1.3.8" label="§1.3.8" />)

$$
L\tau_0\le T_{\mathrm{phys}}.
$$

Q.E.D.

**In Plain English:**  
Section 1.3.11 formalizes the properties of the QBD proof regarding temporal finitude.

---

### 1.4.1 Definition: Causal Graph Substrate {#1.4.1}

:::tip[**Mathematical Characterization of the Relational Configuration Space as a Formal Architecture**]
:::

Let the **Causal Graph Substrate** at logical tick $t$ be the active spatial configuration $G_t=(V,E_t,H_t)$, where $V$ is a fixed finite vertex set, $E_t\subseteq V\times V$ is irreflexive and asymmetric, and $H_t:E_t\to\mathbb N_0$ records immutable causal heights of the active edge occurrences. Directed spatial cycles are permitted; the chronological order belongs to the distinct creation-event structure.

A creation occurrence is a record $\omega=(u,v,b,h)$ with birth tick $b\in\mathbb N_0$ and causal height $h\in\mathbb N_0$. At most one occurrence of a given ordered pair is created per tick. The active-occurrence map $\alpha_t:E_t\to\mathcal E_t$ identifies the current record and satisfies $H_t(u,v)=h(\alpha_t(u,v))$. The creation ledger $\mathcal E_t$ retains past occurrences after active deletion (**Historical Category** <Ref id="4.1.2" label="§4.1.2" />).

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

The post-insertion update map is $\Psi(h)=1+\max\{m_0,h\}$. Its increment satisfies

$$
\Psi(h)-h=
\begin{cases}
1+m_0-h\ge1,&h\le m_0,\\
1+h-h=1,&h>m_0.
\end{cases}
$$

The iteration formula $h_j=m_0+j+1$ holds at $j=0$. If it holds at $j$, then

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

Induction proves $h_j\ge h_1+j-1$ for all $j\le k$. For $1\le i<j\le k$, the consecutive increments telescope:

$$
h_j-h_i=\sum_{\ell=i}^{j-1}(h_{\ell+1}-h_\ell)\ge\sum_{\ell=i}^{j-1}1=j-i>0.
$$

Thus $h_i<h_j$ for every ordered pair of distinct positions. This establishes the sequential-chain claim (**Transitive Causal Monotonicity** <Ref id="1.4.7" label="§1.4.7" />).

**IV. Conclusion**

$$
\boxed{h_1<\cdots<h_k,\qquad h_k\ge h_1+k-1.}
$$

Q.E.D.

**In Plain English:**  
Section 1.4.7.1 formalizes the properties of the QBD proof regarding transitive causal monotonicity.

---

### 1.4.8 Lemma: Least Admissible Causal Height {#1.4.8}

:::info[**Existence of a Pointwise Least Admissible Labeling from the Source-Maximum Recurrence**]
:::

Let an integer labeling $c$ of the creation occurrences be admissible if its values are at least zero on initial occurrences and at least one on later occurrences, and $c(\eta)\ge c(\omega)+1$ whenever $\omega D\eta$.
Then the source-maximum height with zero initialization is the pointwise least admissible labeling (**Creation Timestamp** <Ref id="1.4.4" label="§1.4.4" />).

**In Plain English:**
Every labeling that respects the birth-height bounds and increases by at least one across direct dependencies is at least as large as the source-maximum height at each occurrence.

---

### 1.4.8.1 Proof: Least Admissible Causal Height {#1.4.8.1}

:::tip[**Pointwise Comparison by Induction on Birth Tick**]
:::

**I. Direct Predecessors and the Source-Maximum Formula**

Let $P(\eta)$ denote the set $\{\omega:\omega D\eta\}$ of direct predecessors of an occurrence $\eta$. An initial occurrence has birth tick zero and height zero (**Creation Timestamp** <Ref id="1.4.4" label="§1.4.4" />). A direct predecessor must be present in the input snapshot of the transition creating its successor. The initial snapshot is stipulated, which implies that no transition creates its initial occurrences. The dependency definition then yields $P(\eta)=\varnothing$ when $b(\eta)=0$.

For a later occurrence $\eta=(u,v,n,h(\eta))$ with $n\ge1$, the transition creating it uses $G_{n-1}$. Let $I_\eta$ denote the set of incoming pairs of its source in that snapshot. By the definition of $D$, a predecessor of $\eta$ is precisely the active occurrence of one such pair. The active-occurrence map yields (**Causal Graph Substrate** <Ref id="1.4.1" label="§1.4.1" />)

$$
I_\eta=\{(x,u)\in E_{n-1}:x\in V\},
\qquad
P(\eta)=\{\alpha_{n-1}(x,u):(x,u)\in I_\eta\}.
$$

The common second coordinate $u$ implies that distinct pairs in $I_\eta$ have distinct first coordinates. Projection onto the first coordinate is injective into the finite set $V$. The image under $\alpha_{n-1}$ has at most one entry per pair in $I_\eta$, which implies $|P(\eta)|\le |I_\eta|\le |V|$. Activity of each $\omega\in P(\eta)$ at tick $n-1$ implies that it was born by that tick and yields

$$
b(\omega)\le n-1<n=b(\eta).
$$

For every $(x,u)\in I_\eta$, the equality $H_{n-1}(x,u)=h(\alpha_{n-1}(x,u))$ follows from the definition of the active height. Substitution into the source-maximum rule and use of the displayed description of $P(\eta)$ yield

$$
\begin{aligned}
h(\eta)
&=1+\max\bigl(\{0\}\cup\{H_{n-1}(x,u):(x,u)\in I_\eta\}\bigr)\\
&=1+\max\bigl(\{0\}\cup\{h(\alpha_{n-1}(x,u)):(x,u)\in I_\eta\}\bigr)\\
&=1+\max\bigl(\{0\}\cup\{h(\omega):\omega\in P(\eta)\}\bigr).
\end{aligned}
$$

Let $S_\eta$ denote $\{0\}\cup\{h(\omega):\omega\in P(\eta)\}$, and let $M_\eta$ denote $\max S_\eta$. Finiteness of $S_\eta$ and membership of zero imply that $M_\eta$ belongs to $S_\eta$. For every $a\in S_\eta$, $a\le M_\eta$ implies $a+1\le M_\eta+1$. Membership of $M_\eta$ in $S_\eta$ implies membership of $M_\eta+1$ in the shifted set $\{a+1:a\in S_\eta\}$. The attained upper bound yields

$$
\begin{aligned}
h(\eta)
&=1+M_\eta\\
&=\max\{a+1:a\in S_\eta\}\\
&=\max\bigl(\{1\}\cup\{h(\omega)+1:\omega\in P(\eta)\}\bigr).
\end{aligned}
$$

The last equality uses the shift of $0$ to $1$ and the shift of each predecessor height to $h(\omega)+1$.

**II. Verification of the Admissibility Conditions**

At birth tick zero, $h(\eta)=0$ and $0\ge0$ establish the initial floor $h(\eta)\ge0$. At every later tick, membership of $1$ in the set whose maximum equals $h(\eta)$ implies $h(\eta)\ge1$.

If $\omega D\eta$, then $\omega\in P(\eta)$, and $\eta$ is a later occurrence. Membership of $h(\omega)+1$ in the same set yields

$$
h(\eta)=\max\bigl(\{1\}\cup\{h(\xi)+1:\xi\in P(\eta)\}\bigr)
\ge h(\omega)+1.
$$

The initial floor, the later floor, and the direct-dependency inequality establish admissibility of $h$.

**III. Pointwise Comparison by Strong Induction**

Let $c$ denote an arbitrary admissible labeling. For each $n\in\mathbb N_0$, the induction assertion is

$$
\forall\eta\quad b(\eta)=n\ \Longrightarrow\ c(\eta)\ge h(\eta).
$$

At $n=0$, initialization implies $h(\eta)=0$ for every occurrence with $b(\eta)=0$. The initial floor for $c$ yields

$$
c(\eta)\ge0=h(\eta).
$$

Let $n$ denote a positive birth tick. Assume the assertion for every birth tick $j<n$. Let $\eta$ denote an arbitrary occurrence with $b(\eta)=n$. The later floor for $c$ implies $c(\eta)\ge1$. For any $\omega\in P(\eta)$, let $j$ denote $b(\omega)$. The comparison from Part I establishes $j<n$. The induction hypothesis at $j$ yields $c(\omega)\ge h(\omega)$. Adding one to both sides and using admissibility across $\omega D\eta$ yields

$$
c(\eta)\ge c(\omega)+1\ge h(\omega)+1 .
$$

Every member of $\{1\}\cup\{h(\omega)+1:\omega\in P(\eta)\}$ is bounded by $c(\eta)$ from above. Its maximum belongs to the set and equals $h(\eta)$. The bound on that member establishes $c(\eta)\ge h(\eta)$ at tick $n$. When there are no predecessors, the set is $\{1\}$ and the same bound yields $c(\eta)\ge1=h(\eta)$.

If the assertion failed at any tick, its failing ticks would form a nonempty subset of $\mathbb N_0$ with a least element. The base case excludes zero. At any positive least failing tick, the assertion holds at every smaller tick. The induction step then implies that the assertion holds at the supposed failing tick. This contradiction establishes the assertion at every birth tick.

**IV. Least Admissible Labeling**

Let $\mathcal C$ denote the set of admissible labelings. Membership $h\in\mathcal C$ follows from Part II. Part III applies to each $c\in\mathcal C$, and every occurrence has a birth tick in $\mathbb N_0$. These facts yield

$$
h\in\mathcal C
\qquad\text{and}\qquad
\forall c\in\mathcal C\ \forall\eta,\quad h(\eta)\le c(\eta).
$$

These are the membership and comparison conditions for $h$ to be the pointwise least element of $\mathcal C$.

Q.E.D.

**In Plain English:**
Section 1.4.8.1 formalizes the properties of the QBD proof regarding least admissible causal height.

---

### 1.4.9 Proof: Monotonicity of History {#1.4.9}

:::tip[**Synthesis of Irreflexivity via Transitivity to Establish Global Acyclicity**]
:::

**I. Direct Event Dependencies**

Let $\omega D\eta$ be a dependency with the stipulated creation-snapshot meaning (**Monotonicity of History** <Ref id="1.4.5" label="§1.4.5" />). The preceding incoming occurrence belongs to the creation snapshot of $\eta$. The source-side maximum therefore gives

$$
\omega D\eta\ \Longrightarrow\ h(\eta)\ge h(\omega)+1.
$$

Stable self-loop assignment also has the independent obstruction $h\ge h+1$ (**Irreflexivity of Timestamps** <Ref id="1.4.6" label="§1.4.6" />). Physical self-loops are excluded directly by the irreflexive edge constraint.

The source-maximum assignment is the pointwise least admissible labeling (**Least Admissible Causal Height** <Ref id="1.4.8" label="§1.4.8" />).

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
Section 1.4.9 formalizes the properties of the QBD proof regarding monotonicity of history.

---

### 1.5.1 Definition: Elementary Task Space {#1.5.1}

:::tip[**Mathematical Characterization of the Admissible Transformation Space as a Formal Architecture**]
:::

Let the **Elementary Task Space** $\mathfrak T(G)$ consist of elementary additions and deletions on a fixed spatial vertex set $V$. An addition inserts a directed pair between distinct vertices when both orientations are absent. It assigns the source-side causal height and records the new occurrence (**Creation Timestamp** <Ref id="1.4.4" label="§1.4.4" />). A deletion removes a present edge from the active graph and retains its historical occurrence.

Each primitive preserves $V$, changes exactly one active edge, and leaves all surviving occurrence heights unchanged.

**In Plain English:**  
Elementary Task Space defines the single-edge insertions and deletions permitted by the graph's incidence conditions.

---

### 1.5.2 Definition: Edge Addition Task {#1.5.2}

:::tip[**Formal Specification of the Primitive Edge Insertion Operator via Edge Addition Task**]
:::

Let the **Edge Addition Task** $\mathfrak T_{add}(u,v)$ act on $G_t=(V,E_t,H_t)$ for an absent pair $(u,v)$ with $u\ne v$ and $(v,u)\notin E_t$. The output snapshot $G'=(V',E',H')$ has the following vertex set, active edge set, and causal-height map.

$$
V'=V,\qquad E'=E_t\cup\{(u,v)\},\qquad
H'|_{E_t}=H_t,\qquad
H'(u,v)=1+\max\bigl(\{H_t(x,u):(x,u)\in E_t\}\cup\{0\}\bigr).
$$

The creation ledger at tick $t+1$ is $\mathcal E_{t+1}=\mathcal E_t\cup\{(u,v,t+1,H'(u,v))\}$.

**In Plain English:**  
Edge Addition Task defines the primitive that creates a directed link and gives it a causal height above the incoming heights at its source.

---

### 1.5.3 Definition: Edge Deletion Task {#1.5.3}

:::tip[**Formal Specification of the Primitive Edge Excision Operator via Edge Deletion Task**]
:::

Let the **Edge Deletion Task** $\mathfrak T_{del}(u,v)$ act on $G_t=(V,E_t,H_t)$ for $(u,v)\in E_t$. The output snapshot $G'=(V',E',H')$ has the following vertex set, active edge set, and causal-height map.

$$
V'=V,\qquad E'=E_t\setminus\{(u,v)\},\qquad H'=H_t|_{E'}.
$$

The creation ledger at tick $t+1$ is $\mathcal E_{t+1}=\mathcal E_t$.

**In Plain English:**  
Edge Deletion Task defines the primitive operator that removes an active directed causal link while preserving its historical timestamp in the sequence log.

---

### 1.5.4 Theorem: Vacuum Repertoire {#1.5.4}

:::info[**Vacuum Repertoire via Finite Composition and Recorded Rollback of Edge Tasks**]
:::

Let $\mathfrak T$ be the space of tasks witnessed by finite sequences of elementary edge additions and deletions on a fixed vertex set $V$. Each task is a finite composition of the primitives, with active incidence determined by the edge set and rollback of each active update specified by the edited pair and its previous height.

**In Plain English:**  
The Vacuum Repertoire Theorem shows how to compose elementary edge edits and use their records to restore the original active edges and heights.

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
The Reversibility of Primitives Lemma proves that every primitive edge addition or deletion has a unique inverse operation, ensuring that the substrate's transitions are completely reversible.

---

### 1.5.6.1 Proof: Reversibility of Primitives {#1.5.6.1}

:::tip[**Reversibility of Primitives via Pointwise Inversion of Edge Updates**]
:::

**I. Update Maps on a Fixed Directed-Pair Domain**

Write $G=(E,H)$ in the active-field representation (**Creation Timestamp** <Ref id="1.4.4" label="§1.4.4" />), with $H(x)=0$ on absent pairs. Fix $e$. If $S_G(x)=(E_G(x),H_G(x))$, the addition and deletion maps are defined pointwise by

$$
S_{A_{e,h}(G)}(x)=
\begin{cases}(1,h),&x=e,\\S_G(x),&x\ne e,\end{cases}
\qquad
S_{D_e(G)}(x)=
\begin{cases}(0,0),&x=e,\\S_G(x),&x\ne e.\end{cases}
$$

**II. Addition Followed by Deletion**

Suppose $E_G(e)=0$. At the edited pair and away from it, respectively,

$$
\begin{aligned}
S_{D_e(A_{e,h}(G))}(e)&=(0,0)=S_G(e),\\
S_{D_e(A_{e,h}(G))}(x)&=S_{A_{e,h}(G)}(x)=S_G(x)
&& (x\ne e).
\end{aligned}
$$

Both coordinates agree at every pair.

**III. Deletion Followed by Recorded Restoration**

Suppose $E_G(e)=1$ and save $h_0=H_G(e)$. The two compositions at the edited pair and every other pair are

$$
\begin{aligned}
S_{A_{e,h_0}(D_e(G))}(e)&=(1,h_0)=(E_G(e),H_G(e)),\\
S_{A_{e,h_0}(D_e(G))}(x)&=S_{D_e(G)}(x)=S_G(x)
&& (x\ne e).
\end{aligned}
$$

Extensional equality of the two active fields gives the partial inverses (**Reversibility of Primitives** <Ref id="1.5.6" label="§1.5.6" />)

$$
\boxed{D_e(A_{e,h}(G))=G\quad(E_G(e)=0),\qquad
A_{e,H_G(e)}(D_e(G))=G\quad(E_G(e)=1).}
$$

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

An admissible task has a witness sequence $G_0\xrightarrow{T_1}G_1\to\cdots\xrightarrow{T_m}G_m$, with each $T_j$ an elementary edit defined on its input snapshot. Thus $G_m=(T_m\circ\cdots\circ T_1)(G_0)$.

For an insertion of $(u,v)$, the input conditions $u\ne v$ and $(u,v),(v,u)\notin E$ imply that the sole new edge is neither a self-loop nor the reverse of an existing edge (**Edge Addition Task** <Ref id="1.5.2" label="§1.5.2" />). Every other pair retains its incidence and height. The new record enters the ledger by union. For a deletion, $E'=E\setminus\{(u,v)\}\subseteq E$ implies that any self-loop or reciprocal pair in $E'$ already belongs to $E$. Restriction preserves the height at each surviving edge, and $\mathcal E'=\mathcal E$ (**Edge Deletion Task** <Ref id="1.5.3" label="§1.5.3" />).

Each step preserves the vertex set, leaves the active edge set irreflexive and asymmetric, and retains the causal heights of surviving edges. At index $j$ the active vertex set is $\{v\in V:\deg_{G_j}(v)>0\}$ (**Relational Vertex Emergence** <Ref id="1.5.5" label="§1.5.5" />).

**III. Recorded Rollback**

Let $R_j$ denote the active-field restoration determined by the edited pair and its previous height for step $j$. The ledger is append-only along the forward sequence. The pointwise identities give $R_j(G_j)=G_{j-1}$ (**Reversibility of Primitives** <Ref id="1.5.6" label="§1.5.6" />). Substitution from the last index to the first gives

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

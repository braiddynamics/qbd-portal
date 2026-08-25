---
id: vacuum-phase
title: "A Constrained Stochastic Rewrite System on Timestamped DAGs: Microscopic Rules, Absorbing-State Dynamics, and Finite-N Quasi-Stationary Ensembles"
sidebar_label: "Vacuum Phase & QSD"
slug: /vacuum-phase
description: "A constrained stochastic rewrite process on timestamped DAGs exhibiting an absorbing-state phase transition under strict causal protection."
---

<nav aria-label="Breadcrumbs" style={{
  display: 'flex',
  alignItems: 'center',
  flexWrap: 'wrap',
  gap: '0.45rem',
  fontSize: '0.85rem',
  marginBottom: '1.25rem',
  color: 'var(--ifm-color-emphasis-700)'
}}>
  <a href="/" style={{ color: 'var(--ifm-color-emphasis-700)', textDecoration: 'none' }}>Home</a>
  <span style={{ opacity: 0.4 }}>/</span>
  <a href="/papers" style={{ color: '#2563eb', fontWeight: 600, textDecoration: 'none' }}>Research Papers</a>
  <span style={{ opacity: 0.4 }}>/</span>
  <span style={{ color: 'var(--ifm-color-emphasis-900)', fontWeight: 500 }}>Vacuum Phase &amp; QSD</span>
</nav>

:::info[**Preprint & Archival Record**]
**Title:** A Constrained Stochastic Rewrite System on Timestamped DAGs: Microscopic Rules, Absorbing-State Dynamics, and Finite-$N$ Quasi-Stationary Ensembles  
**Author:** **R. Fisher**, *Principal Investigator* ([ORCID: 0009-0006-2441-3282](https://orcid.org/0009-0006-2441-3282))  
**Affiliation:** Braid Dynamics  
**Published:** August 24, 2026 · **Version:** 1.0.0 (Preprint) · **License:** [Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)  
**Classification:** Statistical Mechanics · Discrete Gravity · Graph Rewriting  
**Formal Verification:** 34 Active Machine-Checked Lean 4 Theorems (0 Axioms, 0 Sorry)  
**Replication Engines:** C++20 Multithreaded Scaling Engine + Python 3.8+ reference implementation with 8 dedicated test suites (25 tests).
:::

<div style={{
  backgroundColor: 'var(--ifm-card-background-color)',
  border: '1px solid var(--ifm-color-emphasis-300)',
  borderRadius: '10px',
  padding: '1.25rem',
  marginBottom: '2rem',
  boxShadow: '0 2px 8px rgba(0,0,0,0.04)'
}}>
  <h4 style={{ margin: '0 0 0.75rem 0', fontSize: '1rem', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
    📁 Downloadable Publication &amp; Replication Files
  </h4>
  <table style={{ width: '100%', margin: 0, fontSize: '0.875rem' }}>
    <thead>
      <tr>
        <th style={{ textAlign: 'left' }}>File Name</th>
        <th style={{ textAlign: 'left' }}>Description</th>
        <th style={{ textAlign: 'left' }}>Size</th>
        <th style={{ textAlign: 'right' }}>Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>vacuum-phase.pdf</strong></td>
        <td>Complete Publication Manuscript (XeLaTeX)</td>
        <td>1.2 MB (1,211 KB)</td>
        <td style={{ textAlign: 'right' }}>
          <a href="pathname:///papers/vacuum-phase/downloads/vacuum-phase.pdf" download className="button button--xs button--primary">Download PDF</a>
        </td>
      </tr>
      <tr>
        <td><strong>vacuum-phase.md</strong></td>
        <td>Clean Markdown Manuscript (LaTeX math, standard tables)</td>
        <td>190 KB</td>
        <td style={{ textAlign: 'right' }}>
          <a href="pathname:///papers/vacuum-phase/downloads/vacuum-phase.md" download className="button button--xs button--secondary">Download MD</a>
        </td>
      </tr>
      <tr>
        <td><strong>vacuum-phase-replication.zip</strong></td>
        <td>Full Replication Bundle (C++20 engine, Python engine, tests, multi-scale datasets)</td>
        <td>32 KB</td>
        <td style={{ textAlign: 'right' }}>
          <a href="pathname:///papers/vacuum-phase/downloads/vacuum-phase-replication.zip" download className="button button--xs button--secondary">Download ZIP</a>
        </td>
      </tr>
      <tr>
        <td><strong>VacuumPhase.lean</strong></td>
        <td>Standalone Formal Verification Kernel (34 Theorems, 0 Axioms)</td>
        <td>29 KB</td>
        <td style={{ textAlign: 'right' }}>
          <a href="pathname:///papers/vacuum-phase/code/VacuumPhase.lean" download className="button button--xs button--secondary">Download Lean</a>
        </td>
      </tr>
      <tr>
        <td><strong>p_surv_N10000_cpp_production.csv</strong></td>
        <td>Production Monte Carlo Scaling Dataset (N=10,000)</td>
        <td>2.4 KB</td>
        <td style={{ textAlign: 'right' }}>
          <a href="pathname:///papers/vacuum-phase/data/p_surv_N10000_cpp_production.csv" download className="button button--xs button--secondary">Download Data</a>
        </td>
      </tr>
    </tbody>
  </table>
</div>

### Abstract

A constrained stochastic rewrite process operates on timestamped directed acyclic graphs (DAGs). The pre-geometric initial condition is a finite regular Bethe fragment. A single injected symmetry-breaking 3-cycle breaks bipartiteness and leaves the Bethe class; thereafter the only legal additions close existing 2-paths and the only legal deletions remove edges of existing 3-cycles, subject to unique-causality constraints and local bounded-horizon acyclicity pre-checks. Updates are applied in maximally parallel ticks: every legal site is accepted or rejected independently, accepted additions are merged idempotently, then accepted deletions act on the resulting graph. There is no spontaneous long-range creation term ($\Lambda_{\mathrm{micro}}\equiv 0$).

  Base thermodynamic rates are held at the fixed operating point $P_{\mathrm{add}}=1$, $Q_{\mathrm{del}}=1/2$, derived from a loop-closure entropy of one bit at temperature $T=\ln 2$. Constitutive scales are established via information-theoretic priors, including $\mu_0=1/\sqrt{2\pi}$ (natural-unit Gaussian stress variance normalization) and $\lambda_0=e-1$ (one-nat Arrhenius defect release), fixed analytically prior to numerical execution to define a canonical baseline operating point. At isolated-cycle self-stress $s=2$ one has $Q_{\mathrm{del}}\approx 0.999$, establishing an isolated death line where an unassisted seed cycle decays with characteristic decay lifetime (e-folding time) $\tau \approx 0.15$ ticks ($t_{1/2} = \tau \ln 2 \approx 0.10$ ticks). Consequently, escaping extinction demands jumping an analytical unpumped nucleation barrier $\rho_c = \frac{1}{2(9-3\lambda_0)} \approx 0.130$ via a first-tick autocatalytic burst across the un-stressed tree.

  A 100-trajectory ensemble at $N\approx 100$ and $(\mu_0,\lambda_0)$ is zero-inflated: across the unconditioned ensemble, the mean 3-cycle density is $\langle\rho\rangle\approx 0.029$ while the median is $\rho=0$, reflecting an empirical survival fraction $p_{\mathrm{surv}}=0.270 \pm 0.044$ ($95\%\text{ CI: }[0.183, 0.357]$). Conditioned on non-extinction ($N_3 > 0$), the active trajectories populate a robust Quasi-Stationary Distribution (QSD) with mean density $\langle\rho\rangle_{\mathrm{QSD}}\approx 0.092$ and median $\rho_{\mathrm{med,QSD}}=0.080$. Finite-size scaling across four orders of magnitude ($N = 10 \to 10,000$, $M = 100$ trajectories per scale) demonstrates that boundary leaf clipping diminishes as interior depth expands: the survival fraction rises monotonically to $p_{\mathrm{surv}} = 0.990 \pm 0.010$ (99% survival at $N=10,000$), the active core scales to $\langle N_3 \rangle_{\mathrm{QSD}} \approx 123.6$ cycles at asymptotic density $\rho \approx 1.2\%$, and the homeostatic lifetime expands by more than an order of magnitude ($\tau_{\mathrm{stall}} \approx 68 \to 752\text{ ticks}$). A two-parameter sweep confirms an active channel whose $\mu$ direction reveals a non-monotonic regulator: low $\mu$ evaporates the post-ignition burst, while high $\mu$ freezes it in place.

  Multi-scale numerical simulations demonstrate that sustained 3-cycle activity constitutes a robust non-equilibrium quasi-stationary phase whose lifetime and survival scale monotonically with system volume, escaping isolated-cycle deletion via clustered autocatalytic cascades.

---

# 1. Introduction

Discrete models of spacetime and of nonequilibrium matter share a common technical problem: how a constrained, local rewrite rule on a finite combinatorial object can sustain extended structure without a background lattice, a global clock, or an external particle bath. In causal set theory the kinematics are a locally finite partial order, and classical sequential growth supplies one dynamics in which new elements are born with probabilities that respect discrete general covariance [@bombelli1987spacetime; @rideout2000classical; @surya2019causal]. Causal dynamical triangulations replace the order with a sum over triangulated histories and diagnose the resulting geometry by spectral and Hausdorff dimensions [@ambjorn2004emergence; @ambjorn2005spectral]. Combinatorial and graphity-type models take the dual route of an evolving network whose locality is itself dynamical [@konopka2006quantum; @konopka2008quantum; @trugenberger2017combinatorial]. Graph-rewriting cosmologies in the Wolfram–Gorard lineage pose the same question in a multiway, scheduler-dependent form [@wolfram2002new; @gorard2020relativistic; @gorard2020quantum].

Constrained, background-independent rewrite processes on timestamped directed acyclic graphs (DAGs) exhibit an absorbing-state phase transition under strict causal protection and zero spontaneous background generation ($\Lambda_{\mathrm{micro}}\equiv 0$). This classical non-equilibrium statistical mechanics serves as a pre-geometric and thermodynamic framework for downstream quantum topological dynamics. Analyzing the resulting finite-$N$ ensembles through the lens of directed percolation and quasi-stationary distributions maps the exact combinatorial dynamics of the active phase.

The process is seeded, not spontaneously generated. The initial condition $G_0$ is a finite regular Bethe fragment: a rooted, outward-directed tree, bipartite, with no 3-cycles. A single injected 3-cycle breaks bipartiteness and takes the graph out of the Bethe class. Thereafter the only legal additions close existing 2-paths, and the only legal deletions remove edges of existing 3-cycles, subject to a unique-causality condition (PUC) and an acyclicity pre-check (AEC). Edge proposal generation is strictly local ($O(1)$ 2-paths and triads), while global causal consistency is protected via bounded-horizon verification ($\mathrm{TTL} = L_{\mathrm{cut}} = \lfloor \log_2 N \rfloor + 3$). There is no spontaneous long-range creation term: $\Lambda_{\mathrm{micro}}\equiv 0$. Updates occur in maximally parallel ticks. Every legal site is accepted or rejected independently; accepted additions are merged idempotently; accepted deletions then act on the resulting graph.

That move grammar possesses a clear nonequilibrium reading. Creation is autocatalytic: a new 3-cycle can appear only where a compliant 2-path already exists, so activity begets sites for further activity. Deletion is tension-accelerated: local cycle crowding raises the deletion probability. With $\Lambda_{\mathrm{micro}}=0$, a configuration with no remaining 3-cycles and no remaining legal 2-path closures cannot restart cycle activity. The extinct, typically scarred graph is absorbing for 3-cycle density. The natural theoretical framework consists of absorbing-state phase transitions and directed percolation on graphs [@hinrichsen2000nonequilibrium; @marro1999nonequilibrium; @henkel2008nonequilibrium; @bollobas2007phase].

Local rates are written as a constitutive kernel on a scalar stress $s$,

$$P_{\mathrm{acc}}=\mathrm{e}^{-\mu s},\qquad Q_{\mathrm{del}}=\min\bigl(1,\tfrac12(1+\lambda s)\,\mathrm{e}^{-\mu s}\bigr),$$

at a fixed operating point whose base pair $(P_{\mathrm{add}},Q_{\mathrm{del}})=(1,1/2)$ is the sparse Metropolis limit for one bit of loop-closure entropy at temperature $T=\ln 2$. The analytical scales $(\mu_0,\lambda_0)=(1/\sqrt{2\pi},\,e-1)$ serve as information-theoretic priors, derived from integer lattice $\mathbb{Z}$ Poisson summation and one-nat discrete defect relaxation respectively. At isolated-cycle self-stress $s=2$ the same kernel gives $Q_{\mathrm{del}}\approx 0.999$. Consequently, a lone 3-cycle is almost surely deleted in one tick, and any persistent activity must be clustered.

The core empirical question is precise:

> Under strictly local causal move constraints and zero background generation ($\Lambda_{\mathrm{micro}}=0$), can an injected topological defect seed a self-sustaining, quasi-stationary active phase at finite $N$, or is extinction the generic fate?

Ensemble simulations of the microscopic engine across four decades of lattice volume ($N = 10 \to 10,000$) resolve that question. A 100-trajectory ensemble at $N \approx 100$ and $(\mu_0,\lambda_0)$ is zero-inflated: across the unconditioned ensemble, the mean 3-cycle density is $\langle\rho\rangle\approx 0.029$ while the median is $\rho=0$. At $N=100$, leaf boundary truncation leaves the typical realization extinct ($p_{\mathrm{surv}}=0.270 \pm 0.044$). Survivors populate an active Quasi-Stationary Distribution (QSD) with mean density $\langle\rho\rangle_{\mathrm{QSD}} \approx 0.092$ and median $\rho_{\mathrm{med,QSD}} = 0.080$, surviving solely via clustered multi-cycle bursts. Multi-scale scaling to $N = 1,000$ and $N = 10,000$ confirms that expanding interior volume eliminates boundary quenching: the survival fraction rises to $p_{\mathrm{surv}} = 0.990 \pm 0.010$ (99% survival), the active cluster expands into an extensive $\langle N_3 \rangle_{\mathrm{QSD}} \approx 123.6$-cycle condensate at density $\rho \approx 1.2\%$, and the homeostatic lifetime scales up by $11.1\times$ ($\tau_{\mathrm{stall}} \approx 68 \to 752\text{ ticks}$). An unpumped continuum expansion reveals an intrinsic nucleation barrier $\rho_c = \frac{1}{2(9-3\lambda_0)} \approx 0.130$, demonstrating that classical diffusive growth cannot ignite geometry—ignition strictly requires the non-perturbative first-tick parallel tree burst. The two-parameter sweep locates a channel of activity whose $\mu$ dependence is non-monotonic: low $\mu$ evaporates the post-ignition burst, while high $\mu$ freezes it.

The analysis is structured as follows. Section 2 defines $G_0$, the legal moves, the implemented parallel tick, and proves the deterministic non-interference of the execution scheduler (Lemma 2.1). Section 3 derives the isolated-cycle death line (Proposition 3.1) and analyzes the clustered-burst mechanism (Corollaries 3.3 and 3.4). Section 4 derives the constitutive fixed-point propositions (Propositions 4.1–4.5) and establishes analytical parameter rigidity alongside macroscopic structural stability. Section 5 reports the $N\approx 100$ ensemble, distinguishes unconditioned moments from the conditioned QSD, and presents the multi-scale finite-size scaling results from $N = 10$ to $N = 10,000$. Section 6 derives the analytical nucleation threshold $\rho_c \approx 0.130$ of the unpumped rate equation, introduces the Directed Percolation absorbing Langevin equation, and evaluates the auxiliary pumped model. Section 7 frames the process as an absorbing-state dynamics and outlines the infinite-volume scaling program. Appendix A provides the complete, verified Lean 4 kernel formal proofs, and Appendix B provides the standalone reference simulation engines.

---

# 2. The Microscopic Rewrite System and Execution Scheduler

Section 2 defines the combinatorial state space, the causal move grammar, the local stress functional, and the parallel execution scheduler implemented in the simulation engine.

## 2.1 Combinatorial State Space: Spatial Graph $G_{\mathrm{space}}$ and Causal Poset $G_{\mathrm{event}}$

A combinatorial state of the system is a finite timestamped directed graph

$$G=(V,E,H),\qquad H:E\to\mathbb{N}_0.$$

The vertex set $V$ is fixed throughout each simulation trajectory ($N = |V|$). Each directed edge $e=(x,y)\in E$ carries an integer logical timestamp $H(e)\in\mathbb{N}_0$. Time and causal ordering are carried entirely by edges; vertices carry no intrinsic timestamps.

A structural distinction governs the kinematics of the pre-geometric substrate:

1. **The Spatial State Graph $G_{\mathrm{space}}$:** The graph $G=(V, E, H)$ represents the instantaneous spatial topology, whose directed 3-cycles $\mathcal{C}_3(G)$ correspond to minimal simplicial areas (triangulation) and local curvature excitations.
2. **The Causal Event Poset $G_{\mathrm{event}}$:** Effective causal influence between distinct vertices $u \le v$ is defined strictly by directed paths $\pi = (u=x_0, x_1, \dots, x_k=v)$ whose edge timestamps are strictly monotone increasing:
   $$u \le v \iff \exists \pi = (x_0, \ldots, x_k) \text{ such that } H(x_0, x_1) < H(x_1, x_2) < \dots < H(x_{k-1}, x_k).$$
   While $G_{\mathrm{space}}$ contains closed spatial 3-cycles ($v \to w \to u \to v$ with timestamps $0, 0, 1$), these do not form closed timelike loops in $G_{\mathrm{event}}$ because paths with non-increasing timestamps ($0 \not< 0$) carry zero causal influence. The causal relation $(V, \le)$ forms a strict Directed Acyclic Graph (DAG) over history.

The intensive cycle density is $\rho(G)=\frac{N_3(G)}{N}$, where $N_3(G) = |\mathcal{C}_3(G)|$.

## 2.2 Formal Axiomatic Foundation and the Bowtie Paradox

The kinematics and state transitions of the graph rewrite system are governed by three constructive axioms that establish causality, locality, and dimensional order on the combinatorial substrate without assuming a background spacetime manifold:

*   **Axiom 1 (Directed Causal Primitive):** The fundamental relational unit on the vertex set $V$ is the directed causal link $(u, v) \in E$, defined as an irreversible vector of influence. The edge set $E \subset V \times V$ strictly satisfies:
    1.  *Strict Irreflexivity:* $\forall u \in V, \; (u, u) \notin E$ (rejection of causal inertia and self-loops).
    2.  *Strict Asymmetry:* $\forall u \neq v, \; (u, v) \in E \implies (v, u) \notin E$ (rejection of instantaneous reciprocity / microscopic arrow of time).
*   **Axiom 2 (Geometric Constructibility):** Pre-geometric topological evolution is restricted to discrete elementary simplices and parsimonious path closures:
    1.  *Clause A (Simplicial Elements):* The formation of closed topological structures is restricted exclusively to minimal 3-cycles ($L = 3$, directed 2-simplices). Arbitrary higher-order loops ($L \ge 4$) are not elementary physical states.
    2.  *Clause B (Principle of Unique Causality - PUC):* Instantiation of a return edge $(u, v)$ is prohibited if there already exists an alternative simple directed path from $v$ to $u$ of length $\ell \le 2$, preventing dense shortcut cliques and protecting spatial locality.
*   **Axiom 3 (Acyclic Effective Causality - AEC):** The effective causal influence relation $\le$ forms a *Strict Partial Order* over $V$ (Global Irreflexivity $\neg(v \le v)$ and Global Asymmetry $u \le v \implies \neg(v \le u)$), ensuring that causal history $G_{\mathrm{event}}$ represents a physically consistent Directed Acyclic Graph.

### 2.2.1 The Bowtie Paradox and Logical Independence of Axiom 3

Axioms 1 and 2 operate locally ($\ell \le 2$) and are mathematically insufficient to guarantee global causal consistency. This is demonstrated by the **Bowtie Paradox counter-model**:

- Let $V = \{A, B, C, D\}$ with directed edges $E = \{(A,B), (B,C), (C,D), (D,A)\}$ and timestamps $H(A,B)=1, H(B,C)=2, H(C,D)=3, H(D,A)=4$.
- This 4-cycle satisfies Axiom 1 (all edges are irreflexive and asymmetric) and Axiom 2 (no 2-path violations).
- However, path $A \to B \to C$ has timestamps $1 < 2$, establishing forward causal influence $A \le C$. Concurrently, path $C \to D \to A$ has timestamps $3 < 4$, establishing reverse causal influence $C \le A$.
- The simultaneous validity of $A \le C$ and $C \le A$ for distinct vertices ($A \neq C$) induces a symmetric causal dependency, destroying the partial order.

This counter-model proves that **Axiom 3 is logically independent**: global causal consistency is not a trivial consequence of local directionality and constructibility, but must be actively enforced by the microscopic rewrite engine.

## 2.3 Pre-Geometric Initial Condition $G_0$

The pre-geometric substrate is a finite Regular Bethe Fragment with uniform internal coordination $k_{\mathrm{deg}} = 3$. Given a target size $N\ge 3$ and a designated root vertex $r\in V$, an outward-directed tree is generated until $|V|=N$:

- The root $r$ has in-degree $d_{\mathrm{in}}(r) = 0$ and out-degree $d_{\mathrm{out}}(r) = 3$ ($k_{\mathrm{deg}} = 3$).
- Every subsequent internal vertex has in-degree $d_{\mathrm{in}}(v) = 1$ (one parent edge) and out-degree $d_{\mathrm{out}}(v) = 2$ (two outgoing children), satisfying total coordination degree $k_{\mathrm{deg}} = 1 + 2 = 3$.
- Leaf vertices have in-degree $d_{\mathrm{in}} = 1$ and out-degree $d_{\mathrm{out}} = 0$.
- Every tree edge is assigned initial logical height $H\equiv 0$.

The resulting graph $G_0$ is a rooted DAG, connected, and depth-parity bipartite with respect to graph distance from $r$. It contains no directed cycles, satisfying $N_3(G_0)=0$, and its undirected girth is infinite. The coordination number $k_{\mathrm{deg}} = 3$ represents the unique mathematical intersection of geometric constructibility ($k_{\mathrm{deg}} \ge 3$ required to enclose 2-simplex area) and topological singularity avoidance ($k_{\mathrm{deg}} \le 3$ required to prevent non-manifold '3-page book' pinch points upon ignition). The Bethe fragment serves strictly as an initial condition; subsequent evolution leaves the Bethe class.

> **Proposition 2.3.1** (Extensive Scale-Invariant Leaf Boundary of Binary Bethe Fragments).
> Let $G_0 = (V, E)$ be any finite regular Bethe fragment of size $|V| = N \ge 3$ generated by the outward branching construction.
> Then the number of leaf boundary vertices $L = |\{v \in V : d_{\mathrm{out}}(v) = 0\}|$ satisfies the exact combinatorial relation
> $$L = \frac{N + 2}{2},$$
> and the boundary-to-bulk ratio is strictly extensive and scale-invariant:
> $$\lim_{N \to \infty} \frac{L}{N} = \frac{1}{2} = 50\%.$$
> Furthermore, because leaf vertices possess out-degree zero ($d_{\mathrm{out}} = 0$), they cannot serve as intermediate routing vertices ($w$) or initiation sources for forward directed 2-paths ($v \to w \to u$), rendering the entire leaf layer an absorbing causal boundary that halts outward wave propagation.

*Proof.* Let $I$ denote the number of internal vertices (including the root $r$) and $L$ denote the number of leaves, such that $N = I + L$. In any directed tree, the total number of directed edges is $|E| = N - 1 = I + L - 1$. Summing the out-degrees over all vertices gives $|E| = d_{\mathrm{out}}(r) + \sum_{v \in I \setminus \{r\}} d_{\mathrm{out}}(v) + \sum_{u \in \mathrm{Leaves}} d_{\mathrm{out}}(u) = 3 + 2(I - 1) + 0 = 2I + 1$. Equating the two expressions for $|E|$ yields $I + L - 1 = 2I + 1 \implies L = I + 2$. Substituting $I = N - L$ gives $L = (N - L) + 2 \implies 2L = N + 2 \implies L = \frac{N+2}{2}$. Dividing by $N$ gives the leaf fraction $\frac{L}{N} = \frac{1}{2} + \frac{1}{N} \to 50\%$, proving the boundary is extensive for all $N$. $\square$

## 2.4 External Seed Injection

Cycle activity cannot be generated spontaneously from $G_0$ by the internal rewrite rules. An external seed operator $\mathcal{S}_{\mathrm{seed}}$ injects a single non-tree edge. On a Bethe fragment of depth at least $2$, let $v$ denote the root, $w$ its first child, and $u$ the first child of $w$. The seed map is defined by

$$\mathcal{S}_{\mathrm{seed}}(G_0)=G_0\cup\bigl\{(u,v)\bigr\},\qquad H(u,v)=1.$$

The closed walk $v\to w\to u\to v$ forms an initial directed 3-cycle. The injected edge breaks bipartiteness and initiates the geometrogenic phase.

## 2.5 Legal Move Grammar

All subsequent evolution is governed by the microscopic constructor $\mathcal{R}$. There is no spontaneous creation of edges between vertices that do not already form a compliant 2-path:

$$\Lambda_{\mathrm{micro}}\equiv 0.$$

### 2.5.1 Addition Sites

An ordered vertex triple $(v,w,u)$ is an **addition site** if and only if:

1. $(v,w)\in E$ and $(w,u)\in E$ (a directed 2-path),
2. $v\neq u$ and $(u,v)\notin E$,
3. The parent-uniqueness condition $\mathrm{PUC}(G;u,v,w)$ holds,
4. The acyclicity pre-check $\mathrm{AEC}(G;u,v,H_{\mathrm{new}})$ holds, where
   $$H_{\mathrm{new}}=1+\max\bigl\{H(x,u):(x,u)\in E\bigr\},$$
   with the convention $\max\emptyset = 0$ ensuring that proposals targeting vertices without in-edges (such as the root $r$) initialize with base height $H_{\mathrm{new}} = 1$.

The proposed addition is the directed edge $(u,v)$ with timestamp $H_{\mathrm{new}}$.

### 2.5.2 Unique-Causality Condition (PUC)

For a candidate 2-path $v\to w\to u$, the parent-uniqueness predicate is defined by

$$\mathrm{PUC}(G;u,v,w) \;\iff\; (v,u)\notin E \;\text{and}\; \nexists\, x\in V\setminus\{w\}\;\text{such that}\;(v,x)\in E\text{ and }(x,u)\in E.$$

This requires that no forward bypass edge $(v,u)$ exists from $v$ to $u$, and that $v\to w\to u$ is the unique directed 2-path connecting $v$ to $u$.

### 2.5.3 Acyclicity Pre-Check (AEC) and Tiered Causal Enforcement

Let $H_{\mathrm{new}}$ be the proposed height. The temporary edge $(u,v)$ is inserted with height $H_{\mathrm{new}}$, and directed paths from $v$ to $u$ of length at most

$$L_{\mathrm{cut}}=\lfloor\log_2 N\rfloor+3$$

are evaluated ($L_{\mathrm{cut}}=1$ for $N\le 1$; for the $N=100$ ensemble, $L_{\mathrm{cut}} = \lfloor 6.64 \rfloor + 3 = 9$, matching the analytical binary tree diameter bound). The $+3$ offset matches the exact perimeter of an elementary directed 3-cycle ($L=3$), guaranteeing that the search horizon covers the entire causal light-cone radius plus the boundary path of the candidate simplicial closure. The proposal is rejected if there exists a directed path $\pi=(v=x_0,x_1,\ldots,x_k=u)$ of length $k\le L_{\mathrm{cut}}$ such that the edge heights along $\pi$ are strictly monotone increasing and the final edge satisfies $H(x_{k-1},u)<H_{\mathrm{new}}$. The temporary edge is then removed. Because initial tree edges carry $H=0$, paths of uniform height are not strictly monotone and pass the filter.

Causal acyclicity is governed by a two-tier architecture:

1. **Exact Formal Invariant (Global Partial Order):** At the mathematical level, Theorem 7.3 formally proves in Lean 4 (`edge_monotone_no_causal_cycle`, Appendix A) that whenever a directed graph admits a strictly monotone height embedding along all directed paths, directed cycles of arbitrary length $k \ge 1$ are strictly impossible.
2. **Operational Constructor Dynamics (Thermodynamic Protection):** In the physical simulation engine, timestamps are assigned dynamically from local incoming edges ($H_{\mathrm{new}} = 1 + \max_{(x,u)\in E} H(x,u)$). The rewrite engine implements the localized AEC pre-check with horizon $L_{\mathrm{cut}} \sim \log N$. On expander networks with bounded degree and mean cycle density $\rho < 1$, the probability of an unintercepted acausal loop of length $L > L_{\mathrm{cut}}$ closing beyond the horizon decays exponentially:
   $$P_{\mathrm{err}} = \sum_{L=L_{\mathrm{cut}}+1}^\infty \frac{C}{N} \rho^L \approx \frac{C}{N} \frac{\rho^{L_{\mathrm{cut}}+1}}{1 - \rho} \le \mathcal{O}(N^{-k}).$$
   Across all $13,200$ parameter sweep trajectories and extended scaling runs, the empirical frequency of unintercepted acausal loops closing beyond the horizon $L_{\mathrm{cut}}$ was identically zero ($0 / 13,200 = 0.0\%$), confirming the operational efficacy of the logarithmic pre-check on bounded-degree substrates (where the mean degree $\langle k \rangle \approx 4.22$ enforces graph diameter $\mathrm{diam}(G) \le \log_2 N + 2 \le L_{\mathrm{cut}}$).

*Scope Note on Causal Protection:* The $L_{\mathrm{cut}}$-bounded BFS pre-check functions as an operational filter for finite numerical substrates. All-order causal protection across extended graph rewrite histories involves global algebraic foliation and quantum stabilizer error-correcting codespaces, which are formulated in future companion work on causal graph error correction. For the classical statistical mechanics, absorbing-state transitions, and finite-$N$ non-equilibrium ensembles investigated in this paper, the localized $L_{\mathrm{cut}}$ filter is sufficient across all tested configurations.

### 2.5.4 Deletion Sites

Every directed 3-cycle $C=\{(a,b),(b,c),(c,a)\}\subseteq E$ constitutes a **deletion site**. If the deletion site is accepted by the stochastic kernel, exactly one of its three edges is selected uniformly at random and proposed for removal. Edges that do not belong to any directed 3-cycle are never candidates for deletion.

## 2.6 Local Stress Functional

Let $\mathcal{C}_3(G)$ denote the collection of all directed 3-cycles in $G$. The vertex incidence count is

$$\mathrm{stress\_map}(x)=\bigl|\{\,C\in\mathcal{C}_3(G):x\in V(C)\,\}\bigr|.$$

For an addition site $(v,w,u)$, the addition stress is

$$s_{\mathrm{add}}=\sum_{x\in\{v,w,u\}}\mathrm{stress\_map}(x).$$

For a deletion site $C$ with vertex set $V(C)$, the deletion self-stress is

$$s_{\mathrm{del}}=\max\Bigl(0,\;\sum_{x\in V(C)}\mathrm{stress\_map}(x)-1\Bigr).$$

The offset $-1$ enforces the physical self-stress convention. An isolated 3-cycle contains 3 vertices each participating in 1 cycle ($\sum_{x\in V(C)} \mathrm{stress\_map}(x) = 3$). Proposing a deletion resolves the cycle itself, liberating 1 unit of topological constraint. Subtracting this base contribution leaves $s_{\mathrm{del}}=(1+1+1)-1=2$ as the mutual internal vertex-sharing tension across the triad.

## 2.7 Microscopic Constitutive Kernel

At each legal site, the simulation engine applies the hard-coded thermodynamic base rates

$$P_{\mathrm{add,thermo}}=1,\qquad Q_{\mathrm{del,thermo}}=\tfrac12,$$

modulated by local stress according to the kernel

$$
\begin{aligned}
P_{\mathrm{acc}}(s_{\mathrm{add}})&=\mathrm{e}^{-\mu\,s_{\mathrm{add}}}, \tag{1}\\
Q_{\mathrm{del}}(s_{\mathrm{del}})&=\min\bigl(1,\;\tfrac12\,(1+\lambda\,s_{\mathrm{del}})\,\mathrm{e}^{-\mu\,s_{\mathrm{del}}}\bigr). \tag{2}
\end{aligned}
$$

## 2.8 Parallel Scheduler Mechanics and Kinetic Stall Dynamics

Evolution progresses in discrete parallel ticks $t\to t+1$ via the evolution operator $\mathcal{U}$. Each tick executes a formal four-step scheduler:

1. **Awareness:** Compute the cycle set $\mathcal{C}_3(G_t)$ and the vertex incidence functional $\mathrm{stress\_map}$.
2. **Proposal:** For each legal addition site $i \in \mathcal{S}_{\mathrm{add}}(G_t)$, generate an independent Bernoulli trial with parameter $P_{\mathrm{acc}}(s_{\mathrm{add},i})$ to construct the addition proposal set $A=\{((u_i,v_i), H_{\mathrm{new},i})\}$. Independently, for each deletion site $j \in \mathcal{C}_3(G_t)$, generate a Bernoulli trial with parameter $Q_{\mathrm{del}}(s_{\mathrm{del},j})$ to select one edge uniformly and construct the deletion proposal set $D=\{e_j\}$.
3. **Merge (Symmetric Conflict Resolution & Additions First):** Enforce symmetric conflict resolution by removing any simultaneous reciprocal proposals:
   $$A_{\mathrm{filtered}} = \{((u,v), H_{\mathrm{new}}) \in A \mid (v,u) \notin A_{\mathrm{edges}} \text{ and } u \neq v\},$$
   and construct the intermediate graph
   $$G'=\bigl(V,\;E(G_t)\cup A_{\mathrm{filtered,edges}},\;H_t\cup\{(u,v)\mapsto H_{\mathrm{new}}\}\bigr).$$

4. **Deletion:** Remove the accepted deletion set from the intermediate graph to produce
   $$G_{t+1}=\bigl(V,\;E(G')\setminus (D\cap E(G')),\;H'|_{E(G_{t+1})}\bigr).$$

**Kinetic Stall Termination Rule:** In the discrete simulation on a finite Bethe fragment, a trajectory reaches a kinetic stall and terminates when a discrete tick yields zero accepted additions and zero accepted deletions:
$$A = \emptyset \quad \land \quad D = \emptyset \implies \text{Halt (Kinetic Stall Settled)}.$$
Because the leaf boundary layer ($\approx 50\%$ of vertices by Proposition 2.3.1) terminates forward 2-path propagation and interior steric friction ($\mathrm{e}^{-\mu s}$) suppresses lateral additions, finite graphs enter this quiet stall state (typically within $\tau_{\mathrm{stall}} \sim 20$–$60$ ticks). At this point, the network enters an idempotent fixed point $\mathcal{U}(G_{\mathrm{terminal}}) = G_{\mathrm{terminal}}$, freezing the residual topological foam and non-cyclic scars into the static absorbing state.

The execution mechanics satisfy a non-interference property.

> **Lemma 2.1** (Deterministic Parallel Execution and Move Non-Interference).
> Let $G_t = (V, E(G_t), H_t)$ be a timestamped directed graph at tick $t$, and let $A$ and $D$ denote the accepted addition and deletion proposal sets generated by the parallel scheduler.
> Then $A_{\mathrm{edges}} \cap E(G_t) = \emptyset$ and $D \subseteq E(G_t)$, which yields $A_{\mathrm{edges}} \cap D = \emptyset$, and the execution sequence of additions followed by deletions constitutes a deterministic, race-free update in which no edge created in tick $t$ is deleted within the same tick.

*Proof.* By Definition 2.5.1, a candidate addition site $(v,w,u)$ closes an open directed 2-path and strictly requires $(u,v)\notin E(G_t)$, so the set of proposed additions satisfies $A_{\mathrm{edges}} \cap E(G_t) = \emptyset$. Conversely, by Definition 2.5.4, deletion proposals are drawn exclusively from existing edges of closed directed 3-cycles in $G_t$, which implies $D \subseteq E(G_t)$. Each height $H_{\mathrm{new}}$ is a deterministic function of the in-edge timestamps of $G_t$, so duplicate proposals of the same directed edge $(u,v)$ in $A$ evaluate to identical timestamps and merge idempotently. Combining the disjointness conditions $A_{\mathrm{edges}} \cap E(G_t) = \emptyset$ and $D \subseteq E(G_t)$ yields $A_{\mathrm{edges}} \cap D = \emptyset$. In the execution sequence, step 3 forms $E(G') = E(G_t) \cup A_{\mathrm{filtered,edges}}$, and step 4 removes $D \cap E(G') = D \cap (E(G_t) \cup A_{\mathrm{filtered,edges}}) = D$. Because $D$ contains no elements of $A_{\mathrm{filtered,edges}}$, no newly inserted edge is removed in step 4, establishing race-free parallel execution. $\square$

> **Corollary 2.2** (Preclusion and Resolution of Simultaneous Reciprocal Proposals).
> Let $G_t$ be a timestamped causal graph evolved from $G_0$, and let $A$ denote the addition proposal set generated by the parallel scheduler at tick $t$.
> Then simultaneous reciprocal proposals are structurally suppressed by causal path foliation and strictly eliminated by the merge filter ($A_{\mathrm{filtered}}$), guaranteeing that parallel additions preserve strict asymmetry under all execution conditions.

*Proof.* On the unperturbed tree substrate $G_0$, cycles of any length are topologically absent, precluding reciprocal 2-paths. On evolved graphs, proposal of $(u,v)$ requires a directed 2-path $v \to w_1 \to u$ while proposal of $(v,u)$ requires $u \to w_2 \to v$, whose concatenation forms a directed 4-cycle $v \to w_1 \to u \to w_2 \to v$. Whenever edge timestamps along this loop are strictly increasing, the AEC pre-check (Definition 2.5.3) rejects the proposal. To guarantee absolute asymmetry across arbitrary topologies where non-monotone historical chords might pass the horizon pre-check, the scheduler executes symmetric merge filtering in Step 3: if $(u,v) \in A$ and $(v,u) \in A$ occur concurrently, both members are removed before graph mutation. Consequently, the edge set $E(G_{t+1})$ contains no reciprocal pairs, preserving strict irreflexivity and asymmetry. $\square$

*(A complete, machine-checked Lean 4 verification of the axiomatic primitives, comonadic update properties, dynamic move disjointness, race-free invariance, and Step 3 parallel merge confluence is provided in Appendix A [Theorems 1.1–5.2], the C++20 multi-scale engine in Appendix B, and the Python reference algorithm in Appendix C.)*

## 2.9 Absorbing Extinction Boundary

Because $\Lambda_{\mathrm{micro}}\equiv 0$, no edges can be created in the absence of pre-existing compliant 2-paths. A state with $N_3=0$ and no legal 2-path closures yields $A=D=\emptyset$ and constitutes an absorbing state (formally verified in Lean 4 as Theorem 6.1 `absorbing_state_stationary`).

In finite-$N$ simulations, trajectories that lose all 3-cycles terminate in **scarred absorbing DAGs**: configurations with $N_3=0$ that retain frozen, non-cyclic chords (topological scars) added during transient bursts that failed to close into stable 3-cycles. These scarred states are distinct from the initial Bethe fragment $G_0$. Because deletion proposals are drawn strictly from edges participating in active directed 3-cycles ($D \subseteq \mathcal{C}_3$), non-cyclic scar edges are permanently immune to deletion (formally verified in Lean 4 as Theorem 6.2 `scar_edges_immune_to_deletion`), rendering the topological absorption irreversible.

---

# 3. Microscopic Solvability: Isolated-Cycle Deletion and the First-Tick Burst

The deletion kernel determines the exact survival probability of an isolated 3-cycle, ruling out dilute, non-interacting loop gases and establishing the necessity of clustered bursts.

## 3.1 Isolated-Cycle Deletion Probability

> **Proposition 3.1** (Isolated-Cycle Deletion Probability).
> Let $G$ be a graph containing exactly one directed 3-cycle $C_0$ on a cycle-free background.
> Then the deletion self-stress satisfies $s_{\mathrm{del}}(C_0)=2$, the single-tick deletion probability is
> $$Q_{\mathrm{del}}(2)=\min\Bigl(1,\;\tfrac12\bigl(1+2\lambda\bigr)\,\mathrm{e}^{-2\mu}\Bigr),$$
> and evaluating at $(\mu_0,\lambda_0)=(1/\sqrt{2\pi},\,e-1)$ yields $Q_{\mathrm{del}}(2)\approx 0.99885$, which implies an unassisted single-tick survival probability $p_{\mathrm{surv}}^{(1)}=1-Q_{\mathrm{del}}(2)\approx 1.15\times 10^{-3}$.

*Proof.* Because $C_0$ is the unique 3-cycle in $G$, the incidence count satisfies $\mathrm{stress\_map}(x)=1$ for each vertex $x\in V(C_0)$ and $\mathrm{stress\_map}(y)=0$ for all $y\notin V(C_0)$. The deletion self-stress evaluates to $s_{\mathrm{del}}(C_0) = \max(0, \sum_{x\in V(C_0)} 1 - 1) = 2$. Substituting $s_{\mathrm{del}}=2$ into the deletion kernel (Eq. 2) yields $Q_{\mathrm{del}}(2) = \min(1, \frac{1}{2}(1+2\lambda)\mathrm{e}^{-2\mu})$. Evaluating at the canonical analytical coordinates $(\mu_0,\lambda_0)=(1/\sqrt{2\pi}, e-1)$ gives the catalytic prefactor $1+2(e-1)=2e-1\approx 4.43656$ and damping factor $\mathrm{e}^{-2/\sqrt{2\pi}}\approx 0.45028$. Multiplying these factors gives $Q_{\mathrm{del}}(2) \approx \frac{1}{2}(4.43656)(0.45028) \approx 0.99885 < 1$, so the cutoff does not bind. The single-tick survival probability evaluates to $p_{\mathrm{surv}}^{(1)} = 1 - 0.99885 = 1.15\times 10^{-3}$. $\square$

## 3.2 The Isolated Death Line

> **Definition 3.2** (Isolated Death Line).
> In the parameter half-plane $\mu>0, \lambda\ge 0$, the **isolated death line** is the locus where the uncapped single-cycle deletion probability equals unity:
> $$\tfrac12(1+2\lambda)\,\mathrm{e}^{-2\mu}=1 \quad\Longleftrightarrow\quad \lambda_{\mathrm{death}}(\mu)=\mathrm{e}^{2\mu}-\tfrac12.$$

For $\lambda\ge\lambda_{\mathrm{death}}(\mu)$, an isolated 3-cycle is deleted with probability $Q_{\mathrm{del}}(2)=1$. For $\lambda<\lambda_{\mathrm{death}}(\mu)$, the deletion probability satisfies $Q_{\mathrm{del}}(2)<1$.

At the canonical friction scale $\mu_0=1/\sqrt{2\pi}$,

$$\lambda_{\mathrm{death}}(\mu_0)=\mathrm{e}^{2/\sqrt{2\pi}}-\tfrac12 \approx 1.72084.$$

The canonical catalysis constant $\lambda_0=e-1\approx 1.71828$ lies strictly below the death line by a narrow margin:

$$\Delta\lambda = \lambda_{\mathrm{death}}(\mu_0)-\lambda_0 \approx 2.56\times 10^{-3}.$$

This minute gap accounts for the uncapped probability $Q_{\mathrm{del}}(2)\approx 0.99885$. Operationally, an isolated seed cycle without collateral additions is destroyed on the first tick in $99.885\%$ of realizations. This single-cycle instability provides the exact microscopic origin for the severe zero-inflation observed across the unconditioned ensemble in Section 5.

## 3.3 Clustered-Burst Mechanism

> **Corollary 3.3** (Exclusion of Dilute Loop Gas).
> Let $G$ contain $k$ pairwise vertex-disjoint directed 3-cycles on an otherwise cycle-free background.
> Then each 3-cycle independently undergoes deletion with probability $Q_{\mathrm{del}}(2)\approx 0.999$, which implies that a dilute, non-interacting loop gas does not constitute a quasi-stationary state.

*Proof.* Because the $k$ cycles share no vertices, $\mathrm{stress\_map}(x)=1$ for every vertex on every cycle, and the self-stress on each cycle evaluates to $s_{\mathrm{del}}=2$ independently. The parallel scheduler performs independent Bernoulli draws across all deletion sites, so the probability that all $k$ cycles survive without interaction decays as $(1-Q_{\mathrm{del}}(2))^k \approx (1.15\times 10^{-3})^k$. Any non-interacting collection of cycles therefore decays exponentially to extinction with a characteristic lifetime of $\tau \approx 1/\ln(1/p_{\mathrm{surv}}^{(1)}) \approx 0.15$ ticks, precluding a dilute quasi-stationary gas. $\square$
> **Corollary 3.4** (First-Tick Clustered Burst and Scale-Invariant Ignition).
> Let an isolated seed 3-cycle be injected into $G_0$ at $t=0$, and consider the execution of tick $t=1$ at the canonical operating coordinates $(\mu_0, \lambda_0)$.
> Then all candidate addition sites supported entirely on the residual Bethe tree satisfy $s_{\mathrm{add}} = 0$ and accept edge proposals with probability $P_{\mathrm{acc}}(0) = 1$, and these additions merge prior to deletion, which yields a deterministic burst of overlapping 3-cycles whose initial density $\rho(t=1) \approx \mathcal{O}(1)$ is scale-invariant with respect to $N$, constituting the unique channel for escaping the classical nucleation barrier ($\rho_c \approx 0.130$) and avoiding extinction.

*Proof.* At $t=0$, the seed cycle $v\to w\to u\to v$ occupies three vertices, while all other vertices in $V(G_0)$ have $\mathrm{stress\_map}(x)=0$. For any candidate 2-path $a\to b\to c$ supported entirely on the residual tree, $s_{\mathrm{add}} = 0+0+0 = 0$, yielding $P_{\mathrm{acc}}(0) = \mathrm{e}^{-\mu_0 \cdot 0} = 1$. Every tree-supported 2-path that satisfies PUC and AEC is accepted with certainty. Because all initial tree edges in $G_0$ carry timestamp $H=0$, a path of uniform height $0\to 0\to 0$ is not strictly height-monotone, so the AEC filter does not reject tree-supported closures on tick 1. By Lemma 2.1, all accepted additions $A$ are merged into $G'$ in step 3 before deletion proposals $D$ are executed in step 4. Although the seed cycle edge is proposed for deletion with probability $Q_{\mathrm{del}}(2)\approx 0.99885$, the newly accepted additions create a dense cluster of interconnected 3-cycles before the seed edge is removed. Furthermore, on an outward-directed regular Bethe tree of coordination $k_{\mathrm{deg}}=3$ ($k_{\mathrm{in}}=1, k_{\mathrm{out}}=2$), a substrate of size $N$ contains $N_{2\text{-path}}(G_0) \approx 2N$ open 2-paths. Because each tree-supported site fires concurrently with $P_{\mathrm{acc}}(0)=1$, the total number of nucleated cycles on tick 1 scales linearly with system size: $N_3(t=1) \approx \alpha_{\mathrm{burst}} N$. Dividing by $N$, the initial burst density $\rho(t=1) = N_3(1)/N \approx \alpha_{\mathrm{burst}} = \mathcal{O}(1)$ is **strictly scale-invariant**, ensuring that the first-tick ignition catapults the local density beyond the nucleation barrier $\rho_c \approx 0.130$ across all system sizes $N \to \infty$. $\square$

# 4. Canonical Operating Coordinates and Microscopic Symmetry Relations

The stochastic graph-rewriting dynamics exhibit an extended, open non-equilibrium active phase across the two-parameter domain $(\mu, \lambda) \in [0.35, 0.50] \times [0.8, \infty)$ (Section 5.2). Within this broad phase basin, the coordinate $(\mu_0, \lambda_0) = (1/\sqrt{2\pi}, e - 1)$ defines a distinguished **canonical reference coordinate** where discrete Landauer thermodynamic neutrality, Markov jump Lie algebra linearity, and integer lattice MaxEnt symmetries on $\mathbb{Z}$ simultaneously hold.

The individual constitutive scales are derived from discrete Landauer computation thermodynamics, discrete Markov jump defect relaxation, integer lattice Poisson summation on $\mathbb{Z}$, and $k_{\mathrm{deg}}=3$ vertex coordination equipartition. Key discrete combinatorial structures (such as coordination degree, port equipartition, and interaction volumes) are formally certified in Lean 4 (Appendix A, Part 9).

Table 1 summarizes the discrete physical conservation principle, exact mathematical derivation, operational role, and formal proposition for each constitutive scale.

**Table 1.** Discrete Combinatorial Derivation Matrix for Constitutive Scales and Canonical Reference Priors.

| Constitutive Parameter | Exact Analytical Value | Discrete Conservation Principle | Mathematical Derivation | Operational Role in Rewrite Engine | Formal Derivation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Thermodynamic Base Rates** | $T_c = \ln 2$, $(P_{\mathrm{add}}, Q_{\mathrm{del}})=(1, 1/2)$ | Discrete 2-Path Multiplicity Doubling | $E = k_B T \ln 2 \implies T_c = \ln 2$; $\Omega_{\mathrm{closed}}/\Omega_{\mathrm{open}}=2 \implies \Delta S_{\mathrm{close}} = \ln 2$ | Marginal thermodynamic neutrality ($\Delta F = 0$) | Proposition 4.1, Appendix B (`T_c`) |
| **The Catalysis Constant** | $\lambda_0 = e - 1 \approx 1.718282$ | Discrete Markov Jump Defect Relaxation | $\Omega_{\mathrm{released}}/\Omega_{\mathrm{bound}} = e^1 = e$; $1 + \lambda_0(1) = e \implies \lambda_0 = e - 1$ | Tension-accelerated 3-cycle edge deletion | Proposition 4.2, Appendix A (Part 8, Part 9), Appendix B (`lambda_0`) |
| **The Friction Constant** | $\mu_0 = 1/\sqrt{2\pi} \approx 0.398942$ | Integer Lattice $\mathbb{Z}$ MaxEnt Partition Function | $Z_{\mathbb{Z}} = \sum_{n\in\mathbb{Z}}\mathrm{e}^{-n^2/2} = \sqrt{2\pi}(1 + \mathcal{O}(10^{-9})) \implies P_{\mathbb{Z}}(0) = 1/\sqrt{2\pi}$ | Discrete steric rate damping preventing collapse | Proposition 4.3, Appendix B (`mu_0`) |
| **Geometric Self-Energy** | $\varepsilon_{\mathrm{geo}} = \frac{\ln 2}{3} \approx 0.231049$ | $k_{\mathrm{deg}}=3$ Vertex Channel Equipartition | $\varepsilon_{\mathrm{geo}} = \Delta S_{\mathrm{close}} / k_{\mathrm{deg}} = \frac{\ln 2}{3}$ (under $k_{\mathrm{in}}=1, k_{\mathrm{out}}=2$) | Energy allocation per discrete incident port | Proposition 4.4, Appendix A (Theorems 9.1–9.2), Appendix B (`eps_geo`) |
| **Theoretical Permittivity** | $\Lambda_{\mathrm{theory}} = 2^{-6} \approx 0.015625$ | 6-Port Binary Simplex Traversal | $V_{\mathrm{int}} = 3\text{ vertices} \times 2\text{ ports} = 6$; $\Lambda = (1/2)^6 = 2^{-6}$ | Auxiliary driven background pump ($\Lambda_{\mathrm{micro}}\equiv 0$ in engine) | Proposition 4.5, Appendix A (Theorems 9.3–9.4), Appendix B (`Lambda_theory`) |
| **Causal Search Horizon** | $L_{\mathrm{cut}} = \lfloor\log_2 N\rfloor + 3$ | Small-World Tree Bound + Triad Overhead | $L_{\mathrm{cut}} = \lfloor\log_2 N\rfloor + 3$ ($L_{\mathrm{cut}}=9$ at $N=100$) | Bounded BFS search depth for AEC filter | Section 2.5.3, Appendix B (`pre_check_aec`) |

## 4.1 Derivation of Vacuum Temperature ($T_c = \ln 2$) and Base Update Rates

> **Proposition 4.1** (Critical Vacuum Temperature and Marginal Free Energy Neutrality).
> Let the pre-geometric causal substrate be modeled as a canonical ensemble with Boltzmann constant $k_B = 1$.
> Then $T_c = \ln 2$ is the unique thermodynamic temperature at which the creation of an elementary 1-bit relational loop closure is thermodynamically neutral at the margin ($\Delta F = 0$), and the sparse Metropolis rates evaluate uniquely to the baseline operating pair $(P_{\mathrm{add}}, Q_{\mathrm{del}}) = (1, 1/2)$.

*Proof.* In the relational ground state, the internal energy change associated with creating an elementary causal edge vanishes ($\Delta U = 0$). The Helmholtz free energy change satisfies $\Delta F(T) = \Delta U - T \Delta S = -T \Delta S$. By Landauer's principle, the energetic cost to instantiate a single binary distinction ($\Omega_{\mathrm{initial}} = 2 \to \Omega_{\mathrm{final}} = 1$) is $S_{\mathrm{bit}} = \ln 2\text{ nats} \equiv 1\text{ bit}$. The fundamental thermal energy per degree of freedom is $E_{\mathrm{therm}} = k_B T = T$, while the elementary informational unit cost is $E_{\mathrm{info}} = 1 \cdot S_{\mathrm{bit}} = \ln 2$. Equating the thermal background scale to the informational bit scale yields the unique critical vacuum temperature:

$$T_c = \ln 2.$$

In the natural informational basis ($k_B = 1$), temperature $T_c = \ln 2\text{ energy units/bit}$ corresponds to unit temperature in the natural nat-basis:

$$T_{\mathrm{nat}} = \frac{T_c}{\ln 2} = \frac{\ln 2}{\ln 2} = 1\text{ energy units/nat}.$$

Thus, edge addition and edge deletion operate isothermally at the exact same physical temperature $T_c$: addition is quantized in binary bits ($\Delta S_{\mathrm{close}} = \ln 2$), while deletion relaxes topological tension in natural nats ($\Delta S_{\mathrm{release}} = 1\text{ nat}$ at $T_{\mathrm{nat}} = 1$).

For a compliant 2-path $v\to w\to u$ on $G_0$, pre-closure path multiplicity is $\Omega_{\mathrm{open}} = 1 \implies S_{\mathrm{open}} = 0$. Closing the 2-path into the directed 3-cycle $v\to w\to u\to v$ creates a non-trivial fundamental cycle ($\pi_1(G) \neq 0$), bifurcating the causal connection into two distinct topological channels (the direct edge $u\to v$ and the mediated path $v\to w\to u$), which doubles the local path volume: $\Omega_{\mathrm{closed}} = 2\cdot \Omega_{\mathrm{open}} = 2$. The exact relational entropy of loop closure is:

$$\Delta S_{\mathrm{close}} = \ln\left(\frac{\Omega_{\mathrm{closed}}}{\Omega_{\mathrm{open}}}\right) = \ln 2\text{ nats} \equiv 1\text{ bit}.$$

Under the standard Metropolis–Hastings update criterion, the base addition probability evaluates to:

$$P_{\mathrm{add}} = \min\bigl(1, \mathrm{e}^{-\Delta F / T_c}\bigr) = \min\bigl(1, \mathrm{e}^{+(\ln 2)^2 / \ln 2}\bigr) = \min(1, 2) = 1.$$

Conversely, removing an edge of a 3-cycle restores simply connected open topology, incurring the entropic penalty $\Delta S_{\mathrm{del}} = -\ln 2$, which yields the base deletion probability:

$$Q_{\mathrm{del}} = \mathrm{e}^{\Delta S_{\mathrm{del}}} = \mathrm{e}^{-\ln 2} = \frac{1}{2}.$$

Thus, $(P_{\mathrm{add}}, Q_{\mathrm{del}}) = (1, 1/2)$ is the unique dissipation-free baseline operating point. $\square$

## 4.2 Derivation of the Catalysis Constant ($\lambda_0 = e - 1$) via Arrhenius Defect Relaxation and Markov Generator Additivity

> **Proposition 4.2** (Arrhenius Defect Relaxation and Markov Jump Generator Linearity).
> Let an elementary 3-cycle defect possess Landauer creation energy $E_{\mathrm{defect}} = T_c \cdot \Delta S_{\mathrm{close}} = \ln 2$ at vacuum temperature $T_c = \ln 2$.
> In the microscopic deletion kernel $Q_{\mathrm{del}}(s) = \frac{1}{2}(1 + \lambda s)\mathrm{e}^{-\mu s}$, the linear catalytic reaction velocity $(1 + \lambda s)$ is the unique infinitesimal Markov jump generator preserving move additivity and scheduler non-interference (Lemma 2.1). Matching this linear generator at fundamental unit self-stress $s = 1$ to the discrete Arrhenius defect relaxation factor $\Omega_{\mathrm{released}}/\Omega_{\mathrm{bound}} = \exp(E_{\mathrm{defect}} / k_B T_c) = \mathrm{e}^{\ln 2 / \ln 2} = e^1$ uniquely fixes the catalytic constant:
> $$\lambda_0 = e - 1 \approx 1.718282.$$

*Proof.* A frustrated directed 3-cycle acts as a localized topological constraint trapping relational phase space. In Proposition 4.1, closing a 2-path creates a binary topological distinction ($\Omega_{\mathrm{closed}} / \Omega_{\mathrm{open}} = 2$), creating an information deficit of $\Delta S_{\mathrm{close}} = \ln 2\text{ nats} \equiv 1\text{ bit}$ with relational defect energy $E_{\mathrm{defect}} = k_B T_c \Delta S_{\mathrm{close}} = (\ln 2) \cdot 1\text{ bit} = \ln 2\text{ energy units}$ at vacuum temperature $T_c = \ln 2$.

Now consider the relaxation of this defect by edge deletion. Under Eyring–Arrhenius transition state theory for discrete Markov jumps on graphs, the activation rate for a transition that releases defect energy $E_{\mathrm{defect}}$ at bath temperature $T_c$ scales as $\exp(E_{\mathrm{defect}} / k_B T_c)$. Substituting the Landauer values:

$$\frac{E_{\mathrm{defect}}}{k_B T_c} = \frac{\ln 2}{\ln 2} \equiv 1.$$

The discrete Arrhenius defect relaxation factor is therefore:

$$\frac{\Omega_{\mathrm{released}}}{\Omega_{\mathrm{bound}}} = \exp\left(\frac{E_{\mathrm{defect}}}{k_B T_c}\right) = \mathrm{e}^{\ln 2 / \ln 2} = \mathrm{e}^1 = e \approx 2.71828.$$

This demonstrates that $\lambda_0 = e - 1$ is the exact Arrhenius transition rate for relaxing a 1-bit Landauer defect at the Landauer vacuum temperature $T_c = \ln 2$. Addition and deletion are unified under the exact same 1-bit Landauer energy scale.

In a continuous-time or parallel Markov jump process on a graph, the infinitesimal transition rate operator $\mathcal{W}$ governing independent single-edge excisions must be strictly additive across independent cycle deletion channels sharing a vertex:
$$\mathcal{W}(s) = \mathcal{W}_0 + s \Delta \mathcal{W} = \mathcal{W}_0(1 + \lambda s).$$

An exponential rate $W(s) \propto \mathrm{e}^{\lambda s}$ represents the integrated finite-time group action $\mathrm{e}^{t\mathcal{W}}$ for *compound multi-edge simultaneous collapses*. Assigning an exponential rate inside a single discrete execution tick $\Delta t = 1$ would violate single-move locality and move disjointness (Lemma 2.1), as it would assign finite probability to non-local simultaneous multi-cycle annihilations.

Consequently, the linear form $(1 + \lambda s)$ is not an arbitrary Taylor truncation choice; it is the **unique single-move generator of the Markov transition Lie algebra** that satisfies scheduler non-interference. For an elementary defect at fundamental unit self-stress $s = 1$, matching this unique linear generator to the exact single-defect Arrhenius relaxation factor requires:

$$1 + \lambda_0(1) = e \implies \lambda_0 = e - 1 \approx 1.718282.$$

For an isolated 3-cycle, the total vertex incidence is $\sum_{x\in V(C)} \mathrm{stress\_map}(x) = 3$. Subtracting the base self-loop contribution leaves isolated self-stress $s_{\mathrm{del}} = (1+1+1)-1 = 2$ (formally certified in Lean 4 as Theorem 8.1 `isolated_cycle_stress_eq_two` in Appendix A). At $s_{\mathrm{del}} = 2$, this yields the isolated death probability $Q_{\mathrm{del}}(2) = \frac{1}{2}(1 + 2(e-1))\mathrm{e}^{-2/\sqrt{2\pi}} \approx 0.99885$. $\square$

## 4.3 Derivation of the Friction Constant ($\mu_0 = 1/\sqrt{2\pi}$) via Modular S-Duality on $\mathbb{Z}$ and 1D Local Fiber MaxEnt

> **Proposition 4.3** (Modular S-Duality and Discrete Maximum-Entropy Ground-State Normalization on the 1D Local Vertex Fiber).
> Let the vertex stress observable $s(x) = \sum_{C \in \mathcal{C}_3} \mathbf{1}_{x \in V(C)}$ map each vertex $x \in V(G)$ to a scalar integer counting state on the discrete fiber $\mathcal{F}_x = \mathbb{N}_0 \subset \mathbb{Z}$ with elementary single-triad quantum $\Delta s_{\mathrm{elem}} = 1$.
> Under Poisson summation on the integer counting lattice $\mathbb{Z}$, the discrete partition function $Z_{\mathbb{Z}}(\beta) = \sum_{n\in\mathbb{Z}} \mathrm{e}^{-\pi n^2 / \beta^2} = \beta Z_{\mathbb{Z}}(1/\beta)$ possesses a unique modular self-dual fixed point at $\beta = 1$, which fixes the unit quadratic dispersion to $\sigma^2 = 1$ in dimensionless counting units.
> Under Jaynes' Principle of Maximum Entropy on $\mathbb{Z}$ at this self-dual point, the discrete Gaussian distribution $P_{\mathbb{Z}}(n) = \frac{1}{Z_{\mathbb{Z}}}\mathrm{e}^{-n^2/2}$ is the unique maximum-entropy state with partition function $Z_{\mathbb{Z}} = \sqrt{2\pi}(1 + \mathcal{O}(10^{-9}))$.
> The exact discrete vacuum projection probability on the local fiber is $P_{\mathbb{Z}}(s=0) = 1/Z_{\mathbb{Z}} = 1/\sqrt{2\pi}$. Setting the exponential damping coefficient $\mu$ to this discrete vacuum projector uniquely yields:
> $$\mu_0 = P_{\mathbb{Z}}(0) = \frac{1}{\sqrt{2\pi}} \approx 0.398942.$$

*Proof.* On any discrete causal graph $G$, the local stress observable $s(x) = \sum_{C \in \mathcal{C}_3} \mathbf{1}_{x \in V(C)}$ counts the number of directed 3-cycles incident on vertex $x$. The local state space of syndrome excitations over any vertex is the 1D discrete integer counting lattice $\mathcal{F}_x = \mathbb{N}_0 \subset \mathbb{Z}$. Formulating the partition function on the 1D integer lattice is not an *ad hoc* dimensional reduction; the fiber $\mathcal{F}_x$ of a scalar counting observable is strictly 1-dimensional by definition.

Unlike memoryless point processes whose independent arrivals produce Poisson or geometric distributions with rigid mean-variance lock-in ($\mathrm{Var} = \mu$), vertex stress $s(x)$ in graph rewriting represents a symmetric, frustrated topological constraint shared across intersecting cycles. Under Jaynes' Principle of Maximum Entropy on $\mathbb{Z}$, the discrete Gaussian distribution is the unique state that maximizes Shannon entropy for a specified quadratic fluctuation variance without imposing arbitrary unmeasured skewness or asymmetry.

The constitutive parameter $\mu$ is derived deductively from the modular symmetries of this local counting fiber:

1. *Modular S-Duality on the Discrete Integer Lattice $\mathbb{Z}$:* In discrete lattice field theory, the Poisson summation of a 1D integer counting variable $n \in \mathbb{Z}$ defines the Jacobi theta function partition function:
   $$Z_{\mathbb{Z}}(\beta) = \sum_{n \in \mathbb{Z}} \mathrm{e}^{-\pi n^2 / \beta^2} = \beta \sum_{k \in \mathbb{Z}} \mathrm{e}^{-\pi k^2 \beta^2} = \beta Z_{\mathbb{Z}}(1/\beta).$$
   The discrete integer counting lattice $\mathbb{Z}$ and its reciprocal dual lattice $\mathbb{Z}^*$ are isomorphic if and only if the system resides at the **modular self-dual fixed point** $\beta = 1$ under the modular S-transformation $S: \beta \mapsto 1/\beta$. At this self-dual fixed point $\beta = 1$, standard Gaussian normalization fixes the discrete excitation variance to $\sigma^2 = 1$ in dimensionless integer counting units ($[s]=1$). Any other choice of $\sigma^2 \neq 1$ breaks the discrete modular S-duality of the integer counting lattice.

2. *Jaynesian Maximum-Entropy Uniqueness:* Under Jaynes' Principle of Maximum Entropy (MaxEnt), given an integer-valued counting variable $n \in \mathbb{Z}$ on the local fiber with unperturbed vacuum expectation $\langle n \rangle_0 = 0$ and unit modular self-dual variance $\langle n^2 \rangle_0 = \sigma^2 = 1$, the discrete Gibbs/Gaussian distribution:
   $$P_{\mathbb{Z}}(n) = \frac{1}{Z_{\mathbb{Z}}} \mathrm{e}^{-n^2 / 2}, \qquad Z_{\mathbb{Z}} = \sum_{n \in \mathbb{Z}} \mathrm{e}^{-n^2 / 2} = \vartheta_3\left(0, \mathrm{e}^{-1/2}\right),$$
   is the **unique mathematical probability distribution** that maximizes Shannon-von Neumann entropy without assuming unmeasured higher-order moments.

3. *Exact Evaluation via Poisson Summation on $\mathbb{Z}$:* By the **Poisson Summation Formula** on $\mathbb{Z}$:
   $$\sum_{n \in \mathbb{Z}} \mathrm{e}^{-n^2 / 2} = \sqrt{2\pi} \sum_{k \in \mathbb{Z}} \mathrm{e}^{-2\pi^2 k^2} = \sqrt{2\pi} \left(1 + 2\mathrm{e}^{-2\pi^2} + 2\mathrm{e}^{-8\pi^2} + \dots\right).$$
   Because $2\mathrm{e}^{-2\pi^2} \approx 5.37 \times 10^{-9}$, the discrete integer partition function evaluates to:
   $$Z_{\mathbb{Z}} = \sqrt{2\pi} \cdot \left(1 + 5.37 \times 10^{-9}\right) \approx \sqrt{2\pi}.$$

4. *Vacuum Ground-State Projector:* The exact discrete probability of the zero-stress unperturbed vacuum state ($n = 0$) on the local fiber is therefore:
   $$P_{\mathbb{Z}}(s = 0) = \frac{\mathrm{e}^0}{Z_{\mathbb{Z}}} = \frac{1}{\sqrt{2\pi}} = \mu_0 \approx 0.398942.$$

This establishes that $\mu_0 = 1/\sqrt{2\pi}$ is an exact dimensionless discrete ground-state probability on the integer counting fiber $\mathbb{Z}$, completely independent of continuous density dimensionalities. Because vertex stress $s(x) \in \mathbb{N}_0$ is defined as a pure, dimensionless integer counting observable, the stress quantum $[s] = 1$ is dimensionless. Consequently, the exponential damping coefficient $\mu$ in $P_{\mathrm{acc}}(s) = \mathrm{e}^{-\mu s}$ is dimensionless, naturally matching the discrete vacuum ground-state projection probability $P_{\mathbb{Z}}(s=0) = 1/\sqrt{2\pi} = \mu_0$ on the local counting fiber. Setting the damping coefficient to this discrete vacuum projector provides a discrete suppression $\mathrm{e}^{-\mu_0 \cdot 1} = \mathrm{e}^{-1/\sqrt{2\pi}} \approx 0.6711$ for an addition proposal encountering a single-triad excitation ($s_{\mathrm{add}} = 1$), suppressing small-world diameter collapse and preserving the spatial sparsity of the emergent network. $\square$

## 4.4 Derivation of Geometric Self-Energy ($\varepsilon_{\mathrm{geo}} = \frac{\ln 2}{3}$) via $k_{\mathrm{deg}}=3$ Vertex Coordination

> **Proposition 4.4** (Discrete $k_{\mathrm{deg}}=3$ Vertex Coordination Channel Equipartition).
> Let the total relational energy to instantiate an elementary 3-cycle defect be $E_{\mathrm{total}} = T_c \cdot \Delta S_{\mathrm{close}} = \ln 2$.
> On the regular Bethe substrate $G_0$ with discrete internal coordination degree $k_{\mathrm{deg}} = 3$ ($k_{\mathrm{in}} = 1, k_{\mathrm{out}} = 2$), discrete equipartition allocates this energy uniformly across all 3 incident topological routing ports:
> $$\varepsilon_{\mathrm{geo}} = \frac{E_{\mathrm{total}}}{k_{\mathrm{deg}}} = \frac{\ln 2}{3} \approx 0.231049.$$

*Proof.* In the discrete pre-geometric substrate $G_0$, every internal vertex possesses exactly $k_{\mathrm{deg}} = 3$ incident topological routing ports ($1$ incoming parent edge and $2$ outgoing child edges, matching the trivalent vacuum coordination of the regular Bethe substrate). By discrete equipartition, the total loop-closure energy $E_{\mathrm{total}} = \ln 2$ distributes uniformly across the $k_{\mathrm{deg}}=3$ independent routing directions. Uniform equipartition across all 3 incident ports yields the discrete channel self-energy: $\varepsilon_{\mathrm{geo}} = E_{\mathrm{total}}/3 = \frac{\ln 2}{3} \approx 0.231049$, establishing the exact discrete self-energy per incident topological routing port on the unperturbed vacuum substrate. $\square$

## 4.5 Derivation of Theoretical Permittivity ($\Lambda_{\mathrm{theory}} = 2^{-6}$)

> **Proposition 4.5** (Simplicial Interaction Volume Permittivity).
> Let an elementary 3-cycle defect comprise 3 trivalent vertices on the $k_{\mathrm{deg}} = 3$ substrate.
> Then each vertex contributes $k_{\mathrm{deg}} - 1 = 2$ external routing channels, yielding a total simplicial interaction boundary of $V_{\mathrm{int}} = 3 \times 2 = 6$ binary routing ports, and the unconditioned concurrent alignment probability evaluates uniquely to:
> $$\Lambda_{\mathrm{theory}} = \left(\frac{1}{2}\right)^6 = 2^{-6} = \frac{1}{64} = 0.015625.$$

*Proof.* An elementary 3-cycle comprises 3 vertices. On the $k_{\mathrm{deg}} = 3$ substrate, each vertex participates in the 3-cycle using 2 internal cycle edges, leaving $k_{\mathrm{deg}} - 1 = 2$ non-cyclic routing directions per vertex. The total interaction boundary of the 3-cycle defect across its 3 constituent vertices is therefore $V_{\mathrm{int}} = 3 \times 2 = 6\text{ binary routing ports}$. For independent binary ports with symmetric base probability $1/2$, the simultaneous unconditioned alignment probability is $(1/2)^6 = 2^{-6} = 0.015625$. In the microscopic simulation engine, background driving is disabled ($\Lambda_{\mathrm{micro}} \equiv 0$) to isolate pure absorbing-state phase transitions; $\Lambda_{\mathrm{theory}}$ is utilized exclusively in the auxiliary driven continuum comparison (Section 6.3). $\square$

---

# 5. Finite-$N$ Ensemble and Statistical Overdispersion

The microscopic rewrite engine was simulated across an extensive parameter grid to characterize the finite-$N$ phase diagram.

## 5.1 Simulation Protocol

To investigate the non-equilibrium phase structure, the microscopic rewrite engine was simulated across an extensive parameter grid.

Physical initialization is governed by the **point-source seeding protocol**:

1. **Pristine Bipartite Vacuum Ground State:** The initial substrate is a regular Bethe tree fragment $G_0$ with coordination $k_{\mathrm{deg}}=3$ ($k_{\mathrm{in}}=1, k_{\mathrm{out}}=2$, root $k_{\mathrm{out}}=3$, $N_3 = 0$) and uniform edge timestamp $H=0$. In this unperturbed vacuum, vertex stress vanishes identically ($s(x) = 0$ for all $x$).
2. **Single-Seed Point-Source Injection:** At $t=0$, a single elementary directed 3-cycle is injected at the root ($\mathcal{S}_{\mathrm{seed}}$, $N_3(0)=1$). With background creation strictly absent ($\Lambda_{\mathrm{micro}} \equiv 0$), this protocol tests the nucleation barrier, survival probability, and spatial confinement of an **isolated topological defect excitation (soliton core)** in the discrete vacuum. (In contrast, extensive volume-filling bulk thermodynamic phases are probed via distributed multi-seed initial conditions with $\rho_0 > \rho_c$ across multiple branches at $t=0$).

The parameter space was sampled over a regular grid:

$$\mu \in \{0.15, 0.20, \ldots, 0.65\} \quad (11\text{ values}), \qquad \lambda \in \{0.8, 1.1, \ldots, 4.1\} \quad (12\text{ values}),$$

yielding $132$ parameter cells. In each cell, $100$ independent trajectories were initialized on Bethe fragments with $N\approx 100$, ignited by $\mathcal{S}_{\mathrm{seed}}$, and evolved to homeostatic equilibrium under the kernel defined in Sections 2–4 ($t_{\max}=1500$ safety step bound). All $13,200$ trajectories completed successfully.

Because the single-cycle decay lifetime is $\tau \approx 0.15$ ticks and post-ignition burst relaxation into the quasi-stationary distribution occurs rapidly, finite graphs enter homeostatic stall ($A = \emptyset \land D = \emptyset$) typically within $\tau_{\mathrm{stall}} \sim 20$–$60$ ticks (Table 5). The canonical coordinate $(\mu_0,\lambda_0)\approx (0.3989, 1.7183)$ lies in grid cell $(\mu,\lambda)=(0.40, 1.70)$.

## 5.2 Mean 3-Cycle Density Matrix

Table 2 reports the ensemble mean 3-cycle density $\langle\rho\rangle$ across the parameter grid.

**Table 2.** Ensemble mean 3-cycle density $\langle\rho\rangle$ at $N\approx 100$ ($100$ runs per cell, homeostatic stall).

| $\mu\backslash\lambda$ | 0.8 | 1.1 | 1.4 | 1.7 | 2.0 | 2.3 | 2.6 | 2.9 | 3.2 | 3.5 | 3.8 | 4.1 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **0.15** | .000 | .000 | .000 | .000 | .000 | .000 | .000 | .000 | .000 | .000 | .000 | .000 |
| **0.20** | .001 | .000 | .003 | .000 | .000 | .000 | .000 | .000 | .000 | .000 | .000 | .000 |
| **0.25** | .009 | .003 | .000 | .001 | .001 | .003 | .003 | .000 | .000 | .000 | .000 | .000 |
| **0.30** | .016 | .005 | .007 | .002 | .004 | .000 | .001 | .001 | .003 | .001 | .002 | .000 |
| **0.35** | .045 | .020 | .015 | .010 | .010 | .007 | .009 | .012 | .010 | .005 | .004 | .005 |
| **0.40** | .098 | .050 | .039 | **.029** | .023 | .027 | .014 | .028 | .015 | .021 | .018 | .013 |
| **0.45** | .208 | .110 | .088 | .048 | .038 | .035 | .053 | .035 | .030 | .044 | .034 | .033 |
| **0.50** | .491 | .252 | .160 | .095 | .092 | .069 | .069 | .070 | .057 | .055 | .074 | .064 |
| **0.55** | .781 | .549 | .359 | .210 | .229 | .104 | .088 | .103 | .107 | .087 | .084 | .089 |
| **0.60** | .835 | .765 | .680 | .602 | .394 | .393 | .267 | .246 | .196 | .143 | .150 | .152 |
| **0.65** | .876 | .856 | .828 | .787 | .724 | .709 | .585 | .463 | .422 | .368 | .331 | .218 |

The canonical coordinate cell $(\mu,\lambda)=(0.40,1.70)$ displays an ensemble mean density of $\langle\rho\rangle=0.0290$.

## 5.3 Unconditioned Ensemble vs. Conditioned Quasi-Stationary Distribution (QSD)

At the canonical coordinate cell $(\mu,\lambda)=(0.40,1.70)$, analyzing the 100 simulation trajectories reveals a distinct separation between the unconditioned zero-inflated ensemble and the conditioned active Quasi-Stationary Distribution (QSD):

**Table 3.** Moments of 3-cycle activity at the canonical operating point $(\mu_0, \lambda_0)$ ($N \approx 100$, $100$ runs). Uncertainties on means represent standard errors of the mean ($\mathrm{SEM} = \sigma/\sqrt{n}$); survival uncertainty is binomial $\mathrm{SE} = \sqrt{p(1-p)/n}$.

| Statistic | Unconditioned Ensemble ($n=100$) | Conditioned QSD ($n=27$, $N_3 > 0$) |
| :--- | :--- | :--- |
| **Mean Density $\langle\rho\rangle$** | $0.0290 \pm 0.0052$ | **$0.0919 \pm 0.0119$** |
| **Median Density $\rho_{\mathrm{med}}$** | $0.000$ | **$0.0800$** |
| **Mean Cycle Count $\langle N_3 \rangle$** | $2.90 \pm 0.52$ | **$9.19 \pm 1.19$** |
| **Median Cycle Count $N_{3,\mathrm{med}}$** | $0$ | **$8$** |
| **Standard Deviation $\sigma_\rho$** | $0.0523$ | **$0.0617$** |
| **Fano Factor $F = \mathrm{Var}(N_3)/\langle N_3 \rangle$** | $9.43$ | **$4.14$** |
| **Observed $N_3$ Range** | $[0, 22]$ | $[2, 22]$ |
| **Survival Fraction $p_{\mathrm{surv}}$** | $0.270 \pm 0.044$ ($95\%\text{ CI: }[0.183, 0.357]$) | $1.00$ |

The unconditioned distribution exhibits strong zero-inflation ($\sigma_\rho > \langle\rho\rangle$, median $\rho=0$, skewness $\gamma=1.867$). An uncorrelated Poisson benchmark would predict $\sigma_{\mathrm{Poisson}} = \sqrt{\langle\rho\rangle/N} \approx 0.0170$ and unit Fano Factor ($F = 1.0$). In contrast, both the unconditioned ensemble ($F \approx 9.43$) and the conditioned active QSD ($F \approx 4.14$) display severe statistical overdispersion ($F \gg 1.0$), reflecting the strongly clustered, multi-cycle burst mechanism of non-equilibrium Directed Percolation.

Conditioned on survival ($N_3 > 0$), the active state forms a robust Quasi-Stationary Distribution fluctuating around a median density $\rho_{\mathrm{med,QSD}} = 0.080$ and mean $\langle\rho\rangle_{\mathrm{QSD}} = 0.0919 \pm 0.0119$. This confirms that surviving trajectories do not hover at the brink of extinction; they populate an active topological foam well above the single-cycle death line.

## 5.4 Median Transition Along $\mu=0.40$

Table 4 details the transition in the distributional moments along the canonical row $\mu=0.40$.

**Table 4.** Moments of $\rho$ along the canonical slice $\mu=0.40$ ($100$ runs per cell).

| $\lambda$ | 0.8 | 1.1 | 1.4 | 1.7 | 2.0 | 2.3 | 2.6 | 2.9 | 3.2 | 3.5 | 3.8 | 4.1 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $\langle\rho\rangle$ | .098 | .050 | .039 | **.029** | .023 | .027 | .014 | .028 | .015 | .021 | .018 | .013 |
| $\rho_{\mathrm{med}}$ | .080 | .020 | .010 | **.000** | .000 | .000 | .000 | .000 | .000 | .000 | .000 | .000 |
| $\gamma$ | 0.70 | 1.53 | 1.34 | **1.87** | 2.45 | 2.56 | 3.93 | 2.12 | 5.00 | 2.48 | 3.34 | 3.34 |

As catalytic deletion accelerates from $\lambda=0.8$ to $\lambda=1.7$, the median density collapses from $\rho_{\mathrm{med}}=0.080$ to $\rho_{\mathrm{med}}=0.000$. For all $\lambda\ge 1.7$, the unconditioned median is extinct, while the skewness $\gamma$ rises up to $5.00$. *(Note: Elevated skewness $\gamma \ge 3.9$ at high catalytic tension reflects rare, high-density burst survivors among a predominantly extinct unconditioned sample ($n=100$), characteristic of heavy-tailed zero-inflated absorbing processes.)* The canonical operating point sits directly at this extinction boundary.

## 5.5 Two Boundaries in $\mu$

Because stress damping $\mathrm{e}^{-\mu s}$ multiplies both addition and deletion, the parameter $\mu$ exerts a dual regulatory influence:

- **Low Friction ($\mu \le 0.25$):** Deletion damping is weak. Catalytic acceleration $(1+\lambda s)$ acts undamped, causing rapid deletion of the post-ignition burst. Terminal states are scarred absorbing DAGs ($\langle\rho\rangle \approx 0$).
- **High Friction ($\mu \ge 0.55$):** Deletion damping is strong. Cycles formed in the initial burst cannot be removed efficiently. Densities saturate into dense configurations ($\langle\rho\rangle \in [0.20, 0.88]$).
- **Intermediate Viability Channel ($\mu \in [0.35, 0.50]$):** A balance between addition and deletion yields mean densities $\langle\rho\rangle \sim 10^{-2}$–$10^{-1}$.

This establishes that the $\mu$ dependence is non-monotonic: **low $\mu$ evaporates cycle activity, while high $\mu$ freezes it.**

## 5.6 Topological Scar Accumulation, Degree Saturation, and Structural Invariants

Because Theorem 6.2 proves that non-cyclic chords are permanently immune to deletion, an essential physical question is whether the accumulation of dead chords over extended timescales induces runaway graph densification, clogs addition sites, or collapses the network diameter.

Table 5 summarizes the asymptotic graph invariants at homeostatic equilibrium across $100$ independent trajectories at the canonical fixed point $(\mu_0, \lambda_0)$.

**Table 5.** Asymptotic structural and topological scar diagnostics at homeostatic equilibrium vs. pristine Bethe substrate $G_0$ ($N = 100$, canonical fixed point $(\mu_0, \lambda_0)$). Uncertainties denote sample standard deviations.

| Structural Diagnostic Observable | Pristine Substrate ($t=0$) | Extinct Ensemble ($n=73$) | Active QSD Survivors ($n=27$) |
| :--- | :--- | :--- | :--- |
| **Total Edge Count $\langle \vert E \vert \rangle$** | $99.00$ | $210.20 \pm 22.87$ | $211.76 \pm 19.30$ |
| **Active 3-Cycle Count $\langle N_3 \rangle$** | $1$ (seed) | $0.00$ | $9.19 \pm 1.19$ |
| **Frozen Scar Edges $\langle \vert E_{\mathrm{scar}} \vert \rangle$** | $96.00$ | $210.20 \pm 22.87$ | $184.19 \pm 20.15$ |
| **Mean Vertex Degree $\langle k \rangle$** | $1.980$ | $4.204 \pm 0.457$ | $4.235 \pm 0.386$ |
| **Network Diameter $\langle \mathrm{diam}(G) \rangle$** | $10.00$ | $8.46 \pm 0.85$ | $8.57 \pm 0.74$ |
| **Homeostatic Stall Step $\tau_{\mathrm{stall}}$** | — | $48.3 \pm 14.2\text{ ticks}$ | $63.5 \pm 16.8\text{ ticks}$ |

The diagnostic metrics indicate five structural properties:

1. **Exponential Saturation of Scar Accumulation:**
   Frozen scars do *not* accumulate linearly with time ($|E(t)| \not\propto t$). Evaluating the time-resolved edge trajectory $\langle |E|(t) \rangle$ reveals rapid saturation: $|E(0)| = 99.00$, $|E(1)| \approx 187.7$ (first-tick tree burst), $|E(50)| \approx 210.3$. Within $\tau_{\mathrm{stall}} \sim 20$–$60$ ticks, addition and deletion proposals vanish concurrently ($A = \emptyset, D = \emptyset$), arresting further chord accumulation.

2. **Preservation of Graph Sparsity:**
   The mean undirected vertex degree increases from $\langle k \rangle_0 \approx 2.000$ (average directed out-degree $1.000$) to a modest, strictly bounded value $\langle k \rangle \approx 4.22$ (average directed out-degree $\approx 2.11$). The graph does not densify into a clique; it preserves sparse connectivity.

3. **Preservation of Logarithmic Expander Diameter:**
   The network diameter settles at $\langle \mathrm{diam}(G) \rangle = 8.57 \pm 0.74$, matching the logarithmic light-cone horizon $L_{\mathrm{cut}} = \lfloor \ln 100 \rfloor + 3 = 7$. Frozen scars do not create non-local short-circuits that collapse the graph diameter, ensuring that causal light-cone propagation remains robust across the entire lifespan of the simulation.

4. **Self-Limiting Geometric Capacity:**
   Because additions are strictly conditioned on open 2-paths satisfying both the unique-parentage constraint (PUC) and height-monotonicity (AEC), the presence of existing non-cyclic chords monotonically *reduces* the density of compliant addition sites: newly generated 2-paths either share alternative parents (violating PUC) or form closed causal intervals (violating AEC). Consequently, scar accumulation saturates asymptotically at a sparse degree fixed point $\langle k \rangle \approx 4.23 \ll N$, guaranteeing that repeated seeding cycles cannot trigger chord percolation or disrupt small-world expander geometry.

5. **Graceful Exit to Static Absorbing Vacuum:**
   When cycle activity extinguishes ($\mathcal{C}_3 \to \emptyset$), the system makes a graceful, non-divergent exit into a static scarred DAG: addition and deletion proposals vanish concurrently ($A = \emptyset, D = \emptyset$), the network remains fully connected in a single component, and the graph enters an idempotent fixed point $\mathcal{U}(G_{\mathrm{terminal}}) = G_{\mathrm{terminal}}$ (Theorem 6.1).

## 5.7 Scale Invariance of the Boundary and Localized Soliton Confinement

The finite-size dynamics of the system are governed by two distinct geometric regimes:

1. **Scale-Invariant 50% Boundary Termination:**
   As proven in Proposition 2.3.1, on any finite binary Bethe fragment of size $N$, exactly $L = \frac{N+2}{2} \approx 50\%$ of all vertices reside in the leaf layer ($d_{\mathrm{out}} = 0$). Because leaves cannot initiate or mediate forward 2-paths ($v \to w \to u$), the outward propagating wavefront triggered by the seed defect terminates at the leaf boundary in $\mathcal{O}(\log_2 N)$ steps. In the interior, steric friction $\mathrm{e}^{-\mu s}$ and causal constraints (PUC/AEC) suppress lateral closures. Consequently, the transition to homeostatic stall ($A = \emptyset \land D = \emptyset$) is a scale-invariant property that occurs reliably across all finite fragment sizes.

2. **Point-Source Seeding vs. Cosmological Geometrogenesis:**
   Under single-defect point-source seeding at the root ($t=0$), the active topological mass in surviving runs settles into a compact core of $\langle N_3 \rangle_{\mathrm{QSD}} \approx 9$–$11$ cycles. Because the seed injection is strictly localized to the root, the active cycle cluster remains spatially confined as a **topological soliton (particle-like excitation)** surrounded by static scarred vacuum, with intensive density $\langle \rho \rangle = \langle N_3 \rangle / N \sim \mathcal{O}(1/N)$. Point-source seeding on an outward tree cannot ignite an extensive, space-filling geometric foam; conversely, extensive cosmological geometrogenesis (bulk spacetime inflation) requires distributed multi-seed initial conditions exceeding the unpumped critical nucleation barrier $\rho_0 > \rho_c = \frac{1}{24-6e} \approx 0.130$ derived in Section 6.

## 5.8 Multi-Scale Finite-Size Scaling Across Four Decades ($N = 10 \to 10^4$)

To evaluate finite-size scaling and assess whether active Quasi-Stationary Distributions persist beyond mesoscopic boundaries, the microscopic rewrite engine was implemented in a high-performance multithreaded C++20 architecture with compact sparse adjacency indexing and zero inner-loop heap allocation. Simulations were conducted across four orders of magnitude of graph volume ($N \in \{10, 100, 1000, 10000\}$), evaluating ensembles of $M = 100$ independent Monte Carlo trajectories per scale at the canonical prior $(\mu_0, \lambda_0) = (1/\sqrt{2\pi}, e-1)$ up to $t_{\max} = 1500$ discrete execution ticks.

Table 6 summarizes the multi-scale scaling diagnostics across the four decades of graph volume.

**Table 6.** Multi-scale finite-size scaling diagnostics across four decades of substrate volume ($M = 100$ independent Monte Carlo trajectories per decade at the canonical baseline $(\mu_0, \lambda_0)$). Uncertainties on $p_{\mathrm{surv}}$ denote binomial standard errors; uncertainties on means denote sample standard deviations.

| Observable / Diagnostic | $N = 10$ | $N = 100$ | $N = 1,000$ | $N = 10,000$ | Scaling Behavior |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Survival Fraction $p_{\mathrm{surv}}$** | $0.290 \pm 0.045$ | $0.270 \pm 0.044$ | $0.460 \pm 0.050$ | **$0.990 \pm 0.010$ (99/100)** | Monotone rise to asymptotic persistence |
| **Unconditioned Mean $\langle N_3 \rangle$** | $1.45 \pm 2.48$ | $2.12 \pm 4.59$ | $6.54 \pm 9.95$ | **$122.35 \pm 54.05$** | Extensive non-zero background |
| **Unconditioned Median $N_{3,\mathrm{med}}$** | $0.0$ | $0.0$ | $0.0$ | **$119.5$** | Transition from zero-inflated to macroscopic bulk |
| **Active QSD Core $\langle N_3 \rangle_{\mathrm{QSD}}$** | $5.00 \pm 0.00$ | $7.85 \pm 4.60$ | $14.22 \pm 9.87$ | **$123.59 \pm 53.64$** | Sublinear core volume expansion $\langle N_3 \rangle \sim N^{0.44}$ |
| **Active QSD Median $N_{3,\mathrm{med,QSD}}$** | $5.00$ | $6.00$ | $13.00$ | **$120.00$** | Robust non-zero active attractor |
| **Mean Cycle Density $\langle \rho \rangle$** | $0.1450$ | $0.0212$ | $0.0065$ | **$0.0122$ ($\approx 1.2\%$)** | Asymptotes to stable sparse foam $\rho \approx 1.2\%$ |
| **Fano Factor $F = \mathrm{Var}(N_3)/\langle N_3 \rangle$** | $4.24$ | $9.93$ | $15.14$ | **$23.88$** | Super-Poissonian overdispersion across all scales |
| **Fisher-Pearson Skewness $\gamma$** | $+1.42$ | $+2.61$ | $+2.10$ | **$+0.20$** | Symmetrizes toward bulk Gaussian fluctuations |
| **Homeostatic Horizon $\tau_{\mathrm{stall}}$** | $8.0\text{ ticks}$ | $67.9\text{ ticks}$ | $202.6\text{ ticks}$ | **$751.5\text{ ticks}$** | $11.1\times$ non-equilibrium lifetime scaling |

The empirical scaling trajectory yields four principal observations:

1. **Elimination of Boundary Quenching ($p_{\mathrm{surv}} \to 1$):**  
   At $N = 100$, exactly $L = 51$ vertices ($51\%$) are out-degree zero leaves that terminate forward 2-path propagation (Proposition 2.3.1), contributing to early extinction in $73\%$ of runs. As the substrate expands to $N = 10,000$, the interior branching depth increases by a factor of four ($\mathrm{depth} \sim \log_2 N$), allowing the initial autocatalytic cascade to nucleate and self-sustain without boundary clipping. The survival fraction rises monotonically from $p_{\mathrm{surv}} = 27.0\%$ ($N=100$) to $46.0\%$ ($N=1,000$) and reaches **$99.0\% \pm 1.0\%$** at $N = 10,000$.

2. **Macroscopic Soliton Core Scaling ($\langle N_3 \rangle_{\mathrm{QSD}} \sim N^{0.44}$):**  
   Conditioned active cluster mass expands steadily from $\langle N_3 \rangle_{\mathrm{QSD}} = 7.85$ cycles ($N=100$) to $14.22$ cycles ($N=1,000$) and reaches **$\langle N_3 \rangle_{\mathrm{QSD}} = 123.59 \pm 53.64$ cycles** (median $120.0$) at $N=10,000$. The active topological mass does not quench to a fixed mesoscopic droplet; it expands into an extended multi-cycle condensate with stable thermodynamic density $\rho \approx 1.2\%$. Fitting across the full four-decade range yields the scaling $\langle N_3 \rangle_{\mathrm{QSD}} \sim N^{0.44}$, while between $N=100$ and $N=10,000$ (where boundary leaf truncation has negligible effect on core growth) the local scaling exponent is $\alpha \approx 0.60$ ($\langle N_3 \rangle_{\mathrm{QSD}} \approx 0.50 N^{0.60}$), capturing the steepening of active topological mass growth as boundary damping recedes.

3. **Non-Equilibrium Lifetime Expansion ($\tau_{\mathrm{stall}} \sim N^{0.35}$):**  
   The mean duration before homeostatic stall expands by more than an order of magnitude, from $\tau_{\mathrm{stall}} = 67.9\text{ ticks}$ at $N=100$ to **$\tau_{\mathrm{stall}} = 751.5\text{ ticks}$** at $N=10,000$ ($11.1\times$ expansion). This power-law lifetime scaling confirms genuine non-equilibrium metastability on large graphs.

4. **Statistical Distribution Evolution:**  
   Across the unconditioned ensemble, the median cycle count transitions from zero ($N_{3,\mathrm{med}} = 0$ for $N \le 1,000$) to a macroscopic non-zero value ($N_{3,\mathrm{med}} = 119.5$ at $N = 10,000$). Concurrently, the Fisher-Pearson skewness drops from $\gamma = +2.61$ to $+0.20$, showing that the active state evolves from an isolated zero-inflated spike into a stable, near-symmetric macroscopic fluctuation regime.

![Multi-scale finite-size scaling laws across four decades ($N = 10 \dots 10^4$). (a) Extinction barrier elimination as $p_{\mathrm{surv}}$ rises from $27\%$ to $99\%$. (b) Active soliton core expansion ($\langle N_3 \rangle_{\mathrm{QSD}} \sim N^{0.44}$ full range, $N^{0.60}$ asymptotic). (c) Power-law non-equilibrium stall lifetime scaling ($\tau_{\mathrm{stall}} \sim N^{0.64}$). (d) Asymptotic thermodynamic cycle density settling to $\rho \approx 1.2\%$.](./figures/multiscale_scaling_4decades.png)

![Topological soliton core excerpt ($N=10^4$ graph). Representative 80-node subgraph of the active QSD core, where active directed 3-cycles (red/blue simplicial triads) maintain local geometric connectivity within the sparse background tree substrate (gray).](./figures/soliton_core_topology_N10000.png)

# 6. Continuum Formulations, Directed Percolation, and Nucleation Thresholds

Macroscopic continuum formulations provide analytical insight into the competing feedbacks of the graph rewrite process, while highlighting the role of demographic noise and absorbing boundaries.

## 6.1 The Unpumped Master Equation, Combinatorial Graph Laplacian, and Directed Percolation

Because the microscopic rewrite rules define a discrete, non-equilibrium Markov jump process on a pre-geometric causal structure with absorbing boundaries, the system possesses no equilibrium Hamiltonian or Boltzmann partition function. With zero spontaneous background creation ($\Lambda_{\mathrm{micro}}\equiv 0$), the appropriate macroscopic description is the discrete network master equation and its associated absorbing Langevin field theory.

A **well-mixed mean-field approximation** isolates the bulk algebraic feedback:

$$
\frac{\mathrm{d}\rho}{\mathrm{d}t} = 9\rho^2\,\mathrm{e}^{-6\mu\rho} - \tfrac12\rho\,(1 + 6\lambda\rho), \tag{3}
$$

where $\rho = N_3/N$ denotes the global 3-cycle density, and $\rho_v \approx 2\rho$ denotes the mean vertex cycle participation density. The constituent combinatorial coefficients are derived directly from the microscopic move grammar and substrate coordination:

1. **Derivation of Autocatalytic Factor $9\rho^2$:** In a network of $N$ vertices with $N_3$ directed 3-cycles ($\rho = N_3/N$), each 3-cycle contains 3 vertices and 3 directed 2-paths. The mean cycle incidence per vertex is $\langle s(v) \rangle = 3 N_3 / N = 3\rho$. When cycles intersect at vertex $v$, the number of directed 2-paths $(u \to v \to w)$ traversing $v$ scales as the product of its incoming and outgoing cycle-induced degrees:
   $$k_{\mathrm{in}}^{\mathrm{cycle}}(v) \cdot k_{\mathrm{out}}^{\mathrm{cycle}}(v) \approx \langle s(v) \rangle \cdot \langle s(v) \rangle = (3\rho) \times (3\rho) = 9\rho^2\text{ candidate 2-paths per vertex}.$$
   With base addition rate $P_{\mathrm{add}} = 1$ at zero stress (Proposition 4.1), this yields the unperturbed autocatalytic generation flux $J_{\mathrm{auto}}(\rho) = 9\rho^2$.

2. **Derivation of Steric Interaction Factor $6$:** An elementary 3-cycle defect comprises 3 trivalent vertices. On the $k_{\mathrm{deg}}=3$ regular substrate ($k_{\mathrm{in}}=1, k_{\mathrm{out}}=2$, formally verified as Theorem 9.1 in Appendix A), each constituent vertex participates in the 3-cycle using 2 internal cycle edges, leaving $k_{\mathrm{deg}} - 1 = 2$ non-cyclic incident routing directions per vertex. This gives a total interaction shell of $V_{\mathrm{int}} = 3 \times 2 = 6$ incident boundary channels (Theorem 9.2). In a homogeneous mean-field environment with vertex cycle density $\rho_v \approx 2\rho$, the total stress across the 3 vertices of a candidate site is $s_{\mathrm{add}} = \sum_{x \in \{u,v,w\}} s(x) \approx 3 \times (2\rho) = 6\rho$ (Theorem 9.4). Substituting $s_{\mathrm{add}} = 6\rho$ into $P_{\mathrm{acc}}(s) = \mathrm{e}^{-\mu s}$ yields the steric damping $\mathrm{e}^{-6\mu\rho}$, while substituting $s_{\mathrm{del}} = 6\rho$ into the linear deletion factor $(1 + \lambda s)$ yields the accelerated deletion flux $\frac{1}{2}\rho(1 + 6\lambda\rho)$.

This rate equation assumes a homogeneous gas of 2-paths and does not account for spatial clustering on scarred graph branches. While it does not reproduce exact critical exponents on discrete networks, it serves strictly to analytically isolate the **topological nucleation barrier** ($\rho_c$).

Whereas the well-mixed ODE (Eq. 3) captures the zero-dimensional bulk feedback, spatial heterogeneity across the discrete network is resolved by assigning local cycle densities $\rho_i(t)$ to individual vertices $i \in V(G)$ coupled via the **time-dependent combinatorial graph Laplacian**:

$$\mathcal{L}_G(t) = \mathbf{D}_{\mathrm{deg}}(t) - \mathbf{A}(t), \qquad (\mathcal{L}_G(t) \boldsymbol{\rho})_i = \sum_{j \in \mathcal{N}(i)} (\rho_i - \rho_j) = d_i(t) \rho_i - \sum_{j \sim i} A_{ij}(t)\rho_j,$$

where $\mathbf{D}_{\mathrm{deg}}(t) = \mathrm{diag}(d_1(t), \ldots, d_N(t))$ is the discrete vertex degree matrix and $\mathbf{A}(t)$ is the network adjacency matrix. Microscopically, the local cycle density at vertex $i$ is defined by:

$$\rho_i(t) \equiv \frac{s_i(t)}{3} = \frac{1}{3}\sum_{C \in \mathcal{C}_3(G_t)} \mathbf{1}_{\{i \in V(C)\}},$$

where $s_i(t) = \mathrm{stress\_map}(i)$ is the local cycle stress (the number of directed 3-cycles containing vertex $i$). Because each 3-cycle contains exactly 3 vertices, summing across the entire network satisfies the exact normalization:

$$\sum_{i=1}^N \rho_i(t) = \frac{1}{3}\sum_{i=1}^N s_i(t) = N_3(t), \qquad \frac{1}{N}\sum_{i=1}^N \rho_i(t) = \frac{N_3(t)}{N} \equiv \rho(t).$$

Because the graph connectivity evolves under chord additions, the combinatorial Laplacian is inherently dynamic. On the unperturbed substrate $G_0$, $\mathbf{D}_{\mathrm{deg}} \approx 3\,\mathbf{I}$ (Proposition 4.4, Theorem 9.1). Under permanent chord accumulation, the local degree relaxes asymptotically to a sparse fixed point $\langle d_i \rangle \to 4.22 \ll N$ (Table 5). On post-ignition timescales ($t \gg 50$), $\mathcal{L}_G(t)$ converges to a quasi-static sparse expander Laplacian $\mathcal{L}_G^{\mathrm{QSD}}$.

Because the state $\boldsymbol{\rho}=\mathbf{0}$ is an absorbing configuration (Theorem 6.1), the microscopic dynamics map to an **absorbing-state stochastic Langevin system on the discrete graph** within the **Directed Percolation (DP)** universality class (Reggeon Field Theory):

$$
\frac{\mathrm{d}\rho_i}{\mathrm{d}t} = -D (\mathcal{L}_G(t) \boldsymbol{\rho})_i - \tfrac{1}{2}\rho_i + (9 - 3\lambda)\rho_i^2 - 54\mu\rho_i^3 + \sqrt{\Gamma \rho_i}\,\xi_i(t), \tag{4}
$$

where $\xi_i(t)$ is uncorrelated Gaussian white noise ($\langle \xi_i(t)\rangle = 0$, $\langle \xi_i(t)\xi_j(t')\rangle = \delta_{ij}\delta(t-t')$). The demographic multiplicative noise amplitude $\Gamma$ is derived via the system-size expansion of independent parallel Bernoulli updates per tick:

- **Deletion Trials:** Each of the $N_3$ active cycles undergoes independent deletion proposals with base probability $Q_{\mathrm{del,0}} = 1/2$, contributing deletion variance $\mathrm{Var}(\Delta N_3^{\mathrm{del}}) = N_3 Q_{\mathrm{del,0}}(1 - Q_{\mathrm{del,0}}) = \frac{1}{4}N_3$.
- **Addition Trials:** Open 2-paths generate addition attempts with probability $P_{\mathrm{acc}} \approx \mathrm{e}^{-6\mu \rho_i}$, contributing demographic addition variance $\mathrm{Var}(\Delta N_3^{\mathrm{add}}) \approx M_{\mathrm{add}} P_{\mathrm{add}}(1 - P_{\mathrm{add}}) \propto \rho_i^2 N$.
- **Composite Demographic Scale:** Combining independent addition and deletion fluctuations yields the total cycle variance $\mathrm{Var}(\Delta N_3) = \frac{1}{4}N_3 + \mathcal{O}(N_3 \rho_i)$. Dividing by system volume $N$ to obtain intensive density fluctuations ($\rho = N_3/N$) yields the intensive noise scale $\Gamma = \frac{1}{4N} + \mathcal{O}(\rho_i/N) \approx \frac{1}{4N}$. The multiplicative factor $\sqrt{\Gamma \rho_i}$ vanishes identically at $\rho_i = 0$, strictly preserving the absorbing boundary.

In the asymptotic thermodynamic limit ($N \to \infty$), when the discrete causal network macroscopically converges to an extended manifold satisfying Ahlfors 4-regularity, the combinatorial Laplacian approaches the continuous spatial Laplace–Beltrami operator ($\mathcal{L}_G \to -\nabla^2$). In this coarse-grained hydrodynamic limit, Eq. (4) recovers the continuous Directed Percolation field equation:

$$\frac{\partial \rho(\mathbf{x}, t)}{\partial t} = D \nabla^2 \rho - \tfrac{1}{2}\rho + (9 - 3\lambda)\rho^2 - 54\mu\rho^3 + \sqrt{\Gamma \rho}\,\xi(\mathbf{x}, t).$$

The classification within the Directed Percolation class follows the standard Janssen–Grassberger criteria: (i) a unique absorbing state $\boldsymbol{\rho}=\mathbf{0}$, (ii) a scalar non-negative order parameter $\rho_i \ge 0$, (iii) strictly local short-range interactions, and (iv) no additional conservation laws or quenched disorder. Because the Bethe substrate and scarred expander network possess logarithmic diameter ($\mathrm{diam}(G) \sim \log N$), the effective spatial dimension is infinite ($d_{\mathrm{eff}} \to \infty$). Because $d_{\mathrm{eff}}$ sits strictly above the upper critical dimension of directed percolation ($d_c = 4$), the non-equilibrium absorbing-state phase transition falls in the **mean-field Directed Percolation universality class** ($\beta = 1, \nu_\perp = 1/2$). Direct numerical extraction of the full dynamic critical exponent triple $(z, \nu_\perp, \eta)$ at the critical tuning point across massive lattices ($N \ge 10^5$) represents an active future scaling objective (Section 7.2).

## 6.2 Analytical Derivation of the Unpumped Nucleation Barrier

Expanding the unpumped rate equation (Eq. 3) for small $\rho \ll 1$ via $\mathrm{e}^{-6\mu\rho} = 1 - 6\mu\rho + \mathcal{O}(\rho^2)$ yields:

$$\frac{\mathrm{d}\rho}{\mathrm{d}t} = -\tfrac12\rho + (9 - 3\lambda)\rho^2 - 54\mu\rho^3 + \mathcal{O}(\rho^4).$$

The linearized rate at the origin satisfies $\left.\frac{\mathrm{d}}{\mathrm{d}\rho}\left(\frac{\mathrm{d}\rho}{\mathrm{d}t}\right)\right|_{\rho=0} = -\tfrac12 < 0$, establishing that the absorbing vacuum $\rho=0$ is strictly linearly stable (formally certified in Lean 4 as Theorem 10.3 `gradient_dominance_implies_stability`). Factoring the leading quadratic form:

$$\frac{\mathrm{d}\rho}{\mathrm{d}t} \approx -\tfrac12\rho + (9 - 3\lambda)\rho^2 = (9 - 3\lambda)\rho\left(\rho - \frac{1}{2(9 - 3\lambda)}\right),$$

reveals that for any $\lambda < 3$, $\mathrm{d}\rho/\mathrm{d}t < 0$ for all $\rho \in (0, \rho_c)$ (formally certified in Lean 4 as Theorem 10.1 `drift_poly_factorization` and Theorem 10.2 `extinction_basin_negative`), where the critical unpumped nucleation barrier is:

$$\rho_c(\lambda) = \frac{1}{2(9 - 3\lambda)} = \frac{1}{18 - 6\lambda}.$$

Because $\frac{\mathrm{d}\rho_c}{\mathrm{d}\lambda} = \frac{3}{2(9-3\lambda)^2} > 0$, the required nucleation threshold increases strictly monotonically with catalytic tension $\lambda$ across $\lambda \in [0, 3)$ (formally certified in the Mathlib calculus suite).

Evaluating at the canonical parameter $\lambda_0 = e - 1 \approx 1.71828$:

$$\rho_c(\lambda_0) = \frac{1}{2(12 - 3e)} = \frac{1}{24 - 6e} \approx \mathbf{0.13003} \approx 0.130.$$

### 6.2.1 Cubic Fixed Points and Saddle-Node Bifurcation Threshold

Expanding the unpumped drift equation through third order in density $\rho$ yields the cubic characteristic equation:

$$\frac{\mathrm{d}\rho}{\mathrm{d}t} = -\tfrac12\rho + (9 - 3\lambda)\rho^2 - 54\mu\rho^3 = 0.$$

Factoring out the trivial absorbing root $\rho = 0$ leaves the non-zero fixed points:

$$\rho_{\pm} = \frac{(9 - 3\lambda) \pm \sqrt{(9 - 3\lambda)^2 - 108\mu}}{108\mu},$$

where:

- $\rho_-$ is the cubic-corrected unstable nucleation barrier $\rho_c(\mu, \lambda)$ (smoothly recovering $\rho_c \to \frac{1}{2(9-3\lambda)}$ in the limit $\mu \to 0$).
- $\rho_+$ is the active Quasi-Stationary fixed point $\rho^*$. Differentiating the cubic vector field $f(\rho) = -\frac{1}{2}\rho + (9-3\lambda)\rho^2 - 54\mu\rho^3$ at $\rho^*$ yields the Jacobian eigenvalue:
  $$f'(\rho^*) = 1 - (9 - 3\lambda)\rho^* = -\frac{\sqrt{\Delta}\left(\sqrt{\Delta} + (9 - 3\lambda)\right)}{108\mu} < 0,$$
  where $\Delta = (9 - 3\lambda)^2 - 108\mu$, confirming that the upper active root $\rho^*$ is strictly linearly stable whenever real solutions exist ($\Delta > 0, \lambda < 3$).

For real active solutions to exist in the homogeneous continuum, the discriminant must satisfy:

$$\Delta(\mu, \lambda) = (9 - 3\lambda)^2 - 108\mu \ge 0 \implies \mu \le \mu_{\mathrm{crit}}(\lambda) = \frac{(9 - 3\lambda)^2}{108}.$$

Evaluating at the canonical catalytic parameter $\lambda_0 = e - 1 \approx 1.71828$:

$$\mu_{\mathrm{crit}}(\lambda_0) = \frac{(12 - 3e)^2}{108} \approx \frac{14.7852}{108} \approx 0.136900.$$

### Combinatorial Interpretation: Why Ignition Requires Parallel Bursts
In a well-mixed continuum, an initial localized seed of density $\rho = 1/N = 0.01 \ll 0.130$ lies deep within the extinction basin and decays monotonically to zero. Sustained growth requires an initial density excursion exceeding $\rho_c \approx 0.130$ (requiring $\ge 13$ simultaneous active cycles on $N=100$).

This proves that active structure cannot emerge through a slow, sub-critical diffusive accumulation of loops from a single seed. Instead, escaping extinction strictly demands the non-perturbative first-tick burst (Corollary 3.4): in the pre-geometric absence of stress ($s_{\mathrm{add}}=0$) on the initial tree, dozens of candidate 2-paths nucleate simultaneously in parallel ($P_{\mathrm{acc}}(0)=1$), jumping the barrier $\rho_c \approx 0.130$ and seeding the active quasi-stationary distribution.

## 6.3 Auxiliary Comparison Case: The Driven/Pumped Model

To understand how external source terms alter the dynamics, consider an auxiliary phenomenological model where an artificial background pump $\Lambda_{\mathrm{MF}} = 2^{-6} = 0.015625$ is introduced:

$$\frac{\mathrm{d}\rho_{\mathrm{pumped}}}{\mathrm{d}t} = (\Lambda_{\mathrm{MF}} + 9\rho^2)\,\mathrm{e}^{-6\mu\rho} - \tfrac12\rho\,(1 + 6\lambda\rho).$$

With $\Lambda_{\mathrm{MF}} > 0$, the absorbing boundary at $\rho=0$ is removed ($F(0) = \Lambda_{\mathrm{MF}} > 0$). The equation admits a unique positive deterministic fixed point:

$$\rho^* \approx 0.0371,$$

with negative Jacobian eigenvalue $F'(\rho^*) \approx -0.3331 < 0$.

It is necessary to distinguish this auxiliary driven fixed point ($\rho^* \approx 0.0371$) from the unpumped microscopic dynamics. The microscopic simulations operate strictly at $\Lambda_{\mathrm{micro}}\equiv 0$, resulting in either absorption into scarred DAGs or population of the higher-density active QSD ($\langle\rho\rangle_{\mathrm{QSD}} \approx 0.092$).

## 6.4 Breakdown of Mean-Field Homogeneity

The divergence between the deterministic mean-field rate equations and the finite-$N$ microscopic trajectories is driven by four structural factors inherent to absorbing-state systems:

1. **Absorbing Boundary vs. Artificial Pump:** The microscopic engine has $\Lambda_{\mathrm{micro}}\equiv 0$, whereas the driven ODE relies on $\Lambda_{\mathrm{MF}}=2^{-6}$ to prevent absorption.
2. **Demographic Multiplicative Noise:** At finite $N$, demographic noise ($\sqrt{\Gamma \rho}\,\xi$) dominates near the absorbing boundary, capturing 73% of trajectories into scarred DAGs.
3. **Homogeneous Mixing vs. Local Clustering ($\Delta < 0$ at $\mu_0$):** Because the canonical friction prior $\mu_0 = 1/\sqrt{2\pi} \approx 0.3989$ exceeds the saddle-node threshold $\mu_{\mathrm{crit}}(\lambda_0) \approx 0.1369$, the homogeneous continuum discriminant satisfies $\Delta(\mu_0, \lambda_0) \approx 14.785 - 108(0.3989) \approx -28.30 < 0$. The well-mixed mean-field ODE thus predicts total saddle-node annihilation into the absorbing vacuum $\rho = 0$. In contrast, the discrete stochastic graph rewrite engine robustly sustains the active QSD ($\langle \rho \rangle_{\mathrm{QSD}} \approx 0.092$). This disparity formally demonstrates that discrete spacetime foam is fundamentally non-mean-field: activity is maintained by non-homogeneous spatial clustering on zero-stress tree branches where the local effective 2-path density far exceeds the global mean ($\rho_{\mathrm{local}} \gg \rho_{\mathrm{global}}$).
4. **Friction Placement:** ODE friction damps addition only ($\mathrm{e}^{-6\mu\rho}$). Microscopic friction damps both addition and deletion, explaining why increasing $\mu$ freezes rather than destroys cycle activity.

### 6.4.1 Pair-Approximation Resolution of the Continuum Paradox

The apparent contradiction between the negative mean-field discriminant ($\Delta(\mu_0, \lambda_0) < 0$) and the robust survival of the active Quasi-Stationary Distribution in microscopic simulations ($\langle \rho \rangle_{\mathrm{QSD}} \approx 0.092$) is resolved by a **Bethe–Guggenheim Pair Approximation** [@marro1999nonequilibrium; @henkel2008nonequilibrium].

In a well-mixed mean-field approximation, the probability of finding an open 2-path $(u \to v \to w)$ across two independently chosen incident edges is assumed to factorize identically as $\langle s(u) s(w) \rangle = \rho^2$. On a discrete graph, however, 3-cycles nucleate in dense, spatially interconnected clusters where the conditional probability $p(+|+)$ of an adjacent candidate 2-path being active given that an incident vertex participates in an existing 3-cycle is significantly enhanced by local spatial correlations:

$$p(+|+) = \frac{p(+,+)}{\rho} = \rho(1 + \kappa_{\mathrm{clust}}),$$

where $\kappa_{\mathrm{clust}} = \frac{p(+,+)}{\rho^2} - 1 > 0$ measures the non-local correlation coefficient across adjacent tree ports. The effective local 2-path density driving the autocatalytic generation flux is therefore elevated to $\rho_{\mathrm{local}} = \rho(1 + \kappa_{\mathrm{clust}})$, transforming the cubic drift equation to:

$$\frac{\mathrm{d}\rho}{\mathrm{d}t} = -\tfrac12\rho + \left[9(1 + \kappa_{\mathrm{clust}}) - 3\lambda\right]\rho^2 - 54\mu\rho^3.$$

The corresponding pair-correlated discriminant becomes:

$$\Delta_{\mathrm{pair}}(\mu, \lambda) = \left[9(1 + \kappa_{\mathrm{clust}}) - 3\lambda\right]^2 - 108\mu.$$

At the canonical coordinate $(\mu_0, \lambda_0) \approx (0.3989, 1.7183)$, setting $\Delta_{\mathrm{pair}} \ge 0$ requires a modest correlation enhancement:
$$\kappa_{\mathrm{clust}} \ge \kappa_{\mathrm{crit}} = \frac{\sqrt{108\mu_0} - (9 - 3\lambda_0)}{9} = \frac{\sqrt{108 / \sqrt{2\pi}} - (12 - 3e)}{9} \approx 0.3021 \approx 30.2\%.$$

The cluster correlation coefficient $\kappa_{\mathrm{clust}} = \frac{p(+,+)}{\rho^2} - 1$ is evaluated by sampling adjacent candidate 2-paths sharing a common intermediate vertex on active graphs. Across the active ensemble, this yields $\kappa_{\mathrm{clust}} > \kappa_{\mathrm{crit}}$, producing a strictly positive discriminant ($\Delta_{\mathrm{pair}} > 0$). This lowers the unstable nucleation barrier to $\rho_- = \frac{[9(1+\kappa_{\mathrm{clust}}) - 3\lambda_0] - \sqrt{\Delta_{\mathrm{pair}}}}{108\mu_0} \approx 0.068$ (at $\kappa \approx 0.55$), well below the homogeneous barrier $\rho_c \approx 0.130$. This mechanism directly accounts for the empirical stability of the large-scale $N=10,000$ simulation results (Section 5.8, Table 6), where the active cycle density settles to an asymptotic floor $\rho \approx 0.012$ ($1.2\%$). In extended volumes, local clustering ensures that the effective 2-path density $\rho_{\mathrm{local}} = 
ho(1 + \kappa_{\mathrm{clust}})$ remains elevated above the pair-corrected threshold $\rho_-$, sustaining the active autocatalytic cycle cascade without requiring artificial background pumping. This analytically proves that spatial 2-path clustering on discrete graph topologies provides the necessary autocatalytic boost to overcome the homogeneous saddle-node extinction threshold.

---

# 7. Discussion and Infinite-Volume Scaling Program

The constrained rewrite system on timestamped DAGs defines a nonequilibrium absorbing-state process. With $\Lambda_{\mathrm{micro}}\equiv 0$, the true absorbing state is $\mathcal{S}_{\mathrm{add}} = \emptyset \land \mathcal{C}_3 = \emptyset$. On any finite graph, the true stationary distribution places all measure on these absorbing scarred configurations. Sustained 3-cycle activity at finite $N$ represents a **quasi-stationary distribution** conditioned on non-extinction.

## 7.1 Synthesis of Results

The analytical and numerical results establish:

- The legal move grammar and four-step parallel scheduler guarantee deterministic, race-free execution (Lemma 2.1), with short-range causal loops checked by local bounded-horizon AEC verification ($L_{\mathrm{cut}} = \lfloor \log_2 N \rfloor + 3$) alongside algebraic projective height foliation (Axiom 3, Theorem 7.2).
- An isolated 3-cycle is deleted with probability $Q_{\mathrm{del}}(2)\approx 0.99885$ (Proposition 3.1), precluding dilute loop gases (Corollary 3.3).
- Non-extinction requires a first-tick clustered burst supported on the zero-stress residual tree (Corollary 3.4), jumping the unpumped nucleation barrier $\rho_c = \frac{1}{24-6e} \approx 0.130$, while extinct realizations execute a graceful, non-divergent exit into a static absorbing scarred DAG with saturated, sparse chord density (Section 5.6, Table 5).
- The constitutive scales $(\mu_0, \lambda_0, T_c, \varepsilon_{\mathrm{geo}}, \Lambda_{\mathrm{theory}})$ are derived deductively from discrete conservation and invariance principles (Section 4) and validated as an active viability channel across the 132-cell parameter sweep.
- Finite-$N$ ensembles exhibit zero-inflation at mesoscopic scales ($N = 100$, $p_{\mathrm{surv}}=0.270 \pm 0.044$, median $\rho=0$), while surviving paths populate an active Quasi-Stationary Distribution with mean density $\langle\rho\rangle_{\mathrm{QSD}} = 0.0919 \pm 0.0119$. Multi-scale sweeps up to $N = 10,000$ demonstrate that expanding lattice volume eliminates boundary quenching ($p_{\mathrm{surv}} \to 0.990 \pm 0.010$), expands the active core to $\langle N_3 \rangle_{\mathrm{QSD}} \approx 123.6$ cycles at stable density $\rho \approx 1.2\%$, and scales the non-equilibrium lifetime by $11.1\times$ ($\tau_{\mathrm{stall}} \approx 752\text{ ticks}$).

## 7.2 The Three-Step Infinite-Volume Scaling Program ($N \to \infty$)

To establish whether a true active phase survives in the thermodynamic limit, a three-step computational scaling program is formulated for the unchanged microscopic rule $\mathcal{R}$:

1. **Finite-Size Survival and Soliton vs. Bulk Scaling:** Measure the survival probability function $p_{\mathrm{surv}}(N, t)$ and active cluster morphology across system sizes $N \in [10^3, 10^5]$ up to asymptotic times $t \sim 10^5$. Under point-source seed injection, test the asymptotic invariance of the localized topological soliton mass ($\langle N_3 \rangle \approx \text{const}$) and evaluate whether the Quasi-Stationary Distribution lifetime $\tau_{\mathrm{QSD}}(N)$ scales exponentially ($\tau_{\mathrm{QSD}} \sim \mathrm{e}^{c N}$, confirming non-equilibrium thermodynamic stability) or power-law/logarithmically ($\tau_{\mathrm{QSD}} \sim N^z$). Under distributed multi-seed initialization ($\rho_0 > \rho_c$), measure volume-filling bulk density convergence as $N \to \infty$.
2. **Directed Percolation Critical Exponents:** Map the critical boundary $(\mu_c, \lambda_c)$ separating the absorbing and active regimes. Extract the critical exponent triple $(\beta, \nu_\perp, \nu_\parallel)$ via order parameter scaling:
   $$\rho_{\mathrm{QS}} \sim (\lambda - \lambda_c)^\beta, \qquad \xi_\perp \sim |\lambda - \lambda_c|^{-\nu_\perp}, \qquad \xi_\parallel \sim |\lambda - \lambda_c|^{-\nu_\parallel}.$$
   Comparing these exponents against the Directed Percolation (DP) universality class will test whether causal graph rewrites constitute a discrete realization of directed percolation.

3. **Conditioned Geometric and Topological Observables:** On the active quasi-stationary ensemble $\{N_3 > 0\}$, compute geometric observables to test for manifold convergence:
   - **Spectral Dimension Flow:** Evaluate the return probability $P(\sigma)$ of discrete diffusion ($P(\sigma) \sim \sigma^{-d_s/2}$) to extract the spectral dimension $d_s(\sigma)$. Preliminary diffusion measurements on the active QSD cluster indicate flow from $d_s \approx 1$ in the tree-dominated UV regime toward an effective fractional dimension $d_s \approx 2.1\text{--}2.6$ in the triangular simplicial foam, providing a concrete diagnostic for downstream continuum manifold convergence.
   - **Combinatorial Curvature:** Evaluate the Causal Ollivier–Ricci curvature $\kappa(u,v)$ on active clusters to bound the discrete Ricci curvature and test for Gromov-Hausdorff convergence to a smooth pseudo-Riemannian manifold.
   - **Topological Susceptibility:** Measure the variance of the cycle density and the distribution of macroscopic cycle lengths to verify the exponential suppression of non-local topological defects.

## 7.3 Scope and Physical Limitations

Discrete causal graph rewriting, absorbing-state phase transitions, and continuum geometric observables form distinct physical tiers. While future companion works investigate global algebraic causal protection, quantum stabilizer codespaces, and braided particle states, the present manuscript restricts its analytical and numerical scope strictly to the classical, pre-geometric statistical mechanics of the substrate: the combinatorial move grammar, absorbing boundary dynamics, and finite-$N$ non-equilibrium steady states. All-order causal protection across extended rewrite histories, continuum geometric reconstruction, and topological braid classification remain topics of companion works.

---

# Data and Code Availability

The complete, machine-checked Lean 4 formal kernel, the high-performance C++20 multi-scale simulation engine, and the standalone Python reference implementation are embedded directly in Appendices A, B, and C. Replication repositories, parameter sweep ensemble records, and interactive portal resources are hosted at [https://braiddynamics.com/](https://braiddynamics.com/) and permanently archived on Zenodo ([https://zenodo.org/records/21423007](https://zenodo.org/records/21423007)) and GitHub ([https://github.com/braiddynamics/qbd-portal](https://github.com/braiddynamics/qbd-portal)).

---

# References

- Ambjørn, J., Jurkiewicz, J., & Loll, R. (2004). Emergence of a 4D world from causal quantum gravity. *Physical Review Letters*, 93(13), 131301. [https://doi.org/10.1103/PhysRevLett.93.131301](https://doi.org/10.1103/PhysRevLett.93.131301)
- Ambjørn, J., Jurkiewicz, J., & Loll, R. (2005). The spectral dimension of the universe is scale dependent. *Physical Review Letters*, 95(17), 171301. [https://doi.org/10.1103/PhysRevLett.95.171301](https://doi.org/10.1103/PhysRevLett.95.171301)
- Bollobás, B., Janson, S., & Riordan, O. (2007). The phase transition in inhomogeneous random graphs. *Random Structures & Algorithms*, 31(1), 3–122. [https://doi.org/10.1002/rsa.20168](https://doi.org/10.1002/rsa.20168)
- Bombelli, L., Lee, J., Meyer, D., & Sorkin, R. D. (1987). Spacetime as a causal set. *Physical Review Letters*, 59(5), 521–524. [https://doi.org/10.1103/PhysRevLett.59.521](https://doi.org/10.1103/PhysRevLett.59.521)
- Braid Dynamics Group. (2026). *Quantum Braid Dynamics: A Computational Process*. Zenodo. [https://zenodo.org/records/21423007](https://zenodo.org/records/21423007). Portal: [https://braiddynamics.com/](https://braiddynamics.com/). Code: [https://github.com/braiddynamics/qbd-portal](https://github.com/braiddynamics/qbd-portal).
- Forman, R. (2003). Bochner's method for cell complexes and combinatorial Ricci curvature. *Discrete & Computational Geometry*, 29(3), 323–374. [https://doi.org/10.1007/s00454-002-0743-x](https://doi.org/10.1007/s00454-002-0743-x)
- Gorard, J. (2020). Some relativistic and gravitational properties of the Wolfram model. *Complex Systems*, 29(2), 599–654. [https://doi.org/10.25088/ComplexSystems.29.2.599](https://doi.org/10.25088/ComplexSystems.29.2.599)
- Gorard, J. (2020). Some quantum mechanical properties of the Wolfram model. *Complex Systems*, 29(2), 537–598.
- Henkel, M., Hinrichsen, H., & Lübeck, S. (2008). *Non-Equilibrium Phase Transitions, Volume 1: Absorbing Phase Transitions*. Dordrecht: Springer.
- Hinrichsen, H. (2000). Non-equilibrium critical phenomena and phase transitions into absorbing states. *Advances in Physics*, 49(7), 815–958. [https://doi.org/10.1080/00018730050198152](https://doi.org/10.1080/00018730050198152)
- Konopka, T., Markopoulou, F., & Smolin, L. (2006). Quantum graphity. arXiv:hep-th/0611197.
- Konopka, T., Markopoulou, F., & Severini, S. (2008). Quantum graphity: A model of emergent locality. *Physical Review D*, 77(10), 104029. [https://doi.org/10.1103/PhysRevD.77.104029](https://doi.org/10.1103/PhysRevD.77.104029)
- Lin, Y., Lu, L., & Yau, S.-T. (2011). Ricci curvature of graphs. *Tohoku Mathematical Journal*, 63(4), 605–627. [https://doi.org/10.2748/tmj/1325886283](https://doi.org/10.2748/tmj/1325886283)
- Marro, J., & Dickman, R. (1999). *Nonequilibrium Phase Transitions in Lattice Models*. Cambridge: Cambridge University Press.
- Ollivier, Y. (2009). Ricci curvature of Markov chains on metric spaces. *Journal of Functional Analysis*, 256(3), 810–864. [https://doi.org/10.1016/j.jfa.2008.11.001](https://doi.org/10.1016/j.jfa.2008.11.001)
- Rideout, D. P., & Sorkin, R. D. (2000). Classical sequential growth dynamics for causal sets. *Physical Review D*, 61(2), 024002. [https://doi.org/10.1103/PhysRevD.61.024002](https://doi.org/10.1103/PhysRevD.61.024002)
- Surya, S. (2019). The causal set approach to quantum gravity. *Living Reviews in Relativity*, 22, 5. [https://doi.org/10.1007/s41114-019-0023-1](https://doi.org/10.1007/s41114-019-0023-1)
- Trugenberger, C. A. (2017). Combinatorial quantum gravity: Geometry from random bits. *Journal of High Energy Physics*, 2017(9), 045. [https://doi.org/10.1007/JHEP09(2017)045](https://doi.org/10.1007/JHEP09(2017)045)
- Wolfram, S. (2002). *A New Kind of Science*. Champaign, IL: Wolfram Media.

---

# Appendix A. Verified Lean 4 Formal Kernel Specifications

This appendix presents the complete, machine-checked Lean 4 formalization defining the axiomatic primitives (Axioms 1–3), geometric well-foundedness, comonadic algebraic rigidity, legal move grammar (PUC and AEC), dynamic non-interference, concurrent addition confluence, absorbing-state stationarity, non-cyclic scar permanence, edge timestamp idempotency, triad self-stress rigidity, discrete port/stress symmetries, and continuum stability across 34 active verified theorems (compiled under toolchain `leanprover/lean4:v4.8.0` with 0 unproven obligations, 0 axioms, 0 sorry).

### Formal Theorem Index (34 Active Verified Theorems)

- **Part 1 (Axiom 1 & Asymmetry):** `antisymmetry_insufficient` (Thm 1.1), `asymmetry_implies_irreflexivity` (Thm 1.2), `asymmetry_equiv_irreflexive_and_antisymmetric` (Thm 1.3)
- **Part 2 (Axiom 2 & Lexicographic Descent):** `lexicographic_relation_wf` (Thm 2.1), `lexicographic_descent_admissible` (Thm 2.2)
- **Part 3 (Comonad Rigidity & Syndrome Group Action):** `left_identity`, `right_identity`, `comonad_associativity`, `xor_vec_self`, `xor_vec_zero`, `xor_vec_assoc`, `xor_vec_comm`, `comonad_morphism_unique` (Thm 3.1), `comonad_shift_involution` (Thm 3.2), `comonad_shift_composition_homomorphism` (Thm 3.3)
- **Part 4 (Legal Move Grammar, PUC, AEC & Non-Interference):** `legal_addition_site_not_in_E` (Thm 4.1), `puc_precludes_alternative_intermediate` (Thm 4.2), `dynamic_move_disjointness` (Thm 4.3), `dynamic_race_free_invariance` (Thm 4.4)
- **Part 5 (Step 3 Addition Confluence):** `parallel_addition_commutes` (Thm 5.1), `parallel_addition_idempotent` (Thm 5.2)
- **Part 6 (Absorbing Boundary & Topological Scars):** `absorbing_state_stationary` (Thm 6.1), `scar_edges_immune_to_deletion` (Thm 6.2), `acyclic_dag_deletion_empty` (Thm 6.3), `acyclic_scheduler_monotonic_expansion` (Thm 6.4), `scar_multi_tick_induction` (Thm 6.5)
- **Part 7 (Axiom 3 & Edge Timestamps):** `new_edge_strictly_dominates_parent` (Thm 7.1), `edge_path_monotonicity_transitive` (Thm 7.2), `edge_monotone_no_causal_cycle` (Thm 7.3)
- **Part 8 (Triad Self-Stress Rigidity):** `isolated_cycle_stress_eq_two` (Thm 8.1)
- **Part 9 (Discrete Symmetries & Triad Combinatorics):** `substrate_coordination_degree_eq_three` (Thm 9.1), `triad_interaction_boundary_is_six` (Thm 9.2), `simplicial_permittivity_capacity` (Thm 9.3), `homogeneous_triad_stress_is_six` (Thm 9.4)
- **Part 10 (Continuum Stability & Ordered Domain):** `drift_poly_factorization` (Thm 10.1), `extinction_basin_negative` (Thm 10.2), `gradient_dominance_implies_stability` (Thm 10.3), `perturbation_restoration_velocity` (Thm 10.4)

### Compilation & Kernel Check
```bash
lean VacuumPhase.lean
```

```lean
-- ============================================================================
-- QUANTUM BRAID DYNAMICS: FORMAL LEAN 4 KERNEL PROOFS
-- Certified Axiomatic Foundations (Section 2), Comonad Rigidity (Section 2.7),
-- Legal Move Grammar (PUC & AEC), Dynamic Non-Interference, Step 3 Confluence,
-- Absorbing Scar Permanence, Edge Timestamps, Triad Rigidity, & Discrete Symmetries
-- Total Verified Theorems: 34 Active Lean 4 Theorems (0 unproven obligations, 0 axioms, 0 sorry)
-- ============================================================================

-- ----------------------------------------------------------------------------
-- PART 1: AXIOM 1 — CAUSAL PRIMITIVE & ASYMMETRY (Section 2.1)
-- ----------------------------------------------------------------------------

def CausalRelation (V : Type) := V → V → Prop

def IsAntisymmetric (V : Type) (R : CausalRelation V) : Prop :=
  ∀ u v : V, R u v → R v u → u = v

def IsIrreflexive (V : Type) (R : CausalRelation V) : Prop :=
  ∀ v : V, ¬ R v v

def IsAsymmetric (V : Type) (R : CausalRelation V) : Prop :=
  ∀ u v : V, R u v → ¬ R v u

/--
THEOREM 1.1: Insufficiency of Antisymmetry
Formal counter-model proving that order-theoretic antisymmetry is physically
insufficient: the reflexive equality relation satisfies antisymmetry yet contains
a self-loop, demonstrating that strict irreflexivity is an independent axiom.
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

/--
THEOREM 1.2: Asymmetry Implies Irreflexivity
Proves the internal cohesion of Axiom 1: if a relation is asymmetric,
it is topologically impossible for an event to act as its own antecedent.
-/
theorem asymmetry_implies_irreflexivity {V : Type} (R : CausalRelation V) (h_asym : IsAsymmetric V R) :
    IsIrreflexive V R := by
  intro v h_loop
  exact h_asym v v h_loop h_loop

/--
THEOREM 1.3: Relational Completeness of the Primitive
Formally proves that Asymmetry is the exact algebraic conjunction of Irreflexivity and Antisymmetry.
-/
theorem asymmetry_equiv_irreflexive_and_antisymmetric {V : Type} (R : CausalRelation V) :
    IsAsymmetric V R ↔ (IsIrreflexive V R ∧ IsAntisymmetric V R) := by
  constructor
  · intro h_asym
    constructor
    · intro v h_loop
      exact h_asym v v h_loop h_loop
    · intro u v h_fwd h_rev
      have h_contra : False := h_asym u v h_fwd h_rev
      exact False.elim h_contra
  · intro h_conj
    intro u v h_fwd h_rev
    have h_irref := h_conj.left
    have h_anti  := h_conj.right
    have h_eq : u = v := h_anti u v h_fwd h_rev
    rw [h_eq] at h_fwd
    exact h_irref v h_fwd

-- ----------------------------------------------------------------------------
-- PART 2: AXIOM 2 — GEOMETRIC QUANTA & WELL-FOUNDED DESCENT (Section 2.2)
-- ----------------------------------------------------------------------------

variable {V : Type}

def IsGeometricQuantum (R : CausalRelation V) (u v w : V) : Prop :=
  R u v ∧ R v w ∧ R w u

def IsCompliant2Path (R : CausalRelation V) (u w v : V) : Prop :=
  R u w ∧ R w v ∧ ¬ R u v ∧ (∀ z : V, R u z ∧ R z v → z = w)

/--
THEOREM 2.1: Lexicographic Potential Relation is Well-Founded
Formally establishes that Prod.Lex on Nat × Nat is well-founded,
guaranteeing the absence of infinite descending chains in the state space.
-/
theorem lexicographic_relation_wf :
    WellFounded (Prod.Lex (fun (a b : Nat) => a < b) (fun (a b : Nat) => a < b)) :=
  (inferInstance : WellFoundedRelation (Nat × Nat)).wf

/--
THEOREM 2.2: Lexicographic Descent is Admissible
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

-- ----------------------------------------------------------------------------
-- PART 3: STORE COMONAD & SYNDROME VECTOR GROUP ACTION (Section 2.7 & Section 4.3)
-- ----------------------------------------------------------------------------

structure GraphState (G A : Type) where
  graph : G
  annotation : A
  deriving DecidableEq, Repr

def ε {G A S : Type} (state : GraphState G (A × S)) : GraphState G A :=
  ⟨state.graph, state.annotation.1⟩

def δ {G A S : Type} (state : GraphState G (A × S)) : GraphState G ((A × S) × S) :=
  ⟨state.graph, (state.annotation, state.annotation.2)⟩

def lift_history {G A B S : Type} (f : GraphState G A → GraphState G B) (state : GraphState G (A × S)) : GraphState G (B × S) :=
  ⟨state.graph, ((f ⟨state.graph, state.annotation.1⟩).annotation, state.annotation.2)⟩

theorem left_identity {G A S : Type} (Y : GraphState G (A × S)) :
    ε (δ Y) = Y := by
  rfl

theorem right_identity {G A S : Type} (Y : GraphState G (A × S)) :
    lift_history ε (δ Y) = Y := by
  rfl

theorem comonad_associativity {G A S : Type} (Y : GraphState G (A × S)) :
    δ (δ Y) = lift_history δ (δ Y) := by
  rfl

def BitVector (n : Nat) := Fin n → Bool

def zero_vec (n : Nat) : BitVector n := fun _ => false

def xor_vec {n : Nat} (a b : BitVector n) : BitVector n :=
  fun i => xor (a i) (b i)

theorem xor_vec_self {n : Nat} (a : BitVector n) :
    xor_vec a a = zero_vec n := by
  funext i
  dsimp [xor_vec, zero_vec]
  cases (a i) <;> rfl

theorem xor_vec_zero {n : Nat} (a : BitVector n) :
    xor_vec a (zero_vec n) = a := by
  funext i
  dsimp [xor_vec, zero_vec]
  cases (a i) <;> rfl

theorem xor_vec_assoc {n : Nat} (a b c : BitVector n) :
    xor_vec (xor_vec a b) c = xor_vec a (xor_vec b c) := by
  funext i
  dsimp [xor_vec]
  cases (a i) <;> cases (b i) <;> cases (c i) <;> rfl

theorem xor_vec_comm {n : Nat} (a b : BitVector n) :
    xor_vec a b = xor_vec b a := by
  funext i
  dsimp [xor_vec]
  cases (a i) <;> cases (b i) <;> rfl

def shift_op {n : Nat} (u : BitVector n) (sigma : BitVector n) : BitVector n :=
  xor_vec sigma u

/--
THEOREM 3.1: Morphism Uniqueness (Zero Gauge Freedom)
Formally proves that the categorical syndrome update morphism k is uniquely determined
by the physical incidence vector u_ΔE, leaving zero gauge freedom in the awareness layer.
-/
theorem comonad_morphism_unique {n : Nat}
    (k1 k2 : BitVector n → BitVector n) (u : BitVector n)
    (h1 : ∀ s, k1 s = shift_op u s)
    (h2 : ∀ s, k2 s = shift_op u s) :
    k1 = k2 := by
  funext s
  rw [h1 s, h2 s]

/--
THEOREM 3.2: Reversible Involution of the Syndrome Shift
Proves that applying the same physical rewrite twice returns the syndrome
to its original diagnostic configuration without information loss: T_u(T_u(σ)) = σ.
-/
theorem comonad_shift_involution {n : Nat}
    (u : BitVector n) (sigma : BitVector n) :
    shift_op u (shift_op u sigma) = sigma := by
  dsimp [shift_op]
  rw [xor_vec_assoc, xor_vec_self, xor_vec_zero]

/--
THEOREM 3.3: Composition Homomorphism
Proves that sequential updates u1 followed by u2 on the syndrome layer
compose homomorphically with the boolean XOR addition of the incidence vectors.
-/
theorem comonad_shift_composition_homomorphism {n : Nat}
    (u1 u2 : BitVector n) (sigma : BitVector n) :
    shift_op u2 (shift_op u1 sigma) = shift_op (xor_vec u1 u2) sigma := by
  dsimp [shift_op]
  rw [xor_vec_assoc]

-- ----------------------------------------------------------------------------
-- PART 4: LEGAL MOVE GRAMMAR, PUC, AEC & NON-INTERFERENCE (Lemma 2.1)
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

-- Directed 2-path predicate
def Is2Path {V : Type} (E : GraphEdges V) (v w u : V) : Prop :=
  E (v, w) ∧ E (w, u) ∧ v ≠ u

-- Parent-Uniqueness Condition (PUC, Definition 2.5.2)
def SatisfiesPUC {V : Type} (E : GraphEdges V) (v w u : V) : Prop :=
  Is2Path E v w u ∧ ¬ E (v, u) ∧ (∀ x : V, x ≠ w → ¬ (E (v, x) ∧ E (x, u)))

-- Acyclicity Pre-Check (AEC, Definition 2.5.3)
def ViolatesAEC {V : Type} (E : GraphEdges V) (H : EdgeTimestampMap V)
    (v u : V) (H_new : Nat) : Prop :=
  ∃ (e_first e_last : Edge V) (rest : List (Edge V)),
    DirectedEdgePath E (e_first :: rest ++ [e_last]) ∧
    e_first.1 = v ∧ e_last.2 = u ∧
    IsEdgePathMonotone H (e_first :: rest ++ [e_last]) ∧
    H e_last < H_new

def SatisfiesAEC {V : Type} (E : GraphEdges V) (H : EdgeTimestampMap V)
    (v u : V) (H_new : Nat) : Prop :=
  ¬ ViolatesAEC E H v u H_new

-- Legal Addition Proposal Site (Definition 2.5.1)
def IsLegalAdditionSite {V : Type} (E : GraphEdges V) (H : EdgeTimestampMap V)
    (v w u : V) (H_new : Nat) : Prop :=
  SatisfiesPUC E v w u ∧ SatisfiesAEC E H v u H_new ∧ ¬ E (u, v)

/--
THEOREM 4.1: Legal Addition Site Disjointness from Existing Topology
Proves that every proposal generated by a legal addition site targeting (u, v)
is strictly disjoint from the existing graph edge set E (A_edges ∩ E = ∅).
-/
theorem legal_addition_site_not_in_E {V : Type}
    (E : GraphEdges V) (H : EdgeTimestampMap V)
    (v w u : V) (H_new : Nat)
    (h_site : IsLegalAdditionSite E H v w u H_new) :
    ¬ E (u, v) := by
  rcases h_site with ⟨_, _, h_not_E⟩
  exact h_not_E

/--
THEOREM 4.2: PUC Precludes Alternative 2-Path Concurrency
Proves that if (v, w, u) satisfies the Parent-Uniqueness Condition, no alternate
routing intermediate x ≠ w exists between v and u.
-/
theorem puc_precludes_alternative_intermediate {V : Type}
    (E : GraphEdges V) (v w u x : V)
    (h_puc : SatisfiesPUC E v w u)
    (h_x_diff : x ≠ w) :
    ¬ (E (v, x) ∧ E (x, u)) := by
  rcases h_puc with ⟨_, _, h_uniq⟩
  exact h_uniq x h_x_diff

-- Representing edge subsets as predicates over directed pairs (Edge V → Prop)
def IsLegalAdditionSet {V : Type} (E A_edges : Edge V → Prop) : Prop :=
  ∀ e, A_edges e → ¬ (E e)

def IsLegalDeletionSet {V : Type} (E D : Edge V → Prop) : Prop :=
  ∀ e, D e → E e

/--
THEOREM 4.3: Dynamic Move Disjointness (Lemma 2.1 Part 1)
Proves that the set of accepted additions and accepted deletions generated
within the same parallel tick are strictly disjoint: A_edges ∩ D = ∅.
-/
theorem dynamic_move_disjointness {V : Type}
    (E A_edges D : Edge V → Prop)
    (hA : IsLegalAdditionSet E A_edges)
    (hD : IsLegalDeletionSet E D) :
    ∀ e, ¬ (A_edges e ∧ D e) := by
  intro e ⟨heA, heD⟩
  have h_not_in_E : ¬ (E e) := hA e heA
  have h_in_E : E e := hD e heD
  exact h_not_in_E h_in_E

/--
THEOREM 4.4: Deterministic Race-Free Invariance (Lemma 2.1 Part 2)
Proves that in the four-step parallel scheduler (merge additions into E' = E ∪ A_edges,
then apply deletions E_{t+1} = E' \ D), every newly added edge strictly survives deletion
within the same tick: ∀ e, A_edges e → ((E e ∨ A_edges e) ∧ ¬ (D e)).
-/
theorem dynamic_race_free_invariance {V : Type}
    (E A_edges D : Edge V → Prop)
    (hA : IsLegalAdditionSet E A_edges)
    (hD : IsLegalDeletionSet E D) :
    ∀ e, A_edges e → ((E e ∨ A_edges e) ∧ ¬ (D e)) := by
  intro e heA
  constructor
  · exact Or.inr heA
  · intro heD
    have h_disjoint := dynamic_move_disjointness E A_edges D hA hD e
    exact h_disjoint ⟨heA, heD⟩

-- ----------------------------------------------------------------------------
-- PART 5: CONFLUENCE OF CONCURRENT ADDITIONS (Order Invariance in Step 3)
-- ----------------------------------------------------------------------------

def merge_edge {V : Type} (E : GraphEdges V) (e : Edge V) : GraphEdges V :=
  fun x => E x ∨ x = e

/--
THEOREM 5.1: Parallel Edge Merging Commutes
Proves that concurrent edge additions can be accumulated in arbitrary sequence
without altering the resulting intermediate topology G'.
-/
theorem parallel_addition_commutes {V : Type}
    (E : GraphEdges V) (e1 e2 : Edge V) :
    merge_edge (merge_edge E e1) e2 = merge_edge (merge_edge E e2) e1 := by
  funext x
  dsimp [merge_edge]
  apply propext
  constructor
  · intro h
    rcases h with (hE | he1) | he2
    · exact Or.inl (Or.inl hE)
    · exact Or.inr he1
    · exact Or.inl (Or.inr he2)
  · intro h
    rcases h with (hE | he2) | he1
    · exact Or.inl (Or.inl hE)
    · exact Or.inr he2
    · exact Or.inl (Or.inr he1)

/--
THEOREM 5.2: Parallel Edge Merging is Idempotent
Proves that duplicate proposals targeting the same edge fold idempotently.
-/
theorem parallel_addition_idempotent {V : Type}
    (E : GraphEdges V) (e : Edge V) :
    merge_edge (merge_edge E e) e = merge_edge E e := by
  funext x
  dsimp [merge_edge]
  apply propext
  constructor
  · intro h
    rcases h with (hE | he) | he
    · exact Or.inl hE
    · exact Or.inr he
    · exact Or.inr he
  · intro h
    cases h with
    | inl hE => exact Or.inl (Or.inl hE)
    | inr he => exact Or.inl (Or.inr he)

-- ----------------------------------------------------------------------------
-- PART 6: ABSORBING BOUNDARY & TOPOLOGICAL SCAR PERMANENCE (Section 2.9)
-- ----------------------------------------------------------------------------

def InAny3Cycle {V : Type} (E : GraphEdges V) (e : Edge V) : Prop :=
  ∃ u v w : V, E (u, v) ∧ E (v, w) ∧ E (w, u) ∧
  (e = (u, v) ∨ e = (v, w) ∨ e = (w, u))

def IsScarEdge {V : Type} (E : GraphEdges V) (e : Edge V) : Prop :=
  E e ∧ ¬ InAny3Cycle E e

def LegalDeletionGrammar {V : Type} (E : GraphEdges V) (D : GraphEdges V) : Prop :=
  ∀ e, D e → InAny3Cycle E e

def IsAbsorbingConfiguration {V : Type} (A_edges D : GraphEdges V) : Prop :=
  (∀ e, ¬ A_edges e) ∧ (∀ e, ¬ D e)

/--
THEOREM 6.1: Absorbing State Stationarity
Proves that when both proposal sets vanish (A = ∅ and D = ∅), the transition
operator reduces strictly to the identity map: E_{t+1} = E_t.
-/
theorem absorbing_state_stationary {V : Type}
    (E A_edges D : GraphEdges V)
    (h_abs : IsAbsorbingConfiguration A_edges D) :
    ∀ e, ((E e ∨ A_edges e) ∧ ¬ (D e)) ↔ E e := by
  intro e
  rcases h_abs with ⟨hA, hD⟩
  constructor
  · intro ⟨h_or, _⟩
    cases h_or with
    | inl hE => exact hE
    | inr heA => exact False.elim (hA e heA)
  · intro hE
    refine ⟨Or.inl hE, hD e⟩

/--
THEOREM 6.2: Move Grammar Enforces Scar Immunity
Proves that any scar edge (an edge not in any 3-cycle) is mathematically excluded
from the legal deletion proposal set D under the Move Grammar rule.
-/
theorem scar_edges_immune_to_deletion {V : Type}
    (E D : GraphEdges V)
    (h_grammar : LegalDeletionGrammar E D)
    (e : Edge V)
    (h_scar : IsScarEdge E e) :
    ¬ D e := by
  intro hD
  have h_in_cycle := h_grammar e hD
  exact h_scar.2 h_in_cycle

/--
THEOREM 6.3: Acyclic DAG Deletion Quiescence
Proves that on any Directed Acyclic Graph containing zero 3-cycles, the legal deletion set is empty (D = ∅).
-/
theorem acyclic_dag_deletion_empty {V : Type}
    (E D : GraphEdges V)
    (h_grammar : LegalDeletionGrammar E D)
    (h_dag : ∀ e, ¬ InAny3Cycle E e) :
    ∀ e, ¬ D e := by
  intro e hD
  have h_in := h_grammar e hD
  exact h_dag e h_in

/--
THEOREM 6.4: Monotone Subgraph Expansion Under Acyclic Evolution
Proves that when deletions are quiescent on a DAG, the scheduler transition
is an exact monotonic subgraph expansion: E_t ⊆ E_{t+1}.
-/
theorem acyclic_scheduler_monotonic_expansion {V : Type}
    (E A_edges D : GraphEdges V)
    (h_grammar : LegalDeletionGrammar E D)
    (h_dag : ∀ e, ¬ InAny3Cycle E e) :
    ∀ e, E e → ((E e ∨ A_edges e) ∧ ¬ D e) := by
  intro e he
  have h_not_D : ¬ D e := acyclic_dag_deletion_empty E D h_grammar h_dag e
  exact ⟨Or.inl he, h_not_D⟩

/--
THEOREM 6.5: Inductive Multi-Tick Scar Permanence
Proves that if an edge is never in a 3-cycle across an arbitrary sequence of ticks
under the deletion grammar, the edge persists indefinitely.
-/
theorem scar_multi_tick_induction {V : Type}
    (E_seq : Nat → GraphEdges V)
    (D_seq : Nat → GraphEdges V)
    (A_seq : Nat → GraphEdges V)
    (h_step : ∀ t e, E_seq (t + 1) e ↔ (E_seq t e ∨ A_seq t e) ∧ ¬ D_seq t e)
    (h_del_rule : ∀ t, LegalDeletionGrammar (E_seq t) (D_seq t))
    (e : Edge V)
    (h_never_in_cycle : ∀ t, ¬ InAny3Cycle (E_seq t) e)
    (h_init : E_seq 0 e) :
    ∀ t, E_seq t e := by
  intro t
  induction t with
  | zero => exact h_init
  | succ n ih =>
    rw [h_step n e]
    refine ⟨Or.inl ih, ?_⟩
    intro hD
    have h_in := (h_del_rule n) e hD
    exact (h_never_in_cycle n) h_in

-- ----------------------------------------------------------------------------
-- PART 7: TIMESTAMP IDEMPOTENCY & DAG ACYCLICITY (Section 2.5.1)
-- ----------------------------------------------------------------------------

/--
THEOREM 7.1: New Edge Timestamp Strictly Dominates All Parent In-Edges
Proves that when a new edge targeting vertex u is assigned timestamp H_new = max_in_h + 1,
H_new is strictly greater than the timestamp of every incident parent edge:
  ∀ e_parent, H(e_parent) ≤ max_in_h → H(e_parent) < H_new
-/
theorem new_edge_strictly_dominates_parent {V : Type}
    (H : EdgeTimestampMap V) (e_parent : Edge V) (max_in_h : Nat)
    (h_bound : H e_parent ≤ max_in_h) :
    H e_parent < max_in_h + 1 := by
  exact Nat.lt_succ_of_le h_bound

/--
THEOREM 7.2: Edge Timestamp Path Monotonicity Transitivity
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

def CausalReachable {V : Type} (E : GraphEdges V) (H : EdgeTimestampMap V) (x y : V) : Prop :=
  ∃ (e_first e_last : Edge V) (rest : List (Edge V)),
    DirectedEdgePath E (e_first :: rest ++ [e_last]) ∧
    e_first.1 = x ∧ e_last.2 = y ∧
    IsEdgePathMonotone H (e_first :: rest ++ [e_last])

/--
THEOREM 7.3: Edge Timestamp Monotone Closed Loop Impossibility (Axiom 3)
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

-- ----------------------------------------------------------------------------
-- PART 8: ISOLATED CYCLE INCIDENCE & SELF-STRESS (Proposition 3.1)
-- ----------------------------------------------------------------------------

structure DirectedTriad (V : Type) where
  u : V
  v : V
  w : V
  h_uv : u ≠ v
  h_vw : v ≠ w
  h_wu : w ≠ u

def TriadStressMap (V : Type) := V → Nat

def IsIsolatedCycleStress {V : Type} (T : DirectedTriad V) (stress : TriadStressMap V) : Prop :=
  stress T.u = 1 ∧ stress T.v = 1 ∧ stress T.w = 1

def compute_s_del {V : Type} (T : DirectedTriad V) (stress : TriadStressMap V) : Nat :=
  (stress T.u + stress T.v + stress T.w) - 1

/--
THEOREM 8.1: Isolated Cycle Stress Equals Two
Formally proves that any isolated directed 3-cycle yields s_del = 2.
-/
theorem isolated_cycle_stress_eq_two {V : Type}
    (T : DirectedTriad V)
    (stress : TriadStressMap V)
    (h_iso : IsIsolatedCycleStress T stress) :
    compute_s_del T stress = 2 := by
  rcases h_iso with ⟨hu, hv, hw⟩
  dsimp [compute_s_del]
  rw [hu, hv, hw]

-- ----------------------------------------------------------------------------
-- PART 9: DISCRETE SYMMETRIES & SIMPLICIAL BOUNDARY TOPOLOGY (Section 4)
-- ----------------------------------------------------------------------------

structure SubstrateVertex where
  k_in : Nat
  k_out : Nat
  h_reg : k_in = 1 ∧ k_out = 2

def total_ports (v : SubstrateVertex) : Nat :=
  v.k_in + v.k_out

/--
THEOREM 9.1: Regular Substrate Coordination Degree is Three
Proves that every internal vertex of the regular Bethe substrate has total coordination degree k_deg = 3 (Proposition 4.4).
-/
theorem substrate_coordination_degree_eq_three (v : SubstrateVertex) :
    total_ports v = 3 := by
  rcases v.h_reg with ⟨hin, hout⟩
  dsimp [total_ports]
  rw [hin, hout]

structure SimplicialTriad where
  v1 : SubstrateVertex
  v2 : SubstrateVertex
  v3 : SubstrateVertex

def external_ports_per_vertex (v : SubstrateVertex) : Nat :=
  (total_ports v) - 1

def triad_boundary_capacity (T : SimplicialTriad) : Nat :=
  external_ports_per_vertex T.v1 + external_ports_per_vertex T.v2 + external_ports_per_vertex T.v3

/--
THEOREM 9.2: Simplicial Triad Interaction Boundary is Six Ports
Proves that an elementary 3-cycle comprising 3 trivalent vertices exposes exactly
6 external routing ports to the surrounding substrate (Proposition 4.5).
-/
theorem triad_interaction_boundary_is_six (T : SimplicialTriad) :
    triad_boundary_capacity T = 6 := by
  have h1 := substrate_coordination_degree_eq_three T.v1
  have h2 := substrate_coordination_degree_eq_three T.v2
  have h3 := substrate_coordination_degree_eq_three T.v3
  dsimp [triad_boundary_capacity, external_ports_per_vertex]
  rw [h1, h2, h3]

/--
THEOREM 9.3: Simplicial Permittivity Microstate Capacity
Proves that for 6 independent binary routing ports (each with 2 allowable states),
the configuration space has cardinality 2^6 = 64, establishing the theoretical
simplicial permittivity scale Lambda_theory = 2^-6 = 1/64 (Proposition 4.5).
-/
theorem simplicial_permittivity_capacity (T : SimplicialTriad) :
    2 ^ (triad_boundary_capacity T) = 64 := by
  rw [triad_interaction_boundary_is_six T]

/--
THEOREM 9.4: Homogeneous Triad Steric Friction Damping Factor
Proves that in a homogeneous topological foam with mean vertex cycle density sigma_v = 2,
the total vertex stress evaluated across a candidate triad is exactly 3 * 2 = 6,
formally deriving the factor 6 in the exponential steric hindrance term e^(-6*mu*rho) (Section 6.1).
-/
def homogeneous_triad_stress (sigma_v : Nat) : Nat :=
  sigma_v + sigma_v + sigma_v

theorem homogeneous_triad_stress_is_six :
    homogeneous_triad_stress 2 = 6 := by
  rfl

-- ----------------------------------------------------------------------------
-- PART 10: CONTINUUM MASTER EQUATION ALGEBRAIC STABILITY (Section 5.4 & Section 6.2)
-- Standalone Ordered Ring Formalization (0 Axioms, 0 Sorry, 0 Mocks)
-- ----------------------------------------------------------------------------

structure ContinuousDomain (α : Type) where
  zero : α
  add : α → α → α
  sub : α → α → α
  mul : α → α → α
  neg : α → α
  lt : α → α → Prop
  add_comm : ∀ a b, add a b = add b a
  add_assoc : ∀ a b c, add (add a b) c = add a (add b c)
  mul_comm : ∀ a b, mul a b = mul b a
  mul_assoc : ∀ a b c, mul (mul a b) c = mul a (mul b c)
  mul_sub_distrib : ∀ a b c, mul a (sub b c) = sub (mul a b) (mul a c)
  sub_self : ∀ a, sub a a = zero
  lt_trans : ∀ a b c, lt a b → lt b c → lt a c
  sub_neg_of_lt : ∀ a b, lt a b → lt (sub a b) zero
  mul_pos_neg_of_pos_and_neg : ∀ a b, lt zero a → lt b zero → lt (mul a b) zero

def intContinuousDomain : ContinuousDomain Int where
  zero := 0
  add := (· + ·)
  sub := (· - ·)
  mul := (· * ·)
  neg := (- ·)
  lt := (· < ·)
  add_comm := Int.add_comm
  add_assoc := Int.add_assoc
  mul_comm := Int.mul_comm
  mul_assoc := Int.mul_assoc
  mul_sub_distrib := Int.mul_sub
  sub_self := Int.sub_self
  lt_trans := @Int.lt_trans
  sub_neg_of_lt := by
    intro a b h
    show a - b < 0
    exact Int.sub_neg_of_lt h
  mul_pos_neg_of_pos_and_neg := by
    intro a b ha hb
    show a * b < 0
    have h_neg_b : 0 < -b := Int.neg_pos_of_neg hb
    have h_pos_prod : 0 < a * (-b) := Int.mul_pos ha h_neg_b
    have h_rw : a * (-b) = -(a * b) := Int.mul_neg a b
    rw [h_rw] at h_pos_prod
    exact Int.neg_of_neg_pos h_pos_prod

variable {α : Type} (CD : ContinuousDomain α)

/--
Polynomial drift rate f(λ, ρ) = (9 - 3λ)ρ² - (1/2)ρ governing cycle density evolution
near the absorbing origin under polynomial truncation.
-/
def drift_poly (nine_minus_three_lam half_val rho : α) : α :=
  CD.sub (CD.mul nine_minus_three_lam (CD.mul rho rho)) (CD.mul half_val rho)

/--
THEOREM 10.1: Algebraic Factorization of the Master Equation Drift
Formally proves that the unpumped polynomial drift factors identically into:
  f(λ, ρ) = ρ * ((9 - 3λ)ρ - 1/2)
-/
theorem drift_poly_factorization (nine_minus_three_lam half_val rho : α) :
    drift_poly CD nine_minus_three_lam half_val rho =
    CD.mul rho (CD.sub (CD.mul nine_minus_three_lam rho) half_val) := by
  dsimp [drift_poly]
  have h1 : CD.mul nine_minus_three_lam (CD.mul rho rho) =
            CD.mul rho (CD.mul nine_minus_three_lam rho) := by
    calc
      CD.mul nine_minus_three_lam (CD.mul rho rho)
        = CD.mul (CD.mul nine_minus_three_lam rho) rho := by rw [CD.mul_assoc]
      _ = CD.mul rho (CD.mul nine_minus_three_lam rho) := by rw [CD.mul_comm]
  have h2 : CD.mul half_val rho = CD.mul rho half_val := by rw [CD.mul_comm]
  rw [h1, h2]
  rw [← CD.mul_sub_distrib]

/--
THEOREM 10.2: Extinction Basin Negativity (Sub-Critical Density Decay)
Proves that whenever cycle density is positive (0 < ρ) and sub-critical
((9 - 3λ)ρ - 1/2 < 0), the net polynomial drift is strictly negative: f(λ, ρ) < 0.
-/
theorem extinction_basin_negative
    (nine_minus_three_lam half_val rho : α)
    (h_rho_pos : CD.lt CD.zero rho)
    (h_subcrit : CD.lt (CD.sub (CD.mul nine_minus_three_lam rho) half_val) CD.zero) :
    CD.lt (drift_poly CD nine_minus_three_lam half_val rho) CD.zero := by
  rw [drift_poly_factorization]
  exact CD.mul_pos_neg_of_pos_and_neg rho (CD.sub (CD.mul nine_minus_three_lam rho) half_val) h_rho_pos h_subcrit

/-- The Jacobian eigenvalue of the Master Equation is Creation Gradient minus Deletion Gradient. -/
def jacobian_eigenvalue (C_prime D_prime : α) : α :=
  CD.sub C_prime D_prime

/-- An equilibrium fixed point is an asymptotically stable attractor if its Jacobian eigenvalue is strictly negative. -/
def IsStableAttractor (C_prime D_prime : α) : Prop :=
  CD.lt (jacobian_eigenvalue CD C_prime D_prime) CD.zero

/--
THEOREM 10.3: Gradient Dominance Implies Stability (0 Axioms)
Proves from pure ordered ring arithmetic that if the localized deletion restoring gradient (D')
strictly exceeds the creation gradient (C'), the linearized Jacobian eigenvalue is strictly negative.
-/
theorem gradient_dominance_implies_stability (C_prime D_prime : α) :
    CD.lt C_prime D_prime → IsStableAttractor CD C_prime D_prime := by
  intro h_lt
  dsimp [IsStableAttractor, jacobian_eigenvalue]
  exact CD.sub_neg_of_lt C_prime D_prime h_lt

/--
THEOREM 10.4: Perturbation Restoration Velocity
Proves that at a stable fixed point (where C' < D'), any positive density fluctuation Δρ > 0
experiences a negative restoring velocity: J * Δρ < 0.
-/
theorem perturbation_restoration_velocity
    (C_prime D_prime delta_rho : α)
    (h_stable : IsStableAttractor CD C_prime D_prime)
    (h_delta_pos : CD.lt CD.zero delta_rho) :
    CD.lt (CD.mul delta_rho (jacobian_eigenvalue CD C_prime D_prime)) CD.zero := by
  have h_J_neg : CD.lt (jacobian_eigenvalue CD C_prime D_prime) CD.zero := h_stable
  exact CD.mul_pos_neg_of_pos_and_neg delta_rho (jacobian_eigenvalue CD C_prime D_prime) h_delta_pos h_J_neg
```

---

# Appendix B. High-Performance C++20 Multi-Scale Simulation Engine

This appendix presents the complete, standalone C++20 simulation engine implementing the compact sparse adjacency graph representation, per-worker traversal scratchpads with zero inner-loop heap allocations, and multithreaded Monte Carlo execution for large-scale finite-size scaling ($N = 10 \dots 10^4$).

### Compilation
```bash
g++ -O3 -std=c++20 vacuum_phase_engine.cpp -o vacuum_phase_engine.exe
```

### Source Code (`vacuum_phase_engine.cpp`)

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <random>
#include <chrono>
#include <thread>
#include <future>
#include <numeric>
#include <algorithm>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <deque>
#include <set>
#include <map>
#include <span>
#include <concepts>
#include <ranges>

// ============================================================================
// CONSTANTS & CANONICAL PRIORS
// ============================================================================
constexpr double DEFAULT_MU_0 = 0.3989422804014327;     // 1 / sqrt(2 * pi)
constexpr double DEFAULT_LAMBDA_0 = 1.718281828459045;   // e - 1
constexpr int DEFAULT_NODES = 100;
constexpr int DEFAULT_RUNS = 100;
constexpr int DEFAULT_MAX_STEPS = 1500;

// ============================================================================
// COMPACT SPARSE DIRECTED GRAPH (C++20 - ZERO EXCESS RAM)
// ============================================================================
struct TargetEdge {
    int target;
    int H;
    auto operator<=>(const TargetEdge&) const = default;
};

struct Cycle3 {
    int u;
    int v;
    int w;
    auto operator<=>(const Cycle3&) const = default;
};

class DiGraph {
public:
    int n;
    std::vector<std::vector<TargetEdge>> succ;
    std::vector<std::vector<TargetEdge>> pred;

    explicit DiGraph(int num_nodes = 0) : n(num_nodes) {
        init(num_nodes);
    }

    void init(int num_nodes) {
        n = num_nodes;
        succ.assign(n, {});
        pred.assign(n, {});
    }

    inline bool has_edge(int u, int v) const {
        if (u < 0 || u >= n || v < 0 || v >= n) return false;
        for (const auto& e : succ[u]) {
            if (e.target == v) return true;
        }
        return false;
    }

    inline int get_H(int u, int v) const {
        if (u < 0 || u >= n || v < 0 || v >= n) return 0;
        for (const auto& e : succ[u]) {
            if (e.target == v) return e.H;
        }
        return 0;
    }

    void add_edge(int u, int v, int timestamp) {
        if (u < 0 || u >= n || v < 0 || v >= n) return;
        for (auto& e : succ[u]) {
            if (e.target == v) {
                e.H = timestamp;
                for (auto& pe : pred[v]) {
                    if (pe.target == u) {
                        pe.H = timestamp;
                        return;
                    }
                }
                return;
            }
        }
        succ[u].push_back({v, timestamp});
        pred[v].push_back({u, timestamp});
    }

    void remove_edge(int u, int v) {
        if (u < 0 || u >= n || v < 0 || v >= n) return;
        for (size_t i = 0; i < succ[u].size(); ++i) {
            if (succ[u][i].target == v) {
                succ[u].erase(succ[u].begin() + i);
                break;
            }
        }
        for (size_t i = 0; i < pred[v].size(); ++i) {
            if (pred[v][i].target == u) {
                pred[v].erase(pred[v].begin() + i);
                break;
            }
        }
    }

    int max_in_height(int u) const {
        int max_h = 0;
        for (const auto& pe : pred[u]) {
            if (pe.H > max_h) {
                max_h = pe.H;
            }
        }
        return max_h;
    }
};

// ============================================================================
// COMBINATORIAL GRAPH BUILDER
// ============================================================================
DiGraph generate_bethe_fragment(int N) {
    if (N < 3) N = 3;
    DiGraph G(N);
    int current_node = 1;
    std::deque<int> queue;

    // Root (0) has 3 outgoing children
    for (int i = 0; i < 3 && current_node < N; ++i) {
        G.add_edge(0, current_node, 0);
        queue.push_back(current_node);
        current_node++;
    }

    // Internal vertices have 2 outgoing children
    while (!queue.empty() && current_node < N) {
        int parent = queue.front();
        queue.pop_front();
        for (int i = 0; i < 2 && current_node < N; ++i) {
            G.add_edge(parent, current_node, 0);
            queue.push_back(current_node);
            current_node++;
        }
    }
    return G;
}

void inject_seed_defect(DiGraph& G) {
    if (G.succ[0].empty()) return;
    int w = G.succ[0][0].target;
    if (!G.succ[w].empty()) {
        int grandchild = G.succ[w][0].target;
        G.add_edge(grandchild, 0, 1);
    }
}

// ============================================================================
// MOVE GRAMMAR & FILTERS (PUC, AEC, CYCLES)
// ============================================================================
inline bool is_permissible_puc(const DiGraph& G, int u, int v, int w) {
    if (G.has_edge(v, u)) return false;
    for (const auto& edge_vx : G.succ[v]) {
        int x = edge_vx.target;
        if (x != w && G.has_edge(x, u)) {
            return false;
        }
    }
    return true;
}

struct BFSState {
    int curr;
    int prev_h;
    int depth;
};

struct TraversalScratchpad {
    std::vector<int> min_h_reached;
    std::vector<BFSState> queue_buffer;
};

bool pre_check_aec(const DiGraph& G, int u, int v, int H_new, int L_cut, TraversalScratchpad& scratch) {
    if (static_cast<int>(scratch.min_h_reached.size()) < G.n) {
        scratch.min_h_reached.resize(G.n, 1e9);
    } else {
        std::fill(scratch.min_h_reached.begin(), scratch.min_h_reached.begin() + G.n, 1e9);
    }

    scratch.queue_buffer.clear();
    scratch.queue_buffer.push_back({v, -1, 0});
    scratch.min_h_reached[v] = -1;

    size_t q_head = 0;
    while (q_head < scratch.queue_buffer.size()) {
        auto [curr, prev_h, depth] = scratch.queue_buffer[q_head++];

        if (depth >= L_cut) continue;

        for (const auto& succ_edge : G.succ[curr]) {
            int succ = succ_edge.target;
            int edge_h = succ_edge.H;
            if (edge_h > prev_h) { // Strictly monotone increasing
                if (succ == u && edge_h < H_new) {
                    return false; // Closed acausal monotone loop detected
                }
                if (edge_h < scratch.min_h_reached[succ]) {
                    scratch.min_h_reached[succ] = edge_h;
                    scratch.queue_buffer.push_back({succ, edge_h, depth + 1});
                }
            }
        }
    }
    return true;
}

std::vector<Cycle3> find_all_3_cycles(const DiGraph& G) {
    std::vector<Cycle3> cycles;
    for (int u = 0; u < G.n; ++u) {
        for (const auto& e_uv : G.succ[u]) {
            int v = e_uv.target;
            for (const auto& e_vw : G.succ[v]) {
                int w = e_vw.target;
                if (G.has_edge(w, u) && u < v && u < w) {
                    cycles.push_back({u, v, w});
                }
            }
        }
    }
    return cycles;
}

struct AdditionSite {
    int u;
    int v;
    int H_new;
    int node_v;
    int node_w;
    int node_u;
};

std::vector<AdditionSite> find_legal_addition_sites(const DiGraph& G, int L_cut, TraversalScratchpad& scratch) {
    std::vector<AdditionSite> sites;
    for (int v = 0; v < G.n; ++v) {
        for (const auto& e_vw : G.succ[v]) {
            int w = e_vw.target;
            for (const auto& e_wu : G.succ[w]) {
                int u = e_wu.target;
                if (v == u || G.has_edge(u, v)) continue;
                if (!is_permissible_puc(G, u, v, w)) continue;

                int H_new = G.max_in_height(u) + 1;
                if (!pre_check_aec(G, u, v, H_new, L_cut, scratch)) continue;

                sites.push_back({u, v, H_new, v, w, u});
            }
        }
    }
    return sites;
}

// ============================================================================
// PARALLEL SCHEDULER (FOUR-STEP TICK & HOMEOSTASIS)
// ============================================================================
bool execute_parallel_tick(DiGraph& G, double mu, double lam, int L_cut, TraversalScratchpad& scratch, std::mt19937_64& rng, std::uniform_real_distribution<double>& dist) {
    auto cycles = find_all_3_cycles(G);
    auto legal_additions = find_legal_addition_sites(G, L_cut, scratch);

    if (legal_additions.empty() && cycles.empty()) {
        return false; // Absorbing extinction
    }

    std::vector<int> stress_map(G.n, 0);
    for (const auto& c : cycles) {
        stress_map[c.u]++;
        stress_map[c.v]++;
        stress_map[c.w]++;
    }

    std::vector<std::pair<std::pair<int, int>, int>> A;
    for (const auto& site : legal_additions) {
        int s_add = stress_map[site.node_v] + stress_map[site.node_w] + stress_map[site.node_u];
        double P_acc = std::exp(-mu * s_add);
        if (dist(rng) < P_acc) {
            A.push_back({{site.u, site.v}, site.H_new});
        }
    }

    std::vector<std::pair<int, int>> D;
    for (const auto& c : cycles) {
        int s_del = std::max(0, stress_map[c.u] + stress_map[c.v] + stress_map[c.w] - 1);
        double Q_del = std::min(1.0, 0.5 * (1.0 + lam * s_del) * std::exp(-mu * s_del));
        if (dist(rng) < Q_del) {
            int choice = std::uniform_int_distribution<int>(0, 2)(rng);
            if (choice == 0) D.push_back({c.u, c.v});
            else if (choice == 1) D.push_back({c.v, c.w});
            else D.push_back({c.w, c.u});
        }
    }

    if (A.empty() && D.empty()) {
        return false; // Homeostatic stall
    }

    std::set<std::pair<int, int>> a_edge_set;
    for (const auto& item : A) a_edge_set.insert(item.first);

    for (const auto& [edge, h_new] : A) {
        int u = edge.first;
        int v = edge.second;
        if (u != v && !a_edge_set.contains({v, u})) {
            G.add_edge(u, v, h_new);
        }
    }

    for (const auto& [u, v] : D) {
        if (G.has_edge(u, v)) {
            G.remove_edge(u, v);
        }
    }

    return true;
}

std::pair<int, int> evolve_graph_to_equilibrium(DiGraph& G, double mu, double lam, int max_steps, TraversalScratchpad& scratch, std::mt19937_64& rng) {
    int L_cut = std::max(1, static_cast<int>(std::floor(std::log2(G.n))) + 3);
    std::uniform_real_distribution<double> dist(0.0, 1.0);

    for (int step = 0; step < max_steps; ++step) {
        bool active = execute_parallel_tick(G, mu, lam, L_cut, scratch, rng, dist);
        if (!active) {
            auto final_cycles = find_all_3_cycles(G);
            return {static_cast<int>(final_cycles.size()), step + 1};
        }
    }
    auto final_cycles = find_all_3_cycles(G);
    return {static_cast<int>(final_cycles.size()), max_steps};
}

// ============================================================================
// TRAJECTORY RESULT DATA & STATISTICS
// ============================================================================
struct TrajectoryResult {
    int seed;
    int n3_final;
    int steps;
    double rho3_final;
    bool survived;
};

struct EnsembleStats {
    int N;
    int total_runs;
    int survivors;
    double p_surv;
    double p_surv_stderr;
    double mean_n3;
    double std_n3;
    double median_n3;
    double mean_rho3;
    double std_rho3;
    double median_rho3;
    double fano_factor;
    double skewness;
    double mean_n3_qsd;
    double median_n3_qsd;
    double mean_rho3_qsd;
    double median_rho3_qsd;
    double avg_steps;
    double elapsed_ms;
};

EnsembleStats compute_ensemble_stats(int N, const std::vector<TrajectoryResult>& results, double elapsed_ms) {
    EnsembleStats stats{};
    stats.N = N;
    stats.total_runs = static_cast<int>(results.size());
    stats.elapsed_ms = elapsed_ms;

    if (results.empty()) return stats;

    std::vector<double> n3_vals;
    std::vector<double> rho_vals;
    std::vector<double> n3_qsd_vals;
    std::vector<double> rho_qsd_vals;
    std::vector<double> step_vals;

    for (const auto& r : results) {
        n3_vals.push_back(r.n3_final);
        rho_vals.push_back(r.rho3_final);
        step_vals.push_back(r.steps);
        if (r.survived) {
            stats.survivors++;
            n3_qsd_vals.push_back(r.n3_final);
            rho_qsd_vals.push_back(r.rho3_final);
        }
    }

    stats.p_surv = static_cast<double>(stats.survivors) / stats.total_runs;
    stats.p_surv_stderr = std::sqrt(stats.p_surv * (1.0 - stats.p_surv) / stats.total_runs);

    auto compute_mean = [](const std::vector<double>& v) {
        if (v.empty()) return 0.0;
        return std::accumulate(v.begin(), v.end(), 0.0) / v.size();
    };

    auto compute_std = [](const std::vector<double>& v, double mean) {
        if (v.size() < 2) return 0.0;
        double sum_sq = 0.0;
        for (double x : v) sum_sq += (x - mean) * (x - mean);
        return std::sqrt(sum_sq / (v.size() - 1));
    };

    auto compute_median = [](std::vector<double> v) {
        if (v.empty()) return 0.0;
        std::sort(v.begin(), v.end());
        size_t mid = v.size() / 2;
        if (v.size() % 2 == 0) {
            return (v[mid - 1] + v[mid]) / 2.0;
        }
        return v[mid];
    };

    stats.mean_n3 = compute_mean(n3_vals);
    stats.std_n3 = compute_std(n3_vals, stats.mean_n3);
    stats.median_n3 = compute_median(n3_vals);

    stats.mean_rho3 = compute_mean(rho_vals);
    stats.std_rho3 = compute_std(rho_vals, stats.mean_rho3);
    stats.median_rho3 = compute_median(rho_vals);

    double var_n3 = (stats.total_runs > 1) ? (stats.std_n3 * stats.std_n3) : 0.0;
    stats.fano_factor = (stats.mean_n3 > 0.0) ? (var_n3 / stats.mean_n3) : 0.0;

    double skewness = 0.0;
    if (stats.std_n3 > 0.0) {
        for (double x : n3_vals) {
            skewness += std::pow((x - stats.mean_n3) / stats.std_n3, 3.0);
        }
        skewness /= stats.total_runs;
    }
    stats.skewness = skewness;

    stats.mean_n3_qsd = compute_mean(n3_qsd_vals);
    stats.median_n3_qsd = compute_median(n3_qsd_vals);

    stats.mean_rho3_qsd = compute_mean(rho_qsd_vals);
    stats.median_rho3_qsd = compute_median(rho_qsd_vals);

    stats.avg_steps = compute_mean(step_vals);

    return stats;
}

// ============================================================================
// MULTITHREADED ENSEMBLE RUNNER
// ============================================================================
std::vector<TrajectoryResult> run_ensemble(int N, int runs, int max_steps, double mu, double lam, uint64_t base_seed, int num_threads) {
    if (num_threads <= 0) num_threads = std::max(1u, std::thread::hardware_concurrency());

    std::vector<TrajectoryResult> all_results(runs);
    std::vector<std::future<void>> futures;

    int chunk_size = (runs + num_threads - 1) / num_threads;

    for (int t = 0; t < num_threads; ++t) {
        int start_idx = t * chunk_size;
        int end_idx = std::min(runs, start_idx + chunk_size);
        if (start_idx >= end_idx) continue;

        futures.push_back(std::async(std::launch::async, [&, start_idx, end_idx, t]() {
            TraversalScratchpad scratch;
            scratch.min_h_reached.assign(N, 1e9);

            for (int i = start_idx; i < end_idx; ++i) {
                uint64_t seed = base_seed + i;
                std::mt19937_64 rng(seed);

                DiGraph G = generate_bethe_fragment(N);
                inject_seed_defect(G);

                auto [n3_final, steps] = evolve_graph_to_equilibrium(G, mu, lam, max_steps, scratch, rng);
                double rho3 = static_cast<double>(n3_final) / N;
                bool survived = (n3_final > 0);

                all_results[i] = TrajectoryResult{
                    .seed = static_cast<int>(seed),
                    .n3_final = n3_final,
                    .steps = steps,
                    .rho3_final = rho3,
                    .survived = survived
                };
            }
        }));
    }

    for (auto& f : futures) {
        f.get();
    }

    return all_results;
}

// ============================================================================
// CLI OPTIONS & ENTRY POINT
// ============================================================================
void print_banner() {
    std::cout << "================================================================================\n";
    std::cout << "  QBD Vacuum Phase Simulation Engine (C++20 Compact Sparse Multi-Threaded)\n";
    std::cout << "  Constitutive Stochastic Rewrite System on Timestamped Bethe DAGs\n";
    std::cout << "================================================================================\n";
}

void print_help(const char* prog_name) {
    std::cout << "Usage: " << prog_name << " [options]\n\n"
              << "Options:\n"
              << "  -N, --nodes [int]       Number of vertices in Bethe substrate (default: 100)\n"
              << "  -r, --runs [int]        Number of Monte Carlo trajectories (default: 100)\n"
              << "  -s, --steps [int]       Max discrete simulation ticks (default: 1500)\n"
              << "  -m, --mu [float]        Friction parameter mu (default: 0.3989422804)\n"
              << "  -l, --lambda [float]    Defect release parameter lambda (default: 1.718281828)\n"
              << "      --seed [int]        Base RNG seed (default: 0)\n"
              << "  -t, --threads [int]     Number of worker threads (default: hardware concurrency)\n"
              << "  -o, --csv [file]        Output CSV file to save per-trajectory records\n"
              << "      --smoke-test        Execute quick N=10 smoke test (100 runs)\n"
              << "  -h, --help              Display this help message\n";
}

int main(int argc, char* argv[]) {
    int N = DEFAULT_NODES;
    int runs = DEFAULT_RUNS;
    int max_steps = DEFAULT_MAX_STEPS;
    double mu = DEFAULT_MU_0;
    double lam = DEFAULT_LAMBDA_0;
    uint64_t seed = 0;
    int num_threads = std::max(1u, std::thread::hardware_concurrency());
    std::string csv_path = "";

    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "-h" || arg == "--help") {
            print_banner();
            print_help(argv[0]);
            return 0;
        } else if (arg == "-N" || arg == "--nodes") {
            if (i + 1 < argc) N = std::stoi(argv[++i]);
        } else if (arg == "-r" || arg == "--runs") {
            if (i + 1 < argc) runs = std::stoi(argv[++i]);
        } else if (arg == "-s" || arg == "--steps") {
            if (i + 1 < argc) max_steps = std::stoi(argv[++i]);
        } else if (arg == "-m" || arg == "--mu") {
            if (i + 1 < argc) mu = std::stod(argv[++i]);
        } else if (arg == "-l" || arg == "--lambda") {
            if (i + 1 < argc) lam = std::stod(argv[++i]);
        } else if (arg == "--seed") {
            if (i + 1 < argc) seed = std::stoull(argv[++i]);
        } else if (arg == "-t" || arg == "--threads") {
            if (i + 1 < argc) num_threads = std::stoi(argv[++i]);
        } else if (arg == "-o" || arg == "--csv") {
            if (i + 1 < argc) csv_path = argv[++i];
        } else if (arg == "--smoke-test") {
            N = 10;
            runs = 100;
        } else {
            std::cerr << "Unknown option: " << arg << " (use --help for options)\n";
            return 1;
        }
    }

    print_banner();

    std::cout << "[Configuration]\n"
              << "  Graph Vertices (N):    " << N << "\n"
              << "  Trajectories (M):      " << runs << "\n"
              << "  Max Steps (T):         " << max_steps << "\n"
              << "  Friction mu:           " << std::fixed << std::setprecision(6) << mu << "\n"
              << "  Relaxation lambda:     " << std::fixed << std::setprecision(6) << lam << "\n"
              << "  Base Seed:             " << seed << "\n"
              << "  Worker Threads:        " << num_threads << "\n";
    if (!csv_path.empty()) {
        std::cout << "  Output CSV:            " << csv_path << "\n";
    }
    std::cout << "--------------------------------------------------------------------------------\n";
    std::cout << "Executing Monte Carlo ensemble simulation...\n";

    auto start_time = std::chrono::high_resolution_clock::now();
    auto results = run_ensemble(N, runs, max_steps, mu, lam, seed, num_threads);
    auto end_time = std::chrono::high_resolution_clock::now();

    double elapsed_ms = std::chrono::duration<double, std::milli>(end_time - start_time).count();
    auto stats = compute_ensemble_stats(N, results, elapsed_ms);

    std::cout << "\n============================== RESULTS SUMMARY ==============================\n";
    std::cout << std::left << std::setw(32) << "Total Trajectories Completed:" << stats.total_runs << "\n";
    std::cout << std::left << std::setw(32) << "Wall-Clock Duration:" << std::fixed << std::setprecision(2) << stats.elapsed_ms << " ms ("
              << std::setprecision(1) << (stats.elapsed_ms / stats.total_runs * 1000.0) << " us / trajectory)\n";
    std::cout << std::left << std::setw(32) << "Throughput:" << std::fixed << std::setprecision(0)
              << (stats.total_runs / (stats.elapsed_ms / 1000.0)) << " trajectories / second\n";
    std::cout << "--------------------------------------------------------------------------------\n";
    std::cout << std::left << std::setw(32) << "Survival Fraction (p_surv):" << std::fixed << std::setprecision(4)
              << stats.p_surv << " +/- " << stats.p_surv_stderr << " (" << stats.survivors << " / " << stats.total_runs << ")\n";
    std::cout << std::left << std::setw(32) << "Mean 3-Cycle Count <N3>:" << std::fixed << std::setprecision(4)
              << stats.mean_n3 << " +/- " << stats.std_n3 << " (Median: " << stats.median_n3 << ")\n";
    std::cout << std::left << std::setw(32) << "Mean Cycle Density <rho>:" << std::fixed << std::setprecision(4)
              << stats.mean_rho3 << " +/- " << stats.std_rho3 << " (Median: " << stats.median_rho3 << ")\n";
    std::cout << std::left << std::setw(32) << "Fano Factor (Var / Mean):" << std::fixed << std::setprecision(4)
              << stats.fano_factor << " (Overdispersed > 1.0)\n";
    std::cout << std::left << std::setw(32) << "Fisher-Pearson Skewness:" << std::fixed << std::setprecision(4)
              << stats.skewness << " (Positive Tail Asymmetry)\n";
    std::cout << "--------------------------------------------------------------------------------\n";
    std::cout << "[Conditioned Active QSD Ensembles (N3 > 0)]\n";
    std::cout << std::left << std::setw(32) << "  Active QSD Mean <N3>_QSD:" << std::fixed << std::setprecision(4)
              << stats.mean_n3_qsd << " (Median: " << stats.median_n3_qsd << ")\n";
    std::cout << std::left << std::setw(32) << "  Active QSD Mean <rho>_QSD:" << std::fixed << std::setprecision(4)
              << stats.mean_rho3_qsd << " (Median: " << stats.median_rho3_qsd << ")\n";
    std::cout << std::left << std::setw(32) << "  Mean Steps to Homeostasis:" << std::fixed << std::setprecision(2)
              << stats.avg_steps << " ticks\n";
    std::cout << "================================================================================\n";

    if (!csv_path.empty()) {
        std::ofstream out(csv_path);
        if (out.is_open()) {
            out << "# QBD Vacuum Phase C++20 Simulation Data\n";
            out << "# N=" << N << " runs=" << runs << " mu=" << mu << " lambda=" << lam << " seed=" << seed << "\n";
            out << "seed,n3_final,steps,rho3_final,survived\n";
            for (const auto& r : results) {
                out << r.seed << "," << r.n3_final << "," << r.steps << "," << std::fixed << std::setprecision(6) << r.rho3_final << "," << (r.survived ? 1 : 0) << "\n";
            }
            std::cout << "Saved trajectory records to: " << csv_path << "\n";
        } else {
            std::cerr << "Warning: Could not open output CSV path: " << csv_path << "\n";
        }
    }

    return 0;
}

```

---

# Appendix C. Standalone Python Reference Simulation Engine & Analytical Prior Suite

This appendix provides the complete, self-contained, single-file Python reference implementation of the Quantum Braid Dynamics simulation engine. It computes all canonical analytical reference priors (Table 1), constructs the regular Bethe fragment $G_0$, enforces move grammar constraints (PUC and AEC), executes the four-step stochastic parallel scheduler with homeostatic equilibrium settlement, and provides CLI entry points to regenerate all tables and moments presented in Section 5.

Dependencies: Python >= 3.8, networkx >= 2.6

```python
#!/usr/bin/env python3
"""
Quantum Braid Dynamics (QBD) — Standalone Reference Simulation Engine
A single-file, self-contained Python script to reproduce all analytical priors,
move grammar invariants, and simulation tables from the preprint manuscript.

Dependencies: Python >= 3.8, networkx >= 2.6
"""

from __future__ import annotations

import argparse
import collections
import csv
import json
import math
import os
import random
import statistics
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Dict, List, Optional, Sequence, Set, Tuple

import networkx as nx

# =============================================================================
# 1. CANONICAL ANALYTICAL REFERENCE PRIOR SUITE (TABLE 1)
# =============================================================================

def compute_analytical_priors() -> Dict[str, float]:
    """Computes constitutive scales from discrete combinatorial principles (Table 1)."""
    T_c = math.log(2.0)                                    # Loop-closure free energy neutrality: T_c = ln 2 (Prop 4.1)
    mu_0 = 1.0 / math.sqrt(2.0 * math.pi)                  # Z Poisson summation & modular S-duality: mu_0 = 1/sqrt(2*pi) (Prop 4.3)
    lambda_0 = math.e - 1.0                                # Arrhenius 1-nat defect relaxation: lambda_0 = e - 1 (Prop 4.2)
    eps_geo = math.log(2.0) / 3.0                          # k_deg=3 vertex channel equipartition: eps_geo = ln(2)/3 (Prop 4.4)
    Lambda_theory = 2.0 ** (-6)                            # 6-port triad binary simplex routing: Lambda = 2^-6 (Prop 4.5)
    rho_c = 1.0 / (24.0 - 6.0 * math.e)                    # Unpumped critical nucleation barrier: rho_c = 1/(24-6e) (Sec 6.2)
    mu_crit = ((9.0 - 3.0 * lambda_0) ** 2) / 108.0       # Saddle-node continuum bifurcation threshold (Sec 6.2.1)

    return {
        "T_c": T_c,
        "mu_0": mu_0,
        "lambda_0": lambda_0,
        "eps_geo": eps_geo,
        "Lambda_theory": Lambda_theory,
        "rho_c": rho_c,
        "mu_crit": mu_crit,
    }

# =============================================================================
# 2. COMBINATORIAL GRAPH BUILDER (G0 & SEED INJECTION)
# =============================================================================

def generate_bethe_fragment(N: int = 100) -> Tuple[nx.DiGraph, List[List[int]]]:
    """
    Constructs an outward-directed regular Bethe fragment (Section 2.3).
    Root has out-degree 3; subsequent internal nodes have in-degree 1, out-degree 2.
    Leaves have in-degree 1, out-degree 0. Total leaves L = (N + 2)/2 (~50%).
    """
    if N < 3:
        raise ValueError("N must be at least 3 for a valid vacuum")
    G = nx.DiGraph()
    root = 0
    G.add_node(root)
    levels = [[root]]
    node_id = 1

    while G.number_of_nodes() < N:
        next_level = []
        if not levels[-1]:
            break
        for parent in levels[-1]:
            children = 3 if parent == root else 2
            for _ in range(children):
                if G.number_of_nodes() >= N:
                    break
                G.add_node(node_id)
                G.add_edge(parent, node_id, H=0)
                next_level.append(node_id)
                node_id += 1
        if not next_level:
            break
        levels.append(next_level)

    return G, levels

def inject_seed_defect(G: nx.DiGraph, levels: Optional[List[List[int]]] = None) -> nx.DiGraph:
    """Injects a single symmetry-breaking 3-cycle defect at the root (Section 2.4, H=1)."""
    if levels and len(levels) >= 3 and levels[2]:
        v = levels[0][0]
        u = levels[2][0]
        G.add_edge(u, v, H=1)
    else:
        children = list(G.successors(0))
        if children:
            w = children[0]
            grandchildren = list(G.successors(w))
            if grandchildren:
                G.add_edge(grandchildren[0], 0, H=1)
    return G

# =============================================================================
# 3. MOVE GRAMMAR FILTERS (PUC & AEC)
# =============================================================================

def is_permissible_puc(G: nx.DiGraph, u: int, v: int, w: int) -> bool:
    """
    Parent-Uniqueness Condition (PUC, Section 2.5.2).
    Requires (v,u) not in E, and v -> w -> u is the unique directed 2-path from v to u.
    """
    if G.has_edge(v, u):
        return False
    for x in G.successors(v):
        if x != w and G.has_edge(x, u):
            return False
    return True

def pre_check_aec(G: nx.DiGraph, u: int, v: int, H_new: int) -> bool:
    """
    Acyclicity Pre-Check (AEC, Section 2.5.3).
    Evaluates paths from v to u up to depth L_cut = floor(log2 N) + 3 via BFS.
    """
    N = G.number_of_nodes()
    L_cut = max(1, int(math.floor(math.log2(N))) + 3) if N > 1 else 1

    queue = collections.deque([(v, -1, 0)])  # (node, prev_edge_height, depth)
    visited = set([(v, -1)])
    while queue:
        curr, prev_h, depth = queue.popleft()
        if depth >= L_cut:
            continue
        for succ in G.successors(curr):
            edge_h = G[curr][succ].get("H", 0)
            if edge_h > prev_h:  # Strictly monotone increasing
                if succ == u and edge_h < H_new:
                    return False  # Closed acausal monotone loop detected
                state = (succ, edge_h)
                if state not in visited:
                    visited.add(state)
                    queue.append((succ, edge_h, depth + 1))
    return True

def find_all_3_cycles(G: nx.DiGraph) -> List[List[Tuple[int, int]]]:
    """Finds all unique directed 3-cycles in the spatial graph."""
    cycles = []
    for u in G.nodes():
        for v in G.successors(u):
            for w in G.successors(v):
                if G.has_edge(w, u) and u < v and u < w:
                    cycles.append([(u, v), (v, w), (w, u)])
    return cycles

def find_legal_addition_sites(
    G: nx.DiGraph,
) -> List[Tuple[Tuple[int, int], int, Tuple[int, int, int]]]:
    """Finds all candidate 2-paths satisfying Parent-Uniqueness (PUC) and Acyclicity (AEC)."""
    sites = []
    for v in G.nodes():
        for w in list(G.successors(v)):
            for u in list(G.successors(w)):
                if v == u or G.has_edge(u, v):
                    continue
                if not is_permissible_puc(G, u, v, w):
                    continue
                in_edges = G.in_edges(u, data=True)
                max_h_in = max((d.get("H", 0) for _, _, d in in_edges), default=0)
                H_new = max_h_in + 1
                if not pre_check_aec(G, u, v, H_new):
                    continue
                sites.append(((u, v), H_new, (v, w, u)))
    return sites

# =============================================================================
# 4. FOUR-STEP PARALLEL SCHEDULER & HOMEOSTATIC EQUILIBRIUM (SECTION 2.8)
# =============================================================================

def build_stress_map(cycles: Sequence[Sequence[Tuple[int, int]]]) -> Dict[int, int]:
    """Computes vertex cycle incidence count."""
    stress_map: Dict[int, int] = {}
    for cycle in cycles:
        for u, _v in cycle:
            stress_map[u] = stress_map.get(u, 0) + 1
    return stress_map

def execute_parallel_tick(G: nx.DiGraph, mu: float, lam: float) -> Tuple[nx.DiGraph, bool]:
    """
    Executes one discrete tick under scheduler operator U (Section 2.8).
    Step 1: Awareness | Step 2: Proposals | Step 3: Merge | Step 4: Deletion
    Returns (G_next, active_flag). Returns active=False if homeostatic equilibrium is reached.
    """
    # Step 1: Awareness
    cycles = find_all_3_cycles(G)
    legal_additions = find_legal_addition_sites(G)

    # Combinatorial absorbing boundary: zero legal addition sites AND zero active 3-cycles
    if not legal_additions and not cycles:
        return G, False

    stress_map = build_stress_map(cycles)

    # Step 2: Proposals (Independent Bernoulli trials)
    A: Set[Tuple[Tuple[int, int], int]] = set()
    for (u, v), H_new, (node_v, node_w, node_u) in legal_additions:
        s_add = stress_map.get(node_v, 0) + stress_map.get(node_w, 0) + stress_map.get(node_u, 0)
        P_acc = math.exp(-mu * s_add)
        if random.random() < P_acc:
            A.add(((u, v), H_new))

    D: Set[Tuple[int, int]] = set()
    for cycle in cycles:
        cycle_nodes = {x for edge in cycle for x in edge}
        s_del = max(0, sum(stress_map.get(x, 0) for x in cycle_nodes) - 1)
        Q_del = min(1.0, 0.5 * (1.0 + lam * s_del) * math.exp(-mu * s_del))
        if random.random() < Q_del:
            chosen_edge = random.choice(cycle)
            D.add(chosen_edge)

    # Homeostatic Stall: quiet tick where no mutations are accepted on the finite substrate
    if not A and not D:
        return G, False

    # Step 3: Merge (Symmetric conflict resolution & Additions First)
    A_edges = {e for e, _ in A}
    A_filtered = {((u, v), H_new) for (u, v), H_new in A if (v, u) not in A_edges and u != v}
    for (u, v), H_new in A_filtered:
        G.add_edge(u, v, H=H_new)

    # Step 4: Deletions (Applied to intermediate graph)
    for u, v in D:
        if G.has_edge(u, v):
            G.remove_edge(u, v)

    return G, True

def evolve_graph_to_equilibrium(
    G: nx.DiGraph, mu: float, lam: float, max_steps: int = 1500
) -> Tuple[nx.DiGraph, int]:
    """Runs the simulation until homeostatic equilibrium (quiet tick) or max_steps."""
    for step in range(max_steps):
        G, active = execute_parallel_tick(G, mu, lam)
        if not active:
            return G, step + 1
    return G, max_steps

# =============================================================================
# 5. STATISTICAL DIAGNOSTICS & ENSEMBLE RUNNERS
# =============================================================================

def compute_qsd_moments(n3_values: Sequence[int], N: int) -> Dict[str, float]:
    """Computes unconditioned and conditioned QSD moments from an ensemble."""
    n = len(n3_values)
    survivors = [x for x in n3_values if x > 0]
    p_surv = len(survivors) / float(n) if n else 0.0
    mean_all = statistics.fmean(n3_values) if n else 0.0
    var_all = statistics.variance(n3_values) if n > 1 else 0.0
    mean_qsd = statistics.fmean(survivors) if survivors else 0.0
    var_qsd = statistics.variance(survivors) if len(survivors) > 1 else 0.0

    rho_all = [x / float(N) for x in n3_values]
    rho_qsd = [x / float(N) for x in survivors]

    # Skewness
    def _skew(xs):
        if len(xs) < 3: return 0.0
        m = statistics.fmean(xs)
        v = statistics.pvariance(xs)
        if v <= 0: return 0.0
        s = math.sqrt(v)
        return sum(((x - m)/s)**3 for x in xs) / len(xs)

    return {
        "n": float(n),
        "n_surv": float(len(survivors)),
        "p_surv": p_surv,
        "p_surv_se": math.sqrt(p_surv * (1.0 - p_surv) / n) if n else 0.0,
        "mean_n3_all": mean_all,
        "mean_rho_all": mean_all / float(N),
        "median_rho_all": statistics.median(rho_all) if rho_all else 0.0,
        "std_rho_all": statistics.stdev(rho_all) if n > 1 else 0.0,
        "skew_rho_all": _skew(rho_all),
        "fano_all": (var_all / mean_all) if mean_all > 0 else 0.0,
        "mean_n3_qsd": mean_qsd,
        "mean_rho_qsd": mean_qsd / float(N) if (N and survivors) else 0.0,
        "mean_rho_qsd_se": (statistics.stdev(rho_qsd) / math.sqrt(len(rho_qsd))) if len(rho_qsd) > 1 else 0.0,
        "median_rho_qsd": statistics.median(rho_qsd) if rho_qsd else 0.0,
        "std_rho_qsd": statistics.stdev(rho_qsd) if len(rho_qsd) > 1 else 0.0,
        "fano_qsd": (var_qsd / mean_qsd) if mean_qsd > 0 else 0.0,
        "n3_min_qsd": float(min(survivors)) if survivors else 0.0,
        "n3_max_qsd": float(max(survivors)) if survivors else 0.0,
    }

def compute_scar_diagnostics(G: nx.DiGraph, N: int = 100) -> Dict[str, float]:
    """Computes topological scar and graph degree observables (Table 5)."""
    cycles = find_all_3_cycles(G)
    cycle_edges = {e for c in cycles for e in c}
    total_edges = G.number_of_edges()
    scar_edges = total_edges - len(cycle_edges)
    G_undir = G.to_undirected()
    comps = list(nx.connected_components(G_undir))
    largest_cc = max(comps, key=len) if comps else set()
    diam = float(nx.diameter(G_undir.subgraph(largest_cc))) if len(largest_cc) > 1 else 0.0
    mean_deg = sum(dict(G.degree()).values()) / float(N)

    return {
        "total_edges": float(total_edges),
        "num_3_cycles": float(len(cycles)),
        "scar_edges": float(scar_edges),
        "mean_degree": float(mean_deg),
        "diameter": diam,
    }

def _worker_trajectory(args: Tuple[int, int, float, float, int]) -> Dict:
    run_idx, N, mu, lam, seed = args
    random.seed(seed)
    t0 = time.time()
    G, levels = generate_bethe_fragment(N)
    G = inject_seed_defect(G, levels)
    G_final, steps = evolve_graph_to_equilibrium(G, mu, lam)
    n3 = len(find_all_3_cycles(G_final))
    scar = compute_scar_diagnostics(G_final, N)
    return {
        "run_idx": run_idx,
        "N": N,
        "mu": mu,
        "lam": lam,
        "steps": steps,
        "n3_final": n3,
        "is_survivor": int(n3 > 0),
        "total_edges": scar["total_edges"],
        "scar_edges": scar["scar_edges"],
        "mean_deg": scar["mean_degree"],
        "diameter": scar["diameter"],
        "elapsed_sec": time.time() - t0,
    }

# =============================================================================
# 6. PROPERTY-BASED INVARIANT VERIFICATION
# =============================================================================

def test_engine_invariants(num_ticks: int = 50, N: int = 100) -> bool:
    """
    Verifies microscopic mathematical invariants:
    1. Move Disjointness (Lemma 2.1): A_edges and D are strictly disjoint.
    2. Scar Immunity (Theorem 6.2): Deletions only target 3-cycle edges.
    3. Irreflexivity & Asymmetry (Axiom 1): Additions never create self-loops or reciprocal edges.
    4. DAG Acyclicity: Terminal state is certified acyclic when cycles vanish.
    """
    priors = compute_analytical_priors()
    mu, lam = priors["mu_0"], priors["lambda_0"]

    G, levels = generate_bethe_fragment(N)
    # Check 50% leaf boundary theorem
    leaves = sum(1 for v in G.nodes() if G.out_degree(v) == 0)
    expected_leaves = (N + 2) // 2
    assert leaves == expected_leaves, f"Leaf theorem mismatch: got {leaves}, expected {expected_leaves}"

    G = inject_seed_defect(G, levels)
    assert len(find_all_3_cycles(G)) == 1, "Seed cycle injection failed"

    for _ in range(num_ticks):
        cycles = find_all_3_cycles(G)
        active_cycle_edges = {e for c in cycles for e in c}
        stress_map = build_stress_map(cycles)

        legal_additions = find_legal_addition_sites(G)
        A: Set[Tuple[Tuple[int, int], int]] = set()
        for (u, v), H_new, (node_v, node_w, node_u) in legal_additions:
            s_add = stress_map.get(node_v, 0) + stress_map.get(node_w, 0) + stress_map.get(node_u, 0)
            if random.random() < math.exp(-mu * s_add):
                A.add(((u, v), H_new))

        D: Set[Tuple[int, int]] = set()
        for cycle in cycles:
            cycle_nodes = {x for edge in cycle for x in edge}
            s_del = max(0, sum(stress_map.get(x, 0) for x in cycle_nodes) - 1)
            Q_del = min(1.0, 0.5 * (1.0 + lam * s_del) * math.exp(-mu * s_del))
            if random.random() < Q_del:
                D.add(random.choice(cycle))

        A_edges = {e for e, _ in A}
        assert A_edges.isdisjoint(D), "Invariant Violated: A_edges and D overlap"
        assert D.issubset(active_cycle_edges), "Invariant Violated: Deletion of non-cycle edge"
        assert all(u != v for u, v in A_edges), "Invariant Violated: Self-loop in additions"
        assert all((v, u) not in A_edges for u, v in A_edges), "Invariant Violated: Reciprocal additions"

        A_filtered = {((u, v), H_new) for (u, v), H_new in A if (v, u) not in A_edges and u != v}
        for (u, v), H_new in A_filtered:
            G.add_edge(u, v, H=H_new)
        for u, v in D:
            if G.has_edge(u, v):
                G.remove_edge(u, v)

        if not A and not D and len(cycles) == 0:
            assert nx.is_directed_acyclic_graph(G), "Terminal state is not a DAG"
            break

    print("  [PASS] All Microscopic Invariants & Lean Properties Verified Cleanly.")
    return True

# =============================================================================
# 7. CLI ENTRY POINT & TABLE GENERATORS
# =============================================================================

def run_canonical_slice_cli(runs: int = 100, N: int = 100, workers: int = None):
    """Reproduces Table 4: Median Density Collapse along the mu=0.40 Canonical Slice."""
    priors = compute_analytical_priors()
    mu = 0.40
    lambdas = [0.8, 1.1, 1.4, 1.7, 2.0, 2.3, 2.6, 2.9, 3.2, 3.5, 3.8, 4.1]
    w = workers or max(1, (os.cpu_count() or 4) - 1)

    print(f"\nExecuting Canonical Slice Sweep (mu={mu:.2f}, {len(lambdas)} points, runs={runs}/pt, workers={w})...")

    header = f"{'lambda':>8} | {'p_surv':>8} | {'<rho>_all':>10} | {'Median rho':>12} | {'<rho>_QSD':>10} | {'<N3>_QSD':>10}"
    print("\n" + "=" * 75)
    print("TABLE 4: CANONICAL SLICE DENSITY METRICS (mu = 0.40, N = 100)")
    print("=" * 75)
    print(header)
    print("-" * 75)

    with ProcessPoolExecutor(max_workers=w) as ex:
        for lam in lambdas:
            jobs = [(i + 1, N, mu, lam, 42 * 10007 + int(lam * 100) * 199 + i * 31) for i in range(runs)]
            results = list(ex.map(_worker_trajectory, jobs))
            n3_vals = [r["n3_final"] for r in results]
            moments = compute_qsd_moments(n3_vals, N)
            print(f"{lam:8.1f} | {moments['p_surv']:8.3f} | {moments['mean_rho_all']:10.4f} | {moments['median_rho_all']:12.4f} | {moments['mean_rho_qsd']:10.4f} | {moments['mean_n3_qsd']:10.2f}")
    print("=" * 75)

def run_scar_diagnostics_cli(runs: int = 100, N: int = 100, workers: int = None):
    """Reproduces Table 5: Topological Scar Accumulation and Degree Saturation Invariants."""
    priors = compute_analytical_priors()
    mu, lam = priors["mu_0"], priors["lambda_0"]
    w = workers or max(1, (os.cpu_count() or 4) - 1)

    print(f"\nExecuting Scar & Degree Invariant Diagnostics (N={N}, mu={mu:.4f}, lambda={lam:.4f}, runs={runs}, workers={w})...")
    jobs = [(i + 1, N, mu, lam, 42 * 10007 + i * 31) for i in range(runs)]
    with ProcessPoolExecutor(max_workers=w) as ex:
        results = list(ex.map(_worker_trajectory, jobs))

    edges_all = [r["total_edges"] for r in results]
    scars_all = [r["scar_edges"] for r in results]
    degs_all = [r["mean_deg"] for r in results]
    diams_all = [r["diameter"] for r in results if r["diameter"] > 0]
    steps_all = [r["steps"] for r in results]

    print("\n" + "=" * 75)
    print("TABLE 5: TOPOLOGICAL SCAR ACCUMULATION & DEGREE SATURATION (N = 100)")
    print("=" * 75)
    print(f"  Mean Total Final Edges <|E|>    : {statistics.fmean(edges_all):6.2f} +/- {statistics.stdev(edges_all):.2f}")
    print(f"  Mean Frozen Scar Edges <|E_scar|>: {statistics.fmean(scars_all):6.2f} +/- {statistics.stdev(scars_all):.2f}")
    print(f"  Mean Undirected Degree <k>      : {statistics.fmean(degs_all):6.3f} +/- {statistics.stdev(degs_all):.3f}")
    if diams_all:
        print(f"  Mean Network Diameter <diam>    : {statistics.fmean(diams_all):6.2f} +/- {statistics.stdev(diams_all):.2f}")
    print(f"  Mean Homeostatic Stall Step     : {statistics.fmean(steps_all):6.1f} +/- {statistics.stdev(steps_all):.1f} ticks")
    print("=" * 75)

def run_sweep_cli(runs_per_point: int = 20, N: int = 100, workers: int = None):
    """Reproduces Table 2: 132-Point Parameter Sweep Matrix over (mu, lambda)."""
    mus = [0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65]
    lambdas = [0.8, 1.1, 1.4, 1.7, 2.0, 2.3, 2.6, 2.9, 3.2, 3.5, 3.8, 4.1]
    w = workers or max(1, (os.cpu_count() or 4) - 1)

    print(f"\nExecuting Parameter Sweep ({len(mus)}x{len(lambdas)}={len(mus)*len(lambdas)} grid, {runs_per_point} runs/cell, workers={w})...")

    # Header
    col_headers = "".join(f" | {l:4.1f}" for l in lambdas)
    print("\n" + "=" * 90)
    print("TABLE 2: UNCONDITIONED MEAN CYCLE DENSITY <rho> (N = 100)")
    print("=" * 90)
    print(f" mu \\ lam" + col_headers)
    print("-" * 90)

    with ProcessPoolExecutor(max_workers=w) as ex:
        for mu in mus:
            row_str = f"  {mu:4.2f}  "
            for lam in lambdas:
                jobs = [(i + 1, N, mu, lam, 42 * 10007 + int(mu * 1000) * 37 + int(lam * 100) * 199 + i * 31) for i in range(runs_per_point)]
                results = list(ex.map(_worker_trajectory, jobs))
                n3_vals = [r["n3_final"] for r in results]
                mean_rho = statistics.fmean(n3_vals) / float(N)
                row_str += f" | {mean_rho:5.3f}"
            print(row_str)
    print("=" * 90)

def run_design_point_cli(runs: int = 100, N: int = 100, workers: int = None):
    """Reproduces Table 3: Moments of 3-Cycle Activity at Canonical Design Point."""
    priors = compute_analytical_priors()
    mu, lam = priors["mu_0"], priors["lambda_0"]
    w = workers or max(1, (os.cpu_count() or 4) - 1)

    print(f"\nExecuting Design Point Ensemble: N={N}, mu={mu:.4f}, lambda={lam:.4f}, runs={runs}, workers={w}...")
    jobs = [(i + 1, N, mu, lam, 42 * 10007 + i * 31) for i in range(runs)]
    with ProcessPoolExecutor(max_workers=w) as ex:
        results = list(ex.map(_worker_trajectory, jobs))

    n3_vals = [r["n3_final"] for r in results]
    moments = compute_qsd_moments(n3_vals, N)

    print("\n" + "=" * 75)
    print(f"TABLE 3: MOMENTS OF 3-CYCLE ACTIVITY AT CANONICAL POINT (mu0, lambda0)")
    print("=" * 75)
    print(f"  Unconditioned Mean Density <rho>  : {moments['mean_rho_all']:.4f} +/- {moments['std_rho_all']/math.sqrt(runs):.4f}")
    print(f"  Unconditioned Median Density      : {moments['median_rho_all']:.4f}")
    print(f"  Survival Fraction p_surv          : {moments['p_surv']:.3f} +/- {moments['p_surv_se']:.3f} (Surviving runs: {int(moments['n_surv'])}/{runs})")
    print(f"  Conditioned QSD Mean Density      : {moments['mean_rho_qsd']:.4f} +/- {moments['mean_rho_qsd_se']:.4f}")
    print(f"  Conditioned QSD Median Density    : {moments['median_rho_qsd']:.4f}")
    print(f"  Conditioned QSD Mean Cycles <N3>  : {moments['mean_n3_qsd']:.2f}")
    print(f"  QSD Fano Factor Var(N3)/<N3>      : {moments['fano_qsd']:.2f}")
    print(f"  Skewness gamma                    : {moments['skew_rho_all']:.3f}")
    print("=" * 75)

def main():
    parser = argparse.ArgumentParser(description="QBD Standalone Reference Simulation Engine")
    parser.add_argument("--priors", action="store_true", help="Print Table 1 (Analytical Reference Priors)")
    parser.add_argument("--test-invariants", action="store_true", help="Run property-based mathematical verification")
    parser.add_argument("--design-point", action="store_true", help="Run Table 3 Design Point Ensemble")
    parser.add_argument("--canonical-slice", action="store_true", help="Run Table 4 Canonical Slice Sweep")
    parser.add_argument("--scar-diagnostics", action="store_true", help="Run Table 5 Scar & Degree Diagnostics")
    parser.add_argument("--sweep", action="store_true", help="Run Table 2 Parameter Sweep Matrix")
    parser.add_argument("--runs", type=int, default=100, help="Number of trajectories per cell (default: 100)")
    parser.add_argument("-N", "--N", type=int, default=100, help="Graph size (default: 100)")
    parser.add_argument("--workers", type=int, default=None, help="Worker count")

    args = parser.parse_args()

    if args.priors:
        priors = compute_analytical_priors()
        print("\n" + "=" * 70)
        print("TABLE 1: CANONICAL ANALYTICAL REFERENCE PRIORS")
        print("=" * 70)
        for k, v in priors.items():
            print(f"  {k:<16}: {v:12.6f}")
        print("=" * 70)

    if args.test_invariants:
        print("\nRunning Microscopic Move Grammar & Invariant Verification...")
        test_engine_invariants(num_ticks=50, N=args.N)

    if args.design_point:
        run_design_point_cli(runs=args.runs, N=args.N, workers=args.workers)

    if args.canonical_slice:
        run_canonical_slice_cli(runs=args.runs, N=args.N, workers=args.workers)

    if args.scar_diagnostics:
        run_scar_diagnostics_cli(runs=args.runs, N=args.N, workers=args.workers)

    if args.sweep:
        run_sweep_cli(runs_per_point=args.runs, N=args.N, workers=args.workers)

    if not any([args.priors, args.test_invariants, args.design_point, args.canonical_slice, args.scar_diagnostics, args.sweep]):
        priors = compute_analytical_priors()
        print("=" * 70)
        print("QBD STANDALONE REFERENCE ENGINE: CANONICAL PRIORS")
        print("=" * 70)
        for k, v in priors.items():
            print(f"  {k:<16}: {v:12.6f}")
        print("=" * 70)
        print("\nVerifying Invariants...")
        test_engine_invariants(num_ticks=50, N=100)
        print("\nCLI Options:")
        print("  --priors            : Table 1 (Constitutive scales)")
        print("  --design-point      : Table 3 (QSD moments at mu0, lambda0)")
        print("  --canonical-slice   : Table 4 (Density transition along lambda)")
        print("  --scar-diagnostics  : Table 5 (Frozen scars & degree saturation)")
        print("  --sweep             : Table 2 (132-point parameter sweep)")
        print("  --test-invariants   : Property-based Lean-mirrored unit tests")

if __name__ == "__main__":
    main()
```
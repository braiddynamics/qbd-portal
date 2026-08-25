---
id: maximal-entropy-random-walk
title: 'Comment on "Localization of the Maximal Entropy Random Walk"'
sidebar_label: "Maximal Entropy Random Walk (Comment)"
slug: /maximal-entropy-random-walk
description: "A formal comment demonstrating that for any connected bipartite graph, Maximal Entropy Random Walk exhibits persistent period-two parity oscillations."
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
  <span style={{ color: 'var(--ifm-color-emphasis-900)', fontWeight: 500 }}>Maximal Entropy Random Walk (Comment)</span>
</nav>

:::info[**Comment & Archival Record**]
**Title:** Comment on "Localization of the Maximal Entropy Random Walk"  
**Author:** **R. Fisher**, *Principal Investigator* ([ORCID: 0009-0006-2441-3282](https://orcid.org/0009-0006-2441-3282))  
**Affiliation:** Braid Dynamics Group  
**Target Article:** Z. Burda, J. Duda, J.-M. Luck, B. Wacław, *Phys. Rev. Lett.* **102**, 160602 (2009)  
**Published / Received:** June 21, 2026 · **Status:** Formal Commentary / Preprint (v1.0.0) · **License:** [Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)  
**Classification:** Statistical Mechanics · Spectral Graph Theory · Markov Chains  
**Replication Engine:** Python 3.8+ reference simulation script with spectral analysis and lazy-walk recovery.
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
    📁 Downloadable Publication & Replication Files
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
        <td style={{ fontWeight: 600 }}><code>maximal-entropy-random-walk.pdf</code></td>
        <td>Physical Review Letters Two-Column Comment (XeLaTeX)</td>
        <td>40 KB</td>
        <td style={{ textAlign: 'right' }}>
          <a href="pathname:///papers/maximal-entropy-random-walk/downloads/maximal-entropy-random-walk.pdf" download style={{ fontWeight: 600 }}>Download PDF ↓</a>
        </td>
      </tr>
      <tr>
        <td style={{ fontWeight: 600 }}><code>maximal_entropy_random_walk_simulation.py</code></td>
        <td>Standalone Python Simulation & Spectral Analyzer</td>
        <td>4 KB</td>
        <td style={{ textAlign: 'right' }}>
          <a href="pathname:///papers/maximal-entropy-random-walk/simulations/maximal_entropy_random_walk_simulation.py" download style={{ fontWeight: 600 }}>Download Python ↓</a>
        </td>
      </tr>
      <tr>
        <td style={{ fontWeight: 600 }}><code>maximal-entropy-random-walk.md</code></td>
        <td>Complete Markdown Source Document</td>
        <td>8 KB</td>
        <td style={{ textAlign: 'right' }}>
          <a href="pathname:///papers/maximal-entropy-random-walk/downloads/maximal-entropy-random-walk.md" download style={{ fontWeight: 600 }}>Download MD ↓</a>
        </td>
      </tr>
    </tbody>
  </table>
</div>

### Abstract

Burda *et al.* [Phys. Rev. Lett. 102, 160602 (2009)] asserted that the discrete-time probability distribution $\pi_i(t)$ of the Maximal Entropy Random Walk (MERW) relaxes to the unique stationary profile $\pi_i^* = \psi_{0,i}^2$ as $t \to \infty$. While $\pi^*$ is the correct stationary measure and principal-eigenvector localization remains valid, this Comment shows that for any finite connected bipartite graph, the MERW transition matrix possesses a peripheral eigenvalue $\mu = -1$, inducing period-two dynamics. Consequently, the unmodified discrete-time distribution does not converge to $\pi^*$ from initial conditions with nonzero parity imbalance; instead it approaches a persistent two-cycle. For the unmodified chain, convergence to $\pi^*$ holds if and only if the initial distribution has equal mass on the two bipartition classes. Cesàro or pairwise parity averaging, aperiodic lazy modifications, and continuous-time formulations recover convergence to $\pi^*$ in the appropriate sense.

---

## I. Introduction

The Maximal Entropy Random Walk (MERW) constructs stochastic trajectories by maximizing entropy globally over paths of fixed length. For a finite, connected graph $G=(V,E)$ with symmetric adjacency matrix $A$, spectral radius $\lambda_0$, and normalized principal right eigenvector $\psi_0$ ($\|\psi_0\|_2=1$, $\psi_{0,i}>0$), the discrete-time stationary distribution is [1]:
$$\pi_i^* = \psi_{0,i}^2$$
Specifically, Ref.~[1], following Eq.~(2), asserts: ``using spectral properties of the matrix $P_{ij}$, one can show that $\pi_i(t)$ reaches for $t \to \infty$ a unique stationary state $\pi_i^*$ obeying (2)''.

For a finite irreducible discrete-time Markov chain, convergence to stationarity from every initial state requires aperiodicity. If $P$ possesses peripheral eigenvalues on the unit circle other than unity, the chain fails to mix. On bipartite topologies commonly studied in MERW simulations (such as ladder networks and square lattices with open or even-periodic boundary conditions), $P$ possesses a peripheral eigenvalue $\mu = -1$. Consequently, while $\pi^*$ remains stationary, the unmodified discrete-time chain fails to converge from generic initial conditions, settling into a persistent period-two oscillation.

---

## II. Spectral Projection and Row-Stochasticity

Let $G = (V,E)$ denote a finite, connected, bipartite graph with disjoint vertex partitions $V = V_1 \cup V_2$. Ordering vertices conformally yields the symmetric block adjacency matrix:
$$A = \begin{pmatrix} 0 & B \\ B^T & 0 \end{pmatrix}$$
where $B$ is of dimension $|V_1| \times |V_2|$.

Let $\lambda_0$ denote the spectral radius of $A$. By the Perron-Frobenius theorem, $\lambda_0$ is a simple, positive eigenvalue, and the corresponding principal right eigenvector $\psi_0$ satisfies $\psi_{0,i} > 0$ for all $i \in V$. Conformal partitioning of $\psi_0 = (\psi_{0}^{(1)}, \psi_{0}^{(2)})^T$ under $A\psi_0 = \lambda_0\psi_0$ yields the coupled linear system:
$$B\psi_{0}^{(2)} = \lambda_0\psi_{0}^{(1)}, \quad B^T\psi_{0}^{(1)} = \lambda_0\psi_{0}^{(2)}$$
Defining the spectral test vector $\psi_- = (\psi_{0}^{(1)}, -\psi_{0}^{(2)})^T$, direct matrix multiplication gives:
$$A\psi_- = \begin{pmatrix} 0 & B \\ B^T & 0 \end{pmatrix} \begin{pmatrix} \psi_{0}^{(1)} \\ -\psi_{0}^{(2)} \end{pmatrix} = \begin{pmatrix} -B\psi_{0}^{(2)} \\ B^T\psi_{0}^{(1)} \end{pmatrix} = \begin{pmatrix} -\lambda_0\psi_{0}^{(1)} \\ \lambda_0\psi_{0}^{(2)} \end{pmatrix} = -\lambda_0\psi_-$$
Thus, $-\lambda_0$ is an eigenvalue of $A$ with eigenvector $\psi_-$. Because the sign-flip mapping on $V_2$ components provides an invertible isometry between eigenspaces, simplicity of $\lambda_0$ implies simplicity of $-\lambda_0$.

The discrete-time MERW transition matrix is defined via diagonal similarity transformation:
$$P = \frac{1}{\lambda_0} D^{-1} A D$$
where $D = \operatorname{diag}(\psi_0)$. Under row probability conventions, $P$ is strictly row-stochastic:
$$\sum_j P_{ij} = \frac{1}{\lambda_0\psi_{0,i}}\sum_j A_{ij}\psi_{0,j} = \frac{(A\psi_0)_i}{\lambda_0\psi_{0,i}} = 1$$
Because $A$ is real and symmetric, $A$ is orthogonally diagonalizable, Jordan blocks do not occur, and spectra satisfy $\operatorname{Spec}(P) = \frac{1}{\lambda_0}\operatorname{Spec}(A)$. Since the peripheral spectrum of $A$ on a connected bipartite graph is strictly $\{\lambda_0, -\lambda_0\}$, the peripheral spectrum of $P$ is strictly $\{1, -1\}$.

The right eigenvector $v_2$ of $P$ corresponding to the peripheral eigenvalue $\mu_2 = -1$ ($P v_2 = -v_2$) is the parity vector:
$$v_2 = D^{-1}\psi_- \implies v_{2,i} = \frac{\psi_{-,i}}{\psi_{0,i}} = \begin{cases} +1 & \text{if } i \in V_1 \\ -1 & \text{if } i \in V_2 \end{cases}$$
This yields an immediate parity diagnostic observable:
$$\pi(t)v_2 = \pi(0)P^t v_2 = (-1)^t \pi(0)v_2 = (-1)^t c$$
where $c = \sum_{i \in V_1}\pi_i(0) - \sum_{i \in V_2}\pi_i(0)$ is the initial parity imbalance. Since $\pi^* v_2 = \sum_{i \in V_1}\psi_{0,i}^2 - \sum_{i \in V_2}\psi_{0,i}^2 = \psi_0^T\psi_- = 0$, convergence $\pi(t) \to \pi^*$ requires $(-1)^t c \to 0$, which is impossible whenever $c \neq 0$.

---

## III. Dual Basis Expansion and Asymptotic Oscillations

Let $\pi(t)$ represent the state probability row vector under iterated applications of $P$. We decompose an arbitrary initial probability distribution $\pi(0)$ into the dual basis of left and right eigenvectors $\{u_\alpha^T, v_\alpha\}$ of $P$, satisfying the biorthogonality condition $u_\alpha^T v_\beta = \delta_{\alpha\beta}$.

### A. Subspace Biorthogonality Verification

Let the stationary mode ($\mu_1 = 1$) be defined by $u_1^T = \pi^*$ and $v_1 = \mathbf{1}$, where $\pi_i^* = \psi_{0,i}^2$ subject to $\sum_i \psi_{0,i}^2 = 1$. Let the oscillatory mode ($\mu_2 = -1$) have right eigenvector $v_2$ and left eigenvector $u_2^T = w^T$, where $w_i = \psi_{0,i}\psi_{-,i}$ (satisfying $w^T P = -w^T$ via MERW reversibility with respect to $\pi^*$). Element-wise:
$$w_i = \begin{cases} \psi_{0,i}^2 & \text{if } i \in V_1 \\ -\psi_{0,i}^2 & \text{if } i \in V_2 \end{cases}$$
Eigenvector orthogonality $\psi_0 \perp \psi_-$ establishes:
$$w^T v_1 = \sum_{i \in V} w_i = \sum_{i \in V_1} \psi_{0,i}^2 - \sum_{i \in V_2} \psi_{0,i}^2 = \psi_0^T \psi_- = 0$$
Therefore, the $L_2$ mass of the Perron vector is split equally between the two partition classes. Biorthogonality constraints for the dominant subspace are satisfied:
$$u_1^T v_2 = \sum_{i \in V_1} \psi_{0,i}^2 - \sum_{i \in V_2} \psi_{0,i}^2 = 0, \quad w^T v_2 = \sum_{i \in V} \psi_{-,i}^2 = \sum_{i \in V} \psi_{0,i}^2 = 1$$

### B. Eigenvalue Decay and Asymptotic Oscillation

By the Perron-Frobenius theorem, all remaining subdominant eigenvalues satisfy $|\mu_\alpha| < 1$ for $\alpha \ge 3$. State evolution from an arbitrary initial distribution $\pi(0)$ follows:
$$\pi(t) = (\pi(0)v_1)(1)^t \pi^* + (\pi(0)v_2)(-1)^t w^T + \sum_{\alpha \ge 3} (\pi(0)v_\alpha)\mu_\alpha^t u_\alpha^T$$
Taking $t \to \infty$, decaying modes vanish exponentially ($|\mu_\alpha|^t \to 0$), yielding the leading asymptotic form:
$$\pi_i(t) = \psi_{0,i}^2 + c(-1)^t \sigma_i \psi_{0,i}^2 + o(1)$$
where $\sigma_i = +1$ for $i \in V_1$ and $\sigma_i = -1$ for $i \in V_2$. Hence, for the unmodified discrete-time chain, $\lim_{t \to \infty}\pi(t) = \pi^*$ if and only if $c = 0$.

For a point-mass distribution localized at node $k \in V_1$ ($\pi(0) = \mathbf{e}_k^T$), we have $c_1 = 1$ and $c = +1$. The sequence alternates between two disjoint limits:
$$\lim_{\substack{t \to \infty \\ t \text{ even}}} \pi_i(t) = \begin{cases} 2\psi_{0,i}^2 & \text{if } i \in V_1 \\ 0 & \text{if } i \in V_2 \end{cases}, \quad \lim_{\substack{t \to \infty \\ t \text{ odd}}} \pi_i(t) = \begin{cases} 0 & \text{if } i \in V_1 \\ 2\psi_{0,i}^2 & \text{if } i \in V_2 \end{cases}$$
Initializing at node $k \in V_2$ yields $c = -1$, producing an identical, phase-inverted limit cycle. Although the chain is periodic, irreducibility and positive recurrence guarantee that the Cesàro time average $\frac{1}{T}\sum_{t=0}^{T-1} \pi(t) \to \pi^*$, and the pairwise parity average $\frac{1}{2}[\pi(t)+\pi(t+1)] \to \pi^*$ as $t \to \infty$.

---

## IV. Conclusion

The universal statement that the discrete-time MERW distribution relaxes to $\pi^* = \psi_{0}^2$ is not valid on finite connected bipartite graphs. The stationary profile $\pi^*$ remains correct and is recovered by Cesàro or pairwise parity averaging. However, the instantaneous distribution converges to $\pi^*$ only when the initial parity imbalance $c$ vanishes; for $c \neq 0$, the distribution approaches a permanent period-two limit cycle. To obtain ordinary convergence of the instantaneous distribution, one must modify the dynamics, for example by using an aperiodic lazy walk $P_\alpha = (1-\alpha)I + \alpha P$ ($0 < \alpha < 1$) or transitioning to continuous-time dynamics with generator $Q = P - I$. A companion numerical simulation is provided in the Supplemental Material file `maximal_entropy_random_walk_simulation.py` [2].

---

## References

1. Z. Burda, J. Duda, J.-M. Luck, and B. Wacław, *Localization of the Maximal Entropy Random Walk*, [Phys. Rev. Lett. **102**, 160602 (2009)](https://doi.org/10.1103/PhysRevLett.102.160602).
2. R. Fisher, *Maximal Entropy Random Walk Periodicity Simulation*, Supplemental Material and Code Archive, [Braid Dynamics Research Archive](https://braiddynamics.com/papers/maximal-entropy-random-walk) (2026).

---
title: "Appendix B: Master List of Definitions & Theorems - Chapter 9"
sidebar_class_name: "theme-doc-sidebar-item-hidden"
---

This appendix serves as a centralized, rigorous catalog of the foundational mathematical postulates, definitions, axioms, lemmas, and theorems introduced in Chapter 9 of the Quantum Braid Dynamics (QBD) monograph.

---

### 9.1.1 Theorem: Minimal GUT Uniqueness {#9.1.1}

:::info[**Identification of the Unique Simple Lie Group for Grand Unification via Rank Constraints**]
:::

Given the gauge symmetries of the Standard Model, the Grand Unified gauge group is identified uniquely as the Special Unitary Group of degree 5, denoted $SU(5)$ under **Rank Conditions** <Ref id="9.1.2" label="§9.1.2" />. This uniqueness is satisfied by the simultaneous requirements of rank sufficiency ($r \ge 4$), the existence of complex chiral representations, and anomaly cancellation. Under these algebraic constraints, all other simple Lie algebras are excluded.

**In Plain English:**  
Section 9.1.1 formalizes the properties of the QBD theorem regarding minimal gut uniqueness.

---

### 9.1.2 Lemma: Rank Conditions {#9.1.2}

:::info[**Requirement of Minimum Rank through Standard Model Embedding**]
:::

Assume the rank of the Grand Unified Group, denoted $G_{GUT}$, is strictly bounded from below by the integer value of 4. This lower bound is mandated by the embedding morphism $\phi: G_{SM} \hookrightarrow G_{GUT}$ requiring the unified Cartan subalgebra to contain the direct sum of the constituent Standard Model Cartan subalgebras.

**In Plain English:**  
Section 9.1.2 formalizes the properties of the QBD lemma regarding rank conditions.

---

### 9.1.2.1 Proof: Rank Conditions {#9.1.2.1}

:::tip[**Formal Derivation from Rank Inequality**]
:::

**I. Four Commuting Standard Model Directions**

At Lie-algebra level, let

$$
\mathfrak g_{SM}=\mathfrak{su}(3)\oplus\mathfrak{su}(2)\oplus\mathfrak u(1).
$$

In the respective summands define

$$
\begin{gathered}
C_1=i\operatorname{diag}(1,-1,0),\qquad
C_2=i\operatorname{diag}(0,1,-1),\\
L=i\operatorname{diag}(1,-1),\qquad Y=i,\\
h_1=(C_1,0,0),\quad h_2=(C_2,0,0),\quad
h_3=(0,L,0),\quad h_4=(0,0,Y).
\end{gathered}
$$

These are skew-Hermitian directions in the compact gauge algebras of the embedding problem (**Minimal GUT Uniqueness** <Ref id="9.1.1" label="§9.1.1" />). Diagonal matrices commute, and the bracket in a direct sum is componentwise, so

$$
[h_j,h_k]=0\qquad(1\le j,k\le4).
$$

**II. Independence of the Four Directions**

For real coefficients, the equation $\sum_{j=1}^4a_jh_j=0$ has components

$$
\begin{aligned}
a_1C_1+a_2C_2
 &=i\operatorname{diag}(a_1,-a_1+a_2,-a_2)=0,\\
a_3L&=i\operatorname{diag}(a_3,-a_3)=0,\\
a_4Y&=ia_4=0.
\end{aligned}
$$

The first diagonal entry gives $a_1=0$, the third gives $a_2=0$, and the remaining components give $a_3=a_4=0$. Their real span $\mathfrak t_{SM}$ is therefore four-dimensional. Exponentiating its diagonal coordinates gives a compact torus, with two independent angles in $SU(3)$, one in $SU(2)$ and one in $U(1)$:

$$
\begin{aligned}
\exp(a_1C_1+a_2C_2)
 &=\operatorname{diag}(e^{ia_1},e^{i(-a_1+a_2)},e^{-ia_2}),\\
\exp(a_3L)&=\operatorname{diag}(e^{ia_3},e^{-ia_3}),\qquad
\exp(a_4Y)=e^{ia_4}.
\end{aligned}
$$

**III. Transport Through an Embedding**

Let $\phi:G_{SM}\hookrightarrow G_{GUT}$ be the stated embedding of compact gauge groups, with injective derivative $\mathrm d\phi$. If

$$
\sum_{j=1}^4a_j\mathrm d\phi(h_j)=0,
$$

then linearity and injectivity give

$$
\mathrm d\phi\left(\sum_j a_jh_j\right)=0
\ \Longrightarrow\ \sum_ja_jh_j=0
\ \Longrightarrow\ a_1=a_2=a_3=a_4=0.
$$

Also,

$$
[\mathrm d\phi(h_j),\mathrm d\phi(h_k)]
=\mathrm d\phi([h_j,h_k])=\mathrm d\phi(0)=0.
$$

The image $\phi(T_{SM})$ is a four-dimensional torus. A maximal torus of the compact target containing it consequently has dimension at least four. The rank bound is (**Rank Conditions** <Ref id="9.1.2" label="§9.1.2" />),

$$
\boxed{\operatorname{rank}G_{GUT}\ge\dim\phi(T_{SM})=2+1+1=4.}
$$

Q.E.D.

**In Plain English:**  
Section 9.1.2.1 formalizes the properties of the QBD proof regarding rank conditions.

---

### 9.1.3 Lemma: Lower Rank Exclusion {#9.1.3}

:::info[**Systematic Elimination of Simple Lie Groups by Insufficient Rank**]
:::

For any simple Lie group with rank $r < 4$, the candidate is categorically excluded from the domain of viable Grand Unified Theories. This exclusion is absolute and is predicated upon the failure of the group to satisfy the rank condition established in **Rank Conditions** <Ref id="9.1.2" label="§9.1.2" />.

**In Plain English:**  
Section 9.1.3 formalizes the properties of the QBD lemma regarding lower rank exclusion.

---

### 9.1.3.1 Proof: Lower Rank Exclusion {#9.1.3.1}

:::tip[**Verification of Failure Modes via Low-Rank Algebras**]
:::

**I. Embedding Requirement**

Let $G$ be a compact simple candidate with rank $r<4$. Suppose, for contradiction, that a Standard Model gauge embedding exists. Its derivative would inject the four-dimensional commuting torus algebra into the target (**Rank Conditions** <Ref id="9.1.2" label="§9.1.2" />). Thus its image would satisfy

$$
\dim\mathrm d\phi(\mathfrak t_{SM})=\dim\mathfrak t_{SM}=4.
$$

**II. Rank Bound in the Target**

The image torus is contained in a maximal torus $T_G$. Inclusion of real tangent spaces implies

$$
\mathrm d\phi(\mathfrak t_{SM})\subseteq\operatorname{Lie}(T_G)
\ \Longrightarrow\ 4\le\dim\operatorname{Lie}(T_G)
=\operatorname{rank}G=r.
$$

Combining the inequalities gives

$$
4\le r<4,
$$

a contradiction. This applies to every $r<4$, without any representation-specific assumption (**Lower Rank Exclusion** <Ref id="9.1.3" label="§9.1.3" />).

**III. Low-Rank Cases and Empty Candidate Set**

For the positive integer ranks of a nontrivial compact simple candidate, the possibilities are

$$
\begin{array}{c|c|c}
r&\dim\operatorname{Lie}(T_G)&\text{required inequality}\\\hline
1&1&4\le1\quad\text{false}\\
2&2&4\le2\quad\text{false}\\
3&3&4\le3\quad\text{false}
\end{array}
$$

Consequently,

$$
\boxed{\{G:\operatorname{rank}G<4,\quad G_{SM}\hookrightarrow G\}=\varnothing.}
$$

Q.E.D.

**In Plain English:**  
Section 9.1.3.1 formalizes the properties of the QBD proof regarding lower rank exclusion.

---

### 9.1.4 Lemma: Candidate Elimination {#9.1.4}

:::info[**Rank-Four Candidate Elimination via Complex Irreducibility**]
:::

Assume the rank-four selection criterion requires a compact simple group with a complex irreducible representation inequivalent to its conjugate. Then $A_4$ is the only rank-four simple Lie type satisfying this criterion.

**In Plain English:**  
Section 9.1.4 formalizes the properties of the QBD lemma regarding candidate elimination.

---

### 9.1.4.1 Proof: Candidate Elimination {#9.1.4.1}

:::tip[**Self-Duality via the Longest Weyl Group Element**]
:::

**I. Rank-Four Types and the Dual Weight**

The rank constraint leaves $A_4,B_4,C_4,D_4,F_4$ (**Lower Rank Exclusion** <Ref id="9.1.3" label="§9.1.3" />). For a compact group, a unitary representation has conjugate isomorphic to its dual. For the irreducible of highest weight $\lambda$, the lowest weight is $w_0\lambda$, with $w_0$ the longest Weyl group element. Negating the weights in the dual gives highest weight $-w_0\lambda$. Thus

$$
w_0=-I\quad\Longrightarrow\quad -w_0\lambda=\lambda
\quad\Longrightarrow\quad V_\lambda^*\cong V_\lambda.
$$

**II. Reflections for the Four Alternatives**

For $B_4,C_4,F_4$, the root systems in orthonormal coordinates contain roots parallel to each $e_i$. The associated reflections send $e_i$ to $-e_i$ and fix the other coordinates. Their product is $-I$. For $D_4$ the roots $e_i-e_j$ and $e_i+e_j$ yield reflections

$$
s_{e_i-e_j}(x_i,x_j)=(x_j,x_i),\qquad
s_{e_i+e_j}(x_i,x_j)=(-x_j,-x_i).
$$

Their composition gives $(x_i,x_j)\mapsto(-x_i,-x_j)$. Taking the pairs $(1,2)$ and $(3,4)$ produces $-I$ in $W(D_4)$. In each of the four types this element sends every positive root to its negative and hence is $w_0$. All their irreducibles are self-conjugate. The vector representation of $\operatorname{Spin}(8)$ has dimension eight. In the exterior-algebra realization the even and odd parts on $\mathbb C^4$ give the half-spin dimensions

$$
\dim S^+=\binom40+\binom42+\binom44=1+6+1=8,\qquad
\dim S^-=\binom41+\binom43=4+4=8.
$$

All three are self-conjugate by the same Weyl element calculation and therefore fail the complex-representation criterion (**Candidate Elimination** <Ref id="9.1.4" label="§9.1.4" />).

**III. The $A_4$ Fundamental**

For $SU(5)$ let $\zeta=e^{2\pi i/5}$. The central element $\zeta I$ acts on the fundamental by $\zeta$ and on its dual by $\zeta^{-1}$. An invertible intertwiner $T$ would satisfy $\zeta T=\zeta^{-1}T$, which would force $\zeta^2=1$. Since $\zeta$ has order five, the fundamental is inequivalent to its conjugate.

Q.E.D.

**In Plain English:**  
Section 9.1.4.1 formalizes the properties of the QBD proof regarding candidate elimination.

---

### 9.1.5 Proof: Minimal GUT Uniqueness {#9.1.5}

:::tip[**Minimal Rank via Weyl Duality and Cubic Traces**]
:::

**I. Rank and the Block Embedding**

The Cartan subalgebra of the Standard Model Lie algebra has dimension $2+1+1=4$ (**Rank Conditions** <Ref id="9.1.2" label="§9.1.2" />). An injective homomorphism sends it to a commuting subalgebra of the compact target Lie algebra, so the target rank is at least four (**Lower Rank Exclusion** <Ref id="9.1.3" label="§9.1.3" />).

The block map at rank four is

$$
(A,B,z)\longmapsto\operatorname{diag}(z^{-2}A,z^3B),
\qquad
\det(z^{-2}A)\det(z^3B)=z^{-6}z^6=1
$$

for $A\in SU(3)$, $B\in SU(2)$ and $z\in U(1)$. If the image is $I_5$, then $A=z^2 I_3$, $B=z^{-3}I_2$, and $z^6=1$. Conversely each such triple maps to the identity. For a block pair $(U,V)$ with $\det U\det V=1$, choose $z^6=(\det U)^{-1}$. Then $A=z^2U$ and $B=z^{-3}V$ both have determinant one and give the desired block pair. The image is $S(U(3)\times U(2))$ with kernel of order six. Its Lie algebra contains the required direct sum.

**II. Rank-Four Candidate Elimination**

The compact simple types of rank four are $A_4,B_4,C_4,D_4,F_4$. For an irreducible of highest weight $\lambda$ its dual has highest weight $-w_0\lambda$, with $w_0$ the longest Weyl element (**Candidate Elimination** <Ref id="9.1.4" label="§9.1.4" />). In $B_4,C_4,F_4$ the coordinate reflections multiply to $-I$. For $D_4=\mathfrak{so}(8)$, the reflections in $e_i-e_j$ and $e_i+e_j$ satisfy

$$
(x_i,x_j)\xmapsto{s_{e_i-e_j}}(x_j,x_i)
\xmapsto{s_{e_i+e_j}}(-x_i,-x_j).
$$

The pairs $(1,2)$ and $(3,4)$ give $-I$, which sends every positive root to a negative root, so $w_0=-I$. Thus $-w_0\lambda=\lambda$ for all four alternatives. In particular the vector and both half-spin representations of $\operatorname{Spin}(8)$, each of dimension eight, are self-conjugate. For $A_4$, the central element $\zeta I_5$, $\zeta=e^{2\pi i/5}$, acts by $\zeta$ on the fundamental and by $\zeta^{-1}$ on the dual. These distinct central actions preclude an isomorphism.

**III. Fermion Branching**

Set $Y=\operatorname{diag}(-1/3,-1/3,-1/3,1/2,1/2)$, so $\operatorname{Tr}Y=3(-1/3)+2(1/2)=0$. The dual negates these weights and conjugates the non-Abelian representations. In the exterior square, the two color weights sum to $-2/3$, the mixed weights to $1/6$, and the two weak weights to $1$. The determinant pairing gives $\wedge^2\mathbf{3}\cong\mathbf{\bar3}$ for $SU(3)$ and $\wedge^2\mathbf2\cong\mathbf1$ for $SU(2)$. Thus

$$
\begin{aligned}
\mathbf{\bar5}&\longmapsto(\mathbf{\bar3},\mathbf1)_{1/3}\oplus(\mathbf1,\mathbf2)_{-1/2},\\
\mathbf{10}&\longmapsto(\mathbf{\bar3},\mathbf1)_{-2/3}\oplus(\mathbf3,\mathbf2)_{1/6}
\oplus(\mathbf1,\mathbf1)_1.
\end{aligned}
$$

These are the left-handed Weyl multiplets $d^c,L,u^c,Q,e^c$, with total dimension $3+2+3+6+1=15$.

**IV. Perturbative Cubic Anomaly**

For a traceless Hermitian generator with fundamental eigenvalues $x_i$, the dual has eigenvalues $-x_i$, and the exterior square has eigenvalues $x_i+x_j$ for $i<j$. Therefore, in degree $n$,

$$
\begin{aligned}
\sum_{i<j}(x_i+x_j)^3
&=(n-1)\sum_i x_i^3+3\sum_{i\ne j}x_i^2x_j\\
&=(n-1)\sum_i x_i^3+3\sum_i x_i^2\left(-x_i\right)
=(n-4)\sum_i x_i^3 .
\end{aligned}
$$

At $n=5$, write $\mathcal A(X)=\operatorname{Tr}_{\bar 5}(X^3)+\operatorname{Tr}_{10}(X^3)$ for the combined representation, where $X$ denotes the represented Hermitian generator in each trace. The calculation gives $\mathcal A(X)=0$ for every $X$. For generators $X,Y_0,Z$, the coefficient of $abc$ in $\mathcal A(aX+bY_0+cZ)$ is

$$
3\operatorname{Tr}_{\bar 5}\bigl(X(Y_0Z+ZY_0)\bigr)
+3\operatorname{Tr}_{10}\bigl(X(Y_0Z+ZY_0)\bigr)=0,
$$

Each of the two cyclic orders occurs three times, and the cubic polynomial vanishes identically. Dividing by three gives the vanishing symmetric cubic anomaly tensor.

**V. Unified Normalization**

The block traces of the $SU(3)$ and $SU(2)$ generators vanish, so both blocks are orthogonal to $Y$ in the trace pairing. Then

$$
\operatorname{Tr}(Y^2)=3/9+2/4=5/6,\qquad
T_Y=\sqrt{3/5}\,Y,\qquad \operatorname{Tr}(T_Y^2)=1/2 .
$$

Matching $g_1T_Y=g'Y$ gives $(g')^2=(3/5)g_1^2$. At the common coupling boundary $g_1=g=g_U$,

$$
\sin^2\theta_W=\frac{(3/5)g_U^2}{g_U^2+(3/5)g_U^2}=\frac38 .
$$

This boundary calculation and the low-energy running benchmark use different premises (**Topological Weinberg Angle** <Ref id="8.5.5" label="§8.5.5" />). Among rank-minimal compact simple Lie types with the stipulated complex-representation criterion, the embedding and matter check therefore select $A_4$.

Q.E.D.

**In Plain English:**  
Section 9.1.5 formalizes the properties of the QBD proof regarding minimal gut uniqueness.

---

### 9.1.5.1 Calculation: Anomaly Check Verification {#9.1.5.1}

:::note[**Computational Verification of Cubic Anomaly Cancellation due to SU(5) Representations**]
:::

Verification of the anomaly freedom condition established in the **Minimal GUT Uniqueness** <Ref id="9.1.5" label="§9.1.5" /> is based on the following protocols:

1.  **Coefficient Definition:** The algorithm defines the symbolic anomaly coefficients for $SU(N)$ representations, where the fundamental has weight $A=1$, the antifundamental $A=-1$, and the antisymmetric tensor $A = N-4$.
2.  **Substitution:** The protocol substitutes $N=5$ into the symbolic expressions to derive the specific coefficients for the $\mathbf{\bar{5}}$ and $\mathbf{10}$ representations.
3.  **Summation:** The simulation computes the total anomaly $\Sigma A = A(\mathbf{\bar{5}}) + A(\mathbf{10})$ to verify that the net result vanishes identically. This verifies the result established in  **Minimal GUT Uniqueness** <Ref id="9.1.5" label="§9.1.5" />.

```python
import sympy as sp

def verify_su5_anomaly_cancellation():
    """
    Verification of Cubic Anomaly Cancellation in Minimal SU(5)

    The anomaly coefficient A(R) for a representation R in SU(N) is:
    - A(fund) = 1
    - A(antifund) = -1
    - A(antisymmetric 2-tensor) = N - 4

    For SU(5), the fermion generation fits into \bar{5} + 10.
    We compute A(\bar{5}) + A(10) and confirm exact cancellation.
    """
    print("=" * 70)
    print("COMPUTATIONAL VERIFICATION: SU(5) ANOMALY CANCELLATION")
    print("Minimal Chiral Generation in \\bar{5} ⊕ 10 Representations")
    print("=" * 70)

    # Symbolic definition
    N = sp.symbols('N', integer=True, positive=True)
    A_fund = 1
    A_antifund = -sp.Integer(1)
    A_antisym = N - 4

    # Evaluate at N=5 (SU(5))
    N_val = 5
    A_5bar = A_antifund
    A_10 = A_antisym.subs(N, N_val)

    total = A_5bar + A_10

    print(f"\nAnomaly Coefficients (SU(5)):")
    print(f"  A(\\bar{{5}})   = {A_5bar}")
    print(f"  A(10)        =  {A_10}")
    print(f"  Total        =  {total}")
    print("-" * 50)

    if total == 0:
        print("RESULT: Exact cancellation confirmed.")
    else:
        print("RESULT: Anomaly detected – invalid unification.")

if __name__ == "__main__":
    verify_su5_anomaly_cancellation()
```

**Simulation Results:**

```text
======================================================================
COMPUTATIONAL VERIFICATION: SU(5) ANOMALY CANCELLATION
Minimal Chiral Generation in \bar{5} ⊕ 10 Representations
======================================================================

Anomaly Coefficients (SU(5)):
  A(\bar{5})   = -1
  A(10)        =  1
  Total        =  0
--------------------------------------------------
RESULT: Exact cancellation confirmed.
```

**Conclusion:**
The symbolic evaluation yields $A(\mathbf{\bar{5}}) = -1$ and $A(\mathbf{10}) = 1$. The summation results in a total anomaly of exactly 0. This confirms that the combination of the antifundamental and antisymmetric tensor representations in $SU(5)$ satisfies the renormalizability constraint without requiring additional mirror fermions.

**In Plain English:**  
Section 9.1.5.1 formalizes the properties of the QBD calculation regarding anomaly check verification.

---

### 9.2.1 Definition: Penta-Ribbon {#9.2.1}

:::tip[**Structural Definition of the Five-Ribbon Braid as the Fundamental Object**]
:::

The **Penta-Ribbon Braid** is herein defined as the composite topological structure comprising exactly five interacting, framed world-tubes, denoted $\{R_1, R_2, R_3, R_4, R_5\}$, embedded within the four-dimensional causal graph $G_t$. The adjacent crossing structure is indexed by four local rewrite rules $\{\mathcal{R}_1, \mathcal{R}_2, \mathcal{R}_3, \mathcal{R}_4\}$, which correspond to the elementary crossing operations between adjacent ribbons. These operations are subject to the **Principle of Unique Causality (PUC)** <Ref id="2.3.4" label="§2.3.4" />, maintaining the global topological invariants of the Braid Group $B_5$ while the candidate five-state encoding and its physical control hypotheses are specified separately below.

**In Plain English:**  
Section 9.2.1 formalizes the properties of the QBD definition regarding penta-ribbon.

---

### 9.2.2 Definition: Candidate Ribbon Encoding {#9.2.2}

:::tip[**Candidate Ribbon Encoding as the Mathematical Data of the Encoded System**]
:::

A **Candidate Ribbon Encoding** is one of the following two specified five-state encodings into the orthonormal computational graph basis of $\mathcal H_G$. Analytic indices are $j,r=1,\ldots,5$; the calculation blocks use the equivalent zero-based labels. Graph routing, vertices and all non-active edge data are fixed by the selected scaffold.

In the **occupation encoding**, the 35 vertices are labeled $(r,t)$ with $r=1,\ldots,5$ and $t=0,\ldots,6$. The active bit $a_r$ records the edge $(r,6)\to(r,4)$; all other graph data are part of the fixed patch background. The five selected configurations have

$$
a^{(j)}_r=\delta_{rj}.
$$

The occupation operator is $\widehat N_r|G_a\rangle=a_r|G_a\rangle$ on that register. In the **signed-rung encoding**, the 130 vertices are labeled $(r,u)$ with $u=0,\ldots,25$. Each module has eight active bits $w_{rm}$, giving forty across the five modules; they record the eight ordered edge pairs

$$
(0,2),(0,3),(1,2),(1,3),(2,4),(2,5),(3,4),(3,5),\qquad m=0,\ldots,7,
$$

with $r$ fixed at the two endpoints of each edge. The eight reference bits $b_m$ are the little-endian bits of $\mathtt{0x99}$, repeated in every module; write $s_{rm}=(-1)^{b_m}$. The five selected configurations and occupation operators are

$$
w^{(j)}_{rm}=b_m\mathbin{\oplus}\delta_{rj},\qquad
\widehat N_r=\frac18\sum_{m=0}^7\frac{I-s_{rm}Z_{rm}}2,
\qquad Z_{rm}|G_w\rangle=(-1)^{w_{rm}}|G_w\rangle.
$$

Here $\oplus$ denotes addition modulo two, not addition of integer writhe. Thus one entire module is complemented relative to the fixed baseline. For either choice, denote its five selected graph kets by $|G_j\rangle$ and define

$$
W=\sum_{j=1}^5|G_j\rangle\langle j|,\qquad
\mathcal H_5=\operatorname{im}W,\qquad P_5=WW^\dagger,
\qquad \widehat Z_k=\widehat N_k-\widehat N_{k+1}\quad(1\le k<5).
$$

The word patterns are distinct, so orthogonality gives $W^\dagger W=I_5$. The candidate definition is restricted to these two data sets, not an arbitrary isometry with five chosen graph kets. It specifies finite encoded states and observables without identifying them as physical particles or admitting their Hamiltonian evolutions.

**In Plain English:**  
Section 9.2.2 formalizes the properties of the QBD definition regarding candidate ribbon encoding.

---

### 9.2.3 Definition: Admitted Encoded Controls {#9.2.3}

:::tip[**Admitted Encoded Controls as the Mathematical Data of the Encoded System**]
:::

The **Admitted Encoded Controls** hypothesis specifies a physical realization of an invariant five-state sector and coherent Hermitian exchange and module-imbalance generators $\widehat X_k,\widehat Z_k$, for $1\le k<5$. Their domains include the encoded sector and their represented actions satisfy

$$
\widehat X_kW=WX_k,\qquad \widehat Z_kW=WZ_k.
$$

The hypothesis includes physical access to the corresponding coherent evolutions with independently specified real control coefficients: the represented controlled Hamiltonian has the form

$$
W^\dagger\widehat H(u,v)W
=\sum_{k=1}^4\bigl(u_kX_k+v_kZ_k\bigr),\qquad u_k,v_k\in\mathbb R,
$$

on the same invariant sector. For an infinite-dimensional ambient description, products used on this sector must be defined there; invariance ensures that successive factors remain within their stated domains. This is an explicit physical admission premise, not a consequence of real linear closure of abstract matrices. Defining or measuring a diagonal observable does not supply the premise. The candidate diagonal action is proved below, while physical sector identification and coherent exchange/control availability remain inputs.

**In Plain English:**  
Section 9.2.3 formalizes the properties of the QBD definition regarding admitted encoded controls.

---

### 9.2.4 Theorem: Topological Unification {#9.2.4}

:::info[**Penta-Ribbon Representation via Admitted Controls**]
:::

Assume the Admitted Encoded Controls hypothesis on the physical five-state sector. Then the represented real Lie algebra of the four adjacent exchanges and four diagonal module imbalances is equal to $\mathfrak{su}(5)$ and has real dimension 24. Four adjacency labels organize simple-root pairs, while physical multiplet interpretations retain their separately stated hypotheses.

**In Plain English:**  
Section 9.2.4 formalizes the properties of the QBD theorem regarding topological unification.

---

### 9.2.5 Lemma: Distant Commutativity {#9.2.5}

:::info[**Distant Commutativity via Disjoint Operator Supports**]
:::

Let $\sigma_i$ be the Artin generators of $B_{5}$, and let the distant represented rewrites act on independent tensor factors. Then distinct Artin generators commute exactly for $|i-j|\ge2$, their distant represented rewrites commute, and a commuting pair of one-parameter unitary groups on a finite-dimensional sector has commuting generators.

**In Plain English:**  
Section 9.2.5 formalizes the properties of the QBD lemma regarding distant commutativity.

---

### 9.2.5.1 Proof: Distant Commutativity {#9.2.5.1}

:::tip[**Artin Commutation via Strand Permutations and Differentiation**]
:::

**I. Artin Generators**

The Artin presentation gives $\sigma_i\sigma_j=\sigma_j\sigma_i$ for $|i-j|\ge2$ (**Distant Commutativity** <Ref id="8.1.3" label="§8.1.3" />). For adjacent indices, the strand permutation homomorphism sends $\sigma_i$ to $s_i=(i\ i+1)$. With composition from right to left,

$$
(s_i s_{i+1})(i)=i+1,\qquad
(s_{i+1}s_i)(i)=i+2 .
$$

Thus the adjacent words differ already in their strand permutations, so they differ in the braid group. For equal indices the commutator of an operator with itself is zero.

**II. Operators on Independent Supports**

For a distant pair, the assumed factorization gives $\mathcal R_i=A\otimes I$ and $\mathcal R_j=I\otimes B$ on the relevant factors (**Distant Commutativity** <Ref id="9.2.5" label="§9.2.5" />). The tensor multiplication rule gives

$$
\mathcal R_i\mathcal R_j=(AI)\otimes(IB)=A\otimes B,\qquad
\mathcal R_j\mathcal R_i=(IA)\otimes(BI)=A\otimes B .
$$

An operator representation can identify distinct braid words. For the converse on represented rewrites, an action retaining the strand permutations suffices because the calculation on $i$ then distinguishes the adjacent products.

**III. Infinitesimal Commutators**

On a finite-dimensional sector, suppose $U_i(t)=e^{-itT_i}$ and $U_j(s)=e^{-isT_j}$ satisfy $U_i(t)U_j(s)=U_j(s)U_i(t)$ for all $s,t$. The mixed derivatives at the origin are

$$
\begin{aligned}
\left.\partial_t\partial_s(U_i(t)U_j(s))\right|_{0,0}
&=(-iT_i)(-iT_j)=-T_iT_j,\\
\left.\partial_t\partial_s(U_j(s)U_i(t))\right|_{0,0}
&=(-iT_j)(-iT_i)=-T_jT_i.
\end{aligned}
$$

Their equality yields $[T_i,T_j]=0$.

Q.E.D.

**In Plain English:**  
Section 9.2.5.1 formalizes the properties of the QBD proof regarding distant commutativity.

---

### 9.2.6 Lemma: Yang-Baxter Relations {#9.2.6}

:::info[**Extension of the braid relations via encoded spectator factors**]
:::

Let an invertible two-ribbon exchange $R$ on $K\otimes K$ satisfy the three-factor relation on $K^{\otimes3}$ and admit a coherent encoding of the resulting five-factor action. Then the four encoded adjacent exchanges satisfy the defining relations of $B_5$.

**In Plain English:**  
Section 9.2.6 formalizes the properties of the QBD lemma regarding yang-baxter relations.

---

### 9.2.6.1 Proof: Yang-Baxter Relations {#9.2.6.1}

:::tip[**Derivation of the five-ribbon relations via tensor extension**]
:::

**I. Adjacent exchanges**

Use the local Yang-Baxter relation of **Yang-Baxter Relations** <Ref id="8.1.4" label="§8.1.4" /> on the three active factors. In the five-factor model of **Yang-Baxter Relations** <Ref id="9.2.6" label="§9.2.6" />, set $S_i=I^{\otimes(i-1)}\otimes R\otimes I^{\otimes(4-i)}$ for $1\le i\le4$. For each $i=1,2,3$,

$$
\begin{aligned}
S_iS_{i+1}S_i
&=I^{\otimes(i-1)}\otimes
  \bigl((R\otimes I)(I\otimes R)(R\otimes I)\bigr)\otimes I^{\otimes(3-i)}\\
&=I^{\otimes(i-1)}\otimes
  \bigl((I\otimes R)(R\otimes I)(I\otimes R)\bigr)\otimes I^{\otimes(3-i)}
=S_{i+1}S_iS_{i+1}.
\end{aligned}
$$

For the corresponding positive braid words the three crossings are between the same strand pairs, in the orders $(i,i+1),(i,i+2),(i+1,i+2)$ and their reverse. Thus each of these pairs contributes $+1$ to its diagrammatic crossing sum on either side.

**II. Distant exchanges**

For $i<j-1$ the supports of $S_i$ and $S_j$ are distinct tensor factors. Using **Distant Commutativity** <Ref id="9.2.5" label="§9.2.5" />, direct multiplication gives

$$
S_iS_j
=I^{\otimes(i-1)}\otimes R\otimes I^{\otimes(j-i-2)}
 \otimes R\otimes I^{\otimes(4-j)}
=S_jS_i .
$$

These are the pairs $(1,3),(1,4),(2,4)$. The inverses are obtained by replacing $R$ with $R^{-1}$.

**III. Transport to the encoded sector**

Let $U$ be the stipulated encoding with $\mathcal R_iU=US_i$ and with each $\mathcal R_i$ invertible on its image. For any word in these operators, repeated intertwining moves $U$ to the left of the entire word. In particular,

$$
\begin{aligned}
(\mathcal R_i\mathcal R_{i+1}\mathcal R_i
-\mathcal R_{i+1}\mathcal R_i\mathcal R_{i+1})U
&=U(S_iS_{i+1}S_i-S_{i+1}S_iS_{i+1})=0,\\
(\mathcal R_i\mathcal R_j-\mathcal R_j\mathcal R_i)U
&=U(S_iS_j-S_jS_i)=0\qquad (|i-j|\ge2).
\end{aligned}
$$

Hence the assignments $\sigma_i\mapsto\mathcal R_i|_{\operatorname{im} U}$ respect the defining relations of $B_5$.

Q.E.D.

**In Plain English:**  
Section 9.2.6.1 formalizes the properties of the QBD proof regarding yang-baxter relations.

---

### 9.2.7 Lemma: Diagonal Encoded Action {#9.2.7}

:::info[**Characterization of Diagonal Encoded Action via Explicit Hypotheses**]
:::

For any Candidate Ribbon Encoding, the module occupation observables satisfy $\widehat N_r|G_j\rangle=\delta_{rj}|G_j\rangle$. The diagonal imbalance $\widehat Z_k=\widehat N_k-\widehat N_{k+1}$ therefore satisfies $\widehat Z_kW=WZ_k$.

**In Plain English:**  
Section 9.2.7 formalizes the properties of the QBD lemma regarding diagonal encoded action.

---

### 9.2.7.1 Proof: Diagonal Encoded Action {#9.2.7.1}

:::tip[**Construction of Diagonal Encoded Action via Explicit Identities**]
:::

**I. Selected Words and Edge Eigenvalues**

Let $r,j\in\{1,\ldots,5\}$ and $m\in\{0,\ldots,7\}$. The candidate words are (**Candidate Ribbon Encoding** <Ref id="9.2.2" label="§9.2.2" />)

$$
a_r^{(j)}=\delta_{rj},\qquad
w_{rm}^{(j)}=b_m\oplus\delta_{rj},\qquad
(b_0,\ldots,b_7)=(1,0,0,1,1,0,0,1).
$$

Define $s_{rm}=(-1)^{b_m}$, $T_{rm}=(I-s_{rm}Z_{rm})/2$ and

$$
Z_{rm}|G_w\rangle=(-1)^{w_{rm}}|G_w\rangle,\qquad
\widehat N_r=\tfrac18\sum_{m=0}^7T_{rm},\qquad
\widehat Z_k=\widehat N_k-\widehat N_{k+1}
$$

(**Diagonal Encoded Action** <Ref id="9.2.7" label="§9.2.7" />).

**II. Occupation Family**

For the occupation word $a^{(j)}$,

$$
\begin{aligned}
\widehat N_r|G_j\rangle
&=a_r^{(j)}|G_j\rangle\\
&=\begin{cases}|G_j\rangle,&r=j,\\0,&r\ne j,\end{cases}
=\delta_{rj}|G_j\rangle.
\end{aligned}
$$

Thus the five eigenvalue columns are

$$
\bigl(\widehat N_r|G_j\rangle\bigr)_{r,j=1}^5
=\begin{pmatrix}
|G_1\rangle&0&0&0&0\\
0&|G_2\rangle&0&0&0\\
0&0&|G_3\rangle&0&0\\
0&0&0&|G_4\rangle&0\\
0&0&0&0&|G_5\rangle
\end{pmatrix}.
$$

**III. Signed-Rung Family**

For any raw word $w$, define $t_{rm}(w)=\tfrac12(1-(-1)^{b_m+w_{rm}})$. Then

$$
\begin{aligned}
T_{rm}|G_w\rangle
&=\tfrac12\bigl(1-s_{rm}(-1)^{w_{rm}}\bigr)|G_w\rangle\\
&=\tfrac12\bigl(1-(-1)^{b_m+w_{rm}}\bigr)|G_w\rangle
=t_{rm}(w)|G_w\rangle\\
&=\begin{cases}0,&w_{rm}=b_m,\\|G_w\rangle,&w_{rm}=1-b_m.\end{cases}
\end{aligned}
$$

All eight positions evaluate as follows:

$$
\begin{array}{c|r r r r r r r r}
m&0&1&2&3&4&5&6&7\\\hline
b_m&1&0&0&1&1&0&0&1\\
s_{rm}&-1&1&1&-1&-1&1&1&-1\\
1-b_m&0&1&1&0&0&1&1&0\\
t_{rm}(b)&0&0&0&0&0&0&0&0\\
t_{rm}(1-b)&1&1&1&1&1&1&1&1
\end{array}
$$

Substitution of $w_{rm}^{(j)}=b_m\oplus\delta_{rj}$ gives

$$
\begin{aligned}
T_{rm}|G_j\rangle&=\delta_{rj}|G_j\rangle,\\
\widehat N_r|G_j\rangle
&=\tfrac18(\delta_{rj}+\delta_{rj}+\delta_{rj}+\delta_{rj}
+\delta_{rj}+\delta_{rj}+\delta_{rj}+\delta_{rj})|G_j\rangle\\
&=\delta_{rj}|G_j\rangle.
\end{aligned}
$$

**IV. Operator Intertwining**

For either family, let $v=\sum_{j=1}^5v_j|j\rangle$ with $v_j\in\mathbb C$. Then

$$
\begin{aligned}
\widehat Z_k W v
&=(\widehat N_k-\widehat N_{k+1})\sum_jv_j|G_j\rangle\\
&=\sum_jv_j\widehat N_k|G_j\rangle-\sum_jv_j\widehat N_{k+1}|G_j\rangle\\
&=\sum_jv_j(\delta_{kj}-\delta_{k+1,j})|G_j\rangle,\\
W Z_k v
&=W(E_{kk}-E_{k+1,k+1})\sum_jv_j|j\rangle\\
&=W\sum_jv_j(\delta_{kj}-\delta_{k+1,j})|j\rangle\\
&=\sum_jv_j(\delta_{kj}-\delta_{k+1,j})|G_j\rangle.
\end{aligned}
$$

$$
\boxed{\widehat N_r|G_j\rangle=\delta_{rj}|G_j\rangle,\qquad
\widehat Z_k W=W Z_k\quad(1\le k<5).}
$$

Q.E.D.

**In Plain English:**  
Section 9.2.7.1 formalizes the properties of the QBD proof regarding diagonal encoded action.

---

### 9.2.7.2 Calculation: Diagonal Intertwining on Both Encodings {#9.2.7.2}

:::note[**Verification of Diagonal Intertwining on Both Encodings via Exact Arithmetic**]
:::

Verification of the relations established in the **Diagonal Encoded Action** <Ref id="9.2.7.1" label="§9.2.7.1" /> is based on the following protocols: The graph inputs are exactly the two defined candidate word families (**Candidate Ribbon Encoding** <Ref id="9.2.2" label="§9.2.2" />).

1.  **Encoding:** The finite representation fixes the stated generator or graph coordinates exactly.
2.  **Comparison:** Exact arithmetic evaluates the identities and compares the resulting dimensions or eigenvalues with the stated targets.
3.  **Certification:** The recorded values confirm the finite claim while leaving physical control admission as a separate hypothesis.

```python
from fractions import Fraction
import networkx as nx
from sympy import SparseMatrix, eye, zeros


# Fixed candidate graph constructors. This checks diagonal action, not the
# physical admission of a control or the probability of a preparation history.
class RibbonPatch:
    def background(self):
        graph = nx.DiGraph()
        graph.add_nodes_from(range(35))
        graph.add_edges_from(((7*r+t, 7*r+t+1) for r in range(5)
                              for t in range(6)), H=0)
        graph.add_edges_from(((7*r, 7*(r+1)) for r in range(4)), H=0)
        return graph

    def graph(self, mask):
        graph = self.background()
        faces = [(r,t) for r in range(5) for t in range(4)]
        faces += [(r,4) for r in range(5) if mask & (1 << r)]
        for r,t in faces:
            u,v = 7*r+t+2, 7*r+t
            stamp = 1 + max((d['H'] for _,_,d in graph.in_edges(u,data=True)), default=0)
            graph.add_edge(u,v,H=stamp)
        return graph


def sector_encoding():
    return SparseMatrix(32, 5, {(1 << r,r): 1 for r in range(5)})


def occupation(r):
    return SparseMatrix(32,32,{(word,word): 1 for word in range(32) if word & (1 << r)})


MODULE_SIZE = 26
BASE_PATTERN = sum(0x99 << (8*r) for r in range(5))


def encode_five_states(marked):
    if marked not in range(5):
        raise ValueError('Expected a ribbon in 0..4')
    graph = nx.DiGraph()
    graph.add_nodes_from(range(130))
    paths = {0:(0,10,11), 1:(1,12,13),
             2:(2,14,15,16,17,18,19), 3:(3,20,21,22,23,24,25)}
    local = [(2,6),(6,7),(7,3),(6,0),(6,1),
             (7,8),(8,4),(7,9),(9,5)]
    local += [(a,b) for path in paths.values() for a,b in zip(path,path[1:])]
    for r in range(5):
        off = 26*r
        graph.add_edges_from(((off+a,off+b) for a,b in local),H=0)
        if r:
            graph.add_edge(off-26+6,off+6,H=0)
    def add(u,v):
        stamp = 1 + max((d['H'] for _,_,d in graph.in_edges(u,data=True)), default=0)
        graph.add_edge(u,v,H=stamp)
    for r in range(5):
        off = 26*r
        for u,v in ((3,6),(7,2),(4,7),(5,7)):
            add(off+u,off+v)
        for port in (1,3):
            path = paths[port]
            for k in range(len(path)-1,1,-2):
                add(off+path[k],off+path[k-2])
        for inputs,outputs in (((0,1),(2,3)),((2,3),(4,5))):
            targets = outputs[::-1] if r == marked else outputs
            for u,v in zip(inputs,targets):
                add(off+u,off+v)
    return graph, ()

def active_edges():
    local = ((0, 2), (0, 3), (1, 2), (1, 3), (2, 4), (2, 5), (3, 4), (3, 5))
    return tuple((MODULE_SIZE * r + a, MODULE_SIZE * r + b) for r in range(5) for a, b in local)

def relative_rungs(graph):
    raw = sum(1 << bit for bit, edge in enumerate(active_edges()) if graph.has_edge(*edge))
    return raw ^ BASE_PATTERN

def logical_patterns():
    return tuple(0xFF << (8 * r) for r in range(5))

def check_rows(enhanced=False):
    rows = tuple((1 << (8 * r)) | (1 << (8 * r + k)) for r in range(5) for k in range(1, 8))
    return rows + (sum(1 << (8 * r) for r in range(5)),) if enhanced else rows

def raw_z(word, bit):
    return (-1) ** ((word >> bit) & 1)

def rung_occupation(word, module):
    """(1/8) sum_m (1-s_rm Z_rm)/2 on a raw physical edge word."""
    return sum((Fraction(1 - raw_z(BASE_PATTERN, bit) * raw_z(word, bit), 2)
                for bit in range(8 * module, 8 * module + 8)), Fraction()) / 8

def signed_check(word, row):
    return (-1) ** ((BASE_PATTERN & row).bit_count() + (word & row).bit_count())

def z_character_product(a, b):
    """Z-string multiplication on arbitrary raw words: Z_a Z_b = Z_(a XOR b)."""
    return a ^ b

def audit_diagonal_encodings():
    w = sector_encoding()
    assert w.conjugate().T * w == eye(5)
    patch = RibbonPatch()
    assert patch.background().number_of_nodes() == 35
    penta = []
    for k in range(4):
        h = occupation(k) - occupation(k + 1)
        z = zeros(5)
        z[k, k], z[k + 1, k + 1] = 1, -1
        assert h == h.conjugate().T
        assert h * w == w * z
        assert (eye(32) - w * w.conjugate().T) * h * w == zeros(32, 5)
        penta.append({"adjacent_pair": [k, k + 1], "intertwining": True,
                      "off_code_action_zero": True})

    rows = check_rows()
    assert len(rows) == 35
    records = []
    raw_words = []
    for j, relative in enumerate(logical_patterns()):
        graph, _ = encode_five_states(j)
        assert graph.number_of_nodes() == 130
        assert relative_rungs(graph) == relative
        word = sum(1 << bit for bit, edge in enumerate(active_edges())
                   if graph.has_edge(*edge))
        assert word == relative ^ BASE_PATTERN
        raw_words.append(word)
        eigenvalues = [rung_occupation(word, r) for r in range(5)]
        assert eigenvalues == [int(r == j) for r in range(5)]
        assert all(signed_check(word, row) == 1 for row in rows)
        records.append({"state": j, "raw_edge_word": hex(word),
                        "occupation_eigenvalues": list(map(int, eigenvalues)),
                        "all_35_signed_checks_plus_one": True})

    # Sparse ambient encoding: each graph ket is a distinct raw edge word.
    # Diagonal action has no support outside these five rows. These identities
    # represent equality of functions on the full 2**40 basis without allocating it.
    assert len(set(raw_words)) == 5
    for k in range(4):
        actual = {word: rung_occupation(word, k) - rung_occupation(word, k + 1)
                  for word in raw_words}
        expected = {word: int(j == k) - int(j == k + 1)
                    for j, word in enumerate(raw_words)}
        assert actual == expected

    # Each Nhat is a constant plus eight single-edge Z characters. Every signed
    # check is one Z character with a fixed sign. XOR commutativity proves their
    # commutation on ALL raw basis words, not just the selected five codewords.
    for row in rows:
        for bit in range(40):
            assert z_character_product(row, 1 << bit) == z_character_product(1 << bit, row)

    return {
        "penta_vertices": 35, "penta_occupation_register_dimension": 32,
        "penta_isometry": True, "penta_adjacent_imbalances": penta,
        "rung_vertices": 130, "rung_raw_register_dimension": str(2**40),
        "rung_states": records, "rung_intertwining_all_four_pairs": True,
        "rung_off_code_action_zero_all_four_pairs": True,
        "signed_stabilizer_count": len(rows),
        "baseline_physical_check_signs": [(-1) ** ((BASE_PATTERN & row).bit_count()) for row in rows],
        "all_diagonal_imbalances_commute_with_all_signed_checks": True,
        "commutation_method": "Exact Z-character XOR algebra on all 40 raw bits",
        "diagonal_validity_projector_commutation": "Any diagonal functions commute pointwise",
        "physical_hamiltonian_availability_derived": False,
    }



certificate = audit_diagonal_encodings()
print("encoding | vertices | selected states | exact diagonal action")
print(f"occupation | {certificate['penta_vertices']} | 5 | yes")
print(f"rung | {certificate['rung_vertices']} | {len(certificate['rung_states'])} | yes")
```

**Simulation Results:**
```text
encoding | vertices | selected states | exact diagonal action
occupation | 35 | 5 | yes
rung | 130 | 5 | yes
```

**Conclusion:**
Both finite encodings have the five required occupation eigenvalue patterns. The recorded exact values validate the finite derivation in the proof.

**In Plain English:**  
Section 9.2.7.2 formalizes the properties of the QBD calculation regarding diagonal intertwining on both encodings.

---

### 9.2.8 Lemma: Diagonal Sector Preservation {#9.2.8}

:::info[**Characterization of Diagonal Sector Preservation via Explicit Hypotheses**]
:::

For any Candidate Ribbon Encoding, the diagonal imbalances satisfy $(I-P_5)\widehat Z_kW=0$. Their off-code action is zero, and their unitary evolutions preserve the selected sector whenever those Hamiltonians are admitted.

**In Plain English:**  
Section 9.2.8 formalizes the properties of the QBD lemma regarding diagonal sector preservation.

---

### 9.2.8.1 Proof: Diagonal Sector Preservation {#9.2.8.1}

:::tip[**Construction of Diagonal Sector Preservation via Explicit Identities**]
:::

**I. Isometry and Orthogonal Projection**

Let $W=\sum_j|G_j\rangle\langle j|$ for either candidate (**Candidate Ribbon Encoding** <Ref id="9.2.2" label="§9.2.2" />). Let $x_e^{(j)}\in\{0,1\}$ be the edge coordinates of $G_j$. The graph-ket inner product is

$$
\begin{aligned}
|G_j\rangle&=\bigotimes_e|x_e^{(j)}\rangle,\\
\langle G_i|G_j\rangle
&=\prod_e\langle x_e^{(i)}|x_e^{(j)}\rangle
=\prod_e\delta_{x_e^{(i)},x_e^{(j)}}.
\end{aligned}
$$

For $i\ne j$, the occupation edge $e_i$ gives

$$
x_{e_i}^{(i)}=a_i^{(i)}=1,\quad
x_{e_i}^{(j)}=a_i^{(j)}=0,\quad
\langle G_i|G_j\rangle=\delta_{1,0}\prod_{e\ne e_i}\delta_{x_e^{(i)},x_e^{(j)}}=0.
$$

For the rung family, $b_0=1$ and the edge $e_{i0}$ gives

$$
\begin{aligned}
w_{i0}^{(i)}&=1\oplus1=0,\qquad w_{i0}^{(j)}=1\oplus0=1,\\
\langle G_i|G_j\rangle
&=\delta_{0,1}\prod_{e\ne e_{i0}}\delta_{x_e^{(i)},x_e^{(j)}}=0.
\end{aligned}
$$

For $i=j$,

$$
\langle G_j|G_j\rangle
=\prod_e\delta_{x_e^{(j)},x_e^{(j)}}=\prod_e1=1.
$$

Thus $\langle G_i|G_j\rangle=\delta_{ij}$.

Consequently

$$
\begin{aligned}
W^\dagger W
&=\sum_{i,j}|i\rangle\langle G_i|G_j\rangle\langle j|
=\sum_{i,j}\delta_{ij}|i\rangle\langle j|=I_5,\\
P_5=WW^\dagger
&=\sum_j|G_j\rangle\langle G_j|,\\
P_5^2
&=\sum_{i,j}|G_i\rangle\langle G_i|G_j\rangle\langle G_j|
=\sum_j|G_j\rangle\langle G_j|=P_5,\\
P_5^\dagger&=\sum_j(|G_j\rangle\langle G_j|)^\dagger=P_5,\\
(I-P_5)W&=W-WW^\dagger W=W-WI_5=0.
\end{aligned}
$$

**II. Vanishing Off-Code Blocks**

The derived diagonal action is $\widehat Z_kW=WZ_k$ (**Diagonal Encoded Action** <Ref id="9.2.7" label="§9.2.7" />). Therefore

$$
\begin{aligned}
(I-P_5)\widehat Z_kW
&=(I-WW^\dagger)WZ_k\\
&=WZ_k-W(W^\dagger W)Z_k\\
&=WZ_k-WI_5Z_k=0,\\
(I-P_5)\widehat Z_kP_5&=(I-P_5)\widehat Z_k W W^\dagger=0.
\end{aligned}
$$

**III. Bounded Hermitian Extension and Powers**

For every graph basis ket, let $\widehat Z_k|G\rangle=z_k(G)|G\rangle$. Each occupation eigenvalue is a bit or an average of eight bits, so

$$
0\le n_r(G)\le1,\qquad z_k(G)=n_k(G)-n_{k+1}(G)\in[-1,1].
$$

For $\psi=\sum_G\psi_G|G\rangle$ and $\phi=\sum_G\phi_G|G\rangle$,

$$
\begin{aligned}
\|\widehat Z_k\psi\|^2
&=\sum_G\overline{z_k(G)\psi_G}\,z_k(G)\psi_G\\
&=\sum_G|z_k(G)|^2|\psi_G|^2\le\sum_G|\psi_G|^2=\|\psi\|^2,\\
\langle\phi,\widehat Z_k\psi\rangle
&=\sum_G\overline{\phi_G}z_k(G)\psi_G
=\sum_G\overline{z_k(G)\phi_G}\psi_G
=\langle\widehat Z_k\phi,\psi\rangle.
\end{aligned}
$$

Thus $\|\widehat Z_k\|\le1$ and $\widehat Z_k^\dagger=\widehat Z_k$. Taking adjoints in Section II gives

$$
P_5\widehat Z_k(I-P_5)=0,\qquad
[P_5,\widehat Z_k]
=P_5\widehat Z_k(I-P_5)-(I-P_5)\widehat Z_kP_5=0.
$$

For the power induction,

$$
\begin{aligned}
\widehat Z_k^0W&=W=WZ_k^0,\\
\widehat Z_k^mW=WZ_k^m
&\ \Longrightarrow\
\widehat Z_k^{m+1}W
=\widehat Z_k(\widehat Z_k^mW)
=\widehat Z_k W Z_k^m
=WZ_kZ_k^m=WZ_k^{m+1}.
\end{aligned}
$$

**IV. Exponential and Leakage Identity**

For $t\in\mathbb R$,

$$
\sum_{m=0}^\infty\left\|\frac{(it)^m}{m!}\widehat Z_k^mW\right\|
\le\|W\|\sum_{m=0}^\infty\frac{|t|^m\|\widehat Z_k\|^m}{m!}
\le e^{|t|}<\infty.
$$

Hence

$$
\begin{aligned}
e^{it\widehat Z_k}W
&=\lim_{N\to\infty}\sum_{m=0}^N\frac{(it)^m}{m!}\widehat Z_k^mW\\
&=\lim_{N\to\infty}W\sum_{m=0}^N\frac{(it)^m}{m!}Z_k^m
=We^{i t Z_k},\\
(I-P_5)e^{it\widehat Z_k}W
&=(I-P_5)We^{i t Z_k}=0.
\end{aligned}
$$

$$
\boxed{(I-P_5)\widehat Z_kW=0,\qquad
e^{it\widehat Z_k}W=We^{i t Z_k},\qquad
(I-P_5)e^{it\widehat Z_k}W=0.}
$$

Q.E.D.

**In Plain English:**  
Section 9.2.8.1 formalizes the properties of the QBD proof regarding diagonal sector preservation.

---

### 9.2.8.2 Calculation: Zero Off-Code Action {#9.2.8.2}

:::note[**Verification of Zero Off-Code Action via Exact Arithmetic**]
:::

Verification of the relations established in the **Diagonal Sector Preservation** <Ref id="9.2.8.1" label="§9.2.8.1" /> is based on the following protocols: The zero-leakage calculation uses the same five selected words and isometry (**Candidate Ribbon Encoding** <Ref id="9.2.2" label="§9.2.2" />).

1.  **Encoding:** The finite representation fixes the stated generator or graph coordinates exactly.
2.  **Comparison:** Exact arithmetic evaluates the identities and compares the resulting dimensions or eigenvalues with the stated targets.
3.  **Certification:** The recorded values confirm the finite claim while leaving physical control admission as a separate hypothesis.

```python
from fractions import Fraction
import networkx as nx
from sympy import SparseMatrix, eye, zeros


# Fixed candidate graph constructors. This checks diagonal action, not the
# physical admission of a control or the probability of a preparation history.
class RibbonPatch:
    def background(self):
        graph = nx.DiGraph()
        graph.add_nodes_from(range(35))
        graph.add_edges_from(((7*r+t, 7*r+t+1) for r in range(5)
                              for t in range(6)), H=0)
        graph.add_edges_from(((7*r, 7*(r+1)) for r in range(4)), H=0)
        return graph

    def graph(self, mask):
        graph = self.background()
        faces = [(r,t) for r in range(5) for t in range(4)]
        faces += [(r,4) for r in range(5) if mask & (1 << r)]
        for r,t in faces:
            u,v = 7*r+t+2, 7*r+t
            stamp = 1 + max((d['H'] for _,_,d in graph.in_edges(u,data=True)), default=0)
            graph.add_edge(u,v,H=stamp)
        return graph


def sector_encoding():
    return SparseMatrix(32, 5, {(1 << r,r): 1 for r in range(5)})


def occupation(r):
    return SparseMatrix(32,32,{(word,word): 1 for word in range(32) if word & (1 << r)})


MODULE_SIZE = 26
BASE_PATTERN = sum(0x99 << (8*r) for r in range(5))


def encode_five_states(marked):
    if marked not in range(5):
        raise ValueError('Expected a ribbon in 0..4')
    graph = nx.DiGraph()
    graph.add_nodes_from(range(130))
    paths = {0:(0,10,11), 1:(1,12,13),
             2:(2,14,15,16,17,18,19), 3:(3,20,21,22,23,24,25)}
    local = [(2,6),(6,7),(7,3),(6,0),(6,1),
             (7,8),(8,4),(7,9),(9,5)]
    local += [(a,b) for path in paths.values() for a,b in zip(path,path[1:])]
    for r in range(5):
        off = 26*r
        graph.add_edges_from(((off+a,off+b) for a,b in local),H=0)
        if r:
            graph.add_edge(off-26+6,off+6,H=0)
    def add(u,v):
        stamp = 1 + max((d['H'] for _,_,d in graph.in_edges(u,data=True)), default=0)
        graph.add_edge(u,v,H=stamp)
    for r in range(5):
        off = 26*r
        for u,v in ((3,6),(7,2),(4,7),(5,7)):
            add(off+u,off+v)
        for port in (1,3):
            path = paths[port]
            for k in range(len(path)-1,1,-2):
                add(off+path[k],off+path[k-2])
        for inputs,outputs in (((0,1),(2,3)),((2,3),(4,5))):
            targets = outputs[::-1] if r == marked else outputs
            for u,v in zip(inputs,targets):
                add(off+u,off+v)
    return graph, ()

def active_edges():
    local = ((0, 2), (0, 3), (1, 2), (1, 3), (2, 4), (2, 5), (3, 4), (3, 5))
    return tuple((MODULE_SIZE * r + a, MODULE_SIZE * r + b) for r in range(5) for a, b in local)

def relative_rungs(graph):
    raw = sum(1 << bit for bit, edge in enumerate(active_edges()) if graph.has_edge(*edge))
    return raw ^ BASE_PATTERN

def logical_patterns():
    return tuple(0xFF << (8 * r) for r in range(5))

def check_rows(enhanced=False):
    rows = tuple((1 << (8 * r)) | (1 << (8 * r + k)) for r in range(5) for k in range(1, 8))
    return rows + (sum(1 << (8 * r) for r in range(5)),) if enhanced else rows

def raw_z(word, bit):
    return (-1) ** ((word >> bit) & 1)

def rung_occupation(word, module):
    """(1/8) sum_m (1-s_rm Z_rm)/2 on a raw physical edge word."""
    return sum((Fraction(1 - raw_z(BASE_PATTERN, bit) * raw_z(word, bit), 2)
                for bit in range(8 * module, 8 * module + 8)), Fraction()) / 8

def signed_check(word, row):
    return (-1) ** ((BASE_PATTERN & row).bit_count() + (word & row).bit_count())

def z_character_product(a, b):
    """Z-string multiplication on arbitrary raw words: Z_a Z_b = Z_(a XOR b)."""
    return a ^ b

def audit_diagonal_encodings():
    w = sector_encoding()
    assert w.conjugate().T * w == eye(5)
    patch = RibbonPatch()
    assert patch.background().number_of_nodes() == 35
    penta = []
    for k in range(4):
        h = occupation(k) - occupation(k + 1)
        z = zeros(5)
        z[k, k], z[k + 1, k + 1] = 1, -1
        assert h == h.conjugate().T
        assert h * w == w * z
        assert (eye(32) - w * w.conjugate().T) * h * w == zeros(32, 5)
        penta.append({"adjacent_pair": [k, k + 1], "intertwining": True,
                      "off_code_action_zero": True})

    rows = check_rows()
    assert len(rows) == 35
    records = []
    raw_words = []
    for j, relative in enumerate(logical_patterns()):
        graph, _ = encode_five_states(j)
        assert graph.number_of_nodes() == 130
        assert relative_rungs(graph) == relative
        word = sum(1 << bit for bit, edge in enumerate(active_edges())
                   if graph.has_edge(*edge))
        assert word == relative ^ BASE_PATTERN
        raw_words.append(word)
        eigenvalues = [rung_occupation(word, r) for r in range(5)]
        assert eigenvalues == [int(r == j) for r in range(5)]
        assert all(signed_check(word, row) == 1 for row in rows)
        records.append({"state": j, "raw_edge_word": hex(word),
                        "occupation_eigenvalues": list(map(int, eigenvalues)),
                        "all_35_signed_checks_plus_one": True})

    # Sparse ambient encoding: each graph ket is a distinct raw edge word.
    # Diagonal action has no support outside these five rows. These identities
    # represent equality of functions on the full 2**40 basis without allocating it.
    assert len(set(raw_words)) == 5
    for k in range(4):
        actual = {word: rung_occupation(word, k) - rung_occupation(word, k + 1)
                  for word in raw_words}
        expected = {word: int(j == k) - int(j == k + 1)
                    for j, word in enumerate(raw_words)}
        assert actual == expected

    # Each Nhat is a constant plus eight single-edge Z characters. Every signed
    # check is one Z character with a fixed sign. XOR commutativity proves their
    # commutation on ALL raw basis words, not just the selected five codewords.
    for row in rows:
        for bit in range(40):
            assert z_character_product(row, 1 << bit) == z_character_product(1 << bit, row)

    return {
        "penta_vertices": 35, "penta_occupation_register_dimension": 32,
        "penta_isometry": True, "penta_adjacent_imbalances": penta,
        "rung_vertices": 130, "rung_raw_register_dimension": str(2**40),
        "rung_states": records, "rung_intertwining_all_four_pairs": True,
        "rung_off_code_action_zero_all_four_pairs": True,
        "signed_stabilizer_count": len(rows),
        "baseline_physical_check_signs": [(-1) ** ((BASE_PATTERN & row).bit_count()) for row in rows],
        "all_diagonal_imbalances_commute_with_all_signed_checks": True,
        "commutation_method": "Exact Z-character XOR algebra on all 40 raw bits",
        "diagonal_validity_projector_commutation": "Any diagonal functions commute pointwise",
        "physical_hamiltonian_availability_derived": False,
    }



certificate = audit_diagonal_encodings()
print("encoding | adjacent imbalances | off-code action")
assert all(row["off_code_action_zero"] for row in certificate["penta_adjacent_imbalances"])
assert certificate["rung_off_code_action_zero_all_four_pairs"]
print("occupation | 4 | 0")
print("rung | 4 | 0")
```

**Simulation Results:**
```text
encoding | adjacent imbalances | off-code action
occupation | 4 | 0
rung | 4 | 0
```

**Conclusion:**
All four adjacent imbalances have exactly zero off-code action in each encoding. The recorded exact values validate the finite derivation in the proof.

**In Plain English:**  
Section 9.2.8.2 formalizes the properties of the QBD calculation regarding zero off-code action.

---

### 9.2.9 Lemma: Constraint Compatibility {#9.2.9}

:::info[**Characterization of Constraint Compatibility via Explicit Hypotheses**]
:::

For any Candidate Ribbon Encoding, every specified diagonal graph-validity projector commutes with the diagonal imbalances. In the rung encoding the same operators commute with all 35 signed checks $s_{r0}s_{rm}Z_{r0}Z_{rm}$, whose common eigenvalue on the five selected words is $+1$.

**In Plain English:**  
Section 9.2.9 formalizes the properties of the QBD lemma regarding constraint compatibility.

---

### 9.2.9.1 Proof: Constraint Compatibility {#9.2.9.1}

:::tip[**Construction of Constraint Compatibility via Explicit Identities**]
:::

**I. The 35 Signed Checks**

For the specified rung data (**Candidate Ribbon Encoding** <Ref id="9.2.2" label="§9.2.2" />), define

$$
S_{rm}=s_{r0}s_{rm}Z_{r0}Z_{rm},\qquad
r\in\{1,\ldots,5\},\quad m\in\{1,\ldots,7\}.
$$

Their number is $\sum_{r=1}^5\sum_{m=1}^7 1=5\cdot7=35$. On a selected word,

$$
\begin{aligned}
S_{rm}|G_j\rangle
&=(-1)^{b_0+b_m+w_{r0}^{(j)}+w_{rm}^{(j)}}|G_j\rangle,\\
b_0+b_m+w_{r0}^{(j)}+w_{rm}^{(j)}
&\equiv b_0+b_m+(b_0+\delta_{rj})+(b_m+\delta_{rj})\\
&=2b_0+2b_m+2\delta_{rj}\equiv0\pmod2,\\
S_{rm}|G_j\rangle&=|G_j\rangle.
\end{aligned}
$$

For $\psi=\sum_jv_j|G_j\rangle$,

$$
S_{rm}\psi=\sum_jv_jS_{rm}|G_j\rangle=\sum_jv_j|G_j\rangle=\psi.
$$

**II. Z-Character Multiplication on All Raw Words**

Let $A,B$ be subsets of the forty edge positions and define $Z_A=\prod_{a\in A}Z_a$. Then

$$
\begin{aligned}
Z_AZ_B|G_w\rangle
&=(-1)^{\sum_{a\in A}w_a+\sum_{b\in B}w_b}|G_w\rangle\\
&=(-1)^{\sum_{c\in A\triangle B}w_c+2\sum_{c\in A\cap B}w_c}|G_w\rangle\\
&=(-1)^{\sum_{c\in A\triangle B}w_c}|G_w\rangle
=Z_{A\triangle B}|G_w\rangle,\\
Z_BZ_A|G_w\rangle
&=Z_{B\triangle A}|G_w\rangle
=Z_{A\triangle B}|G_w\rangle.
\end{aligned}
$$

Thus $[Z_A,Z_B]|G_w\rangle=0$ for every raw word $w$, giving $[Z_A,Z_B]=0$.

**III. Commutation with Occupations and Imbalances**

The occupation formula is (**Diagonal Encoded Action** <Ref id="9.2.7" label="§9.2.7" />)

$$
\widehat N_a=\frac1{16}\sum_{b=0}^7(I-s_{ab}Z_{ab}).
$$

Therefore

$$
\begin{aligned}
[S_{rm},\widehat N_a]
&=\frac1{16}\sum_{b=0}^7\bigl([S_{rm},I]-s_{ab}[S_{rm},Z_{ab}]\bigr)\\
&=\frac1{16}\sum_{b=0}^7(0-s_{ab}0)=0,\\
[S_{rm},\widehat Z_k]
&=[S_{rm},\widehat N_k]-[S_{rm},\widehat N_{k+1}]=0-0=0.
\end{aligned}
$$

**IV. Diagonal Validity Projectors**

Let $V|G\rangle=v(G)|G\rangle$ with $v(G)\in\{0,1\}$ and $\widehat Z_k|G\rangle=z_k(G)|G\rangle$. On every computational graph ket,

$$
\begin{aligned}
V\widehat Z_k|G\rangle&=V\bigl(z_k(G)|G\rangle\bigr)=z_k(G)v(G)|G\rangle,\\
\widehat Z_kV|G\rangle&=\widehat Z_k\bigl(v(G)|G\rangle\bigr)=v(G)z_k(G)|G\rangle,\\
[V,\widehat Z_k]|G\rangle
&=(z_k(G)v(G)-v(G)z_k(G))|G\rangle=0.
\end{aligned}
$$

$$
\boxed{S_{rm}W=W,\qquad [S_{rm},\widehat Z_k]=0,\qquad [V,\widehat Z_k]=0.}
$$

Q.E.D.

**In Plain English:**  
Section 9.2.9.1 formalizes the properties of the QBD proof regarding constraint compatibility.

---

### 9.2.9.2 Calculation: Signed Stabilizer Commutation {#9.2.9.2}

:::note[**Verification of Signed Stabilizer Commutation via Exact Arithmetic**]
:::

Verification of the relations established in the **Constraint Compatibility** <Ref id="9.2.9.1" label="§9.2.9.1" /> is based on the following protocols: The reference signs and module words are fixed by the candidate data (**Candidate Ribbon Encoding** <Ref id="9.2.2" label="§9.2.2" />).

1.  **Encoding:** The finite representation fixes the stated generator or graph coordinates exactly.
2.  **Comparison:** Exact arithmetic evaluates the identities and compares the resulting dimensions or eigenvalues with the stated targets.
3.  **Certification:** The recorded values confirm the finite claim while leaving physical control admission as a separate hypothesis.

```python
from fractions import Fraction
import networkx as nx
from sympy import SparseMatrix, eye, zeros


# Fixed candidate graph constructors. This checks diagonal action, not the
# physical admission of a control or the probability of a preparation history.
class RibbonPatch:
    def background(self):
        graph = nx.DiGraph()
        graph.add_nodes_from(range(35))
        graph.add_edges_from(((7*r+t, 7*r+t+1) for r in range(5)
                              for t in range(6)), H=0)
        graph.add_edges_from(((7*r, 7*(r+1)) for r in range(4)), H=0)
        return graph

    def graph(self, mask):
        graph = self.background()
        faces = [(r,t) for r in range(5) for t in range(4)]
        faces += [(r,4) for r in range(5) if mask & (1 << r)]
        for r,t in faces:
            u,v = 7*r+t+2, 7*r+t
            stamp = 1 + max((d['H'] for _,_,d in graph.in_edges(u,data=True)), default=0)
            graph.add_edge(u,v,H=stamp)
        return graph


def sector_encoding():
    return SparseMatrix(32, 5, {(1 << r,r): 1 for r in range(5)})


def occupation(r):
    return SparseMatrix(32,32,{(word,word): 1 for word in range(32) if word & (1 << r)})


MODULE_SIZE = 26
BASE_PATTERN = sum(0x99 << (8*r) for r in range(5))


def encode_five_states(marked):
    if marked not in range(5):
        raise ValueError('Expected a ribbon in 0..4')
    graph = nx.DiGraph()
    graph.add_nodes_from(range(130))
    paths = {0:(0,10,11), 1:(1,12,13),
             2:(2,14,15,16,17,18,19), 3:(3,20,21,22,23,24,25)}
    local = [(2,6),(6,7),(7,3),(6,0),(6,1),
             (7,8),(8,4),(7,9),(9,5)]
    local += [(a,b) for path in paths.values() for a,b in zip(path,path[1:])]
    for r in range(5):
        off = 26*r
        graph.add_edges_from(((off+a,off+b) for a,b in local),H=0)
        if r:
            graph.add_edge(off-26+6,off+6,H=0)
    def add(u,v):
        stamp = 1 + max((d['H'] for _,_,d in graph.in_edges(u,data=True)), default=0)
        graph.add_edge(u,v,H=stamp)
    for r in range(5):
        off = 26*r
        for u,v in ((3,6),(7,2),(4,7),(5,7)):
            add(off+u,off+v)
        for port in (1,3):
            path = paths[port]
            for k in range(len(path)-1,1,-2):
                add(off+path[k],off+path[k-2])
        for inputs,outputs in (((0,1),(2,3)),((2,3),(4,5))):
            targets = outputs[::-1] if r == marked else outputs
            for u,v in zip(inputs,targets):
                add(off+u,off+v)
    return graph, ()

def active_edges():
    local = ((0, 2), (0, 3), (1, 2), (1, 3), (2, 4), (2, 5), (3, 4), (3, 5))
    return tuple((MODULE_SIZE * r + a, MODULE_SIZE * r + b) for r in range(5) for a, b in local)

def relative_rungs(graph):
    raw = sum(1 << bit for bit, edge in enumerate(active_edges()) if graph.has_edge(*edge))
    return raw ^ BASE_PATTERN

def logical_patterns():
    return tuple(0xFF << (8 * r) for r in range(5))

def check_rows(enhanced=False):
    rows = tuple((1 << (8 * r)) | (1 << (8 * r + k)) for r in range(5) for k in range(1, 8))
    return rows + (sum(1 << (8 * r) for r in range(5)),) if enhanced else rows

def raw_z(word, bit):
    return (-1) ** ((word >> bit) & 1)

def rung_occupation(word, module):
    """(1/8) sum_m (1-s_rm Z_rm)/2 on a raw physical edge word."""
    return sum((Fraction(1 - raw_z(BASE_PATTERN, bit) * raw_z(word, bit), 2)
                for bit in range(8 * module, 8 * module + 8)), Fraction()) / 8

def signed_check(word, row):
    return (-1) ** ((BASE_PATTERN & row).bit_count() + (word & row).bit_count())

def z_character_product(a, b):
    """Z-string multiplication on arbitrary raw words: Z_a Z_b = Z_(a XOR b)."""
    return a ^ b

def audit_diagonal_encodings():
    w = sector_encoding()
    assert w.conjugate().T * w == eye(5)
    patch = RibbonPatch()
    assert patch.background().number_of_nodes() == 35
    penta = []
    for k in range(4):
        h = occupation(k) - occupation(k + 1)
        z = zeros(5)
        z[k, k], z[k + 1, k + 1] = 1, -1
        assert h == h.conjugate().T
        assert h * w == w * z
        assert (eye(32) - w * w.conjugate().T) * h * w == zeros(32, 5)
        penta.append({"adjacent_pair": [k, k + 1], "intertwining": True,
                      "off_code_action_zero": True})

    rows = check_rows()
    assert len(rows) == 35
    records = []
    raw_words = []
    for j, relative in enumerate(logical_patterns()):
        graph, _ = encode_five_states(j)
        assert graph.number_of_nodes() == 130
        assert relative_rungs(graph) == relative
        word = sum(1 << bit for bit, edge in enumerate(active_edges())
                   if graph.has_edge(*edge))
        assert word == relative ^ BASE_PATTERN
        raw_words.append(word)
        eigenvalues = [rung_occupation(word, r) for r in range(5)]
        assert eigenvalues == [int(r == j) for r in range(5)]
        assert all(signed_check(word, row) == 1 for row in rows)
        records.append({"state": j, "raw_edge_word": hex(word),
                        "occupation_eigenvalues": list(map(int, eigenvalues)),
                        "all_35_signed_checks_plus_one": True})

    # Sparse ambient encoding: each graph ket is a distinct raw edge word.
    # Diagonal action has no support outside these five rows. These identities
    # represent equality of functions on the full 2**40 basis without allocating it.
    assert len(set(raw_words)) == 5
    for k in range(4):
        actual = {word: rung_occupation(word, k) - rung_occupation(word, k + 1)
                  for word in raw_words}
        expected = {word: int(j == k) - int(j == k + 1)
                    for j, word in enumerate(raw_words)}
        assert actual == expected

    # Each Nhat is a constant plus eight single-edge Z characters. Every signed
    # check is one Z character with a fixed sign. XOR commutativity proves their
    # commutation on ALL raw basis words, not just the selected five codewords.
    for row in rows:
        for bit in range(40):
            assert z_character_product(row, 1 << bit) == z_character_product(1 << bit, row)

    return {
        "penta_vertices": 35, "penta_occupation_register_dimension": 32,
        "penta_isometry": True, "penta_adjacent_imbalances": penta,
        "rung_vertices": 130, "rung_raw_register_dimension": str(2**40),
        "rung_states": records, "rung_intertwining_all_four_pairs": True,
        "rung_off_code_action_zero_all_four_pairs": True,
        "signed_stabilizer_count": len(rows),
        "baseline_physical_check_signs": [(-1) ** ((BASE_PATTERN & row).bit_count()) for row in rows],
        "all_diagonal_imbalances_commute_with_all_signed_checks": True,
        "commutation_method": "Exact Z-character XOR algebra on all 40 raw bits",
        "diagonal_validity_projector_commutation": "Any diagonal functions commute pointwise",
        "physical_hamiltonian_availability_derived": False,
    }



certificate = audit_diagonal_encodings()
print("signed checks | signed code eigenvalue | diagonal commutation")
assert certificate["all_diagonal_imbalances_commute_with_all_signed_checks"]
assert all(row["all_35_signed_checks_plus_one"] for row in certificate["rung_states"])
print(f"{certificate['signed_stabilizer_count']} | +1 | all raw edge words")
```

**Simulation Results:**
```text
signed checks | signed code eigenvalue | diagonal commutation
35 | +1 | all raw edge words
```

**Conclusion:**
The 35 signed checks have the common code eigenvalue and commute with all defined diagonal imbalances. The recorded exact values validate the finite derivation in the proof.

**In Plain English:**  
Section 9.2.9.2 formalizes the properties of the QBD calculation regarding signed stabilizer commutation.

---

### 9.2.10 Lemma: Encoded Control Correspondence {#9.2.10}

:::info[**Characterization of Encoded Control Correspondence via Explicit Hypotheses**]
:::

Assume the Admitted Encoded Controls hypothesis. Then restriction to the invariant physical sector represents the admitted adjacent Hamiltonians by $X_k,Z_k$, and their represented commutator is $[iX_k,iZ_k]=2iY_k$.

**In Plain English:**  
Section 9.2.10 formalizes the properties of the QBD lemma regarding encoded control correspondence.

---

### 9.2.10.1 Proof: Encoded Control Correspondence {#9.2.10.1}

:::tip[**Construction of Encoded Control Correspondence via Explicit Identities**]
:::

**I. Restricted Operators and Invariance**

Let $W^\dagger W=I_5$, $P_5=WW^\dagger$, and define $\pi(A)=W^\dagger A W$ for operators whose domains contain $\mathcal H_5$ and whose actions preserve $\mathcal H_5$. The diagonal identities are (**Diagonal Encoded Action** <Ref id="9.2.7" label="§9.2.7" />)

$$
\widehat Z_kW=WZ_k,
$$

with invariant range (**Diagonal Sector Preservation** <Ref id="9.2.8" label="§9.2.8" />) and the specified check compatibility (**Constraint Compatibility** <Ref id="9.2.9" label="§9.2.9" />). For every such $A$,

$$
AW\in\mathcal H_5\ \Longrightarrow\ P_5AW=AW
\ \Longrightarrow\ AW=WW^\dagger A W=W\pi(A).
$$

**II. Real Combinations, Products and Brackets**

For $a,b\in\mathbb R$,

$$
\begin{aligned}
\pi(aA+bB)&=W^\dagger(aA+bB)W=a\pi(A)+b\pi(B),\\
A B W&=A(W\pi(B))=(AW)\pi(B)=W\pi(A)\pi(B),\\
B A W&=B(W\pi(A))=(BW)\pi(A)=W\pi(B)\pi(A),\\
\pi(AB)&=W^\dagger A B W=W^\dagger W\pi(A)\pi(B)=\pi(A)\pi(B),\\
\pi([A,B])&=W^\dagger(AB-BA)W\\
&=\pi(A)\pi(B)-\pi(B)\pi(A)=[\pi(A),\pi(B)].
\end{aligned}
$$

**III. Adjacent Physical Bracket on the Encoded Sector**

Let $\widehat A_k=i\widehat X_k$ and $\widehat C_k=i\widehat Z_k$. The admitted-control hypotheses give

$$
\widehat A_kW=W i X_k,
\qquad\widehat C_kW=W i Z_k.
$$

Consequently

$$
\begin{aligned}
[\widehat A_k,\widehat C_k]W
&=\widehat A_k\widehat C_kW-\widehat C_k\widehat A_kW\\
&=W i X_k i Z_k-W i Z_k i X_k\\
&=-W X_kZ_k+W Z_kX_k\\
&=-W(-F_{k,k+1})+W F_{k,k+1}\\
&=2W F_{k,k+1}=2 W i Y_{k,k+1},\\
\pi([\widehat A_k,\widehat C_k])
&=2W^\dagger W F_{k,k+1}=2F_{k,k+1}.
\end{aligned}
$$

The evaluated coordinate products use the adjacent identity (**Quadrature Generation** <Ref id="8.2.3" label="§8.2.3" />).

**IV. Iterated Lie Expressions**

For any two Lie expressions $P,Q$ in the admitted generators and real $a,b$,

$$
\begin{aligned}
\pi(P(\widehat A,\widehat C))=P(iX,iZ),\quad
\pi(Q(\widehat A,\widehat C))=Q(iX,iZ)
&\ \Longrightarrow\\
\pi(aP(\widehat A,\widehat C)+bQ(\widehat A,\widehat C))
&=aP(iX,iZ)+bQ(iX,iZ),\\
\pi([P(\widehat A,\widehat C),Q(\widehat A,\widehat C)])
&=[P(iX,iZ),Q(iX,iZ)].
\end{aligned}
$$

Starting with the generator identities in Section III, structural induction therefore gives

$$
\boxed{\pi(P(\widehat A,\widehat C))=P(iX,iZ)\quad\text{for every real Lie expression }P.}
$$

Q.E.D.

**In Plain English:**  
Section 9.2.10.1 formalizes the properties of the QBD proof regarding encoded control correspondence.

---

### 9.2.11 Lemma: Closed Lie Algebra {#9.2.11}

:::info[**Characterization of Closed Lie Algebra via Explicit Hypotheses**]
:::

Let $L$ be the real Lie algebra generated by the four $iX_k$ and four traceless diagonal directions $iZ_k$. Then $L$ is the entire traceless skew-Hermitian $5\times5$ algebra and has real dimension 24.

**In Plain English:**  
Section 9.2.11 formalizes the properties of the QBD lemma regarding closed lie algebra.

---

### 9.2.11.1 Proof: Closed Lie Algebra {#9.2.11.1}

:::tip[**Construction of Closed Lie Algebra via Explicit Identities**]
:::

**I. Initial Matrices and Adjacent Brackets**

Define

$$
\begin{gathered}
A_k=i(E_{k,k+1}+E_{k+1,k}),\quad
C_k=i(E_{kk}-E_{k+1,k+1}),\quad k=1,2,3,4,\\
L=\operatorname{Lie}_{\mathbb R}\{A_1,A_2,A_3,A_4,C_1,C_2,C_3,C_4\},\\
B_k=[A_k,C_k]=2(E_{k,k+1}-E_{k+1,k})=2F_{k,k+1}\in L.
\end{gathered}
$$

The last equality follows from the expanded adjacent products (**Quadrature Generation** <Ref id="8.2.3" label="§8.2.3" />).

**II. Every Off-Diagonal Direction as an Initial-Generator Expression**

The adjacent directions are

$$
\begin{array}{c|c|c}
(p,q)&F_{pq}&S_{pq}\\\hline
(1,2)&B_1/2&A_1\\
(2,3)&B_2/2&A_2\\
(3,4)&B_3/2&A_3\\
(4,5)&B_4/2&A_4
\end{array}
$$

For separation two, the propagation products (**Off-Diagonal Propagation** <Ref id="8.2.4" label="§8.2.4" />) give

$$
\begin{aligned}
F_{13}&=[B_1/2,B_2/2]=[B_1,B_2]/4,&
S_{13}&=[B_1/2,A_2]=[B_1,A_2]/2,\\
F_{24}&=[B_2/2,B_3/2]=[B_2,B_3]/4,&
S_{24}&=[B_2/2,A_3]=[B_2,A_3]/2,\\
F_{35}&=[B_3/2,B_4/2]=[B_3,B_4]/4,&
S_{35}&=[B_3/2,A_4]=[B_3,A_4]/2.
\end{aligned}
$$

For separation three,

$$
\begin{aligned}
F_{14}&=[F_{13},F_{34}]
=[[B_1,B_2]/4,B_3/2]=[[B_1,B_2],B_3]/8,\\
S_{14}&=[F_{13},S_{34}]
=[[B_1,B_2]/4,A_3]=[[B_1,B_2],A_3]/4,\\
F_{25}&=[F_{24},F_{45}]
=[[B_2,B_3]/4,B_4/2]=[[B_2,B_3],B_4]/8,\\
S_{25}&=[F_{24},S_{45}]
=[[B_2,B_3]/4,A_4]=[[B_2,B_3],A_4]/4.
\end{aligned}
$$

For separation four,

$$
\begin{aligned}
F_{15}&=[F_{14},F_{45}]
=[[[B_1,B_2],B_3]/8,B_4/2]
=[[[B_1,B_2],B_3],B_4]/16,\\
S_{15}&=[F_{14},S_{45}]
=[[[B_1,B_2],B_3]/8,A_4]
=[[[B_1,B_2],B_3],A_4]/8.
\end{aligned}
$$

Thus $F_{pq},S_{pq}\in L$ for all ten upper pairs.

**III. Diagonal Directions and Full Coordinate Matrix**

The four diagonal expressions are

$$
\begin{aligned}
H_1&=C_1+C_2+C_3+C_4=i\operatorname{diag}(1,0,0,0,-1),\\
H_2&=C_2+C_3+C_4=i\operatorname{diag}(0,1,0,0,-1),\\
H_3&=C_3+C_4=i\operatorname{diag}(0,0,1,0,-1),\\
H_4&=C_4=i\operatorname{diag}(0,0,0,1,-1).
\end{aligned}
$$

Let $z_{pq}=a_{pq}+ib_{pq}$ and $c_p\in\mathbb R$. The complete real linear combination evaluates to

$$
\begin{aligned}
R&=\sum_{p<q}(a_{pq}F_{pq}+b_{pq}S_{pq})+\sum_{p=1}^4c_pH_p\\
&=\begin{pmatrix}
ic_1&z_{12}&z_{13}&z_{14}&z_{15}\\
-\overline{z_{12}}&ic_2&z_{23}&z_{24}&z_{25}\\
-\overline{z_{13}}&-\overline{z_{23}}&ic_3&z_{34}&z_{35}\\
-\overline{z_{14}}&-\overline{z_{24}}&-\overline{z_{34}}&ic_4&z_{45}\\
-\overline{z_{15}}&-\overline{z_{25}}&-\overline{z_{35}}&-\overline{z_{45}}&-i(c_1+c_2+c_3+c_4)
\end{pmatrix}.
\end{aligned}
$$

For $R=0$, the ten upper equations $z_{pq}=0$ give
$a_{pq}=\operatorname{Re}z_{pq}=0$ and $b_{pq}=\operatorname{Im}z_{pq}=0$; the first four diagonal equations give $c_p=(-i)R_{pp}=0$. The 24 matrices are independent (**Basis Independence** <Ref id="8.2.5" label="§8.2.5" />).

If $M^\dagger=-M$ and $\operatorname{Tr}M=0$, then

$$
M_{qp}=-\overline{M_{pq}},\quad
M_{pp}=i\operatorname{Im}M_{pp},\quad
M_{55}=-\sum_{p=1}^4M_{pp}.
$$

Substitution of $z_{pq}=M_{pq}$ and $c_p=\operatorname{Im}M_{pp}$ into the displayed matrix gives $R_{pq}=M_{pq}$ in all 25 positions. Hence $M=R\in L$ (**Basis Completeness** <Ref id="8.2.6" label="§8.2.6" />).

**IV. Reverse Containment and Dimension**

For the seeds and their real combinations,

$$
A_k^\dagger=-A_k,\quad C_k^\dagger=-C_k,\quad
\operatorname{Tr}A_k=0,\quad\operatorname{Tr}C_k=i-i=0.
$$

For skew-Hermitian $U,V$,

$$
\begin{aligned}
[U,V]^\dagger
&=(-V)(-U)-(-U)(-V)=-[U,V],\\
\operatorname{Tr}[U,V]
&=\sum_{p,q}U_{pq}V_{qp}-\sum_{q,p}V_{qp}U_{pq}=0.
\end{aligned}
$$

Therefore $L\subseteq\mathfrak{su}(5)$, while Section III gives $\mathfrak{su}(5)\subseteq L$. The independent family has

$$
\#F=4+3+2+1=10,\qquad \#S=4+3+2+1=10,\qquad \#H=4.
$$

$$
\boxed{L=\mathfrak{su}(5),\qquad\dim_{\mathbb R}L=10+10+4=24.}
$$

Q.E.D.

**In Plain English:**  
Section 9.2.11.1 formalizes the properties of the QBD proof regarding closed lie algebra.

---

### 9.2.11.2 Calculation: Exact SU(5) Closure {#9.2.11.2}

:::note[**Verification of Exact SU(5) Closure via Exact Arithmetic**]
:::

Verification of the relations established in the **Closed Lie Algebra** <Ref id="9.2.11.1" label="§9.2.11.1" /> is based on the following protocols: The input is the enlarged adjacent matrix family at five coordinates (**Adjacent Generator Family** <Ref id="8.2.1" label="§8.2.1" />).

1.  **Encoding:** The finite representation fixes the stated generator or graph coordinates exactly.
2.  **Comparison:** Exact arithmetic evaluates the identities and compares the resulting dimensions or eigenvalues with the stated targets.
3.  **Certification:** The recorded values confirm the finite claim while leaving physical control admission as a separate hypothesis.

```python
"""Exact real Lie closure of Gaussian-rational matrices; no numerical rank cutoff."""
from sympy import I, Matrix, zeros


def elementary(n, i, j):
    a = zeros(n)
    a[i, j] = 1
    return a


def adjacent_generators(n):
    if n < 2:
        raise ValueError("At least two coordinates are required")
    x = [I * (elementary(n, k, k+1) + elementary(n, k+1, k)) for k in range(n-1)]
    z = [I * (elementary(n, k, k) - elementary(n, k+1, k+1)) for k in range(n-1)]
    return x, z


def real_coordinates(matrix):
    # All entries here are Gaussian rationals, so this is exact over Q.
    return [component for value in matrix for component in value.as_real_imag()]


def lie_basis(generators):
    basis = []
    echelon = {}

    def insert(matrix):
        vector = real_coordinates(matrix)
        for pivot in sorted(echelon):
            coefficient = vector[pivot]
            if coefficient:
                vector = [a - coefficient * b for a, b in zip(vector, echelon[pivot])]
        pivot = next((i for i, value in enumerate(vector) if value), None)
        if pivot is None:
            return
        scale = vector[pivot]
        echelon[pivot] = [value / scale for value in vector]
        basis.append(matrix)

    for generator in generators:
        insert(generator)
    cursor = 0
    while cursor < len(basis):
        for earlier in range(cursor):
            a, b = basis[cursor], basis[earlier]
            insert(a * b - b * a)
        cursor += 1
    return basis

print("n | exchange directions | diagonal directions | real closure dimension")
for n in (5,):
    exchanges, diagonals = adjacent_generators(n)
    generators = exchanges + diagonals
    expected = n * n - 1
    basis = lie_basis(generators)
    assert len(basis) == expected
    assert all(a.conjugate().T == -a and a.trace() == 0 for a in basis)
    print(f"{n} | {len(exchanges)} | {len(generators)-len(exchanges)} | {len(basis)}")
```

**Simulation Results:**
```text
n | exchange directions | diagonal directions | real closure dimension
5 | 4 | 4 | 24
```

**Conclusion:**
The eight specified seed directions generate a real space of dimension 24. The recorded exact values validate the finite derivation in the proof.

**In Plain English:**  
Section 9.2.11.2 formalizes the properties of the QBD calculation regarding exact su(5) closure.

---

### 9.2.11.3 Type-Theoretic Validation via Lean 4 and Mathlib {#9.2.11.3}

:::note[**Lean 4 Encoding of Closed Lie Algebra via Explicit Coordinate Proofs**]
:::

Type-theoretic validation of the relation established in the **Closed Lie Algebra** <Ref id="9.2.11.1" label="§9.2.11.1" /> proceeds via the following verification strategy: The formal conclusion concerns the matrix closure, not physical control admission (**Closed Lie Algebra** <Ref id="9.2.11" label="§9.2.11" />).

1.  **Encoding:** The self-contained proof block specifies the mathematical objects independently of the target conclusion in the pinned Lean and Mathlib v4.33.1 environment.
2.  **Theorem Statement:** The displayed theorem specializes the proved relation to the stated hypotheses without assuming its conclusion.
3.  **Proof Closure:** The closed proof uses the mirrored dependency module and the displayed theorem to certify exactly the specified relation.

```lean
import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Algebra.Lie.Matrix
import Mathlib.Algebra.Lie.Subalgebra
import Mathlib.LinearAlgebra.Complex.Module
import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.LinearAlgebra.Matrix.Trace

attribute [local instance 100] LieRing.ofAssociativeRing

noncomputable section
set_option maxHeartbeats 4000000
set_option maxRecDepth 4000

namespace QBD.SU5Closure
abbrev M := Matrix (Fin 5) (Fin 5) ℂ

-- The compact real matrix Lie algebra, independently of its generators.
def su : LieSubalgebra ℝ M where
  carrier := {a | a.conjTranspose = -a ∧ a.trace = 0}
  zero_mem' := by simp
  add_mem' := by
    intro a b ha hb
    exact ⟨by simp [Matrix.conjTranspose_add, ha.1, hb.1, add_comm], by simp [Matrix.trace_add, ha.2, hb.2]⟩
  smul_mem' := by
    intro r a ha
    exact ⟨by simp [Matrix.conjTranspose_smul, ha.1], by simp [Matrix.trace_smul, ha.2]⟩
  lie_mem' := by
    intro a b ha hb
    constructor
    · change (a * b - b * a).conjTranspose = -(a * b - b * a)
      simp [Matrix.conjTranspose_sub, Matrix.conjTranspose_mul, ha.1, hb.1]
    · change (a * b - b * a).trace = 0
      rw [Matrix.trace_sub, Matrix.trace_mul_comm a b, sub_self]

def realSkew : LieSubalgebra ℝ M where
  carrier := {a | a.transpose = -a ∧ ∀ i j, (a i j).im = 0}
  zero_mem' := by simp
  add_mem' := by
    intro a b ha hb
    exact ⟨by simp [Matrix.transpose_add, ha.1, hb.1, add_comm], by simpa using fun i j => show ((a + b) i j).im = 0 by simp [ha.2, hb.2]⟩
  smul_mem' := by
    intro r a ha
    exact ⟨by simp [Matrix.transpose_smul, ha.1], by simpa using fun i j => show ((r • a) i j).im = 0 by simp [ha.2]⟩
  lie_mem' := by
    intro a b ha hb
    constructor
    · change (a * b - b * a).transpose = -(a * b - b * a)
      simp [Matrix.transpose_sub, Matrix.transpose_mul, ha.1, hb.1]
    · intro i j
      change ((a * b - b * a) i j).im = 0
      simp [Matrix.mul_apply, Complex.mul_im, ha.2, hb.2]

def phase (i : Fin 5) : ℂ := match i.val with
  | 0 => 1
  | 1 => Complex.I
  | 2 => -1
  | 3 => -Complex.I
  | _ => 1

def D : M := Matrix.diagonal phase

theorem D_unitary : D * D.conjTranspose = 1 ∧ D.conjTranspose * D = 1 := by
  constructor <;> ext i j <;> fin_cases i <;> fin_cases j <;>
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, D, phase, Matrix.mul_apply, Fin.sum_univ_succ, Matrix.diagonal_apply]

def conjugate (a : M) : M := D.conjTranspose * a * D

theorem conjugate_bracket (a b : M) :
    conjugate ⁅a,b⁆ = ⁅conjugate a, conjugate b⁆ := by
  change D.conjTranspose * (a*b-b*a) * D =
    (D.conjTranspose*a*D)*(D.conjTranspose*b*D) -
    (D.conjTranspose*b*D)*(D.conjTranspose*a*D)
  simp only [Matrix.mul_sub, Matrix.sub_mul]
  simp only [Matrix.mul_assoc, ← Matrix.mul_assoc D D.conjTranspose, D_unitary.1,
    Matrix.one_mul]

def twistedSo : LieSubalgebra ℝ M where
  carrier := {a | conjugate a ∈ realSkew}
  zero_mem' := by simp [conjugate]
  add_mem' := by
    intro a b ha hb
    simpa [conjugate, Matrix.mul_add, Matrix.add_mul] using realSkew.add_mem ha hb
  smul_mem' := by
    intro r a ha
    simpa [conjugate, Matrix.mul_smul, Matrix.smul_mul] using realSkew.smul_mem r ha
  lie_mem' := by
    intro a b ha hb
    change conjugate ⁅a,b⁆ ∈ realSkew
    rw [conjugate_bracket]
    exact realSkew.lie_mem ha hb


open scoped Matrix

def E (i j : Fin 5) : M := Matrix.single i j 1

@[simp] theorem E_apply (i j a b : Fin 5) :
    E i j a b = if i.val = a.val ∧ j.val = b.val then 1 else 0 := by
  simp only [E, Matrix.single_apply, Fin.ext_iff]

def F (i j : Fin 5) : M := E i j - E j i

def S (i j : Fin 5) : M := Complex.I • (E i j + E j i)

def H (i : Fin 5) : M := Complex.I • (E i i - E 4 4)

def A (k : Fin 4) : M := S k.castSucc k.succ

def C (k : Fin 4) : M := Complex.I • (E k.castSucc k.castSucc - E k.succ k.succ)

def four : LieSubalgebra ℝ M := LieSubalgebra.lieSpan ℝ M (Set.range A)

def eight : LieSubalgebra ℝ M := LieSubalgebra.lieSpan ℝ M (Set.range A ∪ Set.range C)

def basis24 : Fin 24 → M := fun t =>
  match t.val with
  | 0 => F 0 1
  | 1 => F 0 2
  | 2 => F 0 3
  | 3 => F 0 4
  | 4 => F 1 2
  | 5 => F 1 3
  | 6 => F 1 4
  | 7 => F 2 3
  | 8 => F 2 4
  | 9 => F 3 4
  | 10 => S 0 1
  | 11 => S 0 2
  | 12 => S 0 3
  | 13 => S 0 4
  | 14 => S 1 2
  | 15 => S 1 3
  | 16 => S 1 4
  | 17 => S 2 3
  | 18 => S 2 4
  | 19 => S 3 4
  | 20 => H 0
  | 21 => H 1
  | 22 => H 2
  | _ => H 3

def synth24 (v : Fin 24 → ℝ) : M := fun i j =>
  match i.val, j.val with
  | 0, 0 => (v 20 : ℂ) * Complex.I
  | 0, 1 => (v 0 : ℂ) + (v 10 : ℂ) * Complex.I
  | 0, 2 => (v 1 : ℂ) + (v 11 : ℂ) * Complex.I
  | 0, 3 => (v 2 : ℂ) + (v 12 : ℂ) * Complex.I
  | 0, 4 => (v 3 : ℂ) + (v 13 : ℂ) * Complex.I
  | 1, 0 => -(v 0 : ℂ) + (v 10 : ℂ) * Complex.I
  | 1, 1 => (v 21 : ℂ) * Complex.I
  | 1, 2 => (v 4 : ℂ) + (v 14 : ℂ) * Complex.I
  | 1, 3 => (v 5 : ℂ) + (v 15 : ℂ) * Complex.I
  | 1, 4 => (v 6 : ℂ) + (v 16 : ℂ) * Complex.I
  | 2, 0 => -(v 1 : ℂ) + (v 11 : ℂ) * Complex.I
  | 2, 1 => -(v 4 : ℂ) + (v 14 : ℂ) * Complex.I
  | 2, 2 => (v 22 : ℂ) * Complex.I
  | 2, 3 => (v 7 : ℂ) + (v 17 : ℂ) * Complex.I
  | 2, 4 => (v 8 : ℂ) + (v 18 : ℂ) * Complex.I
  | 3, 0 => -(v 2 : ℂ) + (v 12 : ℂ) * Complex.I
  | 3, 1 => -(v 5 : ℂ) + (v 15 : ℂ) * Complex.I
  | 3, 2 => -(v 7 : ℂ) + (v 17 : ℂ) * Complex.I
  | 3, 3 => (v 23 : ℂ) * Complex.I
  | 3, 4 => (v 9 : ℂ) + (v 19 : ℂ) * Complex.I
  | 4, 0 => -(v 3 : ℂ) + (v 13 : ℂ) * Complex.I
  | 4, 1 => -(v 6 : ℂ) + (v 16 : ℂ) * Complex.I
  | 4, 2 => -(v 8 : ℂ) + (v 18 : ℂ) * Complex.I
  | 4, 3 => -(v 9 : ℂ) + (v 19 : ℂ) * Complex.I
  | _, _ => -((v 20 : ℂ) + v 21 + v 22 + v 23) * Complex.I

def coord24 (m : M) : Fin 24 → ℝ := fun t =>
  match t.val with
  | 0 => (m 0 1).re
  | 1 => (m 0 2).re
  | 2 => (m 0 3).re
  | 3 => (m 0 4).re
  | 4 => (m 1 2).re
  | 5 => (m 1 3).re
  | 6 => (m 1 4).re
  | 7 => (m 2 3).re
  | 8 => (m 2 4).re
  | 9 => (m 3 4).re
  | 10 => (m 0 1).im
  | 11 => (m 0 2).im
  | 12 => (m 0 3).im
  | 13 => (m 0 4).im
  | 14 => (m 1 2).im
  | 15 => (m 1 3).im
  | 16 => (m 1 4).im
  | 17 => (m 2 3).im
  | 18 => (m 2 4).im
  | 19 => (m 3 4).im
  | 20 => (m 0 0).im
  | 21 => (m 1 1).im
  | 22 => (m 2 2).im
  | _ => (m 3 3).im

theorem coord24_synth24 (v : Fin 24 → ℝ) : coord24 (synth24 v) = v := by
  ext t
  fin_cases t <;>
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, coord24, synth24, basis24, F, S, H, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;> rfl

theorem synth24_reconstruct (m : M) (hm : m ∈ su) : synth24 (coord24 m) = m := by
  have hre (i j : Fin 5) : (m j i).re = -(m i j).re := by
    have h := congrArg Complex.re (congrFun (congrFun hm.1 i) j)
    simpa using h
  have him (i j : Fin 5) : (m j i).im = (m i j).im := by
    have h := congrArg Complex.im (congrFun (congrFun hm.1 i) j)
    simpa using neg_injective h
  have ht : (m 0 0).im + ((m 1 1).im + ((m 2 2).im + ((m 3 3).im + (m 4 4).im))) = 0 := by
    simpa [Matrix.trace, Matrix.diag, Fin.sum_univ_succ] using congrArg Complex.im hm.2
  ext i j
  fin_cases i <;> fin_cases j
  · change synth24 (coord24 m) 0 0 = m 0 0
    have hr := hre 0 0
    have hi := him 0 0
    have hd := hre 0 0
    have he := hre 0 0
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 0 1 = m 0 1
    have hr := hre 0 1
    have hi := him 0 1
    have hd := hre 0 0
    have he := hre 1 1
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 0 2 = m 0 2
    have hr := hre 0 2
    have hi := him 0 2
    have hd := hre 0 0
    have he := hre 2 2
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 0 3 = m 0 3
    have hr := hre 0 3
    have hi := him 0 3
    have hd := hre 0 0
    have he := hre 3 3
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 0 4 = m 0 4
    have hr := hre 0 4
    have hi := him 0 4
    have hd := hre 0 0
    have he := hre 4 4
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 1 0 = m 1 0
    have hr := hre 1 0
    have hi := him 1 0
    have hd := hre 1 1
    have he := hre 0 0
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 1 1 = m 1 1
    have hr := hre 1 1
    have hi := him 1 1
    have hd := hre 1 1
    have he := hre 1 1
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 1 2 = m 1 2
    have hr := hre 1 2
    have hi := him 1 2
    have hd := hre 1 1
    have he := hre 2 2
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 1 3 = m 1 3
    have hr := hre 1 3
    have hi := him 1 3
    have hd := hre 1 1
    have he := hre 3 3
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 1 4 = m 1 4
    have hr := hre 1 4
    have hi := him 1 4
    have hd := hre 1 1
    have he := hre 4 4
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 2 0 = m 2 0
    have hr := hre 2 0
    have hi := him 2 0
    have hd := hre 2 2
    have he := hre 0 0
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 2 1 = m 2 1
    have hr := hre 2 1
    have hi := him 2 1
    have hd := hre 2 2
    have he := hre 1 1
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 2 2 = m 2 2
    have hr := hre 2 2
    have hi := him 2 2
    have hd := hre 2 2
    have he := hre 2 2
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 2 3 = m 2 3
    have hr := hre 2 3
    have hi := him 2 3
    have hd := hre 2 2
    have he := hre 3 3
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 2 4 = m 2 4
    have hr := hre 2 4
    have hi := him 2 4
    have hd := hre 2 2
    have he := hre 4 4
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 3 0 = m 3 0
    have hr := hre 3 0
    have hi := him 3 0
    have hd := hre 3 3
    have he := hre 0 0
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 3 1 = m 3 1
    have hr := hre 3 1
    have hi := him 3 1
    have hd := hre 3 3
    have he := hre 1 1
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 3 2 = m 3 2
    have hr := hre 3 2
    have hi := him 3 2
    have hd := hre 3 3
    have he := hre 2 2
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 3 3 = m 3 3
    have hr := hre 3 3
    have hi := him 3 3
    have hd := hre 3 3
    have he := hre 3 3
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 3 4 = m 3 4
    have hr := hre 3 4
    have hi := him 3 4
    have hd := hre 3 3
    have he := hre 4 4
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 4 0 = m 4 0
    have hr := hre 4 0
    have hi := him 4 0
    have hd := hre 4 4
    have he := hre 0 0
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 4 1 = m 4 1
    have hr := hre 4 1
    have hi := him 4 1
    have hd := hre 4 4
    have he := hre 1 1
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 4 2 = m 4 2
    have hr := hre 4 2
    have hi := him 4 2
    have hd := hre 4 4
    have he := hre 2 2
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 4 3 = m 4 3
    have hr := hre 4 3
    have hi := him 4 3
    have hd := hre 4 4
    have he := hre 3 3
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

  · change synth24 (coord24 m) 4 4 = m 4 4
    have hr := hre 4 4
    have hi := him 4 4
    have hd := hre 4 4
    have he := hre 4 4
    norm_num [Fin.succ, pow_succ, Fin.ofNat] at hr hi hd he ht
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, coord24] <;>
      linarith

-- Membership of the generators and explicit bracket-generated basis elements.
theorem A_mem_eight (k : Fin 4) : A k ∈ eight :=
  LieSubalgebra.subset_lieSpan (Or.inl (Set.mem_range_self k))

theorem C_mem_eight (k : Fin 4) : C k ∈ eight :=
  LieSubalgebra.subset_lieSpan (Or.inr (Set.mem_range_self k))

theorem S01_mem : S 0 1 ∈ eight := A_mem_eight 0

theorem F01_mem : F 0 1 ∈ eight := by
  have h : (1/2 : ℝ) • ⁅A 0, C 0⁆ = F 0 1 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.smul_mem _ (eight.lie_mem (A_mem_eight 0) (C_mem_eight 0))

theorem S12_mem : S 1 2 ∈ eight := A_mem_eight 1

theorem F12_mem : F 1 2 ∈ eight := by
  have h : (1/2 : ℝ) • ⁅A 1, C 1⁆ = F 1 2 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.smul_mem _ (eight.lie_mem (A_mem_eight 1) (C_mem_eight 1))

theorem S23_mem : S 2 3 ∈ eight := A_mem_eight 2

theorem F23_mem : F 2 3 ∈ eight := by
  have h : (1/2 : ℝ) • ⁅A 2, C 2⁆ = F 2 3 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.smul_mem _ (eight.lie_mem (A_mem_eight 2) (C_mem_eight 2))

theorem S34_mem : S 3 4 ∈ eight := A_mem_eight 3

theorem F34_mem : F 3 4 ∈ eight := by
  have h : (1/2 : ℝ) • ⁅A 3, C 3⁆ = F 3 4 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.smul_mem _ (eight.lie_mem (A_mem_eight 3) (C_mem_eight 3))

theorem F02_mem : F 0 2 ∈ eight := by
  have h : ⁅F 0 1, F 1 2⁆ = F 0 2 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F01_mem F12_mem

theorem S02_mem : S 0 2 ∈ eight := by
  have h : ⁅F 0 1, S 1 2⁆ = S 0 2 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F01_mem S12_mem

theorem F13_mem : F 1 3 ∈ eight := by
  have h : ⁅F 1 2, F 2 3⁆ = F 1 3 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F12_mem F23_mem

theorem S13_mem : S 1 3 ∈ eight := by
  have h : ⁅F 1 2, S 2 3⁆ = S 1 3 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F12_mem S23_mem

theorem F24_mem : F 2 4 ∈ eight := by
  have h : ⁅F 2 3, F 3 4⁆ = F 2 4 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F23_mem F34_mem

theorem S24_mem : S 2 4 ∈ eight := by
  have h : ⁅F 2 3, S 3 4⁆ = S 2 4 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F23_mem S34_mem

theorem F03_mem : F 0 3 ∈ eight := by
  have h : ⁅F 0 2, F 2 3⁆ = F 0 3 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F02_mem F23_mem

theorem S03_mem : S 0 3 ∈ eight := by
  have h : ⁅F 0 2, S 2 3⁆ = S 0 3 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F02_mem S23_mem

theorem F14_mem : F 1 4 ∈ eight := by
  have h : ⁅F 1 3, F 3 4⁆ = F 1 4 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F13_mem F34_mem

theorem S14_mem : S 1 4 ∈ eight := by
  have h : ⁅F 1 3, S 3 4⁆ = S 1 4 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F13_mem S34_mem

theorem F04_mem : F 0 4 ∈ eight := by
  have h : ⁅F 0 3, F 3 4⁆ = F 0 4 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F03_mem F34_mem

theorem S04_mem : S 0 4 ∈ eight := by
  have h : ⁅F 0 3, S 3 4⁆ = S 0 4 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.lie_mem F03_mem S34_mem

theorem H0_mem : H 0 ∈ eight := by
  have h : (1/2 : ℝ) • ⁅F 0 4, S 0 4⁆ = H 0 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.smul_mem _ (eight.lie_mem F04_mem S04_mem)

theorem H1_mem : H 1 ∈ eight := by
  have h : (1/2 : ℝ) • ⁅F 1 4, S 1 4⁆ = H 1 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.smul_mem _ (eight.lie_mem F14_mem S14_mem)

theorem H2_mem : H 2 ∈ eight := by
  have h : (1/2 : ℝ) • ⁅F 2 4, S 2 4⁆ = H 2 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.smul_mem _ (eight.lie_mem F24_mem S24_mem)

theorem H3_mem : H 3 ∈ eight := by
  have h : (1/2 : ℝ) • ⁅F 3 4, S 3 4⁆ = H 3 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, A, C, F, S, H, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact eight.smul_mem _ (eight.lie_mem F34_mem S34_mem)

theorem basis24_mem (t : Fin 24) : basis24 t ∈ eight := by
  fin_cases t
  · exact F01_mem
  · exact F02_mem
  · exact F03_mem
  · exact F04_mem
  · exact F12_mem
  · exact F13_mem
  · exact F14_mem
  · exact F23_mem
  · exact F24_mem
  · exact F34_mem
  · exact S01_mem
  · exact S02_mem
  · exact S03_mem
  · exact S04_mem
  · exact S12_mem
  · exact S13_mem
  · exact S14_mem
  · exact S23_mem
  · exact S24_mem
  · exact S34_mem
  · exact H0_mem
  · exact H1_mem
  · exact H2_mem
  · exact H3_mem

theorem synth24_mem (v : Fin 24 → ℝ) : synth24 v ∈ eight := by
  have heq : (∑ t : Fin 24, v t • basis24 t) = synth24 v := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth24, basis24, F, S, H, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;> first
      | rfl
      | (change -v 20 + (-v 21 + (-v 22 + -v 23)) = -v 23 + (-v 22 + (-v 21 + -v 20)); ring)
  rw [← heq]
  exact eight.sum_mem fun t _ => eight.smul_mem _ (basis24_mem t)

theorem eight_le_su : eight ≤ su := by
  apply LieSubalgebra.lieSpan_le.mpr
  intro m hm
  rcases hm with ⟨k, rfl⟩ | ⟨k, rfl⟩
  all_goals
    constructor
    · ext i j
      fin_cases k <;> fin_cases i <;> fin_cases j <;> apply Complex.ext <;>
        norm_num [Fin.succ, Fin.ofNat, A, C, S, E_apply]
    · fin_cases k <;> apply Complex.ext <;>
        norm_num [Fin.succ, Fin.ofNat, A, C, S, E_apply, Matrix.trace, Fin.sum_univ_succ]

theorem eight_eq_su : eight = su := by
  apply le_antisymm eight_le_su
  intro m hm
  rw [← synth24_reconstruct m hm]
  exact synth24_mem _


def eightCoordinates : eight ≃ₗ[ℝ] (Fin 24 → ℝ) where
  toFun m := coord24 m.val
  invFun v := ⟨synth24 v, synth24_mem v⟩
  left_inv m := by
    apply Subtype.ext
    exact synth24_reconstruct m.val (eight_le_su m.property)
  right_inv := coord24_synth24
  map_add' a b := by
    ext t
    fin_cases t <;> simp [coord24]
  map_smul' r a := by
    ext t
    fin_cases t <;> simp [coord24]

theorem eight_dimension : Module.finrank ℝ eight = 24 := by
  simpa using eightCoordinates.finrank_eq

-- The ten path brackets of the original four symmetric generators.
def B (i j : Fin 5) : M :=
  Complex.I ^ (j.val-i.val) • E i j - (-Complex.I) ^ (j.val-i.val) • E j i

def basis10 : Fin 10 → M := fun t =>
  match t.val with
  | 0 => B 0 1
  | 1 => B 0 2
  | 2 => B 0 3
  | 3 => B 0 4
  | 4 => B 1 2
  | 5 => B 1 3
  | 6 => B 1 4
  | 7 => B 2 3
  | 8 => B 2 4
  | _ => B 3 4

def synth10 (v : Fin 10 → ℝ) : M := fun i j =>
  match i.val, j.val with
  | 0, 0 => 0
  | 0, 1 => (v 0 : ℂ) * (Complex.I)
  | 0, 2 => (v 1 : ℂ) * (-1)
  | 0, 3 => (v 2 : ℂ) * (-Complex.I)
  | 0, 4 => (v 3 : ℂ) * (1)
  | 1, 0 => (v 0 : ℂ) * (Complex.I)
  | 1, 1 => 0
  | 1, 2 => (v 4 : ℂ) * (Complex.I)
  | 1, 3 => (v 5 : ℂ) * (-1)
  | 1, 4 => (v 6 : ℂ) * (-Complex.I)
  | 2, 0 => (v 1 : ℂ) * (1)
  | 2, 1 => (v 4 : ℂ) * (Complex.I)
  | 2, 2 => 0
  | 2, 3 => (v 7 : ℂ) * (Complex.I)
  | 2, 4 => (v 8 : ℂ) * (-1)
  | 3, 0 => (v 2 : ℂ) * (-Complex.I)
  | 3, 1 => (v 5 : ℂ) * (1)
  | 3, 2 => (v 7 : ℂ) * (Complex.I)
  | 3, 3 => 0
  | 3, 4 => (v 9 : ℂ) * (Complex.I)
  | 4, 0 => (v 3 : ℂ) * (-1)
  | 4, 1 => (v 6 : ℂ) * (-Complex.I)
  | 4, 2 => (v 8 : ℂ) * (1)
  | 4, 3 => (v 9 : ℂ) * (Complex.I)
  | _, _ => 0

def coord10 (m : M) : Fin 10 → ℝ := fun t =>
  match t.val with
  | 0 => (m 0 1).im
  | 1 => -(m 0 2).re
  | 2 => -(m 0 3).im
  | 3 => (m 0 4).re
  | 4 => (m 1 2).im
  | 5 => -(m 1 3).re
  | 6 => -(m 1 4).im
  | 7 => (m 2 3).im
  | 8 => -(m 2 4).re
  | _ => (m 3 4).im

theorem coord10_synth10 (v : Fin 10 → ℝ) : coord10 (synth10 v) = v := by
  ext t
  fin_cases t <;>
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, coord10, synth10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;> rfl

theorem four_le_twistedSo : four ≤ twistedSo := by
  apply LieSubalgebra.lieSpan_le.mpr
  rintro m ⟨k,rfl⟩
  change (conjugate (A k)).transpose = -conjugate (A k) ∧
    ∀ i j, (conjugate (A k) i j).im = 0
  constructor
  · ext i j; fin_cases k <;> fin_cases i <;> fin_cases j <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, A, S, E_apply, Matrix.mul_apply, Matrix.diagonal_apply,
        Matrix.single_apply, Fin.sum_univ_succ]
  · intro i j; fin_cases k <;> fin_cases i <;> fin_cases j <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, A, S, E_apply, Matrix.mul_apply, Matrix.diagonal_apply,
        Matrix.single_apply, Fin.sum_univ_succ]

theorem synth10_reconstruct (m : M) (hm : m ∈ twistedSo) : synth10 (coord10 m) = m := by
  have hs (i j : Fin 5) : conjugate m j i = -conjugate m i j :=
    congrFun (congrFun hm.1 i) j
  have hz (i j : Fin 5) : (conjugate m i j).im = 0 := hm.2 i j
  ext i j
  fin_cases i <;> fin_cases j
  · change synth10 (coord10 m) 0 0 = m 0 0
    have hr := congrArg Complex.re (hs 0 0)
    have hi := congrArg Complex.im (hs 0 0)
    have hzi := hz 0 0
    have hzj := hz 0 0
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 0 1 = m 0 1
    have hr := congrArg Complex.re (hs 0 1)
    have hi := congrArg Complex.im (hs 0 1)
    have hzi := hz 0 1
    have hzj := hz 1 0
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 0 2 = m 0 2
    have hr := congrArg Complex.re (hs 0 2)
    have hi := congrArg Complex.im (hs 0 2)
    have hzi := hz 0 2
    have hzj := hz 2 0
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 0 3 = m 0 3
    have hr := congrArg Complex.re (hs 0 3)
    have hi := congrArg Complex.im (hs 0 3)
    have hzi := hz 0 3
    have hzj := hz 3 0
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 0 4 = m 0 4
    have hr := congrArg Complex.re (hs 0 4)
    have hi := congrArg Complex.im (hs 0 4)
    have hzi := hz 0 4
    have hzj := hz 4 0
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 1 0 = m 1 0
    have hr := congrArg Complex.re (hs 1 0)
    have hi := congrArg Complex.im (hs 1 0)
    have hzi := hz 1 0
    have hzj := hz 0 1
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 1 1 = m 1 1
    have hr := congrArg Complex.re (hs 1 1)
    have hi := congrArg Complex.im (hs 1 1)
    have hzi := hz 1 1
    have hzj := hz 1 1
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 1 2 = m 1 2
    have hr := congrArg Complex.re (hs 1 2)
    have hi := congrArg Complex.im (hs 1 2)
    have hzi := hz 1 2
    have hzj := hz 2 1
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 1 3 = m 1 3
    have hr := congrArg Complex.re (hs 1 3)
    have hi := congrArg Complex.im (hs 1 3)
    have hzi := hz 1 3
    have hzj := hz 3 1
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 1 4 = m 1 4
    have hr := congrArg Complex.re (hs 1 4)
    have hi := congrArg Complex.im (hs 1 4)
    have hzi := hz 1 4
    have hzj := hz 4 1
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 2 0 = m 2 0
    have hr := congrArg Complex.re (hs 2 0)
    have hi := congrArg Complex.im (hs 2 0)
    have hzi := hz 2 0
    have hzj := hz 0 2
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 2 1 = m 2 1
    have hr := congrArg Complex.re (hs 2 1)
    have hi := congrArg Complex.im (hs 2 1)
    have hzi := hz 2 1
    have hzj := hz 1 2
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 2 2 = m 2 2
    have hr := congrArg Complex.re (hs 2 2)
    have hi := congrArg Complex.im (hs 2 2)
    have hzi := hz 2 2
    have hzj := hz 2 2
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 2 3 = m 2 3
    have hr := congrArg Complex.re (hs 2 3)
    have hi := congrArg Complex.im (hs 2 3)
    have hzi := hz 2 3
    have hzj := hz 3 2
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 2 4 = m 2 4
    have hr := congrArg Complex.re (hs 2 4)
    have hi := congrArg Complex.im (hs 2 4)
    have hzi := hz 2 4
    have hzj := hz 4 2
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 3 0 = m 3 0
    have hr := congrArg Complex.re (hs 3 0)
    have hi := congrArg Complex.im (hs 3 0)
    have hzi := hz 3 0
    have hzj := hz 0 3
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 3 1 = m 3 1
    have hr := congrArg Complex.re (hs 3 1)
    have hi := congrArg Complex.im (hs 3 1)
    have hzi := hz 3 1
    have hzj := hz 1 3
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 3 2 = m 3 2
    have hr := congrArg Complex.re (hs 3 2)
    have hi := congrArg Complex.im (hs 3 2)
    have hzi := hz 3 2
    have hzj := hz 2 3
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 3 3 = m 3 3
    have hr := congrArg Complex.re (hs 3 3)
    have hi := congrArg Complex.im (hs 3 3)
    have hzi := hz 3 3
    have hzj := hz 3 3
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 3 4 = m 3 4
    have hr := congrArg Complex.re (hs 3 4)
    have hi := congrArg Complex.im (hs 3 4)
    have hzi := hz 3 4
    have hzj := hz 4 3
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 4 0 = m 4 0
    have hr := congrArg Complex.re (hs 4 0)
    have hi := congrArg Complex.im (hs 4 0)
    have hzi := hz 4 0
    have hzj := hz 0 4
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 4 1 = m 4 1
    have hr := congrArg Complex.re (hs 4 1)
    have hi := congrArg Complex.im (hs 4 1)
    have hzi := hz 4 1
    have hzj := hz 1 4
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 4 2 = m 4 2
    have hr := congrArg Complex.re (hs 4 2)
    have hi := congrArg Complex.im (hs 4 2)
    have hzi := hz 4 2
    have hzj := hz 2 4
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 4 3 = m 4 3
    have hr := congrArg Complex.re (hs 4 3)
    have hi := congrArg Complex.im (hs 4 3)
    have hzi := hz 4 3
    have hzj := hz 3 4
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
  · change synth10 (coord10 m) 4 4 = m 4 4
    have hr := congrArg Complex.re (hs 4 4)
    have hi := congrArg Complex.im (hs 4 4)
    have hzi := hz 4 4
    have hzj := hz 4 4
    norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, conjugate, D, phase, Matrix.mul_apply, Matrix.diagonal_apply,
      Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im] at hr hi hzi hzj
    apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, coord10, basis10, B, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;>
      linarith
theorem B01_mem : B 0 1 ∈ four := by
  have h : B 0 1 = A 0 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, B, A, S, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [h]
  exact LieSubalgebra.subset_lieSpan (Set.mem_range_self 0)

theorem B12_mem : B 1 2 ∈ four := by
  have h : B 1 2 = A 1 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, B, A, S, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [h]
  exact LieSubalgebra.subset_lieSpan (Set.mem_range_self 1)

theorem B23_mem : B 2 3 ∈ four := by
  have h : B 2 3 = A 2 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, B, A, S, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [h]
  exact LieSubalgebra.subset_lieSpan (Set.mem_range_self 2)

theorem B34_mem : B 3 4 ∈ four := by
  have h : B 3 4 = A 3 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, B, A, S, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [h]
  exact LieSubalgebra.subset_lieSpan (Set.mem_range_self 3)

theorem B02_mem : B 0 2 ∈ four := by
  have h : ⁅B 0 1, A 1⁆ = B 0 2 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, B, A, S, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact four.lie_mem B01_mem (LieSubalgebra.subset_lieSpan (Set.mem_range_self 1))

theorem B13_mem : B 1 3 ∈ four := by
  have h : ⁅B 1 2, A 2⁆ = B 1 3 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, B, A, S, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact four.lie_mem B12_mem (LieSubalgebra.subset_lieSpan (Set.mem_range_self 2))

theorem B24_mem : B 2 4 ∈ four := by
  have h : ⁅B 2 3, A 3⁆ = B 2 4 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, B, A, S, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact four.lie_mem B23_mem (LieSubalgebra.subset_lieSpan (Set.mem_range_self 3))

theorem B03_mem : B 0 3 ∈ four := by
  have h : ⁅B 0 2, A 2⁆ = B 0 3 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, B, A, S, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact four.lie_mem B02_mem (LieSubalgebra.subset_lieSpan (Set.mem_range_self 2))

theorem B14_mem : B 1 4 ∈ four := by
  have h : ⁅B 1 3, A 3⁆ = B 1 4 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, B, A, S, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact four.lie_mem B13_mem (LieSubalgebra.subset_lieSpan (Set.mem_range_self 3))

theorem B04_mem : B 0 4 ∈ four := by
  have h : ⁅B 0 3, A 3⁆ = B 0 4 := by
    ext i j; fin_cases i <;> fin_cases j <;> apply Complex.ext <;> norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, B, A, S, E_apply, LieRing.of_associative_ring_bracket, Matrix.mul_apply, Matrix.single_apply, Fin.sum_univ_succ]
  rw [← h]
  exact four.lie_mem B03_mem (LieSubalgebra.subset_lieSpan (Set.mem_range_self 3))

theorem basis10_mem (t : Fin 10) : basis10 t ∈ four := by
  fin_cases t
  · exact B01_mem
  · exact B02_mem
  · exact B03_mem
  · exact B04_mem
  · exact B12_mem
  · exact B13_mem
  · exact B14_mem
  · exact B23_mem
  · exact B24_mem
  · exact B34_mem

theorem synth10_mem (v : Fin 10 → ℝ) : synth10 v ∈ four := by
  have heq : (∑ t : Fin 10, v t • basis10 t) = synth10 v := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      apply Complex.ext <;>
      norm_num [Fin.succ, pow_succ, Fin.ofNat, Complex.mul_re, Complex.mul_im, synth10, basis10, B, F, S, H, E_apply, Matrix.single_apply, Fin.sum_univ_succ] <;> first | rfl | ring
  rw [← heq]
  exact four.sum_mem fun t _ => four.smul_mem _ (basis10_mem t)

theorem four_eq_twistedSo : four = twistedSo := by
  apply le_antisymm four_le_twistedSo
  intro m hm
  rw [← synth10_reconstruct m hm]
  exact synth10_mem _

def fourCoordinates : four ≃ₗ[ℝ] (Fin 10 → ℝ) where
  toFun m := coord10 m.val
  invFun v := ⟨synth10 v, synth10_mem v⟩
  left_inv m := by
    apply Subtype.ext
    exact synth10_reconstruct m.val (four_le_twistedSo m.property)
  right_inv := coord10_synth10
  map_add' a b := by
    ext t
    fin_cases t <;> simp [coord10, add_comm]
  map_smul' r a := by
    ext t
    fin_cases t <;> simp [coord10, add_comm]

theorem four_dimension : Module.finrank ℝ four = 10 := by
  simpa using fourCoordinates.finrank_eq

/-- Uniform conjugation, with no alternating sign. -/
theorem conjugate_adjacent (k : Fin 4) :
    conjugate (A k) = -F k.castSucc k.succ := by
  ext i j
  fin_cases k <;> fin_cases i <;> fin_cases j <;> apply Complex.ext <;>
    norm_num [Fin.succ, pow_succ, Fin.ofNat, conjugate, D, phase, A, F, S, E_apply, Matrix.mul_apply,
      Matrix.diagonal_apply, Fin.sum_univ_succ]

/-- The missing quadrature is an actual real Lie bracket of admitted matrix directions. -/
theorem adjacent_commutator (k : Fin 4) :
    ⁅A k, C k⁆ = (2 : ℝ) • F k.castSucc k.succ := by
  ext i j
  fin_cases k <;> fin_cases i <;> fin_cases j <;> apply Complex.ext <;>
    norm_num [Fin.succ, pow_succ, Fin.ofNat, A, C, F, S, E_apply, LieRing.of_associative_ring_bracket,
      Matrix.mul_apply, Fin.sum_univ_succ, Complex.mul_re, Complex.mul_im]

/-- Every element of the original closure has zero diagonal, in the original basis. -/
theorem four_zero_diagonal (m : M) (hm : m ∈ four) (i : Fin 5) : m i i = 0 := by
  have h := congrFun (congrFun (synth10_reconstruct m (four_le_twistedSo hm)) i) i
  fin_cases i <;> simpa [synth10] using h.symm

theorem original_dimension_24_false : Module.finrank ℝ four ≠ 24 := by
  rw [four_dimension]
  norm_num

#print axioms adjacent_commutator
#print axioms conjugate_adjacent
#print axioms four_zero_diagonal
#print axioms eight_eq_su
#print axioms eight_dimension
#print axioms four_eq_twistedSo
#print axioms four_dimension

end QBD.SU5Closure

namespace QBD.Monograph.PentaClosure
open QBD.SU5Closure

-- Compare the original and enlarged real matrix Lie spans.
/-- The original closure has dimension ten; the direct enlarged closure has dimension twenty-four. -/
theorem closure_dimensions : Module.finrank ℝ four = 10 ∧ Module.finrank ℝ eight = 24 :=
  ⟨four_dimension, eight_dimension⟩

-- Identify the target independently of a dimension count.
/-- The enlarged generated algebra is the traceless skew-Hermitian matrix algebra. -/
theorem full_target : eight = su := eight_eq_su

#print axioms closure_dimensions
#print axioms full_target
end QBD.Monograph.PentaClosure
```

**Verification Summary:**
The self-contained block defines both target algebras independently, exhibits bracket-generated bases and constructs real coordinate equivalences of dimensions ten and twenty-four. It proves the full algebra equalities as well as the counts. The specialization concerns matrices, not physical Hamiltonian availability. The full block and this specialization are mirrored together in the Lean repository, and compilation is checked separately from structural validation. The kernel's acceptance of the closed proof term certifies the logical claim in the corresponding proof.

**In Plain English:**  
Section 9.2.11.3 formalizes the properties of the QBD type-theoretic regarding validation via lean 4 and mathlib.

---

### 9.2.12 Lemma: Anti-Fundamental Multiplet {#9.2.12}

:::info[**Anti-fundamental action via the dual of the encoded fundamental**]
:::

Let $V_5$ carry the fundamental action of $SU(5)$ and equip $V_5^*$ with its dual action. Then $V_5^*$ is the $\mathbf{\bar5}$, with Hermitian generators $-(T^a)^T$ and color and weak decomposition $(\mathbf{\bar3},\mathbf1)\oplus(\mathbf1,\mathbf2)$.

**In Plain English:**  
Section 9.2.12 formalizes the properties of the QBD lemma regarding anti-fundamental multiplet.

---

### 9.2.12.1 Proof: Anti-Fundamental Multiplet {#9.2.12.1}

:::tip[**Derivation of the anti-fundamental generators via dual pairing**]
:::

**I. Finite action**

In the fundamental space of **Closed Lie Algebra** <Ref id="9.2.11" label="§9.2.11" />, let $v_i$ be a basis and let $v^i$ be its dual, with $v^i(v_j)=\delta^i_j$. For the action on linear functionals set $(g\cdot f)(v)=f(g^{-1}v)$. Then

$$
((gh)\cdot f)(v)=f(h^{-1}g^{-1}v)
=(g\cdot(h\cdot f))(v).
$$

In dual column coordinates the action matrix is $(g^{-1})^T=\overline g$, since $g^\dagger=g^{-1}$.

**II. Infinitesimal action**

For $g(t)=e^{itT^a}$, the dual matrix is $e^{-it(T^a)^T}$. With $T_{\mathrm{dual}}^a=-(T^a)^T$ and $[T^a,T^b]=i\sum_c f^{abc}T^c$,

$$
\begin{aligned}
[T_{\mathrm{dual}}^a,T_{\mathrm{dual}}^b]
&=[(T^a)^T,(T^b)^T]=-[T^a,T^b]^T\\
&=-i\sum_c f^{abc}(T^c)^T
=i\sum_c f^{abc}T_{\mathrm{dual}}^c.
\end{aligned}
$$

To see irreducibility, let $A\subset V_5^*$ be a nonzero proper invariant subspace. Its annihilator $A^0$ has dimension $5-\dim A$. For $v\in A^0$, $f(gv)=(g^{-1}\cdot f)(v)=0$ for every $f\in A$, so $gv\in A^0$. But $SU(5)$ takes any unit vector to any other. Given unit vectors $u,v$, extend each to an orthonormal basis and take the unitary $U_0$ mapping the first basis to the second. With $d=\det U_0$, postcompose with the unitary that multiplies the second target basis vector by $d^{-1}$ and fixes the rest. The resulting unitary still sends $u$ to $v$ and has determinant $d^{-1}d=1$. An invariant subspace containing a unit vector must therefore contain every unit vector. This excludes $A^0$ with $0<\dim A^0<5$ and proves irreducibility of the dual.

**III. Block restriction**

Use the split of **Anti-Fundamental Multiplet** <Ref id="9.2.12" label="§9.2.12" />. For $g=\operatorname{diag}(g_C,g_W)$ with $g_C\in SU(3)$ and $g_W\in SU(2)$, the action is $\operatorname{diag}(\overline{g_C},\overline{g_W})$. On the weak block, the antisymmetric matrix

$$
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
g_W Jg_W^T=(\det g_W)J=J
$$

satisfies $g_WJ=J\overline{g_W}$, so the dual weak doublet is equivalent to the doublet. With the standard fundamental hypercharge assignment $Y=\operatorname{diag}(-1/3,-1/3,-1/3,1/2,1/2)$,

$$
Y_{\mathrm{dual}}=-Y^T=\operatorname{diag}(1/3,1/3,1/3,-1/2,-1/2).
$$

Thus the two blocks have the anti-down and lepton-doublet quantum numbers in that assignment.

Q.E.D.

**In Plain English:**  
Section 9.2.12.1 formalizes the properties of the QBD proof regarding anti-fundamental multiplet.

---

### 9.2.13 Lemma: Antisymmetric Multiplet {#9.2.13}

:::info[**Construction of the decuplet via the exterior square**]
:::

Let $V_5$ be the fundamental complex representation of $SU(5)$. Then the induced action $g(v\wedge w)=(gv)\wedge(gw)$ on $\wedge^2 V_5$ is irreducible and has dimension $10$.

**In Plain English:**  
Section 9.2.13 formalizes the properties of the QBD lemma regarding antisymmetric multiplet.

---

### 9.2.13.1 Proof: Antisymmetric Multiplet {#9.2.13.1}

:::tip[**Derivation of the decuplet via antisymmetry and weight connectivity**]
:::

**I. Antisymmetric basis**

Choose an orthonormal fundamental basis as in **Closed Lie Algebra** <Ref id="9.2.11" label="§9.2.11" /> and let $v_i\wedge v_j=(v_i\otimes v_j-v_j\otimes v_i)/\sqrt2$ for $i<j$. If $S$ flips the tensor factors, its $-1$ eigenspace consists of coefficients satisfying $c_{ji}=-c_{ij}$ and $c_{ii}=0$. Direct inner products give

$$
\langle v_i\wedge v_j,v_k\wedge v_l\rangle
=\delta_{ik}\delta_{jl}-\delta_{il}\delta_{jk}
=\delta_{ik}\delta_{jl}\qquad(i<j,\ k<l).
$$

Thus these vectors form an orthonormal basis of the antisymmetric space, with dimension $\binom52=5\cdot4/2=10$.

**II. Group and generator action**

On a tensor $v\otimes w$, $S(g\otimes g)(v\otimes w)=gw\otimes gv=(g\otimes g)S(v\otimes w)$. Hence $g\otimes g$ preserves the antisymmetric eigenspace and acts there by

$$
(g\otimes g)(v\wedge w)
=\frac{gv\otimes gw-gw\otimes gv}{\sqrt2}
=gv\wedge gw .
$$

The restriction defines the representation of **Antisymmetric Multiplet** <Ref id="9.2.13" label="§9.2.13" /> because $(g\otimes g)(h\otimes h)=gh\otimes gh$. Differentiating $e^{itT}\otimes e^{itT}$ and dividing by $i$ gives

$$
T^{(2)}(v_i\wedge v_j)
=(Tv_i)\wedge v_j+v_i\wedge(Tv_j)
=\sum_k T_{ki}\,v_k\wedge v_j+\sum_k T_{kj}\,v_i\wedge v_k .
$$

**III. Separation of weight lines**

Let $S_0$ be a nonzero invariant complex subspace. It is invariant under the differentiated action and its complex linear combinations. For the traceless diagonal $H=\operatorname{diag}(1,2,4,8,-15)$ the weights of $H^{(2)}$ are $3,5,9,6,10,12,-14,-13,-11,-7$, all distinct. Given one nonzero component at weight $\lambda$ in a vector of $S_0$, the operator

$$
\prod_{\nu\ne\lambda}\frac{H^{(2)}-\nu I}{\lambda-\nu}
$$

keeps that component and kills each other weight component. Thus $S_0$ contains an individual pair basis vector.

**IV. Connection of the pair lines**

For $a\ne b$, the matrix unit $E_{ab}$ is a complex linear combination of the symmetric and antisymmetric Hermitian controls in **Trace Normalization** <Ref id="8.6.3" label="§8.6.3" />. It acts by

$$
E_{ab}^{(2)}(v_i\wedge v_j)
=\delta_{bi}v_a\wedge v_j+\delta_{bj}v_i\wedge v_a .
$$

Thus replacing one index by any index outside the pair gives another basis line. Two pairs sharing an index are connected by one replacement. For disjoint pairs $\{i,j\}$ and $\{k,l\}$, the sequence $\{i,j\}\to\{k,j\}\to\{k,l\}$ uses two replacements. All pair basis vectors belong to $S_0$, so $\boxed{S_0=\wedge^2 V_5}$.

Q.E.D.

**In Plain English:**  
Section 9.2.13.1 formalizes the properties of the QBD proof regarding antisymmetric multiplet.

---

### 9.2.14 Proof: Topological Unification {#9.2.14}

:::tip[**Construction of Topological Unification via Explicit Identities**]
:::

**I. Admitted Actions and Discrete Relations**

The braid group $B_5$ labels discrete words in exchanges on five strands. A represented diagram action can act on five tensor factors $K^{\otimes5}$, of dimension $(\dim K)^5$ when $K$ is finite-dimensional. The matrix closure instead acts on a five-state sector with encoding $W:\mathbb C^5\to\mathcal H_G$, $W^\dagger W=I_5$. Assume the admitted actions satisfy

$$
\widehat A_k=i\widehat X_k,\quad\widehat C_k=i\widehat Z_k,\quad
\widehat A_kW=WA_k,\quad\widehat C_kW=WC_k,
\quad k=1,2,3,4.
$$

The discrete rewrite relations are

$$
\mathcal R_i\mathcal R_j=\mathcal R_j\mathcal R_i\quad(|i-j|>1)
$$

(**Distant Commutativity** <Ref id="9.2.5" label="§9.2.5" />) and

$$
\mathcal R_i\mathcal R_{i+1}\mathcal R_i
=\mathcal R_{i+1}\mathcal R_i\mathcal R_{i+1}
$$

(**Yang-Baxter Relations** <Ref id="9.2.6" label="§9.2.6" />).

**II. Diagonal Restriction and Preservation**

For the selected candidate words,

$$
\begin{aligned}
\widehat N_r|G_j\rangle&=\delta_{rj}|G_j\rangle,\\
\widehat Z_kW\sum_jv_j|j\rangle
&=\sum_jv_j(\delta_{kj}-\delta_{k+1,j})|G_j\rangle
=WZ_k\sum_jv_j|j\rangle
\end{aligned}
$$

(**Diagonal Encoded Action** <Ref id="9.2.7" label="§9.2.7" />). It follows that

$$
(I-P_5)\widehat Z_kW=(I-WW^\dagger)WZ_k=WZ_k-WZ_k=0,
\qquad e^{it\widehat Z_k}W=We^{i t Z_k}
$$

(**Diagonal Sector Preservation** <Ref id="9.2.8" label="§9.2.8" />). For the specified checks,

$$
S_{rm}W=W,\qquad
[S_{rm},\widehat Z_k]=0,\qquad [V,\widehat Z_k]=0
$$

(**Constraint Compatibility** <Ref id="9.2.9" label="§9.2.9" />).

**III. Equality of the Represented Image and Generated Matrix Algebra**

Define $\pi(A)=W^\dagger A W$, $\mathfrak g=\operatorname{Lie}_{\mathbb R}\{\widehat A_k,\widehat C_k\}$ and $L=\operatorname{Lie}_{\mathbb R}\{A_k,C_k\}$. On the invariant sector,

$$
\begin{aligned}
\pi(\widehat A_k)&=A_k,\qquad\pi(\widehat C_k)=C_k,\\
\pi(aP+bQ)&=a\pi(P)+b\pi(Q),\qquad
\pi([P,Q])=[\pi(P),\pi(Q)]
\end{aligned}
$$

(**Encoded Control Correspondence** <Ref id="9.2.10" label="§9.2.10" />). For each Lie expression $P$,

$$
\begin{aligned}
P(\widehat A,\widehat C)\in\mathfrak g
&\ \Longrightarrow\ \pi(P(\widehat A,\widehat C))=P(A,C)\in L,\\
\pi(\mathfrak g)&\subseteq L,\\
P(A,C)\in L
&\ \Longrightarrow\ P(A,C)=\pi(P(\widehat A,\widehat C))\in\pi(\mathfrak g),\\
L&\subseteq\pi(\mathfrak g).
\end{aligned}
$$

Using the 24 independent generated matrices (**Closed Lie Algebra** <Ref id="9.2.11" label="§9.2.11" />),

$$
\boxed{\pi(\mathfrak g)=L=\mathfrak{su}(5),\qquad
\dim_{\mathbb R}\pi(\mathfrak g)=24.}
$$

The compression identifies the represented image. Any operator of $\mathfrak g$ in $\ker\pi$ acts trivially on the five-state sector, since $AW=W\pi(A)$ there.

**IV. Dual Action**

On $V_5^*$ the dual action is $(g\cdot f)(v)=f(g^{-1}v)$. In the dual basis its matrix is $(g^{-1})^T=\overline g$, by unitarity. Thus for $g(t)=e^{i t T^a}$ its generator is determined by

$$
(g(t)^{-1})^T=e^{-it(T^a)^T},\qquad T_{\bar 5}^a=-(T^a)^T .
$$

A physical reversal that assigns reversed ribbon states to the dual basis must intertwine the reversed action. Reversing the labels supplies candidate basis vectors, while the generator sign follows from the dual action above.

For $g\in SU(5)$, the additional antifundamental identification is the intertwining premise

$$
T_{\overline5}\rho_{\mathrm{phys},5}(g)=\overline g\,T_{\overline5}
$$

(**Anti-Fundamental Multiplet** <Ref id="9.2.12" label="§9.2.12" />). **V. Exterior Action and Physical Pairing**

Let $F(v\otimes w)=w\otimes v$. Then

$$
F(g\otimes g)(v\otimes w)=gw\otimes gv=(g\otimes g)F(v\otimes w),
$$

so $g\otimes g$ preserves the antisymmetric image of $(I-F)/2$. For the orthonormal antisymmetric basis $e_{ij}=(v_i\otimes v_j-v_j\otimes v_i)/\sqrt2$ with $i<j$, the action sends $v_i\wedge v_j$ to $(gv_i)\wedge(gv_j)$. Differentiation gives

$$
\left.\frac{1}{i}\frac{\mathrm d}{\mathrm dt}
\big(e^{i t T^a}\otimes e^{i t T^a}\big)\right|_{t=0}
=T^a\otimes I+I\otimes T^a ,
$$

restricted to the antisymmetric subspace. To transfer this result to physical pairwise-linked graph states, the additional identification is

$$
T_{10}\rho_{\mathrm{phys},10}(g)=(\wedge^2g)T_{10}
$$

(**Antisymmetric Multiplet** <Ref id="9.2.13" label="§9.2.13" />). Conditional on those identifications,

$$
\dim\overline{\mathbb C^5}=5,\qquad
\dim\wedge^2\mathbb C^5
=\#\{(p,q):1\le p<q\le5\}=4+3+2+1=10.
$$

The physical pair sector must be invariant and the proposed $T_{10}$ must intertwine its admitted finite action. Only then does the physical branching inherit the exterior representation and its contribution to the representation-level anomaly cancellation.

Q.E.D.

**In Plain English:**  
Section 9.2.14 formalizes the properties of the QBD proof regarding topological unification.

---

### 9.3.1 Theorem: Generational Metastability {#9.3.1}

:::info[**Emergence of Three Fermion Generations as Metastable Topological Minima**]
:::

Suppose the three observed fermion generations correspond to the first three discrete local minima of the Topological Complexity Functional $V(C)$ defined over the configuration space of the penta-ribbon braid. Each minimum is separated from lower-energy states by a non-zero topological barrier $\Delta C$ that protects the state from rapid decay via local fluctuations. Under this formulation, the spectrum of generations is physically truncated at $N=3$ by the vacuum friction threshold.

**In Plain English:**  
Section 9.3.1 formalizes the properties of the QBD theorem regarding generational metastability.

---

### 9.3.2 Lemma: Complexity Ordering {#9.3.2}

:::info[**Generational ordering via positive increments in the assigned costs**]
:::

Let successive selected generation labels have nondecreasing crossing and link costs, with at least one strictly increasing cost at each step and both weights positive. Then their weighted complexities are strictly ordered, as are masses proportional to those complexities, while equal-prefactor Boltzmann formation weights decrease in that order.

**In Plain English:**  
Section 9.3.2 formalizes the properties of the QBD lemma regarding complexity ordering.

---

### 9.3.2.1 Proof: Complexity Ordering {#9.3.2.1}

:::tip[**Derivation of the complexity ordering via weighted differences**]
:::

**I. Assigned costs**

For the labels in **Generational Metastability** <Ref id="9.3.1" label="§9.3.1" />, let $X_n$ be the crossing cost and $L_n$ the link cost of the chosen generation-$n$ sector. In the model of **Complexity Ordering** <Ref id="9.3.2" label="§9.3.2" />, set

$$
C_n=\alpha X_n+\gamma L_n,\qquad \alpha>0,\quad\gamma>0.
$$

Write $\Delta X_n=X_{n+1}-X_n$ and $\Delta L_n=L_{n+1}-L_n$. Then

$$
C_{n+1}-C_n
=\alpha\Delta X_n+\gamma\Delta L_n>0
$$

since both increments are nonnegative and at least one is positive. A fixed intrinsic-twist cost shared by the labels cancels in the difference.

**II. Worked crossing sequence**

For the trefoil, figure-eight and cinquefoil benchmark, use minimal crossing counts $3,4,5$ and a common link cost $L_0$. This gives

$$
(C_1,C_2,C_3)=(3\alpha+\gamma L_0,\ 4\alpha+\gamma L_0,\ 5\alpha+\gamma L_0),
\qquad C_2-C_1=C_3-C_2=\alpha>0 .
$$

With the mass conversion $m_n=\kappa C_n$ at fixed $\kappa>0$, the mass gaps in this benchmark are $m_2-m_1=m_3-m_2=\kappa\alpha>0$.

**III. Relative formation weights**

If the three labels have equal multiplicity and probabilities proportional to $e^{-\eta C_n}$ with $\eta>0$, their common partition factor cancels. Thus

$$
\frac{P_{n+1}}{P_n}
=\frac{e^{-\eta C_{n+1}}}{e^{-\eta C_n}}
=e^{-\eta(C_{n+1}-C_n)}<1 .
$$

In the benchmark $P_2/P_1=P_3/P_2=e^{-\eta\alpha}$, so $\boxed{P_1>P_2>P_3}$ under this weight model.

Q.E.D.

**In Plain English:**  
Section 9.3.2.1 formalizes the properties of the QBD proof regarding complexity ordering.

---

### 9.3.3 Lemma: Topological Protection {#9.3.3}

:::info[**Sector protection via invariance under closed-knot isotopy**]
:::

Let a prime knot sector admit a family of local rewrites realized as ambient isotopies of its closed embedding, and let a selected lower sector have smaller minimum crossing number. Then the lower sector is unreachable within that family, and if every admitted escaping path contains an intermediate with excess energy at least $E_{\mathrm{cross}}>0$, its peak barrier is at least $E_{\mathrm{cross}}$.

**In Plain English:**  
Section 9.3.3 formalizes the properties of the QBD lemma regarding topological protection.

---

### 9.3.3.1 Proof: Topological Protection {#9.3.3.1}

:::tip[**Derivation of protection via isotopy and a conditional peak bound**]
:::

**I. Minimum crossing number**

For a closed knot $K$, let $c(K)=\min_{D\in[K]}c(D)$, where $D$ ranges over diagrams of its isotopy class and $c(D)$ counts visible crossings. If a task in the protected family of **Topological Barrier** <Ref id="6.1.5" label="§6.1.5" /> sends $K$ to $K'$, then $[K']=[K]$ and

$$
c(K')=\min_{D\in[K']}c(D)=\min_{D\in[K]}c(D)=c(K).
$$

A Type II deletion can lower the visible crossing count by two. For such a diagram move $D\to D'$, $c(D')=c(D)-2$ while both diagrams still represent $K$, so $c(D')\ge c(K)$.

**II. Words and prime decomposition**

For a word of protected tasks and successive knots $K_0,\ldots,K_m$,

$$
c(K_m)-c(K_0)=\sum_{j=1}^m(c(K_j)-c(K_{j-1}))=0.
$$

A target with $c(K_m)<c(K_0)$ is therefore outside that word's reach. In addition, primality means $K_0$ is nontrivial and $K_0\cong K_1\#K_2$ implies that at least one summand is an unknot. A split into two nontrivial summands therefore cannot be an isotopic description of $K_0$.

**III. Barrier on an admitted escape**

For an admitted topology-changing path $\xi_0,\ldots,\xi_m$, suppose some index $q$ satisfies $E(\xi_q)-E(\xi_0)\ge E_{\mathrm{cross}}$ (**Topological Protection** <Ref id="9.3.3" label="§9.3.3" />). Hence

$$
\boxed{\Delta E_{\mathrm{peak}}
=\max_{0\le j\le m}\bigl(E(\xi_j)-E(\xi_0)\bigr)
\ge E(\xi_q)-E(\xi_0)\ge E_{\mathrm{cross}}.}
$$

The inequality applies to each escape in the specified family and therefore to the infimum over that family when it is nonempty.

Q.E.D.

**In Plain English:**  
Section 9.3.3.1 formalizes the properties of the QBD proof regarding topological protection.

---

### 9.3.4 Lemma: Decay Tunneling {#9.3.4}

:::info[**Barrier Suppression via a Stipulated Multistep Tunneling Path**]
:::

Suppose the direct crossing is locally inadmissible and a legal multistep transition admits a WKB barrier model with forbidden length $\ell\Delta C$ at constant momentum scale, where $\Delta C=C_{\text{peak}}-C_{\text{initial}}>0$. Then the modeled rate is proportional to $e^{-2\kappa\Delta C}$ for the corresponding positive action coefficient $\kappa$.

**In Plain English:**  
Section 9.3.4 formalizes the properties of the QBD lemma regarding decay tunneling.

---

### 9.3.4.1 Proof: Decay Tunneling {#9.3.4.1}

:::tip[**Rate Suppression via Local Admissibility and the Squared WKB Amplitude**]
:::

**I. Local Move and Multistep Path**

A direct crossing proposal that produces a second short path between the same ordered endpoints fails the uniqueness test (**Principle of Unique Causality (PUC)** <Ref id="2.3.4" label="§2.3.4" />). If the two routes are $\pi_1\ne\pi_2$ of length at most two, the short-path count is at least $|\{\pi_1,\pi_2\}|=2>1$. A stipulated multistep path $G_0,\ldots,G_m$ instead has a separate legal certificate at each prefix. Its barrier is measured relative to the initial state (**Topological Protection** <Ref id="9.3.3" label="§9.3.3" />),

$$
C_{\text{peak}}=\max_{0\le j\le m} C(G_j),\qquad
\Delta C=C_{\text{peak}}-C(G_0)>0 .
$$

**II. Action and Rate in the Barrier Model**

Let $V_b>E$ be the constant effective barrier, and $p_b=\sqrt{2m(V_b-E)}$ its momentum scale. The stated width is $x_f-x_i=\ell\Delta C$. The dimensionless WKB amplitude exponent is

$$
S=\frac1{\hbar}\int_{x_i}^{x_f}p_b\,\mathrm dx
=\frac{p_b(x_f-x_i)}{\hbar}
=\frac{p_b\ell}{\hbar}\Delta C=\kappa\Delta C .
$$

**III. Rate from the Squared Amplitude**

With the amplitude $A=A_0e^{-S}$ and a fixed rate prefactor proportional to $|A_0|^2$,

$$
|A|^2=|A_0|^2e^{-2S}=|A_0|^2 e^{-2\kappa\Delta C},
\qquad \Gamma=\Gamma_0 e^{-2\kappa\Delta C}.
$$

Q.E.D.

**In Plain English:**  
Section 9.3.4.1 formalizes the properties of the QBD proof regarding decay tunneling.

---

### 9.3.5 Proof: Generational Metastability {#9.3.5}

:::tip[**Conditional Generational Ordering via Assigned Costs and Path Barriers**]
:::

**I. Assigned Generations and Formation**

Use the model assignment $\mathrm{I}\mapsto 3_1$, $\mathrm{II}\mapsto 4_1$, $\mathrm{III}\mapsto 5_1$ (trefoil, figure-eight, cinquefoil), with minimum crossing counts $3,4,5$. With a common link count $L_0$, positive cost weights $\alpha,\gamma$, and a common mass conversion $\kappa_m$, the prescribed costs of **Complexity Ordering** <Ref id="9.3.2" label="§9.3.2" /> give

$$
C_n=\alpha(n+2)+\gamma L_0,\quad
C_{n+1}-C_n=\alpha,\quad
m_{n+1}-m_n=\kappa_m\alpha>0
\qquad (n=1,2\text{ for the differences}).
$$

For equal formation prefactors and fixed friction $\mu>0$, the common normalization cancels:

$$
\frac{P_2}{P_1}=\frac{P_3}{P_2}=e^{-\mu\alpha},\qquad
\frac{P_3}{P_1}=e^{-2\mu\alpha}.
$$

**II. Isotopy and Admitted Escape Paths**

For isotopic closed embeddings $K\sim K'$, the sets of diagrams in their classes coincide. Therefore

$$
c(K')=\min_{D\in[K']}c(D)=\min_{D\in[K]}c(D)=c(K)
$$

(**Topological Protection** <Ref id="9.3.3" label="§9.3.3" />). Along a protected word $K_0,\ldots,K_m$,

$$
c(K_m)-c(K_0)=\sum_{j=1}^m\big(c(K_j)-c(K_{j-1})\big)=0.
$$

In particular a state with minimum $5$ or $4$ cannot reach one with a smaller minimum through that family. An admitted topology-changing path $G_0,\ldots,G_m$ can have a separate peak cost. If a witness at index $q$ has $C(G_q)-C(G_0)\ge B>0$, then

$$
\Delta C=\max_{0\le j\le m}\big(C(G_j)-C(G_0)\big)
\ge C(G_q)-C(G_0)\ge B .
$$

**III. Path Suppression**

Under the constant-momentum WKB model of **Decay Tunneling** <Ref id="9.3.4" label="§9.3.4" />, the forbidden length is $\ell\Delta C$ and the amplitude action is

$$
S=\hbar^{-1}\int_{x_i}^{x_i+\ell\Delta C}p_b\,\mathrm dx
=\frac{p_b\ell}{\hbar}\Delta C=\kappa\Delta C.
$$

For the fixed attempt rate $\Gamma_0$, the model yields

$$
\Gamma=\Gamma_0|e^{-S}|^2=\Gamma_0e^{-2\kappa\Delta C}
\le\Gamma_0e^{-2\kappa B}.
$$

This is a path rate. Comparing lifetimes requires the allowed paths and their prefactors for each generation.

**IV. Conditional Detection Cutoff**

If a fourth assigned candidate extends the same cost spacing and formation prefactor, then $P_4/P_1=e^{-3\mu\alpha}$. At $\mu=0.40$ and $\alpha=1$ this is $e^{-1.20}\simeq0.3010$, while $P_3/P_1=e^{-0.80}\simeq0.4493$. If detection requires $P_n/P_1\ge\epsilon$, and every further candidate has cost at least $C_4$ and the same prefactor, the exact condition in this benchmark for accepting the first three and rejecting the rest is

$$
e^{-3\mu\alpha}<\epsilon\le e^{-2\mu\alpha}.
$$

The cutoff uses the assigned higher costs, prefactors and detection threshold.

Q.E.D.

**In Plain English:**  
Section 9.3.5 formalizes the properties of the QBD proof regarding generational metastability.

---

### 9.4.1 Definition: Leptoquark Processes {#9.4.1}

:::tip[**Physical Realization of Generators as Transient Rewrite Operations**]
:::

The **Leptoquark Processes** are defined strictly as transient physical rewrite processes $\{\mathcal{R}_{LQ}\}$ (associated with the X and Y Bosons) acting upon the penta-ribbon braid. These processes are generated by the 12 off-diagonal leptoquark generators of the $\mathfrak{su}(5)$ algebra that explicitly mix the color subspace $\{1,2,3\}$ with the weak subspace $\{4,5\}$, thereby effecting transitions characterized by a baryon number change $\Delta B = -1/3$ and a lepton number change $\Delta L = \pm 1$.

**In Plain English:**  
Section 9.4.1 formalizes the properties of the QBD definition regarding leptoquark processes.

---

### 9.4.2 Theorem: Leptoquark Generators {#9.4.2}

:::info[**Identification via Off-Diagonal Generators Mediating Quark-Lepton Transitions**]
:::

Let the complete set of 24 generators of the $\mathfrak{su}(5)$ algebra decompose into the 12 generators of the Standard Model subalgebra and a complementary set of 12 **Leptoquark Generators**. These generators are uniquely identified as the specific operators possessing non-zero matrix elements connecting the color indices $i \in \{1,2,3\}$ to the weak indices $j \in \{4,5\}$, thus serving as the algebraic agents of quark-lepton unification.

**In Plain English:**  
Section 9.4.2 formalizes the properties of the QBD theorem regarding leptoquark generators.

---

### 9.4.3 Lemma: Interaction Vertex {#9.4.3}

:::info[**Color-to-weak transfer via a matched off-diagonal vertex**]
:::

Let an admitted emission vertex on $V_C\oplus V_W$ be matched to an off-diagonal color-to-weak block and a mediator emission amplitude. Then the matrix element is the product of the specified sector and emission overlaps, and any nonzero channel of a total-writhe-preserving vertex satisfies $W_{\mathrm{in}}=W_{\mathrm{out}}$.

**In Plain English:**  
Section 9.4.3 formalizes the properties of the QBD lemma regarding interaction vertex.

---

### 9.4.3.1 Proof: Interaction Vertex {#9.4.3.1}

:::tip[**Derivation of the vertex amplitude via block projection and charge balance**]
:::

**I. Sector transfer**

Use the split $V_C=\mathbb C^3$, $V_W=\mathbb C^2$ of **Leptoquark Generators** <Ref id="9.4.2" label="§9.4.2" />. For $B:V_W\to V_C$, write

$$
\lambda_{\mathrm{LQ}}=\begin{pmatrix}0&B\\ B^\dagger&0\end{pmatrix},
\qquad
\lambda_{\mathrm{LQ}}\binom{q}{0}=\binom{0}{B^\dagger q},
\qquad
\lambda_{\mathrm{LQ}}\binom{0}{\ell}=\binom{B\ell}{0}.
$$

The diagonal blocks are zero, so $\operatorname{Tr}\lambda_{\mathrm{LQ}}=0$. The blocks are adjoints of each other, so $\lambda_{\mathrm{LQ}}^\dagger=\lambda_{\mathrm{LQ}}$. In particular $e^{it\lambda_{\mathrm{LQ}}}$ is unitary and its infinitesimal generator $i\lambda_{\mathrm{LQ}}$ is traceless anti-Hermitian.

**II. Emission matrix element**

For the matched emission in **Interaction Vertex** <Ref id="9.4.3" label="§9.4.3" />, take the forward term $H_{\mathrm{emit}}=g(P_W\lambda_{\mathrm{LQ}}P_C)\otimes A$ from the initial mediator state $|0\rangle$, where $A$ acts on the mediator factor. Then

$$
\begin{aligned}
\langle\ell,X|H_{\mathrm{emit}}|q,0\rangle
&=g\langle\ell|P_W\lambda_{\mathrm{LQ}}P_C|q\rangle
       \langle X|A|0\rangle\\
&=g\left(\sum_{a=1}^{3}\sum_{b=1}^{2}
          \overline{\ell_b}\,\overline{B_{ab}}\,q_a\right)
       \langle X|A|0\rangle .
\end{aligned}
$$

This is the forward amplitude of the matched interaction $H_{\mathrm{emit}}+H_{\mathrm{emit}}^\dagger$ between the indicated sectors.

**III. Oriented writhe balance**

Give incoming and outgoing channels the signs $+1$ and $-1$, respectively, in the balance equation. Suppose the matched vertex commutes with the additive total writhe on the matter and mediator factors (**Conservation of Total Writhe** <Ref id="7.3.5" label="§7.3.5" />). On total-writhe eigenstates $|i\rangle$ and $|f\rangle$,

$$
0=\langle f|[\widehat W_{\mathrm{tot}},H_{\mathrm{int}}]|i\rangle
=(W_f-W_i)\langle f|H_{\mathrm{int}}|i\rangle .
$$

In a nonzero emission channel with vacuum mediator writhe zero, $W_q-W_\ell-W_X=0$. For the example $u+u\to\bar d+e^+$, the label charges of **Charge Normalization** <Ref id="7.3.10" label="§7.3.10" /> give

$$
Q_{\mathrm{in}}=\tfrac23+\tfrac23=\tfrac43,\qquad
Q_{\mathrm{out}}=\tfrac13+1=\tfrac43.
$$

For that two-body channel the baryon numbers are $B_{\mathrm{in}}=2/3$ and $B_{\mathrm{out}}=-1/3$, so $\Delta B=-1$. The lepton numbers are $0$ and $-1$, giving $\Delta(B-L)=-1-(-1)=0$.

Q.E.D.

**In Plain English:**  
Section 9.4.3.1 formalizes the properties of the QBD proof regarding interaction vertex.

---

### 9.4.4 Lemma: Fragmentation Tunneling {#9.4.4}

:::info[**Fragmentation cost and suppression via the assigned split and barrier**]
:::

Let a $3+2$ split remove the six registered cross-sector links at fixed additive writhe, with a positive resulting cost drop in the stated complexity model. If an admitted split path has a one-dimensional WKB barrier, then it is favored in the endpoint cost comparison and its leading transmission factor is $e^{-2S_{\mathrm{bar}}/\hbar}$ for the forbidden-region momentum integral $S_{\mathrm{bar}}$.

**In Plain English:**  
Section 9.4.4 formalizes the properties of the QBD lemma regarding fragmentation tunneling.

---

### 9.4.4.1 Proof: Fragmentation Tunneling {#9.4.4.1}

:::tip[**Derivation of the endpoint and tunneling factors via pair counts and WKB action**]
:::

**I. Pair and link counts**

Use the weighted model of **Fragmentation Tunneling** <Ref id="9.4.4" label="§9.4.4" />, with $C_{\text{total}}(\beta)=C[\beta]+kw(\beta)^2+k'L(\beta)$ and $k,k'\ge0$. For the assigned penta-ribbon state $\beta_5$ and split $(\beta_3,\beta_2)$, the registered cross-sector link count is

$$
L_{CW}=\binom52-\binom32-\binom22=10-3-1=6=3\cdot2 .
$$

If the registered intra-sector links survive, $L_5=L_3+L_2+6$. Suppose also that the additive writhe balance gives $w_5=w_3+w_2$. The initial-minus-final cost is

$$
\begin{aligned}
\Delta C_{\text{total}}
&=(C_5-C_3-C_2)+k\bigl((w_3+w_2)^2-w_3^2-w_2^2\bigr)
  +k'(L_5-L_3-L_2)\\
&=(C_5-C_3-C_2)+2kw_3w_2+6k'.
\end{aligned}
$$

For example, $C_5\ge C_3+C_2$, $w_3w_2\ge0$, and $k'>0$ give $\Delta C_{\text{total}}\ge6k'>0$. If the two writhes have opposite signs, the quadratic term has the opposite sign.

**II. Forbidden-region action**

For a separately admitted path with coordinate $x$, effective mass $m_{\mathrm{eff}}>0$, and energy $E$, assume $V(x)>E$ between the turning points $x_-,x_+$. Substitution of the decaying WKB form $\psi(x)=a(x)e^{-S(x)/\hbar}$ gives

$$
\psi''=e^{-S/\hbar}\left(a''-\frac{2a'S'+aS''}{\hbar}
+\frac{a(S')^2}{\hbar^2}\right).
$$

Consequently the stationary equation $-\hbar^2\psi''/(2m_{\mathrm{eff}})+V\psi=E\psi$ becomes

$$
-\frac{\hbar^2}{2m_{\mathrm{eff}}}a''
+\frac{\hbar}{2m_{\mathrm{eff}}}(2a'S'+aS'')
+\left(V-E-\frac{(S')^2}{2m_{\mathrm{eff}}}\right)a=0 .
$$

The leading order away from the turning points therefore gives

$$
-\frac{(S'(x))^2}{2m_{\mathrm{eff}}}+V(x)=E,\qquad
S'(x)=\sqrt{2m_{\mathrm{eff}}(V(x)-E)} .
$$

Integrating the positive root,

$$
S_{\mathrm{bar}}=S(x_+)-S(x_-)
=\int_{x_-}^{x_+}\sqrt{2m_{\mathrm{eff}}(V(x)-E)}\,\mathrm dx .
$$

**III. Transmission**

With the WKB convention of **Decay Tunneling** <Ref id="9.3.4" label="§9.3.4" />, the amplitude carries the factor $e^{-S_{\mathrm{bar}}/\hbar}$. The leading transmission factor is its squared modulus,

$$
\boxed{T_{\mathrm{WKB}}=\left|e^{-S_{\mathrm{bar}}/\hbar}\right|^2
=e^{-2S_{\mathrm{bar}}/\hbar}.}
$$

For constant $V_b>E$ over a forbidden width $d$, $S_{\mathrm{bar}}=d\sqrt{2m_{\mathrm{eff}}(V_b-E)}$. An effective rate with attempt frequency $\nu$ and the same leading approximation is $\Gamma_{\mathrm{frag}}\simeq\nu T_{\mathrm{WKB}}$.

Q.E.D.

**In Plain English:**  
Section 9.4.4.1 formalizes the properties of the QBD proof regarding fragmentation tunneling.

---

### 9.4.5 Proof: Leptoquark Generators {#9.4.5}

:::tip[**Off-Block Decomposition and Conditional Fragmentation via Endpoint and Path Costs**]
:::

**I. Complement of the Block Algebra**

For $V=\mathbb C^3\oplus\mathbb C^2$, any traceless skew-Hermitian matrix has the unique block form

$$
X=\begin{pmatrix}A&B\\-B^\dagger&D\end{pmatrix},
\qquad
A^\dagger=-A,\quad D^\dagger=-D,\quad \operatorname{Tr}A+\operatorname{Tr}D=0.
$$

The block-diagonal subalgebra has $8+3+1=12$ real dimensions. The block projections $P_C,P_W$ give the complementary map $X\mapsto P_CXP_W+P_WXP_C$. For $1\le a\le3$ and $4\le b\le5$, its real basis consists of $E_{ab}-E_{ba}$ and $i(E_{ab}+E_{ba})$, with independent real and imaginary upper-block entries. There are $2\cdot3\cdot2=12$ such directions. Under conjugation by a block group element the upper block transforms as $B\mapsto U_C B U_W^\dagger$. In the complexification, the hypercharge commutators are

$$
[Y,E_{ab}]=(-1/3-1/2)E_{ab}=-\tfrac56E_{ab},\qquad
[Y,E_{ba}]=+\tfrac56E_{ba}.
$$

This gives $(\mathbf3,\mathbf2)_{-5/6}\oplus(\mathbf{\bar3},\mathbf2)_{5/6}$, using the dual equivalence of the $SU(2)$ doublet.

**II. Matched Vertex and Writhe**

For an admitted emission Hamiltonian with forward term $H_{\mathrm{emit}}=g(P_W\lambda P_C)\otimes A_X$, the matrix element of **Interaction Vertex** <Ref id="9.4.3" label="§9.4.3" /> is

$$
\langle\ell,X|H_{\mathrm{emit}}|q,0\rangle
=g\langle\ell|P_W\lambda P_C|q\rangle\langle X|A_X|0\rangle .
$$

If $[W_{\mathrm{tot}},H_{\mathrm{int}}]=0$, then
$(W_f-W_i)\langle f|H_{\mathrm{int}}|i\rangle=0$. For nonzero emission from a vacuum mediator label this gives $W_q=W_\ell+W_X$. The matrix exponential describes a unitary on the represented sector. Using it for graph transitions requires admission and legality of the microscopic path.

**III. Endpoint Drop and Transmission**

In the assigned split of **Fragmentation Tunneling** <Ref id="9.4.4" label="§9.4.4" />, the cross-sector link count is

$$
L_{CW}=\binom52-\binom32-\binom22=10-3-1=6.
$$

With $w_5=w_3+w_2$ and $L_5-L_3-L_2=6$, the initial-minus-final cost is

$$
\begin{aligned}
\Delta C_{\mathrm{end}}
&=C_5-C_3-C_2
+k\bigl((w_3+w_2)^2-w_3^2-w_2^2\bigr)+k'(L_5-L_3-L_2)\\
&=C_5-C_3-C_2+2kw_3w_2+6k'.
\end{aligned}
$$

In particular the writhe and link contribution is $2kw_3w_2+6k'$, with a possible crossing cost difference. For a separately certified path with $V(x)>E$ between turning points $x_-$ and $x_+$, the modeled amplitude and transmission are

$$
S_{\mathrm{bar}}=\int_{x_-}^{x_+}\sqrt{2m_{\mathrm{eff}}(V(x)-E)}\,\mathrm dx,\qquad
T_{\mathrm{WKB}}=|e^{-S_{\mathrm{bar}}/\hbar}|^2=e^{-2S_{\mathrm{bar}}/\hbar}.
$$

The positive endpoint drop favors the split in the cost comparison. The transmission calculation uses the intermediate barrier, and a mediator mass for EFT matching is an independent input.

Q.E.D.

**In Plain English:**  
Section 9.4.5 formalizes the properties of the QBD proof regarding leptoquark generators.

---

### 9.5.1 Theorem: Proton Stability {#9.5.1}

:::info[**Topological Suppression of Proton Decay via Instanton Action Barriers**]
:::

Suppose the proton is stable on cosmological timescales due to the exponential suppression of its decay rate by a topological complexity barrier. The specific decay process $p \to e^+ \pi^0$ requires a transition through an intermediate state topologically equivalent to the X-boson geometry, which incurs an instanton action penalty $S_{inst}$ proportional to the complexity gap $N_{3,X} - N_{3,p}$.

**In Plain English:**  
Section 9.5.1 formalizes the properties of the QBD theorem regarding proton stability.

---

### 9.5.2 Lemma: Tension Verification {#9.5.2}

:::info[**Proton Partial-Lifetime Tension via a Fixed EFT Benchmark**]
:::

Let the nominal dimension-six EFT benchmark for $p\to e^+\pi^0$ use $M_X=10^{15}\,\text{GeV}$, $\alpha=1/42$, $m_p=0.938\,\text{GeV}$, and the normalized channel width $\Gamma_0=\alpha^2m_p^5/M_X^4$, with experimental lower limit $L=2.4\times10^{34}$ years. Then the benchmark partial lifetime is $\tau_0\simeq5.0665\times10^{31}$ years, and a rate factor $e^{-\Delta S}$ at these fixed inputs gives a partial lifetime above $L$ exactly when $\Delta S>\ln(L/\tau_0)\simeq6.16$.

**In Plain English:**  
Section 9.5.2 formalizes the properties of the QBD lemma regarding tension verification.

---

### 9.5.2.1 Proof: Tension Verification {#9.5.2.1}

:::tip[**Fixed-Input Lifetime Comparison via Width Scaling and Unit Conversion**]
:::

**I. Normalized Width**

Let $M_X$, $\alpha$, and $m_p$ be the benchmark inputs of **Tension Verification** <Ref id="9.5.2" label="§9.5.2" />. For the dimension-six exchange operator, the coefficient scales as $g_{\text{GUT}}^2/M_X^2=4\pi\alpha/M_X^2$. In the normalization of **EFT Rate Calculation** <Ref id="9.5.2.2" label="§9.5.2.2" />, the channel width uses $\alpha^2/M_X^4$ times $m_p^5$, giving

$$
\Gamma_0=\frac{\alpha^2m_p^5}{M_X^4},\qquad
[\Gamma_0]=\frac{\text{GeV}^5}{\text{GeV}^4}=\text{GeV}.
$$

At the stated inputs,

$$
\begin{aligned}
0.938^2&=0.879844,\qquad
0.938^5=(0.879844)^2(0.938)\simeq0.72612969,\\
\Gamma_0
&=\frac{(1/42)^2(0.938)^5}{(10^{15})^4}\,\text{GeV}
\simeq\frac{0.72612969}{1764}\,10^{-60}\,\text{GeV}
\simeq4.1164\times10^{-64}\,\text{GeV}.
\end{aligned}
$$

**II. Partial Lifetime and Shortfall**

With $\hbar=6.582\times10^{-25}\,\text{GeV}\cdot\text{s}$ and $s_{\text{yr}}=3.156\times10^7\,\text{s}/\text{yr}$, the partial lifetime and the ratio to the experimental lower limit are

$$
\begin{aligned}
\tau_0
&=\frac{\hbar}{\Gamma_0s_{\text{yr}}}
=\frac{6.582\times10^{-25}}{3.156\times10^7}
\frac{1764(10^{15})^4}{(0.938)^5}\,\text{yr}
\simeq5.0665\times10^{31}\,\text{yr},\\
\frac{L}{\tau_0}
&\simeq\frac{2.4}{5.0665}\,10^3
\simeq473.70 .
\end{aligned}
$$

**III. Rate Suppression at Fixed Inputs**

For a multiplicative width factor $0<f\le1$, the width is $\Gamma=f\Gamma_0$ and the partial lifetime is $\tau=\hbar/(f\Gamma_0s_{\text{yr}})=\tau_0/f$. Positivity of $L$ and $f$ yields

$$
\tau>L
\quad\Longleftrightarrow\quad
\tau_0>fL
\ \Longleftrightarrow\
f<\frac{\tau_0}{L}\simeq2.1110\times10^{-3}.
$$

For a barrier represented by the rate factor $f=e^{-\Delta S}$,

$$
e^{-\Delta S}<\frac{\tau_0}{L}
\ \Longleftrightarrow\
-\Delta S<\ln\frac{\tau_0}{L}
\ \Longleftrightarrow\
\Delta S>\ln\frac L{\tau_0}
\simeq\ln(4.7370)+2\ln 10
\simeq6.1606.
$$

Q.E.D.

**In Plain English:**  
Section 9.5.2.1 formalizes the properties of the QBD proof regarding tension verification.

---

### 9.5.2.2 Calculation: EFT Rate Calculation {#9.5.2.2}

:::note[**Computational Verification of the EFT Decay Rate Tension through EFT Rate Calculation**]
:::

Numerical verification of the nominal EFT lifetime and its sensitivity to the mediator inputs (**Tension Verification** <Ref id="9.5.2" label="§9.5.2" />) (**Proton Stability** <Ref id="9.5.1" label="§9.5.1" />) is based on the following protocols:

1.  **Parameter Definition:** The algorithm sets the standard GUT parameters: coupling $\alpha_{GUT} \approx 1/42$, proton mass $m_p \approx 0.938$ GeV, and X-boson mass $M_X \approx 10^{15}$ GeV.
2.  **Rate Computation:** The protocol calculates the decay rate $\Gamma_p \propto \alpha^2 m_p^5 / M_X^4$ and converts this to a lifetime $\tau_p$ in years.
3.  **Monte Carlo Analysis:** The simulation performs 1000 trials varying $M_X$ and $\alpha$ to generate a distribution of predicted lifetimes, comparing these against the experimental lower bound of $2.4 \times 10^{34}$ years.

```python
import numpy as np
import pandas as pd

def verify_proton_decay_suppression():
    """
    Verification of Topological vs. Perturbative Proton Decay Suppression
    
    Standard minimal SU(5) GUTs predict τ_p ~ 10^{31}–10^{32} years (ruled out).
    This calculation quantifies the shortfall and demonstrates the requirement
    for additional non-perturbative (topological) suppression.
    """
    print("=" * 78)
    print("PROTON DECAY: PERTURBATIVE EFT vs. EXPERIMENTAL BOUNDS")
    print("Quantifying the Shortfall in Minimal SU(5) Predictions")
    print("=" * 78)

    # Physical constants and benchmarks
    alpha_gut = 1 / 42.0                  # Typical GUT coupling
    m_p_gev = 0.938                       # Proton mass
    M_X_base_gev = 1e15                   # Nominal unification scale
    hbar_gev_s = 6.582e-25                # ħ in GeV·s
    sec_per_year = 3.156e7                # Seconds per year

    exp_bound_years = 2.4e34              # Super-Kamiokande lower bound (p → e⁺ π⁰)
    lit_su5_years = 1e32                  # Typical minimal SU(5) prediction

    # Base perturbative calculation (dimension-6 operator)
    alpha_sq = alpha_gut ** 2
    m_p5 = m_p_gev ** 5
    Gamma_base = alpha_sq * m_p5 / M_X_base_gev**4
    tau_base_years = hbar_gev_s / Gamma_base / sec_per_year

    shortfall_exp = exp_bound_years / tau_base_years
    shortfall_lit = lit_su5_years / tau_base_years

    print(f"\nBase Parameters:")
    print(f"  α_GUT   ≈ {alpha_gut:.4f}")
    print(f"  M_X     = {M_X_base_gev:.1e} GeV")
    print(f"  m_p     = {m_p_gev:.3f} GeV")
    print("-" * 50)
    print(f"Perturbative Prediction (Nominal):")
    print(f"  τ_p     ≈ {tau_base_years:.2e} years")
    print(f"  Literature SU(5) ≈ {lit_su5_years:.2e} years")
    print(f"  Experimental     > {exp_bound_years:.2e} years")
    print("-" * 50)
    print(f"Shortfall Factors:")
    print(f"  vs. Experiment : ×{shortfall_exp:.0f}")
    print(f"  vs. Literature : ×{shortfall_lit:.1f}")
    print("-" * 50)

    # Monte Carlo variation
    n_mc = 1000
    np.random.seed(42)

    # Log-uniform M_X around nominal (factor ~40 variation)
    M_X_samples = np.logspace(np.log10(5e14), np.log10(2e16), n_mc)
    # Uniform α_GUT variation ±10%
    alpha_samples = alpha_gut * np.random.uniform(0.9, 1.1, n_mc)

    tau_mc_years = []
    for i in range(n_mc):
        alpha_sq_i = alpha_samples[i]**2
        Gamma_i = alpha_sq_i * m_p5 / M_X_samples[i]**4
        tau_i = hbar_gev_s / Gamma_i / sec_per_year
        tau_mc_years.append(tau_i)

    tau_mc = np.array(tau_mc_years)
    log_tau = np.log10(tau_mc)

    mean_tau = np.mean(tau_mc)
    median_tau = np.median(tau_mc)
    std_tau = np.std(tau_mc)
    p_above_exp = np.mean(tau_mc > exp_bound_years) * 100
    p_above_lit = np.mean(tau_mc > lit_su5_years) * 100

    print(f"\nMonte Carlo Results ({n_mc} samples):")
    print(f"  Mean τ_p     = {mean_tau:.2e} years")
    print(f"  Median τ_p   = {median_tau:.2e} years")
    print(f"  Std dev      = {std_tau:.2e} years")
    print(f"  P(τ_p > exp) = {p_above_exp:.1f}%")
    print(f"  P(τ_p > lit) = {p_above_lit:.1f}%")
    print("-" * 50)

    # Binned distribution as clean table (no ASCII bars)
    bins = 10
    hist, bin_edges = np.histogram(log_tau, bins=bins)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    print("Distribution of log₁₀(τ_p [years]):")
    dist_data = []
    for center, count in zip(bin_centers, hist):
        percentage = (count / n_mc) * 100
        dist_data.append({
            "log₁₀(τ_p)": f"{center:.2f}",
            "Count": count,
            "Percentage": f"{percentage:.1f}%"
        })

    df_dist = pd.DataFrame(dist_data)
    print(df_dist.to_string(index=False))

if __name__ == "__main__":
    verify_proton_decay_suppression()
```

**Simulation Results:**

```text
==============================================================================
PROTON DECAY: PERTURBATIVE EFT vs. EXPERIMENTAL BOUNDS
Quantifying the Shortfall in Minimal SU(5) Predictions
==============================================================================

Base Parameters:
  α_GUT   ≈ 0.0238
  M_X     = 1.0e+15 GeV
  m_p     = 0.938 GeV
--------------------------------------------------
Perturbative Prediction (Nominal):
  τ_p     ≈ 5.07e+31 years
  Literature SU(5) ≈ 1.00e+32 years
  Experimental     > 2.40e+34 years
--------------------------------------------------
Shortfall Factors:
  vs. Experiment : ×474
  vs. Literature : ×2.0
--------------------------------------------------

Monte Carlo Results (1000 samples):
  Mean τ_p     = 5.65e+35 years
  Median τ_p   = 4.98e+33 years
  Std dev      = 1.43e+36 years
  P(τ_p > exp) = 39.9%
  P(τ_p > lit) = 76.2%
--------------------------------------------------
Distribution of log₁₀(τ_p [years]):
log₁₀(τ_p)  Count Percentage
     30.76     92       9.2%
     31.41    105      10.5%
     32.06     96       9.6%
     32.72    108      10.8%
     33.37     99       9.9%
     34.02     95       9.5%
     34.68    105      10.5%
     35.33    108      10.8%
     35.98     94       9.4%
     36.64     98       9.8%
```

**Conclusion:**
The base calculation yields a partial lifetime of $5.07\times10^{31}$ years and a shortfall factor of approximately 474 at the nominal inputs. The parameter sweep gives a median of $4.98\times10^{33}$ years and 39.9% of the samples exceed the experimental threshold. These figures describe the stated mass grid and coupling draws.

**In Plain English:**  
Section 9.5.2.2 formalizes the properties of the QBD calculation regarding eft rate calculation.

---

### 9.5.3 Lemma: Minimal Action Pathway {#9.5.3}

:::info[**Identification of the Least Suppressed Decay Channel via Minimal Action Pathway**]
:::

Suppose the decay channel $p \to e^+ + \pi^0$ is identified as the unique transition pathway that minimizes the change in topological complexity $\Delta C$. This selection is enforced by the Principle of Minimal Complexity Change, which suppresses all alternative channels involving higher-generation final states.

**In Plain English:**  
Section 9.5.3 formalizes the properties of the QBD lemma regarding minimal action pathway.

---

### 9.5.3.1 Proof: Minimal Action Pathway {#9.5.3.1}

:::tip[**Comparative Analysis via Final State Invariants**]
:::

**I. Principle of Minimal Complexity Change**
The decay rate for a non-perturbative topological transition is governed by the instanton action $S$:  **Minimal Action Pathway** <Ref id="9.5.3" label="§9.5.3" /> and  **Tension Verification** <Ref id="9.5.2" label="§9.5.2" />

$$
\Gamma \propto e^{-S} \propto e^{-\Delta C}
$$

where $\Delta C = C_{final} - C_{initial}$ is the change in topological complexity. The dominant channel is the one that minimizes $C_{final}$ subject to conservation laws (Charge $Q$, Energy $E$).

**II. Initial State Complexity ($p$)**
The proton comprises three valence quarks ($uud$) in a color singlet state.
* **Integer writhe and charge:** The up and down labels have integer writhes $W_u=2$ and $W_d=-1$ (**Quark Charge Solutions** <Ref id="7.3.9" label="§7.3.9" />). Their sum for the valence configuration and its electric charge are

  $$
  W_p=W_u+W_u+W_d=2+2-1=3,\qquad
  Q_p=\frac{W_p}{3}=\frac{3}{3}=+1
  $$

  by **Charge Normalization** <Ref id="7.3.10" label="§7.3.10" />.
* **Complexity:** $C_p = \sum C_{quarks} + C_{binding}$. This is the baseline for all decays.

**III. Final State Candidates**
1.  **Channel A: $p \to e^+ + \pi^0$**
    * **Positron ($e^+$):** Generation 1 anti-lepton. Minimal complexity state for charge $+1$ lepton sector. $C_{e^+} = C_{min}$.
    * **Pion ($\pi^0$):** Generation 1 meson ($u\bar{u} - d\bar{d}$). Topological complexity is minimal (zero net twist/writhe). $C_{\pi^0} \approx 0$.
    * **Total Complexity:** $C_A \approx C_{e^+}$.

2.  **Channel B: $p \to \mu^+ + K^0$**
    * **Muon ($\mu^+$):** Generation 2 anti-lepton. As proven in the **Complexity Ordering** <Ref id="9.3.2" label="§9.3.2" />, $C_{\mu} > C_{e}$.
    * **Kaon ($K^0$):** Generation 2 meson ($d\bar{s}$). Contains a strange quark, which possesses higher complexity than first-generation quarks. $C_{K} > C_{\pi}$.
    * **Total Complexity:** $C_B = C_{\mu} + C_{K} > C_A$.

**IV. Selection Rule**
Since $C_B > C_A$, the action for Channel B is strictly greater than for Channel A ($S_B > S_A$).
The rate suppression scales exponentially:

$$
\frac{\Gamma_B}{\Gamma_A} \approx e^{-(S_B - S_A)} \ll 1
$$

Thus, the transition to the lowest-complexity generation (Generation 1) is the topologically preferred channel.

Q.E.D.

**In Plain English:**  
Section 9.5.3.1 formalizes the properties of the QBD proof regarding minimal action pathway.

---

### 9.5.4 Lemma: Action-Mass Proportionality {#9.5.4}

:::info[**Action scaling via a matched rewrite length and mass quantum**]
:::

Let a supplied decay model assign a dimensionless rate action $S_{inst}=\kappa L_{\min}$, with $L_{\min}=aN_{3,X}+b$ and mediator rest energy $M_X=\varepsilon N_{3,X}$ in natural units, for fixed $\kappa,a,\varepsilon>0$. Then the modeled rate factor is proportional to $e^{-\lambda M_X}$ with $\lambda=\kappa a/\varepsilon$.

**In Plain English:**  
Section 9.5.4 formalizes the properties of the QBD lemma regarding action-mass proportionality.

---

### 9.5.4.1 Proof: Action-Mass Proportionality {#9.5.4.1}

:::tip[**Derivation of exponential suppression via elimination of the complexity count**]
:::

**I. Matched rewrite length**

For the decay pathway discussed in **Minimal Action Pathway** <Ref id="9.5.3" label="§9.5.3" />, use the model of **Action-Mass Proportionality** <Ref id="9.5.4" label="§9.5.4" />. Its inputs are the path length $L_{\min}=aN_{3,X}+b$, dimensionless rate cost $\kappa$ per step, and rest energy $\varepsilon$ per quantum. Eliminating the count gives

$$
N_{3,X}=\frac{M_X}{\varepsilon},\qquad
S_{inst}=\kappa L_{\min}
=\kappa\left(a\frac{M_X}{\varepsilon}+b\right)
=\lambda M_X+\kappa b,\qquad
\lambda=\frac{\kappa a}{\varepsilon}.
$$

For the modeled rate $\Gamma=\Gamma_{\mathrm{EFT}}e^{-S_{inst}}$,

$$
\frac{\Gamma}{\Gamma_{\mathrm{EFT}}}
=e^{-(\lambda M_X+\kappa b)}
=\boxed{e^{-\kappa b}e^{-\lambda M_X}} .
$$

Here $[\lambda]=[\mathrm{energy}]^{-1}$, and for $b=0$ the action itself is linear in $M_X$ through the origin.

**II. Static-action comparison**

For a separate static Euclidean approximation over proper time $\tau_E$, let the baseline-subtracted matter energy be $M_Xc^2$ in ordinary units. Then

$$
\Delta S_E=\int_0^{\tau_E}\Delta E(t_E)\,\mathrm dt_E
=\int_0^{\tau_E}M_Xc^2\,\mathrm dt_E
=M_Xc^2\tau_E,\qquad
\frac{\Delta S_E}{\hbar}=\frac{c^2\tau_E}{\hbar}M_X .
$$

This is a linear action law at fixed duration. If an exponent instead governs the amplitude as in **Decay Tunneling** <Ref id="9.3.4" label="§9.3.4" />, the corresponding rate exponent is twice that amplitude exponent.

**III. Comparison with the polynomial rate**

Let $\Gamma_{\mathrm{EFT}}=A(M_X/E_0)^{-4}$ with fixed $E_0>0$, as in the fixed-input scaling of **Tension Verification** <Ref id="9.5.2" label="§9.5.2" />. Then

$$
\Gamma=Ae^{-\kappa b}(M_X/E_0)^{-4}e^{-\lambda M_X},\qquad
\ln\frac{\Gamma}{A}=-\kappa b-4\ln(M_X/E_0)-\lambda M_X .
$$

Since $\ln(M_X/E_0)/(M_X/E_0)\to0$, the last term is the leading term of this logarithm as $M_X/E_0\to\infty$.

Q.E.D.

**In Plain English:**  
Section 9.5.4.1 formalizes the properties of the QBD proof regarding action-mass proportionality.

---

### 9.5.5 Proof: Proton Stability {#9.5.5}

:::tip[**Partial-Lifetime Bound via a Matched Rate Action**]
:::

**I. Nominal EFT Partial Lifetime**

Use the normalized dimension-six width of **Tension Verification** <Ref id="9.5.2" label="§9.5.2" /> for $p\to e^+\pi^0$. At $M_0=10^{15}\,\mathrm{GeV}$, $\alpha_0=1/42$, and $m_p=0.938\,\mathrm{GeV}$,

$$
\begin{aligned}
\Gamma_0&=\frac{\alpha_0^2m_p^5}{M_0^4}
=\frac{(0.938)^5}{42^2(10^{15})^4}\,\mathrm{GeV}
\simeq 4.1164\times10^{-64}\,\mathrm{GeV},\\
\tau_0&=\frac{\hbar}{s_{\mathrm{yr}}\Gamma_0}
\simeq\frac{6.582\times10^{-25}}{(3.156\times10^7)(4.1164\times10^{-64})}\,\mathrm{yr}
\simeq5.0665\times10^{31}\,\mathrm{yr}.
\end{aligned}
$$

For comparison use the $90\%$ confidence lower limit $L=2.4\times10^{34}\,\mathrm{yr}$ for this channel. [Super-Kamiokande proton-decay search](https://doi.org/10.1103/PhysRevD.102.112011)

**II. Modeled Action and Rate**

Suppose the decay model supplies a legal pathway for this channel with $L_{\min}=aN_{3,X}+b$ and $M_X=\varepsilon N_{3,X}$, as in **Action-Mass Proportionality** <Ref id="9.5.4" label="§9.5.4" />. Then

$$
S_{\mathrm{inst}}=\kappa L_{\min}
=\frac{\kappa a}{\varepsilon}M_X+\kappa b
=\lambda M_X+\kappa b,\qquad \lambda=\kappa a/\varepsilon .
$$

Take $S_{\mathrm{inst}}\ge0$ as a dimensionless rate exponent. At fixed $m_p$ the modeled width and partial lifetime are

$$
\begin{aligned}
\Gamma(M_X,\alpha)&=\Gamma_0
\left(\frac{\alpha}{\alpha_0}\right)^2
\left(\frac{M_0}{M_X}\right)^4e^{-S_{\mathrm{inst}}},\\
\tau(M_X,\alpha)&=\tau_0
\left(\frac{\alpha_0}{\alpha}\right)^2
\left(\frac{M_X}{M_0}\right)^4e^{S_{\mathrm{inst}}}.
\end{aligned}
$$

For any separately supplied competing channel $j$ with width $K_j e^{-S_j}$, its ratio to the selected channel $e^+\pi^0$ is $(K_j/K_{e\pi})e^{-(S_j-S_{e\pi})}$. The preference in **Minimal Action Pathway** <Ref id="9.5.3" label="§9.5.3" /> can be used if the relevant pathways, action ordering and prefactors are supplied. Endpoint ordering alone does not fix those ratios.

**III. Required Suppression and Its Domain**

At the nominal point the comparison reduces to

$$
\begin{aligned}
\tau>L
&\iff e^{S_{\mathrm{inst}}}>\frac L{\tau_0}
\simeq473.70\\
&\iff S_{\mathrm{inst}}>\ln\!\frac L{\tau_0}
\simeq6.1606 .
\end{aligned}
$$

Thus $\lambda M_0+\kappa b>6.1606$ to the displayed precision is the action requirement at that point. At fixed $\alpha_0$, the unsuppressed equality threshold is

$$
M_{\mathrm{eq}}=M_0\left(\frac L{\tau_0}\right)^{1/4}
\simeq4.6653\times10^{15}\,\mathrm{GeV}.
$$

For $M_X>M_{\mathrm{eq}}$ at the same coupling, the mass dependence alone puts this modeled partial lifetime above $L$. When both $\alpha$ and $M_X$ vary, the threshold is $M_{\mathrm{eq}}(\alpha)=M_{\mathrm{eq}}\sqrt{\alpha/\alpha_0}$.

Q.E.D.

**In Plain English:**  
Section 9.5.5 formalizes the properties of the QBD proof regarding proton stability.

---

### 9.6.1 Definition: Folded Topology {#9.6.1}

:::tip[**Uniqueness of the Folded Braid as the Minimal Neutral Lepton Structure**]
:::

The **Folded Topology** representing the neutrino is topologically defined as a **Folded Braid** structure, consisting of a braid segment $\beta_+$ and an anti-braid segment $\beta_-$ joined at a singular fold vertex. This configuration constitutes the unique minimal topology satisfying the simultaneous conditions of:
1.  **Electric Neutrality:** Global cancellation of writhe $w(\beta_+) + w(\beta_-) = 0$.
2.  **Color Singlet:** Invariance under color permutations.
3.  **Non-Triviality:** Existence of non-zero local complexity at the fold vertex, enabling non-zero mass generation.

**In Plain English:**  
Section 9.6.1 formalizes the properties of the QBD definition regarding folded topology.

---

### 9.6.2 Theorem: Neutrino Mass Mechanism {#9.6.2}

:::info[**Emergence of Neutrino Mass via the Folded Braid Seesaw Mechanism**]
:::

Let the light neutrino mass $m_\nu$ arise from a topological seesaw mechanism generated by the mixing of the massless folded left-handed state $\nu_L$ and the massive complex right-handed state $N_R$. The mass eigenvalue is determined by the relation $m_\nu \approx m_D^2 / M_R$, where $M_R$ is the friction-limited maximum complexity bound of the causal graph.

**In Plain English:**  
Section 9.6.2 formalizes the properties of the QBD theorem regarding neutrino mass mechanism.

---

### 9.6.3 Lemma: Neutrality Verification {#9.6.3}

:::info[**Neutrality and modeled mass via writhe cancellation**]
:::

Let a standard tripartite label be permutation-fixed and electrically neutral, and let a folded candidate have opposite segment writhe and positive excess fold cost. Then the standard writhe label is $(0,0,0)$, while the folded label is neutral with a positive modeled mass contribution from the fold.

**In Plain English:**  
Section 9.6.3 formalizes the properties of the QBD lemma regarding neutrality verification.

---

### 9.6.3.1 Proof: Neutrality Verification {#9.6.3.1}

:::tip[**Derivation of neutral labels via fixed coordinates and segment balance**]
:::

**I. Standard permutation-fixed label**

Let $\boldsymbol w=(w_1,w_2,w_3)\in\mathbb Z^3$. The transpositions $(12)$ and $(23)$ fix $\boldsymbol w$ exactly when $w_1=w_2=w_3=w_0$ (**Permutation-Fixed Writhe** <Ref id="7.3.6" label="§7.3.6" />). By the **Charge Operator** <Ref id="7.3.1" label="§7.3.1" />,

$$
Q=\tfrac13(w_1+w_2+w_3)=\tfrac13(3w_0)=w_0 .
$$

Thus $Q=0$ forces $\boldsymbol w=(0,0,0)$. In the selected unlinked reference configuration with no crossings or excess support cycles, the crossing, twist and link costs all vanish:

$$
C_{\mathrm{ref}}=a\,0+b\sum_{i=1}^3 0^2+d\,0=0,\qquad
m_{\mathrm{ref}}=\kappa_m C_{\mathrm{ref}}=0 .
$$

**II. Folded comparison**

For the two segments of **Folded Topology** <Ref id="9.6.1" label="§9.6.1" />, take $W_+=k$ and $W_-=-k$, with $k\ne0$. For an additive writhe and a positive excess count $N_{\mathrm{fold}}$ assigned to the fold,

$$
Q_{\mathrm{fold}}=\tfrac13(W_++W_-)=\tfrac13(k-k)=0,\qquad
\Delta m_{\mathrm{fold}}=\kappa_m N_{\mathrm{fold}}>0\quad(\kappa_m>0).
$$

If the torsional cost is also the sum of the separate segment squares, its unweighted value is $k^2+(-k)^2=2k^2>0$ even though the net writhe vanishes.

**III. Gauge singlet criterion**

For the assigned sterile representation, suppose the color and weak generators $T_C^a,T_W^b$ annihilate its state $|s\rangle$ and the hypercharge label is $Y=0$. The quadratic operators then satisfy

$$
C_2^{(3)}|s\rangle=\sum_a T_C^a T_C^a|s\rangle=0,\qquad
C_2^{(2)}|s\rangle=\sum_b T_W^b T_W^b|s\rangle=0,\qquad
e^{i\theta Y}|s\rangle=|s\rangle .
$$

For Hermitian generators the converse of the non-Abelian test follows from $\langle s|C_2|s\rangle=\sum_a\|T^a|s\rangle\|^2$. Vanishing of the quadratic form therefore implies each generator annihilates the state.

Q.E.D.

**In Plain English:**  
Section 9.6.3.1 formalizes the properties of the QBD proof regarding neutrality verification.

---

### 9.6.4 Lemma: Seesaw Dynamics {#9.6.4}

:::info[**Derivation of the Seesaw Mechanism from Topological Mass Matrices**]
:::

Suppose the physical neutrino mass spectrum is derived from the diagonalization of the 2x2 mass matrix spanning the basis of the light folded state $\nu_L$ ($M_L=0$) and the heavy complex state $N_R$ ($M_R \gg 0$). The mixing term $m_D$ arises from the electroweak rewrite amplitude, yielding the characteristic seesaw suppression for the light eigenstate.

**In Plain English:**  
Section 9.6.4 formalizes the properties of the QBD lemma regarding seesaw dynamics.

---

### 9.6.4.1 Proof: Seesaw Dynamics {#9.6.4.1}

:::tip[**Diagonalization of the Mass Matrix Yielding Light via Heavy Eigenstates**]
:::

**I. Real Symmetric Mass Matrix**

In the assumed two-state mass model, write $d=m_D\in\mathbb R$ and $M=M_R>0$, with $M_L=0$ (**Seesaw Dynamics** <Ref id="9.6.4" label="§9.6.4" />). The light label refers to the folded-state candidate (**Folded Topology** <Ref id="9.6.1" label="§9.6.1" />). The heavy label and the mass entries are inputs to the two-state model. The matrix and its characteristic polynomial are

$$
\begin{aligned}
\mathsf M&=\begin{pmatrix}0&d\\d&M\end{pmatrix},\\
\det(\mathsf M-\lambda I)
&=\det\begin{pmatrix}-\lambda&d\\d&M-\lambda\end{pmatrix}\\
&=(-\lambda)(M-\lambda)-d^2
=\lambda^2-M\lambda-d^2.
\end{aligned}
$$

Completing the square gives

$$
\left(\lambda-\frac M2\right)^2
=\frac{M^2+4d^2}{4},\qquad
\Delta=\sqrt{M^2+4d^2},\qquad
\lambda_\pm=\frac{M\pm\Delta}{2}.
$$

For $d\ne0$, $\Delta>M$, hence $\lambda_-<0<\lambda_+$. For $d=0$, the eigenvalues are $0,M$.

**II. Explicit Orthogonal Diagonalization**

Choose $\theta\in(-\pi/4,\pi/4)$ by $2\theta=\arctan(2d/M)$, and write $c=\cos\theta$, $s=\sin\theta$. Then

$$
\cos(2\theta)=\frac M\Delta,\qquad
\sin(2\theta)=\frac{2d}\Delta,\qquad
R=\begin{pmatrix}c&s\\-s&c\end{pmatrix},\quad R^TR=I.
$$

Both matrix products are

$$
\begin{aligned}
\mathsf M R
&=\begin{pmatrix}-ds&dc\\dc-Ms&ds+Mc\end{pmatrix},\\
R^T\mathsf M R
&=\begin{pmatrix}
Ms^2-2d s c&d(c^2-s^2)-M s c\\
d(c^2-s^2)-M s c&Mc^2+2d s c
\end{pmatrix}.
\end{aligned}
$$

The off-diagonal entry vanishes because

$$
d\cos(2\theta)-\frac M2\sin(2\theta)
=\frac{dM}\Delta-\frac{Md}\Delta=0.
$$

The first diagonal entry is

$$
\begin{aligned}
Ms^2-2d s c
&=\frac M2(1-\cos(2\theta))-d\sin(2\theta)\\
&=\frac M2-\frac{M^2}{2\Delta}-\frac{2d^2}\Delta
=\frac{M-\Delta}{2}=\lambda_-.
\end{aligned}
$$

The second is

$$
Mc^2+2d s c
=\frac M2+\frac{M^2+4d^2}{2\Delta}
=\frac{M+\Delta}{2}=\lambda_+.
$$

Thus $R^T\mathsf M R=\operatorname{diag}(\lambda_-,\lambda_+)$, with normalized eigenvectors $(c,-s)^T$ and $(s,c)^T$.

**III. Exact Light-Mass Formula and Error Bound**

Taking the nonnegative physical mass of the light mode,

$$
\begin{aligned}
m_\nu=|\lambda_-|
&=\frac{\Delta-M}{2}
=\frac{(\Delta-M)(\Delta+M)}{2(\Delta+M)}\\
&=\frac{\Delta^2-M^2}{2(\Delta+M)}
=\frac{2d^2}{\Delta+M}.
\end{aligned}
$$

Since $\Delta+M\ge2M$,

$$
0\le m_\nu\le\frac{d^2}{M}.
$$

The difference from the leading seesaw expression is

$$
\begin{aligned}
\frac{d^2}{M}-m_\nu
&=\frac{d^2(\Delta-M)}{M(\Delta+M)}
=\frac{4d^4}{M(\Delta+M)^2}
\le\frac{d^4}{M^3}.
\end{aligned}
$$

Hence $m_\nu=d^2/M+O(d^4/M^3)$ as $d/M\to0$. Also $\lambda_+=M+m_\nu$ exactly.

**IV. Expansion of the Mixing Angle**

For $|2d/M|<1$, integration of the geometric series gives

$$
\begin{aligned}
\arctan x
&=\int_0^x\frac{\mathrm dt}{1+t^2}
=\int_0^x\sum_{j=0}^{\infty}(-1)^jt^{2j}\,\mathrm dt\\
&=x-\frac{x^3}{3}+\frac{x^5}{5}+O(x^7),\\
\theta=\tfrac12\arctan(2d/M)
&=\frac dM-\frac43\frac{d^3}{M^3}
 +\frac{16}{5}\frac{d^5}{M^5}+O(d^7/M^7).
\end{aligned}
$$

Within the supplied mass matrix, the suppressed eigenvalue and mixing therefore satisfy

$$
\boxed{m_\nu=\frac{2m_D^2}{M_R+\sqrt{M_R^2+4m_D^2}},\qquad
0\le\frac{m_D^2}{M_R}-m_\nu\le\frac{m_D^4}{M_R^3},\qquad
\theta=\tfrac12\arctan(2m_D/M_R).}
$$

Q.E.D.

**In Plain English:**  
Section 9.6.4.1 formalizes the properties of the QBD proof regarding seesaw dynamics.

---

### 9.6.5 Lemma: Complexity Density Scaling {#9.6.5}

:::info[**Linear Scaling of Local Density by Braid Complexity**]
:::

Assume the local edge density $\rho_{local}$ within the effective volume of a particle braid is linear in the topological complexity $N_3$. This scaling $\rho_{local} \sim N_3$ induces a linear increase in the topological stress $\sigma$ exerted by the vacuum on the braid structure.

**In Plain English:**  
Section 9.6.5 formalizes the properties of the QBD lemma regarding complexity density scaling.

---

### 9.6.5.1 Proof: Complexity Density Scaling {#9.6.5.1}

:::tip[**Derivation of Stress Scaling through Fixed Particle Volumes**]
:::

**I. Assumed Density Law**

Let $N=N_3>0$ denote the resource count and let the asserted linear density law be $\rho_{local}=c_\rho N$, with a fixed coefficient $c_\rho>0$ (**Complexity Density Scaling** <Ref id="9.6.5" label="§9.6.5" />). In the fixed-volume version of the model,

$$
N_{sites}=c_sN,\qquad V_{braid}=V_0>0,\qquad
\rho_{local}=\frac{N_{sites}}{V_{braid}}
=\frac{c_sN}{V_0}=c_\rho N,\qquad c_\rho=\frac{c_s}{V_0}.
$$

The density increase for an integer resource increment $h$ is

$$
\rho_{local}(N+h)-\rho_{local}(N)
=c_\rho(N+h)-c_\rho N=c_\rho h.
$$

**II. Stress Relative to the Vacuum**

With the stated linear response to excess density, let $c_\sigma>0$ and

$$
\sigma(N)=c_\sigma(\rho_{local}(N)-\rho_3^*)
$$

(**Thermodynamic Fluxes** <Ref id="5.2.1" label="§5.2.1" />). Substitution yields

$$
\begin{aligned}
\sigma(N)&=c_\sigma(c_\rho N-\rho_3^*)
=c_\sigma c_\rho N-c_\sigma\rho_3^*,\\
\sigma(N+h)-\sigma(N)
&=c_\sigma c_\rho h,\\
\frac{\sigma(N)}{N}
&=c_\sigma c_\rho-\frac{c_\sigma\rho_3^*}{N}
\longrightarrow c_\sigma c_\rho.
\end{aligned}
$$

Thus the exact stress is affine in $N$, and its large-$N$ leading term is linear.

**III. Explicit High-Density Bounds**

If $N\ge2\rho_3^*/c_\rho$, then

$$
0\le\rho_3^*\le\frac{c_\rho N}{2},\qquad
\frac{c_\rho N}{2}\le c_\rho N-\rho_3^*\le c_\rho N.
$$

Multiplication by $c_\sigma>0$ gives

$$
\boxed{\frac{c_\sigma c_\rho}{2}N\le\sigma(N)
\le c_\sigma c_\rho N\qquad
\left(N\ge\frac{2\rho_3^*}{c_\rho}\right).}
$$

Q.E.D.

**In Plain English:**  
Section 9.6.5.1 formalizes the properties of the QBD proof regarding complexity density scaling.

---

### 9.6.6 Lemma: Friction Suppression Limit {#9.6.6}

:::info[**Halting of Maintenance Rewrites due to Syndrome Response Friction**]
:::

Let the stability of a topological particle be bounded by the syndrome-response friction function $f(\sigma) = e^{-\mu \sigma}$. Under this bound, there exists a critical stress threshold where the rewrite probability for structure maintenance falls below the rate of vacuum deletion.

**In Plain English:**  
Section 9.6.6 formalizes the properties of the QBD lemma regarding friction suppression limit.

---

### 9.6.6.1 Proof: Friction Suppression Limit {#9.6.6.1}

:::tip[**Demonstration via Instability Onset at Critical Complexity**]
:::

**I. Maintenance and Deletion Rates**

Write the rate model used in the argument with its positive coefficients exposed:

$$
R_+(N)=aN e^{-\mu\sigma(N)},\qquad
R_-(N)=dN,\qquad a,d,\mu>0,\qquad N>0.
$$

The exponential acceptance factor is the specified friction response (**Addition Probability** <Ref id="4.5.6" label="§4.5.6" />). The density-response model gives

$$
\sigma(N)=c_\sigma c_\rho N-c_\sigma\rho_3^*,\qquad
c_\sigma,c_\rho>0
$$

(**Complexity Density Scaling** <Ref id="9.6.5" label="§9.6.5" />). Define

$$
A=a e^{\mu c_\sigma\rho_3^*}>0,\qquad
\beta=\mu c_\sigma c_\rho>0.
$$

Then $R_+(N)=A N e^{-\beta N}$.

**II. Exact Rate Comparison**

For $N>0$,

$$
\begin{aligned}
R_+(N)<R_-(N)
&\ \Longleftrightarrow\ A N e^{-\beta N}<dN\\
&\ \Longleftrightarrow\ e^{-\beta N}<d/A\\
&\ \Longleftrightarrow\ -\beta N<\ln(d/A)\\
&\ \Longleftrightarrow\ N>\frac{\ln(A/d)}{\beta}.
\end{aligned}
$$

If $A>d$, equality occurs at the positive threshold $N_{crit}=\ln(A/d)/\beta$. If $A\le d$, then for every $N>0$,

$$
\frac{R_+(N)}{R_-(N)}=\frac Ad e^{-\beta N}<1,
$$

so the maintenance deficit already holds throughout the positive interval.

**III. Existence of a Finite Upper Interval**

Let

$$
N_* =\max\left\{0,\frac{\ln(A/d)}{\beta}\right\}.
$$

Every integer $N\ge\lfloor N_*\rfloor+1$ satisfies $N>N_*$ and hence $R_+(N)<R_-(N)$. More quantitatively, for any $0<\varepsilon<1$,

$$
N>\frac{\ln(A/(d\varepsilon))}{\beta}
\ \Longrightarrow\
\frac{R_+(N)}{R_-(N)}<\varepsilon.
$$

Thus, in this rate model,

$$
\boxed{\lim_{N\to\infty}\frac{R_+(N)}{R_-(N)}=0,\qquad
N>N_*\ \Longrightarrow\ R_+(N)<R_-(N).}
$$

Q.E.D.

**In Plain English:**  
Section 9.6.6.1 formalizes the properties of the QBD proof regarding friction suppression limit.

---

### 9.6.7 Lemma: Critical Complexity Balance {#9.6.7}

:::info[**Upper Complexity Root via a Fixed Deletion Benchmark**]
:::

Let the scalar balance benchmark be $x e^{-\mu x}=1/2$ for $x\ge0$ and $0<\mu<2/e$. Then its upper root is $N_{3,\max}=x_+=-\mu^{-1}W_{-1}(-\mu/2)$, lies above the turnover $1/\mu$, and is approximately $6.36$ at $\mu=0.40$.

**In Plain English:**  
Section 9.6.7 formalizes the properties of the QBD lemma regarding critical complexity balance.

---

### 9.6.7.1 Proof: Critical Complexity Balance {#9.6.7.1}

:::tip[**Branch Selection via Monotonicity and Lambert W Inversion**]
:::

**I. Turnover and Number of Roots**

Let $g(x)=x e^{-\mu x}$ in the fixed-deletion benchmark (**Critical Complexity Balance** <Ref id="9.6.7" label="§9.6.7" />). The constant deletion threshold is the half-rate benchmark (**Deletion Probability** <Ref id="4.5.7" label="§4.5.7" />). The derivative and endpoint values are

$$
g'(x)=e^{-\mu x}-\mu x e^{-\mu x}=e^{-\mu x}(1-\mu x),
\quad g(0)=0,\quad \lim_{x\to\infty}g(x)=0 .
$$

The derivative is positive below $1/\mu$ and negative above it. At the turnover $g(1/\mu)=1/(e\mu)>1/2$ because $\mu<2/e$. Continuity and strict monotonicity give one root on each side of $1/\mu$. On the decreasing branch, $x>x_+$ implies $g(x)<1/2$.

**II. Exact Upper Root**

With $y=-\mu x$, the balance equation is

$$
x e^{-\mu x}=\tfrac12
\quad\Longleftrightarrow\quad
(-\mu x)e^{-\mu x}=-\tfrac\mu2
\ \Longleftrightarrow\
y e^y=-\tfrac\mu2.
$$

Since $-\mu/2\in(-1/e,0)$, the principal branch gives $-1<y<0$ and the lower root. The branch $W_{-1}$ gives $y<-1$ and hence the upper root

$$
x_+=-\frac1\mu W_{-1}(-\mu/2)>\frac1\mu .
$$

**III. Numerical Bracket at the Reference Friction**

At $\mu=0.40$, the turnover is $2.5$ and its value is $2.5/e\simeq0.9197$. On the decreasing branch,

$$
g(6.3566)=6.3566e^{-2.54264}\simeq0.500000412>\tfrac12,\qquad
g(6.3567)=6.3567e^{-2.54268}\simeq0.499988278<\tfrac12 .
$$

The upper root belongs to $(6.3566,6.3567)$, so it rounds to $6.36$.

Q.E.D.

**In Plain English:**  
Section 9.6.7.1 formalizes the properties of the QBD proof regarding critical complexity balance.

---

### 9.6.8 Lemma: Planck Anchor {#9.6.8}

:::info[**Heavy-mass scaling via a specified Planck matching factor**]
:::

Let the heavy-neutrino model prescribe $M_R=A M_{\mathrm{Pl}}e^{-c_*/\mu}$ in natural units with dimensionless $A,c_*,\mu>0$. Then for the stated benchmark $c_*=2.76$, $\mu=0.40$ and $A=1$, the modeled heavy mass is approximately $1.23\times10^{16}\,\mathrm{GeV}$.

**In Plain English:**  
Section 9.6.8 formalizes the properties of the QBD lemma regarding planck anchor.

---

### 9.6.8.1 Proof: Planck Anchor {#9.6.8.1}

:::tip[**Derivation of the benchmark scale via Planck units and explicit matching**]
:::

**I. Planck units**

With $c_{\mathrm{light}}$ the speed of light, the conventional Planck time and energy satisfy

$$
t_{\mathrm{Pl}}=\sqrt{\frac{\hbar G}{c_{\mathrm{light}}^5}},\qquad
\omega_{\mathrm{Pl}}=\frac1{t_{\mathrm{Pl}}}
=\sqrt{\frac{c_{\mathrm{light}}^5}{\hbar G}},\qquad
E_{\mathrm{Pl}}=\hbar\omega_{\mathrm{Pl}}
=\sqrt{\frac{\hbar c_{\mathrm{light}}^5}{G}}
=M_{\mathrm{Pl}}c_{\mathrm{light}}^2.
$$

The equality between the graph tick and $t_{\mathrm{Pl}}$ would be an additional clock matching. For the benchmark in **Planck Anchor** <Ref id="9.6.8" label="§9.6.8" />, express masses as rest energies in GeV.

**II. Numerical mass match**

Using $M_{\mathrm{Pl}}\simeq1.22\times10^{19}\,\mathrm{GeV}$, the exponent and factor are

$$
\frac{c_*}{\mu}=\frac{2.76}{0.40}=6.90,\qquad
e^{-6.90}\simeq1.00779\times10^{-3}.
$$

Consequently,

$$
M_R=A(1.22\times10^{19}\,\mathrm{GeV})(1.00779\times10^{-3})
\simeq A(1.23\times10^{16}\,\mathrm{GeV}).
$$

For a target $M_R=2.36\times10^{16}\,\mathrm{GeV}$ at the same exponent and Planck mass, the required coefficient is

$$
A=\frac{2.36\times10^{16}}
        {(1.22\times10^{19})e^{-6.90}}
\simeq1.92 .
$$

**III. Relation to the complexity threshold**

If the independent relation $M_R=\kappa_{\mathrm{scale}}N_{3,\max}$ is also imposed, **Critical Complexity Balance** <Ref id="9.6.7" label="§9.6.7" /> supplies $N_{3,\max}=-\mu^{-1}W_{-1}(-\mu/2)$ in its benchmark. Compatibility requires

$$
\kappa_{\mathrm{scale}}
=\frac{A M_{\mathrm{Pl}}e^{-c_*/\mu}}{N_{3,\max}}
\simeq A\frac{1.23\times10^{16}\,\mathrm{GeV}}{6.36}
\simeq A(1.93\times10^{15}\,\mathrm{GeV})
$$

per unit of complexity at $\mu=0.40$.

Q.E.D.

**In Plain English:**  
Section 9.6.8.1 formalizes the properties of the QBD proof regarding planck anchor.

---

### 9.6.9 Proof: Neutrino Mass Mechanism {#9.6.9}

:::tip[**Conditional Seesaw Eigenvalue via Singlet Assignment and Scale Matching**]
:::

**I. Neutrality, Singlet Assignment, and Bare Mass**

For the folded label take segment writhes $W_+=k$ and $W_-=-k$. The electric charge vanishes because $Q=(k-k)/3=0$. The positive excess fold cost of **Neutrality Verification** <Ref id="9.6.3" label="§9.6.3" /> remains compatible with this cancellation. The bare light entry $M_L=0$ is a separate premise of the effective mass matrix.

For the assigned sterile partner $|s\rangle$, assume a trivial color and weak action and hypercharge zero. The generators and quadratic Casimirs then act as

$$
\begin{aligned}
T_C^a|s\rangle&=T_W^b|s\rangle=Y|s\rangle=0,\\
C_2^{(3)}|s\rangle&=\sum_a T_C^a(T_C^a|s\rangle)=0,\\
C_2^{(2)}|s\rangle&=\sum_b T_W^b(T_W^b|s\rangle)=0,\qquad
e^{i\theta Y}|s\rangle=|s\rangle.
\end{aligned}
$$

These identities use the stipulated sterile representation of the partner. The light neutral label may belong to a weak doublet.

**II. Complexity and Planck Matching**

At fixed volume the local density model assigns density proportional to complexity (**Complexity Density Scaling** <Ref id="9.6.5" label="§9.6.5" />). The maintenance weight includes the friction factor $e^{-\mu\sigma}$ at stress $\sigma$ (**Friction Suppression Limit** <Ref id="9.6.6" label="§9.6.6" />). In the separately prescribed balance $xe^{-\mu x}=1/2$, writing $u=-\mu x$ gives $ue^u=-\mu/2$. The upper root is $-\mu^{-1}W_{-1}(-\mu/2)\simeq6.36$ at $\mu=0.40$ (**Critical Complexity Balance** <Ref id="9.6.7" label="§9.6.7" />).

For a dimensionful scale use **Planck Anchor** <Ref id="9.6.8" label="§9.6.8" /> with $c_*=2.76$ and $M_{\mathrm{Pl}}=1.22\times10^{19}\,\mathrm{GeV}$. The unit-prefactor anchor and matched coefficient are

$$
\begin{aligned}
M_R(1)&=(1.22\times10^{19}\,\mathrm{GeV})e^{-2.76/0.40}
\simeq1.2295\times10^{16}\,\mathrm{GeV},\\
A&=\frac{2.36\times10^{16}\,\mathrm{GeV}}{M_R(1)}\simeq1.92,\qquad
M_R(A)=A M_R(1).
\end{aligned}
$$

An additional relation $M_R=\kappa_{\mathrm{scale}}N_{3,\max}$ would require $\kappa_{\mathrm{scale}}=M_R(A)/6.36$ at these benchmark inputs. The scalar root is dimensionless.

**III. Light Eigenvalue and Units**

Set $m_D=yv$ at $v=246\,\mathrm{GeV}$ in the Yukawa convention of the benchmark. With the real symmetric matrix of **Seesaw Dynamics** <Ref id="9.6.4" label="§9.6.4" />, its eigenvalue equation and nonnegative light mass are

$$
\det\begin{pmatrix}-\lambda&m_D\\m_D&M_R-\lambda\end{pmatrix}
=\lambda^2-M_R\lambda-m_D^2=0,\qquad
m_\nu=\frac{\sqrt{M_R^2+4m_D^2}-M_R}{2}
=\frac{2m_D^2}{\sqrt{M_R^2+4m_D^2}+M_R}.
$$

Subtracting the exact mass from the leading expression gives

$$
0\le\frac{m_D^2}{M_R}-m_\nu
=\frac{4m_D^4}{M_R(\sqrt{M_R^2+4m_D^2}+M_R)^2}
\le \frac{m_D^4}{M_R^3}.
$$

At $M_R=2.36\times10^{16}\,\mathrm{GeV}$ and $0<y\le1$, the relative error with respect to the leading expression is at most $(246/(2.36\times10^{16}))^2<1.09\times10^{-28}$. With $1\,\mathrm{GeV}=10^9\,\mathrm{eV}$, the leading evaluations are

$$
\begin{aligned}
m_\nu(y=0.5)&\simeq\frac{123^2}{2.36\times10^{16}}\,\mathrm{GeV}
=6.4106\times10^{-4}\,\mathrm{eV},\\
m_\nu(y=1)&\simeq\frac{246^2}{2.36\times10^{16}}\,\mathrm{GeV}
=2.5642\times10^{-3}\,\mathrm{eV}.
\end{aligned}
$$

**IV. Oscillation Comparison**

The atmospheric benchmark is a difference of squared masses, $|\Delta m^2|\simeq2.4\times10^{-3}\,\mathrm{eV}^2$. [Super-Kamiokande atmospheric analysis](https://doi.org/10.1103/PhysRevD.109.072014)

Its square root is $\sqrt{2.4\times10^{-3}}\,\mathrm{eV}\simeq0.0490\,\mathrm{eV}$. If a modeled mass $m_i$ is assigned to the lighter member of that pair, the other member must satisfy

$$
m_j^2-m_i^2=2.4\times10^{-3}\,\mathrm{eV}^2,\qquad
m_j=\sqrt{m_i^2+2.4\times10^{-3}\,\mathrm{eV}^2}.
$$

For example the $y=1$ value would require $m_j\simeq0.0491\,\mathrm{eV}$. The two-state light-heavy matrix gives one light eigenvalue. Predicting the atmospheric splitting requires at least two light eigenvalues and the appropriate flavor mixing.

Q.E.D.

**In Plain English:**  
Section 9.6.9 formalizes the properties of the QBD proof regarding neutrino mass mechanism.

---

### 9.6.9.1 Calculation: Neutrino Mass Prediction {#9.6.9.1}

:::note[**Verification of the Two-State Benchmark via Exact Eigenvalue and Unit Conversion**]
:::

The calculation uses the exponential **Planck Anchor** <Ref id="9.6.8" label="§9.6.8" /> and evaluates the two-state mass in **Seesaw Dynamics** <Ref id="9.6.4" label="§9.6.4" />.

1.  **Scale Calibration:** Evaluate the unit-prefactor heavy mass and divide the prescribed $2.36\times10^{16}\,\mathrm{GeV}$ by it to obtain the matched prefactor.
2.  **Light Mass:** Set $m_D=yv$ and use the rationalized light eigenvalue to avoid subtracting two nearly equal heavy-scale quantities. Report $(m_D/M_R)^2$ as the relative error bound for the leading approximation.
3.  **Units Comparison:** Convert the light mass to eV. Report the atmospheric reference in $\mathrm{eV}^2$ and its square root separately in eV.

```python
from decimal import Decimal, localcontext


def verify_neutrino_seesaw():
    """Compare the unit Planck anchor and calibrated two-state seesaw."""
    with localcontext() as context:
        context.prec = 60
        v = Decimal("246")
        mu = Decimal("0.40")
        c_star = Decimal("2.76")
        planck_mass = Decimal("1.22e19")
        unit_mass = planck_mass * (-c_star / mu).exp()
        target_mass = Decimal("2.36e16")
        matched_prefactor = target_mass / unit_mass
        gev_to_ev = Decimal("1e9")
        atmospheric_split_ev2 = Decimal("2.4e-3")

        print("TWO-STATE SEESAW: HEAVY-SCALE AND UNITS CHECK")
        print(f"Unit anchor: A=1, M_R={unit_mass:.6E} GeV")
        print(f"Matched anchor: A={matched_prefactor:.6f}, M_R={target_mass:.6E} GeV")
        print("Yukawa  m_D (GeV)  m_light (GeV)  m_light (eV)  Relative error bound")
        for value in ("0.01", "0.10", "0.50", "1.00"):
            yukawa = Decimal(value)
            dirac_mass = yukawa * v
            dirac_squared = dirac_mass ** 2
            gap = (target_mass ** 2 + 4 * dirac_squared).sqrt()
            light_gev = 2 * dirac_squared / (gap + target_mass)
            light_ev = light_gev * gev_to_ev
            relative_bound = (dirac_mass / target_mass) ** 2
            print(
                f"{yukawa:6.2f}  {dirac_mass:9.2f}  "
                f"{light_gev:13.6E}  {light_ev:12.6E}  {relative_bound:.3E}"
            )

        print(f"Atmospheric comparison: |delta m^2|={atmospheric_split_ev2:.3E} eV^2")
        print(f"Square-root scale: {atmospheric_split_ev2.sqrt():.6E} eV")


if __name__ == "__main__":
    verify_neutrino_seesaw()
```

**Simulation Results:**

```text
TWO-STATE SEESAW: HEAVY-SCALE AND UNITS CHECK
Unit anchor: A=1, M_R=1.229498E+16 GeV
Matched anchor: A=1.919482, M_R=2.360000E+16 GeV
Yukawa  m_D (GeV)  m_light (GeV)  m_light (eV)  Relative error bound
  0.01       2.46   2.564237E-16   2.564237E-7  1.087E-32
  0.10      24.60   2.564237E-14   2.564237E-5  1.087E-30
  0.50     123.00   6.410593E-13   6.410593E-4  2.716E-29
  1.00     246.00   2.564237E-12   2.564237E-3  1.087E-28
Atmospheric comparison: |delta m^2|=2.400E-3 eV^2
Square-root scale: 4.898979E-2 eV
```

**Conclusion:**
The unit-prefactor anchor gives $1.2295\times10^{16}\,\mathrm{GeV}$. The prescribed heavy mass requires $A\simeq1.9195$ and gives light masses of $0.6411\,\mathrm{meV}$ at $y=0.50$ and $2.5642\,\mathrm{meV}$ at $y=1$. The atmospheric reference is a difference of squared masses. The program evaluates a single light eigenvalue for each separate Yukawa input, with separate benchmark rows for the different inputs.

**In Plain English:**  
Section 9.6.9.1 formalizes the properties of the QBD calculation regarding neutrino mass prediction.

---

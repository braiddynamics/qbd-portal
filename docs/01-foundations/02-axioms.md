---
title: "Chapter 2: Axioms (Constraints)"
sidebar_label: "Chapter 2: Axioms"
---
import SimTable from '@site/src/components/sim-table';
import simData from '@site/static/data/sim_cycle_reduction.json';

Principles of causal structure dictate that links maintain directionality and form bounded geometries without redundancy or cycles that undermine progression. The axioms channel relations into a framework where influence propagates unidirectionally, assembling space from minimal closures while preserving order across scales.



## 2.1 Axiom 1: The Causal Primitive

### 2.1.1 Axiom: The Directed Causal Link
The directed causal link, denoted $v_i \to v_j$, constitutes the minimal relational unit of causality. The link is **irreflexive** ($v_i \nrightarrow v_i$) and **asymmetric** ($v_i \to v_j \implies v_j \nrightarrow v_i$).

### 2.2.1 Theorem: Insufficiency of Antisymmetry
Antisymmetry alone is insufficient because it permits self-loops ($v \to v$). 

#### 2.2.1.2 Diagram: Ordering Constraints

```mermaid
graph TD;
    subgraph Math["(A) Mathematical Antisymmetry"]
        U1((u)) -->|Loop| U1
        style U1 fill:#f9f,stroke:#333,stroke-width:2px
    end
    subgraph Phys["(B) Physical Irreflexivity"]
        U2((u)) --> V2((v))
        style U2 fill:#bbf,stroke:#333
        style V2 fill:#bbf,stroke:#333
    end
# Chapter 1: Substrate

## 1.1 The Ontology (Smoke Test)
We posit that the fundamental ontology is a Directed Acyclic Graph (DAG), $\Graph$.

### 1.2.1 Time and Evolution
We distinguish between the fundamental update step and the emergent manifold time.

$$
\tphys \neq \tL
$$

The state of the universe at step $\tL$, denoted $U_{\tL}$, evolves via the universal operator:

$$
\ket{\Psi(\tL + 1)} = \Evol \ket{\Psi(\tL)}
$$

Where the entropy is given by:
$$
\Ent = -k_B \text{Tr}(\rho \ln \rho)
$$

## 1.3 Geometric Emergence
Spatial geometry emerges from the density of directed 3-cycles, denoted $\geom$.
The total curvature is related to the count of these cycles:

$$
R_{disc} \propto \sum_{v \in V} \card{\geom_v}
$$

### 1.4 Visualizing the DAG
The causal structure is locally finite but globally growing.

```mermaid
graph TD;
    A((Event A)) --> B((Event B));
    A --> C((Event C));
    B --> D((Event D));
    C --> D;
    D --> E((Event E));
    style A fill:#f9f,stroke:#333,stroke-width:4px
    style E fill:#bbf,stroke:#333,stroke-width:2px
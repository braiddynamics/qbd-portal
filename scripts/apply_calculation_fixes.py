import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
docs_root = os.path.join(PROJECT_ROOT, "docs")

# Mapping of file relative paths to the calculation updates
# We will do exact block replacements to ensure safety and precision.
# Use raw strings for both patterns and replacements to avoid invalid escape sequence errors in python.
replacements = {
    "01-rules/02-axioms/2.4.md": [
        (
            r"### 2.4.10 Calculation: Simulation Verification {#2.4.10}\n\n:::note\[\*\*Simulation Verification of the Cycle Reduction Algorithm via Deterministic Execution\*\*\]\n:::\n\nConfirmation of the finite termination condition established in the General Cycle Decomposition the \*\*general cycle decomposition proof\*\* \[\(§2\.4\.6\)\].*?\n\n1\.\s+\*\*Initialization:\*\*.*?\n2\.\s+\*\*Chordal Insertion:\*\*.*?\n3\.\s+\*\*Entropic Deletion:\*\*.*?\n4\.\s+\*\*Metric:\*\*.*?\n",
            r"""### 2.4.10 Calculation: Simulation Verification {#2.4.10}

:::note[**Simulation Verification of the Cycle Reduction Algorithm via Deterministic Execution**]
:::

Verification of the finite termination condition established in the General Cycle Decomposition Proof [(§2.4.6)](/monograph/rules/axioms/2.4/#2.4.6) is based on the following protocols:

1.  **Defect Initialization:** The algorithm constructs isolated directed cycles of length $k \in [4, 12]$ to serve as standardized topological defects. This mapping represents the initialization of unstable macroscopic loops within the vacuum.
2.  **Topological Reduction:** The protocol simulates a maximally parallel update by instantiating chords across open 2-paths and subsequently prunes macro-cycles ($L > 3$) via entropic deletion to resolve topological tension.
3.  **Operation Counting:** The metric tracks the total additions and deletions required for the system to reach the simplicial ground state ($L_{\max} = 3$).
"""
        )
    ],
    
    "01-rules/03-architecture/3.1.md": [
        (
            r"2\.\s+\*\*Topological Sort:\*\* The protocol utilizes the `networkx\.is_directed_acyclic_graph` function to perform a depth-first search traversal\. This function tests for the presence of back-edges that would indicate closed topological loops\.",
            r"2.  **Topological Sort:** The protocol utilizes the `networkx.is_directed_acyclic_graph` check to perform a depth-first search traversal. This procedure tests for the presence of back-edges that would indicate closed topological loops."
        )
    ],
    
    "01-rules/03-architecture/3.2.md": [
        (
            r"partitions the vertex set into equivalence classes \(orbits\)",
            r"partitions the vertex set into equivalence partitions (orbits)"
        )
    ],
    
    "01-rules/03-architecture/3.3.md": [
        (
            r"### 3.3.5.2 Calculation: Cycle Resolution {#3.3.5.2}\n\n:::info\[\*\*Algorithmic Resolution of Symmetric Overlaps in a 6-Cycle Graph using Parallel Operations\*\*\]\n:::\n\nInitial state with timestamps: A → B",
            r"""### 3.3.5.2 Calculation: Cycle Resolution {#3.3.5.2}

:::note[**Resolution of Symmetric Overlaps via Parallel Operations**]
:::

Verification of the conflict resolution established in the Conflict Resolution Proof [(§3.3.5.1)](/monograph/rules/architecture/3.3/#3.3.5.1) is based on the following protocols:

1.  **Chordal Addition:** The algorithm instantiates chords across all open 2-paths to partition symmetric overlaps. This maps the initial expansion of cycles under background-independent rules.
2.  **Overlap Identification:** The protocol flags shared boundary edges within newly created cycles of length four or greater.
3.  **Parallel Deletion:** The metric tracks the elimination of all flagged overlap edges to break the original cycle and restore symmetry.

Initial state with timestamps: A → B"""
        ),
        (
            r"1\.\s+\*\*State Initialization:\*\* A balanced \$N=7\$ Bethe fragment is constructed\..*?\n2\.\s+\*\*Sequential Perturbation:\*\*.*?\n3\.\s+\*\*Parallel Perturbation:\*\*.*?\n4\.\s+\*\*Group Analysis:\*\*.*?\n",
            r"""1.  **State Initialization:** A balanced $N=7$ Bethe fragment is constructed. The graph topology possesses an initial $S_3$ symmetry group due to the structural indistinguishability of its three primary branches.
2.  **Scheduler Perturbation:** The protocol simulates both sequential scheduling (instantiating a single compliant chord $(1,2)$) and maximally parallel scheduling (simultaneously instantiating all compliant chords $\{(1,2), (2,3), (1,3)\}$).
3.  **Group Analysis:** The metric evaluates the automorphism group size post-update to determine if the scheduling operations broke the initial symmetry state.
"""
        )
    ],
    
    "01-rules/03-architecture/3.5.md": [
        (
            r"error subspace \(open strings\)",
            r"error subspace (unclosed paths)"
        ),
        (
            r"1\.\s+\*\*Commutation Logic:\*\* A function is defined to test the commutation relations between Pauli error operators",
            r"1.  **Commutation Logic:** A procedure is defined to test the commutation relations between Pauli error operators"
        )
    ],
    
    "01-rules/04-dynamics/4.2.md": [
        (
            r"Verification of the structural claims established in \*\*The Partial Order Property\*\* \[\(§4\.2\.9\)\].*?is performed via topological path analysis on a generated causal graph\.",
            r"Verification of the structural claims established in the Partial Order Property Proof [(§4.2.9.1)](/monograph/rules/dynamics/4.2/#4.2.9.1) is based on the following protocols:"
        )
    ],
    
    "01-rules/04-dynamics/4.3.md": [
        (
            r"1\.\s+\*\*Object Definition:\*\* The algorithm defines an `AnnotatedGraph` class that couples a causal graph structure \(via NetworkX\) with a nested tuple annotation",
            r"1.  **State Definition:** The algorithm defines an `AnnotatedGraph` representation that couples a causal graph structure (via NetworkX) with a nested coordinate mapping"
        )
    ],
    
    "01-rules/04-dynamics/4.4.md": [
        (
            r"3\.\s+\*\*Topological Closure:\*\* The simulation introduces the return edge \$u \\to v\$ to close the directed 3-cycle\.",
            r"3.  **Topological Closure:** The simulation introduces the closing edge $u \to v$ to close the directed 3-cycle."
        ),
        (
            r"Verification of the entropic driver established in the Relational Entropy the \*\*entropy of closure theorem\*\* \[\(§4\.4\.2\)\].*?is based on the following protocols:",
            r"Verification of the entropic driver established in the Entropy of Closure Proof [(§4.4.2.1)](/monograph/rules/dynamics/4.4/#4.4.2.1) is based on the following protocols:"
        ),
        (
            r"2\.\s+\*\*Stress Sweep:\*\* The protocol applies the damping function \$f\(s\) = e\^\{-\\mu s\}\$",
            r"2.  **Stress Sweep:** The protocol applies the damping factor $f(s) = e^{-\mu s}$"
        ),
        (
            r"Validation of the stress-dependent damping factor established in the Friction the \*\*the friction coefficient theorem\*\* \[\(§4\.4\.6\)\].*?is based on the following protocols:",
            r"Validation of the stress-dependent damping factor established in the Friction Coefficient Proof [(§4.4.6.1)](/monograph/rules/dynamics/4.4/#4.4.6.1) is based on the following protocols:"
        )
    ],
    
    "01-rules/04-dynamics/4.6.md": [
        (
            r"Verification of the emergent probability weights established in the \*\*Born Rule Derivation\*\* \[\(§4\.6\.2\)\].*?is based on the following protocols:",
            r"Verification of the emergent probability weights established in the Born Rule Proof [(§4.6.2.1)](/monograph/rules/dynamics/4.6/#4.6.2.1) is based on the following protocols:"
        ),
        (
            r"Quantification of the information loss inherent in the Time Evolution Operator \$\\mathcal\{U\}\$ established in the Irreversibility the \*\*the thermodynamic arrow theorem\*\* \[\(§4\.6\.3\)\].*?is based on the following protocols:",
            r"Quantification of the information loss inherent in the Time Evolution Operator $\mathcal{U}$ established in the Thermodynamic Arrow Proof [(§4.6.3.1)](/monograph/rules/dynamics/4.6/#4.6.3.1) is based on the following protocols:"
        )
    ],
    
    "01-rules/05-equilibrium/5.1.md": [
        (
            r"Quantification of the subextensive boundary term and verification of the independence assumption are based on a simulation of a 2D toroidal lattice\. The simulation protocols are as follows:",
            r"Quantification of the subextensive boundary term and verification of the independence assumption established in the Boundary Phase Stability Proof [(§5.1.4)](/monograph/rules/equilibrium/5.1/#5.1.4) is based on the following protocols:"
        )
    ],
    
    "01-rules/05-equilibrium/5.2.md": [
        (
            r"Verification of the combinatorial derivation established in the \*\*Growth Term Derivation\*\* \[\(§5\.2\.4\)\].*?is based on the following protocols:",
            r"Verification of the combinatorial derivation established in the Combinatorial Precursors Proof [(§5.2.4.1)](/monograph/rules/equilibrium/5.2/#5.2.4.1) is based on the following protocols:"
        ),
        (
            r"Validation of the exponential suppression factor established in the \*\*Friction Term Derivation\*\* \[\(§5\.2\.5\)\].*?is based on the following protocols:",
            r"Validation of the exponential suppression factor established in the Friction Term Derivation Proof [(§5.2.5.1)](/monograph/rules/equilibrium/5.2/#5.2.5.1) is based on the following protocols:"
        ),
        (
            r"Validation of the catalytic stress term established in the \*\*Instability Derivation\*\* \[\(§5\.2\.6\)\].*?is based on the following protocols:",
            r"Validation of the catalytic stress term established in the Instability Derivation Proof [(§5.2.6.1)](/monograph/rules/equilibrium/5.2/#5.2.6.1) is based on the following protocols:"
        ),
        (
            r"2\.\s+\*\*Root Finding:\*\* The protocol uses Brent's method to numerically solve",
            r"2.  **Root Finding:** The protocol uses Brent's search algorithm to numerically solve"
        ),
        (
            r"Verification of the Master Equation's equilibrium properties is based on the following protocols:",
            r"Verification of the Master Equation's equilibrium properties established in the Equation Resolution Proof [(§5.2.7)](/monograph/rules/equilibrium/5.2/#5.2.7) is based on the following protocols:"
        )
    ],
    
    "01-rules/05-equilibrium/5.3.md": [
        (
            r"### 5.3.3 Calculation: The Phase Space Sweep {#5.3.3}\n\n:::tip\[\*\*Implementation of the Evolution Operator and Sweep Logic\*\*\]\n:::\n\nThe following snippets from the full simulation illustrate the core logic of the worker trajectory, the localized awareness computation, and the thermodynamic proposal generation\.",
            r"""### 5.3.3 Calculation: The Phase Space Sweep {#5.3.3}

:::note[**Algorithmic Sweep of Phase Space via Parallel Execution**]
:::

Verification of the phase space trajectories established in the Phase Space Consistency Proof [(§5.3.2)](/monograph/rules/equilibrium/5.3/#5.3.2) is based on the following protocols:

1.  **Worker Orchestration:** The algorithm coordinates the spatial trajectory of parallel workers traversing the network substrate. This maps to the localized propagation of events in the physical vacuum.
2.  **Awareness Computation:** The protocol evaluates local syndromes and causal histories to determine update eligibility at active sites.
3.  **Proposal Generation:** The metric tracks the thermodynamic acceptance weights for proposed structural transitions across the phase space.

The following snippets from the full simulation illustrate the core logic of the worker trajectory, the localized awareness computation, and the thermodynamic proposal generation."""
        )
    ],
    
    "02-players/07-topology/7.4.md": [
        (
            r"1\.\s+\xa0\*\*Parameter Definition:\*\*",
            r"1.  **Parameter Definition:**"
        ),
        (
            r"2\.\s+\xa0\*\*Topological Harmonics:\*\*",
            r"2.  **Topological Harmonics:**"
        ),
        (
            r"3\.\s+\xa0\*\*Spectrum Matching:\*\*",
            r"3.  **Spectrum Matching:**"
        )
    ],
    
    "02-players/08-braids/8.2.md": [
        (
            r"1\.\s+\*\*Parameter Definition:\*\* The algorithm defines a range of separation lengths \$L\$ and sets the string tension",
            r"1.  **Parameter Definition:** The algorithm defines a range of separation lengths $L$ and sets the confinement tension"
        ),
        (
            r"2\.\s+\*\*Energy Calculation:\*\* The protocol computes the potential energy as a linear function of length",
            r"2.  **Energy Calculation:** The protocol computes the potential energy as a linear mapping of length"
        )
    ],
    
    "02-players/09-unification/9.5.md": [
        (
            r"failure of perturbative methods established",
            r"failure of perturbative procedures established"
        ),
        (
            r"the \*\*decay rate calculation proof\*\*",
            r"the **Decay Rate Calculation Proof**"
        )
    ],
    
    "02-players/10-computation/10.9.md": [
        (
            r"established in the Group Closure the \*\*argument outline commentary\*\* \[\(§10\.9\.1\.1\)\].*?is based on the following protocols:",
            r"established in the Group Closure Verification Proof [(§10.9.2.1)](/monograph/players/computation/10.9/#10.9.2.1) is based on the following protocols:"
        ),
        (
            r"established in the \*\*Universality Implementation\*\* \[\(§10\.9\.4\)\].*?is based on the following protocols:",
            r"established in the Computational Universality Proof [(§10.9.3)](/monograph/players/computation/10.9/#10.9.3) is based on the following protocols:"
        )
    ]
}

def apply_fixes():
    for relpath, fix_list in replacements.items():
        filepath = os.path.join(docs_root, relpath.replace("/", os.sep))
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content
        for pat, repl in fix_list:
            content, count = re.subn(pat, lambda m, r=repl: r, content, flags=re.DOTALL)
            if count == 0:
                # Try without DOTALL if it's a simple regex
                content, count = re.subn(pat, lambda m, r=repl: r, content)
                
            if count > 0:
                print(f"Applied fix in {relpath} ({count} replacements)")
            else:
                print(f"WARNING: Pattern did not match in {relpath}")
                
        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Saved modified file: {relpath}")
            
if __name__ == "__main__":
    apply_fixes()

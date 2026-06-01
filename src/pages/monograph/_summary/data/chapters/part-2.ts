import { ChapterData } from '../../types';

export const part2Chapters: ChapterData[] = [
  {
    num: 6,
    part: "Part II: Topological Nature of Matter (The Players)",
    title: "Tripartite Braid",
    taxonomy: "Fermions",
    status: "Theoretical Model",
    leanProofs: 0,
    pythonSims: 4,
    executiveEvaluation: "Fermions emerge naturally as stable, localized twists (3-strand tripartite braids) embedded in the pre-geometric vacuum network, rather than point-like particle coordinates. Symmetries emerge as local transformations of local braid groups.",
    breakdowns: [
      {
        title: "6.1 Principles of Particle Formation",
        content: "Establishes the topological origin of matter, showing that particles are not point-like coordinates but localized braid defects."
      },
      {
        title: "6.2 Tripartite Braid",
        content: "Constructs fermions as tripartite braids formed by three intertwined ribbons, mapping spin and charge to ribbon twists."
      },
      {
        title: "6.3 Braid Complexity Functional",
        content: "Defines the braid complexity functional, which measures the topological energy barrier protecting localized twists."
      },
      {
        title: "6.4 Topological Stability",
        content: "Proves the topological stability of tripartite braids under vacuum rewrites, guaranteeing particle conservation."
      }
    ],
    specialists: [
      {
        area: "For Particle Physicists",
        text: "Braid twist states construct localized boundaries that behave like point-like Dirac particles under coordinate transformations, deriving mass from pre-geometric constraints."
      },
      {
        area: "For High Energy Physicists",
        text: "Triple-strand braid crossings enforce chiral asymmetry, explaining the natural preservation of left-handed lepton structures."
      },
      {
        area: "For Quantum Topologists",
        text: "Ribbon writhe calculations map tripartite braids directly to discrete fermion spin representations without continuous spatial coordinate frames."
      }
    ],
    analogy: "Rather than particles being tiny solid marbles moving through space, they are localized, self-sustaining knots tied into the spatial web itself, much like a knot sliding smoothly along a piece of rope.",
    link: "/monograph/players/fermions/6.1",
    style: "A",
    definitions: [
      {
        term: "Tripartite Braid",
        definition: "A localized, stable 3-strand twist in the empty vacuum network, representing an elementary particle (fermion) rather than a point mass."
      },
      {
        term: "Ribbon Twists",
        definition: "The helical rotations of network bands that topologically protect particles from decaying or dispersing."
      }
    ],
    historicalCallout: {
      title: "Lord Kelvin's Vortex Atoms",
      text: "In 1867, Lord Kelvin proposed that atoms were knotted vortices in the ether, protecting them from structural decay. QBD mathematically formalizes this: mass and particles are indeed topological knots protected from decaying by graph conservation rules."
    }
  },
  {
    num: 7,
    part: "Part II: Topological Nature of Matter (The Players)",
    title: "Quantum Numbers",
    taxonomy: "Topology",
    status: "Theoretical Model",
    leanProofs: 0,
    pythonSims: 1,
    executiveEvaluation: "Maps physical quantum properties (such as electric charge, spin, and color charge) directly to conserved topological braid invariants.",
    breakdowns: [
      {
        title: "7.1 Spin and Statistics",
        content: "Derives spin-statistics relation directly from cycle parity, explaining half-integer spin from tripartite rotation symmetries."
      },
      {
        title: "7.2 Pauli Exclusion Principle",
        content: "Formulates a coordinate-free proof of the Pauli Exclusion Principle, arising from topological braid crossing constraints."
      },
      {
        title: "7.3 Quantized Electric Charge",
        content: "Identifies electric charge as the net writhe polynomial of the tripartite braid, explaining why quark charges are quantized in thirds."
      },
      {
        title: "7.4 Topological Mass Functional",
        content: "Develops the topological mass functional, deriving particle inertial mass from localized graph curvature stress."
      }
    ],
    specialists: [
      {
        area: "For Quantum Information Theorists",
        text: "Quantum numbers are conserved as global topological invariants, preventing decoherence and explaining standard quantum numbers from topological robustness."
      },
      {
        area: "For Mathematical Physicists",
        text: "Integer writhe polynomials generate exact fractional quantum charges, deriving quantum numbers directly from ribbon twist states."
      },
      {
        area: "For Quantum Computing Researchers",
        text: "The topological conservation of ribbon invariants provides hardware-level protection against local phase errors."
      }
    ],
    analogy: "The number of twists and loops in a ribbon. No matter how much you stretch or pull the ribbon, the count of twists remains completely unchanged, representing conserved properties like electric charge.",
    link: "/monograph/players/topology/7.1",
    style: "B",
    definitions: [
      {
        term: "Topological Writhe",
        definition: "The net rotation cycles of the braid strands, which mathematically determines electric charge and explains why it is quantized in thirds."
      },
      {
        term: "Cycle Parity",
        definition: "The algebraic rotational count that establishes a particle's spin and half-integer statistics coordinate-freely."
      }
    ],
    historicalCallout: {
      title: "Dirac's Chiral Belt Topology",
      text: "Paul Dirac demonstrated that a 360-degree rotation of a ribbon twists it, but a 720-degree rotation can be untwisted without moving the endpoints, explaining spin-1/2 fermions. QBD implements this belt trick directly in the tripartite braid twist network."
    }
  },
  {
    num: 8,
    part: "Part II: Topological Nature of Matter (The Players)",
    title: "Gauge Symmetries",
    taxonomy: "Braids",
    status: "Theoretical Model",
    leanProofs: 0,
    pythonSims: 5,
    executiveEvaluation: "Gauge symmetries (such as $SU(3) \\times SU(2) \\times U(1)$) emerge naturally from coordinate-free local coordinate transitions of the braid network.",
    breakdowns: [
      {
        title: "8.1 Generator Principle",
        content: "Formulates the generator principle, deriving gauge fields directly from the local coordinate swaps of the ribbon braids."
      },
      {
        title: "8.2 Strong Interaction",
        content: "Derives the strong interaction from SU(3) permutation symmetries of tripartite braid strand swaps."
      },
      {
        title: "8.3 Chiral Weak Interaction",
        content: "Constructs the weak interaction as a chiral swap transition acting selectively on specific braid generations."
      },
      {
        title: "8.4 Electroweak Mixing",
        content: "Explains electroweak mixing and Weinberg angle values strictly from topological ribbon crossing ratios."
      },
      {
        title: "8.5 Emergent Gauge Coupling",
        content: "Derives emergent gauge coupling constants, showing they are governed by pure integer-based graph adjacency coefficients."
      },
      {
        title: "8.6 Mass Generation",
        content: "Models the mass generation mechanism, deriving particle masses from localized vacuum rewrite backreactions."
      }
    ],
    specialists: [
      {
        area: "For High Energy Theorists",
        text: "The commutativity of distant swap operations aligns with Cartan Subalgebras, deriving the exact Gell-Mann basis from topological invariants."
      },
      {
        area: "For Gauge Theorists",
        text: "Coordinate-free ribbon swaps generate local gauge transformations, deriving electroweak and strong forces from topological preservation rules."
      },
      {
        area: "For Lie Algebra Specialists",
        text: "The commutator structure of localized braid swap generators constructs the exact Lie algebra of the Standard Model gauge groups."
      }
    ],
    analogy: "Untangling headphones by shifting strands around. Even if you swap adjacent wires, the underlying knot's configuration remains identical, explaining why the forces of nature look the same under shifts.",
    link: "/monograph/players/braids/8.1",
    style: "C",
    image: {
      src: "/img/braid_crossing_invariants.png",
      alt: "Figure 2.4: Topological Braid Invariants",
      description: "This high-fidelity scientific plate illustrates how a 3-strand tripartite braid with labeled crossing operations (s1, s2) generates electric charge and spin from topological invariants.",
      math: "Q = \\frac{1}{3} (w_1 + w_2 + w_3) \\quad J = \\frac{1}{2}"
    },
    definitions: [
      {
        term: "Gauge Symmetries",
        definition: "Symmetries that emerge from the relational coordinate transitions of ribbon swaps, unifying forces and matter."
      },
      {
        term: "Ribbon Swaps",
        definition: "Localized exchange operations of adjacent network edges that correspond to standard gauge bosons (photons, gluons)."
      }
    ],
    historicalCallout: {
      title: "Weyl's Gauge Principle",
      text: "Hermann Weyl introduced gauge theory by proposing that physics must be invariant under local coordinate scale adjustments. QBD resolves this discrete-wise: gauge fields are not continuous connections, but local edge-swapping topological invariants."
    }
  },
  {
    num: 9,
    part: "Part II: Topological Nature of Matter (The Players)",
    title: "Generations and Decay",
    taxonomy: "Unification",
    status: "Theoretical Model",
    leanProofs: 0,
    pythonSims: 4,
    executiveEvaluation: "Derives the three generations of matter and explains decay paths as discrete rewrite operations under strict conservation laws.",
    breakdowns: [
      {
        title: "9.1 Necessity of Unification",
        content: "Demonstrates the mathematical necessity of grand unification, mapping forces and particles to a single braid group."
      },
      {
        title: "9.2 Penta-Ribbon Braid",
        content: "Constructs the penta-ribbon braid model, unifying leptons and quarks into a single topological object."
      },
      {
        title: "9.3 Origin of Generations",
        content: "Explains the origin of the three generations of matter from the discrete topological boundaries of B3 braid configurations."
      },
      {
        title: "9.4 Leptoquark Dynamics",
        content: "Models leptoquark dynamics as transition states that mediate proton decay under topological writhe conservation."
      },
      {
        title: "9.5 Proton Decay",
        content: "Calculates the proton lifetime boundary, proving that baryon number conservation is protected by high topological barriers."
      },
      {
        title: "9.6 Neutrino Mass",
        content: "Derives neutrino masses and oscillation profiles from the non-local swapping of Majorana-like ribbon endings."
      }
    ],
    specialists: [
      {
        area: "For Knot Theorists",
        text: "Decay rates are calculated from the topological complexity gradients of the braid transitions, matching the experimental Standard Model parameters."
      },
      {
        area: "For Mathematical Physicists",
        text: "Chiral braid swap decay channels are computed relationally, providing an elegant topological resolution to baryogenesis and primordial abundance anomalies."
      },
      {
        area: "For High Energy Phenomenologists",
        text: "The transition probability between stable twist states explains the exact hierarchy of particle generations and decay lifetimes."
      }
    ],
    analogy: "A system of three stable knots of increasing complexity. The most complex knot (Generation 3) eventually untwists and decays step-by-step into the simplest, most stable knot (Generation 1).",
    link: "/monograph/players/unification/9.1",
    style: "D",
    definitions: [
      {
        term: "Matter Generations",
        definition: "The three distinct families of elementary particles (e.g. electron, muon, tau) emerging from the topological limits of B3 braid twisting."
      },
      {
        term: "Knot Simplification",
        definition: "The process by which an unstable braid twisted state decays systematically into a lower-energy stable configuration."
      }
    ],
    historicalCallout: {
      title: "Gell-Mann's Eightfold Path",
      text: "Murray Gell-Mann classified particles into families using SU(3) flavor symmetry. QBD derives this hierarchy naturally: the three generations correspond to the topological bounds of twisting 3-strand knots in a trivalent graph."
    }
  },
  {
    num: 10,
    part: "Part II: Topological Nature of Matter (The Players)",
    title: "Quantum Universality",
    taxonomy: "Computation",
    status: "Theoretical Model",
    leanProofs: 0,
    pythonSims: 6,
    executiveEvaluation: "Proves that braid interactions constitute a computationally universal set of gates, formalizing the vacuum as a fault-tolerant quantum computer.",
    breakdowns: [
      {
        title: "10.1 Topological Qubit Structure",
        content: "Constructs the topological qubit structure, mapping quantum information to the non-local braid configurations."
      },
      {
        title: "10.10 Formal Synthesis",
        content: "Formulates the mathematical models and pre-geometric causal posets of Quantum Braid Dynamics."
      },
      {
        title: "10.2 Braid Code Consistency",
        content: "Establishes braid code consistency, proving that comonadic updates behave like logical gates on the codespace."
      },
      {
        title: "10.3 Topological Fault Tolerance",
        content: "Develops the fault-tolerance framework, showing that topological quantum error correction protects states from random edge decay."
      },
      {
        title: "10.4 Logical X-Gate",
        content: "Implements the logical X-gate as a specific braid strand swap operation on the codespace."
      },
      {
        title: "10.5 Logical Z-Gate",
        content: "Implements the logical Z-gate as a phase-shifting ribbon twist on the codespace."
      },
      {
        title: "10.6 Hadamard Gate",
        content: "Constructs the Hadamard gate as a composite sequence of tripartite swaps, mapping spin directions."
      },
      {
        title: "10.7 Controlled-Z Gate",
        content: "Constructs the Controlled-Z gate as a topological linking operation between two adjacent braids."
      },
      {
        title: "10.8 T-Gate",
        content: "Implements the T-gate, completing the Clifford set by introducing non-Clifford topological rotations."
      }
    ],
    specialists: [
      {
        area: "For Quantum Computing Researchers",
        text: "Braid twist dynamics map directly to stabilizer code syndrome measurements, formalizing the vacuum as a self-correcting quantum processor."
      },
      {
        area: "For Fault-Tolerant System Architects",
        text: "Fault-tolerant stabilizer checks protect logical qubits from phase-slip errors during universal swap operations."
      },
      {
        area: "For Complexity Theorists",
        text: "The tripartite braid swap network is proven to be universal, demonstrating that the pre-geometric vacuum can simulate any quantum circuit."
      }
    ],
    analogy: "An enormous loom weaving a tapestry. By twisting and swapping threads in specific sequences, the loom can perform any calculation, meaning space itself acts as a massive quantum computer.",
    link: "/monograph/players/computation/10.1",
    style: "E",
    sandbox: "braid",
    definitions: [
      {
        term: "Stabilizer Codes",
        definition: "Fault-tolerant quantum error-correcting codes embedded intrinsically in the vacuum adjacency to protect data states."
      },
      {
        term: "Universal Gate Set",
        definition: "A complete set of logical operations (like swaps and twists) capable of executing any quantum computation in empty space."
      }
    ],
    historicalCallout: {
      title: "Shor's Stabilizer Codes",
      text: "Peter Shor proved quantum computing is possible in noisy systems using stabilizer quantum error correction. QBD shows that vacuum stability is protected by stabilizer codes embedded intrinsically in the space-generating poset."
    }
  }
];

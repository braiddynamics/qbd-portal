import { ChapterData } from '../../types';

export const part3Chapters: ChapterData[] = [
  {
    num: 11,
    part: "Part III: Emergent Reality (The Stage)",
    title: "Differential Geometry",
    taxonomy: "Discrete",
    status: "Theoretical Model",
    leanProofs: 1,
    pythonSims: 5,
    executiveEvaluation: "Defines discrete analogues of differential forms, connections, and curvatures directly on coordinate-free relational network graphs.",
    breakdowns: [
      {
        title: "11.1 Theorem: The Continuum Limit",
        content: "Formulates discrete exterior calculus on graphs, defining discrete differential forms and exterior derivatives that satisfy $d^2 = 0$."
      },
      {
        title: "11.2 Causal Geometry Construction",
        content: "Constructs curved causal geometry on posets, deriving a coordinate-free Riemannian curvature tensor analogue from path metrics."
      },
      {
        title: "11.3 Monotonicity Theorem",
        content: "Proves the Monotonicity Theorem, showing that parallel transport along causal loops preserves topological invariants."
      }
    ],
    specialists: [
      {
        area: "For Differential Geometers",
        text: "The discrete exterior derivative satisfies the boundary of a boundary is zero strictly on relational posets, guaranteeing topological invariance at all scales."
      },
      {
        area: "For Discrete Calculus Experts",
        text: "Discrete exterior calculus forms a metric-free basis for field equations, ensuring complete coordinate independence."
      },
      {
        area: "For Geometric Topologists",
        text: "Causal Ollivier-Ricci curvature bounds the discrete connection, linking localized 3-cycles directly to spatial geometry."
      }
    ],
    analogy: "Navigating a city using only block-by-block directions (turn left, turn right) instead of GPS coordinates. You can still calculate curvature and distance purely by measuring the mismatch when you walk in a circle.",
    link: "/monograph/stage/discrete/11.1",
    style: "A",
    definitions: [
      {
        term: "Discrete Exterior Calculus",
        definition: "A coordinate-free method of performing calculus directly on the network nodes and edges without continuous charts."
      },
      {
        term: "Parallel Transport",
        definition: "The systematic moving of a relational vector along a closed loop of the graph, which measures localized curvature."
      }
    ],
    historicalCallout: {
      title: "Gauss's Theorema Egregium",
      text: "Carl Friedrich Gauss proved that curvature is intrinsic to a surface, measurable without reference to an embedding container. QBD formalizes this on graphs: curvature is computed purely from local path metrics inside the discrete network."
    }
  },
  {
    num: 12,
    part: "Part III: Emergent Reality (The Stage)",
    title: "Discrete Field Equations",
    taxonomy: "Einstein",
    status: "Theoretical Model",
    leanProofs: 0,
    pythonSims: 3,
    executiveEvaluation: "Gravity is derived as an emergent thermodynamic hydrodynamic equation of state from the causal network updates, bypassing continuous coordinate charts.",
    breakdowns: [
      {
        title: "12.1 Discrete Stress-Energy",
        content: "Defines the discrete stress-energy tensor on graphs, mapping mass-energy to localized edge-update density perturbations."
      },
      {
        title: "12.2 Discrete Field Equations",
        content: "Formulates the discrete Einstein Field Equations, deriving gravity as a thermodynamic equation of state of the network."
      },
      {
        title: "12.3 Geometric Conservation",
        content: "Establishes the geometric conservation law, proving that the discrete Bianchi identity is satisfied strictly by the poset."
      }
    ],
    specialists: [
      {
        area: "For Relativists & Cosmology Experts",
        text: "Curvature emerges as a thermodynamic pressure balance, bridging Jacobson's thermodynamics of spacetime with discrete network models."
      },
      {
        area: "For Gravitational Theorists",
        text: "The discrete stress-energy tensor is derived from the probability flux of network updates, sourcing emergent gravity relationally."
      },
      {
        area: "For Einstein Equation Researchers",
        text: "Stationary action constraints on the discrete event poset enforce the exact balance of curvature and information flux."
      }
    ],
    analogy: "A heavy bowling ball resting on a trampoline. A knot (matter) in the network forces adjacent threads to stretch and crowd together, which nearby knots naturally roll toward, creating gravity.",
    link: "/monograph/stage/einstein/12.1",
    style: "B",
    definitions: [
      {
        term: "Stress-Energy Equivalent",
        definition: "The localized update density perturbations on the lattice, which couples directly to emergent gravity."
      },
      {
        term: "Thermodynamic Gravity",
        definition: "The description of gravity not as a fundamental mechanical force, but as an emergent thermodynamic equation of state."
      }
    ],
    historicalCallout: {
      title: "Jacobson's Thermal Gravity",
      text: "In 1995, Ted Jacobson derived Einstein's field equations as a thermodynamic equation of state of a horizon. QBD implements this on networks: gravity emerges as a macroscopic thermal balance of discrete graph rewrites."
    }
  },
  {
    num: 13,
    part: "Part III: Emergent Reality (The Stage)",
    title: "Continuum Limit",
    taxonomy: "Convergence",
    status: "Theoretical Model",
    leanProofs: 0,
    pythonSims: 5,
    executiveEvaluation: "Proves that the discrete causal network sequence converges mathematically to a smooth, curved Lorentzian spacetime manifold under the Gromov-Hausdorff-Prokhorov metric.",
    breakdowns: [
      {
        title: "13.1 Riemannian Convergence",
        content: "Proves that the sequence of discrete graphs converges strictly to a smooth Riemannian manifold under the Gromov-Hausdorff-Prokhorov metric."
      },
      {
        title: "13.2 Tensorial Reorganization",
        content: "Develops the coarse-graining framework, showing how micro-updates group into macroscopic tensor fields."
      },
      {
        title: "13.3 Causal Geometry",
        content: "Validates that emergent causal geometry satisfies classical general relativity in the thermodynamic limit."
      }
    ],
    specialists: [
      {
        area: "For Mathematical Physicists",
        text: "Convergence is bounded under the Gromov-Hausdorff-Prokhorov metric, establishing the first formal proof of smooth spacetime emergence from causal networks."
      },
      {
        area: "For Spectral Geometers",
        text: "The eigenvalues of the discrete graph Laplacian converge to the Laplace-Beltrami spectrum, proving that smooth metric manifolds emerge in the continuum limit."
      },
      {
        area: "For Analysis Experts",
        text: "Wasserstein transport metrics regulate probability distribution limits, preventing dimensional collapse during scaling."
      }
    ],
    analogy: "A digital photo. Zoomed in close, it is a grid of distinct, square pixels (discrete graph). Zoomed out, the pixels merge seamlessly into a smooth, continuous, curved image (classical spacetime).",
    link: "/monograph/stage/convergence/13.1",
    style: "C",
    image: {
      src: "/img/manifold_convergence.png",
      alt: "Figure 3.2: Discrete Graph Lorentzian Manifold Convergence",
      description: "This high-resolution scientific diagram illustrates a dense lattice of causal sets (DAG) smoothly converging into a warped 3D gravitational grid representing curved Lorentzian spacetime.",
      math: "d_{GHP}(G_n, \\mathcal{M}) \\rightarrow 0 \\quad \\text{as } n \\rightarrow \\infty"
    },
    definitions: [
      {
        term: "GHP Metric Convergence",
        definition: "A rigorous mathematical metric proving that discrete networks converge strictly to smooth Riemannian manifolds as events grow large."
      },
      {
        term: "Spectral Dimension",
        definition: "The effective dimension of space as measured by diffusion processes, which stabilizes at exactly 4 in the macroscopic limit."
      }
    ],
    historicalCallout: {
      title: "Hausdorff's Metric Topology",
      text: "Felix Hausdorff formalized the math of metric spaces and topological dimension. QBD uses Mikhail Gromov's generalization (Gromov-Hausdorff metric) to prove that discrete graph meshes converge strictly to smooth 4D containers."
    }
  },
  {
    num: 14,
    part: "Part III: Emergent Reality (The Stage)",
    title: "Lorentzian Reality",
    taxonomy: "Time",
    status: "Theoretical Model",
    leanProofs: 1,
    pythonSims: 5,
    executiveEvaluation: "Reconciles logical rewrite causality with observed continuous physical time, deriving a $(3+1)$-dimensional Lorentzian spacetime signature from event irreflexivity.",
    breakdowns: [
      {
        title: "14.1 Time Recovery",
        content: "Reconstructs physical continuous time, proving that observer frames are emergent foliations of the global poset."
      },
      {
        title: "14.2 Metric & Motion",
        content: "Derives the relativistic metric and equations of motion, showing that geodesics correspond to maximum logical-time paths."
      },
      {
        title: "14.3 Section: Field Axiomatics",
        content: "Lays down the field axiomatics for continuous matter, mapping quantum fields to discrete network stress densities."
      },
      {
        title: "14.4 Section: Gravity from Entanglement Thermodynamics",
        content: "Derives general relativity from entanglement thermodynamics, bridging poset dynamics with Jacobson's gravity."
      },
      {
        title: "14.5 Theorem: The Continuum Limit",
        content: "Proves that the macroscopic continuum limit of the causal set reproduces curved Lorentzian spacetime."
      }
    ],
    specialists: [
      {
        area: "For Relativists & Quantum Cosmologists",
        text: "Observer frame transitions commute with global logical sequencer steps, proving the compatibility of local covariance with a global clock."
      },
      {
        area: "For Temporal Geometers",
        text: "The lapse function is derived from localized event density, recovering gravitational time dilation from pure logical update rates."
      },
      {
        area: "For Lorentzian Physicists",
        text: "Chiral event posets break the local rotational symmetry, dynamically generating the Lorentzian signature from directional network flow."
      }
    ],
    analogy: "Raindrops falling on a pond. The ripples expand outwards as circles (lightcones). Events can only affect things inside their expanding ripples, establishing past, present, and future.",
    link: "/monograph/stage/time/14.1",
    style: "D",
    definitions: [
      {
        term: "Time Foliation",
        definition: "The process by which observers group events into sequential spatial slices, creating the illusion of continuous time."
      },
      {
        term: "Maximum Path Geodesic",
        definition: "The trajectory of maximum logical time steps through the poset, which recovers classical relativistic equations of motion."
      }
    ],
    historicalCallout: {
      title: "Minkowski's Causal Spacetime",
      text: "Hermann Minkowski unified space and time by showing that spatial coordinate systems are relative, but causal intervals are absolute. QBD implements Minkowski's insight: Lorentzian time emerges from maximum path computations."
    }
  },
  {
    num: 15,
    part: "Part III: Emergent Reality (The Stage)",
    title: "Geometry of Entanglement",
    taxonomy: "EPR",
    status: "Theoretical Model",
    leanProofs: 0,
    pythonSims: 3,
    executiveEvaluation: "Quantum entanglement is shown to mathematically generate spatial connectivity, formalizing the ER = EPR conjecture as microscopic topological wormhole connections.",
    breakdowns: [
      {
        title: "15.1 Entanglement as Topological Connection",
        content: "Formulates quantum entanglement as dynamic topological edge connections in the pre-geometric poset."
      },
      {
        title: "15.2 Bell Violation",
        content: "Proves that discrete entanglement connections reproduce Bell inequality violations without non-local coordinate assumptions."
      },
      {
        title: "15.3 ER = EPR (Topological Wormholes)",
        content: "Formulates the ER = EPR conjecture on graphs, proving that entangled event clusters are connected by topological wormholes."
      },
      {
        title: "15.4 Quantum Eraser (Temporal Non-Locality)",
        content: "Models the quantum eraser effect, explaining temporal non-locality as a consequence of post-selected poset paths."
      }
    ],
    specialists: [
      {
        area: "For Quantum Information Theorists",
        text: "Entanglement entropy scales directly with the boundary cut-set of the causal set, deriving the Area Law from discrete graph bounds."
      },
      {
        area: "For Gravitational Physicists",
        text: "Entanglement connections act as physical wormhole bridges, providing a discrete, pre-geometric mechanism for the ER equals EPR conjecture."
      },
      {
        area: "For Quantum Cosmology Researchers",
        text: "The bi-metric distance structure separates topological communication channels from the emergent bulk metric."
      }
    ],
    analogy: "Two tin cans connected by a taut string. Even if the cans are placed on opposite sides of a room, a whisper travels instantly along the string, bypassing the spatial distance between them.",
    link: "/monograph/stage/epr/15.1",
    style: "E",
    sandbox: "curvature",
    definitions: [
      {
        term: "Entanglement Edge",
        definition: "A non-local connection edge established relationally between two event clusters, proving that spatial distance is an entanglement property."
      },
      {
        term: "ER = EPR Wormhole",
        definition: "The equivalence proving that quantum entanglement generates microscopic wormholes, bridging general relativity and quantum information."
      }
    ],
    historicalCallout: {
      title: "Wheeler's Quantum Foam",
      text: "John Wheeler envisioned Planck-scale gravity as a chaotic, bubbling quantum foam of wormholes. QBD formalizes this: entanglement acts as wormhole pathways that dynamically alter the graph metrics of emergent space."
    }
  },
  {
    num: 16,
    part: "Part III: Emergent Reality (The Stage)",
    title: "Isomorphism Principle",
    taxonomy: "Holography",
    status: "Theoretical Model",
    leanProofs: 1,
    pythonSims: 2,
    executiveEvaluation: "Establishes a holographic boundary-to-bulk isomorphism, proving n-dimensional bulk gravity is isomorphic to $(n-1)$-dimensional boundary stabilizer codes.",
    breakdowns: [
      {
        title: "16.1 Surface Code (Discrete Holography)",
        content: "Formulates discrete holography, proving that bulk poset gravity is isomorphic to boundary surface stabilizer codes."
      },
      {
        title: "16.2 Bekenstein Bound (Thermodynamic Limits)",
        content: "Derives the Bekenstein entropy bound, proving that boundary information capacities constrain bulk geometry."
      }
    ],
    specialists: [
      {
        area: "For Holographic Physicists",
        text: "Holographic mapping is formalized algebraically without relying on continuous smooth boundaries, providing a discrete origin for the AdS/CFT correspondence."
      },
      {
        area: "For Quantum Gravity Theorists",
        text: "The bulk-boundary dictionary is constructed as a quantum error-correcting code over causal tensor networks."
      },
      {
        area: "For Mathematical Physicists",
        text: "Boundary conformal field theories map isomorphically to bulk stabilizer codes, verifying the holographic principle."
      }
    ],
    analogy: "A 3D hologram projected from a flat 2D film. Everything happening in the 3D volume of space is actually a projection of the complex information encoded on the outer 2D boundary.",
    link: "/monograph/stage/holography/16.1",
    style: "A",
    definitions: [
      {
        term: "Boundary-Bulk Duality",
        definition: "The exact algebraic isomorphism mapping n-dimensional bulk network gravity onto (n-1)-dimensional boundary stabilizer codes."
      },
      {
        term: "Surface Codespace",
        definition: "The redundant boundary error-correcting codespace protecting bulk metric connectivity from local information losses."
      }
    ],
    historicalCallout: {
      title: "Bekenstein's Holographic Limit",
      text: "Jacob Bekenstein discovered that the maximum entropy of a volume is bounded by its boundary area, not its volume. QBD mathematically derives this limit: bulk graph configurations are strictly isomorphic to boundary error-correcting codes."
    }
  },
  {
    num: 17,
    part: "Part III: Emergent Reality (The Stage)",
    title: "String Limit",
    taxonomy: "Worldsheets",
    status: "Theoretical Model",
    leanProofs: 0,
    pythonSims: 5,
    executiveEvaluation: "Shows that emergent 1D braided strings sweep out 2D worldsheet manifolds in the continuum limit, bridging QBD with Nambu-Goto string action approximations.",
    breakdowns: [
      {
        title: "17.1 Discrete Worldsheet (Braid Isomorphism)",
        content: "Shows that emergent 1D braided strings sweep out 2D worldsheet manifolds in the continuous limit."
      },
      {
        title: "17.2 T-Duality and Spectrum",
        content: "Derives T-duality and compactification spectra from the discrete topological boundaries of compactified graph dimensions."
      },
      {
        title: "17.3 Critical Dimension (D=26)",
        content: "Calculates the critical dimension ($D=26$) strictly from the anomaly-free partition functions of discrete worldsheets."
      },
      {
        title: "17.4 Heterotic Unification (E8 x E8)",
        content: "Models heterotic unification ($E_8 \times E_8$) as symmetric swap configurations of twenty-six dimensional lattices."
      }
    ],
    specialists: [
      {
        area: "For String Theorists",
        text: "Virasoro constraints and compactification dualities are derived as macroscopic limits of topological network constraints."
      },
      {
        area: "For High Energy Physicists",
        text: "2D worldsheet dynamics emerge as the collective phase attractor of intersecting 3-strand braid histories."
      },
      {
        area: "For Mathematical Physicists",
        text: "Compactified dimensions arise naturally from the localized modular symmetries of the underlying poset."
      }
    ],
    analogy: "A vibrating guitar string. As a knotted braid propagates through the network, its motion forms a 2D ribbon surface, exactly matching the mathematics of strings moving through spacetime.",
    link: "/monograph/stage/worldsheets/17.1",
    style: "B",
    definitions: [
      {
        term: "Worldsheet",
        definition: "The 2D area swept out by a 1D braided string moving in logical time, approximating classical string action."
      },
      {
        term: "T-Duality",
        definition: "The topological equivalence between strings compactified on different graph radii, preserving the physical spectrum."
      }
    ],
    historicalCallout: {
      title: "The Nambu-Goto Action",
      text: "Yoichiro Nambu and Tetsuo Goto modeled strings as 1D objects sweeping out 2D areas in spacetime. QBD retrieves this action as an emergent limit of tripartite braids propagating within coordinate-free causal lattices."
    }
  }
];

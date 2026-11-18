export interface PaperLink {
  label: string;
  href: string;
  isDownload?: boolean;
  isExternal?: boolean;
  icon?: string;
  size?: string;
}

export interface CompanionAsset {
  id: string;
  name: string;
  type: 'code' | 'proof' | 'dataset' | 'bundle' | 'simulation';
  typeLabel: string;
  description: string;
  href: string;
  isDownload?: boolean;
  isExternal?: boolean;
  icon?: string;
  badge?: string;
  size?: string;
}

export interface PaperRecord {
  id: string;
  slug: string;
  title: string;
  shortTitle?: string;
  type: 'preprint' | 'working-paper' | 'comment';
  typeLabel: string;
  version?: string;
  date: string;
  dateISO: string;
  isOpenAccess: boolean;
  licenseLabel: string;
  authors: string;
  orcid?: string;
  abstract?: string;
  subMeta: string;
  category: string;
  verifiedBadges?: string[];
  primaryLinks: PaperLink[];
  companionAssets?: CompanionAsset[];
  bibtex?: string;
  doiUrl?: string;
}

export const papers: PaperRecord[] = [
  {
    id: 'geometric-unity',
    slug: '/papers/geometric-unity',
    type: 'preprint',
    typeLabel: 'Technical Note',
    date: 'November 17, 2026',
    dateISO: '2026-11-17',
    isOpenAccess: true,
    licenseLabel: 'Text: CC BY 4.0 · Software: MIT',
    doiUrl: 'https://doi.org/10.5281/zenodo.24325062',
    title: 'Clifford Contractions and the First-Order Bosonic Action in Geometric Unity',
    shortTitle: 'Geometric Unity: Clifford Contractions and the First-Order Action',
    authors: 'R. Fisher',
    orcid: '0009-0006-2441-3282',
    category: 'Mathematical Physics & Differential Geometry',
    subMeta: 'Technical Note · Braid Dynamics Applied Research Group · Mathematical Physics & Differential Geometry',
    abstract: "We examine the Clifford-algebra contractions and variational structure of the bosonic sector in Eric Weinstein's 2021 working draft of Geometric Unity. We classify equivariant curvature contractions, identify one that recovers the Einstein tensor in the Levi-Civita limit, and derive the associated covariant divergence identities. Unconstrained variation of a corresponding first-order action produces an additional quadratic term in the augmented torsion. An explicit Clifford-algebra example and finite-difference tests show that this term can be nonzero. We compare the reconstructed action and operator with the printed equations under stated bracket and coefficient conventions.",
    verifiedBadges: [
      'Lean 4 Formalizations (40 Source Files)',
      'Python Clifford-Algebra and Variation Checks',
      'Complete Markdown Supplement & Source Archive',
    ],
    primaryLinks: [
      { label: 'Read Online', href: '/papers/geometric-unity', icon: '📖' },
      { label: 'DOI / Zenodo', href: 'https://doi.org/10.5281/zenodo.24325062', isExternal: true },
      { label: 'PDF', href: 'pathname:///papers/geometric-unity/downloads/fisher-geometric-unity-2026-11-17.pdf', isDownload: true, icon: '📄', size: '218 KB' },
      { label: 'Markdown', href: 'pathname:///papers/geometric-unity/downloads/fisher-geometric-unity-2026-11-17.md', isDownload: true, icon: '📝', size: '90 KB' },
      { label: 'Computational Supplement (MD)', href: 'pathname:///papers/geometric-unity/downloads/fisher-geometric-unity-2026-11-17-computational-supplement.md', isDownload: true, icon: '📋', size: '862 KB' },
      { label: 'Code Guide', href: '/papers/geometric-unity/code-guide', icon: '📑' },
      { label: 'Source Archive (ZIP)', href: 'pathname:///papers/geometric-unity/downloads/fisher-geometric-unity-2026-11-17-code.zip', isDownload: true, icon: '📦', size: '225 KB' },
    ],
    companionAssets: [
      {
        id: 'gu-computational-supplement',
        name: 'Computational Supplement (Complete Markdown Source)',
        type: 'proof',
        typeLabel: 'Computational Supplement',
        description: 'All 40 Lean files, the Python verification program, and three project configuration files, with a linked index and a summary for every source listing.',
        href: 'pathname:///papers/geometric-unity/downloads/fisher-geometric-unity-2026-11-17-computational-supplement.md',
        isDownload: true,
        icon: '📋',
        size: '862 KB',
      },
      {
        id: 'gu-code-guide',
        name: 'Code Guide: Coverage, File Descriptions, and Execution Instructions',
        type: 'proof',
        typeLabel: 'Code Guide',
        description: 'Descriptions of every source file, the scope and assumptions of the formalizations, Lean and Python execution instructions, and benchmark results. Available online and as PDF and Markdown.',
        href: '/papers/geometric-unity/code-guide',
        icon: '📑',
      },
      {
        id: 'gu-code-archive',
        name: 'GU Verification Source Archive (ZIP)',
        type: 'bundle',
        typeLabel: 'Source Archive',
        description: 'Extractable Lean and Python sources, pinned Lean 4.33.1 and Mathlib configuration, SHA256SUMS, a publication README, and full CC BY 4.0 and MIT license terms. The code guide explains dependency installation and execution.',
        href: 'pathname:///papers/geometric-unity/downloads/fisher-geometric-unity-2026-11-17-code.zip',
        isDownload: true,
        icon: '📦',
        size: '225 KB',
      },
    ],
    bibtex: `@article{fisher2026geometricunity,
  title={Clifford Contractions and the First-Order Bosonic Action in Geometric Unity},
  author={Fisher, R.},
  journal={Braid Dynamics Research Archive},
  year={2026},
  month={November},
  day={17},
  doi={10.5281/zenodo.24325062},
  url={https://braiddynamics.com/papers/geometric-unity}
}`,
  },
  {
    id: 'vacuum-phase',
    slug: '/papers/vacuum-phase',
    type: 'preprint',
    typeLabel: 'Preprint / Research Article',
    version: 'v1.0.0',
    date: 'August 24, 2026',
    dateISO: '2026-08-24',
    isOpenAccess: true,
    licenseLabel: 'CC BY 4.0',
    title: 'Constrained Stochastic Rewrite System on Timestamped DAGs: Vacuum Architecture, Absorbing-State Dynamics, and the Emergence of Causal Geometry',
    shortTitle: 'Vacuum Phase & Causal Geometry',
    authors: 'R. Fisher',
    orcid: '0009-0006-2441-3282',
    category: 'Statistical Mechanics & Discrete Gravity',
    subMeta: 'Category: Statistical Mechanics & Discrete Gravity',
    abstract: 'We present a computational framework based on a discrete causal substrate governed by a dual logical-physical time architecture, irreflexivity, and acyclicity. The unperturbed vacuum is uniquely deduced as a regular Bethe fragment possessing bipartite pre-geometric symmetry, where a localized parity-breaking instanton triggers an initial parallel burst that nucleates geometry. Axiomatic constraints are represented as commuting occupancy projectors on directed-edge configurations, so accepted rewrites remain inside the kinematically allowed set. Dynamic evolution on timestamped directed acyclic graphs is driven by a comonadic self-observation and stochastic rewrite constructor operating under information-theoretic principles. Rapid single-cycle decay and boundary leaf dissipation establish an analytical nucleation barrier, while multi-scale simulations from N = 10 to 10,000 demonstrate that boundary quenching diminishes with volume to sustain a stable quasi-stationary active phase. Together, these results establish the discrete non-equilibrium statistical mechanics of the causal vacuum, providing the foundational substrate and scaling hypotheses required for continuum geometric reconstruction.',
    verifiedBadges: [
      'Preprint / Research Article',
      '48 Active Lean 4 Theorems (61 Declarations, 0 Axioms)',
      '25 Dedicated Pytest Checks (8 Modules)',
      'Full Non-Equilibrium Phase Diagram & Replication Bundle'
    ],
    primaryLinks: [
      { label: 'Read Online', href: '/papers/vacuum-phase', icon: '📖' },
      { label: 'PDF', href: 'pathname:///papers/vacuum-phase/downloads/vacuum-phase.pdf', isDownload: true, icon: '📄', size: '852 KB' },
      { label: 'Markdown', href: 'pathname:///papers/vacuum-phase/downloads/vacuum-phase.md', isDownload: true, icon: '📝', size: '167 KB' },
      { label: 'Supplement (Online)', href: '/papers/vacuum-phase/supplement', icon: '📑' },
      { label: 'Supplement (MD)', href: 'pathname:///papers/vacuum-phase/downloads/vacuum-phase-supplement.md', isDownload: true, icon: '📋', size: '140 KB' }
    ],
    companionAssets: [
      {
        id: 'vacuum-phase-supplement-asset',
        name: 'Technical & Computational Supplement (Appendices A–C)',
        type: 'proof',
        typeLabel: 'Technical Supplement',
        description: 'Complete formal Lean 4 kernel specifications (Appendix A, 48 active verified theorems), C++20 multi-scale simulation engine (Appendix B), and standalone Python reference implementation (Appendix C).',
        href: '/papers/vacuum-phase/supplement',
        icon: '📑',
        badge: 'Online & Downloadable',
        size: '140 KB'
      },
      {
        id: 'vacuum-phase-lean',
        name: 'VacuumPhase.lean (Lean 4 Core Kernel)',
        type: 'proof',
        typeLabel: 'Formal Verification Kernel',
        description: 'Complete 48-theorem machine-checked formal proof suite in Lean 4 Core across 61 declarations with zero unproven axioms (0 sorry).',
        href: 'pathname:///papers/vacuum-phase/code/VacuumPhase.lean',
        isDownload: true,
        icon: '📐',
        badge: '48 Theorems / Lean 4.33.1+',
        size: '52 KB'
      },
      {
        id: 'vacuum-phase-replication-zip',
        name: 'Full Replication Bundle (ZIP)',
        type: 'bundle',
        typeLabel: 'Replication Archive',
        description: 'Self-contained replication package including C++20 multithreaded simulation engine, Python engine, Makefile, and multi-scale datasets (N=10 to 10,000).',
        href: 'pathname:///papers/vacuum-phase/downloads/vacuum-phase-replication.zip',
        isDownload: true,
        icon: '📦',
        badge: '49 KB ZIP',
        size: '49 KB'
      },
      {
        id: 'vacuum-phase-dataset',
        name: 'Multi-Scale Production Trajectories (N = 10 to 10,000 CSV)',
        type: 'dataset',
        typeLabel: 'Monte Carlo Dataset',
        description: 'Raw simulation records across four orders of magnitude (N = 10, 100, 1,000, 10,000) at the canonical prior (μ₀ = 1/√2π, λ₀ = e - 1).',
        href: 'pathname:///papers/vacuum-phase/data/p_surv_N10000_cpp_production.csv',
        isDownload: true,
        icon: '📊',
        badge: 'CSV (Pandas-ready)'
      }
    ],
    bibtex: `@article{fisher2026vacuumphase,
  title={Constrained Stochastic Rewrite System on Timestamped DAGs: Vacuum Architecture, Absorbing-State Dynamics, and the Emergence of Causal Geometry},
  author={Fisher, R.},
  journal={Quantum Braid Dynamics Research Archive},
  year={2026},
  url={https://braiddynamics.com/papers/vacuum-phase}
}`
  },
  {
    id: 'causal-invariance-hypergraphs',
    slug: '/papers/causal-invariance-hypergraphs',
    type: 'preprint',
    typeLabel: 'Preprint / Research Article',
    version: 'v1.0.0',
    date: 'July 27, 2026',
    dateISO: '2026-07-27',
    isOpenAccess: true,
    licenseLabel: 'CC BY 4.0',
    title: 'Information-Theoretic Constraints on Finite-Time Causal Invariance and Pre-Geometric Dimensional Reduction in Discrete Hypergraph Models',
    shortTitle: 'Causal Invariance & Landauer Limits',
    authors: 'R. Fisher',
    orcid: '0009-0006-2441-3282',
    category: 'Discrete Physics & Quantum Information',
    subMeta: 'Category: Discrete Physics & Quantum Information',
    verifiedBadges: [
      'Machine-Checked Lean 4 Proof Suite (0 Axioms)',
      '28 Dedicated Pytest Checks (Simulation & Spectra)',
      'First Law Entanglement & Lovász Graph Limits'
    ],
    primaryLinks: [
      { label: 'Read Online', href: '/papers/causal-invariance-hypergraphs', icon: '📖' },
      { label: 'PDF', href: 'pathname:///papers/causal-invariance-hypergraphs/downloads/causal-invariance-hypergraphs.pdf', isDownload: true, icon: '📄', size: '908 KB' },
      { label: 'Markdown', href: 'pathname:///papers/causal-invariance-hypergraphs/downloads/causal-invariance-hypergraphs.md', isDownload: true, icon: '📝', size: '95 KB' }
    ],
    companionAssets: [
      {
        id: 'causal-invariance-lean',
        name: 'CausalInvariance.lean (Lean 4 Formal Proofs)',
        type: 'proof',
        typeLabel: 'Formal Verification Kernel',
        description: 'Complete machine-checked Lean 4 formal proofs of ARS confluence and causal DAG poset independence (0 sorry, 0 axioms).',
        href: 'pathname:///papers/causal-invariance-hypergraphs/code/CausalInvariance.lean',
        isDownload: true,
        icon: '📐',
        badge: '0 Axioms / Lean 4.33.1+'
      },
      {
        id: 'causal-invariance-simulation',
        name: 'simulation.py (Dual-Mode Simulation Engine)',
        type: 'simulation',
        typeLabel: 'Python Simulation Suite',
        description: 'Exact multiway graph canonicalization, Lovász homomorphism density evaluators, spectral moment computers, and Wolfram hypergraph auditors.',
        href: 'pathname:///papers/causal-invariance-hypergraphs/simulations/simulation.py',
        isDownload: true,
        icon: '🐍',
        badge: 'Python 3.8+'
      },
      {
        id: 'causal-invariance-replication-zip',
        name: 'Full Replication Bundle (ZIP)',
        type: 'bundle',
        typeLabel: 'Replication Archive',
        description: 'Complete replication package including simulation engine, 28 unit tests, Lean 4 kernel, generated figures, and README.',
        href: 'pathname:///papers/causal-invariance-hypergraphs/downloads/causal-invariance-replication.zip',
        isDownload: true,
        icon: '📦',
        badge: '590 KB ZIP',
        size: '590 KB'
      }
    ],
    bibtex: `@article{fisher2026causalinvariance,
  title={Information-Theoretic Constraints on Finite-Time Causal Invariance and Pre-Geometric Dimensional Reduction in Discrete Hypergraph Models},
  author={Fisher, R.},
  journal={Quantum Braid Dynamics Research Archive},
  year={2026},
  url={https://braiddynamics.com/papers/causal-invariance-hypergraphs}
}`
  },
  {
    id: 'maximal-entropy-random-walk',
    slug: '/papers/maximal-entropy-random-walk',
    type: 'comment',
    typeLabel: 'Comment / Article',
    version: 'v1.0.0',
    date: 'June 21, 2026',
    dateISO: '2026-06-21',
    isOpenAccess: true,
    licenseLabel: 'CC BY 4.0',
    title: 'Comment on "Localization of the Maximal Entropy Random Walk"',
    shortTitle: 'Maximal Entropy Random Walk Parity Oscillations',
    authors: 'R. Fisher',
    orcid: '0009-0006-2441-3282',
    category: 'Statistical Mechanics & Spectral Graph Theory',
    subMeta: 'Formal Comment on Phys. Rev. Lett. 102, 160602 (2009) · Category: Statistical Mechanics & Spectral Graph Theory',
    verifiedBadges: [
      'Bipartite Spectrum Proof (μ = -1)',
      'Python Verification Simulation & Spectral Analyzer'
    ],
    primaryLinks: [
      { label: 'Read Online', href: '/papers/maximal-entropy-random-walk', icon: '📖' },
      { label: 'PDF', href: 'pathname:///papers/maximal-entropy-random-walk/downloads/maximal-entropy-random-walk.pdf', isDownload: true, icon: '📄', size: '49 KB' },
      { label: 'Markdown', href: 'pathname:///papers/maximal-entropy-random-walk/downloads/maximal-entropy-random-walk.md', isDownload: true, icon: '📝', size: '9 KB' }
    ],
    companionAssets: [
      {
        id: 'merw-simulation-py',
        name: 'maximal_entropy_random_walk_simulation.py',
        type: 'simulation',
        typeLabel: 'Python Verification Simulation',
        description: 'Standalone spectral analysis script demonstrating parity oscillations and lazy-walk convergence on bipartite graphs.',
        href: 'pathname:///papers/maximal-entropy-random-walk/simulations/maximal_entropy_random_walk_simulation.py',
        isDownload: true,
        icon: '🐍',
        badge: 'Python 3.8+'
      }
    ],
    bibtex: `@article{fisher2026merwcomment,
  title={Comment on "Localization of the Maximal Entropy Random Walk"},
  author={Fisher, R.},
  journal={Quantum Braid Dynamics Research Archive},
  year={2026},
  url={https://braiddynamics.com/papers/maximal-entropy-random-walk}
}`
  }
];

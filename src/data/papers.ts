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
  version: string;
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
    id: 'vacuum-phase',
    slug: '/papers/vacuum-phase',
    type: 'preprint',
    typeLabel: 'Preprint / Article',
    version: 'v1.0.0',
    date: 'August 24, 2026',
    dateISO: '2026-08-24',
    isOpenAccess: true,
    licenseLabel: 'CC BY 4.0',
    title: 'A Constrained Stochastic Rewrite System on Timestamped DAGs: Microscopic Rules, Absorbing-State Dynamics, and Finite-N Quasi-Stationary Ensembles',
    shortTitle: 'Vacuum Phase & Quasi-Stationary Distributions',
    authors: 'R. Fisher',
    orcid: '0009-0006-2441-3282',
    category: 'Statistical Mechanics & Discrete Gravity',
    subMeta: 'Category: Statistical Mechanics & Discrete Gravity',
    verifiedBadges: [
      '34 Machine-Checked Lean 4 Theorems (0 Axioms)',
      '25 Dedicated Pytest Checks (8 Modules)'
    ],
    primaryLinks: [
      { label: 'Read Online', href: '/papers/vacuum-phase', icon: '📖' },
      { label: 'PDF', href: 'pathname:///papers/vacuum-phase/downloads/vacuum-phase.pdf', isDownload: true, icon: '📄', size: '1.2 MB' },
      { label: 'Markdown', href: 'pathname:///papers/vacuum-phase/downloads/vacuum-phase.md', isDownload: true, icon: '📝', size: '188 KB' }
    ],
    companionAssets: [
      {
        id: 'vacuum-phase-lean',
        name: 'VacuumPhase.lean (Lean 4 Core Kernel)',
        type: 'proof',
        typeLabel: 'Formal Verification Kernel',
        description: 'Complete 34-theorem machine-checked formal proof suite in Lean 4 Core with zero unproven axioms (0 sorry).',
        href: 'pathname:///papers/vacuum-phase/code/VacuumPhase.lean',
        isDownload: true,
        icon: '📐',
        badge: '0 Axioms / Lean 4.33.1+'
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
        badge: '31 KB ZIP',
        size: '31 KB'
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
  title={A Constrained Stochastic Rewrite System on Timestamped DAGs: Microscopic Rules, Absorbing-State Dynamics, and Finite-$N$ Quasi-Stationary Ensembles},
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
      { label: 'PDF', href: 'pathname:///papers/causal-invariance-hypergraphs/downloads/causal-invariance-hypergraphs.pdf', isDownload: true, icon: '📄', size: '897 KB' },
      { label: 'Markdown', href: 'pathname:///papers/causal-invariance-hypergraphs/downloads/causal-invariance-hypergraphs.md', isDownload: true, icon: '📝', size: '97 KB' }
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
      { label: 'PDF', href: 'pathname:///papers/maximal-entropy-random-walk/downloads/maximal-entropy-random-walk.pdf', isDownload: true, icon: '📄', size: '40 KB' },
      { label: 'Markdown', href: 'pathname:///papers/maximal-entropy-random-walk/downloads/maximal-entropy-random-walk.md', isDownload: true, icon: '📝', size: '8 KB' }
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

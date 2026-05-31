import React from 'react';
import Head from '@docusaurus/Head';
import Layout from '@theme/Layout';

// ─────────────────────────────────────────────────────────────────────────────
// Static data — keep in sync with /src/data/ai-downloads-info.json
// ─────────────────────────────────────────────────────────────────────────────

const SITE_INFO = {
  name: 'Quantum Braid Dynamics (QBD)',
  tagline: 'A background-independent, parameter-free formulation of quantum gravity',
  url: 'https://braiddynamics.com',
  github: 'https://github.com/braiddynamics/qbd-portal',
  contact: 'https://x.com/BraidDynamics',
  license: 'https://braiddynamics.com/legal',
  lastUpdated: '2026-05-31',
};

const DESCRIPTION = `Quantum Braid Dynamics (QBD) is an independent theoretical physics research project
that models the cosmos as a computational process running on a discrete causal network.
The universe is represented as a dynamically evolving graph of braid-topological events,
from which spacetime geometry, matter (fermions and bosons), and gauge symmetries emerge
without free parameters. QBD unifies General Relativity and the Standard Model of particle
physics through topological invariants of braided 3-cycles, connects to the Wolfram Physics
Project, Causal Set Theory, and Causal Dynamical Triangulations, and validates its claims
with formal Lean 4 proofs and Python simulations embedded directly in the monograph text.`;

const QUICK_START = [
  {
    label: 'Downloads index (JSON) — START HERE',
    url: 'https://braiddynamics.com/data/ai-downloads-info.json',
    note: 'Machine-readable catalogue of every available download with byte sizes and token counts. Use this to locate the specific chapter URL(s) you need.',
  },
  {
    label: 'Individual chapter — Markdown pattern',
    url: 'https://braiddynamics.com/downloads/chapters/chapter_N.md',
    note: 'Replace N with chapter number (1–25). This is the recommended unit of analysis. See chapter index below for titles and token counts.',
  },
  {
    label: 'Individual chapter — JSON pattern',
    url: 'https://braiddynamics.com/downloads/chapters/chapter_N.json',
    note: 'Structured JSON version. Better for section-level lookups or equation ID queries.',
  },
  {
    label: 'Download portal (browser / visual agents only)',
    url: 'https://braiddynamics.com/monograph/download',
    note: 'Human-facing interactive page. Download links are rendered inside buttons — not suitable for text-based crawling. Use the JSON catalogue above instead.',
  },
];

const PARTS = [
  {
    number: 1,
    title: 'The Foundational Principles (The Rules)',
    chapters: '1–5',
    tokens: '~310K',
    md: 'https://braiddynamics.com/downloads/parts/qbd_part_1_the_foundational_principles_the_rules.md',
    summary: 'Substrate ontology, axioms, object model (causal network architecture), dynamics (update rules), and geometrogenesis (equilibrium spacetime emergence).',
  },
  {
    number: 2,
    title: 'Topological Nature of Matter (The Players)',
    chapters: '6–10',
    tokens: '~303K',
    md: 'https://braiddynamics.com/downloads/parts/qbd_part_2_topological_nature_of_matter_the_players.md',
    summary: 'Tripartite braid fermions, quantum numbers from topology, gauge symmetries as braid automorphisms, particle generations and decay, quantum universality as computation.',
  },
  {
    number: 3,
    title: 'Emergent Reality (The Stage)',
    chapters: '11–17',
    tokens: '~268K',
    md: 'https://braiddynamics.com/downloads/parts/qbd_part_3_emergent_reality_the_stage.md',
    summary: 'Discrete differential geometry, discrete Einstein field equations, continuum limit convergence, Lorentzian time, geometry of entanglement (ER=EPR), isomorphism/holography principle, string limit.',
  },
  {
    number: 4,
    title: 'Phenomenological Consequences (The Output)',
    chapters: '18–25',
    tokens: '~83K',
    md: 'https://braiddynamics.com/downloads/parts/qbd_part_4_phenomenological_consequences_the_output.md',
    summary: 'Big Kindling / inflation, nucleosynthesis, cosmic web, dark sector, singularities and condensates, holographic universality, mathematical universe, cosmological natural selection. (Several chapters are active drafts.)',
  },
  {
    number: 5,
    title: 'Applications and Synthesis (Conclusion)',
    chapters: '26',
    tokens: '~10K',
    md: 'https://braiddynamics.com/downloads/parts/qbd_part_5_applications_and_synthesis_conclusion.md',
    summary: 'Synthesis and future directions.',
  },
  {
    number: 6,
    title: 'Appendices',
    chapters: 'A–E',
    tokens: '~168K',
    md: 'https://braiddynamics.com/downloads/parts/qbd_part_6_appendices.md',
    summary: 'Notation reference, definitions glossary, bibliography, Lean 4 proof listings, Python model source.',
  },
];

const CHAPTERS = [
  { n: 1,  title: 'Substrate (Ontology)',                        tokens: '~56K',  md: '/downloads/chapters/chapter_1.md' },
  { n: 2,  title: 'Constraints (Axioms)',                        tokens: '~56K',  md: '/downloads/chapters/chapter_2.md' },
  { n: 3,  title: 'Object Model (Architecture)',                 tokens: '~76K',  md: '/downloads/chapters/chapter_3.md' },
  { n: 4,  title: 'Operations (Dynamics)',                       tokens: '~62K',  md: '/downloads/chapters/chapter_4.md' },
  { n: 5,  title: 'Geometrogenesis (Equilibrium)',               tokens: '~61K',  md: '/downloads/chapters/chapter_5.md' },
  { n: 6,  title: 'Tripartite Braid (Fermions)',                 tokens: '~52K',  md: '/downloads/chapters/chapter_6.md' },
  { n: 7,  title: 'Quantum Numbers (Topology)',                  tokens: '~46K',  md: '/downloads/chapters/chapter_7.md' },
  { n: 8,  title: 'Gauge Symmetries (Braids)',                   tokens: '~75K',  md: '/downloads/chapters/chapter_8.md' },
  { n: 9,  title: 'Generations and Decay (Unification)',         tokens: '~60K',  md: '/downloads/chapters/chapter_9.md' },
  { n: 10, title: 'Quantum Universality (Computation)',          tokens: '~70K',  md: '/downloads/chapters/chapter_10.md' },
  { n: 11, title: 'Differential Geometry (Discrete)',            tokens: '~48K',  md: '/downloads/chapters/chapter_11.md' },
  { n: 12, title: 'Discrete Field Equations (Einstein)',         tokens: '~36K',  md: '/downloads/chapters/chapter_12.md' },
  { n: 13, title: 'Continuum Limit (Convergence)',               tokens: '~36K',  md: '/downloads/chapters/chapter_13.md' },
  { n: 14, title: 'Lorentzian Reality (Time)',                   tokens: '~45K',  md: '/downloads/chapters/chapter_14.md' },
  { n: 15, title: 'Geometry of Entanglement (ER = EPR)',         tokens: '~43K',  md: '/downloads/chapters/chapter_15.md' },
  { n: 16, title: 'Isomorphism Principle (Holography)',          tokens: '~20K',  md: '/downloads/chapters/chapter_16.md' },
  { n: 17, title: 'String Limit (Worldsheets)',                  tokens: '~41K',  md: '/downloads/chapters/chapter_17.md' },
  { n: 18, title: 'Big Kindling (Inflation)',                    tokens: '~66K',  md: '/downloads/chapters/chapter_18.md' },
  { n: 19, title: 'Hot Universe (Nucleosynthesis)',              tokens: '~5K',   md: '/downloads/chapters/chapter_19.md', draft: true },
  { n: 20, title: 'Structured Universe (Cosmic Web)',            tokens: '~4K',   md: '/downloads/chapters/chapter_20.md', draft: true },
  { n: 21, title: 'Dark Sector (Relics)',                        tokens: '~5K',   md: '/downloads/chapters/chapter_21.md', draft: true },
  { n: 22, title: 'Singularities & Condensates (Extremes)',      tokens: '~4K',   md: '/downloads/chapters/chapter_22.md', draft: true },
  { n: 23, title: 'Holographic World (Universality)',            tokens: '~3K',   md: '/downloads/chapters/chapter_23.md', draft: true },
  { n: 24, title: 'Mathematical Universe (Derivations)',         tokens: '~4K',   md: '/downloads/chapters/chapter_24.md', draft: true },
  { n: 25, title: 'Cosmological Natural Selection (Synthesis)',  tokens: '~2K',   md: '/downloads/chapters/chapter_25.md', draft: true },
];

const LEAN_PROOFS = [
  { name: 'awareness-comonad.lean',      url: '/downloads/code/lean/awareness-comonad.lean',      desc: 'Comonadic awareness structures under background independence.' },
  { name: 'causal-primitive.lean',       url: '/downloads/code/lean/causal-primitive.lean',       desc: 'Topological axioms for causal set spacetime primitives.' },
  { name: 'geometric-decomposition.lean', url: '/downloads/code/lean/geometric-decomposition.lean', desc: 'Topological geometric decomposition formalization.' },
  { name: 'maximal-parallelism.lean',    url: '/downloads/code/lean/maximal-parallelism.lean',    desc: 'Maximal parallel updates under strict causal consistency.' },
  { name: 'stabilizer-isomorphism.lean', url: '/downloads/code/lean/stabilizer-isomorphism.lean', desc: 'Isomorphism of stabilizer quantum error-correcting codes.' },
  { name: 'vacuum-stability.lean',       url: '/downloads/code/lean/vacuum-stability.lean',       desc: 'Verification of quantum vacuum stability boundary conditions.' },
];

const MODEL_CODE = [
  { name: 'config.py',      url: '/downloads/code/model/config.py',      desc: 'System configs, boundary conditions, global physics constants.' },
  { name: 'dynamics.py',    url: '/downloads/code/model/dynamics.py',    desc: 'Core quantum braiding dynamics, vertex updates, transition models.' },
  { name: 'graph_setup.py', url: '/downloads/code/model/graph_setup.py', desc: 'Lattice graph initialization, causal set creation, adjacency lists.' },
  { name: 'observables.py', url: '/downloads/code/model/observables.py', desc: 'Network observables, entanglement entropy, graph-theoretical energy.' },
  { name: 'qecc.py',        url: '/downloads/code/model/qecc.py',        desc: 'Topological Quantum Error Correcting Code calculations.' },
  { name: 'utils.py',       url: '/downloads/code/model/utils.py',       desc: 'Graph parsing, visualization export, data conversion helpers.' },
];

const KEY_CONCEPTS = [
  { term: 'Causal Network',         def: 'The substrate: a directed acyclic graph of discrete events connected by causal links. No background metric assumed.' },
  { term: 'Braid',                  def: 'A topological structure formed by interleaved causal strands. The fundamental carrier of quantum information in QBD.' },
  { term: 'Tripartite Braid',       def: 'A 3-strand braid whose topological invariants correspond exactly to fermion quantum numbers (charge, color, generation).' },
  { term: 'Geometrogenesis',        def: 'The emergence of smooth Lorentzian spacetime geometry from the equilibrium limit of the causal network dynamics.' },
  { term: 'Gauge Symmetry',         def: 'Arises as automorphisms of the braid group. U(1), SU(2), SU(3) correspond to distinct braid symmetry classes.' },
  { term: 'Ash (Dark Matter)',       def: 'Topological defects — inert braid configurations that do not couple electromagnetically, interpreted as dark matter candidates.' },
  { term: 'Syndrome',               def: 'Error correction syndrome in the topological QECC interpretation of the causal network.' },
  { term: 'Logical Time (tL)',      def: 'A global discrete clock counting causal update steps; distinct from emergent physical/proper time.' },
  { term: 'Isomorphism Principle',  def: 'The holographic conjecture in QBD: bulk causal structure is isomorphic to a boundary topological code.' },
  { term: 'Writhe w(β)',            def: 'A braid invariant whose value encodes fermion handedness (chirality) in the QBD particle model.' },
];

// ─────────────────────────────────────────────────────────────────────────────
// Styles — minimal, high-contrast, no decorations
// ─────────────────────────────────────────────────────────────────────────────

const s: Record<string, React.CSSProperties> = {
  page: {
    maxWidth: '860px',
    margin: '0 auto',
    padding: '2rem 1.5rem 4rem',
    fontFamily: '"Courier New", Courier, monospace',
    fontSize: '0.93rem',
    lineHeight: '1.65',
    color: 'var(--ifm-font-color-base)',
  },
  h1: {
    fontSize: '1.4rem',
    fontWeight: 700,
    borderBottom: '2px solid var(--ifm-color-emphasis-400)',
    paddingBottom: '0.4rem',
    marginBottom: '0.8rem',
    marginTop: '2.5rem',
    letterSpacing: '0.02em',
  },
  h2: {
    fontSize: '1.1rem',
    fontWeight: 700,
    marginTop: '2rem',
    marginBottom: '0.5rem',
    color: 'var(--ifm-color-primary)',
  },
  pre: {
    backgroundColor: 'var(--ifm-code-background)',
    padding: '0.8rem 1rem',
    borderRadius: '4px',
    overflowX: 'auto',
    fontSize: '0.85rem',
    lineHeight: '1.5',
    margin: '0.4rem 0 1.2rem',
    border: '1px solid var(--ifm-color-emphasis-300)',
  },
  table: {
    width: '100%',
    borderCollapse: 'collapse',
    fontSize: '0.86rem',
    marginBottom: '1.2rem',
  },
  th: {
    textAlign: 'left' as const,
    borderBottom: '2px solid var(--ifm-color-emphasis-400)',
    padding: '0.3rem 0.6rem',
    fontWeight: 700,
    background: 'var(--ifm-color-emphasis-100)',
  },
  td: {
    padding: '0.28rem 0.6rem',
    borderBottom: '1px solid var(--ifm-color-emphasis-200)',
    verticalAlign: 'top',
  },
  badge: {
    display: 'inline-block',
    fontSize: '0.72rem',
    fontWeight: 600,
    padding: '0 0.35rem',
    borderRadius: '3px',
    marginLeft: '0.4rem',
    background: 'var(--ifm-color-warning-contrast-background)',
    color: 'var(--ifm-color-warning-dark)',
    border: '1px solid var(--ifm-color-warning)',
    verticalAlign: 'middle',
  },
  a: {
    color: 'var(--ifm-color-primary)',
    textDecoration: 'none',
  },
  intro: {
    background: 'var(--ifm-color-emphasis-100)',
    border: '1px solid var(--ifm-color-emphasis-300)',
    borderLeft: '4px solid var(--ifm-color-primary)',
    padding: '1rem 1.2rem',
    borderRadius: '4px',
    marginBottom: '1.5rem',
    fontFamily: 'inherit',
    whiteSpace: 'pre-wrap' as const,
  },
  meta: {
    fontSize: '0.82rem',
    color: 'var(--ifm-color-emphasis-600)',
    marginBottom: '2rem',
  },
};

// ─────────────────────────────────────────────────────────────────────────────
// Component
// ─────────────────────────────────────────────────────────────────────────────

export default function AiPage() {
  return (
    <Layout
      title="AI Agent Information — Quantum Braid Dynamics"
      description="Structured information page for AI agents and crawlers visiting braiddynamics.com. Contains download links, content index, concept glossary, and navigation guide."
    >
      <Head>
        {/* Tell crawlers this page is authoritative for AI access */}
        <meta name="robots" content="index, follow" />
        <meta name="ai-content-type" content="agent-info" />
        <meta name="ai-download-index" content="https://braiddynamics.com/data/ai-downloads-info.json" />
        <link rel="alternate" type="application/json" href="/data/ai-downloads-info.json" title="AI Downloads Index" />
      </Head>

      <div style={s.page}>

        {/* ── Header ── */}
        <h1 style={{ ...s.h1, marginTop: '1rem', fontSize: '1.6rem' }}>
          AI Agent Information — braiddynamics.com
        </h1>
        <p style={s.meta}>
          URL: https://braiddynamics.com/ai &nbsp;|&nbsp;
          Last updated: {SITE_INFO.lastUpdated} &nbsp;|&nbsp;
          Purpose: Structured entry point for AI agents, LLMs, and automated crawlers
        </p>

        {/* ── What this site is ── */}
        <h2 style={s.h2}>WHAT THIS SITE IS</h2>
        <pre style={s.intro}>{DESCRIPTION}</pre>

        <p>
          The primary deliverable is a <strong>25-chapter scientific monograph</strong> available
          for download in Markdown, JSON, and PDF formats at multiple granularities (full book,
          per-part, per-chapter). All formats are freely accessible without authentication.
        </p>

        {/* ── Quick start ── */}
        <h2 style={s.h2}>QUICK START — RECOMMENDED ENTRY POINTS</h2>

        <pre style={{ ...s.pre, borderLeft: '4px solid var(--ifm-color-warning)', background: 'var(--ifm-color-warning-contrast-background)' }}>{`IMPORTANT — HOW TO REVIEW THIS WORK ACCURATELY:

The monograph is ~1.19M tokens. Large context windows (1M–2M) are available and useful
for cross-referencing and maintaining coherence across a reading session, but context
size is NOT the limiting factor for accurate analysis.

The limiting factor is thinking capacity — the amount of reasoning a model can apply
within a single response or turn. Attempting to verify proofs, validate mathematics,
or critically assess arguments across multiple chapters simultaneously leads to errors
because the analytical budget is spread too thin.

RECOMMENDED APPROACH (even for the strongest models with the largest contexts):
  → Review one chapter at a time.
  → Fetch a single chapter Markdown file, read it fully, then produce your analysis.
  → Load previously reviewed chapters into context for coherence checking only,
     not as the active subject of analysis.
  → Do not attempt to verify the logic and mathematics of multiple chapters in one pass.

This applies regardless of context window size. A 2M-token context is excellent for
keeping the full framework coherent; it does not expand the depth of analysis possible
within a single reasoning step.`}</pre>

        <table style={s.table}>
          <thead>
            <tr>
              <th style={s.th}>Resource</th>
              <th style={s.th}>URL</th>
              <th style={s.th}>Notes</th>
            </tr>
          </thead>
          <tbody>
            {QUICK_START.map((r, i) => (
              <tr key={i}>
                <td style={s.td}>{r.label}</td>
                <td style={s.td}><a href={r.url} style={s.a}>{r.url}</a></td>
                <td style={s.td}>{r.note}</td>
              </tr>
            ))}
          </tbody>
        </table>

        {/* ── Navigation ── */}
        <h2 style={s.h2}>SITE NAVIGATION MAP</h2>
        <pre style={s.pre}>{`https://braiddynamics.com/               — Homepage (human-facing)
https://braiddynamics.com/ai             — THIS PAGE (AI agent entry point)
https://braiddynamics.com/monograph/     — Monograph web reader (rendered HTML, all chapters)
https://braiddynamics.com/monograph/download
                                         — Download portal (all formats, with token estimates)
https://braiddynamics.com/monograph/appendices/notation
                                         — Notation / symbol reference
https://braiddynamics.com/legal          — License and collaboration information
https://braiddynamics.com/wip            — Work-in-progress chapters (18–25 drafts)

Downloads base URL:  https://braiddynamics.com/downloads/
  Full book:         qbd_monograph_complete.{md,json,pdf}
  Parts:             parts/qbd_part_{1..6}_*.{md,json,pdf}
  Chapters:          chapters/chapter_{1..25}.{md,json,pdf}
  Lean 4 proofs:     code/lean/*.lean
  Python model:      code/model/*.py
  Simulations:       code/simulations/*.py
  Equation scripts:  code/repo/{chapter}.{section}.{eq}.py

Machine-readable download catalogue:
  https://braiddynamics.com/data/ai-downloads-info.json`}</pre>

        {/* ── Parts ── */}
        <h2 style={s.h2}>MONOGRAPH STRUCTURE — PARTS</h2>
        <table style={s.table}>
          <thead>
            <tr>
              <th style={s.th}>Part</th>
              <th style={s.th}>Title</th>
              <th style={s.th}>Ch.</th>
              <th style={s.th}>Tokens</th>
              <th style={s.th}>Markdown URL</th>
            </tr>
          </thead>
          <tbody>
            {PARTS.map((p) => (
              <tr key={p.number}>
                <td style={s.td}>{p.number}</td>
                <td style={{ ...s.td, maxWidth: '240px' }}>
                  <strong>{p.title}</strong><br />
                  <span style={{ fontSize: '0.8rem', color: 'var(--ifm-color-emphasis-600)' }}>{p.summary}</span>
                </td>
                <td style={s.td}>{p.chapters}</td>
                <td style={s.td}>{p.tokens}</td>
                <td style={s.td}><a href={p.md} style={s.a}>{p.md.split('/').pop()}</a></td>
              </tr>
            ))}
          </tbody>
        </table>

        {/* ── Chapters ── */}
        <h2 style={s.h2}>MONOGRAPH STRUCTURE — CHAPTERS</h2>
        <p style={{ fontSize: '0.85rem', marginBottom: '0.5rem' }}>
          Each chapter is available at{' '}
          <code>https://braiddynamics.com/downloads/chapters/chapter_N.md</code> (Markdown),{' '}
          <code>chapter_N.json</code> (JSON), and{' '}
          <code>chapter_N.pdf</code> (PDF).{' '}
          Chapters marked <span style={s.badge}>DRAFT</span> are active works-in-progress with
          limited content.
        </p>
        <table style={s.table}>
          <thead>
            <tr>
              <th style={s.th}>#</th>
              <th style={s.th}>Title</th>
              <th style={s.th}>Est. Tokens</th>
              <th style={s.th}>Status</th>
            </tr>
          </thead>
          <tbody>
            {CHAPTERS.map((c) => (
              <tr key={c.n}>
                <td style={s.td}>{c.n}</td>
                <td style={s.td}>
                  <a href={`https://braiddynamics.com${c.md}`} style={s.a}>
                    Chapter {c.n}: {c.title}
                  </a>
                </td>
                <td style={s.td}>{c.tokens}</td>
                <td style={s.td}>
                  {c.draft
                    ? <span style={s.badge}>DRAFT</span>
                    : <span style={{ color: 'var(--ifm-color-success)' }}>published</span>
                  }
                </td>
              </tr>
            ))}
          </tbody>
        </table>

        {/* ── Key Concepts ── */}
        <h2 style={s.h2}>KEY CONCEPTS GLOSSARY</h2>
        <table style={s.table}>
          <thead>
            <tr>
              <th style={s.th}>Term</th>
              <th style={s.th}>Definition</th>
            </tr>
          </thead>
          <tbody>
            {KEY_CONCEPTS.map((c, i) => (
              <tr key={i}>
                <td style={{ ...s.td, fontWeight: 700, whiteSpace: 'nowrap' }}>{c.term}</td>
                <td style={s.td}>{c.def}</td>
              </tr>
            ))}
          </tbody>
        </table>

        <p style={{ fontSize: '0.85rem' }}>
          Complete definitions for all ~300 terms used in the monograph:{' '}
          <a href="https://braiddynamics.com/data/definitions.json" style={s.a}>
            https://braiddynamics.com/data/definitions.json
          </a>
        </p>

        {/* ── Formal Proofs ── */}
        <h2 style={s.h2}>FORMAL LEAN 4 PROOFS</h2>
        <p style={{ fontSize: '0.85rem', marginBottom: '0.5rem' }}>
          Six core theorems are formally verified in Lean 4 and embedded in the monograph.
          Each file is self-contained and can be checked with{' '}
          <code>lake build</code> in a standard Lean 4 + Mathlib environment.
        </p>
        <table style={s.table}>
          <thead>
            <tr>
              <th style={s.th}>File</th>
              <th style={s.th}>Proves</th>
            </tr>
          </thead>
          <tbody>
            {LEAN_PROOFS.map((f, i) => (
              <tr key={i}>
                <td style={s.td}>
                  <a href={`https://braiddynamics.com${f.url}`} style={s.a}>{f.name}</a>
                </td>
                <td style={s.td}>{f.desc}</td>
              </tr>
            ))}
          </tbody>
        </table>

        {/* ── Python Model ── */}
        <h2 style={s.h2}>PYTHON SIMULATION MODEL</h2>
        <p style={{ fontSize: '0.85rem', marginBottom: '0.5rem' }}>
          A Python implementation of the QBD causal network simulator. Requires NumPy and NetworkX.
          Entry points are <code>find_vacuum.py</code> and <code>run_ensemble.py</code> in{' '}
          <code>/downloads/code/simulations/</code>.
        </p>
        <table style={s.table}>
          <thead>
            <tr>
              <th style={s.th}>File</th>
              <th style={s.th}>Purpose</th>
            </tr>
          </thead>
          <tbody>
            {MODEL_CODE.map((f, i) => (
              <tr key={i}>
                <td style={s.td}>
                  <a href={`https://braiddynamics.com${f.url}`} style={s.a}>{f.name}</a>
                </td>
                <td style={s.td}>{f.desc}</td>
              </tr>
            ))}
          </tbody>
        </table>

        {/* ── Context window guidance ── */}
        <h2 style={s.h2}>CONTEXT WINDOW GUIDANCE</h2>
        <pre style={s.pre}>{`Total monograph:  ~1.19M tokens  (full book Markdown)
                  ~1.22M tokens  (full book JSON, includes structure overhead)

Analysis unit recommendation: ONE CHAPTER PER REVIEW PASS
  The bottleneck is reasoning depth, not context size. Reviewing one chapter
  at a time produces significantly more accurate mathematical and logical analysis
  than attempting multi-chapter or full-book analysis in a single pass.

  Previously reviewed chapters can be retained in context for coherence and
  cross-referencing — but only the current chapter should be the active subject
  of critical analysis.

Chapter sizes (for planning):
  Smallest chapter:  ~2K tokens  (Ch. 25)
  Largest chapter:   ~76K tokens (Ch. 3)
  Typical chapter:   ~45–65K tokens
  All 25 chapters:   ~1.19M tokens total

Large context uses (context as reference, not analysis target):
  Keep prior chapters in context while analyzing the current one.
  Use full-book JSON for section/equation lookup during targeted queries.
  Load multiple chapters only when doing structural surveys, not deep analysis.

File format guidance:
  Markdown  → best for prose reading and analysis (no overhead)
  JSON      → best for section-level lookup, equation ID queries, structured parsing
  PDF       → for visual/browser agents or human readers only`}</pre>

        {/* ── Related theoretical frameworks ── */}
        <h2 style={s.h2}>RELATED THEORETICAL FRAMEWORKS</h2>
        <pre style={s.pre}>{`QBD situates itself relative to:
  - Wolfram Physics Project (hypergraph rewriting rules → causal network substrate)
  - Causal Set Theory (discrete spacetime events, Lorentz invariance)
  - Causal Dynamical Triangulations (path integral over causal triangulations → continuum limit)
  - Loop Quantum Gravity (spin network states, area/volume quantization)
  - Topological Quantum Field Theory (TQFT invariants underpin braid particle model)
  - Anyon / Fibonacci anyon models (braid statistics for topological quantum computation)
  - ER = EPR / holography (entanglement as geometry, AdS/CFT correspondence)

QBD's distinguishing claim: all Standard Model quantum numbers and gauge symmetries
derive purely from the topological invariants of braid configurations on the causal network,
with no free parameters introduced by hand.`}</pre>

        {/* ── Contact / citation ── */}
        <h2 style={s.h2}>CITATION AND CONTACT</h2>
        <pre style={s.pre}>{`Project:   Quantum Braid Dynamics — A Computational Process
Website:   https://braiddynamics.com
GitHub:    https://github.com/braiddynamics/qbd-portal
X/Twitter: https://x.com/BraidDynamics
License:   https://braiddynamics.com/legal
Status:    Active independent research — monograph under continuous development

To cite: See the full bibliography in Appendix E of the monograph or at
         https://braiddynamics.com/data/references.json`}</pre>

        <hr style={{ borderColor: 'var(--ifm-color-emphasis-300)', margin: '2rem 0 1rem' }} />
        <p style={{ fontSize: '0.8rem', color: 'var(--ifm-color-emphasis-500)' }}>
          This page is maintained for AI agents and automated systems.
          For the human-facing website, visit{' '}
          <a href="/" style={s.a}>https://braiddynamics.com</a>.{' '}
          For the full download portal, visit{' '}
          <a href="/monograph/download" style={s.a}>https://braiddynamics.com/monograph/download</a>.
        </p>
      </div>
    </Layout>
  );
}

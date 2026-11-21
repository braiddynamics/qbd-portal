import React, { useState } from 'react';
import Layout from '@theme/Layout';
import Head from '@docusaurus/Head';
import { ParticleGraphic } from '../components/graphics/spectrum-graphics';
import HeroNetworkCanvas from '../components/graphics/hero-network-canvas';

interface ParticleData {
  row: number;
  col: number;
  symbol: string;
  name: string;
  charge: React.ReactNode;
  modalCharge?: React.ReactNode;
  chargeLabel?: React.ReactNode;
  param: React.ReactNode;
  complexity: React.ReactNode;
  complexityLabel?: React.ReactNode;
  mass: string;
  massLabel?: React.ReactNode;
  qbdMass?: React.ReactNode;
  qbdMassLabel?: React.ReactNode;
  writheConfig: React.ReactNode;
  description: React.ReactNode;
  colorType: 'blue' | 'green' | 'red' | 'gold' | 'amber';
}

const particles: ParticleData[] = [
  // ROW 1: UP-TYPE QUARKS & UNIFICATION
  {
    row: 1,
    col: 1,
    symbol: 'u',
    name: 'Up Quark',
    charge: '+2/3 e',
    param: 'Writhe: +2/3',
    complexity: <span>1 (N<sub>3</sub>)</span>,
    mass: '2.2 MeV',
    qbdMass: <span>0.170 MeV (bare, κ<sub>m</sub> · 1)</span>,
    qbdMassLabel: 'Bare Topo Mass (§7.4)',
    writheConfig: '(1, 1, 0)',
    description: (
      <span>
        Chiral tripartite asymmetric braid configuration with writhe vector (1, 1, 0). Parallel ribbon sharing (k<sub>share</sub> = 1) reduces its bare complexity to N<sub>3</sub> = 1 (zeroth-order mass 0.170 MeV, degenerate with the down quark); matching to the 2 GeV MS-bar running mass (2.2 MeV) requires electroweak Yukawa splitting and strong RG running (§7.4.Z).
      </span>
    ),
    colorType: 'blue'
  },
  {
    row: 1,
    col: 2,
    symbol: 'c',
    name: 'Charm Quark',
    charge: '+2/3 e',
    param: 'C2 Crossing',
    complexity: <span>7,626 (N<sub>3</sub>)</span>,
    mass: '1,275.0 MeV',
    qbdMass: '1,298.96 MeV (Δ 1.88%)',
    qbdMassLabel: 'Bare Topo Mass (§7.4)',
    writheConfig: '(62, 62, 0)',
    description: (
      <span>
        Second-generation up-type quark with benchmark writhe vector (62, 62, 0). Under the up-type sharing rule N<sub>net</sub> = 2w<sup>2</sup> − w, its complexity reaches 7,626 3-cycles, giving a bare topological mass of 1,298.96 MeV (within 1.88% of the 1,275.0 MeV reference, §7.4.6.1).
      </span>
    ),
    colorType: 'blue'
  },
  {
    row: 1,
    col: 3,
    symbol: 't',
    name: 'Top Quark',
    charge: '+2/3 e',
    param: 'Torsion Peak',
    complexity: <span>1,013,176 (N<sub>3</sub>)</span>,
    mass: '172,900.0 MeV',
    qbdMass: '172,577.65 MeV (Δ 0.19%)',
    qbdMassLabel: 'Bare Topo Mass (§7.4)',
    writheConfig: '(712, 712, 0)',
    description: (
      <span>
        Third-generation up-type quark exhibiting extreme torsional complexity with benchmark writhe vector (712, 712, 0). Yielding 1,013,176 geometric 3-cycle quanta, its bare topological mass of 172,577.65 MeV matches the observed 172,900.0 MeV mass within 0.19% (§7.4.6.1).
      </span>
    ),
    colorType: 'blue'
  },
  {
    row: 1,
    col: 4,
    symbol: 'g',
    name: 'Gluon',
    charge: '',
    param: 'su(3) Adjoint Swaps',
    complexity: '8 su(3) Generators',
    complexityLabel: 'Gauge Structure',
    mass: '0.0 MeV',
    qbdMass: '0.0 MeV (Unbroken SU(3))',
    qbdMassLabel: 'QBD Sector (§8.3)',
    writheConfig: 'SU(3) Adjoint Rewrite',
    description: (
      <span>
        Emergent massless gauge boson representing the eight independent color-sector generators (exchanges and diagonal imbalances) of su(3) acting on tripartite quark ribbons (§8.3).
      </span>
    ),
    colorType: 'red'
  },
  {
    row: 1,
    col: 5,
    symbol: 'β₅',
    name: 'Pentaribbon',
    charge: '',
    chargeLabel: 'Symmetry Group',
    modalCharge: 'SU(5) Unified',
    param: 'Unified State',
    complexity: <span>5 Strands (R<sub>1</sub>…R<sub>5</sub>)</span>,
    complexityLabel: 'Braid Architecture',
    mass: 'GUT Scale',
    massLabel: 'Energy Scale',
    qbdMass: '24 su(5) Generators (§9.2)',
    qbdMassLabel: 'Algebraic Closure',
    writheConfig: '5-Ribbon Unified Sector',
    description: (
      <span>
        A five-strand composite braid representing the unified pre-geometric state at grand unification scales. Four adjacent exchanges and four diagonal imbalances generate the 24-dimensional su(5) algebra, with fragmentation tunneling into SU(3) × SU(2) × U(1) severing the 6 cross-sector color-weak links (§9.2, §9.4).
      </span>
    ),
    colorType: 'gold'
  },

  // ROW 2: DOWN-TYPE QUARKS & EM
  {
    row: 2,
    col: 1,
    symbol: 'd',
    name: 'Down Quark',
    charge: '-1/3 e',
    param: 'Writhe: -1/3',
    complexity: <span>1 (N<sub>3</sub>)</span>,
    mass: '4.7 MeV',
    qbdMass: <span>0.170 MeV (bare, κ<sub>m</sub> · 1)</span>,
    qbdMassLabel: 'Bare Topo Mass (§7.4)',
    writheConfig: '(-1, 0, 0)',
    description: (
      <span>
        Chiral tripartite asymmetric braid with writhe vector (-1, 0, 0), giving electric charge −1/3 and bare complexity N<sub>3</sub> = 1 (zeroth-order mass 0.170 MeV). Matching to the 2 GeV MS-bar running mass (4.7 MeV) requires electroweak Yukawa splitting (y<sub>d</sub> &gt; y<sub>u</sub>) and strong RG running (§7.4.Z).
      </span>
    ),
    colorType: 'blue'
  },
  {
    row: 2,
    col: 2,
    symbol: 's',
    name: 'Strange Quark',
    charge: '-1/3 e',
    param: 'S2 Crossing',
    complexity: <span>576 (N<sub>3</sub>)</span>,
    mass: '95.0 MeV',
    qbdMass: '98.11 MeV (Δ 3.28%)',
    qbdMassLabel: 'Bare Topo Mass (§7.4)',
    writheConfig: '(-24, 0, 0)',
    description: (
      <span>
        Second-generation down-type quark with benchmark writhe vector (-24, 0, 0). Under N<sub>net</sub> = w<sup>2</sup>, its complexity of 576 3-cycles produces a bare topological mass of 98.11 MeV (within 3.28% of the 95.0 MeV reference, §7.4.6.1).
      </span>
    ),
    colorType: 'blue'
  },
  {
    row: 2,
    col: 3,
    symbol: 'b',
    name: 'Bottom Quark',
    charge: '-1/3 e',
    param: 'B3 Crossing',
    complexity: <span>24,649 (N<sub>3</sub>)</span>,
    mass: '4,180.0 MeV',
    qbdMass: '4,198.55 MeV (Δ 0.44%)',
    qbdMassLabel: 'Bare Topo Mass (§7.4)',
    writheConfig: '(-157, 0, 0)',
    description: (
      <span>
        Third-generation down-type quark with benchmark writhe vector (-157, 0, 0). Its complexity of 24,649 3-cycles yields a bare topological mass of 4,198.55 MeV, within 0.44% of the 4,180.0 MeV reference (§7.4.6.1).
      </span>
    ),
    colorType: 'blue'
  },
  {
    row: 2,
    col: 4,
    symbol: 'γ',
    name: 'Photon',
    charge: '',
    param: 'U(1) Frame Twist',
    complexity: '4-Cycle U(1) Transport',
    complexityLabel: 'Gauge Structure',
    mass: '0.0 MeV',
    qbdMass: <span>0.0 MeV (Unbroken Q = T<sup>3</sup> + Y)</span>,
    qbdMassLabel: 'QBD Sector (§8.5, §8.7)',
    writheConfig: 'U(1) Phase Transport',
    description: (
      <span>
        Massless gauge field corresponding to the unbroken electromagnetic generator Q = T<sup>3</sup> + Y and enclosing 4-cycle U(1) phase transport along the causal substrate (§8.5.4, §8.7.7).
      </span>
    ),
    colorType: 'red'
  },
  {
    row: 2,
    col: 5,
    symbol: 'β₃',
    name: 'Tripartite Braid',
    charge: '',
    chargeLabel: 'Admitted Charges',
    modalCharge: '0, −1, −1/3, +2/3 e',
    param: 'Topological Quantum',
    complexity: '3 Framed Ribbons',
    complexityLabel: 'Braid Architecture',
    mass: 'Ground State',
    massLabel: 'Sector Role',
    qbdMass: 'Spin-1/2 Protected Sector (§6.2, §7.1)',
    qbdMassLabel: 'Matter Statistics',
    writheConfig: 'Framed 3-Ribbon Sector',
    description: (
      <span>
        The fundamental tripartite (three-strand) framed ribbon braid forming the minimal topologically protected matter sector. Chiral twists and crossings of these three ribbons generate spin-1/2 statistics, fractional and integer charges, and the elementary fermion spectrum (Ch. 6–7).
      </span>
    ),
    colorType: 'gold'
  },

  // ROW 3: CHARGED LEPTONS & WEAK NEUTRAL
  {
    row: 3,
    col: 1,
    symbol: 'e',
    name: 'Electron',
    charge: '-1 e',
    param: 'Writhe: -1',
    complexity: <span>3 (N<sub>3</sub>)</span>,
    mass: '0.511 MeV',
    qbdMass: <span>0.511 MeV (anchor, κ<sub>m</sub> = m<sub>e</sub>/3)</span>,
    qbdMassLabel: 'Bare Topo Mass (§7.4)',
    writheConfig: '(-1, -1, -1)',
    description: (
      <span>
        Minimal stable color-singlet symmetric 3-braid with writhe vector (-1, -1, -1) and complexity N<sub>3</sub> = 3w<sup>2</sup> = 3. Anchors the universal mass-per-quantum scale κ<sub>m</sub> = 0.511 / 3 ≈ 0.170 MeV (§7.4.2, §7.4.6.1).
      </span>
    ),
    colorType: 'green'
  },
  {
    row: 3,
    col: 2,
    symbol: 'μ',
    name: 'Muon',
    charge: '-1 e',
    param: 'Symmetric C2',
    complexity: <span>588 (N<sub>3</sub>)</span>,
    mass: '105.66 MeV',
    qbdMass: '100.16 MeV (Δ 5.21%)',
    qbdMassLabel: 'Bare Topo Mass (§7.4)',
    writheConfig: '(-14, -14, -14)',
    description: (
      <span>
        Second-generation charged lepton modeled as a tighter symmetric color-singlet braid (-14, -14, -14) with complexity N<sub>3</sub> = 3(14<sup>2</sup>) = 588, giving a bare topological mass of 100.16 MeV (within 5.21% of 105.66 MeV, §7.4.6.1).
      </span>
    ),
    colorType: 'green'
  },
  {
    row: 3,
    col: 3,
    symbol: 'τ',
    name: 'Tau',
    charge: '-1 e',
    param: 'Symmetric C3',
    complexity: <span>10,443 (N<sub>3</sub>)</span>,
    mass: '1,776.80 MeV',
    qbdMass: '1,778.79 MeV (Δ 0.11%)',
    qbdMassLabel: 'Bare Topo Mass (§7.4)',
    writheConfig: '(-59, -59, -59)',
    description: (
      <span>
        Third-generation charged lepton represented by a densely wound symmetric braid (-59, -59, -59) with complexity N<sub>3</sub> = 3(59<sup>2</sup>) = 10,443. Its quadratic torsion cost yields 1,778.79 MeV, matching the 1,776.80 MeV reference within 0.11% (§7.4.6.1).
      </span>
    ),
    colorType: 'green'
  },
  {
    row: 3,
    col: 4,
    symbol: 'Z',
    name: 'Z Boson',
    charge: '',
    param: <span>su(2)<sub>L</sub> Neutrality</span>,
    complexity: '3-Cycle / 4-Cycle Mixing',
    complexityLabel: 'Gauge Structure',
    mass: '91,187.6 MeV',
    qbdMass: '93.2 ± 2.0 GeV (ensemble, §8.7.3)',
    qbdMassLabel: 'QBD Ensemble Benchmark',
    writheConfig: <span>Neutral Weak Mixing (θ<sub>W</sub>)</span>,
    description: (
      <span>
        Neutral weak gauge boson emerging from electroweak mixing of 3-cycle SU(2)<sub>L</sub> bridges and 4-cycle U(1) transport (baseline sin<sup>2</sup>θ<sub>W</sub><sup>(0)</sup> = 0.25, benchmark 0.2457). Acquires mass m<sub>Z</sub> = m<sub>W</sub> / cos θ<sub>W</sub> from the 3-cycle geometric reservoir (§8.5, §8.7.3).
      </span>
    ),
    colorType: 'red'
  },
  {
    row: 3,
    col: 5,
    symbol: 'H',
    name: 'Higgs Boson',
    charge: '',
    param: '3-Cycle Condensate',
    complexity: <span>Geometric Reservoir (v ∝ √ρ<sub>3</sub>*)</span>,
    complexityLabel: 'Condensate Order',
    mass: '125.09 GeV',
    qbdMass: <span>v ≈ 246 GeV at ρ<sub>3</sub>* ≈ 0.0290 (§8.7.1)</span>,
    qbdMassLabel: 'Vacuum Reservoir VEV',
    writheConfig: <span>3-Cycle EW Condensate (Q = T<sup>3</sup> + Y unbroken)</span>,
    description: (
      <span>
        Within QBD, no fundamental scalar field is postulated: the electroweak VEV (v ≈ 246 GeV) is the macroscopic order parameter of the discrete-ensemble 3-cycle density ρ<sub>3</sub>* ≈ 0.0290 (v ∝ √ρ<sub>3</sub>*). Fermion masses obey the Topological Yukawa Identity m<sub>f</sub> = y<sub>f</sub> v = κ<sub>m</sub> N<sub>3</sub> (§8.7.1, §8.7.5).
      </span>
    ),
    colorType: 'gold'
  },

  // ROW 4: NEUTRINOS & WEAK CHARGED
  {
    row: 4,
    col: 1,
    symbol: 'νe',
    name: 'Electron Neutrino',
    charge: '0',
    param: 'Folded Gen I',
    complexity: <span>0 bare (+ N<sub>fold</sub>)</span>,
    mass: '~meV (Seesaw)',
    massLabel: 'Mass Regime',
    qbdMass: '0.64–2.56 meV (benchmark, §9.6.9)',
    qbdMassLabel: 'Two-State Seesaw (§9.6)',
    writheConfig: <span>Folded: W<sub>+</sub> + W<sub>−</sub> = 0</span>,
    description: (
      <span>
        Minimal folded braid joining a braid segment β<sub>+</sub> to its anti-braid β<sub>−</sub> at a fold vertex so global writhe cancels (W<sub>+</sub> + W<sub>−</sub> = 0, Q = 0) while retaining positive fold cost N<sub>fold</sub>. Light mass arises via topological seesaw m<sub>ν</sub> ≈ m<sub>D</sub><sup>2</sup> / M<sub>R</sub> (§7.4.Z, §9.6.1–9.6.9).
      </span>
    ),
    colorType: 'green'
  },
  {
    row: 4,
    col: 2,
    symbol: 'νμ',
    name: 'Muon Neutrino',
    charge: '0',
    param: 'Folded Gen II',
    complexity: <span>Folded Gen II (N<sub>fold</sub> &gt; 0)</span>,
    mass: 'Sub-eV (Seesaw)',
    massLabel: 'Mass Regime',
    qbdMass: <span>√|Δm<sup>2</sup><sub>atm</sub>| ≈ 0.049 eV ref (§9.6.9)</span>,
    qbdMassLabel: 'Oscillation Scale (§9.6)',
    writheConfig: <span>Folded: W<sub>+</sub> + W<sub>−</sub> = 0</span>,
    description: (
      <span>
        Second-generation color-singlet folded neutrino configuration. Opposing segment writhes cancel electric charge globally while higher fold topology mixes with the Planck-anchored heavy partner N<sub>R</sub> to yield sub-eV eigenstates (§9.6).
      </span>
    ),
    colorType: 'green'
  },
  {
    row: 4,
    col: 3,
    symbol: 'ντ',
    name: 'Tau Neutrino',
    charge: '0',
    param: 'Folded Gen III',
    complexity: <span>Folded Gen III (N<sub>fold</sub> &gt; 0)</span>,
    mass: 'Sub-eV (Seesaw)',
    massLabel: 'Mass Regime',
    qbdMass: <span>M<sub>R</sub> ≈ 1.23–2.36×10<sup>16</sup> GeV (§9.6.8)</span>,
    qbdMassLabel: 'Heavy Seesaw Anchor',
    writheConfig: <span>Folded: W<sub>+</sub> + W<sub>−</sub> = 0</span>,
    description: (
      <span>
        Third-generation folded neutrino configuration. Remains electrically and color neutral via opposite segment writhe cancellation, with its tiny active mass suppressed by the friction-limited heavy complexity scale M<sub>R</sub> ≈ 1.23–2.36 × 10<sup>16</sup> GeV (§9.6.8–9.6.9).
      </span>
    ),
    colorType: 'green'
  },
  {
    row: 4,
    col: 4,
    symbol: 'W',
    name: 'W Boson',
    charge: '±1 e',
    param: 'su(2) Charged Swaps',
    complexity: <span>3-Cycle SU(2)<sub>L</sub> Bridge</span>,
    complexityLabel: 'Gauge Structure',
    mass: '80,379.0 MeV',
    qbdMass: '81.7 ± 1.5 GeV (ensemble, §8.7.3)',
    qbdMassLabel: 'QBD Ensemble Benchmark',
    writheConfig: <span>SU(2)<sub>L</sub> Chiral Rewrite</span>,
    description: (
      <span>
        Charged weak gauge boson mediating left-handed flavor transitions via chiral 3-cycle SU(2)<sub>L</sub> strand-swap bridges. Acquires mass m<sub>W</sub> = gv / 2 from the 3-cycle geometric reservoir (§8.4, §8.5.4, §8.7.3).
      </span>
    ),
    colorType: 'red'
  },
  {
    row: 4,
    col: 5,
    symbol: 'ρ*',
    name: 'Vacuum Substrate',
    charge: <span>β<sub>c</sub> = ln(2)</span>,
    chargeLabel: <span>Info Modulus (β<sub>c</sub>)</span>,
    param: 'Calibration & Constants',
    complexity: <span>ρ* ≈ 0.037061 (MF) | ρ<sub>3</sub>* ≈ 0.0290 (Ens.)</span>,
    complexityLabel: 'Equilibrium Density',
    mass: 'ρ* ≈ 0.03706',
    massLabel: 'Mean-Field Fixed Point',
    qbdMass: <span>Λ<sub>0</sub> = 2<sup>−6</sup> | λ<sub>0</sub> = e − 1 | μ<sub>0</sub> = 1/√(2π)</span>,
    qbdMassLabel: 'Constitutive Priors (§4.4)',
    writheConfig: 'Calibration Baseline',
    description: (
      <span>
        The pre-geometric vacuum substrate is governed by constitutive informational constants rather than a heat bath (§4.4.2): base-conversion modulus β<sub>c</sub> = ln(2) (1 bit = ln 2 nats; physical temperature cancels), simplicial permittivity Λ<sub>0</sub> = 2<sup>−6</sup> = 0.015625, friction μ<sub>0</sub> = 1/√(2π) ≈ 0.3989, and catalytic generator λ<sub>0</sub> = e − 1 ≈ 1.7183. These fix the driven mean-field equilibrium ρ* ≈ 0.037061 and unpumped discrete-ensemble mean ρ<sub>3</sub>* ≈ 0.0290 (§5.2–5.4).
      </span>
    ),
    colorType: 'gold'
  }
];

const rowLabels: React.ReactNode[] = [
  <span>UP-TYPE QUARKS<br /><span style={{ fontSize: '0.75rem', color: '#8b949e', fontWeight: 'normal' }}>(Asymmetric Braids)</span></span>,
  <span>DOWN-TYPE QUARKS<br /><span style={{ fontSize: '0.75rem', color: '#8b949e', fontWeight: 'normal' }}>(Asymmetric Braids)</span></span>,
  <span>CHARGED LEPTONS<br /><span style={{ fontSize: '0.75rem', color: '#8b949e', fontWeight: 'normal' }}>(Symmetric Braids)</span></span>,
  <span>NEUTRINOS<br /><span style={{ fontSize: '0.75rem', color: '#8b949e', fontWeight: 'normal' }}>(Folded Loops)</span></span>
];

export default function ParticleSpectrumPage() {
  const [selectedParticle, setSelectedParticle] = useState<ParticleData | null>(null);

  const getCellForCoords = (r: number, c: number) => {
    return particles.find(p => p.row === r && p.col === c);
  };

  return (
    <Layout
      title="QBD Particle Spectrum"
      description="Quantum Braid Dynamics Particle Spectrum Wall Chart. A technical scientific blueprint layout detailing emergent Standard Model states."
    >
      <Head>
        <meta name="robots" content="index, follow" />
        <meta property="og:title" content="Quantum Braid Dynamics Particle Spectrum Chart" />
        {/* Force page background to deep dark slate blueprint color */}
        <style dangerouslySetInnerHTML={{__html: `
          body {
            background-color: #0D1117 !important;
          }
          /* Scrollbar blueprint customization */
          ::-webkit-scrollbar {
            height: 8px;
            width: 8px;
          }
          ::-webkit-scrollbar-track {
            background: #0D1117;
            border-left: 1px dashed rgba(0, 245, 255, 0.15);
          }
          ::-webkit-scrollbar-thumb {
            background: rgba(0, 245, 255, 0.2);
            border-radius: 4px;
          }
          ::-webkit-scrollbar-thumb:hover {
            background: rgba(0, 245, 255, 0.4);
          }
        `}} />
      </Head>

      <main className="spectrum-page-container">
        <div className="spectrum-content">

          {/* Header */}
          <div className="spectrum-header">
            <HeroNetworkCanvas />
            <h1 className="spectrum-title">QUANTUM BRAID DYNAMICS (QBD) PARTICLE SPECTRUM</h1>
            <p className="spectrum-subtitle">
              Topological and geometric invariants of standard model fermions and gauge boson states mapped as emergent knot and rewrite systems on the relational pre-geometric vacuum substrate.
            </p>
            <div className="spectrum-header-corners" />
          </div>

          {/* Mobile / Narrow Viewport Scroll Hint */}
          <div className="spectrum-scroll-hint">
            <span>⇄</span> Swipe horizontally to explore all generations &amp; vacuum states
          </div>

          {/* Matrix Area */}
          <div className="spectrum-matrix-wrapper">
            <div className="spectrum-matrix-grid">

              {/* Top Corner Empty Header */}
              <div style={{ borderBottom: '2px solid rgba(255,255,255,0.06)' }}></div>

              <div className="spectrum-super-header matter-super combined-header">
                <span className="spectrum-super-title">Three Generations of Matter (Fermions)</span>
                <div className="spectrum-sub-labels">
                  <div className="spectrum-sub-label">Generation I</div>
                  <div className="spectrum-sub-label">Generation II</div>
                  <div className="spectrum-sub-label">Generation III</div>
                </div>
              </div>

              <div className="spectrum-super-header gauge-super combined-header col-4-header single-title-header">
                <span className="spectrum-super-title">Gauge Fields (Rewrites)</span>
              </div>

              <div className="spectrum-super-header vacuum-super combined-header col-5-header single-title-header">
                <span className="spectrum-super-title">Vacuum Substrate<br />(Topology)</span>
              </div>

              {/* Grid Rows */}
              {[1, 2, 3, 4].map((r) => (
                <React.Fragment key={r}>

                  {/* Row Header */}
                  <div className="spectrum-row-label-cell">
                    <div className="spectrum-row-label-text">{rowLabels[r - 1]}</div>
                  </div>

                  {/* 5 Cards for standard and empty/legend cells */}
                  {[1, 2, 3, 4, 5].map((c) => {
                    const p = getCellForCoords(r, c);

                    if (!p) {
                      return (
                        <div
                          key={c}
                          style={{
                            backgroundColor: 'rgba(255,255,255,0.01)',
                            border: '1px dashed rgba(255,255,255,0.04)',
                            borderRadius: '8px',
                            minHeight: '240px'
                          }}
                        />
                      );
                    }

                    return (
                      <div
                        key={c}
                        className={`spectrum-card ${p.colorType}-glow ${c === 5 ? `col-5-card row-${r}-card` : ''}`}
                        onClick={() => setSelectedParticle(p)}
                      >
                        {/* Large Background Symbol Watermark */}
                        <div className={`spectrum-card-symbol ${p.symbol.length > 1 ? 'wide-symbol' : ''}`}>{p.symbol}</div>

                        {/* Header: Mass & Charge */}
                        <div className="spectrum-card-header">
                          <span className="spectrum-card-mass">
                            {p.mass}
                          </span>
                          <span className={`spectrum-card-charge ${p.colorType}-text`}>
                            {p.charge}
                          </span>
                        </div>

                        {/* Graphic Braid Container */}
                        <div className="spectrum-card-graphic-container">
                          <ParticleGraphic symbol={p.symbol} isCard={true} />
                        </div>

                        {/* Footer Details */}
                        <div className="spectrum-card-footer">
                          <div className="spectrum-card-name">{p.name}</div>
                          {p.symbol === 'ρ*' ? (
                            <div className="spectrum-card-constants-micro">
                              <div>Λ<sub>0</sub> = 2<sup>−6</sup> | μ<sub>0</sub> ≈ 0.3989</div>
                              <div>λ<sub>0</sub> = e−1 | ℓ<sub>0</sub> ≈ 1.62×10<sup>−35</sup> m</div>
                            </div>
                          ) : (
                            <div className="spectrum-card-param">{p.param}</div>
                          )}
                        </div>
                      </div>
                    );
                  })}

                </React.Fragment>
              ))}

            </div>
          </div>

        </div>

        {/* Modal Overlay */}
        {selectedParticle && (
          <div className="spectrum-modal-overlay" onClick={() => setSelectedParticle(null)}>
            <div className="spectrum-modal-content" onClick={(e) => e.stopPropagation()}>
              <button className="spectrum-modal-close" onClick={() => setSelectedParticle(null)}>×</button>

              <div className="spectrum-modal-header">
                <div className={`spectrum-modal-symbol-badge ${selectedParticle.colorType}-badge`}>
                  {selectedParticle.symbol}
                </div>
                <div>
                  <h2 className="spectrum-modal-title">{selectedParticle.name}</h2>
                  <div className="spectrum-modal-subtitle">{selectedParticle.param}</div>
                </div>
              </div>

              <div className="spectrum-modal-body">
                <div className="spectrum-modal-grid">

                  {/* Left Column: Clean Unobstructed SVG Graphic */}
                  <div className={`spectrum-modal-left ${selectedParticle.colorType}-border`}>
                    <div className="spectrum-modal-left-graphic">
                      <ParticleGraphic symbol={selectedParticle.symbol} />
                    </div>
                  </div>

                  {/* Right Column: Descriptions & parameters */}
                  <div>
                    <p style={{ margin: '0 0 1.25rem 0' }}>
                      {selectedParticle.description}
                    </p>

                    <h4 style={{ margin: '0 0 0.5rem 0', color: '#ffffff', fontFamily: 'monospace' }}>TOPOLOGICAL INVARIANTS</h4>
                    <div className="spectrum-modal-parameters">
                      <div className="spectrum-modal-param-label">
                        {selectedParticle.chargeLabel || 'Electric Charge'}
                      </div>
                      <div className={`spectrum-modal-param-value ${selectedParticle.colorType}-text`}>
                        {selectedParticle.modalCharge ?? (selectedParticle.charge || '0')}
                      </div>

                      <div className="spectrum-modal-param-label">Writhe / Topology</div>
                      <div className="spectrum-modal-param-value">{selectedParticle.writheConfig}</div>

                      <div className="spectrum-modal-param-label">
                        {selectedParticle.complexityLabel || <span>Net Complexity (N<sub>3</sub>)</span>}
                      </div>
                      <div className="spectrum-modal-param-value">{selectedParticle.complexity}</div>

                      <div className="spectrum-modal-param-label">
                        {selectedParticle.massLabel || 'Observed Mass (SM)'}
                      </div>
                      <div className="spectrum-modal-param-value">{selectedParticle.mass}</div>

                      {selectedParticle.qbdMass && (
                        <>
                          <div className="spectrum-modal-param-label">
                            {selectedParticle.qbdMassLabel || 'QBD Prediction'}
                          </div>
                          <div className={`spectrum-modal-param-value ${selectedParticle.colorType}-text`}>
                            {selectedParticle.qbdMass}
                          </div>
                        </>
                      )}
                    </div>
                  </div>

                </div>

                <div style={{ textAlign: 'right', marginTop: '1.25rem' }}>
                  <button
                    className="button button--secondary button--sm"
                    onClick={() => setSelectedParticle(null)}
                    style={{ border: '1px solid rgba(255,255,255,0.1)' }}
                  >
                    Close Parameters
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}
      </main>
    </Layout>
  );
}

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
  charge: string;
  param: React.ReactNode;
  complexity: React.ReactNode;
  mass: string;
  writheConfig: string;
  description: string;
  colorType: 'blue' | 'green' | 'red' | 'gold';
}

const particles: ParticleData[] = [
  // ROW 1: UP-TYPE QUARKS & SCALAR (Strong/Higgs/Scalar)
  {
    row: 1,
    col: 1,
    symbol: 'u',
    name: 'Up Quark',
    charge: '+2/3 e',
    param: 'Writhe: +2/3',
    complexity: <span>1 (N<sub>3</sub>)</span>,
    mass: '2.2 MeV',
    writheConfig: '(1, 1, 0)',
    description: 'Chiral tripartite asymmetric braid configuration with writhe vector (1, 1, 0). The asymmetry accounts for its fractional electric charge (+2/3) and strong force color charges in the pre-geometric causal network.',
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
    writheConfig: '(62, 62, 0)',
    description: 'Second-generation up-type quark mapped to the crossing-well boundary configuration in the causal network. Its twist state is wound to writhe vector (62, 62, 0), exhibiting intermediate complexity.',
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
    writheConfig: '(712, 712, 0)',
    description: 'Third-generation up-type quark exhibiting massive torsion peak stress in the pre-geometric graph. Its extremely dense writhe configuration (712, 712, 0) yields over one million geometric 3-cycle quanta.',
    colorType: 'blue'
  },
  {
    row: 1,
    col: 4,
    symbol: 'g',
    name: 'Gluon',
    charge: '',
    param: 'su(3) Adjoint Swaps',
    complexity: '8 (Adjoint)',
    mass: '0.0 MeV',
    writheConfig: 'SU(3) Adjoint Rewrite',
    description: 'Emergent gauge boson representing logical graph rewrite swaps in the su(3) adjoint representation. Mediates color exchanges between quarks by dynamically swapping ribbon indices.',
    colorType: 'red'
  },
  {
    row: 1,
    col: 5,
    symbol: 'β₅',
    name: 'Pentaribbon',
    charge: '',
    param: 'Unified State',
    complexity: <span>5 (Strands)</span>,
    mass: 'GUT Scale',
    writheConfig: 'SU(5) Unified Braid',
    description: 'A five-strand composite Braid representing the unified pre-geometric state at grand unification energy scales. Local adjacent swap rewrites of this pentaribbon configuration generate the SU(5) Lie algebra, embedding both quarks and leptons as distinct topological phases.',
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
    writheConfig: '(-1, 0, 0)',
    description: 'Chiral tripartite asymmetric braid with writhe vector (-1, 0, 0), giving it an electric charge of -1/3. Its bare geometric mass is low, but QCD binding energy dominates its observed current mass.',
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
    writheConfig: '(-24, 0, 0)',
    description: 'Second-generation down-type quark with writhe vector (-24, 0, 0). Exhibits intermediate complexity in the crossing well, resulting in an observed rest mass of approximately 95.0 MeV.',
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
    writheConfig: '(-157, 0, 0)',
    description: 'Third-generation down-type quark with writhe vector (-157, 0, 0). Its high complexity yields a rest mass of 4,180 MeV, validating the QBD mass functional scaling.',
    colorType: 'blue'
  },
  {
    row: 2,
    col: 4,
    symbol: 'γ',
    name: 'Photon',
    charge: '',
    param: 'U(1) Frame Twist',
    complexity: '2 (Twist)',
    mass: '0.0 MeV',
    writheConfig: 'U(1) Frame twist',
    description: 'Massless gauge field representing a U(1) frame twist rewrite on the causal network. It corresponds to a topological twist action propagating along the vacuum substrate.',
    colorType: 'red'
  },
  {
    row: 2,
    col: 5,
    symbol: 'β₃',
    name: 'Tripartite Braid',
    charge: '',
    param: 'Topological Quantum',
    complexity: <span>3 (Strands)</span>,
    mass: 'Ground State',
    writheConfig: 'Unbraided base manifold',
    description: 'The fundamental tripartite (three-strand) braid representing the stable topological ground state of the pre-geometric vacuum. Stable knotting configurations of this braid under deletions and noise give rise to the three generations of elementary leptons and quarks.',
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
    writheConfig: '(-1, -1, -1)',
    description: 'Minimal stable symmetric 3-braid configuration with writhe vector (-1, -1, -1). Its charge permutation group acts symmetrically, yielding an electric charge of -1 and stable rest mass.',
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
    writheConfig: '(-14, -14, -14)',
    description: 'Second-generation charged lepton defined as a symmetric braid with tighter twists (-14, -14, -14). It acts as a resonant isomer of the electron with identical symmetry but higher localized self-strain.',
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
    mass: '1,776.86 MeV',
    writheConfig: '(-59, -59, -59)',
    description: 'Third-generation charged lepton representing a highly wound symmetric braid (-59, -59, -59). The quadratic energy barrier of its twist configuration matches the observed tau mass to within 0.2%.',
    colorType: 'green'
  },
  {
    row: 3,
    col: 4,
    symbol: 'Z',
    name: 'Z Boson',
    charge: '',
    param: <span>su(2)<sub>L</sub> Neutrality</span>,
    complexity: '12 (Fusion)',
    mass: '91,187.6 MeV',
    writheConfig: 'Neutral Weak Braid Fusion',
    description: 'Neutral weak boson representing a loop fusion rewrite on the network. Operates as a short-range, massive force carrier through symmetric graph identification events.',
    colorType: 'red'
  },
  {
    row: 3,
    col: 5,
    symbol: 'H',
    name: 'Higgs Boson',
    charge: '',
    param: '3-Cycle Condensate',
    complexity: 'Vacuum Condensate Density',
    mass: '125.09 GeV',
    writheConfig: 'Unbroken Vacuum Stabilizer',
    description: 'Within the QBD framework, the Higgs boson emerges as a coherent excitation of the pre-geometric vacuum\'s 3-cycle density (ρ*). Rather than postulating a fundamental scalar field, mass generation arises dynamically from this localized fluctuation in the geometric condensate, which exerts topological drag on propagating fermions and vector bosons.',
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
    complexity: <span>0 (N<sub>3</sub>)</span>,
    mass: '< 0.00012 MeV',
    writheConfig: '(0, 0, 0) Folded',
    description: 'Folded loop configuration representing the minimal color-neutral, charge-neutral vacuum topology. Exhibits zero bare writhe (0, 0, 0) and extremely low emergent mass via seesaw dynamics.',
    colorType: 'green'
  },
  {
    row: 4,
    col: 2,
    symbol: 'νμ',
    name: 'Muon Neutrino',
    charge: '0',
    param: 'Folded Gen II',
    complexity: <span>18 (N<sub>3</sub>)</span>,
    mass: '< 0.19 MeV',
    writheConfig: 'Folded Gen II Twist',
    description: 'Second-generation folded neutrino configuration. Has a double-twist folded geometry at its vertex, creating higher localized complexity than the first generation.',
    colorType: 'green'
  },
  {
    row: 4,
    col: 3,
    symbol: 'ντ',
    name: 'Tau Neutrino',
    charge: '0',
    param: 'Folded Gen III',
    complexity: <span>36 (N<sub>3</sub>)</span>,
    mass: '< 18.2 MeV',
    writheConfig: 'Folded Gen III Twist',
    description: 'Third-generation folded neutrino configuration. Features a triple-twist folded structure resulting in a heavier neutrino mass boundary while remaining color and charge neutral.',
    colorType: 'green'
  },
  {
    row: 4,
    col: 4,
    symbol: 'W',
    name: 'W Boson',
    charge: '±1 e',
    param: 'su(2) Charged Swaps',
    complexity: '12 (Charged rewrite)',
    mass: '80,379.0 MeV',
    writheConfig: 'SU(2) Chiral Rewrite',
    description: 'Charged weak boson representing an active su(2) charged rewrite transition. Mediates flavor changes (e.g., Up to Down quark conversions) by altering the braid\'s chiral twists at local vertices.',
    colorType: 'red'
  },
  {
    row: 4,
    col: 5,
    symbol: 'ρ*',
    name: 'Vacuum Substrate',
    charge: 'T = ln(2)',
    param: 'Calibration & Constants',
    complexity: <span>ρ* ≈ 0.03699</span>,
    mass: 'ρ* ≈ 0.03699',
    writheConfig: 'Calibration Baseline',
    description: <span>The pre-geometric vacuum substrate parameters define the fundamental constants of the topological network. These include the equilibrium 3-cycle density (ρ*), friction modulus (μ*), and the relaxation rate of local rewrites (Γ<sub>vac</sub>) which dictate the background dynamics and emergent mass scales.</span>,
    colorType: 'gold'
  }
];

// Column sub-labels are now merged directly inside the combined header row.

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
                    
                    const isAmber = p.colorType === 'amber';
                    
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
                              <div>α<sub>vac</sub> ≈ 0.0073 | μ* ≈ 0.3989</div>
                              <div>Λ<sub>L</sub> ≈ 1.61 × 10⁻³⁵ m</div>
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
                <h2 className="spectrum-modal-title">{selectedParticle.name}</h2>
                <div className="spectrum-modal-subtitle">{selectedParticle.param}</div>
              </div>

              <div className="spectrum-modal-body">
                <div className="spectrum-modal-grid">
                  
                  {/* Left Column: Large Image */}
                  <div className={`spectrum-modal-left ${selectedParticle.colorType}-border`}>
                    <div className="spectrum-modal-left-symbol">{selectedParticle.symbol}</div>
                    <div className="spectrum-modal-left-graphic">
                      <ParticleGraphic symbol={selectedParticle.symbol} />
                    </div>
                  </div>

                  {/* Right Column: Descriptions & parameters */}
                  <div>
                    <p style={{ margin: '0 0 1.5rem 0' }}>
                      {selectedParticle.description}
                    </p>

                    <h4 style={{ margin: '0 0 0.5rem 0', color: '#ffffff', fontFamily: 'monospace' }}>TOPOLOGICAL INVARIANTS</h4>
                    <div className="spectrum-modal-parameters">
                      <div className="spectrum-modal-param-label">
                        {selectedParticle.symbol === 'ρ*' ? 'Vacuum Temp (T)' : 'Electric Charge'}
                      </div>
                      <div className={`spectrum-modal-param-value ${selectedParticle.colorType}-text`}>
                        {selectedParticle.charge || '0'}
                      </div>

                      <div className="spectrum-modal-param-label">Writhe Config</div>
                      <div className="spectrum-modal-param-value">{selectedParticle.writheConfig}</div>

                      <div className="spectrum-modal-param-label">Net Complexity (N₃)</div>
                      <div className="spectrum-modal-param-value">{selectedParticle.complexity}</div>

                      <div className="spectrum-modal-param-label">Topological Mass</div>
                      <div className="spectrum-modal-param-value">{selectedParticle.mass}</div>
                    </div>
                  </div>

                </div>

                <div style={{ textAlign: 'right', marginTop: '1.5rem' }}>
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

import React, { useState } from 'react';
import Layout from '@theme/Layout';
import Head from '@docusaurus/Head';
import { ParticleGraphic } from '../components/graphics/spectrum-graphics';

interface ParticleData {
  row: number;
  col: number;
  symbol: string;
  name: string;
  charge: string;
  param: string;
  complexity: string;
  mass: string;
  writheConfig: string;
  description: string;
  colorType: 'blue' | 'amber';
}

const particles: ParticleData[] = [
  // ROW 1: QUARKS (Asymmetric Braids)
  {
    row: 1,
    col: 1,
    symbol: 'u',
    name: 'Up Quark',
    charge: '+2/3 e',
    param: 'Writhe: +2/3',
    complexity: '1 (N₃)',
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
    complexity: '7,626 (N₃)',
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
    complexity: '1,013,176 (N₃)',
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
    charge: '0',
    param: 'su(3) Adjoint Swaps',
    complexity: '8 (Adjoint)',
    mass: '0.0 MeV',
    writheConfig: 'SU(3) Adjoint Rewrite',
    description: 'Emergent gauge boson representing logical graph rewrite swaps in the su(3) adjoint representation. Mediates color exchanges between quarks by dynamically swapping ribbon indices.',
    colorType: 'blue'
  },

  // ROW 2: LEPTONS (Symmetric Braids)
  {
    row: 2,
    col: 1,
    symbol: 'e',
    name: 'Electron',
    charge: '-1 e',
    param: 'Writhe: -1',
    complexity: '3 (N₃)',
    mass: '0.511 MeV',
    writheConfig: '(-1, -1, -1)',
    description: 'Minimal stable symmetric 3-braid configuration with writhe vector (-1, -1, -1). Its charge permutation group acts symmetrically, yielding an electric charge of -1 and stable rest mass.',
    colorType: 'blue'
  },
  {
    row: 2,
    col: 2,
    symbol: 'μ',
    name: 'Muon',
    charge: '-1 e',
    param: 'Symmetric C2',
    complexity: '588 (N₃)',
    mass: '105.66 MeV',
    writheConfig: '(-14, -14, -14)',
    description: 'Second-generation charged lepton defined as a symmetric braid with tighter twists (-14, -14, -14). It acts as a resonant isomer of the electron with identical symmetry but higher localized self-strain.',
    colorType: 'blue'
  },
  {
    row: 2,
    col: 3,
    symbol: 'τ',
    name: 'Tau',
    charge: '-1 e',
    param: 'Symmetric C3',
    complexity: '10,443 (N₃)',
    mass: '1,776.86 MeV',
    writheConfig: '(-59, -59, -59)',
    description: 'Third-generation charged lepton representing a highly wound symmetric braid (-59, -59, -59). The quadratic energy barrier of its twist configuration matches the observed tau mass to within 0.2%.',
    colorType: 'blue'
  },
  {
    row: 2,
    col: 4,
    symbol: 'γ',
    name: 'Photon',
    charge: '0',
    param: 'U(1) Frame Twist',
    complexity: '2 (Twist)',
    mass: '0.0 MeV',
    writheConfig: 'U(1) Frame twist',
    description: 'Massless gauge field representing a U(1) frame twist rewrite on the causal network. It corresponds to a topological twist action propagating along the vacuum substrate.',
    colorType: 'blue'
  },

  // ROW 3: NEUTRINOS (Folded Loops)
  {
    row: 3,
    col: 1,
    symbol: 'νe',
    name: 'Electron Neutrino',
    charge: '0',
    param: 'Folded Gen I',
    complexity: '0 (N₃)',
    mass: '< 0.00012 MeV',
    writheConfig: '(0, 0, 0) Folded',
    description: 'Folded loop configuration representing the minimal color-neutral, charge-neutral vacuum topology. Exhibits zero bare writhe (0, 0, 0) and extremely low emergent mass via seesaw dynamics.',
    colorType: 'amber'
  },
  {
    row: 3,
    col: 2,
    symbol: 'νμ',
    name: 'Muon Neutrino',
    charge: '0',
    param: 'Folded Gen II',
    complexity: '18 (N₃)',
    mass: '< 0.19 MeV',
    writheConfig: 'Folded Gen II Twist',
    description: 'Second-generation folded neutrino configuration. Has a double-twist folded geometry at its vertex, creating higher localized complexity than the first generation.',
    colorType: 'amber'
  },
  {
    row: 3,
    col: 3,
    symbol: 'ντ',
    name: 'Tau Neutrino',
    charge: '0',
    param: 'Folded Gen III',
    complexity: '36 (N₃)',
    mass: '< 18.2 MeV',
    writheConfig: 'Folded Gen III Twist',
    description: 'Third-generation folded neutrino configuration. Features a triple-twist folded structure resulting in a heavier neutrino mass boundary while remaining color and charge neutral.',
    colorType: 'amber'
  },
  {
    row: 3,
    col: 4,
    symbol: 'Z',
    name: 'Z Boson',
    charge: '0',
    param: 'su(2)_L Neutrality',
    complexity: '12 (Fusion)',
    mass: '91,187.6 MeV',
    writheConfig: 'Neutral Weak Braid Fusion',
    description: 'Neutral weak boson representing a loop fusion rewrite on the network. Operates as a short-range, massive force carrier through symmetric graph identification events.',
    colorType: 'amber'
  },

  // ROW 4: D-QUARKS (Asymmetric Braids)
  {
    row: 4,
    col: 1,
    symbol: 'd',
    name: 'Down Quark',
    charge: '-1/3 e',
    param: 'Writhe: -1/3',
    complexity: '1 (N₃)',
    mass: '4.7 MeV',
    writheConfig: '(-1, 0, 0)',
    description: 'Chiral tripartite asymmetric braid with writhe vector (-1, 0, 0), giving it an electric charge of -1/3. Its bare geometric mass is low, but QCD binding energy dominates its observed current mass.',
    colorType: 'amber'
  },
  {
    row: 4,
    col: 2,
    symbol: 's',
    name: 'Strange Quark',
    charge: '-1/3 e',
    param: 'S2 Crossing',
    complexity: '576 (N₃)',
    mass: '95.0 MeV',
    writheConfig: '(-24, 0, 0)',
    description: 'Second-generation down-type quark with writhe vector (-24, 0, 0). Exhibits intermediate complexity in the crossing well, resulting in an observed rest mass of approximately 95.0 MeV.',
    colorType: 'amber'
  },
  {
    row: 4,
    col: 3,
    symbol: 'b',
    name: 'Bottom Quark',
    charge: '-1/3 e',
    param: 'B3 Crossing',
    complexity: '24,649 (N₃)',
    mass: '4,180.0 MeV',
    writheConfig: '(-157, 0, 0)',
    description: 'Third-generation down-type quark with writhe vector (-157, 0, 0). Its high complexity yields a rest mass of 4,180 MeV, validating the QBD mass functional scaling.',
    colorType: 'amber'
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
    colorType: 'amber'
  }
];

const colLabels = [
  'Generation I (Well C1)',
  'Generation II (Well C2)',
  'Generation III (Well C3)',
  'Gauge Fields (Rewrites)'
];

const rowLabels = [
  'QUARKS (Asymmetric Braids)',
  'LEPTONS (Symmetric Braids)',
  'NEUTRINOS (Folded Loops)',
  'D-QUARKS (Asymmetric Braids)'
];

export default function ParticleSpectrumPage() {
  const [selectedParticle, setSelectedParticle] = useState<ParticleData | null>(null);

  const getCellForCoords = (r: number, c: number) => {
    return particles.find(p => p.row === r && p.col === c);
  };

  return (
    <Layout
      title="QBD Particle Spectrum"
      description="Quantum Braid Dynamics Particle Spectrum Wall Chart. An immaculate scientific blueprint layout detailing emergent Standard Model states."
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
            <div className="spectrum-title-tag">
              <span style={{
                width: '6px',
                height: '6px',
                borderRadius: '50%',
                backgroundColor: '#ffb01f',
                display: 'inline-block',
                boxShadow: '0 0 6px #ffb01f',
                marginRight: '0.25rem'
              }} />
              VACUUM RESONANCE MAPPING
            </div>
            <h1 className="spectrum-title">QUANTUM BRAID DYNAMICS (QBD) PARTICLE SPECTRUM</h1>
            <p className="spectrum-subtitle">
              Topological invariants and geometric invariants of standard model fermions and gauge boson states mapped as emergent knot and rewrite systems on the relational pre-geometric vacuum substrate.
            </p>
          </div>

          {/* Matrix Area */}
          <div className="spectrum-matrix-wrapper">
            <div className="spectrum-matrix-grid">
              
              {/* Corner Empty Header */}
              <div style={{ borderBottom: '2px solid rgba(255,255,255,0.06)' }}></div>

              {/* Column Headers */}
              {colLabels.map((label, idx) => (
                <div key={idx} className="spectrum-col-label-cell">
                  <div className="spectrum-col-label-text">{label}</div>
                </div>
              ))}

              {/* Grid Rows */}
              {[1, 2, 3, 4].map((r) => (
                <React.Fragment key={r}>
                  
                  {/* Row Header */}
                  <div className="spectrum-row-label-cell">
                    <div className="spectrum-row-label-text">{rowLabels[r - 1]}</div>
                  </div>

                  {/* 4 Cards for this row */}
                  {[1, 2, 3, 4].map((c) => {
                    const p = getCellForCoords(r, c);
                    if (!p) return <div key={c} style={{ backgroundColor: 'rgba(0,0,0,0.2)' }} />;
                    
                    const isAmber = p.colorType === 'amber';
                    
                    return (
                      <div 
                        key={c} 
                        className={`spectrum-card ${isAmber ? 'amber-glow' : ''}`}
                        onClick={() => setSelectedParticle(p)}
                      >
                        {/* Header: Index & Charge */}
                        <div className="spectrum-card-header">
                          <span className="spectrum-card-index">{`S(${r},${c})`}</span>
                          <span className={`spectrum-card-charge ${isAmber ? 'amber-text' : ''}`}>
                            {p.charge}
                          </span>
                        </div>

                        {/* Graphic Braid Container */}
                        <div className="spectrum-card-graphic-container">
                          <div className="spectrum-card-symbol">{p.symbol}</div>
                          <ParticleGraphic symbol={p.symbol} />
                        </div>

                        {/* Footer Details */}
                        <div className="spectrum-card-footer">
                          <div className="spectrum-card-name">{p.name}</div>
                          <div className="spectrum-card-param">{p.param}</div>
                        </div>
                      </div>
                    );
                  })}

                </React.Fragment>
              ))}

            </div>
          </div>

          {/* Footer Plinth */}
          <div className="spectrum-footer-plinth">
            <div className="spectrum-footer-plinth-label">THE GEOMETRIC VACUUM SUBSTRATE</div>
            <div className="spectrum-footer-plinth-text">
              Equilibrium 3-Cycle Density: <span className="spectrum-footer-plinth-highlight">ρ* ≈ 0.03</span>
              <span style={{ margin: '0 1.5rem', opacity: 0.3 }}>|</span>
              Friction Modulus: <span className="spectrum-footer-plinth-highlight">μ ≈ 0.40</span>
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
                  <div className={`spectrum-modal-left ${selectedParticle.colorType === 'amber' ? 'amber-border' : ''}`}>
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
                      <div className="spectrum-modal-param-label">Electric Charge</div>
                      <div className="spectrum-modal-param-value" style={{ color: selectedParticle.colorType === 'amber' ? '#ffb01f' : '#00f5ff' }}>
                        {selectedParticle.charge}
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

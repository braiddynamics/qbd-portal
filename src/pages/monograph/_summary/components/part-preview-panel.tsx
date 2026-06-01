import React from 'react';
import { partsList } from '../data/previews';

interface FlowStep {
  num: string;
  title: string;
  taxonomy: string;
  question: string;
  ingredients: string;
}

interface PartPreviewData {
  title: string;
  subtitle: string;
  paragraphs: string[];
  steps: FlowStep[];
}

const PREVIEW_REGISTRY: Record<number, PartPreviewData> = {
  0: {
    title: "🔬 DEDUCTIVE COSMOLOGICAL CHAIN",
    subtitle: "Constructing the Physical Universe",
    paragraphs: [
      "In Part 1, The Foundational Principles begins the construction of the physical universe as a deductive chain, moving from abstract requirements to concrete emergence.",
      "By starting with pure ontology and layering axiomatic constraints, this framework systematically derives the geometry of our continuous universe from discrete graph updates.",
      "Through this process, local relational updates yield a stable macroscopic phase of spacetime, demonstrating that the physical laws we observe are the inevitable thermodynamic equilibrium of a deeper computational reality."
    ],
    steps: [
      {
        num: '01',
        title: 'SUBSTRATE',
        taxonomy: 'Ontology',
        question: 'What Exists?',
        ingredients: 'Vertices, Edges, Logical Time',
      },
      {
        num: '02',
        title: 'CONSTRAINTS',
        taxonomy: 'Axioms',
        question: 'What is Allowed?',
        ingredients: 'Irreflexivity, No-Cloning, Acyclicity',
      },
      {
        num: '03',
        title: 'OBJECT MODEL',
        taxonomy: 'Architecture',
        question: 'Where do we Start?',
        ingredients: 'Regular Bethe Vacuum Tree',
      },
      {
        num: '04',
        title: 'OPERATIONS',
        taxonomy: 'Dynamics',
        question: 'How does it Move?',
        ingredients: 'Universal Constructor & Local Awareness',
      },
      {
        num: '05',
        title: 'GEOMETROGENESIS',
        taxonomy: 'Equilibrium',
        question: 'What does it Become?',
        ingredients: 'Dimensionality & Thermodynamic Phases',
      }
    ]
  },
  1: {
    title: "🔬 TOPOLOGICAL NATURE OF MATTER",
    subtitle: "The Players in the Network",
    paragraphs: [
      "In Part 2, The Topological Nature of Matter shifts our perspective from empty space to the localized excitations that form physical matter, proving that elementary particles are not point-like inputs, but stable topological knots.",
      "By modeling particles as localized tripartite braids, the framework demonstrates that fundamental properties (such as spin, mass, and three distinct families of matter) arise naturally from the structural writhe of network strands.",
      "Through coordinate-free ribbon swaps, gauge symmetries like electromagnetism and the nuclear forces emerge as simple geometric preservation rules, uniting particle physics and topology under a single computational paradigm."
    ],
    steps: [
      {
        num: '06',
        title: 'PARTICLES',
        taxonomy: 'Fermions',
        question: 'What is Matter?',
        ingredients: 'Localized 3-Strand Tripartite Braids',
      },
      {
        num: '07',
        title: 'CHARGE',
        taxonomy: 'Writhe',
        question: 'Why is Charge Quantized?',
        ingredients: 'Fractional Writhe Polynomial Thirds',
      },
      {
        num: '08',
        title: 'GAUGE SYMMETRIES',
        taxonomy: 'Ribbon Swaps',
        question: 'Where do Forces Come From?',
        ingredients: 'SU(3) × SU(2) × U(1) Coord-free Swaps',
      },
      {
        num: '09',
        title: 'GENERATIONS',
        taxonomy: 'Families',
        question: 'Why Three Families?',
        ingredients: 'Three Stable Topological Twist States',
      },
      {
        num: '10',
        title: 'QUANTUM COMPUTATION',
        taxonomy: 'Gates',
        question: 'Can the Universe Compute?',
        ingredients: 'Universal Fault-Tolerant Swap Circuits',
      }
    ]
  },
  2: {
    title: "🔬 EMERGENT REALITY",
    subtitle: "The Stage of Spacetime",
    paragraphs: [
      "In Part 3, Emergent Reality constructs the cosmological stage, demonstrating how the discrete, metric-free updates of a causal poset transition into the smooth curved geometry of General Relativity.",
      "By tracking parallel transport across network cycles, the framework proves that Einstein's field equations are not fundamental postulates, but the macroscopic statistical average of microscopic information conservation.",
      "Through this continuous limit, discrete topological cycles converge into smooth, curved Riemannian manifolds under the Gromov-Hausdorff-Prokhorov metric. This mathematical convergence bridges the gap between discrete causal networks and the classical spacetime coordinate systems of general relativity, showing that gravity is an emergent thermodynamic property of the network.",
      "Finally, by treating entanglement as physical wormhole connections and boundaries as error-correcting codes, holography and quantum geometry emerge not as mathematical curiosities, but as the foundational mechanics of space itself."
    ],
    steps: [
      {
        num: '11',
        title: 'CURVATURE',
        taxonomy: 'Discrete Connection',
        question: 'How is Curvature Bounded?',
        ingredients: 'Discrete Exterior Calculus (d² = 0)',
      },
      {
        num: '12',
        title: 'EINSTEIN EQUATIONS',
        taxonomy: 'Gravity',
        question: 'What Causes Gravity?',
        ingredients: 'Network Update Erasure Balances',
      },
      {
        num: '13',
        title: 'METRIC CONVERGENCE',
        taxonomy: 'Manifolds',
        question: 'How does Space Become Smooth?',
        ingredients: 'Gromov-Hausdorff-Prokhorov Limits',
      },
      {
        num: '15',
        title: 'ENTANGLEMENT',
        taxonomy: 'ER = EPR',
        question: 'What is Physical Distance?',
        ingredients: 'Non-local Entanglement Connections',
      },
      {
        num: '16',
        title: 'HOLOGRAPHY',
        taxonomy: 'Bulk-Boundary',
        question: 'Where is Space Coded?',
        ingredients: 'AdS/CFT Quantum Error-Correcting Codes',
      },
      {
        num: '17',
        title: 'STRING LIMIT',
        taxonomy: 'Worldsheets',
        question: 'What do Braids Sweep Out?',
        ingredients: '2D Nambu-Goto Worldsheet Actions',
      }
    ]
  },
  3: {
    title: "🔬 PHENOMENOLOGICAL CONSEQUENCES",
    subtitle: "The Output of the Cosmos",
    paragraphs: [
      "In Part 4, Phenomenological Consequences turns our mathematical machinery toward the sky, deriving the large-scale cosmological events and mysterious dark sectors that govern our actual universe.",
      "By tracing the evolution of network updates, the framework derives autocatalytic inflation and the subsequent settling of thermal stress into the vast voids and filaments of the cosmic web.",
      "Remarkably, classical black hole singularities and dark energy emerge not as mathematical crises, but as natural quantized boundaries, where maximum edge densities limit collapse and empty relic vacancies exert cosmic pressure."
    ],
    steps: [
      {
        num: '18',
        title: 'INFLATION',
        taxonomy: 'Autocatalysis',
        question: 'How did Space Expand?',
        ingredients: 'Branching Poset Feedback Loops',
      },
      {
        num: '19',
        title: 'NUCLEATION',
        taxonomy: 'Matter Cooling',
        question: 'How did Particles Form?',
        ingredients: 'Topological Knot Primordial Settling',
      },
      {
        num: '20',
        title: 'FILAMENTS',
        taxonomy: 'Cosmic Web',
        question: 'Why is the Universe a Web?',
        ingredients: 'Stress-Lattice Voids & Filament Nodes',
      },
      {
        num: '21',
        title: 'DARK SECTOR',
        taxonomy: 'Relic Vacancies',
        question: 'What is Dark Energy?',
        ingredients: 'Stable Empty Poset Vacancy Pressure',
      },
      {
        num: '22',
        title: 'GRAPH CONDENSATES',
        taxonomy: 'Singularities',
        question: 'What Binds Black Holes?',
        ingredients: 'Max-Density Complete Graph Cutoffs',
      }
    ]
  },
  4: {
    title: "🔬 APPLICATIONS AND SYNTHESIS",
    subtitle: "Conclusion of the Cosmos",
    paragraphs: [
      "In Part 5, Applications and Synthesis delivers the grand philosophical and mathematical culmination of Quantum Braid Dynamics, mapping our emergent spacetime onto universal computational attractors.",
      "By exploring the thermodynamic stability of holographic codespaces, the framework proves that arbitrary bulk metrics can be reconstructed entirely from boundary entanglement entropy gradients.",
      "Finally, the framework introduces a cosmic Darwinian mechanism, where rewrite rules dynamically select for networks that maximize error-correcting code stability, deriving general relativity as the inevitable cosmic attractor."
    ],
    steps: [
      {
        num: '23',
        title: 'HOLOGRAPHIC WORLD',
        taxonomy: 'Universality',
        question: 'Is the Bulk Stable?',
        ingredients: 'Partition Function & Bulk Reconstruction',
      },
      {
        num: '24',
        title: 'MATHEMATICAL UNIVERSE',
        taxonomy: 'Derivations',
        question: 'Can We Derive Constants?',
        ingredients: 'Adjacency Coefficients & Symmetries',
      },
      {
        num: '25',
        title: 'NATURAL SELECTION',
        taxonomy: 'Synthesis',
        question: 'What Selects Stable Physics?',
        ingredients: 'Compile Space Attractors & QECC Selection',
      }
    ]
  }
};
export const PartPreviewPanel: React.FC<{ partIdx: number }> = ({ partIdx }) => {
  const data = PREVIEW_REGISTRY[partIdx];
  const partInfo = partsList[partIdx];
  if (!data || !partInfo) return null;

  return (
    <div 
      style={{ 
        backgroundColor: 'rgba(255,255,255,0.01)',
        border: '1px solid var(--ifm-color-emphasis-300)',
        borderRadius: '16px',
        padding: '1rem',
        boxShadow: '0 8px 30px rgba(0,0,0,0.03)',
        height: '100%',
        display: 'flex',
        flexDirection: 'column',
        boxSizing: 'border-box',
        overflow: 'hidden'
      }}
    >
      {/* Integrated Part Title inside the Box */}
      <div style={{ marginBottom: '0.8rem', borderBottom: '1px solid var(--ifm-color-emphasis-200)', paddingBottom: '0.4rem', flexShrink: 0 }}>
        <span style={{ 
          fontSize: '0.7rem', 
          fontWeight: '900', 
          color: 'var(--ifm-color-primary)', 
          letterSpacing: '2px', 
          textTransform: 'uppercase',
          display: 'block'
        }}>
          SYSTEM FRAMEWORK PART {partIdx + 1}
        </span>
        <h2 style={{ 
          fontSize: '1.45rem', 
          fontWeight: '850', 
          marginTop: '0.1rem', 
          letterSpacing: '-0.3px',
          marginBottom: 0
        }}>
          {partInfo.name}
        </h2>
      </div>

      <div style={{ display: 'flex', flexGrow: 1, minHeight: 0, gap: '1.5rem', alignItems: 'stretch' }}>
        {/* Left: Modular Roadmap Paragraphs */}
        <div style={{ width: '50%', display: 'flex', flexDirection: 'column', gap: '0.8rem', overflow: 'hidden', paddingRight: '1rem' }}>
          <span style={{ 
            display: 'block', 
            fontSize: '0.9rem', 
            fontWeight: '900', 
            color: 'var(--ifm-color-primary)', 
            textTransform: 'uppercase', 
            letterSpacing: '1.5px',
            marginBottom: '0.3rem'
          }}>
            {data.title}
          </span>
          <h3 style={{ fontSize: '1.75rem', fontWeight: '850', marginBottom: '0.8rem', letterSpacing: '-0.4px', lineHeight: '1.3' }}>
            {data.subtitle}
          </h3>
          
          <div style={{
            borderLeft: '4px solid var(--ifm-color-primary)',
            paddingLeft: '1.25rem',
            display: 'flex',
            flexDirection: 'column',
            gap: '1rem',
            overflowY: 'auto',
            flexGrow: 1
          }} className="qbd-column-scroll">
            {data.paragraphs.map((paragraph, idx) => (
              <p 
                key={idx}
                style={{ 
                  fontSize: '1.15rem', 
                  lineHeight: '1.75', 
                  color: 'var(--ifm-color-emphasis-800)', 
                  margin: '0 0 1rem 0',
                  textAlign: 'justify'
                }}
              >
                {paragraph}
              </p>
            ))}
          </div>
        </div>

        {/* Right: Highly Responsive, Premium HTML/CSS flowchart */}
        <div style={{ width: '50%', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', height: '100%', overflow: 'hidden', padding: '1rem 0' }}>
          <div style={{ display: 'flex', flexDirection: 'column', width: '100%', maxWidth: '370px', gap: '0.4rem', height: 'auto', flexGrow: 0, flexShrink: 0, justifyContent: 'center', margin: 'auto' }}>
            {data.steps.map((step, idx, arr) => (
              <React.Fragment key={idx}>
                <div 
                  style={{
                    backgroundColor: 'var(--ifm-color-emphasis-100)',
                    border: '1px solid var(--ifm-color-emphasis-300)',
                    borderLeft: `4px solid var(--ifm-color-primary)`,
                    borderRadius: '8px',
                    padding: '0.35rem 0.6rem',
                    boxShadow: '0 2px 8px rgba(0,0,0,0.02)',
                    transition: 'all 0.2s ease',
                    position: 'relative',
                    flexGrow: 0,
                    flexShrink: 0,
                    height: 'auto'
                  }}
                  className="qbd-deductive-card"
                >
                  {/* Keep the global hover styling scoped correctly */}
                  {idx === 0 && (
                    <style dangerouslySetInnerHTML={{ __html: `
                      .qbd-deductive-card:hover {
                        transform: translateY(-1px);
                        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
                        border-color: var(--ifm-color-primary);
                      }
                    `}} />
                  )}

                  <div style={{ display: 'flex', gap: '0.6rem', alignItems: 'flex-start' }}>
                    {/* Left Monospace Number anchor */}
                    <span style={{ 
                      fontSize: '0.95rem', 
                      fontWeight: '900', 
                      fontFamily: 'monospace, Georgia, serif', 
                      color: 'var(--ifm-color-primary)',
                      opacity: '0.85',
                      minWidth: '18px',
                      marginTop: '0.05rem'
                    }}>
                      {step.num}
                    </span>

                    {/* Right Content Stack */}
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '0.05rem', flex: 1 }}>
                      <div style={{ display: 'flex', alignItems: 'baseline', gap: '0.3rem', flexWrap: 'wrap' }}>
                        <strong style={{ 
                          fontSize: '0.78rem', 
                          fontWeight: '900', 
                          color: 'var(--ifm-color-emphasis-950)',
                          letterSpacing: '0.3px'
                        }}>
                          {step.title}
                        </strong>
                        <span style={{ 
                          fontSize: '0.66rem', 
                          color: 'var(--ifm-color-emphasis-600)',
                          fontWeight: '600'
                        }}>
                          ({step.taxonomy})
                        </span>
                      </div>

                      <div style={{ 
                        fontSize: '0.8rem', 
                        fontWeight: '800', 
                        color: 'var(--ifm-color-primary)',
                        fontStyle: 'italic',
                        fontFamily: 'Georgia, serif',
                        margin: '0.02rem 0'
                      }}>
                        "{step.question}"
                      </div>

                      <div style={{ 
                        fontSize: '0.68rem', 
                        color: 'var(--ifm-color-emphasis-700)', 
                        lineHeight: '1.3',
                        borderTop: '1px dashed var(--ifm-color-emphasis-200)',
                        paddingTop: '0.15rem',
                        marginTop: '0.05rem'
                      }}>
                        <strong style={{ color: 'var(--ifm-color-emphasis-800)' }}>Ingredients:</strong> {step.ingredients}
                      </div>
                    </div>
                  </div>
                </div>

                {/* Connecting Dotted Line with Arrow */}
                {idx < arr.length - 1 && (
                  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', height: '14px', justifyContent: 'center', flexGrow: 0, flexShrink: 0 }}>
                    <div style={{ 
                      width: '2px', 
                      height: '100%', 
                      borderLeft: '2px dashed var(--ifm-color-emphasis-300)',
                      position: 'relative'
                    }}>
                      <div style={{
                        position: 'absolute',
                        bottom: '-1px',
                        left: '-4px',
                        width: '0',
                        height: '0',
                        borderLeft: '3px solid transparent',
                        borderRight: '3px solid transparent',
                        borderTop: '4px solid var(--ifm-color-emphasis-400)'
                      }} />
                    </div>
                  </div>
                )}
              </React.Fragment>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
export default PartPreviewPanel;


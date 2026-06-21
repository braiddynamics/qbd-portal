import React, { useState, useEffect, useRef } from 'react';
import Layout from '@theme/Layout';
import Head from '@docusaurus/Head';
import HeroNetworkCanvas from '../components/graphics/hero-network-canvas';
import { 
  QubitZeroGraphic, 
  QubitOneGraphic,
  XGateGraphic,
  ZGateGraphic,
  HadamardGraphic,
  CZGateGraphic,
  TGateGraphic,
  ReadoutGraphic,
  QuantumCoreGraphic
} from '../components/graphics/quantum-graphics';
import '../css/quantum.css';

const CYAN = '#00f5ff';
const AMBER = '#ffb01f';
const RED = '#ef4444';

interface QubitModalProps {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  subtitle: string;
  writhe: string;
  charge: string;
  representation: string;
  explanation: React.ReactNode;
}

const QubitDetailModal: React.FC<QubitModalProps> = ({
  isOpen,
  onClose,
  title,
  subtitle,
  writhe,
  charge,
  representation,
  explanation
}) => {
  if (!isOpen) return null;
  return (
    <div className="quantum-modal-overlay" onClick={onClose}>
      <div className="quantum-modal-content" onClick={(e) => e.stopPropagation()}>
        <button className="quantum-modal-close" onClick={onClose}>&times;</button>
        
        <div className="quantum-modal-header">
          <h2 className="quantum-modal-title">{title}</h2>
          <div className="quantum-modal-subtitle">{subtitle}</div>
        </div>

        <div className="quantum-modal-body">
          <div className="quantum-modal-parameters">
            <div>
              <span className="quantum-modal-param-label">Invariants</span>
              <div className="quantum-modal-param-value">{writhe}</div>
            </div>
            <div>
              <span className="quantum-modal-param-label">Electric Charge</span>
              <div className="quantum-modal-param-value">{charge}</div>
            </div>
            <div>
              <span className="quantum-modal-param-label">Mathematical Core</span>
              <div className="quantum-modal-param-value">{representation}</div>
            </div>
          </div>
          <div className="quantum-modal-text">{explanation}</div>
        </div>
      </div>
    </div>
  );
};

export default function QuantumConsole(): React.JSX.Element {
  const [activeModal, setActiveModal] = useState<null | string>(null);
  const [scrollProgress, setScrollProgress] = useState(0);
  const [activeSlideIndex, setActiveSlideIndex] = useState(0);
  const containerRef = useRef<HTMLDivElement>(null);

  // Stage 4: Interactive Stabilizer Lattice state
  const [errors, setErrors] = useState({
    p1: false,
    p2: false,
    p3: false,
    p4: false,
    v1: false,
    v2: false
  });
  const [isHealing, setIsHealing] = useState(false);

  const toggleError = (key: keyof typeof errors) => {
    if (isHealing) return;
    setErrors(prev => ({ ...prev, [key]: !prev[key] }));
  };

  const triggerSelfHealing = () => {
    if (isHealing) return;
    setIsHealing(true);

    const errorKeys = Object.keys(errors) as Array<keyof typeof errors>;
    const activeKeys = errorKeys.filter(k => errors[k]);

    if (activeKeys.length === 0) {
      setIsHealing(false);
      return;
    }

    // Sequentially clear errors to show a sweeping correction effect
    let step = 0;
    const interval = setInterval(() => {
      if (step >= activeKeys.length) {
        clearInterval(interval);
        setIsHealing(false);
      } else {
        const keyToClear = activeKeys[step];
        setErrors(prev => ({ ...prev, [keyToClear]: false }));
        step++;
      }
    }, 250);
  };

  const hasErrors = Object.values(errors).some(v => v);

  useEffect(() => {
    const handleScroll = () => {
      const container = containerRef.current;
      if (!container) return;
      
      const rect = container.getBoundingClientRect();
      const containerHeight = rect.height;
      const windowHeight = window.innerHeight;
      
      const startScroll = rect.top;
      const totalScrollable = containerHeight - windowHeight;
      
      let progress = 0;
      if (startScroll < 0) {
        progress = Math.min(Math.max(-startScroll / totalScrollable, 0), 1);
      }
      
      const totalSlides = 8;
      const maxTranslate = ((totalSlides - 1) / totalSlides) * 100;
      setScrollProgress(progress * maxTranslate);
      
      const activeIndex = Math.min(Math.max(Math.round(progress * (totalSlides - 1)), 0), totalSlides - 1);
      setActiveSlideIndex(activeIndex);
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    window.addEventListener('resize', handleScroll);
    handleScroll();

    return () => {
      window.removeEventListener('scroll', handleScroll);
      window.removeEventListener('resize', handleScroll);
    };
  }, []);

  return (
    <Layout
      title="Quantum Gate & Mapping Console"
      description="Interactive scroll-driven visualizer for QBD quantum computing gates and pre-geometric logical mappings."
    >
      <Head>
        <title>Quantum Gate & Mapping Console | QBD Portal</title>
        <meta name="description" content="Interactive visualizer for QBD quantum computing gates and logical mappings." />
      </Head>

      <main className="quantum-page-container">
        {/* Liquid background blobs */}
        <div className="quantum-liquid-bg">
          <div className="quantum-blob quantum-blob-cyan" />
          <div className="quantum-blob quantum-blob-amber" />
          <div className="quantum-blob quantum-blob-green" />
        </div>

        {/* Slide 1: Welcome Slide */}
        <section className="quantum-viewport-slide">
          <div className="quantum-welcome-slide">
            <div className="quantum-welcome-left">
              <div className="quantum-welcome-tag">
                <span className="quantum-pulse-dot" />
                SYSTEM STATUS: ACTIVE
              </div>
              <h1 className="quantum-welcome-title">Quantum Computing & Gates</h1>
              <p className="quantum-welcome-subtitle">
                Tracing quantum calculations down Standard Model ribbon braids and pre-geometric topological manifolds.
              </p>

              {/* HUD Telemetry Panel */}
              <div className="quantum-welcome-telemetry">
                <div className="telemetry-item">
                  <span className="telemetry-label">OPERATING TEMP</span>
                  <span className="telemetry-value cyan-text">0.010 K</span>
                </div>
                <div className="telemetry-item">
                  <span className="telemetry-label">COHERENCE TIME</span>
                  <span className="telemetry-value amber-text">142.8 μs</span>
                </div>
                <div className="telemetry-item">
                  <span className="telemetry-label">GATE FIDELITY</span>
                  <span className="telemetry-value green-text">99.982%</span>
                </div>
              </div>

              <div className="quantum-welcome-indicator">
                <span>SCROLL TO START TIMELINE</span>
                <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <line x1="12" y1="5" x2="12" y2="19" />
                  <polyline points="19 12 12 19 5 12" />
                </svg>
              </div>
            </div>
            <div className="quantum-welcome-right">
              <QuantumCoreGraphic />
            </div>
          </div>
        </section>

        {/* Stage 3: The Horizontal Scroll Gate Suite */}
        <div className="gates-scrolly-container" ref={containerRef}>
          <div className="gates-sticky-window">
            <div 
              className="gates-horizontal-track" 
              style={{ transform: `translate3d(-${scrollProgress}%, 0, 0)` }}
            >
              {/* Slide 2: The Qubit Basis Space */}
              <section className={`quantum-viewport-slide gate-slide split-slide basis-slide ${activeSlideIndex === 0 ? 'active-slide' : ''}`}>
                <div className="quantum-slide-header-panel">
                  <span className="quantum-slide-stage-tag">STAGE 1: BASIS REPRESENTATION</span>
                  <h2 className="quantum-slide-title">The Topological Qubit Space</h2>
                  <p className="quantum-slide-subtitle">
                    Click on either state card to explore its mathematical invariants, representations, and gauge coupling properties.
                  </p>
                </div>

                <div className="qubit-cards-container">
                  {/* Logical Zero Card */}
                  <div className="qubit-card cyan-glow" onClick={() => setActiveModal('zero')}>
                    <div className="qubit-card-corners" />
                    <div className="qubit-card-header">
                      <span className="qubit-card-logical-val">|0<sub>L</sub>⟩</span>
                      <span className="qubit-card-label">GROUND STATE</span>
                    </div>
                    <div className="qubit-card-graphic-container">
                      <QubitZeroGraphic />
                    </div>
                    <div className="qubit-card-footer">
                      <div className="qubit-card-title">Symmetric Braid</div>
                      <div className="qubit-card-invariants">Writhe: (-1, -1, -1)</div>
                    </div>
                  </div>

                  {/* Logical One Card */}
                  <div className="qubit-card amber-glow" onClick={() => setActiveModal('one')}>
                    <div className="qubit-card-corners" />
                    <div className="qubit-card-header">
                      <span className="qubit-card-logical-val">|1<sub>L</sub>⟩</span>
                      <span className="qubit-card-label">EXCITED STATE</span>
                    </div>
                    <div className="qubit-card-graphic-container">
                      <QubitOneGraphic />
                    </div>
                    <div className="qubit-card-footer">
                      <div className="qubit-card-title">Asymmetric Braid</div>
                      <div className="qubit-card-invariants">Writhe: (-2, -1, 0)</div>
                    </div>
                  </div>
                </div>
              </section>

              {/* Gate 1: X-Gate */}
              <section className={`quantum-viewport-slide gate-slide cyan-border ${activeSlideIndex === 1 ? 'active-slide' : ''}`} onClick={() => setActiveModal('gate_x')}>
                <div className="gate-slide-layout">
                  <div className="gate-slide-left">
                    <XGateGraphic />
                  </div>
                  <div className="gate-slide-right">
                    <span className="quantum-slide-stage-tag">STAGE 2: UNIVERSAL INSTRUCTION SET</span>
                    <h2 className="gate-slide-name">Logical Pauli-X (NOT)</h2>
                    <p className="gate-slide-desc">
                      The Pauli-X gate acts as a topological "writhe shuffle," shifting the twist configuration 
                      of the braid between the symmetric ground state and the asymmetric excited state.
                    </p>
                    <div className="gate-expert-summary">
                      <div className="gate-expert-title">EXPERT BREAKDOWN (CHAPTER 10.4)</div>
                      <p>
                        The rewrite operation <strong>R_X</strong> executes a charge-conserving twist redistribution. 
                        It unties a single crossing on one ribbon and reties it as a double loop elsewhere, changing 
                        the writhe vector from <strong>(-1, -1, -1)</strong> to <strong>(-2, -1, 0)</strong>. 
                        The total writhe sum is strictly conserved at <strong>W = -3</strong>, preserving the electron charge 
                        observable <strong>Q = -1</strong> across the logical computation.
                      </p>
                      <div className="gate-click-hint">CLICK ANYWHERE ON SLIDE FOR PROOFS & CHAPTER DETAILS</div>
                    </div>
                  </div>
                </div>
              </section>

              {/* Gate 2: Z-Gate */}
              <section className={`quantum-viewport-slide gate-slide red-border ${activeSlideIndex === 2 ? 'active-slide' : ''}`} onClick={() => setActiveModal('gate_z')}>
                <div className="gate-slide-layout">
                  <div className="gate-slide-left">
                    <ZGateGraphic />
                  </div>
                  <div className="gate-slide-right">
                    <span className="quantum-slide-stage-tag">STAGE 2: UNIVERSAL INSTRUCTION SET</span>
                    <h2 className="gate-slide-name">Logical Pauli-Z (Phase)</h2>
                    <p className="gate-slide-desc">
                      The Pauli-Z gate exploits the non-trivial holonomy of the gauge connection to imprint a 
                      geometric phase shift exclusively on the excited qubit state.
                    </p>
                    <div className="gate-expert-summary">
                      <div className="gate-expert-title">EXPERT BREAKDOWN (CHAPTER 10.5)</div>
                      <p>
                        A gauge field probe (gluon loop) interacts with the braid. Because the ground state 
                        <strong>|0_L⟩</strong> transforms as a trivial singlet representation of <strong>SU(3)</strong>, 
                        it is transparent to the field. The excited state <strong>|1_L⟩</strong>, being color charged, 
                        couples actively to the connection, accumulating an Aharonov-Bohm phase holonomy of 
                        exactly <strong>e^iπ = -1</strong>.
                      </p>
                      <div className="gate-click-hint">CLICK ANYWHERE ON SLIDE FOR PROOFS & CHAPTER DETAILS</div>
                    </div>
                  </div>
                </div>
              </section>

              {/* Gate 3: Hadamard Gate */}
              <section className={`quantum-viewport-slide gate-slide cyan-border ${activeSlideIndex === 3 ? 'active-slide' : ''}`} onClick={() => setActiveModal('gate_h')}>
                <div className="gate-slide-layout">
                  <div className="gate-slide-left">
                    <HadamardGraphic />
                  </div>
                  <div className="gate-slide-right">
                    <span className="quantum-slide-stage-tag">STAGE 2: UNIVERSAL INSTRUCTION SET</span>
                    <h2 className="gate-slide-name">Hadamard (Superposition)</h2>
                    <p className="gate-slide-desc">
                      The Hadamard gate uses a thermodynamic cycle to randomize the braid state and 
                      freeze it into a coherent, equal-weight quantum superposition.
                    </p>
                    <div className="gate-expert-summary">
                      <div className="gate-expert-title">EXPERT BREAKDOWN (CHAPTER 10.6)</div>
                      <p>
                        The local rewrite rate is transiently driven to elevate the temperature to the critical 
                        mixing threshold <strong>T_mix = ln 2</strong>. Due to the topological degeneracy of the basis 
                        energies, this randomizes the state. A subsequent diabatic quench freezes the system 
                        into a coherent, minimum-entropy superposition <strong>|+⟩ = (|0_L⟩ + |1_L⟩) / √2</strong>.
                      </p>
                      <div className="gate-click-hint">CLICK ANYWHERE ON SLIDE FOR PROOFS & CHAPTER DETAILS</div>
                    </div>
                  </div>
                </div>
              </section>

              {/* Gate 4: Controlled-Z Gate */}
              <section className={`quantum-viewport-slide gate-slide amber-border ${activeSlideIndex === 4 ? 'active-slide' : ''}`} onClick={() => setActiveModal('gate_cz')}>
                <div className="gate-slide-layout">
                  <div className="gate-slide-left">
                    <CZGateGraphic />
                  </div>
                  <div className="gate-slide-right">
                    <span className="quantum-slide-stage-tag">STAGE 2: UNIVERSAL INSTRUCTION SET</span>
                    <h2 className="gate-slide-name">Controlled-Z (CZ)</h2>
                    <p className="gate-slide-desc">
                      The Controlled-Z gate connects spatially separated qubits via a temporary vacuum bridge, 
                      enabling conditional logical operations and entanglement generation.
                    </p>
                    <div className="gate-expert-summary">
                      <div className="gate-expert-title">EXPERT BREAKDOWN (CHAPTER 10.7)</div>
                      <p>
                        A sequence of edge additions creates a "logic wire" bridge connecting the control and target 
                        environments. An excited control state <strong>|1_L⟩</strong> (high local stress <strong>σ = -1</strong>) 
                        catalytically lowers the friction barrier <strong>f(σ)</strong> at the target, allowing the Z-gate 
                        phase imprint rewrite to execute. If the control is <strong>|0_L⟩</strong>, the friction remains high and the gate is inhibited, realizing the Controlled-Z conditional unitary.
                      </p>
                      <div className="gate-click-hint">CLICK ANYWHERE ON SLIDE FOR PROOFS & CHAPTER DETAILS</div>
                    </div>
                  </div>
                </div>
              </section>

              {/* Gate 5: T-Gate */}
              <section className={`quantum-viewport-slide gate-slide amber-border ${activeSlideIndex === 5 ? 'active-slide' : ''}`} onClick={() => setActiveModal('gate_t')}>
                <div className="gate-slide-layout">
                  <div className="gate-slide-left">
                    <TGateGraphic />
                  </div>
                  <div className="gate-slide-right">
                    <span className="quantum-slide-stage-tag">STAGE 2: UNIVERSAL INSTRUCTION SET</span>
                    <h2 className="gate-slide-name">Topological T-Gate</h2>
                    <p className="gate-slide-desc">
                      The T-gate completes the universal gate set, providing the necessary non-Clifford 
                      fractional phase rotation through ribbon self-braiding.
                    </p>
                    <div className="gate-expert-summary">
                      <div className="gate-expert-title">EXPERT BREAKDOWN (CHAPTER 10.8)</div>
                      <p>
                        A closed 3-cycle loop is nucleated from the vacuum, wraps around a strand of the target 
                        qubit, and dissolves. This self-braiding path corresponds to a half-Dehn twist in the 
                        Ribbon Category, naturally yielding a conformal spin phase of exactly <strong>e^iπ/4</strong> 
                        on the charged excited state without requiring magic state distillation.
                      </p>
                      <div className="gate-click-hint">CLICK ANYWHERE ON SLIDE FOR PROOFS & CHAPTER DETAILS</div>
                    </div>
                  </div>
                </div>
              </section>

              {/* Slide 3: Readout & Measurement */}
              <section className={`quantum-viewport-slide gate-slide split-slide read-slide ${activeSlideIndex === 6 ? 'active-slide' : ''}`} onClick={() => setActiveModal('readout')}>
                <div className="quantum-slide-header-panel">
                  <span className="quantum-slide-stage-tag">STAGE 3: STATE READOUT & MEASUREMENT</span>
                  <h2 className="quantum-slide-title">Quantum Non-Demolition Readout</h2>
                  <p className="quantum-slide-subtitle">
                    Measuring a topological qubit requires extracting its invariants without destroying its coherent braid state. 
                  </p>
                </div>

                <div className="gate-slide-layout">
                  <div className="gate-slide-left">
                    <ReadoutGraphic />
                  </div>
                  <div className="gate-slide-right">
                    <p className="gate-slide-desc">
                      Extracting logical configurations is realized through QND sensors that couple to the boundary values of the graph.
                    </p>
                    <div className="gate-expert-summary">
                      <div className="gate-expert-title">EXPERT BREAKDOWN (CHAPTER 10.1.6)</div>
                      <p>
                        Measurement operators project the quantum state onto the writhe and color bases. The 
                        <strong>Writhe Sensor</strong> measures the geometric winding number of the ribbons, returning the 
                        valence charge, while the <strong>Color Sensor</strong> extracts the boundary holonomy under 
                        the SU(3) gauge field to identify color charge asymmetry without collapsing the ribbon structure.
                      </p>
                      <div className="gate-click-hint">CLICK ANYWHERE ON SLIDE FOR PROOFS & DETAILS</div>
                    </div>
                  </div>
                </div>
              </section>

              {/* Slide 4: Stabilizer Grid & Fault Tolerance */}
              <section className={`quantum-viewport-slide gate-slide split-slide stabilizer-slide ${activeSlideIndex === 7 ? 'active-slide' : ''}`}>
                <div className="quantum-slide-header-panel">
                  <span className="quantum-slide-stage-tag">STAGE 4: TOPOLOGICAL PROTECTION & FAULT TOLERANCE</span>
                  <h2 className="quantum-slide-title">Self-Healing Stabilizer Lattice</h2>
                  <p className="quantum-slide-subtitle">
                    <strong>Interactive Simulation:</strong> Click anywhere on the grid cells/vertices below to inject local errors, then trigger the vacuum's thermodynamic healing cycle.
                  </p>
                </div>

                <div className="gate-slide-layout">
                  <div className="gate-slide-left stabilizer-grid-container">
                    {/* Interactive Stabilizer Grid SVG */}
                    <svg viewBox="0 0 120 120" style={{ width: '100%', height: '100%', maxWidth: '350px' }}>
                      {/* Plaquette P1 (Top-Left, Cyan) */}
                      <rect 
                        x="10" y="10" width="48" height="48" 
                        fill={errors.p1 ? "rgba(239, 68, 68, 0.25)" : "rgba(0, 245, 255, 0.04)"} 
                        stroke={errors.p1 ? RED : CYAN} 
                        strokeWidth="1.2" 
                        onClick={() => toggleError('p1')}
                        style={{ cursor: 'pointer', transition: 'all 0.3s' }}
                      />
                      
                      {/* Plaquette P2 (Top-Right, Amber) */}
                      <rect 
                        x="62" y="10" width="48" height="48" 
                        fill={errors.p2 ? "rgba(239, 68, 68, 0.25)" : "rgba(245, 158, 11, 0.04)"} 
                        stroke={errors.p2 ? RED : AMBER} 
                        strokeWidth="1.2" 
                        onClick={() => toggleError('p2')}
                        style={{ cursor: 'pointer', transition: 'all 0.3s' }}
                      />

                      {/* Plaquette P3 (Bottom-Left, Amber) */}
                      <rect 
                        x="10" y="62" width="48" height="48" 
                        fill={errors.p3 ? "rgba(239, 68, 68, 0.25)" : "rgba(245, 158, 11, 0.04)"} 
                        stroke={errors.p3 ? RED : AMBER} 
                        strokeWidth="1.2" 
                        onClick={() => toggleError('p3')}
                        style={{ cursor: 'pointer', transition: 'all 0.3s' }}
                      />

                      {/* Plaquette P4 (Bottom-Right, Cyan) */}
                      <rect 
                        x="62" y="62" width="48" height="48" 
                        fill={errors.p4 ? "rgba(239, 68, 68, 0.25)" : "rgba(0, 245, 255, 0.04)"} 
                        stroke={errors.p4 ? RED : CYAN} 
                        strokeWidth="1.2" 
                        onClick={() => toggleError('p4')}
                        style={{ cursor: 'pointer', transition: 'all 0.3s' }}
                      />

                      {/* Plaquette labels */}
                      <text x="34" y="36" fill={errors.p1 ? RED : CYAN} fontSize="8" fontWeight="bold" fontFamily="monospace" textAnchor="middle" pointerEvents="none">Bp</text>
                      <text x="86" y="36" fill={errors.p2 ? RED : AMBER} fontSize="8" fontWeight="bold" fontFamily="monospace" textAnchor="middle" pointerEvents="none">Av</text>
                      <text x="34" y="88" fill={errors.p3 ? RED : AMBER} fontSize="8" fontWeight="bold" fontFamily="monospace" textAnchor="middle" pointerEvents="none">Av</text>
                      <text x="86" y="88" fill={errors.p4 ? RED : CYAN} fontSize="8" fontWeight="bold" fontFamily="monospace" textAnchor="middle" pointerEvents="none">Bp</text>

                      {/* Lattice line dividers */}
                      <line x1="10" y1="60" x2="110" y2="60" stroke="rgba(255,255,255,0.15)" strokeWidth="1" pointerEvents="none" />
                      <line x1="60" y1="10" x2="60" y2="110" stroke="rgba(255,255,255,0.15)" strokeWidth="1" pointerEvents="none" />

                      {/* Vertex V1 (Central Node) */}
                      <circle 
                        cx="60" cy="60" r="5" 
                        fill={errors.v1 ? RED : "#ffffff"} 
                        stroke={errors.v1 ? RED : "rgba(255,255,255,0.3)"} 
                        strokeWidth="1.5" 
                        onClick={() => toggleError('v1')}
                        style={{ cursor: 'pointer', transition: 'all 0.3s', filter: errors.v1 ? 'drop-shadow(0 0 5px #ef4444)' : 'none' }}
                      />

                      {/* Vertex V2 (Top Node) */}
                      <circle 
                        cx="60" cy="10" r="5" 
                        fill={errors.v2 ? RED : "#ffffff"} 
                        stroke={errors.v2 ? RED : "rgba(255,255,255,0.3)"} 
                        strokeWidth="1.5" 
                        onClick={() => toggleError('v2')}
                        style={{ cursor: 'pointer', transition: 'all 0.3s', filter: errors.v2 ? 'drop-shadow(0 0 5px #ef4444)' : 'none' }}
                      />
                    </svg>
                  </div>
                  
                  <div className="gate-slide-right">
                    <p className="gate-slide-desc">
                      Topological protection is enforced by commuting stabilizer operators. 
                      Any local disturbance creates defects corrected by the vacuum.
                    </p>
                    <div className="gate-expert-summary">
                      <div className="gate-expert-title">EXPERT BREAKDOWN (CHAPTER 3.5 & 10.2)</div>
                      <p>
                        Commuting plaquette operators <strong>Bp</strong> and vertex operators <strong>Av</strong> form the stabilizer group. 
                        Faults project non-trivial syndromic values. The vacuum's thermodynamic drive 
                        (governed by <strong>λ_cat = e - 1</strong>) creates a stress-minimizing pressure that accelerates 
                        the deletion of these defects, restoring code consistency.
                      </p>
                    </div>

                    {/* Interactive trigger button */}
                    <button 
                      className={`quantum-healing-btn ${hasErrors ? 'active' : ''} ${isHealing ? 'healing' : ''}`}
                      onClick={triggerSelfHealing}
                      disabled={!hasErrors || isHealing}
                    >
                      {isHealing ? 'THERMODYNAMIC HEALING ACTIVE...' : hasErrors ? 'TRIGGER THERMODYNAMIC HEALING' : 'GRID IS SECURE (CLICK GRID TO INJECT FAULTS)'}
                    </button>
                  </div>
                </div>
              </section>
            </div>
          </div>
        </div>

        {/* Qubit Modals (Basis) */}
        <QubitDetailModal
          isOpen={activeModal === 'zero'}
          onClose={() => setActiveModal(null)}
          title="Logical Zero |0_L⟩ Ground State"
          subtitle="Symmetric singlet configuration of the electron braid"
          writhe="(-1, -1, -1)"
          charge="-1 e"
          representation="Trivial Singlet (1)"
          explanation={
            <>
              <p>
                The logical zero state represents the undisturbed ground state of the tripartite electron braid. 
                All three strands possess identical twist values, forming a perfectly symmetrical writhe vector of 
                <strong> w = (-1, -1, -1)</strong>.
              </p>
              <p>
                Under the ribbon permutation group <strong>S_3</strong>, this configuration transforms as the 
                trivial singlet representation <strong>1</strong>. Because of this perfect spatial symmetry, 
                any coupling to color gauge fields cancels out exactly at the boundaries:
              </p>
              <pre className="quantum-math-block">
                ⟨ 0_L | J^a_μ | 0_L ⟩ = 0
              </pre>
              <p>
                Consequently, the ground state is electromagnetically active (charge -1) but completely "invisible" 
                (transparent) to the color strong force field, ensuring that probe fields do not accumulate phase 
                or disturb the state during gate operations.
              </p>
            </>
          }
        />

        <QubitDetailModal
          isOpen={activeModal === 'one'}
          onClose={() => setActiveModal(null)}
          title="Logical One |1_L⟩ Excited State"
          subtitle="Asymmetric multiplet configuration of the electron braid"
          writhe="(-2, -1, 0)"
          charge="-1 e"
          representation="Non-Trivial Multiplet (3 / 8)"
          explanation={
            <>
              <p>
                The logical one state represents the excited, topologically asymmetric state of the electron braid. 
                The twist is redistributed unevenly among the strands, producing the writhe vector 
                <strong> w = (-2, -1, 0)</strong>. One ribbon stays straight (writhe 0), while another accumulates a double crossing (writhe -2).
              </p>
              <p>
                Because the twist is distributed asymmetric-ally, the state transforms as a non-trivial representation 
                under the permutation group <strong>S_3</strong>. This breaks the color singlet symmetry, causing the 
                qubit to couple actively to the strong force gauge connection:
              </p>
              <pre className="quantum-math-block">
                ⟨ 1_L | J^a_μ | 1_L ⟩ ≠ 0
              </pre>
              <p>
                This non-zero coupling is the key physical mechanism behind the <strong>Z-Gate</strong>: looping a color 
                probe field around the braid induces a non-trivial Aharonov-Bohm holonomy that imprints a phase shift of 
                exactly <strong>π</strong> (Pauli-Z rotation) exclusively on this excited state.
              </p>
            </>
          }
        />

        {/* Gate Modals */}
        <QubitDetailModal
          isOpen={activeModal === 'gate_x'}
          onClose={() => setActiveModal(null)}
          title="Pauli-X NOT Gate (Writhe Shuffling)"
          subtitle="Monograph Proof: Lemma 10.4.3 & 10.4.4"
          writhe="(-1, -1, -1) ↔ (-2, -1, 0)"
          charge="-1 e (Invariant)"
          representation="Writhe Conservation Proof"
          explanation={
            <>
              <p>
                <strong>Lemma 10.4.3: Writhe Conservation.</strong> The rewrite process <strong>R_X</strong> executes a local topological surgery that preserves the total writhe. By summing the writhe values:
              </p>
              <pre className="quantum-math-block">
                W_0 = (-1) + (-1) + (-1) = -3
                {"\n"}
                W_1 = (-2) + (-1) + (0)  = -3
              </pre>
              <p>
                Because the sum remains identical, the rewrite complies with the local electric charge conservation law (Q = W/3 = -1), allowing the system to perform binary flips without mutating the particle's flavor.
              </p>
              <p>
                <strong>Lemma 10.4.4: Charge Conservation.</strong> Under the action of the rewrite operator, the gauge charge current matrix elements are conserved modulo the logical state definition. The transition is driven by local SU(3) color fluctuations that shift the braid state across the logical boundary, mapping logically to the unitary Pauli-X operator.
              </p>
            </>
          }
        />

        <QubitDetailModal
          isOpen={activeModal === 'gate_z'}
          onClose={() => setActiveModal(null)}
          title="Pauli-Z Phase Gate (AB Holonomy)"
          subtitle="Monograph Proof: Lemma 10.5.2 & 10.5.3"
          writhe="Phase Rotation: |1⟩ → -|1⟩"
          charge="0 Phase on |0⟩"
          representation="Aharonov-Bohm Color Holonomy"
          explanation={
            <>
              <p>
                <strong>Lemma 10.5.2: Singlet Transparency.</strong> The logical zero state <strong>|0_L⟩</strong> is a color singlet (symmetric braid), resulting in a vanishing coupling amplitude to the SU(3) probe field. The interaction energy is zero:
              </p>
              <pre className="quantum-math-block">
                E_int = g ⟨ 0_L | J^a_μ | 0_L ⟩ A^μ_a = 0
              </pre>
              <p>
                This ensures the state is undisturbed and accumulates exactly zero phase: <strong>|0_L⟩ → |0_L⟩</strong>.
              </p>
              <p>
                <strong>Lemma 10.5.3: Color Phase.</strong> The logical one state <strong>|1_L⟩</strong> is color charged, coupling directly to the gauge field. A loop of the connection yields a non-trivial holonomy (Aharonov-Bohm geometric phase) of exactly <strong>π</strong>:
              </p>
              <pre className="quantum-math-block">
                ∮ A_μ dx^μ = π  ⇒  |1_L⟩ → e^iπ |1_L⟩ = -|1_L⟩
              </pre>
              <p>
                This differential phase shift implements the Pauli-Z operator with full topological protection.
              </p>
            </>
          }
        />

        <QubitDetailModal
          isOpen={activeModal === 'gate_h'}
          onClose={() => setActiveModal(null)}
          title="Hadamard Superposition (Thermodynamic Quench)"
          subtitle="Monograph Proof: Lemma 10.6.2 & 10.6.3"
          writhe="Unbiased Superposition State"
          charge="T_mix = ln 2"
          representation="Coherent Thermal Annealing"
          explanation={
            <>
              <p>
                <strong>Lemma 10.6.2: Temperature Control.</strong> The local temperature <strong>T_local</strong> is modulated by the density of rewrite operations acceptances. The system is driven away from vacuum equilibrium to the mixing temperature:
              </p>
              <pre className="quantum-math-block">
                T_local = T_vac + k (N_rewrite / V)
              </pre>
              <p>
                <strong>Lemma 10.6.3: Topological Degeneracy.</strong> Because both states are topologically degenerate (equal mass and complexity index), the partition function at <strong>T_mix = ln 2</strong> yields an unbiased maximal entropy mixture where the probabilities of finding the system in states $|0⟩$ and $|1⟩$ are exactly equal.
              </p>
              <p>
                <strong>Hadamard Quench:</strong> A rapid diabatic cooling (quench) freezes the thermal mixture before it decoheres, locking the wave function into a coherent equal-weight quantum superposition: <strong>(|0⟩ + |1⟩)/√2</strong>.
              </p>
            </>
          }
        />

        <QubitDetailModal
          isOpen={activeModal === 'gate_cz'}
          onClose={() => setActiveModal(null)}
          title="Controlled-Z Gate (Catalytic Stress Bridge)"
          subtitle="Monograph Proof: Lemma 10.7.2 & 10.7.3"
          writhe="Entanglement Generation"
          charge="Friction Coupling: f(σ)"
          representation="State-Dependent Catalysis"
          explanation={
            <>
              <p>
                <strong>Lemma 10.7.2: Syndrome Coupling.</strong> A topological bridge (logic wire) constructed of edge additions connects the control and target qubit patches, establishing a coupled stress syndrome function:
              </p>
              <pre className="quantum-math-block">
                σ_eff(T) = g(σ_C, σ_T)
              </pre>
              <p>
                This allows the stress configuration of the control qubit to dictate the environment at the target.
              </p>
              <p>
                <strong>Lemma 10.7.3: Control Dynamics.</strong> When the control is in the excited state <strong>|1_L⟩</strong>, its asymmetric configuration creates high stress (<strong>σ_C = -1</strong>). This acts as a catalyst, lowering the target friction barrier <strong>f(σ_eff)</strong> and allowing the target's Z-operation rewrite to execute. If the control is <strong>|0_L⟩</strong>, the friction remains high and the gate is inhibited, realizing the Controlled-Z conditional unitary.
              </p>
            </>
          }
        />

        <QubitDetailModal
          isOpen={activeModal === 'gate_t'}
          onClose={() => setActiveModal(null)}
          title="Topological T-Gate (Self-Braiding Dehn Twist)"
          subtitle="Monograph Proof: Lemma 10.8.3 & 10.8.7"
          writhe="Phase Rotation: |1⟩ → e^iπ/4 |1⟩"
          charge="Non-Clifford Gate Completeness"
          representation="Ribbon Category twist morphism (θ)"
          explanation={
            <>
              <p>
                <strong>Lemma 10.8.3: Ribbon Category.</strong> In topological quantum field theory (TQFT), the self-braiding of a ribbon corresponds to a fractional twist.
              </p>
              <p>
                <strong>Lemma 10.8.7: Twist Structure.</strong> The T-gate process nucleates a closed loop that wraps around a strand of the braid, performing a half-Dehn twist on the ribbon's framing before dissolving:
              </p>
              <pre className="quantum-math-block">
                θ_V = e^(2iπ h_V)
              </pre>
              <p>
                For the charged state <strong>|1_L⟩</strong> (with conformal weight <strong>h_V = 1/8</strong>), this self-interaction naturally imprints a conformal spin phase of exactly <strong>e^iπ/4</strong>. This digital twist completes the universal gate set without requiring magic state distillation.
              </p>
            </>
          }
        />

        {/* Readout Detail Modal */}
        <QubitDetailModal
          isOpen={activeModal === 'readout'}
          onClose={() => setActiveModal(null)}
          title="QND Measurement & State Readout"
          subtitle="Monograph Proof: Chapter 10.1.6"
          writhe="Writhe Operator: W_op"
          charge="Color Holonomy Operator"
          representation="Quantum Non-Demolition Projection"
          explanation={
            <>
              <p>
                To convert quantum computational states back to classical outcomes, the system executes projection measurements that extract topological invariants.
              </p>
              <p>
                <strong>Writhe Readout:</strong> The writhe operator measures the local spatial crossings of the ribbons, projection-mapping the wave function onto the discrete writhe eigenstates.
              </p>
              <p>
                <strong>Color Measurement:</strong> The gauge sensor extracts the Aharonov-Bohm holonomy around the braid boundary, distinguishing the color singlet state (logical zero) from the color charged state (logical one) through boundary connection integrals. Both operators are QND, ensuring the measurement does not collapse or fray the underlying physical ribbons, maintaining topological memory integrity.
              </p>
            </>
          }
        />
      </main>
    </Layout>
  );
}

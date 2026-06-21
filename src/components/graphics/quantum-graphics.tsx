import React from 'react';

// Design constants matching spectrum-graphics
const CYAN = '#00f5ff';
const AMBER = '#ffb01f';
const RED = '#ef4444';
const BLUE = '#25c2a0'; // Auxiliary green-blue for multi-strand visuals
const BG_DARK = '#0D1117';

// Blueprint grid overlay for graphic boxes
export const BlueprintGrid: React.FC = () => (
  <>
    {/* Grid points */}
    <circle cx="20" cy="20" r="0.5" fill="rgba(255,255,255,0.15)" />
    <circle cx="20" cy="50" r="0.5" fill="rgba(255,255,255,0.15)" />
    <circle cx="20" cy="80" r="0.5" fill="rgba(255,255,255,0.15)" />
    <circle cx="50" cy="20" r="0.5" fill="rgba(255,255,255,0.15)" />
    <circle cx="50" cy="50" r="0.5" fill="rgba(255,255,255,0.15)" />
    <circle cx="50" cy="80" r="0.5" fill="rgba(255,255,255,0.15)" />
    <circle cx="80" cy="20" r="0.5" fill="rgba(255,255,255,0.15)" />
    <circle cx="80" cy="50" r="0.5" fill="rgba(255,255,255,0.15)" />
    <circle cx="80" cy="80" r="0.5" fill="rgba(255,255,255,0.15)" />

    {/* Subtle axes */}
    <line x1="10" y1="50" x2="90" y2="50" stroke="rgba(255,255,255,0.06)" strokeWidth="0.5" strokeDasharray="2 2" />
    <line x1="50" y1="10" x2="50" y2="90" stroke="rgba(255,255,255,0.06)" strokeWidth="0.5" strokeDasharray="2 2" />
  </>
);

// 1. Qubit |0_L> Ground State: Symmetric Braid (-1, -1, -1)
// All three strands weave symmetrically, exhibiting SU(3) singlet invariance.
export const QubitZeroGraphic: React.FC = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    {/* Background Masking Paths to create overlap/underpass visual weave */}
    <path d="M 30 15 C 30 30, 70 40, 70 50 C 70 60, 30 70, 30 85" fill="none" stroke={BG_DARK} strokeWidth="6" strokeLinecap="round" />
    <path d="M 30 15 C 30 30, 70 40, 70 50 C 70 60, 30 70, 30 85" fill="none" stroke={CYAN} strokeWidth="2.2" strokeLinecap="round" className="quantum-flow-path-cyan" />

    <path d="M 50 15 C 70 25, 30 35, 30 50 C 30 65, 70 75, 50 85" fill="none" stroke={BG_DARK} strokeWidth="6" strokeLinecap="round" />
    <path d="M 50 15 C 70 25, 30 35, 30 50 C 30 65, 70 75, 50 85" fill="none" stroke={BLUE} strokeWidth="2.2" strokeLinecap="round" className="quantum-flow-path-cyan" />

    <path d="M 70 15 C 70 30, 30 40, 30 50 C 30 60, 70 70, 70 85" fill="none" stroke={BG_DARK} strokeWidth="6" strokeLinecap="round" />
    <path d="M 70 15 C 70 30, 30 40, 30 50 C 30 60, 70 70, 70 85" fill="none" stroke={AMBER} strokeWidth="2.2" strokeLinecap="round" className="quantum-flow-path-amber" />

    {/* Center node crossings representing symmetric writhe units */}
    <circle cx="50" cy="325" r="2.5" fill="#ffffff" style={{ opacity: 0.1 }} />
    <circle cx="38" cy="50" r="3" fill="#ffffff" stroke={CYAN} strokeWidth="1" />
    <circle cx="50" cy="68" r="3" fill="#ffffff" stroke={CYAN} strokeWidth="1" />
    <circle cx="62" cy="32" r="3" fill="#ffffff" stroke={CYAN} strokeWidth="1" />
  </svg>
);

// 2. Qubit |1_L> Excited State: Asymmetric Braid (-2, -1, 0)
// One strand stays straight (writhe 0), other two twist, with one double loop (writhe -2).
export const QubitOneGraphic: React.FC = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    {/* Straight Strand (Ribbon 3: Writhe 0) */}
    <line x1="75" y1="15" x2="75" y2="85" stroke={BLUE} strokeWidth="2.5" strokeLinecap="round" style={{ filter: 'drop-shadow(0 0 2px rgba(37, 194, 160, 0.4))' }} />

    {/* Twisting strands (Ribbons 1 and 2: Writhe -2 and -1) */}
    {/* Over/under weaving paths */}
    <path d="M 25 15 C 25 30, 55 35, 55 50 C 55 60, 25 65, 25 85" fill="none" stroke={BG_DARK} strokeWidth="6" strokeLinecap="round" />
    <path d="M 25 15 C 25 30, 55 35, 55 50 C 55 60, 25 65, 25 85" fill="none" stroke={CYAN} strokeWidth="2.2" strokeLinecap="round" className="quantum-flow-path-cyan" />

    <path d="M 55 15 C 55 25, 25 35, 25 50 C 25 65, 55 70, 55 85" fill="none" stroke={BG_DARK} strokeWidth="6" strokeLinecap="round" />
    <path d="M 55 15 C 55 25, 25 35, 25 50 C 25 65, 55 70, 55 85" fill="none" stroke={AMBER} strokeWidth="2.2" strokeLinecap="round" className="quantum-flow-path-amber" />

    {/* Extra Loop node indicating double twist density on one strand */}
    <path d="M 25 30 C 15 30, 15 40, 25 40" fill="none" stroke={CYAN} strokeWidth="1.8" strokeLinecap="round" className="quantum-flow-path-cyan" />
    <circle cx="20" cy="35" r="2.5" fill="#ffffff" stroke={CYAN} strokeWidth="1" />
    <circle cx="40" cy="50" r="3" fill="#ffffff" stroke={AMBER} strokeWidth="1" />
  </svg>
);

// 3. X-Gate Graphic: Writhe Shuffling Transition
export const XGateGraphic: React.FC = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    {/* Show writhe transfer arrows over symmetric-to-asymmetric ghost paths */}
    <path d="M 30 35 C 30 45, 70 55, 70 65" fill="none" stroke="rgba(0,245,255,0.2)" strokeWidth="1.5" strokeDasharray="3 3" />
    <path d="M 70 35 C 70 45, 30 55, 30 65" fill="none" stroke="rgba(245,158,11,0.2)" strokeWidth="1.5" strokeDasharray="3 3" />
    <line x1="50" y1="15" x2="50" y2="85" stroke="rgba(37,194,160,0.2)" strokeWidth="1.5" strokeDasharray="3 3" />

    {/* Dynamic loop transfer indicators */}
    <path d="M 30 35 C 40 40, 50 30, 50 50 C 50 70, 30 60, 30 65" fill="none" stroke={CYAN} strokeWidth="2.2" strokeLinecap="round" />
    <circle cx="50" cy="50" r="3" fill="#ffffff" stroke={CYAN} strokeWidth="1" />
    
    {/* Curved action arrow representing twist migration */}
    <path d="M 75 40 C 85 45, 85 55, 75 60" fill="none" stroke={AMBER} strokeWidth="1.5" markerEnd="url(#arrow)" />
    <path d="M 75 60 L 73 57 M 75 60 L 78 57" stroke={AMBER} strokeWidth="1.5" />
    <text x="82" y="53" fill={AMBER} fontSize="5" fontFamily="monospace" textAnchor="middle">SHUFFLE</text>
  </svg>
);

// 4. Z-Gate Graphic: Aharonov-Bohm Color Holonomy
export const ZGateGraphic: React.FC = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    {/* Asymmetric Braid underneath */}
    <line x1="75" y1="15" x2="75" y2="85" stroke="rgba(37,194,160,0.15)" strokeWidth="1.5" />
    <path d="M 25 15 C 25 35, 55 45, 55 85" fill="none" stroke="rgba(0,245,255,0.15)" strokeWidth="1.5" />
    <path d="M 55 15 C 55 35, 25 45, 25 85" fill="none" stroke="rgba(245,158,11,0.15)" strokeWidth="1.5" />

    {/* Color Gauge Field Loop wrapping around the center of the braid */}
    <ellipse cx="50" cy="50" rx="35" ry="12" fill="none" stroke={RED} strokeWidth="2" strokeDasharray="3 2" className="gauge-field-loop" />
    <ellipse cx="50" cy="50" rx="35" ry="12" fill="none" stroke={RED} strokeWidth="0.8" style={{ filter: 'drop-shadow(0 0 4px #ef4444)' }} />
    
    {/* Phase indicator text */}
    <circle cx="50" cy="50" r="11" fill={BG_DARK} stroke={RED} strokeWidth="1" />
    <text x="50" y="53" fill={RED} fontSize="9" fontWeight="bold" fontFamily="monospace" textAnchor="middle">e^iπ</text>
  </svg>
);

// 5. Hadamard Gate Graphic: Thermodynamic Mixing / Quench
export const HadamardGraphic: React.FC = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    {/* Fluctuating double braid */}
    <path d="M 30 15 C 50 35, 50 45, 30 85" fill="none" stroke={CYAN} strokeWidth="1.5" style={{ opacity: 0.3 }} />
    <path d="M 70 15 C 50 35, 50 45, 70 85" fill="none" stroke={AMBER} strokeWidth="1.5" style={{ opacity: 0.3 }} />

    {/* Heated superposition waves */}
    <path d="M 50 20 Q 40 35, 60 50 T 50 80" fill="none" stroke={RED} strokeWidth="1.2" strokeDasharray="4 4" className="hadamard-wave-1" style={{ opacity: 0.5, transformOrigin: '50px 50px' }} />
    <path d="M 50 20 Q 60 35, 40 50 T 50 80" fill="none" stroke={RED} strokeWidth="1.2" strokeDasharray="4 4" className="hadamard-wave-2" style={{ opacity: 0.5, transformOrigin: '50px 50px' }} />

    {/* Quenched (coherent frozen) central superposition node */}
    <circle cx="50" cy="50" r="14" fill={BG_DARK} stroke={CYAN} strokeWidth="1.5" style={{ filter: 'drop-shadow(0 0 5px rgba(0,245,255,0.4))' }} />
    <text x="50" y="52" fill={CYAN} fontSize="6" fontFamily="monospace" fontWeight="bold" textAnchor="middle">|+⟩ / |-⟩</text>
    <text x="50" y="60" fill="rgba(255,255,255,0.4)" fontSize="3.5" fontFamily="monospace" textAnchor="middle">T_c = ln 2</text>
  </svg>
);

// 6. Controlled-Z Graphic: Catalytic Stress Bridge (Logic Wire)
export const CZGateGraphic: React.FC = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    {/* Grid of points */}
    <circle cx="15" cy="50" r="0.5" fill="rgba(255,255,255,0.15)" />
    <circle cx="85" cy="50" r="0.5" fill="rgba(255,255,255,0.15)" />

    {/* Left Control Qubit Box */}
    <rect x="5" y="15" width="28" height="70" rx="3" fill="rgba(22, 27, 34, 0.4)" stroke="rgba(245, 158, 11, 0.3)" strokeWidth="1" />
    <text x="19" y="24" fill={AMBER} fontSize="5.5" fontFamily="monospace" textAnchor="middle">CONTROL |1⟩</text>
    {/* Asymmetric Braid silhouette */}
    <path d="M 12 35 L 12 75 M 26 35 C 26 50, 19 60, 19 75" fill="none" stroke="rgba(245,158,11,0.2)" strokeWidth="1.2" />
    <circle cx="19" cy="52" r="2.5" fill="none" stroke={AMBER} strokeWidth="1" />

    {/* Right Target Qubit Box */}
    <rect x="67" y="15" width="28" height="70" rx="3" fill="rgba(22, 27, 34, 0.4)" stroke="rgba(0, 245, 255, 0.3)" strokeWidth="1" />
    <text x="81" y="24" fill={CYAN} fontSize="5.5" fontFamily="monospace" textAnchor="middle">TARGET |T⟩</text>
    {/* Z-operation silhouette */}
    <path d="M 74 35 C 74 55, 88 55, 88 75" fill="none" stroke="rgba(0,245,255,0.2)" strokeWidth="1.2" />
    <circle cx="81" cy="55" r="2" fill={RED} />

    {/* Catalytic Stress Bridge (Logic Wire) */}
    <path d="M 33 50 L 67 50" fill="none" stroke={AMBER} strokeWidth="1.8" strokeDasharray="6 4" className="quantum-flow-path-amber" />
    <path d="M 33 50 L 67 50" fill="none" stroke={AMBER} strokeWidth="0.8" style={{ filter: 'drop-shadow(0 0 3px #ffb01f)' }} />
    <text x="50" y="45" fill={AMBER} fontSize="5" fontFamily="monospace" textAnchor="middle">STRESS BRIDGE</text>
    
    {/* Flow arrows on bridge */}
    <polygon points="48,48 52,50 48,52" fill={AMBER} />
    <polygon points="56,48 60,50 56,52" fill={AMBER} />
  </svg>
);

// 7. T-Gate Graphic: Self-Braiding Twist
export const TGateGraphic: React.FC = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    {/* Central Braid ribbon */}
    <line x1="50" y1="15" x2="50" y2="85" stroke={CYAN} strokeWidth="2.2" strokeLinecap="round" />

    {/* Winding Loop trajectory performing a half-twist (Dehn twist) */}
    <path d="M 50 35 C 20 35, 20 45, 50 45 C 80 45, 80 55, 50 55" fill="none" stroke={AMBER} strokeWidth="1.8" strokeDasharray="6 4" strokeLinecap="round" className="quantum-flow-path-amber" />
    <path d="M 50 35 C 20 35, 20 45, 50 45 C 80 45, 80 55, 50 55" fill="none" stroke={AMBER} strokeWidth="0.8" style={{ filter: 'drop-shadow(0 0 3px #ffb01f)' }} />
    
    {/* Loop nucleation/annihilation particles */}
    <circle cx="50" cy="35" r="2.5" fill="#ffffff" stroke={AMBER} strokeWidth="1" />
    <circle cx="50" cy="55" r="2.5" fill="#ffffff" stroke={AMBER} strokeWidth="1" />
    <text x="50" y="30" fill={AMBER} fontSize="5.5" fontFamily="monospace" textAnchor="middle">LOOP NUCLEATION</text>
    <text x="50" y="65" fill={AMBER} fontSize="5.5" fontFamily="monospace" textAnchor="middle">ANNIHILATION (e^iπ/4)</text>
  </svg>
);

// 8. Readout Graphic: Writhe & Color Non-Demolition Measurement
export const ReadoutGraphic: React.FC = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    {/* Left Sensor: Writhe Sensor */}
    <rect x="10" y="25" width="35" height="50" rx="4" fill="rgba(22, 27, 34, 0.4)" stroke={CYAN} strokeWidth="1.2" />
    <text x="27.5" y="36" fill={CYAN} fontSize="6" fontWeight="bold" fontFamily="monospace" textAnchor="middle">WRITHE SENSOR</text>
    <path d="M 20 48 Q 27.5 40, 35 48 T 20 64" fill="none" stroke={CYAN} strokeWidth="1.5" />
    <text x="27.5" y="70" fill={CYAN} fontSize="5.5" fontFamily="monospace" textAnchor="middle">Q = 1/3 Σ w_i</text>

    {/* Right Sensor: Color Sensor */}
    <rect x="55" y="25" width="35" height="50" rx="4" fill="rgba(22, 27, 34, 0.4)" stroke={AMBER} strokeWidth="1.2" />
    <text x="72.5" y="36" fill={AMBER} fontSize="6" fontWeight="bold" fontFamily="monospace" textAnchor="middle">COLOR SENSOR</text>
    <ellipse cx="72.5" cy="50" rx="8" ry="6" fill="none" stroke={AMBER} strokeWidth="1.2" strokeDasharray="2 1" />
    <circle cx="72.5" cy="50" r="2" fill={RED} />
    <text x="72.5" y="70" fill={AMBER} fontSize="5.5" fontFamily="monospace" textAnchor="middle">SU(3) Holonomy</text>
  </svg>
);

// 9. Stabilizer Plaquette and Vertex Grid Graphic
export const StabilizerGridGraphic: React.FC = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    {/* Plaquettes (Shaded red and blue cells) */}
    <rect x="15" y="15" width="35" height="35" fill="rgba(0, 245, 255, 0.05)" stroke={CYAN} strokeWidth="0.8" />
    <rect x="50" y="15" width="35" height="35" fill="rgba(245, 158, 11, 0.05)" stroke={AMBER} strokeWidth="0.8" />
    <rect x="15" y="50" width="35" height="35" fill="rgba(245, 158, 11, 0.05)" stroke={AMBER} strokeWidth="0.8" />
    <rect x="50" y="50" width="35" height="35" fill="rgba(0, 245, 255, 0.05)" stroke={CYAN} strokeWidth="0.8" />

    {/* Plaquette Operator Labels */}
    <text x="32.5" y="35" fill={CYAN} fontSize="8" fontWeight="bold" fontFamily="monospace" textAnchor="middle" style={{ opacity: 0.65 }}>Bp</text>
    <text x="67.5" y="35" fill={AMBER} fontSize="8" fontWeight="bold" fontFamily="monospace" textAnchor="middle" style={{ opacity: 0.65 }}>Av</text>
    <text x="32.5" y="70" fill={AMBER} fontSize="8" fontWeight="bold" fontFamily="monospace" textAnchor="middle" style={{ opacity: 0.65 }}>Av</text>
    <text x="67.5" y="70" fill={CYAN} fontSize="8" fontWeight="bold" fontFamily="monospace" textAnchor="middle" style={{ opacity: 0.65 }}>Bp</text>

    {/* Lattice lines */}
    <line x1="15" y1="50" x2="85" y2="50" stroke="rgba(255,255,255,0.12)" strokeWidth="1" />
    <line x1="50" y1="15" x2="50" y2="85" stroke="rgba(255,255,255,0.12)" strokeWidth="1" />

    {/* Syndrome error defect points */}
    <circle cx="50" cy="50" r="4.5" fill={RED} style={{ filter: 'drop-shadow(0 0 4px #ef4444)' }} />
    <text x="50" y="44" fill={RED} fontSize="5" fontWeight="bold" fontFamily="monospace" textAnchor="middle">SYNDROME ERROR</text>

    {/* Self-healing correction path arrows */}
    <path d="M 50 50 Q 50 35, 32.5 35" fill="none" stroke="#25c2a0" strokeWidth="1.2" strokeDasharray="3 2" />
    <polygon points="32.5,33 29,35 32.5,37" fill="#25c2a0" />
    <text x="48" y="27" fill="#25c2a0" fontSize="4.5" fontFamily="monospace">PRUNING DIRECTION</text>
  </svg>
);

// 10. Quantum Core Graphic (Dilution Refrigerator Chandelier) for Cinematic landing portal
export const QuantumCoreGraphic: React.FC = () => (
  <svg viewBox="0 0 100 115" style={{ width: '100%', height: '100%', maxWidth: '380px' }}>
    <BlueprintGrid />
    
    {/* Upper room-temperature flange */}
    <rect x="15" y="10" width="70" height="4" rx="1" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.2)" strokeWidth="0.8" />
    <line x1="20" y1="14" x2="20" y2="28" stroke="rgba(255,255,255,0.25)" strokeWidth="1" />
    <line x1="50" y1="14" x2="50" y2="28" stroke="rgba(255,255,255,0.3)" strokeWidth="1.5" />
    <line x1="80" y1="14" x2="80" y2="28" stroke="rgba(255,255,255,0.25)" strokeWidth="1" />
    
    {/* Stage 1: 50K Plate */}
    <rect x="23" y="28" width="54" height="3" rx="0.5" fill="rgba(255,255,255,0.12)" stroke="rgba(255,255,255,0.3)" strokeWidth="0.8" />
    <line x1="28" y1="31" x2="28" y2="48" stroke="rgba(255,255,255,0.25)" strokeWidth="1" />
    <line x1="72" y1="31" x2="72" y2="48" stroke="rgba(255,255,255,0.25)" strokeWidth="1" />
    
    {/* Stage 2: 4K Plate */}
    <rect x="30" y="48" width="40" height="3" rx="0.5" fill="rgba(255,255,255,0.16)" stroke="rgba(255,255,255,0.35)" strokeWidth="0.8" />
    <line x1="35" y1="51" x2="35" y2="70" stroke="rgba(255,255,255,0.25)" strokeWidth="1" />
    <line x1="65" y1="51" x2="65" y2="70" stroke="rgba(255,255,255,0.25)" strokeWidth="1" />
    
    {/* Stage 3: Still Plate (1.5K) */}
    <rect x="36" y="70" width="28" height="2.5" rx="0.5" fill="rgba(255,255,255,0.2)" stroke="rgba(255,255,255,0.4)" strokeWidth="0.8" />
    <line x1="41" y1="72.5" x2="41" y2="92" stroke="rgba(255,255,255,0.25)" strokeWidth="1" />
    <line x1="59" y1="72.5" x2="59" y2="92" stroke="rgba(255,255,255,0.25)" strokeWidth="1" />
    
    {/* Stage 4: Mixing Chamber Plate (10mK) */}
    <rect x="40" y="92" width="20" height="2" rx="0.5" fill="rgba(255,255,255,0.25)" stroke="rgba(255,255,255,0.5)" strokeWidth="0.8" />

    {/* Micro-Coaxial Cabling Bundles weaving down through stages */}
    {/* Left cable bundle (Cyan path) */}
    <path id="left-cable" d="M 26 31 C 24 40, 31 40, 33 48 C 35 56, 33 62, 38 70 C 40 78, 39 84, 42 92" fill="none" stroke={CYAN} strokeWidth="0.8" style={{ opacity: 0.75 }} />
    <path d="M 28 31 C 26 39, 33 39, 35 48 C 37 56, 35 62, 40 70 C 42 78, 41 84, 44 92" fill="none" stroke={CYAN} strokeWidth="0.5" style={{ opacity: 0.45 }} />
    
    {/* Right cable bundle (Amber path) */}
    <path id="right-cable" d="M 74 31 C 76 40, 69 40, 67 48 C 65 56, 67 62, 62 70 C 60 78, 61 84, 58 92" fill="none" stroke={AMBER} strokeWidth="0.8" style={{ opacity: 0.75 }} />
    <path d="M 72 31 C 74 39, 67 39, 65 48 C 63 56, 65 62, 60 70 C 58 78, 59 84, 56 92" fill="none" stroke={AMBER} strokeWidth="0.5" style={{ opacity: 0.45 }} />

    {/* Center coaxial line (Direct RF input line) */}
    <path id="center-cable" d="M 50 14 L 50 92" fill="none" stroke="#ffffff" strokeWidth="0.8" style={{ opacity: 0.65 }} />
    
    {/* The Quantum Processor shield / canister at the bottom */}
    <rect x="43" y="94" width="14" height="15" rx="1" fill={BG_DARK} stroke={CYAN} strokeWidth="1" style={{ filter: 'drop-shadow(0 0 3px rgba(0, 245, 255, 0.35))' }} />
    
    {/* Telemetry/grid markings on canister */}
    <line x1="46" y1="98" x2="54" y2="98" stroke="rgba(0, 245, 255, 0.25)" strokeWidth="0.5" />
    <line x1="46" y1="102" x2="54" y2="102" stroke="rgba(0, 245, 255, 0.25)" strokeWidth="0.5" />
    <line x1="46" y1="106" x2="54" y2="106" stroke="rgba(0, 245, 255, 0.25)" strokeWidth="0.5" />
    <line x1="50" y1="94" x2="50" y2="109" stroke="rgba(0, 245, 255, 0.15)" strokeWidth="0.5" />

    {/* Glowing processor chip inside canister */}
    <rect x="47.5" y="100.5" width="5" height="5" fill="none" stroke={AMBER} strokeWidth="0.8" style={{ filter: 'drop-shadow(0 0 2px #ffb01f)' }} />
    <circle cx="50" cy="103" r="0.75" fill="#ffffff" className="quantum-node-pulse" />

    {/* Outer vacuum chamber outline (dashed phantom line) */}
    <path d="M 12 15 L 12 108 A 4 4 0 0 0 16 112 L 84 112 A 4 4 0 0 0 88 108 L 88 15" fill="none" stroke="rgba(255,255,255,0.05)" strokeWidth="0.6" strokeDasharray="3 3" />
    
    {/* Animated signal pulses moving down the cables */}
    <circle r="0.8" fill="#ffffff" style={{ filter: 'drop-shadow(0 0 2px #ffffff)' }}>
      <animateMotion dur="3.5s" repeatCount="indefinite">
        <mpath href="#left-cable" />
      </animateMotion>
    </circle>
    <circle r="0.8" fill={CYAN} style={{ filter: 'drop-shadow(0 0 2.5px #00f5ff)' }}>
      <animateMotion dur="2.2s" repeatCount="indefinite">
        <mpath href="#center-cable" />
      </animateMotion>
    </circle>
    <circle r="0.8" fill="#ffffff" style={{ filter: 'drop-shadow(0 0 2px #ffffff)' }}>
      <animateMotion dur="2.9s" repeatCount="indefinite">
        <mpath href="#right-cable" />
      </animateMotion>
    </circle>
  </svg>
);


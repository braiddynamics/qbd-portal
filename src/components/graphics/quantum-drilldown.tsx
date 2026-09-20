import React, { useState } from 'react';
import './quantum-drilldown.css';

const CYAN = '#00f5ff';
const AMBER = '#ffb01f';
const RED = '#ef4444';
const GREEN = '#10b981';

// Blueprint grid overlay for graphic boxes
const BlueprintGrid: React.FC = () => (
  <g opacity="0.35">
    <circle cx="20" cy="20" r="0.6" fill="rgba(255,255,255,0.2)" />
    <circle cx="20" cy="50" r="0.6" fill="rgba(255,255,255,0.2)" />
    <circle cx="20" cy="80" r="0.6" fill="rgba(255,255,255,0.2)" />
    <circle cx="50" cy="20" r="0.6" fill="rgba(255,255,255,0.2)" />
    <circle cx="50" cy="50" r="0.6" fill="rgba(255,255,255,0.2)" />
    <circle cx="50" cy="80" r="0.6" fill="rgba(255,255,255,0.2)" />
    <circle cx="80" cy="20" r="0.6" fill="rgba(255,255,255,0.2)" />
    <circle cx="80" cy="50" r="0.6" fill="rgba(255,255,255,0.2)" />
    <circle cx="80" cy="80" r="0.6" fill="rgba(255,255,255,0.2)" />
    <line x1="10" y1="50" x2="90" y2="50" stroke="rgba(255,255,255,0.06)" strokeWidth="0.5" strokeDasharray="2 2" />
    <line x1="50" y1="10" x2="50" y2="90" stroke="rgba(255,255,255,0.06)" strokeWidth="0.5" strokeDasharray="2 2" />
  </g>
);

// -------------------------------------------------------------
// TIER 1: The Dilution Refrigerator (Cryostat)
// Rich copper/gold plates, glowing cold mist, animated pulses
// -------------------------------------------------------------
export const CryostatGraphic: React.FC = () => (
  <svg viewBox="0 0 100 120" style={{ width: '100%', height: '100%', overflow: 'visible' }}>
    <defs>
      {/* Metallic Gold/Copper Gradients for Thermal Plates */}
      <linearGradient id="copperPlate" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stopColor="#b45309" />
        <stop offset="35%" stopColor="#fbbf24" />
        <stop offset="70%" stopColor="#d97706" />
        <stop offset="100%" stopColor="#92400e" />
      </linearGradient>

      <linearGradient id="goldPlate" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stopColor="#d97706" />
        <stop offset="50%" stopColor="#fef08a" />
        <stop offset="100%" stopColor="#b45309" />
      </linearGradient>

      {/* Cryogenic Cold Aura (10mK bottom mist) */}
      <radialGradient id="coldAura" cx="50%" cy="85%" r="45%">
        <stop offset="0%" stopColor="rgba(0, 245, 255, 0.35)" />
        <stop offset="50%" stopColor="rgba(0, 245, 255, 0.08)" />
        <stop offset="100%" stopColor="transparent" />
      </radialGradient>

      {/* Plate glow filter */}
      <filter id="goldGlow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="1.5" result="blur" />
        <feComposite in="SourceGraphic" in2="blur" operator="over" />
      </filter>
    </defs>

    {/* Background blueprint grid */}
    <BlueprintGrid />

    {/* Cold mist ambient aura at bottom */}
    <circle cx="50" cy="100" r="30" fill="url(#coldAura)" pointerEvents="none" />

    {/* Outer vacuum shield contour (ghost outline) */}
    <path
      d="M 14 16 L 14 104 A 6 6 0 0 0 20 110 L 80 110 A 6 6 0 0 0 86 104 L 86 16"
      fill="none"
      stroke="rgba(0, 245, 255, 0.12)"
      strokeWidth="0.8"
      strokeDasharray="4 3"
    />

    {/* Thermal Stage Rods (Structural stainless-steel supports) */}
    <line x1="22" y1="16" x2="22" y2="92" stroke="rgba(255,255,255,0.25)" strokeWidth="1" />
    <line x1="50" y1="16" x2="50" y2="92" stroke="rgba(255,255,255,0.35)" strokeWidth="1.2" />
    <line x1="78" y1="16" x2="78" y2="92" stroke="rgba(255,255,255,0.25)" strokeWidth="1" />

    {/* Staged Thermal Flanges (Gold/Copper Plated Disks) */}
    {/* Stage 0: 300K Room Temp Flange */}
    <rect x="14" y="14" width="72" height="4.5" rx="1.2" fill="url(#copperPlate)" stroke="#fef08a" strokeWidth="0.4" filter="url(#goldGlow)" />
    <text x="50" y="17.2" fill="#000000" fontSize="2.5" fontWeight="bold" fontFamily="monospace" textAnchor="middle">300 K FLANGE</text>

    {/* Stage 1: 50K Plate */}
    <rect x="20" y="32" width="60" height="3.5" rx="1" fill="url(#goldPlate)" stroke="#fef08a" strokeWidth="0.4" />
    <text x="83" y="35" fill="rgba(255,255,255,0.6)" fontSize="2.8" fontFamily="monospace">50 K</text>

    {/* Stage 2: 4K Plate */}
    <rect x="26" y="50" width="48" height="3.5" rx="1" fill="url(#goldPlate)" stroke="#fef08a" strokeWidth="0.4" />
    <text x="77" y="53" fill="rgba(255,255,255,0.6)" fontSize="2.8" fontFamily="monospace">4 K</text>

    {/* Stage 3: Still Plate (1.5K) */}
    <rect x="32" y="68" width="36" height="3" rx="0.8" fill="url(#goldPlate)" stroke="#fef08a" strokeWidth="0.4" />
    <text x="71" y="70.5" fill="rgba(255,255,255,0.6)" fontSize="2.8" fontFamily="monospace">1.5 K</text>

    {/* Stage 4: Mixing Chamber Plate (10 mK Cold Head) */}
    <rect x="36" y="86" width="28" height="3" rx="0.8" fill="url(#copperPlate)" stroke="#00f5ff" strokeWidth="0.7" style={{ filter: 'drop-shadow(0 0 4px rgba(0,245,255,0.5))' }} />
    <text x="67" y="88.5" fill={CYAN} fontSize="3" fontWeight="bold" fontFamily="monospace">10 mK</text>

    {/* Micro-Coaxial Microwave Cable Bundles */}
    {/* Left Bundle (Cyan) */}
    <path id="coax-left" d="M 28 18 C 24 35, 32 45, 34 50 C 36 60, 32 72, 38 86 C 41 90, 42 94, 44 98" fill="none" stroke={CYAN} strokeWidth="1" opacity="0.8" />
    <path d="M 26 18 C 22 34, 30 44, 32 50 C 34 59, 30 71, 36 86" fill="none" stroke={CYAN} strokeWidth="0.5" opacity="0.4" />

    {/* Right Bundle (Amber) */}
    <path id="coax-right" d="M 72 18 C 76 35, 68 45, 66 50 C 64 60, 68 72, 62 86 C 59 90, 58 94, 56 98" fill="none" stroke={AMBER} strokeWidth="1" opacity="0.8" />
    <path d="M 74 18 C 78 34, 70 44, 68 50 C 66 59, 70 71, 64 86" fill="none" stroke={AMBER} strokeWidth="0.5" opacity="0.4" />

    {/* Center RF Feedline (White) */}
    <path id="coax-center" d="M 50 18 L 50 98" fill="none" stroke="#ffffff" strokeWidth="0.9" opacity="0.7" />

    {/* Bottom QPU Canister (Superconducting Magnetic Shield) */}
    <rect x="42" y="94" width="16" height="18" rx="2" fill="#080c18" stroke={CYAN} strokeWidth="1.2" style={{ filter: 'drop-shadow(0 0 8px rgba(0, 245, 255, 0.45))' }} />
    
    {/* Telemetry stripes on shield */}
    <line x1="45" y1="99" x2="55" y2="99" stroke="rgba(0, 245, 255, 0.4)" strokeWidth="0.7" />
    <line x1="45" y1="103" x2="55" y2="103" stroke="rgba(0, 245, 255, 0.4)" strokeWidth="0.7" />
    <line x1="45" y1="107" x2="55" y2="107" stroke="rgba(0, 245, 255, 0.4)" strokeWidth="0.7" />

    {/* Glowing Transmon QPU Silicon Die inside canister */}
    <rect x="46" y="99" width="8" height="8" rx="1" fill="rgba(245, 158, 11, 0.25)" stroke={AMBER} strokeWidth="0.9" style={{ filter: 'drop-shadow(0 0 5px #ffb01f)' }} />
    <circle cx="50" cy="103" r="1.4" fill="#ffffff">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite" />
    </circle>

    {/* Animated Microwave Signal Pulses traveling down */}
    <circle r="1.2" fill="#ffffff" style={{ filter: 'drop-shadow(0 0 3px #ffffff)' }}>
      <animateMotion dur="2.8s" repeatCount="indefinite">
        <mpath href="#coax-left" />
      </animateMotion>
    </circle>
    <circle r="1.2" fill={CYAN} style={{ filter: 'drop-shadow(0 0 3px #00f5ff)' }}>
      <animateMotion dur="1.9s" repeatCount="indefinite">
        <mpath href="#coax-center" />
      </animateMotion>
    </circle>
    <circle r="1.2" fill={AMBER} style={{ filter: 'drop-shadow(0 0 3px #ffb01f)' }}>
      <animateMotion dur="2.4s" repeatCount="indefinite">
        <mpath href="#coax-right" />
      </animateMotion>
    </circle>
  </svg>
);

// -------------------------------------------------------------
// TIER 2: The Physical Quantum Chip (QPU - Heavy-Hex Transmon)
// High-tech blueprint, glowing waveguides, transmon cross-pads
// -------------------------------------------------------------
export const ChipGraphic: React.FC = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%', overflow: 'visible' }}>
    <defs>
      {/* Silicon Wafer Gradient */}
      <linearGradient id="siliconDie" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stopColor="#0f172a" />
        <stop offset="50%" stopColor="#090d16" />
        <stop offset="100%" stopColor="#0f172a" />
      </linearGradient>

      {/* Gold Pad Gradient */}
      <linearGradient id="goldPad" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stopColor="#fde047" />
        <stop offset="100%" stopColor="#b45309" />
      </linearGradient>
    </defs>

    <BlueprintGrid />

    {/* Silicon Substrate Die */}
    <rect x="8" y="8" width="84" height="84" rx="4" fill="url(#siliconDie)" stroke="rgba(0, 245, 255, 0.3)" strokeWidth="1.2" style={{ filter: 'drop-shadow(0 0 12px rgba(0,0,0,0.8))' }} />
    <rect x="12" y="12" width="76" height="76" rx="2" fill="none" stroke="rgba(245, 158, 11, 0.25)" strokeWidth="0.6" strokeDasharray="4 2" />

    {/* Perimeter Wirebond Gold Pads */}
    {Array.from({ length: 9 }).map((_, i) => (
      <React.Fragment key={i}>
        <rect x={18 + i * 7.5} y="9" width="4.5" height="2.2" fill="url(#goldPad)" rx="0.3" />
        <rect x={18 + i * 7.5} y="88.8" width="4.5" height="2.2" fill="url(#goldPad)" rx="0.3" />
        <rect x="9" y={18 + i * 7.5} width="2.2" height="4.5" fill="url(#goldPad)" rx="0.3" />
        <rect x="88.8" y={18 + i * 7.5} width="2.2" height="4.5" fill="url(#goldPad)" rx="0.3" />
      </React.Fragment>
    ))}

    {/* Serpentine Coplanar Waveguides (Readout Resonators) */}
    <path id="res-1" d="M 16 26 Q 22 20, 28 26 T 38 26 T 46 32" fill="none" stroke={CYAN} strokeWidth="1" opacity="0.6" strokeDasharray="3 1.5" />
    <path id="res-2" d="M 16 74 Q 22 80, 28 74 T 38 74 T 46 68" fill="none" stroke={CYAN} strokeWidth="1" opacity="0.6" strokeDasharray="3 1.5" />
    <path id="res-3" d="M 84 26 Q 78 20, 72 26 T 62 26 T 54 32" fill="none" stroke={AMBER} strokeWidth="1" opacity="0.6" strokeDasharray="3 1.5" />
    <path id="res-4" d="M 84 74 Q 78 80, 72 74 T 62 74 T 54 68" fill="none" stroke={AMBER} strokeWidth="1" opacity="0.6" strokeDasharray="3 1.5" />

    {/* Heavy-Hexagonal Lattice Interconnects */}
    {/* Hexagon Left */}
    <polygon points="34,36 46,36 52,46 46,56 34,56 28,46" fill="rgba(0, 245, 255, 0.03)" stroke="rgba(0, 245, 255, 0.35)" strokeWidth="1" />
    {/* Hexagon Right */}
    <polygon points="54,36 66,36 72,46 66,56 54,56 48,46" fill="rgba(245, 158, 11, 0.03)" stroke="rgba(245, 158, 11, 0.35)" strokeWidth="1" />
    {/* Hexagon Bottom */}
    <polygon points="44,56 56,56 62,66 56,76 44,76 38,66" fill="rgba(16, 185, 129, 0.03)" stroke="rgba(16, 185, 129, 0.35)" strokeWidth="1" />

    {/* Transmon Cross-Capacitor Qubits (Crosses with glowing cores) */}
    {[
      { x: 34, y: 36, c: CYAN }, { x: 46, y: 36, c: AMBER }, { x: 54, y: 36, c: CYAN }, { x: 66, y: 36, c: AMBER },
      { x: 28, y: 46, c: AMBER }, { x: 50, y: 46, c: '#ffffff', master: true }, { x: 72, y: 46, c: CYAN },
      { x: 34, y: 56, c: CYAN }, { x: 46, y: 56, c: AMBER }, { x: 54, y: 56, c: CYAN }, { x: 66, y: 56, c: AMBER },
      { x: 38, y: 66, c: AMBER }, { x: 62, y: 66, c: CYAN },
      { x: 44, y: 76, c: CYAN }, { x: 56, y: 76, c: AMBER },
    ].map((q, idx) => (
      <g key={idx} transform={`translate(${q.x}, ${q.y})`}>
        {/* Cross Capacitor Arms */}
        <line x1="-3" y1="0" x2="3" y2="0" stroke={q.c} strokeWidth="1.6" strokeLinecap="round" />
        <line x1="0" y1="-3" x2="0" y2="3" stroke={q.c} strokeWidth="1.6" strokeLinecap="round" />
        {/* Center Josephson Junction Pad */}
        <rect x="-0.8" y="-0.8" width="1.6" height="1.6" fill="#ffffff" style={{ filter: `drop-shadow(0 0 3px ${q.c})` }} />
        {q.master && (
          <circle cx="0" cy="0" r="4.5" fill="none" stroke="#ffffff" strokeWidth="0.6" strokeDasharray="1.5 1.5">
            <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="10s" repeatCount="indefinite" />
          </circle>
        )}
      </g>
    ))}

    {/* Central Transmon Core Target Ring */}
    <circle cx="50" cy="46" r="8" fill="none" stroke="rgba(0,245,255,0.25)" strokeWidth="0.8" strokeDasharray="3 2" />
  </svg>
);

// -------------------------------------------------------------
// TIER 3: The Pre-Geometric Codespace Lattice (Vacuum QECC)
// Dynamic diamond causal graph, dual face checks, embedded braid,
// interactive syndrome injection, and expansion healing pulse
// -------------------------------------------------------------
interface CodespaceGraphicProps {
  errors: { p1: boolean; p2: boolean; p3: boolean; p4: boolean };
  onTogglePlaquette: (key: 'p1' | 'p2' | 'p3' | 'p4') => void;
  isHealing: boolean;
}

export const CodespaceLatticeGraphic: React.FC<CodespaceGraphicProps> = ({
  errors,
  onTogglePlaquette,
  isHealing
}) => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%', overflow: 'visible' }}>
    <defs>
      {/* Plaquette Invariant Gradients */}
      <radialGradient id="p1Cyan" cx="50%" cy="50%" r="60%">
        <stop offset="0%" stopColor="rgba(0, 245, 255, 0.3)" />
        <stop offset="100%" stopColor="rgba(0, 245, 255, 0.06)" />
      </radialGradient>

      <radialGradient id="p2Amber" cx="50%" cy="50%" r="60%">
        <stop offset="0%" stopColor="rgba(245, 158, 11, 0.3)" />
        <stop offset="100%" stopColor="rgba(245, 158, 11, 0.06)" />
      </radialGradient>

      <radialGradient id="pError" cx="50%" cy="50%" r="60%">
        <stop offset="0%" stopColor="rgba(239, 68, 68, 0.6)" />
        <stop offset="100%" stopColor="rgba(239, 68, 68, 0.15)" />
      </radialGradient>
    </defs>

    <BlueprintGrid />

    {/* Background Causal Diamond Frame (Edge Qubits: |0> absent, |1> present) */}
    <polygon points="50,12 88,50 50,88 12,50" fill="rgba(8, 12, 24, 0.6)" stroke="rgba(255,255,255,0.25)" strokeWidth="1.2" />

    {/* Cross Lattice Dividers */}
    <line x1="50" y1="12" x2="50" y2="88" stroke="rgba(255,255,255,0.3)" strokeWidth="1" strokeDasharray="3 2" />
    <line x1="12" y1="50" x2="88" y2="50" stroke="rgba(255,255,255,0.3)" strokeWidth="1" strokeDasharray="3 2" />

    {/* 4 Interactive Plaquettes (Face Z-Checks) */}
    {/* P1: Top-Left (Geometric Check Bp) */}
    <polygon
      points="50,14 14,50 48,50"
      fill={errors.p1 ? 'url(#pError)' : 'url(#p1Cyan)'}
      stroke={errors.p1 ? RED : CYAN}
      strokeWidth={errors.p1 ? '1.8' : '1.2'}
      onClick={() => onTogglePlaquette('p1')}
      style={{ cursor: 'pointer', transition: 'all 0.25s ease' }}
    />
    <text x="36" y="38" fill={errors.p1 ? RED : CYAN} fontSize="5.5" fontWeight="bold" fontFamily="monospace" textAnchor="middle" pointerEvents="none">
      {errors.p1 ? 'σ = -1' : 'Bp (+1)'}
    </text>

    {/* P2: Top-Right (Vertex Flux Check Av) */}
    <polygon
      points="50,14 86,50 52,50"
      fill={errors.p2 ? 'url(#pError)' : 'url(#p2Amber)'}
      stroke={errors.p2 ? RED : AMBER}
      strokeWidth={errors.p2 ? '1.8' : '1.2'}
      onClick={() => onTogglePlaquette('p2')}
      style={{ cursor: 'pointer', transition: 'all 0.25s ease' }}
    />
    <text x="64" y="38" fill={errors.p2 ? RED : AMBER} fontSize="5.5" fontWeight="bold" fontFamily="monospace" textAnchor="middle" pointerEvents="none">
      {errors.p2 ? 'σ = -1' : 'Av (+1)'}
    </text>

    {/* P3: Bottom-Left (Vertex Flux Check Av) */}
    <polygon
      points="14,50 50,86 48,52"
      fill={errors.p3 ? 'url(#pError)' : 'url(#p2Amber)'}
      stroke={errors.p3 ? RED : AMBER}
      strokeWidth={errors.p3 ? '1.8' : '1.2'}
      onClick={() => onTogglePlaquette('p3')}
      style={{ cursor: 'pointer', transition: 'all 0.25s ease' }}
    />
    <text x="36" y="65" fill={errors.p3 ? RED : AMBER} fontSize="5.5" fontWeight="bold" fontFamily="monospace" textAnchor="middle" pointerEvents="none">
      {errors.p3 ? 'σ = -1' : 'Av (+1)'}
    </text>

    {/* P4: Bottom-Right (Geometric Check Bp) */}
    <polygon
      points="86,50 50,86 52,52"
      fill={errors.p4 ? 'url(#pError)' : 'url(#p1Cyan)'}
      stroke={errors.p4 ? RED : CYAN}
      strokeWidth={errors.p4 ? '1.8' : '1.2'}
      onClick={() => onTogglePlaquette('p4')}
      style={{ cursor: 'pointer', transition: 'all 0.25s ease' }}
    />
    <text x="64" y="65" fill={errors.p4 ? RED : CYAN} fontSize="5.5" fontWeight="bold" fontFamily="monospace" textAnchor="middle" pointerEvents="none">
      {errors.p4 ? 'σ = -1' : 'Bp (+1)'}
    </text>

    {/* Embedded Tripartite Fermion Braid (The Non-Local Logical Qubit) */}
    {/* Strand 1 (Red / Ruby) */}
    <path
      d="M 44 86 C 44 68, 56 60, 56 50 C 56 40, 44 32, 44 14"
      fill="none"
      stroke="#ef4444"
      strokeWidth="2.2"
      strokeLinecap="round"
      style={{ filter: 'drop-shadow(0 0 3px rgba(239, 68, 68, 0.7))' }}
    />
    {/* Strand 2 (Emerald / Green) */}
    <path
      d="M 50 86 C 50 72, 44 62, 44 50 C 44 38, 56 28, 56 14"
      fill="none"
      stroke={GREEN}
      strokeWidth="2.2"
      strokeLinecap="round"
      style={{ filter: 'drop-shadow(0 0 3px rgba(16, 185, 129, 0.7))' }}
    />
    {/* Strand 3 (Sapphire / Blue) */}
    <path
      d="M 56 86 C 56 70, 50 60, 50 50 C 50 38, 50 28, 50 14"
      fill="none"
      stroke="#3b82f6"
      strokeWidth="2.2"
      strokeLinecap="round"
      style={{ filter: 'drop-shadow(0 0 3px rgba(59, 130, 246, 0.7))' }}
    />

    {/* Central Knot Node (Borromean core) */}
    <circle cx="50" cy="50" r="4" fill="#080c18" stroke="#ffffff" strokeWidth="1.4" />
    <circle cx="50" cy="50" r="1.8" fill={CYAN} />

    {/* Corner Star-Check Operator Nodes */}
    <circle cx="50" cy="12" r="3" fill="#080c18" stroke={AMBER} strokeWidth="1.2" />
    <circle cx="88" cy="50" r="3" fill="#080c18" stroke={CYAN} strokeWidth="1.2" />
    <circle cx="50" cy="88" r="3" fill="#080c18" stroke={AMBER} strokeWidth="1.2" />
    <circle cx="12" cy="50" r="3" fill="#080c18" stroke={CYAN} strokeWidth="1.2" />

    {/* Thermodynamic Healing Wave (Animated Expansion Pulse) */}
    {isHealing && (
      <g pointerEvents="none">
        <circle cx="50" cy="50" r="42" fill="none" stroke={GREEN} strokeWidth="3" opacity="0.9" style={{ filter: 'drop-shadow(0 0 12px #10b981)' }}>
          <animate attributeName="r" from="4" to="48" dur="0.75s" repeatCount="indefinite" />
          <animate attributeName="opacity" from="1" to="0" dur="0.75s" repeatCount="indefinite" />
        </circle>
      </g>
    )}
  </svg>
);

// -------------------------------------------------------------
// MAIN COMPONENT: QuantumDrilldown
// -------------------------------------------------------------
export default function QuantumDrilldown(): React.JSX.Element {
  const [activeTier, setActiveTier] = useState<'cryostat' | 'chip' | 'codespace'>('cryostat');

  // Interactive Codespace fault state
  const [errors, setErrors] = useState({
    p1: false,
    p2: false,
    p3: false,
    p4: false
  });
  const [isHealing, setIsHealing] = useState(false);

  const togglePlaquette = (key: keyof typeof errors) => {
    if (isHealing) return;
    setErrors(prev => ({ ...prev, [key]: !prev[key] }));
  };

  const triggerThermodynamicHealing = () => {
    if (isHealing) return;
    setIsHealing(true);

    const activeKeys = (Object.keys(errors) as Array<keyof typeof errors>).filter(k => errors[k]);
    if (activeKeys.length === 0) {
      setIsHealing(false);
      return;
    }

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
    }, 220);
  };

  const errorCount = Object.values(errors).filter(Boolean).length;
  const hasErrors = errorCount > 0;

  return (
    <div className="quantum-drilldown-container">
      {/* Top Header Bar with Segmented Tier Switcher */}
      <div className="quantum-drilldown-header">
        <div className="quantum-drilldown-title-group">
          <span className={`quantum-drilldown-badge ${activeTier}`}>
            {activeTier === 'cryostat' ? 'Level 1: Hardware' : activeTier === 'chip' ? 'Level 2: Silicon' : 'Level 3: Codespace'}
          </span>
          <h3 className="quantum-drilldown-title">Quantum Processing Architecture</h3>
        </div>

        {/* Mobile-First Segmented Touch Switcher */}
        <div className="quantum-tier-switcher">
          <button
            className={`quantum-tier-btn cryostat ${activeTier === 'cryostat' ? 'active' : ''}`}
            onClick={() => setActiveTier('cryostat')}
          >
            <span>🧊</span> Cryostat (10mK)
          </button>
          <button
            className={`quantum-tier-btn chip ${activeTier === 'chip' ? 'active' : ''}`}
            onClick={() => setActiveTier('chip')}
          >
            <span>⚡</span> QPU Chip
          </button>
          <button
            className={`quantum-tier-btn codespace ${activeTier === 'codespace' ? 'active' : ''}`}
            onClick={() => setActiveTier('codespace')}
          >
            <span>🕸️</span> Codespace Lattice
          </button>
        </div>
      </div>

      {/* Main Interactive Body */}
      <div className="quantum-drilldown-body">
        {/* Viewport Stage */}
        <div className="quantum-viewport-stage">
          <div className="quantum-svg-viewport">
            {activeTier === 'cryostat' && <CryostatGraphic />}
            {activeTier === 'chip' && <ChipGraphic />}
            {activeTier === 'codespace' && (
              <CodespaceLatticeGraphic
                errors={errors}
                onTogglePlaquette={togglePlaquette}
                isHealing={isHealing}
              />
            )}
          </div>
        </div>

        {/* Narrative & Telemetry Panel */}
        <div className="quantum-drilldown-info">
          <div>
            {activeTier === 'cryostat' && (
              <>
                <div className="quantum-info-header">
                  <div className="quantum-info-subtitle">MACROSCOPIC ISOLATION APPARATUS</div>
                  <h4 className="quantum-info-title">The Dilution Refrigerator</h4>
                </div>
                <p className="quantum-info-desc">
                  To protect fragile quantum information from thermal decoherence, physical quantum computers 
                  (IBM, Google, Rigetti) utilize staged helium dilution chandeliers. By cooling the lowest canister 
                  to <strong>10 millikelvin</strong> (colder than deep outer space), ambient thermal fluctuations are silenced, 
                  allowing macroscopic circuits to manifest subtle topological quantum behavior.
                </p>

                {/* Telemetry */}
                <div className="quantum-drilldown-telemetry">
                  <div className="drilldown-telemetry-item">
                    <span className="drilldown-telemetry-label">BASE TEMP</span>
                    <span className="drilldown-telemetry-value">0.010 K</span>
                  </div>
                  <div className="drilldown-telemetry-item">
                    <span className="drilldown-telemetry-label">CHAMBER VACUUM</span>
                    <span className="drilldown-telemetry-value amber">&lt; 10⁻⁶ mbar</span>
                  </div>
                  <div className="drilldown-telemetry-item">
                    <span className="drilldown-telemetry-label">THERMAL CASCADE</span>
                    <span className="drilldown-telemetry-value green">50K → 4K → 10mK</span>
                  </div>
                </div>
                <div className="quantum-action-hint">
                  Next: Tap <strong>QPU Chip</strong> to inspect the transmon lattice inside the canister.
                </div>
              </>
            )}

            {activeTier === 'chip' && (
              <>
                <div className="quantum-info-header">
                  <div className="quantum-info-subtitle">SILICON SUPERCONDUCTING HARDWARE</div>
                  <h4 className="quantum-info-title">The Heavy-Hex Transmon QPU</h4>
                </div>
                <p className="quantum-info-desc">
                  Inside the 10 mK shield lies the physical processor. In modern architectures like IBM Heron, 
                  superconducting transmons are arranged in a <strong>heavy-hexagonal lattice</strong> with coplanar 
                  waveguide resonators. Microwave pulses drive multi-qubit interactions, physically measuring 
                  syndrome parities to detect phase and bit-flip errors.
                </p>

                {/* Telemetry */}
                <div className="quantum-drilldown-telemetry">
                  <div className="drilldown-telemetry-item">
                    <span className="drilldown-telemetry-label">TOPOLOGY</span>
                    <span className="drilldown-telemetry-value amber">Heavy-Hexagonal</span>
                  </div>
                  <div className="drilldown-telemetry-item">
                    <span className="drilldown-telemetry-label">DRIVE FREQ</span>
                    <span className="drilldown-telemetry-value">4.8 - 5.2 GHz</span>
                  </div>
                  <div className="drilldown-telemetry-item">
                    <span className="drilldown-telemetry-label">GATE FIDELITY</span>
                    <span className="drilldown-telemetry-value green">99.85% (CZ)</span>
                  </div>
                </div>
                <div className="quantum-action-hint">
                  Next: Tap <strong>Codespace Lattice</strong> to see the underlying pre-geometric theory.
                </div>
              </>
            )}

            {activeTier === 'codespace' && (
              <>
                <div className="quantum-info-header">
                  <div className="quantum-info-subtitle">PRE-GEOMETRIC TOPOLOGICAL SUBSTRATE</div>
                  <h4 className="quantum-info-title">The Vacuum Stabilizer Codespace</h4>
                </div>
                <p className="quantum-info-desc">
                  Quantum Braid Dynamics reveals that physical hardware is an emulation of the pre-geometric vacuum. 
                  Every potential causal link is an edge qubit (|0⟩, |1⟩). Geometric face checks (Bp) 
                  and vertex checks (Av) continuously police topological consistency. Elementary fermions (the central 
                  tripartite braid) exist as topologically protected non-local knots that survive deletion noise.
                </p>

                {/* Telemetry */}
                <div className="quantum-drilldown-telemetry">
                  <div className="drilldown-telemetry-item">
                    <span className="drilldown-telemetry-label">CODESPACE PARITY</span>
                    <span className={`drilldown-telemetry-value ${hasErrors ? 'red' : 'green'}`}>
                      {hasErrors ? 'σ = -1 (UNSTABLE)' : 'σ = +1 (PROTECTED)'}
                    </span>
                  </div>
                  <div className="drilldown-telemetry-item">
                    <span className="drilldown-telemetry-label">LOCAL STRESS</span>
                    <span className={`drilldown-telemetry-value ${hasErrors ? 'red' : 'green'}`}>
                      {errorCount} Defect{errorCount !== 1 ? 's' : ''}
                    </span>
                  </div>
                  <div className="drilldown-telemetry-item">
                    <span className="drilldown-telemetry-label">DISSIPATION RULE</span>
                    <span className="drilldown-telemetry-value amber">λ_cat = e - 1</span>
                  </div>
                </div>

                {/* Interactive Controls for Tier 3 */}
                <div className="quantum-interactive-bar">
                  <button
                    className={`quantum-action-btn ${isHealing ? 'healing' : ''}`}
                    onClick={triggerThermodynamicHealing}
                    disabled={!hasErrors || isHealing}
                  >
                    {isHealing
                      ? 'DISSIPATING DEFECTS (λ = e - 1)...'
                      : hasErrors
                      ? 'TRIGGER THERMODYNAMIC HEALING'
                      : 'LATTICE SECURE (CLICK FACES TO INJECT ERRORS)'}
                  </button>
                </div>
              </>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

import React from 'react';

// Design constants
const BLUE = '#00f5ff';
const AMBER = '#ffb01f';
const BLUE_GLOW = 'rgba(0, 245, 255, 0.4)';
const AMBER_GLOW = 'rgba(245, 158, 11, 0.4)';

// Blueprint background helper for the graphics
const BlueprintGrid = () => (
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

// 1. Up Quark (u) - Chiral asymmetric braid (Writhe: 1, 1, 0)
// Two outer active ribbons crossing, one straight central ribbon (writhe 0)
export const UpQuarkGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    {/* Straight middle strand (Writhe 0) */}
    <line x1="50" y1="15" x2="50" y2="85" className="spectrum-svg-path" stroke={AMBER} strokeWidth="1" strokeDasharray="3 2" />
    {/* Twisting outer strands (Writhe 1 each) */}
    <path d="M 30 15 C 30 40, 70 60, 70 85" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" />
    <path d="M 70 15 C 70 40, 30 60, 30 85" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" />
    {/* Crossing point indicator */}
    <circle cx="50" cy="50" r="2" fill="#ffffff" />
  </svg>
);

// 2. Charm Quark (c) - C2 Crossing well (Writhe: 62, 62, 0)
// Higher density up-type quark. Straight middle strand, two outer strands wrapping multiple times in the central well.
export const CharmQuarkGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    {/* Crossing well boundary */}
    <rect x="25" y="30" width="50" height="40" fill="none" stroke="rgba(0, 245, 255, 0.1)" strokeWidth="0.75" strokeDasharray="3 3" />
    {/* Straight middle strand (Writhe 0) */}
    <line x1="50" y1="15" x2="50" y2="85" className="spectrum-svg-path" stroke={AMBER} strokeWidth="1" strokeDasharray="3 2" />
    {/* Wrap 1 */}
    <path d="M 30 15 C 30 35, 70 30, 30 50 C 30 62, 70 62, 70 85" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" fill="none" />
    <path d="M 70 15 C 70 35, 30 30, 70 50 C 70 62, 30 62, 30 85" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" fill="none" />
    {/* Dual crossing points */}
    <circle cx="50" cy="38" r="2" fill="#ffffff" />
    <circle cx="50" cy="62" r="2" fill="#ffffff" />
  </svg>
);

// 3. Top Quark (t) - Torsion Peak (Writhe: 712, 712, 0)
// Extremely dense up-type quark. Central straight strand, outer strands wrapping in ultra-dense helix.
export const TopQuarkGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    {/* Straight middle strand (Writhe 0) */}
    <line x1="50" y1="15" x2="50" y2="85" className="spectrum-svg-path" stroke={AMBER} strokeWidth="1" strokeDasharray="3 2" />
    {/* High frequency helix wrapping */}
    <path d="M 30 15 Q 70 22, 50 30 Q 30 38, 50 46 Q 70 54, 50 62 Q 30 70, 50 78 Q 70 82, 30 85" 
      className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" fill="none" />
    <path d="M 70 15 Q 30 22, 50 30 Q 70 38, 50 46 Q 30 54, 50 62 Q 70 70, 50 78 Q 30 82, 70 85" 
      className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" fill="none" />
    
    <circle cx="50" cy="30" r="1.5" fill="#ffffff" />
    <circle cx="50" cy="46" r="1.5" fill="#ffffff" />
    <circle cx="50" cy="62" r="1.5" fill="#ffffff" />
    <circle cx="50" cy="78" r="1.5" fill="#ffffff" className="spectrum-node-pulse" />
  </svg>
);

// 4. Gluon (g) - su(3) Adjoint Swaps (Permutation rewrite)
// Shows three strands with a dotted interaction bubble swapping outer colors.
export const GluonGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    <line x1="30" y1="15" x2="30" y2="35" stroke={BLUE} strokeWidth="1.5" />
    <line x1="50" y1="15" x2="50" y2="35" stroke={AMBER} strokeWidth="1.5" />
    <line x1="70" y1="15" x2="70" y2="35" stroke={BLUE} strokeWidth="1.5" />
    
    <circle cx="50" cy="50" r="20" fill="none" stroke={AMBER} strokeWidth="1" strokeDasharray="3 3" />
    
    <path d="M 30 35 C 30 45, 70 55, 70 65" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" />
    <path d="M 70 35 C 70 45, 30 55, 30 65" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" />
    <path d="M 50 35 L 50 65" className="spectrum-svg-path" stroke={AMBER} strokeWidth="1.5" strokeDasharray="2 2" />
    
    <path d="M 66 60 L 70 65 L 65 67" fill="none" stroke={BLUE} strokeWidth="1" />
    <path d="M 34 60 L 30 65 L 35 67" fill="none" stroke={BLUE} strokeWidth="1" />
    
    <line x1="30" y1="65" x2="30" y2="85" stroke={BLUE} strokeWidth="1.5" />
    <line x1="50" y1="65" x2="50" y2="85" stroke={AMBER} strokeWidth="1.5" />
    <line x1="70" y1="65" x2="70" y2="85" stroke={BLUE} strokeWidth="1.5" />
  </svg>
);

// 5. Electron (e) - Symmetric 3-braid (Writhe: -1, -1, -1)
// All three strands twist symmetrically around each other.
export const ElectronGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    <path d="M 30 15 C 30 30, 70 40, 70 50 C 70 60, 30 70, 30 85" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" />
    <path d="M 50 15 C 70 25, 30 35, 30 50 C 30 65, 70 75, 50 85" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" />
    <path d="M 70 15 C 70 30, 30 40, 30 50 C 30 60, 70 70, 70 85" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" />
    
    <circle cx="50" cy="32" r="1.5" fill="#ffffff" />
    <circle cx="38" cy="50" r="1.5" fill="#ffffff" />
    <circle cx="50" cy="68" r="1.5" fill="#ffffff" />
  </svg>
);

// 6. Muon (μ) - Symmetric C2 (Writhe: -14, -14, -14)
// Tighter symmetric 3-braid, double twist density.
export const MuonGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    <path d="M 30 15 C 30 25, 70 30, 70 40 C 70 50, 30 55, 30 65 C 30 75, 70 80, 70 85" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" />
    <path d="M 50 15 C 70 20, 30 28, 30 40 C 30 52, 70 60, 70 72 C 70 80, 30 80, 50 85" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" />
    <path d="M 70 15 C 70 25, 30 30, 30 40 C 30 50, 70 55, 70 65 C 70 75, 30 80, 30 85" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" />
    
    <circle cx="50" cy="27" r="1.5" fill="#ffffff" />
    <circle cx="50" cy="48" r="1.5" fill="#ffffff" />
    <circle cx="50" cy="62" r="1.5" fill="#ffffff" />
    <circle cx="50" cy="78" r="1.5" fill="#ffffff" />
  </svg>
);

// 7. Tau (τ) - Symmetric C3 (Writhe: -59, -59, -59)
// Extremely tight, dense symmetric twist cable.
export const TauGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    <path d="M 50 15 L 50 85" stroke="rgba(0, 245, 255, 0.2)" strokeWidth="4" />
    <path d="M 35 15 Q 65 22, 50 30 Q 35 38, 50 46 Q 65 54, 50 62 Q 35 70, 50 78 Q 65 82, 35 85" 
      className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" fill="none" />
    <path d="M 50 15 Q 35 22, 50 30 Q 65 38, 50 46 Q 35 54, 50 62 Q 65 70, 50 78 Q 35 82, 50 85" 
      className="spectrum-svg-path" stroke={AMBER} strokeWidth="1.25" fill="none" strokeDasharray="2 1" />
    <path d="M 65 15 Q 35 25, 50 38 Q 65 50, 50 62 Q 35 72, 65 85" 
      className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.25" fill="none" />
  </svg>
);

// 8. Photon (γ) - U(1) Frame Twist
// Three parallel strands twisting 360 degrees as a cohesive frame update.
export const PhotonGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    {/* 3 twisted frame ribbons */}
    <path d="M 32 15 C 32 35, 68 45, 32 65 L 32 85" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" fill="none" />
    <path d="M 50 15 C 50 35, 50 50, 50 65 L 50 85" className="spectrum-svg-path" stroke={AMBER} strokeWidth="1.25" fill="none" strokeDasharray="3 2" />
    <path d="M 68 15 C 68 35, 32 45, 68 65 L 68 85" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" fill="none" />
    
    <circle cx="50" cy="50" r="2.5" fill="#ffffff" />
  </svg>
);

// 9. Electron Neutrino (νe) - Folded Loop Gen I (Writhe: 0, 0, 0)
// Minimal color-neutral vacuum loop: 3 nested parallel loops folding back at the base. No crossings.
export const ElectronNeutrinoGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    {/* 3 parallel folded loops */}
    <path d="M 35 15 L 35 52 C 35 72, 65 72, 65 52 L 65 15" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" fill="none" />
    <path d="M 43 15 L 43 52 C 43 63, 57 63, 57 52 L 57 15" className="spectrum-svg-path" stroke={AMBER} strokeWidth="1.25" fill="none" strokeDasharray="3 2" />
    <path d="M 50 15 L 50 52 C 50 54, 50 54, 50 52 L 50 15" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" fill="none" />
    
    {/* Singular fold vertex */}
    <circle cx="50" cy="62" r="3" fill="#ffffff" className="spectrum-node-pulse" />
  </svg>
);

// 10. Muon Neutrino (νμ) - Folded Loop Gen II (1 twist fold)
// 3 nested loops that cross each other once near the fold base (2 twist crossings).
export const MuonNeutrinoGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    {/* Twisted folded loops */}
    <path d="M 35 15 C 35 35, 65 45, 65 60 C 65 70, 35 70, 35 60 C 35 45, 65 35, 65 15" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" fill="none" />
    <path d="M 44 15 C 44 32, 56 38, 56 50 C 56 58, 44 58, 44 50 C 44 38, 56 32, 56 15" className="spectrum-svg-path" stroke={AMBER} strokeWidth="1.25" fill="none" strokeDasharray="3 2" />
    <path d="M 50 15 L 50 42 C 50 45, 50 45, 50 42 L 50 15" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" fill="none" />
    
    <circle cx="50" cy="46" r="2" fill="#ffffff" />
    <circle cx="50" cy="54" r="2" fill="#ffffff" />
    <circle cx="50" cy="65" r="2.5" fill="#ffffff" className="spectrum-node-pulse" />
  </svg>
);

// 11. Tau Neutrino (ντ) - Folded Loop Gen III (Multiple twist folds)
// 3 nested loops twisting multiple times at the fold base.
export const TauNeutrinoGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    <path d="M 32 15 C 32 30, 68 35, 68 45 C 68 55, 32 60, 32 70 C 32 75, 68 75, 68 70 C 68 60, 32 55, 32 45 C 32 35, 68 30, 68 15" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" fill="none" />
    <path d="M 41 15 C 41 28, 59 33, 59 43 C 59 50, 41 55, 41 62 C 41 66, 59 66, 59 62 C 59 55, 41 50, 41 43 C 41 33, 59 28, 59 15" className="spectrum-svg-path" stroke={AMBER} strokeWidth="1.25" fill="none" strokeDasharray="2 1" />
    <path d="M 50 15 C 50 25, 50 35, 50 50 C 50 54, 50 54, 50 50 L 50 15" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" fill="none" />
    
    <circle cx="50" cy="38" r="1.5" fill="#ffffff" />
    <circle cx="50" cy="49" r="1.5" fill="#ffffff" />
    <circle cx="50" cy="56" r="1.5" fill="#ffffff" />
    <circle cx="50" cy="64" r="1.5" fill="#ffffff" />
    <circle cx="50" cy="73" r="2.5" fill="#ffffff" className="spectrum-node-pulse" />
  </svg>
);

// 12. Z Boson (Z) - su(2)L Neutrality (Weak neutral rewrite)
// Three channels on left and right merging at a central neutral fusion vertex.
export const ZBosonGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    {/* Left Incoming 3-braid */}
    <path d="M 20 25 C 35 25, 45 45, 50 50" stroke={AMBER} strokeWidth="1.25" fill="none" strokeDasharray="3 2" />
    <path d="M 20 35 C 35 35, 45 48, 50 50" stroke={BLUE} strokeWidth="1.5" fill="none" />
    <path d="M 20 45 C 35 45, 45 50, 50 50" stroke={BLUE} strokeWidth="1.5" fill="none" />
    
    {/* Right Incoming 3-braid */}
    <path d="M 80 25 C 65 25, 55 45, 50 50" stroke={AMBER} strokeWidth="1.25" fill="none" strokeDasharray="3 2" />
    <path d="M 80 35 C 65 35, 55 48, 50 50" stroke={BLUE} strokeWidth="1.5" fill="none" />
    <path d="M 80 45 C 65 45, 55 50, 50 50" stroke={BLUE} strokeWidth="1.5" fill="none" />

    {/* Neutral weak fusion throat */}
    <circle cx="50" cy="50" r="3.5" fill="#00f5ff" className="spectrum-node-pulse" />
    
    {/* Outgoing product channels */}
    <path d="M 50 50 C 45 50, 35 55, 20 55" stroke={BLUE} strokeWidth="1.5" fill="none" />
    <path d="M 50 50 C 45 52, 35 65, 20 65" stroke={AMBER} strokeWidth="1.25" fill="none" strokeDasharray="3 2" />
    <path d="M 50 50 C 45 55, 35 75, 20 75" stroke={BLUE} strokeWidth="1.5" fill="none" />

    <path d="M 50 50 C 55 50, 65 55, 80 55" stroke={BLUE} strokeWidth="1.5" fill="none" />
    <path d="M 50 50 C 55 52, 65 65, 80 65" stroke={AMBER} strokeWidth="1.25" fill="none" strokeDasharray="3 2" />
    <path d="M 50 50 C 55 55, 65 75, 80 75" stroke={BLUE} strokeWidth="1.5" fill="none" />
  </svg>
);

// 13. Down Quark (d) - Asymmetric braid (Writhe: -1, 0, 0)
// One active wrapping outer strand, two passive straight parallel strands (writhe 0).
export const DownQuarkGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    {/* Two straight passive ribbons */}
    <line x1="38" y1="15" x2="38" y2="85" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" />
    <line x1="52" y1="15" x2="52" y2="85" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" />
    {/* One active wrapping ribbon (Writhe -1) */}
    <path d="M 68 15 C 68 35, 22 45, 68 65 L 68 85" className="spectrum-svg-path" stroke={AMBER} strokeWidth="1.5" strokeDasharray="3 2" fill="none" />
    
    <circle cx="38" cy="42" r="2" fill="#ffffff" />
    <circle cx="52" cy="48" r="2" fill="#ffffff" />
  </svg>
);

// 14. Strange Quark (s) - S2 Crossing (Writhe: -24, 0, 0)
// Two straight passive strands, one active wrapping strand.
export const StrangeQuarkGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    {/* Straight passive strands */}
    <line x1="38" y1="15" x2="38" y2="85" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" />
    <line x1="52" y1="15" x2="52" y2="85" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" />
    {/* One active wrapping strand */}
    <path d="M 68 15 C 68 35, 22 32, 68 50 C 68 62, 22 62, 68 85" className="spectrum-svg-path" stroke={AMBER} strokeWidth="1.5" fill="none" />
    
    <circle cx="38" cy="36" r="2" fill="#ffffff" />
    <circle cx="52" cy="45" r="2" fill="#ffffff" />
    <circle cx="38" cy="55" r="2" fill="#ffffff" />
    <circle cx="52" cy="64" r="2" fill="#ffffff" />
  </svg>
);

// 15. Bottom Quark (b) - B3 Crossing (Writhe: -157, 0, 0)
// Heavy asymmetric quark: two straight passive strands, one active wrapping strand in a dense spiral.
export const BottomQuarkGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    {/* Straight passive strands */}
    <line x1="38" y1="15" x2="38" y2="85" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" />
    <line x1="52" y1="15" x2="52" y2="85" className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.5" />
    {/* High density wrap */}
    <path d="M 68 15 Q 22 25, 45 32 Q 68 39, 45 46 Q 22 53, 45 60 Q 68 67, 45 74 Q 22 81, 68 85" 
      className="spectrum-svg-path" stroke={AMBER} strokeWidth="1.5" fill="none" />
    
    <circle cx="38" cy="30" r="1.5" fill="#ffffff" />
    <circle cx="52" cy="39" r="1.5" fill="#ffffff" />
    <circle cx="38" cy="48" r="1.5" fill="#ffffff" />
    <circle cx="52" cy="58" r="1.5" fill="#ffffff" />
    <circle cx="38" cy="67" r="1.5" fill="#ffffff" />
    <circle cx="52" cy="76" r="1.5" fill="#ffffff" />
  </svg>
);

// 16. W Boson (W) - su(2) Charged Swaps (Charged rewrite)
// Three strands enter and exit, and a wavy gauge field (W boson) branches from a chiral vertex carrying charge.
export const WBosonGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    {/* Incoming 3-braid strands */}
    <path d="M 20 20 C 35 20, 42 42, 45 50" stroke={BLUE} strokeWidth="1.5" fill="none" />
    <path d="M 20 30 C 35 30, 43 45, 45 50" stroke={AMBER} strokeWidth="1.25" fill="none" strokeDasharray="3 2" />
    <path d="M 20 40 C 35 40, 44 48, 45 50" stroke={BLUE} strokeWidth="1.5" fill="none" />
    
    {/* Chiral active vertex */}
    <circle cx="45" cy="50" r="3.5" fill="#ffb01f" className="spectrum-node-pulse" />
    
    {/* Outgoing 3-braid strands */}
    <path d="M 45 50 C 47 52, 60 55, 80 55" stroke={BLUE} strokeWidth="1.5" fill="none" />
    <path d="M 45 50 C 47 55, 60 68, 80 68" stroke={AMBER} strokeWidth="1.25" fill="none" strokeDasharray="3 2" />
    <path d="M 45 50 C 47 58, 60 78, 80 78" stroke={BLUE} strokeWidth="1.5" fill="none" />
    
    {/* Wavy departing W-boson propagator */}
    <path d="M 45 50 Q 42 60, 47 68 Q 52 75, 47 80 Q 42 85, 45 90" 
      className="spectrum-svg-path" stroke={BLUE} strokeWidth="1.75" fill="none" />
    <path d="M 42 86 L 45 90 L 49 86" fill="none" stroke={BLUE} strokeWidth="1" />
  </svg>
);

// Central selector helper
export const ParticleGraphic = ({ symbol }: { symbol: string }) => {
  switch (symbol) {
    case 'u': return <UpQuarkGraphic />;
    case 'c': return <CharmQuarkGraphic />;
    case 't': return <TopQuarkGraphic />;
    case 'g': return <GluonGraphic />;
    case 'e': return <ElectronGraphic />;
    case 'μ': return <MuonGraphic />;
    case 'τ': return <TauGraphic />;
    case 'γ': return <PhotonGraphic />;
    case 'νe': return <ElectronNeutrinoGraphic />;
    case 'νμ': return <MuonNeutrinoGraphic />;
    case 'ντ': return <TauNeutrinoGraphic />;
    case 'Z': return <ZBosonGraphic />;
    case 'd': return <DownQuarkGraphic />;
    case 's': return <StrangeQuarkGraphic />;
    case 'b': return <BottomQuarkGraphic />;
    case 'W': return <WBosonGraphic />;
    default: return null;
  }
};

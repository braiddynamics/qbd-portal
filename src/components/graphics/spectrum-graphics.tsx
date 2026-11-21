import React from 'react';

// Unified Blueprint & Semantic Color Constants
const BG = '#0D1117';
const CYAN = '#00f5ff';
const TEAL = '#25c2a0';
const AMBER = '#ffb01f';
const RED = '#ef4444';
const GREEN = '#22c55e';
const BLUE = '#38bdf8';
const ORANGE = '#f97316';
const PASSIVE = 'rgba(148, 163, 184, 0.42)';

// Subtle blueprint grid background helper
const BlueprintGrid = () => (
  <>
    <circle cx="20" cy="20" r="0.5" fill="rgba(255,255,255,0.14)" />
    <circle cx="20" cy="50" r="0.5" fill="rgba(255,255,255,0.14)" />
    <circle cx="20" cy="80" r="0.5" fill="rgba(255,255,255,0.14)" />
    <circle cx="50" cy="20" r="0.5" fill="rgba(255,255,255,0.14)" />
    <circle cx="50" cy="50" r="0.5" fill="rgba(255,255,255,0.14)" />
    <circle cx="50" cy="80" r="0.5" fill="rgba(255,255,255,0.14)" />
    <circle cx="80" cy="20" r="0.5" fill="rgba(255,255,255,0.14)" />
    <circle cx="80" cy="50" r="0.5" fill="rgba(255,255,255,0.14)" />
    <circle cx="80" cy="80" r="0.5" fill="rgba(255,255,255,0.14)" />
    <line x1="10" y1="50" x2="90" y2="50" stroke="rgba(255,255,255,0.05)" strokeWidth="0.5" strokeDasharray="2 2" />
    <line x1="50" y1="10" x2="50" y2="90" stroke="rgba(255,255,255,0.05)" strokeWidth="0.5" strokeDasharray="2 2" />
  </>
);

/**
 * Renders a framed ribbon centered at `cx` from `yStart` to `yEnd`.
 * - `turns = 0`: Untwisted flat framed ribbon (two parallel rails + subtle stabilizer rungs, w = 0).
 * - `turns > 0`: Chiral framed ribbon with true 3D over/under crossing masks:
 *     - `chirality = +1`: Right-handed (+w) — descending `\` rail crosses OVER `/` rail.
 *     - `chirality = -1`: Left-handed (-w) — descending `/` rail crosses OVER `\` rail.
 */
interface FramedRibbonProps {
  cx: number;
  turns: number;
  chirality?: 1 | -1;
  color: string;
  altColor: string;
  yStart?: number;
  yEnd?: number;
  halfWidth?: number;
  strokeWidth?: number;
}

const FramedRibbon: React.FC<FramedRibbonProps> = ({
  cx,
  turns,
  chirality = 1,
  color,
  altColor,
  yStart = 14,
  yEnd = 86,
  halfWidth = 6.5,
  strokeWidth = 1.6,
}) => {
  if (turns === 0) {
    const rungYs = [26, 42, 58, 74].filter((y) => y > yStart + 4 && y < yEnd - 4);
    return (
      <g>
        {rungYs.map((ry, i) => (
          <line
            key={i}
            x1={cx - halfWidth * 0.55}
            y1={ry}
            x2={cx + halfWidth * 0.55}
            y2={ry}
            stroke={PASSIVE}
            strokeWidth="0.6"
            opacity="0.55"
          />
        ))}
        <line
          x1={cx - halfWidth * 0.55}
          y1={yStart}
          x2={cx - halfWidth * 0.55}
          y2={yEnd}
          stroke={PASSIVE}
          strokeWidth="1.2"
          strokeDasharray="3 2"
          strokeLinecap="round"
        />
        <line
          x1={cx + halfWidth * 0.55}
          y1={yStart}
          x2={cx + halfWidth * 0.55}
          y2={yEnd}
          stroke={PASSIVE}
          strokeWidth="1.2"
          strokeDasharray="3 2"
          strokeLinecap="round"
        />
      </g>
    );
  }

  const segHeight = (yEnd - yStart) / turns;
  const segments = Array.from({ length: turns }, (_, idx) => {
    const y0 = yStart + idx * segHeight;
    const y1 = y0 + segHeight;
    const ym = (y0 + y1) / 2;
    const ctrlOffset = segHeight * 0.42;

    // Even index: edge A starts left -> goes right; edge B starts right -> goes left.
    // Odd index:  edge A starts right -> goes left; edge B starts left -> goes right.
    const aStartsLeft = idx % 2 === 0;
    const xL = cx - halfWidth;
    const xR = cx + halfWidth;

    const pathLR = `M ${xL} ${y0} C ${xL} ${y0 + ctrlOffset}, ${xR} ${y1 - ctrlOffset}, ${xR} ${y1}`;
    const pathRL = `M ${xR} ${y0} C ${xR} ${y0 + ctrlOffset}, ${xL} ${y1 - ctrlOffset}, ${xL} ${y1}`;

    const colorLR = aStartsLeft ? color : altColor;
    const colorRL = aStartsLeft ? altColor : color;

    // Chirality: +1 puts LR (\) OVER RL (/); -1 puts RL (/) OVER LR (\).
    const underPath = chirality === 1 ? pathRL : pathLR;
    const underColor = chirality === 1 ? colorRL : colorLR;
    const overPath = chirality === 1 ? pathLR : pathRL;
    const overColor = chirality === 1 ? colorLR : colorRL;

    return (
      <g key={idx}>
        {/* Subtle ribbon surface shading inside twist */}
        <path
          d={`M ${xL} ${y0} C ${xL} ${ym}, ${xR} ${ym}, ${xR} ${y1} L ${xL} ${y1} C ${xL} ${ym}, ${xR} ${ym}, ${xR} ${y0} Z`}
          fill={color}
          opacity="0.06"
        />
        {/* Under rail */}
        <path
          d={underPath}
          fill="none"
          stroke={underColor}
          strokeWidth={strokeWidth}
          strokeLinecap="round"
        />
        {/* Over rail eraser mask (creates true 3D chiral over-crossing) */}
        <path
          d={overPath}
          fill="none"
          stroke={BG}
          strokeWidth={strokeWidth + 3.2}
          strokeLinecap="round"
        />
        {/* Over rail */}
        <path
          d={overPath}
          fill="none"
          stroke={overColor}
          strokeWidth={strokeWidth}
          strokeLinecap="round"
        />
      </g>
    );
  });

  return <g>{segments}</g>;
};

// ============================================================================
// ROW 1: UP-TYPE QUARKS (+2/3 e) — Writhe (+w, +w, 0), Right-Handed (+1)
// Two parallel positively twisted ribbons + one flat spectator ribbon (§7.3.9.3)
// ============================================================================

// 1. Up Quark (u): (+1, +1, 0)
export const UpQuarkGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    {/* Parallel-sharing bridge indicator between R1 and R2 (k_share = 1) */}
    <line x1="31" y1="50" x2="43" y2="50" stroke={CYAN} strokeWidth="0.9" strokeDasharray="1.8 1.5" opacity="0.65" />
    <FramedRibbon cx={24} turns={1} chirality={1} color={CYAN} altColor="#7dd3fc" />
    <FramedRibbon cx={50} turns={1} chirality={1} color={CYAN} altColor="#7dd3fc" />
    <FramedRibbon cx={76} turns={0} color={PASSIVE} altColor={PASSIVE} />
  </svg>
);

// 2. Charm Quark (c): (+62, +62, 0) — Denser Gen II right-handed winding
export const CharmQuarkGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    <rect x="13" y="25" width="48" height="50" rx="4" fill="none" stroke="rgba(0, 245, 255, 0.14)" strokeWidth="0.75" strokeDasharray="3 2" />
    <line x1="31" y1="32" x2="43" y2="32" stroke={CYAN} strokeWidth="0.85" strokeDasharray="1.8 1.5" opacity="0.55" />
    <line x1="31" y1="68" x2="43" y2="68" stroke={CYAN} strokeWidth="0.85" strokeDasharray="1.8 1.5" opacity="0.55" />
    <FramedRibbon cx={24} turns={2} chirality={1} color={CYAN} altColor="#7dd3fc" />
    <FramedRibbon cx={50} turns={2} chirality={1} color={CYAN} altColor="#7dd3fc" />
    <FramedRibbon cx={76} turns={0} color={PASSIVE} altColor={PASSIVE} />
  </svg>
);

// 3. Top Quark (t): (+712, +712, 0) — High-torsion Gen III right-handed coils
export const TopQuarkGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    <rect x="12" y="13" width="50" height="74" rx="5" fill="rgba(0, 245, 255, 0.03)" stroke="rgba(0, 245, 255, 0.22)" strokeWidth="0.75" strokeDasharray="2 2" />
    <FramedRibbon cx={24} turns={4} chirality={1} color={CYAN} altColor="#7dd3fc" halfWidth={6.5} strokeWidth={1.5} />
    <FramedRibbon cx={50} turns={4} chirality={1} color={CYAN} altColor="#7dd3fc" halfWidth={6.5} strokeWidth={1.5} />
    <FramedRibbon cx={76} turns={0} color={PASSIVE} altColor={PASSIVE} />
  </svg>
);

// ============================================================================
// ROW 2: DOWN-TYPE QUARKS (-1/3 e) — Writhe (-w, 0, 0), Left-Handed (-1)
// One negatively twisted ribbon + two flat spectator ribbons (§7.3.9.3)
// ============================================================================

// 4. Down Quark (d): (-1, 0, 0)
export const DownQuarkGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    <FramedRibbon cx={24} turns={1} chirality={-1} color={AMBER} altColor={CYAN} />
    <FramedRibbon cx={50} turns={0} color={PASSIVE} altColor={PASSIVE} />
    <FramedRibbon cx={76} turns={0} color={PASSIVE} altColor={PASSIVE} />
  </svg>
);

// 5. Strange Quark (s): (-24, 0, 0)
export const StrangeQuarkGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    <rect x="13" y="25" width="22" height="50" rx="4" fill="none" stroke="rgba(255, 176, 31, 0.18)" strokeWidth="0.75" strokeDasharray="3 2" />
    <FramedRibbon cx={24} turns={2} chirality={-1} color={AMBER} altColor={CYAN} />
    <FramedRibbon cx={50} turns={0} color={PASSIVE} altColor={PASSIVE} />
    <FramedRibbon cx={76} turns={0} color={PASSIVE} altColor={PASSIVE} />
  </svg>
);

// 6. Bottom Quark (b): (-157, 0, 0)
export const BottomQuarkGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    <rect x="12" y="13" width="24" height="74" rx="5" fill="rgba(255, 176, 31, 0.04)" stroke="rgba(255, 176, 31, 0.25)" strokeWidth="0.75" strokeDasharray="2 2" />
    <FramedRibbon cx={24} turns={4} chirality={-1} color={AMBER} altColor={CYAN} halfWidth={6.5} strokeWidth={1.5} />
    <FramedRibbon cx={50} turns={0} color={PASSIVE} altColor={PASSIVE} />
    <FramedRibbon cx={76} turns={0} color={PASSIVE} altColor={PASSIVE} />
  </svg>
);

// ============================================================================
// ROW 3: CHARGED LEPTONS (-1 e) — Writhe (-w, -w, -w), Symmetric Left-Handed (-1)
// All three ribbons carry identical left-handed twists (color singlet, §7.3.9.3)
// ============================================================================

// 7. Electron (e): (-1, -1, -1)
export const ElectronGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    <FramedRibbon cx={23} turns={1} chirality={-1} color={TEAL} altColor="#6ee7b7" halfWidth={6} />
    <FramedRibbon cx={50} turns={1} chirality={-1} color={TEAL} altColor="#6ee7b7" halfWidth={6} />
    <FramedRibbon cx={77} turns={1} chirality={-1} color={TEAL} altColor="#6ee7b7" halfWidth={6} />
  </svg>
);

// 8. Muon (μ): (-14, -14, -14)
export const MuonGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    <rect x="12" y="25" width="76" height="50" rx="5" fill="none" stroke="rgba(37, 194, 160, 0.16)" strokeWidth="0.75" strokeDasharray="3 2" />
    <FramedRibbon cx={23} turns={2} chirality={-1} color={TEAL} altColor="#6ee7b7" halfWidth={6} />
    <FramedRibbon cx={50} turns={2} chirality={-1} color={TEAL} altColor="#6ee7b7" halfWidth={6} />
    <FramedRibbon cx={77} turns={2} chirality={-1} color={TEAL} altColor="#6ee7b7" halfWidth={6} />
  </svg>
);

// 9. Tau (τ): (-59, -59, -59)
export const TauGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    <rect x="11" y="13" width="78" height="74" rx="5" fill="rgba(37, 194, 160, 0.03)" stroke="rgba(37, 194, 160, 0.24)" strokeWidth="0.75" strokeDasharray="2 2" />
    <FramedRibbon cx={23} turns={4} chirality={-1} color={TEAL} altColor="#6ee7b7" halfWidth={6} strokeWidth={1.45} />
    <FramedRibbon cx={50} turns={4} chirality={-1} color={TEAL} altColor="#6ee7b7" halfWidth={6} strokeWidth={1.45} />
    <FramedRibbon cx={77} turns={4} chirality={-1} color={TEAL} altColor="#6ee7b7" halfWidth={6} strokeWidth={1.45} />
  </svg>
);

// ============================================================================
// ROW 4: NEUTRINOS (Q = 0) — Folded Braid (§9.6.1.2)
// Left braid arm β_+ (writhe +w, right-handed) folded into mirror right anti-braid
// arm β_- (writhe -w, left-handed) at a bottom fold vortex: W_+ + W_- = 0.
// ============================================================================

const FoldedNeutrino: React.FC<{ turns: number; vortexRings: number }> = ({ turns, vortexRings }) => {
  const yTop = 14;
  const yFoldTop = 62;
  const yVortex = 81;

  return (
    <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
      <BlueprintGrid />

      {/* Subtle symmetry axis between β_+ and β_- arms */}
      <line x1="50" y1="12" x2="50" y2="72" stroke="rgba(255,255,255,0.08)" strokeWidth="0.7" strokeDasharray="2 2" />

      {/* Fold loop connecting left arm (cx=28) and right arm (cx=72) through the bottom vortex */}
      <path
        d={`M 23 ${yFoldTop} C 23 ${yVortex + 3}, 77 ${yVortex + 3}, 77 ${yFoldTop}`}
        fill="none"
        stroke={TEAL}
        strokeWidth="1.45"
        opacity="0.85"
      />
      <path
        d={`M 33 ${yFoldTop} C 33 ${yVortex - 6}, 67 ${yVortex - 6}, 67 ${yFoldTop}`}
        fill="none"
        stroke={AMBER}
        strokeWidth="1.25"
        strokeDasharray="2.5 1.5"
        opacity="0.75"
      />

      {/* Left arm: β_+ (+w right-handed twist) */}
      <FramedRibbon
        cx={28}
        turns={turns}
        chirality={1}
        color={TEAL}
        altColor={CYAN}
        yStart={yTop}
        yEnd={yFoldTop}
        halfWidth={5}
        strokeWidth={1.5}
      />

      {/* Right arm: β_- (-w mirror left-handed anti-twist) */}
      <FramedRibbon
        cx={72}
        turns={turns}
        chirality={-1}
        color={AMBER}
        altColor={TEAL}
        yStart={yTop}
        yEnd={yFoldTop}
        halfWidth={5}
        strokeWidth={1.5}
      />

      {/* Bottom Fold Vortex (N_fold > 0) */}
      {vortexRings >= 3 && (
        <circle cx="50" cy={yVortex - 1} r="10" fill="none" stroke={TEAL} strokeWidth="0.7" strokeDasharray="2 2" opacity="0.45" />
      )}
      {vortexRings >= 2 && (
        <circle cx="50" cy={yVortex - 1} r="7" fill="none" stroke={AMBER} strokeWidth="0.85" strokeDasharray="2.5 1.5" opacity="0.65" />
      )}
      <circle cx="50" cy={yVortex - 1} r="4" fill="rgba(37, 194, 160, 0.25)" stroke={TEAL} strokeWidth="1.2" className="spectrum-node-pulse" />
      <circle cx="50" cy={yVortex - 1} r="1.8" fill="#ffffff" />
    </svg>
  );
};

// 10. Electron Neutrino (νe): Minimal Gen I folded braid (+1 / -1 mirror fold)
export const ElectronNeutrinoGraphic = () => <FoldedNeutrino turns={1} vortexRings={1} />;

// 11. Muon Neutrino (νμ): Gen II folded braid (+2 / -2 mirror fold)
export const MuonNeutrinoGraphic = () => <FoldedNeutrino turns={2} vortexRings={2} />;

// 12. Tau Neutrino (ντ): Gen III folded braid (+3 / -3 mirror fold)
export const TauNeutrinoGraphic = () => <FoldedNeutrino turns={3} vortexRings={3} />;

// ============================================================================
// COLUMN 4: GAUGE FIELDS (REWRITES) — Ch. 8 (§8.3.1.2, §8.4, §8.5.5.1)
// ============================================================================

// 13. Gluon (g) — Adjacent SU(3) swap (1 <-> 2) leaving ribbon 3 spectator (§8.3.1.2)
export const GluonGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />

    {/* Interaction zone around adjacent pair R1 (Red) & R2 (Green) */}
    <circle cx="38" cy="50" r="20" fill="rgba(239, 68, 68, 0.04)" stroke={AMBER} strokeWidth="1" strokeDasharray="3 2.5" opacity="0.7" />

    {/* Spectator Ribbon 3 (Blue) — straight through */}
    <line x1="74" y1="14" x2="74" y2="86" stroke={BLUE} strokeWidth="2.2" strokeLinecap="round" opacity="0.85" />

    {/* Ribbon 2 (Green) — Under crossing (52 -> 24) */}
    <path d="M 52 14 L 52 34 C 52 46, 24 54, 24 66 L 24 86" fill="none" stroke={GREEN} strokeWidth="2.2" strokeLinecap="round" />

    {/* Eraser mask for Ribbon 1 (Red) over-crossing */}
    <path d="M 24 14 L 24 34 C 24 46, 52 54, 52 66 L 52 86" fill="none" stroke={BG} strokeWidth="6" strokeLinecap="round" />

    {/* Ribbon 1 (Red) — Over crossing (24 -> 52) */}
    <path d="M 24 14 L 24 34 C 24 46, 52 54, 52 66 L 52 86" fill="none" stroke={RED} strokeWidth="2.2" strokeLinecap="round" />

    {/* Direction arrows indicating completed adjacent swap */}
    <path d="M 48.5 81 L 52 86 L 55.5 81" fill="none" stroke={RED} strokeWidth="1.3" strokeLinecap="round" strokeLinejoin="round" />
    <path d="M 20.5 81 L 24 86 L 27.5 81" fill="none" stroke={GREEN} strokeWidth="1.3" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

// 14. Photon (γ) — 4-Cycle U(1) Enclosing Phase Transport (§8.5.5.1)
export const PhotonGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />

    {/* Enclosing 4-Cycle Phase Transport Plaquette (v1-v2-v3-v4) */}
    <polygon
      points="50,20 80,50 50,80 20,50"
      fill="rgba(0, 245, 255, 0.05)"
      stroke={CYAN}
      strokeWidth="1.6"
      strokeLinejoin="round"
    />
    {/* 4-cycle directional phase arrows */}
    <path d="M 62 29 L 67 37 L 59 35" fill="none" stroke={CYAN} strokeWidth="1.2" strokeLinecap="round" strokeLinejoin="round" />
    <path d="M 67 63 L 59 65 L 62 71" fill="none" stroke={CYAN} strokeWidth="1.2" strokeLinecap="round" strokeLinejoin="round" />
    <path d="M 38 71 L 33 63 L 41 65" fill="none" stroke={CYAN} strokeWidth="1.2" strokeLinecap="round" strokeLinejoin="round" />
    <path d="M 33 37 L 41 35 L 38 29" fill="none" stroke={CYAN} strokeWidth="1.2" strokeLinecap="round" strokeLinejoin="round" />

    {/* 4-cycle vertices */}
    <circle cx="50" cy="20" r="2.6" fill="#ffffff" stroke={CYAN} strokeWidth="1.1" />
    <circle cx="80" cy="50" r="2.6" fill="#ffffff" stroke={CYAN} strokeWidth="1.1" />
    <circle cx="50" cy="80" r="2.6" fill="#ffffff" stroke={CYAN} strokeWidth="1.1" />
    <circle cx="20" cy="50" r="2.6" fill="#ffffff" stroke={CYAN} strokeWidth="1.1" />

    {/* Central propagating photon wave */}
    <path
      d="M 32 50 Q 38 42, 44 50 T 56 50 T 68 50"
      fill="none"
      stroke={AMBER}
      strokeWidth="2"
      strokeLinecap="round"
      className="spectrum-svg-path"
    />
  </svg>
);

// 15. Z Boson (Z) — Neutral Current Mixed 3-Cycle / 4-Cycle Electroweak Bridge (§8.5, §8.7)
export const ZBosonGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />

    {/* Left flavor-preserving fermion ribbon (unchanged top to bottom) */}
    <path d="M 22 14 L 22 86" stroke={CYAN} strokeWidth="2.1" strokeLinecap="round" />
    <path d="M 16 14 L 16 86" stroke={CYAN} strokeWidth="1" strokeDasharray="3 2" opacity="0.55" />

    {/* Right flavor-preserving fermion ribbon (unchanged top to bottom) */}
    <path d="M 78 14 L 78 86" stroke={TEAL} strokeWidth="2.1" strokeLinecap="round" />
    <path d="M 84 14 L 84 86" stroke={TEAL} strokeWidth="1" strokeDasharray="3 2" opacity="0.55" />

    {/* Neutral Z0 mixed electroweak bridge (3-cycle + 4-cycle mixing halo) */}
    <polygon points="50,35 61,54 39,54" fill="rgba(239, 68, 68, 0.08)" stroke={RED} strokeWidth="1.1" opacity="0.7" />
    <rect x="41" y="41" width="18" height="18" fill="none" stroke={CYAN} strokeWidth="0.9" strokeDasharray="2 1.5" opacity="0.55" />

    {/* Wavy neutral Z0 propagator coupling the two vertices without changing flavor */}
    <path
      d="M 22 50 Q 28 43, 34 50 T 46 50 T 58 50 T 70 50 L 78 50"
      fill="none"
      stroke={RED}
      strokeWidth="2"
      strokeLinecap="round"
    />

    {/* Neutral coupling vertices */}
    <circle cx="22" cy="50" r="3" fill="#ffffff" stroke={CYAN} strokeWidth="1.3" />
    <circle cx="78" cy="50" r="3" fill="#ffffff" stroke={TEAL} strokeWidth="1.3" />
    <circle cx="50" cy="50" r="2.2" fill={RED} className="spectrum-node-pulse" />
  </svg>
);

// 16. W Boson (W) — Chiral 3-Cycle SU(2)_L Flavor-Changing Vertex (§8.4, §8.5.5.1)
export const WBosonGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />

    {/* Incoming flavor state (left ribbons in Cyan) */}
    <path d="M 16 26 C 28 26, 36 38, 43 44" stroke={CYAN} strokeWidth="1.7" fill="none" strokeLinecap="round" />
    <path d="M 16 38 C 28 38, 35 45, 41 50" stroke={CYAN} strokeWidth="1.7" fill="none" strokeLinecap="round" />
    <path d="M 16 50 C 28 50, 35 53, 43 56" stroke={PASSIVE} strokeWidth="1.2" strokeDasharray="3 2" fill="none" />

    {/* Outgoing flavor-changed state (right ribbons flipped to Amber/Red) */}
    <path d="M 57 44 C 65 38, 72 26, 84 26" stroke={AMBER} strokeWidth="1.7" fill="none" strokeLinecap="round" />
    <path d="M 59 50 C 67 45, 72 38, 84 38" stroke={AMBER} strokeWidth="1.7" fill="none" strokeLinecap="round" />
    <path d="M 57 56 C 65 53, 72 50, 84 50" stroke={PASSIVE} strokeWidth="1.2" strokeDasharray="3 2" fill="none" />

    {/* Chiral 3-Cycle SU(2)_L Bridge Triangle (§8.5.5.1) */}
    <polygon
      points="50,36 60,55 40,55"
      fill="rgba(255, 176, 31, 0.14)"
      stroke={AMBER}
      strokeWidth="1.8"
      strokeLinejoin="round"
    />
    <circle cx="50" cy="36" r="2.2" fill="#ffffff" stroke={AMBER} strokeWidth="1" />
    <circle cx="60" cy="55" r="2.2" fill="#ffffff" stroke={AMBER} strokeWidth="1" />
    <circle cx="40" cy="55" r="2.2" fill="#ffffff" stroke={AMBER} strokeWidth="1" />

    {/* Departing charged W± boson propagator */}
    <path
      d="M 50 55 Q 45 63, 52 70 Q 57 76, 48 82 Q 45 86, 50 90"
      className="spectrum-svg-path"
      stroke={RED}
      strokeWidth="2"
      fill="none"
      strokeLinecap="round"
    />
    <path d="M 46.5 86.5 L 50 90.5 L 53.5 86.5" fill="none" stroke={RED} strokeWidth="1.3" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

// ============================================================================
// COLUMN 5: VACUUM SUBSTRATE & STRUCTURAL TOPOLOGIES (β₅, β₃, H, ρ*)
// ============================================================================

// 17. Higgs Boson (H) — Modal Mechanism Graphic (3-Cycle Condensate & Topological Drag)
export const HiggsMechanismGraphic = () => (
  <svg viewBox="0 0 200 500" style={{ width: '100%', height: '100%', overflow: 'visible' }}>
    {/* Grid Background points */}
    {[50, 100, 150].map((x) =>
      [50, 150, 250, 350, 450].map((y) => (
        <circle key={`${x}-${y}`} cx={x} cy={y} r="0.5" fill="rgba(255,255,255,0.15)" />
      ))
    )}

    {/* Section 1: Vacuum Lattice (3-cycles) */}
    <line x1="30" y1="70" x2="100" y2="30" stroke="rgba(0, 245, 255, 0.3)" strokeWidth="1.5" />
    <line x1="100" y1="30" x2="100" y2="75" stroke="rgba(0, 245, 255, 0.3)" strokeWidth="1.5" />
    <line x1="100" y1="75" x2="30" y2="70" stroke="rgba(0, 245, 255, 0.3)" strokeWidth="1.5" />
    <line x1="100" y1="30" x2="170" y2="70" stroke="rgba(0, 245, 255, 0.3)" strokeWidth="1.5" />
    <line x1="170" y1="70" x2="100" y2="75" stroke="rgba(0, 245, 255, 0.3)" strokeWidth="1.5" />
    <line x1="30" y1="70" x2="60" y2="115" stroke="rgba(0, 245, 255, 0.3)" strokeWidth="1.5" />
    <line x1="60" y1="115" x2="100" y2="75" stroke="rgba(0, 245, 255, 0.3)" strokeWidth="1.5" />
    <line x1="60" y1="115" x2="140" y2="115" stroke="rgba(0, 245, 255, 0.3)" strokeWidth="1.5" />
    <line x1="140" y1="115" x2="100" y2="75" stroke="rgba(0, 245, 255, 0.3)" strokeWidth="1.5" />
    <line x1="140" y1="115" x2="170" y2="70" stroke="rgba(0, 245, 255, 0.3)" strokeWidth="1.5" />

    <circle cx="30" cy="70" r="3.5" fill="rgba(0, 245, 255, 0.65)" />
    <circle cx="100" cy="30" r="3.5" fill="rgba(0, 245, 255, 0.65)" />
    <circle cx="60" cy="115" r="3.5" fill="rgba(0, 245, 255, 0.65)" />
    <circle cx="140" cy="115" r="3.5" fill="rgba(0, 245, 255, 0.65)" />
    <circle cx="170" cy="70" r="3.5" fill="rgba(0, 245, 255, 0.65)" />
    <circle cx="100" cy="75" r="3.5" fill="rgba(0, 245, 255, 0.65)" />

    <text x="100" y="152" fill="rgba(255,255,255,0.72)" fontSize="11.5" fontFamily="monospace" textAnchor="middle" letterSpacing="0.8">VACUUM SUBSTRATE (ρ₃*)</text>

    {/* Divider 1 */}
    <line x1="15" y1="168" x2="185" y2="168" stroke="rgba(0, 245, 255, 0.18)" strokeWidth="1.5" strokeDasharray="4 4" />

    {/* Section 2: Higgs Density Excitation (Directed 3-Cycle) */}
    <polygon points="50,280 100,190 150,280" fill="none" stroke={AMBER} strokeWidth="4"
      style={{ filter: 'drop-shadow(0 0 8px rgba(245, 158, 11, 0.6))' }} />
    <circle cx="50" cy="280" r="5" fill="#ffffff" stroke={AMBER} strokeWidth="1.5" />
    <circle cx="100" cy="190" r="5" fill="#ffffff" stroke={AMBER} strokeWidth="1.5" />
    <circle cx="150" cy="280" r="5" fill="#ffffff" stroke={AMBER} strokeWidth="1.5" />

    {/* Clockwise circulation arrows */}
    <path d="M 64.90 240.83 L 75.00 235.00 L 75.39 246.66" fill="none" stroke={AMBER} strokeWidth="2" strokeLinecap="round" />
    <path d="M 125.39 223.34 L 125.00 235.00 L 114.90 229.17" fill="none" stroke={AMBER} strokeWidth="2" strokeLinecap="round" />
    <path d="M 110.00 286.00 L 100.00 280.00 L 110.00 274.00" fill="none" stroke={AMBER} strokeWidth="2" strokeLinecap="round" />

    <circle cx="100" cy="250" r="14" fill="rgba(245,158,11,0.15)" stroke={AMBER} strokeWidth="1.5" strokeDasharray="3 3" className="spectrum-node-pulse" />
    <circle cx="100" cy="250" r="6" fill={AMBER} opacity="0.8" />

    <text x="100" y="312" fill={AMBER} fontSize="10.5" fontFamily="monospace" textAnchor="middle" style={{ fontWeight: 'bold' }} letterSpacing="1">3-CYCLE CONDENSATE EXC. (H)</text>

    {/* Divider 2 */}
    <line x1="15" y1="328" x2="185" y2="328" stroke="rgba(0, 245, 255, 0.18)" strokeWidth="1.5" strokeDasharray="4 4" />

    {/* Section 3: Topological Drag / Yukawa Mass with 3D over/under crossings */}
    <path d="M 100 340 C 100 380, 55 400, 55 430 C 55 450, 100 450, 100 480" stroke={AMBER} strokeWidth="2.8" fill="none" strokeDasharray="4 3" />
    <path d="M 50 340 C 50 380, 95 400, 95 430 C 95 450, 50 450, 50 480" stroke={BG} strokeWidth="8.5" fill="none" />
    <path d="M 50 340 C 50 380, 95 400, 95 430 C 95 450, 50 450, 50 480" stroke={CYAN} strokeWidth="3.5" fill="none" />
    <path d="M 150 340 C 150 380, 125 400, 125 430 L 125 480" stroke={CYAN} strokeWidth="3.5" fill="none" />

    <path d="M 40 425 A 60 20 0 0 0 160 425" stroke={AMBER} strokeWidth="2.5" fill="none" opacity="0.4" strokeDasharray="3 3" />
    <path d="M 25 435 A 75 25 0 0 0 175 435" stroke={AMBER} strokeWidth="1.5" fill="none" opacity="0.25" strokeDasharray="4 4" />

    <line x1="180" y1="440" x2="180" y2="395" stroke={CYAN} strokeWidth="2.5" />
    <path d="M 174 402 L 180 395 L 186 402" fill="none" stroke={CYAN} strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
    <text x="180" y="383" fill={CYAN} fontSize="8.5" fontFamily="monospace" textAnchor="middle" style={{ fontWeight: 'bold' }}>DRAG</text>

    <text x="100" y="495" fill="rgba(255,255,255,0.72)" fontSize="11" fontFamily="monospace" textAnchor="middle" letterSpacing="0.4">
      TOPOLOGICAL YUKAWA (m<tspan dy="2" fontSize="8">f</tspan><tspan dy="-2"> = y</tspan><tspan dy="2" fontSize="8">f</tspan><tspan dy="-2"> v)</tspan>
    </text>
  </svg>
);

// 18. Higgs Boson (H) — Card Graphic (Directed 3-Cycle Condensate)
export const HiggsCardGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />
    <polygon points="25,75 50,30 75,75" fill="none" stroke={AMBER} strokeWidth="2.5"
      style={{ filter: 'drop-shadow(0 0 6px rgba(245, 158, 11, 0.6))' }} />
    <circle cx="25" cy="75" r="3" fill="#ffffff" stroke={AMBER} strokeWidth="1" />
    <circle cx="50" cy="30" r="3" fill="#ffffff" stroke={AMBER} strokeWidth="1" />
    <circle cx="75" cy="75" r="3" fill="#ffffff" stroke={AMBER} strokeWidth="1" />
    <path d="M 32.45 55.41 L 37.50 52.50 L 37.69 58.33" fill="none" stroke={AMBER} strokeWidth="1.5" strokeLinecap="round" />
    <path d="M 62.69 46.67 L 62.50 52.50 L 57.45 49.59" fill="none" stroke={AMBER} strokeWidth="1.5" strokeLinecap="round" />
    <path d="M 55.00 78.00 L 50.00 75.00 L 55.00 72.00" fill="none" stroke={AMBER} strokeWidth="1.5" strokeLinecap="round" />
    <circle cx="50" cy="60" r="9" fill="rgba(245,158,11,0.15)" stroke={AMBER} strokeWidth="1" strokeDasharray="2 2" className="spectrum-node-pulse" />
    <circle cx="50" cy="60" r="3.5" fill={AMBER} opacity="0.8" />
  </svg>
);

// 19. Tripartite Braid (β₃) — Prime 3-Strand Weave in QCD RGB Colors (§6.2.1.2)
export const TripartiteBraidGraphic = () => (
  <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
    <BlueprintGrid />

    {/* Blue Strand (Under) */}
    <path
      d="M 50 85 L 50 70 C 50 62, 84 62, 84 54 L 84 15"
      fill="none"
      stroke={BLUE}
      strokeWidth="2.6"
      strokeLinecap="round"
    />

    {/* Green Strand (Middle — crosses over Blue if needed, under Red) */}
    <path
      d="M 16 85 L 16 46 C 16 38, 50 38, 50 30 L 50 15"
      fill="none"
      stroke={GREEN}
      strokeWidth="2.6"
      strokeLinecap="round"
    />

    {/* Eraser halo for Red Strand (Over) */}
    <path
      d="M 84 85 L 84 70 C 84 62, 50 62, 50 54 L 50 46 C 50 38, 16 38, 16 30 L 16 15"
      fill="none"
      stroke={BG}
      strokeWidth="6.5"
      strokeLinecap="round"
    />

    {/* Red Strand (Over — QCD Red) */}
    <path
      d="M 84 85 L 84 70 C 84 62, 50 62, 50 54 L 50 46 C 50 38, 16 38, 16 30 L 16 15"
      fill="none"
      stroke={RED}
      strokeWidth="2.6"
      strokeLinecap="round"
    />
  </svg>
);

// 20. Pentaribbon (β₅) — Unified SU(5) 5-Strand Braid with Active Color–Weak Crossings (§9.2.1.2)
export const PentaribbonSidewaysGraphic = () => {
  // Five strands entering at y = 24, 35, 46 (Color R,G,B) and y = 63, 75 (Weak W1,W2)
  // In the central unified zone, Color R3 (Blue) crosses DOWN into the Weak sector
  // and Weak R4 (Amber) crosses UP into the Color sector (leptoquark cross-sector links!).
  const r1 = 'M 10 24 C 28 24, 34 36, 50 36 C 66 36, 72 24, 90 24';
  const r2 = 'M 10 35 C 26 35, 34 24, 50 24 C 66 24, 74 35, 90 35';
  const r3 = 'M 10 46 C 28 46, 36 65, 50 65 C 64 65, 72 46, 90 46';
  const r4 = 'M 10 63 C 28 63, 36 46, 50 46 C 64 46, 72 63, 90 63';
  const r5 = 'M 10 75 C 28 75, 38 64, 50 75 C 62 84, 74 75, 90 75';

  return (
    <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
      <BlueprintGrid />

      {/* Dashed sector boundary that strands actively cross in the unified SU(5) phase */}
      <line x1="10" y1="55" x2="90" y2="55" stroke="rgba(255,255,255,0.12)" strokeWidth="0.85" strokeDasharray="3 2.5" />
      <text x="12" y="14" fill="rgba(56, 189, 248, 0.55)" fontSize="5.5" fontFamily="monospace" letterSpacing="0.5">COLOR SU(3)</text>
      <text x="12" y="93" fill="rgba(255, 176, 31, 0.55)" fontSize="5.5" fontFamily="monospace" letterSpacing="0.5">WEAK SU(2)</text>

      {/* Layer 1: Under strands */}
      <path d={r2} fill="none" stroke={GREEN} strokeWidth="2.1" strokeLinecap="round" />
      <path d={r5} fill="none" stroke={ORANGE} strokeWidth="2.1" strokeLinecap="round" />
      <path d={r3} fill="none" stroke={BLUE} strokeWidth="2.1" strokeLinecap="round" />

      {/* Layer 2: Over strands with true 3D eraser masks */}
      <path d={r1} fill="none" stroke={BG} strokeWidth="5.2" strokeLinecap="round" />
      <path d={r1} fill="none" stroke={RED} strokeWidth="2.1" strokeLinecap="round" />

      <path d={r4} fill="none" stroke={BG} strokeWidth="5.2" strokeLinecap="round" />
      <path d={r4} fill="none" stroke={AMBER} strokeWidth="2.1" strokeLinecap="round" />

      {/* Cross-sector leptoquark link highlights where R3 & R4 cross the SU(3)/SU(2) boundary */}
      <circle cx="33" cy="55" r="2.2" fill="#ffffff" stroke={AMBER} strokeWidth="0.9" className="spectrum-node-pulse" />
      <circle cx="67" cy="55" r="2.2" fill="#ffffff" stroke={AMBER} strokeWidth="0.9" className="spectrum-node-pulse" />
    </svg>
  );
};

// 21. Vacuum Calibration (ρ*) — True k = 3 Regular Bethe Fragment + 3-Cycle Tunneling Chord (§3.2.1.2, §5.2)
export const VacuumCalibrationGraphic = () => {
  const cx = 50;
  const cy = 50;
  const deg = (a: number) => (a * Math.PI) / 180;

  // Generation 1: 3 symmetric children from root (exact k = 3 regularity at root!)
  const gen1Angles = [-90, 30, 150];
  const r1 = 18;
  const r2 = 33;
  const r3 = 44;

  const gen1 = gen1Angles.map((a) => ({
    angle: a,
    x: cx + r1 * Math.cos(deg(a)),
    y: cy + r1 * Math.sin(deg(a)),
  }));

  // Generation 2: each Gen 1 node branches into 2 children (degree 1 + 2 = 3)
  const gen2 = gen1.flatMap((p) =>
    [-28, 28].map((offset) => {
      const a = p.angle + offset;
      return {
        parent: p,
        angle: a,
        x: cx + r2 * Math.cos(deg(a)),
        y: cy + r2 * Math.sin(deg(a)),
      };
    })
  );

  // Generation 3: each Gen 2 node branches into 2 leaves (12 outer frontier nodes)
  const gen3 = gen2.flatMap((p) =>
    [-13, 13].map((offset) => {
      const a = p.angle + offset;
      return {
        parent: p,
        x: cx + r3 * Math.cos(deg(a)),
        y: cy + r3 * Math.sin(deg(a)),
      };
    })
  );

  // Non-perturbative 2-path closure chord between Gen 1[0] (-90°) and Gen 1[1] (+30°)
  // closing a directed 3-cycle with the root!
  const nA = gen1[0];
  const nB = gen1[1];

  return (
    <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%' }}>
      <BlueprintGrid />

      {/* Generation 2 -> Generation 3 leaf edges */}
      {gen3.map((leaf, i) => (
        <line
          key={`e3-${i}`}
          x1={leaf.parent.x}
          y1={leaf.parent.y}
          x2={leaf.x}
          y2={leaf.y}
          stroke="rgba(0, 245, 255, 0.22)"
          strokeWidth="0.7"
        />
      ))}

      {/* Generation 1 -> Generation 2 edges */}
      {gen2.map((node, i) => (
        <line
          key={`e2-${i}`}
          x1={node.parent.x}
          y1={node.parent.y}
          x2={node.x}
          y2={node.y}
          stroke="rgba(0, 245, 255, 0.4)"
          strokeWidth="1.05"
        />
      ))}

      {/* Root -> Generation 1 edges (3-way k=3 branching) */}
      {gen1.map((node, i) => (
        <line
          key={`e1-${i}`}
          x1={cx}
          y1={cy}
          x2={node.x}
          y2={node.y}
          stroke={i < 2 ? AMBER : 'rgba(0, 245, 255, 0.6)'}
          strokeWidth={i < 2 ? '1.6' : '1.3'}
        />
      ))}

      {/* Nucleated 3-cycle fill & non-perturbative tunneling chord closing Root-nA-nB */}
      <polygon
        points={`${cx},${cy} ${nA.x},${nA.y} ${nB.x},${nB.y}`}
        fill="rgba(255, 176, 31, 0.14)"
      />
      <line
        x1={nA.x}
        y1={nA.y}
        x2={nB.x}
        y2={nB.y}
        stroke={AMBER}
        strokeWidth="1.7"
        strokeDasharray="3 1.8"
      />

      {/* Generation 3 leaves */}
      {gen3.map((leaf, i) => (
        <circle key={`n3-${i}`} cx={leaf.x} cy={leaf.y} r="1.4" fill={BG} stroke={CYAN} strokeWidth="0.75" />
      ))}

      {/* Generation 2 nodes */}
      {gen2.map((node, i) => (
        <circle key={`n2-${i}`} cx={node.x} cy={node.y} r="2.1" fill={BG} stroke={AMBER} strokeWidth="1" />
      ))}

      {/* Generation 1 nodes */}
      {gen1.map((node, i) => (
        <circle
          key={`n1-${i}`}
          cx={node.x}
          cy={node.y}
          r="2.7"
          fill={i < 2 ? AMBER : CYAN}
          stroke="#ffffff"
          strokeWidth="0.6"
        />
      ))}

      {/* Root node (Generation 0, degree k = 3) */}
      <circle cx={cx} cy={cy} r="3.4" fill={AMBER} stroke="#ffffff" strokeWidth="0.8" className="spectrum-node-pulse" />
    </svg>
  );
};

// Central selector helper
export const ParticleGraphic = ({ symbol, isCard = false }: { symbol: string; isCard?: boolean }) => {
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
    case 'H': return isCard ? <HiggsCardGraphic /> : <HiggsMechanismGraphic />;
    case 'β₃': return <TripartiteBraidGraphic />;
    case 'β₅': return <PentaribbonSidewaysGraphic />;
    case 'ρ*': return <VacuumCalibrationGraphic />;
    default: return null;
  }
};

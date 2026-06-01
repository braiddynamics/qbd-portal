import React from 'react';

// Lightcone sandbox
export const LightConeSandbox: React.FC<{
  hoveredNode: number | null;
  setHoveredNode: (val: number | null) => void;
}> = ({ hoveredNode, setHoveredNode }) => (
  <div style={{
    backgroundColor: 'rgba(0, 0, 0, 0.12)',
    border: '1px solid var(--qbd-glow-color)',
    borderRadius: '16px',
    padding: '1.25rem',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center'
  }}>
    <span style={{ display: 'block', alignSelf: 'flex-start', fontSize: '0.75rem', fontWeight: 'bold', color: 'var(--ifm-color-primary)', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '0.6rem' }}>
      Light-Cone Causal Sandbox
    </span>
    <svg width="240" height="130" style={{ border: '1px solid rgba(255,255,255,0.05)', borderRadius: '8px', backgroundColor: 'rgba(0,0,0,0.2)' }}>
      <line x1="40" y1="100" x2="90" y2="65" stroke={hoveredNode === 1 || hoveredNode === 2 ? 'var(--ifm-color-primary)' : 'rgba(255,255,255,0.15)'} strokeWidth={hoveredNode === 1 || hoveredNode === 2 ? '3' : '1.5'} />
      <line x1="140" y1="100" x2="90" y2="65" stroke={hoveredNode === 1 || hoveredNode === 3 ? 'var(--ifm-color-primary)' : 'rgba(255,255,255,0.15)'} strokeWidth={hoveredNode === 1 || hoveredNode === 3 ? '3' : '1.5'} />
      <line x1="200" y1="100" x2="160" y2="65" stroke={hoveredNode === 4 || hoveredNode === 5 ? 'var(--ifm-color-primary)' : 'rgba(255,255,255,0.15)'} strokeWidth={hoveredNode === 4 || hoveredNode === 5 ? '3' : '1.5'} />
      <line x1="90" y1="65" x2="125" y2="30" stroke={hoveredNode === 1 || hoveredNode === 2 || hoveredNode === 3 ? 'var(--qbd-spine-color)' : 'rgba(255,255,255,0.15)'} strokeWidth={hoveredNode === 1 ? '3' : '1.5'} />
      <line x1="160" y1="65" x2="125" y2="30" stroke={hoveredNode === 1 || hoveredNode === 4 || hoveredNode === 5 ? 'var(--qbd-spine-color)' : 'rgba(255,255,255,0.15)'} strokeWidth={hoveredNode === 1 ? '3' : '1.5'} />

      <circle cx="40" cy="100" r="8" 
        fill={hoveredNode === 2 ? 'var(--ifm-color-primary)' : 'rgba(255,255,255,0.3)'} 
        onMouseEnter={() => setHoveredNode(2)} onMouseLeave={() => setHoveredNode(null)} 
        style={{ cursor: 'pointer', transition: 'all 0.2s' }} />
      <circle cx="140" cy="100" r="8" 
        fill={hoveredNode === 3 ? 'var(--ifm-color-primary)' : 'rgba(255,255,255,0.3)'} 
        onMouseEnter={() => setHoveredNode(3)} onMouseLeave={() => setHoveredNode(null)} 
        style={{ cursor: 'pointer', transition: 'all 0.2s' }} />
      <circle cx="200" cy="100" r="8" 
        fill={hoveredNode === 5 ? 'var(--ifm-color-primary)' : 'rgba(255,255,255,0.3)'} 
        onMouseEnter={() => setHoveredNode(5)} onMouseLeave={() => setHoveredNode(null)} 
        style={{ cursor: 'pointer', transition: 'all 0.2s' }} />
      
      <circle cx="90" cy="65" r="10" 
        fill={hoveredNode === 1 ? '#25c2a0' : hoveredNode === 2 || hoveredNode === 3 ? 'var(--ifm-color-primary)' : 'rgba(255,255,255,0.5)'} 
        onMouseEnter={() => setHoveredNode(1)} onMouseLeave={() => setHoveredNode(null)} 
        style={{ cursor: 'pointer', transition: 'all 0.2s' }} />
      <circle cx="160" cy="65" r="10" 
        fill={hoveredNode === 4 ? '#25c2a0' : hoveredNode === 5 ? 'var(--ifm-color-primary)' : 'rgba(255,255,255,0.5)'} 
        onMouseEnter={() => setHoveredNode(4)} onMouseLeave={() => setHoveredNode(null)} 
        style={{ cursor: 'pointer', transition: 'all 0.2s' }} />
      
      <circle cx="125" cy="30" r="12" 
        fill={hoveredNode === 1 || hoveredNode === 2 || hoveredNode === 3 || hoveredNode === 4 || hoveredNode === 5 ? 'var(--qbd-spine-color)' : 'rgba(255,255,255,0.7)'} />
    </svg>
    <span style={{ fontSize: '0.74rem', color: 'var(--ifm-color-emphasis-500)', marginTop: '0.6rem', textAlign: 'center' }}>
      {hoveredNode === null ? "Hover nodes to trace light cones." : "Causal links active."}
    </span>
  </div>
);

// Braid animator
export const BraidAnimator: React.FC<{
  braidType: 'electron' | 'quark' | 'neutrino';
  setBraidType: (val: 'electron' | 'quark' | 'neutrino') => void;
}> = ({ braidType, setBraidType }) => (
  <div style={{
    backgroundColor: 'rgba(0, 0, 0, 0.12)',
    border: '1px solid var(--qbd-glow-color)',
    borderRadius: '16px',
    padding: '1.25rem',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center'
  }}>
    <span style={{ display: 'block', alignSelf: 'flex-start', fontSize: '0.75rem', fontWeight: 'bold', color: 'var(--ifm-color-primary)', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '0.6rem' }}>
      Tripartite Braid Animator
    </span>
    <div style={{ display: 'flex', gap: '0.3rem', marginBottom: '0.8rem' }}>
      <button onClick={() => setBraidType('electron')} className={`button button--xs ${braidType === 'electron' ? 'button--primary' : 'button--secondary'}`} style={{ fontWeight: 'bold', fontSize: '0.7rem' }}>Electron</button>
      <button onClick={() => setBraidType('quark')} className={`button button--xs ${braidType === 'quark' ? 'button--primary' : 'button--secondary'}`} style={{ fontWeight: 'bold', fontSize: '0.7rem' }}>Quark</button>
      <button onClick={() => setBraidType('neutrino')} className={`button button--xs ${braidType === 'neutrino' ? 'button--primary' : 'button--secondary'}`} style={{ fontWeight: 'bold', fontSize: '0.7rem' }}>Neutrino</button>
    </div>
    <svg width="220" height="90" style={{ border: '1px solid rgba(255,255,255,0.05)', borderRadius: '8px', backgroundColor: 'rgba(0,0,0,0.2)' }}>
      {braidType === 'electron' && (
        <g strokeWidth="2.5" fill="none">
          <path d="M 20 15 C 60 15, 80 75, 200 75" stroke="#25c2a0" />
          <path d="M 20 45 C 60 75, 100 15, 200 15" stroke="#8b5cf6" />
          <path d="M 20 75 C 100 45, 120 45, 200 45" stroke="#3b82f6" strokeDasharray="3,3" />
        </g>
      )}
      {braidType === 'quark' && (
        <g strokeWidth="2.5" fill="none">
          <path d="M 20 15 C 80 75, 80 15, 200 45" stroke="#ef4444" />
          <path d="M 20 45 C 45 15, 110 75, 200 75" stroke="#25c2a0" />
          <path d="M 20 75 C 90 15, 60 75, 200 15" stroke="#3b82f6" />
        </g>
      )}
      {braidType === 'neutrino' && (
        <g strokeWidth="2.5" fill="none">
          <path d="M 20 15 L 200 15" stroke="#25c2a0" />
          <path d="M 20 45 L 200 45" stroke="#8b5cf6" />
          <path d="M 20 75 L 200 75" stroke="#3b82f6" />
        </g>
      )}
    </svg>
    <span style={{ fontSize: '0.74rem', fontWeight: 'bold', color: 'var(--ifm-color-primary-light)', marginTop: '0.5rem' }}>
      {braidType === 'electron' && "Writhe: -3, Q: -1, J: 1/2"}
      {braidType === 'quark' && "Writhe: +2/3, Q: +2/3, J: 1/2"}
      {braidType === 'neutrino' && "Writhe: 0, Q: 0, J: 1/2"}
    </span>
  </div>
);

// Curvature warp
export const CurvatureWarp: React.FC<{
  warpStrength: number;
  setWarpStrength: (val: number) => void;
}> = ({ warpStrength, setWarpStrength }) => (
  <div style={{
    backgroundColor: 'rgba(0, 0, 0, 0.12)',
    border: '1px solid var(--qbd-glow-color)',
    borderRadius: '16px',
    padding: '1.25rem',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center'
  }}>
    <span style={{ display: 'block', alignSelf: 'flex-start', fontSize: '0.75rem', fontWeight: 'bold', color: 'var(--ifm-color-primary)', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '0.6rem' }}>
      Relational Gravitational Curvature
    </span>
    <input 
      type="range" 
      min="10" 
      max="90" 
      value={warpStrength} 
      onChange={(e) => setWarpStrength(Number(e.target.value))} 
      style={{ width: '90%', accentColor: 'var(--ifm-color-primary)', marginBottom: '0.8rem' }}
    />
    <svg width="220" height="90" style={{ border: '1px solid rgba(255,255,255,0.05)', borderRadius: '8px', backgroundColor: 'rgba(0,0,0,0.2)' }}>
      <path d={`M 15 15 Q 110 ${15 + warpStrength * 0.3}, 205 15`} stroke="rgba(37, 194, 160, 0.4)" strokeWidth="1.5" fill="none" />
      <path d={`M 15 45 Q 110 ${45 + warpStrength * 0.6}, 205 45`} stroke="rgba(37, 194, 160, 0.8)" strokeWidth="2" fill="none" />
      <path d={`M 15 75 Q 110 ${75 + warpStrength * 0.3}, 205 75`} stroke="rgba(37, 194, 160, 0.4)" strokeWidth="1.5" fill="none" />

      <path d={`M 40 10 Q ${40 + warpStrength * 0.15} 45, 40 80`} stroke="rgba(139, 92, 246, 0.4)" strokeWidth="1.5" fill="none" />
      <path d={`M 110 10 Q ${110} ${45 + warpStrength * 0.75}, 110 80`} stroke="rgba(139, 92, 246, 0.8)" strokeWidth="2" fill="none" />
      <path d={`M 180 10 Q ${180 - warpStrength * 0.15} 45, 180 80`} stroke="rgba(139, 92, 246, 0.4)" strokeWidth="1.5" fill="none" />

      <circle cx="110" cy={45 + warpStrength * 0.4} r={4 + warpStrength * 0.1} fill="var(--ifm-color-primary)" opacity="0.7" />
    </svg>
    <span style={{ fontSize: '0.74rem', fontWeight: 'bold', color: 'var(--ifm-color-primary-light)', marginTop: '0.5rem' }}>
      Gravity Warp metric: G_ab = {((warpStrength / 90) * 8.4).toFixed(3)}
    </span>
  </div>
);

// Cosmic timeline sandbox
export const TimelineSandbox: React.FC<{
  timelineIndex: number;
  setTimelineIndex: (val: number) => void;
  timelineEvents: Array<{
    title: string;
    chapter: number;
    math: string;
    description: string;
    badge: string;
    color: string;
  }>;
}> = ({ timelineIndex, setTimelineIndex, timelineEvents }) => (
  <div style={{
    backgroundColor: 'rgba(0, 0, 0, 0.12)',
    border: '1px solid var(--qbd-glow-color)',
    borderRadius: '16px',
    padding: '1.25rem',
    display: 'flex',
    flexDirection: 'column'
  }}>
    <span style={{ display: 'block', fontSize: '0.75rem', fontWeight: 'bold', color: 'var(--ifm-color-primary)', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '0.6rem' }}>
      Cosmological Timeline
    </span>
    <div style={{ display: 'flex', flexDirection: 'column', gap: '0.3rem', marginBottom: '0.8rem' }}>
      {timelineEvents.slice(0, 3).map((evt, idx) => (
        <button
          key={idx}
          onClick={() => setTimelineIndex(idx)}
          style={{
            backgroundColor: timelineIndex === idx ? 'var(--ifm-color-primary)' : 'rgba(255, 255, 255, 0.02)',
            border: '1px solid rgba(255,255,255,0.1)',
            color: timelineIndex === idx ? '#ffffff' : 'var(--ifm-color-emphasis-700)',
            padding: '0.4rem 0.6rem',
            fontWeight: '700',
            fontSize: '0.75rem',
            borderRadius: '6px',
            cursor: 'pointer',
            transition: 'all 0.15s',
            textAlign: 'left'
          }}
        >
          {evt.title}
        </button>
      ))}
    </div>
    <div style={{
      backgroundColor: 'rgba(0,0,0,0.15)',
      borderRadius: '8px',
      padding: '0.8rem',
      border: '1px solid rgba(255,255,255,0.03)',
      fontSize: '0.8rem',
      lineHeight: '1.4',
      color: 'var(--ifm-color-emphasis-800)'
    }}>
      <strong style={{ color: timelineEvents[timelineIndex].color, fontSize: '0.85rem', display: 'block', marginBottom: '0.3rem' }}>
        Ch. {timelineEvents[timelineIndex].chapter} &bull; {timelineEvents[timelineIndex].badge}
      </strong>
      {timelineEvents[timelineIndex].description}
    </div>
  </div>
);

// Selection sandbox
export const SelectionSandbox: React.FC<{
  selectionStability: number;
  setSelectionStability: (val: number) => void;
}> = ({ selectionStability, setSelectionStability }) => (
  <div style={{
    backgroundColor: 'rgba(0, 0, 0, 0.12)',
    border: '1px solid var(--qbd-glow-color)',
    borderRadius: '16px',
    padding: '1.5rem',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center'
  }}>
    <span style={{ display: 'block', alignSelf: 'flex-start', fontSize: '0.75rem', fontWeight: 'bold', color: 'var(--ifm-color-primary)', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '0.6rem' }}>
      Cosmological Selection Sandbox
    </span>
    <input 
      type="range" 
      min="20" 
      max="99" 
      value={selectionStability} 
      onChange={(e) => setSelectionStability(Number(e.target.value))} 
      style={{ width: '90%', accentColor: 'var(--ifm-color-primary)', marginBottom: '0.8rem' }}
    />
    <svg width="220" height="90" style={{ border: '1px solid rgba(255,255,255,0.05)', borderRadius: '8px', backgroundColor: 'rgba(0,0,0,0.2)' }}>
      <line x1="110" y1="80" x2="110" y2="55" stroke="var(--ifm-color-primary)" strokeWidth="3" />
      <line x1="110" y1="55" x2="60" y2="35" stroke="var(--qbd-spine-color)" strokeWidth="2" />
      <line x1="110" y1="55" x2="160" y2="35" stroke="var(--ifm-color-primary)" strokeWidth="2.5" />
      
      <line x1="60" y1="35" x2="35" y2="15" stroke="rgba(239, 68, 68, 0.5)" strokeWidth={1} strokeDasharray="2,2" />
      <line x1="60" y1="35" x2="85" y2="15" stroke="var(--qbd-spine-color)" strokeWidth="1.5" />
      
      <line x1="160" y1="35" x2="135" y2="15" stroke="var(--ifm-color-primary)" strokeWidth="1.8" />
      <line x1="160" y1="35" x2="185" y2="15" stroke="var(--ifm-color-primary)" strokeWidth={selectionStability > 60 ? "2.2" : "1"} />

      <circle cx="110" cy="80" r="4" fill="var(--ifm-color-primary)" />
      <circle cx="110" cy="55" r="4" fill="var(--ifm-color-primary)" />
      <circle cx="60" cy="35" r="4" fill="var(--qbd-spine-color)" />
      <circle cx="160" cy="35" r="4" fill="var(--ifm-color-primary)" />
      
      <circle cx="35" cy="15" r="3" fill="#ef4444" />
      <circle cx="85" cy="15" r="3" fill="var(--qbd-spine-color)" />
      <circle cx="135" cy="15" r="3" fill="var(--ifm-color-primary)" />
      <circle cx="185" cy="15" r={selectionStability > 60 ? "4" : "2"} fill="var(--ifm-color-primary-light)" />
    </svg>
    <span style={{ fontSize: '0.74rem', fontWeight: 'bold', color: 'var(--ifm-color-primary-light)', marginTop: '0.5rem' }}>
      Survival Probability: {selectionStability}% &bull; {selectionStability > 60 ? "Code Stable" : "Code Decaying"}
    </span>
  </div>
);

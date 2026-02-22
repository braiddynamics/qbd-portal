import React from 'react';
import './appendix-graphic.css';

export default function AppendixGraphic() {
  const primaryColor = 'var(--ifm-color-primary)';
  const secondaryColor = 'var(--ifm-color-emphasis-400)';
  const textColor = 'var(--ifm-color-emphasis-700)';

  return (
    <div style={{ width: '100%', height: '100%', display: 'flex', justifyContent: 'center', alignItems: 'center', padding: '1rem' }}>
      <svg viewBox="0 0 200 200" style={{ width: '100%', maxWidth: '160px', height: 'auto', overflow: 'visible' }}>
        
        {/* Background Cipher Rings */}
        <circle cx="100" cy="100" r="45" fill="none" stroke={secondaryColor} strokeWidth="1" opacity="0.2" />
        <circle cx="100" cy="100" r="35" fill="none" stroke={primaryColor} strokeWidth="1.5" strokeDasharray="4 8" className="appendix-ring" opacity="0" />

        {/* The Geometric Reference Hub (Replaces the Gamma) */}
        <g className="appendix-hub">
          {/* 3 intersecting lines forming a 6-point asterisk / tensor node */}
          <line x1="100" y1="85" x2="100" y2="115" stroke={primaryColor} strokeWidth="3" strokeLinecap="round" />
          <line x1="87" y1="92.5" x2="113" y2="107.5" stroke={primaryColor} strokeWidth="3" strokeLinecap="round" />
          <line x1="87" y1="107.5" x2="113" y2="92.5" stroke={primaryColor} strokeWidth="3" strokeLinecap="round" />
          {/* Core Hollow Node */}
          <circle cx="100" cy="100" r="4" fill="var(--ifm-background-surface-color)" stroke={primaryColor} strokeWidth="2" />
        </g>

        {/* Left Mechanism (Bracket + Nodes + Construction Line) */}
        <g className="appendix-bracket bracket-left">
          <path d="M 65 45 L 35 100 L 65 155" fill="none" stroke={textColor} strokeWidth="4" strokeLinecap="round" strokeLinejoin="round" />
          <circle cx="35" cy="100" r="3" fill={primaryColor} opacity="0.5" className="bracket-node" />
          <line x1="35" y1="100" x2="70" y2="100" stroke={secondaryColor} strokeWidth="1" strokeDasharray="2 2" opacity="0.4" />
        </g>
        
        {/* Right Mechanism (Bracket + Nodes + Construction Line) */}
        <g className="appendix-bracket bracket-right">
          <path d="M 135 45 L 165 100 L 135 155" fill="none" stroke={textColor} strokeWidth="4" strokeLinecap="round" strokeLinejoin="round" />
          <circle cx="165" cy="100" r="3" fill={primaryColor} opacity="0.5" className="bracket-node" />
          <line x1="165" y1="100" x2="130" y2="100" stroke={secondaryColor} strokeWidth="1" strokeDasharray="2 2" opacity="0.4" />
        </g>
      </svg>
    </div>
  );
}
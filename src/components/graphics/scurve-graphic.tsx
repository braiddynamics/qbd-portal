import React from 'react';
import './scurve-graphic.css';

export default function SCurveGraphic() {
  const primaryColor = 'var(--ifm-color-primary)';
  const axisColor = 'var(--ifm-color-emphasis-400)';
  const asymptoteColor = 'var(--ifm-color-emphasis-500)';

  return (
    <div style={{ width: '100%', height: '100%', display: 'flex', justifyContent: 'center', alignItems: 'center', padding: '1rem' }}>
      <svg viewBox="0 0 200 200" style={{ width: '100%', maxWidth: '180px', height: 'auto', overflow: 'visible' }}>
        
        {/* The X and Y Axes */}
        <polyline points="20,20 20,180 180,180" fill="none" stroke={axisColor} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
        
        {/* The Asymptote (Friction Equilibrium) */}
        <line x1="20" y1="50" x2="180" y2="50" fill="none" stroke={asymptoteColor} strokeWidth="2" strokeDasharray="6 6" className="scurve-asymptote" />
        
        {/* The Logistic S-Curve (Inflation to Saturation) */}
        <path d="M 20 178 C 90 178, 90 52, 180 52" fill="none" stroke={primaryColor} strokeWidth="4" strokeLinecap="round" className="scurve-line" />
        
        {/* A subtle gradient fill that appears under the curve */}
        <path d="M 20 178 C 90 178, 90 52, 180 52 L 180 180 L 20 180 Z" fill={primaryColor} className="scurve-fill" />

        {/* The "Current State" marker node */}
        <circle cx="180" cy="52" r="6" fill={primaryColor} className="scurve-node" />
      </svg>
    </div>
  );
}
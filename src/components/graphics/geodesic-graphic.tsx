import React from 'react';
import './geodesic-graphic.css';

export default function GeodesicGraphic() {
  const primaryColor = 'var(--ifm-color-primary)';
  const secondaryColor = 'var(--ifm-color-emphasis-400)';
  const massColor = 'var(--ifm-color-emphasis-800)';

  return (
    <div style={{ width: '100%', height: '100%', display: 'flex', justifyContent: 'center', alignItems: 'center', padding: '1rem' }}>
      <svg viewBox="0 0 200 200" style={{ width: '100%', maxWidth: '180px', height: 'auto', overflow: 'visible' }}>
        <defs>
           {/* Cartesian Grid to represent the background network */}
           <pattern id="cartesian-grid" width="20" height="20" patternUnits="userSpaceOnUse">
             <path d="M 20 0 L 0 0 0 20" fill="none" stroke="var(--ifm-color-emphasis-200)" strokeWidth="0.5" />
           </pattern>
        </defs>

        {/* Background Grid */}
        <rect x="0" y="0" width="200" height="200" fill="url(#cartesian-grid)" opacity="0.6" />

        {/* --- The Massive Object & Density Rings --- */}
        <g className="geo-mass-group">
          {/* Concentric rings representing computational density/gravity well */}
          <circle cx="100" cy="160" r="60" fill="none" stroke={massColor} strokeWidth="1" opacity="0.15" className="geo-ring ring-2" />
          <circle cx="100" cy="160" r="40" fill="none" stroke={massColor} strokeWidth="1" opacity="0.3" className="geo-ring ring-1" />
          {/* The Mass itself */}
          <circle cx="100" cy="160" r="22" fill={massColor} className="geo-mass" />
        </g>

        {/* --- The Trajectories --- */}
        
        {/* 1. Low Proper Time (The "Straight" Euclidean Path) */}
        <line x1="30" y1="60" x2="170" y2="60" stroke={secondaryColor} strokeWidth="2" strokeDasharray="4 4" className="geo-straight" />

        {/* 2. Maximum Computational Throughput (The Geodesic Path) */}
        {/* Uses a Quadratic Bezier Curve (Q) to dip down toward the mass */}
        <path d="M 30 60 Q 100 180 170 60" fill="none" stroke={primaryColor} strokeWidth="2.5" className="geo-curved" />
        
        {/* The animating particle tracing the Geodesic */}
        <path d="M 30 60 Q 100 180 170 60" fill="none" stroke="#ffffff" strokeWidth="3" className="geo-packet" />

        {/* Point A and Point B Nodes */}
        <circle cx="30" cy="60" r="5" fill={primaryColor} />
        <circle cx="170" cy="60" r="5" fill={primaryColor} />
      </svg>
    </div>
  );
}
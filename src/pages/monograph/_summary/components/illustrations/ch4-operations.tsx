import React from 'react';

const Ch4_Operations: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Local neighborhood circle */}
            <circle cx="130" cy="90" r="40" fill="rgba(37,194,160,0.06)" stroke="var(--ifm-color-primary)" strokeWidth="1.5" strokeDasharray="3,3" />
            <text x="130" y="42" fill="var(--ifm-color-primary)" fontSize="8" fontWeight="bold" textAnchor="middle">Comonadic Neighborhood Filter</text>

            {/* Mesh Graph */}
            <line x1="80" y1="90" x2="130" y2="90" stroke="rgba(255,255,255,0.2)" strokeWidth="1.5" />
            <line x1="130" y1="90" x2="180" y2="90" stroke="rgba(255,255,255,0.2)" strokeWidth="1.5" />
            <line x1="130" y1="90" x2="130" y2="140" stroke="rgba(255,255,255,0.2)" strokeWidth="1.5" />
            
            {/* New rewritten edge */}
            <path d="M 80,90 Q 130,130 180,90" fill="none" stroke="var(--qbd-spine-color)" strokeWidth="2.5" />

            {/* Nodes */}
            <circle cx="130" cy="90" r="7" fill="var(--ifm-color-primary)" />
            <circle cx="80" cy="90" r="5" fill="#ffffff" />
            <circle cx="180" cy="90" r="5" fill="#ffffff" />
            <circle cx="130" cy="140" r="5" fill="#ffffff" />

            {/* Text markers */}
            <text x="130" y="80" fill="var(--ifm-color-primary)" fontSize="8" textAnchor="middle">Active Focus</text>
            <text x="130" y="125" fill="var(--qbd-spine-color)" fontSize="9" fontWeight="bold" textAnchor="middle">New Causal Link Added</text>
            <text x="250" y="90" fill="rgba(255,255,255,0.5)" fontSize="9" textAnchor="start">
              <tspan x="220" dy="0" fontWeight="bold">Action Rule:</tspan>
              <tspan x="220" dy="12">If unique 2-path exists</tspan>
              <tspan x="220" dy="12">within neighborhood,</tspan>
              <tspan x="220" dy="12">bridge to close triangle.</tspan>
            </text>
          </svg>
  );
};

export default Ch4_Operations;

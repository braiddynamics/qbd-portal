import React from 'react';

const Ch3_ObjectModel: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Hierarchical tree structure */}
            <g transform="translate(170, 20)">
              {/* Level 0 -> Level 1 */}
              <line x1="0" y1="0" x2="-80" y2="45" stroke="var(--ifm-color-primary)" strokeWidth="2" />
              <line x1="0" y1="0" x2="80" y2="45" stroke="var(--ifm-color-primary)" strokeWidth="2" />
              
              {/* Level 1 -> Level 2 */}
              <line x1="-80" y1="45" x2="-120" y2="95" stroke="var(--qbd-spine-color)" strokeWidth="1.5" />
              <line x1="-80" y1="45" x2="-40" y2="95" stroke="var(--qbd-spine-color)" strokeWidth="1.5" />
              <line x1="80" y1="45" x2="40" y2="95" stroke="var(--qbd-spine-color)" strokeWidth="1.5" />
              <line x1="80" y1="45" x2="120" y2="95" stroke="var(--qbd-spine-color)" strokeWidth="1.5" />

              {/* Event Nodes */}
              <circle cx="0" cy="0" r="7" fill="var(--ifm-color-primary)" />
              <circle cx="-80" cy="45" r="5.5" fill="#3b82f6" />
              <circle cx="80" cy="45" r="5.5" fill="#3b82f6" />
              <circle cx="-120" cy="95" r="4.5" fill="var(--qbd-spine-color)" />
              <circle cx="-40" cy="95" r="4.5" fill="var(--qbd-spine-color)" />
              <circle cx="40" cy="95" r="4.5" fill="var(--qbd-spine-color)" />
              <circle cx="120" cy="95" r="4.5" fill="var(--qbd-spine-color)" />

              {/* Explanatory labels */}
              <text x="0" y="-8" fill="#ffffff" fontSize="9" fontWeight="bold" textAnchor="middle">Root (t_L = 0)</text>
              <text x="-95" y="47" fill="#3b82f6" fontSize="8" textAnchor="end">Even Layer</text>
              <text x="95" y="47" fill="#3b82f6" fontSize="8" textAnchor="start">Even Layer</text>
              <text x="0" y="115" fill="rgba(255,255,255,0.4)" fontSize="9" textAnchor="middle">Strictly Bipartite Causal Tree</text>
              <text x="0" y="130" fill="var(--ifm-color-primary-light)" fontSize="8" textAnchor="middle">Zero Accidental Geometry</text>
            </g>
          </svg>
  );
};

export default Ch3_ObjectModel;

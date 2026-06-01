import React from 'react';

const Ch22_SingularitiesGraphCondensates: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Graph condensate singularity cutoff */}
            <g transform="translate(170, 85)">
              <circle cx="0" cy="0" r="30" fill="rgba(37,194,160,0.1)" stroke="var(--ifm-color-primary)" strokeWidth="2" />
              
              {/* Ultra dense, complete graph connections inside */}
              <line x1="-15" y1="-15" x2="15" y2="15" stroke="#ffffff" strokeWidth="1" />
              <line x1="-15" y1="15" x2="15" y2="-15" stroke="#ffffff" strokeWidth="1" />
              <line x1="-20" y1="0" x2="20" y2="0" stroke="#ffffff" strokeWidth="1" />
              <line x1="0" y1="-20" x2="0" y2="20" stroke="#ffffff" strokeWidth="1" />
              
              <circle cx="-15" cy="-15" r="3" fill="#ffffff" />
              <circle cx="15" cy="15" r="3" fill="#ffffff" />
              <circle cx="-15" cy="15" r="3" fill="#ffffff" />
              <circle cx="15" cy="-15" r="3" fill="#ffffff" />
              <circle cx="0" cy="0" r="3.5" fill="var(--qbd-spine-color)" />

              <text x="0" y="-38" fill="var(--ifm-color-primary)" fontSize="9.5" fontWeight="bold" textAnchor="middle">Maximum Density Condensate</text>
              <text x="0" y="45" fill="var(--ifm-color-primary-light)" fontSize="9" fontWeight="bold" textAnchor="middle">Singularity Cutoff Bounded</text>
              
              <text x="0" y="65" fill="rgba(255,255,255,0.4)" fontSize="8.5" textAnchor="middle">
                Lattice density limits prevent infinite collapse and resolve singularities.
              </text>
            </g>
          </svg>
  );
};

export default Ch22_SingularitiesGraphCondensates;

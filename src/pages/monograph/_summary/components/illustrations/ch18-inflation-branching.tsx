import React from 'react';

const Ch18_InflationBranching: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Exponentially branching poset lines representing rapid inflation */}
            <g transform="translate(40, 90)">
              <line x1="0" y1="0" x2="50" y2="-20" stroke="var(--ifm-color-primary)" strokeWidth="2.5" />
              <line x1="0" y1="0" x2="50" y2="20" stroke="var(--ifm-color-primary)" strokeWidth="2.5" />
              
              {/* Gen 2 */}
              <line x1="50" y1="-20" x2="120" y2="-40" stroke="#3b82f6" strokeWidth="2" />
              <line x1="50" y1="-20" x2="120" y2="-10" stroke="#3b82f6" strokeWidth="2" />
              <line x1="50" y1="20" x2="120" y2="5" stroke="#3b82f6" strokeWidth="2" />
              <line x1="50" y1="20" x2="120" y2="35" stroke="#3b82f6" strokeWidth="2" />

              {/* Gen 3 */}
              <line x1="120" y1="-40" x2="200" y2="-65" stroke="var(--qbd-spine-color)" strokeWidth="1.5" />
              <line x1="120" y1="-40" x2="200" y2="-45" stroke="var(--qbd-spine-color)" strokeWidth="1.5" />
              <line x1="120" y1="-10" x2="200" y2="-20" stroke="var(--qbd-spine-color)" strokeWidth="1.5" />
              <line x1="120" y1="-10" x2="200" y2="-2" stroke="var(--qbd-spine-color)" strokeWidth="1.5" />
              <line x1="120" y1="5" x2="200" y2="12" stroke="var(--qbd-spine-color)" strokeWidth="1.5" />
              <line x1="120" y1="35" x2="200" y2="55" stroke="var(--qbd-spine-color)" strokeWidth="1.5" />

              <circle cx="0" cy="0" r="5" fill="#ffffff" />
              <circle cx="50" cy="-20" r="4.5" fill="#ffffff" />
              <circle cx="50" cy="20" r="4.5" fill="#ffffff" />
              <circle cx="120" cy="-40" r="4" fill="#ffffff" />
              <circle cx="120" cy="-10" r="4" fill="#ffffff" />

              <text x="0" y="-12" fill="var(--ifm-color-primary)" fontSize="9" fontWeight="bold">Big Kindling</text>
              <text x="120" y="-72" fill="var(--qbd-spine-color)" fontSize="9" fontWeight="bold">Autocatalytic Inflation</text>
              <text x="120" y="72" fill="rgba(255,255,255,0.4)" fontSize="8.5" textAnchor="middle">
                poset branching feedback drives rapid spatial creation.
              </text>
            </g>
          </svg>
  );
};

export default Ch18_InflationBranching;

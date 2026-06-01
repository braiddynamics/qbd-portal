import React from 'react';

const Ch19_PrimordialCooling: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Primordial matter nucleation */}
            <g transform="translate(170, 90)">
              {/* Heavy primordial foam ring */}
              <circle cx="0" cy="0" r="50" fill="none" stroke="rgba(239, 68, 68, 0.15)" strokeWidth="8" />
              <circle cx="0" cy="0" r="50" stroke="var(--ifm-color-primary)" strokeWidth="1" strokeDasharray="3,3" fill="none" />
              <text x="0" y="5" fill="var(--ifm-color-primary)" fontSize="10" fontWeight="bold" textAnchor="middle">Decelerating Foam</text>

              {/* Emergent nucleated particles inside */}
              <circle cx="-25" cy="-20" r="6" fill="var(--qbd-spine-color)" />
              <path d="M -28,-20 Q -25,-25 -22,-20" fill="none" stroke="#ffffff" strokeWidth="1" />
              <text x="-25" y="-6" fill="var(--qbd-spine-color)" fontSize="7.5" textAnchor="middle">Proton Braid</text>

              <circle cx="25" cy="20" r="6" fill="#3b82f6" />
              <path d="M 22,20 Q 25,15 28,20" fill="none" stroke="#ffffff" strokeWidth="1" />
              <text x="25" y="34" fill="#3b82f6" fontSize="7.5" textAnchor="middle">Neutron Braid</text>
              
              <text x="0" y="-70" fill="var(--ifm-color-primary-light)" fontSize="9" fontWeight="bold" textAnchor="middle">primordial Particle Nucleation</text>
              <text x="0" y="75" fill="rgba(255,255,255,0.4)" fontSize="8.5" textAnchor="middle">
                cooling network lets energy settle into stable tripartite knots.
              </text>
            </g>
          </svg>
  );
};

export default Ch19_PrimordialCooling;

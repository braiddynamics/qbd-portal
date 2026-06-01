import React from 'react';

const Ch25_NaturalSelectionAttractors: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Attractor orbit compile space */}
            <g transform="translate(170, 90)">
              {/* Attractor focal point */}
              <circle cx="0" cy="0" r="6" fill="var(--ifm-color-primary)" />
              <text x="0" y="-12" fill="var(--ifm-color-primary)" fontSize="9" fontWeight="bold" textAnchor="middle">stable Attraction phase</text>

              {/* Orbiting spiral lines (Attractor) */}
              <path d="M 0,0 C 20,-20 40,0 30,30 C 10,50 -30,30 -20,-10 C -10,-40 30,-30 40,10" fill="none" stroke="var(--qbd-spine-color)" strokeWidth="2.5" />
              <path d="M 0,0 C -20,20 -40,0 -30,-30 C -10,-50 30,-30 20,10 C 10,40 -30,30 -40,-10" fill="none" stroke="var(--ifm-color-primary-light)" strokeWidth="1.5" strokeDasharray="3,3" />

              {/* Orbiting nodes */}
              <circle cx="30" cy="30" r="3" fill="#ffffff" />
              <circle cx="-20" cy="-10" r="3" fill="#ffffff" />
              
              <text x="0" y="65" fill="var(--ifm-color-primary-light)" fontSize="9.5" fontWeight="bold" textAnchor="middle">Cosmological Natural Selection</text>
              <text x="0" y="80" fill="rgba(255,255,255,0.4)" fontSize="8.5" textAnchor="middle">
                Networks select for stable error-correcting codes, yielding general relativity.
              </text>
            </g>
          </svg>
  );
};

export default Ch25_NaturalSelectionAttractors;

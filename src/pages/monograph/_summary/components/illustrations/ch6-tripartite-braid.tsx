import React from 'react';

const Ch6_TripartiteBraid: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* 3-Strand Braid Graphic */}
            <g transform="translate(50, 40)">
              {/* Ribbon 1 */}
              <path d="M 10,20 C 60,60 60,-20 110,20 C 160,60 160,-20 210,20" fill="none" stroke="var(--ifm-color-primary)" strokeWidth="3" />
              {/* Ribbon 2 */}
              <path d="M 10,40 C 60,0 60,80 110,40 C 160,0 160,80 210,40" fill="none" stroke="var(--qbd-spine-color)" strokeWidth="2.5" />
              {/* Ribbon 3 */}
              <path d="M 10,60 C 60,100 60,20 110,60 C 160,100 160,20 210,60" fill="none" stroke="var(--ifm-color-primary-light)" strokeWidth="2" strokeDasharray="3,3" />
              
              {/* Nodes at vertices */}
              <circle cx="60" cy="30" r="4.5" fill="#ffffff" />
              <circle cx="110" cy="40" r="4.5" fill="#ffffff" />
              <circle cx="160" cy="30" r="4.5" fill="#ffffff" />

              {/* Explanatory Annotations */}
              <text x="110" y="-12" fill="#ffffff" fontSize="10" fontWeight="bold" textAnchor="middle">The Tripartite Fermion Braid</text>
              <text x="110" y="90" fill="rgba(255,255,255,0.5)" fontSize="8.5" textAnchor="middle">
                Localized twisting of 3 network strands represents particle mass and properties
              </text>
            </g>
          </svg>
  );
};

export default Ch6_TripartiteBraid;

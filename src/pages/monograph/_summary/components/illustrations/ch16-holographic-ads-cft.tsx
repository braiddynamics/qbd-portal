import React from 'react';

const Ch16_HolographicADSCFT: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Holographic bulk circle boundary */}
            <circle cx="170" cy="90" r="60" fill="none" stroke="var(--ifm-color-primary)" strokeWidth="2.5" />
            <text x="170" y="22" fill="var(--ifm-color-primary)" fontSize="9" fontWeight="bold" textAnchor="middle">Boundary Code (n-1 Dimension)</text>

            {/* Bulk events */}
            <circle cx="170" cy="90" r="5" fill="var(--qbd-spine-color)" />
            <circle cx="140" cy="75" r="4" fill="#ffffff" />
            <circle cx="200" cy="105" r="4" fill="#ffffff" />
            <circle cx="150" cy="110" r="4" fill="#ffffff" />
            <circle cx="190" cy="70" r="4" fill="#ffffff" />

            {/* Projection rays */}
            <line x1="170" y1="90" x2="110" y2="90" stroke="rgba(255,255,255,0.15)" strokeWidth="1" strokeDasharray="2,2" />
            <line x1="170" y1="90" x2="230" y2="90" stroke="rgba(255,255,255,0.15)" strokeWidth="1" strokeDasharray="2,2" />
            <line x1="170" y1="90" x2="170" y2="30" stroke="rgba(255,255,255,0.15)" strokeWidth="1" strokeDasharray="2,2" />
            <line x1="170" y1="90" x2="170" y2="150" stroke="rgba(255,255,255,0.15)" strokeWidth="1" strokeDasharray="2,2" />

            <text x="170" y="82" fill="var(--qbd-spine-color)" fontSize="8.5" fontWeight="bold" textAnchor="middle">Bulk Gravity (nD)</text>
            <text x="170" y="163" fill="rgba(255,255,255,0.5)" fontSize="8.5" textAnchor="middle">
              Bulk poset gravity is strictly isomorphic to boundary error-correcting codes.
            </text>
          </svg>
  );
};

export default Ch16_HolographicADSCFT;

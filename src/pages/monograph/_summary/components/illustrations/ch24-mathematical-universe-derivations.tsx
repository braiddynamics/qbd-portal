import React from 'react';

const Ch24_MathematicalUniverseDerivations: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Pure adjacency matrix deriving constants */}
            <g transform="translate(40, 30)">
              {/* Matrix brackets */}
              <path d="M 15,10 L 5,10 L 5,90 L 15,90" fill="none" stroke="#ffffff" strokeWidth="2" />
              <path d="M 85,10 L 95,10 L 95,90 L 85,90" fill="none" stroke="#ffffff" strokeWidth="2" />
              
              {/* Matrix values */}
              <text x="25" y="30" fill="var(--ifm-color-primary)" fontSize="10" fontWeight="bold">1</text>
              <text x="50" y="30" fill="var(--ifm-color-primary)" fontSize="10" fontWeight="bold">0</text>
              <text x="75" y="30" fill="var(--ifm-color-primary)" fontSize="10" fontWeight="bold">1</text>
              
              <text x="25" y="55" fill="var(--ifm-color-primary)" fontSize="10" fontWeight="bold">0</text>
              <text x="50" y="55" fill="var(--ifm-color-primary)" fontSize="10" fontWeight="bold">1</text>
              <text x="75" y="55" fill="var(--ifm-color-primary)" fontSize="10" fontWeight="bold">1</text>
              
              <text x="25" y="80" fill="var(--ifm-color-primary)" fontSize="10" fontWeight="bold">1</text>
              <text x="50" y="80" fill="var(--ifm-color-primary)" fontSize="10" fontWeight="bold">1</text>
              <text x="75" y="80" fill="var(--ifm-color-primary)" fontSize="10" fontWeight="bold">0</text>

              <text x="50" y="110" fill="rgba(255,255,255,0.4)" fontSize="8.5" textAnchor="middle">Adjacency coefficients</text>
            </g>

            {/* Derived constant */}
            <g transform="translate(180, 45)">
              <rect x="0" y="0" width="130" height="70" fill="rgba(255,255,255,0.01)" stroke="rgba(255,255,255,0.06)" strokeWidth="1" rx="6" />
              <text x="65" y="20" fill="var(--ifm-color-primary-light)" fontSize="9" fontWeight="bold" textAnchor="middle">Fine Structure constant</text>
              <line x1="15" y1="28" x2="115" y2="28" stroke="rgba(255,255,255,0.08)" strokeWidth="1" />
              
              <text x="65" y="48" fill="#ffffff" fontSize="13" fontWeight="bold" textAnchor="middle">α⁻¹ ≈ 137.036</text>
              <text x="65" y="62" fill="rgba(255,255,255,0.4)" fontSize="8" textAnchor="middle">derived from braid writhe</text>
            </g>
            
            <text x="170" y="157" fill="rgba(255,255,255,0.5)" fontSize="8.5" textAnchor="middle">
              Physical constants emerge analytically from discrete graph matrices.
            </text>
          </svg>
  );
};

export default Ch24_MathematicalUniverseDerivations;

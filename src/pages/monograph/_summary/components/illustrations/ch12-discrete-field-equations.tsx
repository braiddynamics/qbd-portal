import React from 'react';

const Ch12_DiscreteFieldEquations: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Warped mesh representing curved gravity */}
            <path d="M 20,90 Q 170,150 320,90" fill="none" stroke="var(--ifm-color-primary)" strokeWidth="2.5" />
            <path d="M 20,40 Q 170,120 320,40" fill="none" stroke="rgba(255,255,255,0.1)" strokeWidth="1" />
            <path d="M 20,140 Q 170,160 320,140" fill="none" stroke="rgba(255,255,255,0.1)" strokeWidth="1" />

            {/* Vertical grid lines warped */}
            <line x1="50" y1="40" x2="50" y2="140" stroke="rgba(255,255,255,0.1)" strokeWidth="1" />
            <path d="M 110,30 Q 140,90 110,150" fill="none" stroke="var(--qbd-spine-color)" strokeWidth="1.5" strokeDasharray="3,3" />
            <path d="M 230,30 Q 200,90 230,150" fill="none" stroke="var(--qbd-spine-color)" strokeWidth="1.5" strokeDasharray="3,3" />
            <line x1="290" y1="40" x2="290" y2="140" stroke="rgba(255,255,255,0.1)" strokeWidth="1" />

            {/* Heavy defect causing gravity warp */}
            <circle cx="170" cy="115" r="10" fill="var(--ifm-color-primary)" />
            <circle cx="170" cy="115" r="18" fill="none" stroke="var(--ifm-color-primary-light)" strokeWidth="1" strokeDasharray="3,3" />

            {/* Labeled terms */}
            <text x="170" y="85" fill="var(--ifm-color-primary-light)" fontSize="9" fontWeight="bold" textAnchor="middle">Matter Defect Density</text>
            <text x="245" y="60" fill="#ffffff" fontSize="9" textAnchor="start">Emergent Gravity Warp</text>
            <text x="170" y="167" fill="rgba(255,255,255,0.5)" fontSize="9" textAnchor="middle">
              Gravity emerges macroscopically from network update erasure balances.
            </text>
          </svg>
  );
};

export default Ch12_DiscreteFieldEquations;

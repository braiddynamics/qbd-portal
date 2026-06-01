import React from 'react';

const Ch23_HolographicPartitionFunction: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Ads/CFT boundary partition projection */}
            <g transform="translate(170, 90)">
              {/* Boundary ring */}
              <circle cx="0" cy="0" r="55" fill="none" stroke="var(--ifm-color-primary)" strokeWidth="2.5" />
              <text x="0" y="-62" fill="var(--ifm-color-primary)" fontSize="9" fontWeight="bold" textAnchor="middle">Boundary Code state Z_boundary</text>
              
              {/* Bulk grid interior */}
              <line x1="-55" y1="0" x2="55" y2="0" stroke="rgba(255,255,255,0.06)" strokeWidth="1" />
              <line x1="0" y1="-55" x2="0" y2="55" stroke="rgba(255,255,255,0.06)" strokeWidth="1" />
              
              {/* Entangled projection rays */}
              <path d="M -38,-38 Q 0,0 38,38" fill="none" stroke="var(--qbd-spine-color)" strokeWidth="1.5" strokeDasharray="2,2" />
              <path d="M -38,38 Q 0,0 38,-38" fill="none" stroke="var(--qbd-spine-color)" strokeWidth="1.5" strokeDasharray="2,2" />
              
              <circle cx="0" cy="0" r="5" fill="#ffffff" />
              <text x="0" y="14" fill="#ffffff" fontSize="9" textAnchor="middle">Bulk Z_bulk</text>
              <text x="0" y="26" fill="var(--ifm-color-primary-light)" fontSize="10" fontWeight="bold" textAnchor="middle">Z_bulk ≡ Z_boundary</text>
              
              <text x="0" y="78" fill="rgba(255,255,255,0.4)" fontSize="8.5" textAnchor="middle">
                Thermodynamic partition functions are isomorphic across dimensions.
              </text>
            </g>
          </svg>
  );
};

export default Ch23_HolographicPartitionFunction;

import React from 'react';

const Ch7_QuantumNumbers: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Circular braid loop illustrating writhe */}
            <circle cx="170" cy="90" r="45" fill="none" stroke="var(--ifm-color-primary)" strokeWidth="3" />
            
            {/* Helical twists overlay */}
            <path d="M 125,90 C 125,75 140,65 170,65 C 200,65 215,75 215,90" fill="none" stroke="var(--qbd-spine-color)" strokeWidth="2" />
            <path d="M 125,90 C 125,105 140,115 170,115 C 200,115 215,105 215,90" fill="none" stroke="var(--ifm-color-primary-light)" strokeWidth="1.5" strokeDasharray="2,2" />

            {/* Crossing points */}
            <circle cx="125" cy="90" r="4" fill="#ffffff" />
            <circle cx="215" cy="90" r="4" fill="#ffffff" />

            {/* Vectors and labels */}
            <line x1="170" y1="40" x2="170" y2="10" stroke="var(--ifm-color-primary-light)" strokeWidth="2" markerEnd="url(#arrow)" />
            <text x="170" y="32" fill="var(--ifm-color-primary-light)" fontSize="9" textAnchor="start">Spin Vector (J=1/2)</text>
            
            {/* Formulas */}
            <text x="170" y="87" fill="#ffffff" fontSize="10" fontWeight="bold" textAnchor="middle">Writhe (w) = Charge (Q)</text>
            <text x="170" y="99" fill="rgba(255,255,255,0.4)" fontSize="8" textAnchor="middle">Q = 1/3 (w1 + w2 + w3)</text>
            
            <text x="30" y="152" fill="rgba(255,255,255,0.5)" fontSize="8.5" textAnchor="start">
              Fractional writhe polynomials explain why quark charges exist in strict thirds.
            </text>
          </svg>
  );
};

export default Ch7_QuantumNumbers;

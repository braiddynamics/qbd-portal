import React from 'react';

const Ch11_DifferentialGeometry: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Curvature loops */}
            <g transform="translate(10, 0)">
              {/* Triangle loop */}
              <polygon points="60,40 100,110 30,110" fill="none" stroke="var(--ifm-color-primary)" strokeWidth="2" />
              
              {/* Parallel transport vector arrows */}
              <line x1="60" y1="40" x2="80" y2="75" stroke="var(--qbd-spine-color)" strokeWidth="2" />
              <polygon points="80,75 75,70 78,79" fill="var(--qbd-spine-color)" />
              
              <circle cx="60" cy="40" r="5" fill="#ffffff" />
              <circle cx="100" cy="110" r="5" fill="#ffffff" />
              <circle cx="30" cy="110" r="5" fill="#ffffff" />

              <text x="65" y="27" fill="var(--ifm-color-primary)" fontSize="10" fontWeight="bold" textAnchor="middle">Discrete Connection</text>
              <text x="65" y="130" fill="rgba(255,255,255,0.4)" fontSize="9" textAnchor="middle">Loop parallel transport</text>
            </g>

            {/* Curvature math card */}
            <g transform="translate(160, 45)">
              <rect x="0" y="0" width="160" height="85" fill="rgba(255,255,255,0.01)" stroke="rgba(255,255,255,0.06)" strokeWidth="1" rx="6" />
              <text x="80" y="22" fill="var(--ifm-color-primary-light)" fontSize="10" fontWeight="bold" textAnchor="middle">Topological Invariance</text>
              <line x1="15" y1="32" x2="145" y2="32" stroke="rgba(255,255,255,0.08)" strokeWidth="1" />
              
              <text x="80" y="52" fill="#ffffff" fontSize="13" fontWeight="bold" textAnchor="middle">d² = 0</text>
              <text x="80" y="70" fill="rgba(255,255,255,0.4)" fontSize="8" textAnchor="middle">Discrete connection connecting connections</text>
            </g>
            
            <text x="170" y="157" fill="rgba(255,255,255,0.5)" fontSize="8.5" textAnchor="middle">
              Calculus on posets satisfies d² = 0, securing metric-free curvature conservation.
            </text>
          </svg>
  );
};

export default Ch11_DifferentialGeometry;

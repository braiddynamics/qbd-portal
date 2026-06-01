import React from 'react';

const Ch13_ContinuumLimit: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Left: Dense discrete network mesh */}
            <g transform="translate(10, 0)">
              <rect x="10" y="30" width="110" height="120" fill="rgba(255,255,255,0.01)" stroke="rgba(255,255,255,0.1)" strokeWidth="1" rx="6" />
              {/* Dense grid */}
              <line x1="20" y1="50" x2="110" y2="130" stroke="var(--ifm-color-primary-light)" strokeWidth="0.8" />
              <line x1="20" y1="130" x2="110" y2="50" stroke="var(--ifm-color-primary-light)" strokeWidth="0.8" />
              <line x1="65" y1="35" x2="65" y2="145" stroke="var(--ifm-color-primary-light)" strokeWidth="0.8" />
              <circle cx="65" cy="90" r="5" fill="var(--ifm-color-primary)" />
              <text x="65" y="22" fill="var(--ifm-color-primary)" fontSize="9" fontWeight="bold" textAnchor="middle">1. Discrete Poset Mesh</text>
              <text x="65" y="140" fill="rgba(255,255,255,0.4)" fontSize="8" textAnchor="middle">Lattice spacing l_p → 0</text>
            </g>

            {/* Convergence Arrow */}
            <g transform="translate(130, 85)">
              <line x1="0" y1="0" x2="30" y2="0" stroke="var(--qbd-spine-color)" strokeWidth="2.5" />
              <path d="M 24,-3 L 30,0 L 24,3" fill="none" stroke="var(--qbd-spine-color)" strokeWidth="2.5" />
              <text x="15" y="-6" fill="var(--qbd-spine-color)" fontSize="8" textAnchor="middle">GHP Limit</text>
            </g>

            {/* Right: Curved manifold sheet */}
            <g transform="translate(165, 0)">
              <rect x="10" y="30" width="110" height="120" fill="rgba(255,255,255,0.01)" stroke="rgba(255,255,255,0.1)" strokeWidth="1" rx="6" />
              {/* Smooth curved ribbon */}
              <path d="M 20,70 C 50,30 70,110 110,60" fill="none" stroke="var(--qbd-spine-color)" strokeWidth="3" />
              <path d="M 20,110 C 50,70 70,150 110,100" fill="none" stroke="var(--qbd-spine-color)" strokeWidth="1" strokeDasharray="3,3" />
              
              <text x="65" y="22" fill="var(--qbd-spine-color)" fontSize="9" fontWeight="bold" textAnchor="middle">2. Smooth Manifold</text>
              <text x="65" y="140" fill="var(--ifm-color-primary-light)" fontSize="8" textAnchor="middle">Curved Spacetime (M, g)</text>
            </g>
          </svg>
  );
};

export default Ch13_ContinuumLimit;

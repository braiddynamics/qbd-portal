import React from 'react';

const Ch5_Geometrogenesis: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Left: Chaos pre-geometry */}
            <g transform="translate(10, 0)">
              <rect x="10" y="30" width="110" height="120" fill="rgba(239, 68, 68, 0.03)" stroke="rgba(239, 68, 68, 0.2)" strokeWidth="1" rx="6" />
              <path d="M 25,60 L 50,45 L 85,75 L 35,115 L 95,120 L 70,55" fill="none" stroke="#ef4444" strokeWidth="1" />
              <circle cx="25" cy="60" r="4" fill="#ef4444" />
              <circle cx="50" cy="45" r="4" fill="#ef4444" />
              <circle cx="85" cy="75" r="4" fill="#ef4444" />
              <circle cx="35" cy="115" r="4" fill="#ef4444" />
              <circle cx="95" cy="120" r="4" fill="#ef4444" />
              <circle cx="70" cy="55" r="4" fill="#ef4444" />
              <text x="65" y="22" fill="#ef4444" fontSize="10" fontWeight="bold" textAnchor="middle">1. Pre-Geometric Foam</text>
              <text x="65" y="140" fill="rgba(239,68,68,0.7)" fontSize="8" textAnchor="middle">High Relational Entropy</text>
            </g>

            {/* Transition Arrow */}
            <g transform="translate(130, 85)">
              <line x1="0" y1="0" x2="30" y2="0" stroke="var(--ifm-color-primary-light)" strokeWidth="2" />
              <path d="M 24,-3 L 30,0 L 24,3" fill="none" stroke="var(--ifm-color-primary-light)" strokeWidth="2" />
              <text x="15" y="-6" fill="var(--ifm-color-primary-light)" fontSize="8" textAnchor="middle">Phase Change</text>
            </g>

            {/* Right: Crystallized geometry */}
            <g transform="translate(165, 0)">
              <rect x="10" y="30" width="110" height="120" fill="rgba(37, 194, 160, 0.03)" stroke="rgba(37, 194, 160, 0.2)" strokeWidth="1" rx="6" />
              {/* Triangles grid */}
              <polygon points="30,60 65,40 100,60" fill="none" stroke="var(--ifm-color-primary)" strokeWidth="1.5" />
              <polygon points="30,60 65,80 100,60" fill="none" stroke="var(--ifm-color-primary)" strokeWidth="1.5" />
              <polygon points="30,100 65,80 100,100" fill="none" stroke="var(--ifm-color-primary)" strokeWidth="1.5" />
              <polygon points="30,100 65,120 100,100" fill="none" stroke="var(--ifm-color-primary)" strokeWidth="1.5" />
              
              <circle cx="30" cy="60" r="4" fill="#ffffff" />
              <circle cx="65" cy="40" r="4" fill="#ffffff" />
              <circle cx="100" cy="60" r="4" fill="#ffffff" />
              <circle cx="65" cy="80" r="4" fill="#ffffff" />
              <circle cx="30" cy="100" r="4" fill="#ffffff" />
              <circle cx="100" cy="100" r="4" fill="#ffffff" />
              <circle cx="65" cy="120" r="4" fill="#ffffff" />
              <text x="65" y="22" fill="var(--ifm-color-primary)" fontSize="10" fontWeight="bold" textAnchor="middle">2. Spatial Grid</text>
              <text x="65" y="140" fill="var(--ifm-color-primary-light)" fontSize="8" textAnchor="middle">Crystallized Vacuum</text>
            </g>
          </svg>
  );
};

export default Ch5_Geometrogenesis;

import React from 'react';

const Ch9_GenerationsAndDecay: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Three generations side-by-side */}
            <g transform="translate(10, 40)">
              {/* Gen 1: Electron */}
              <rect x="10" y="10" width="85" height="90" fill="rgba(37,194,160,0.03)" stroke="rgba(37,194,160,0.2)" strokeWidth="1" rx="4" />
              <path d="M 25,60 C 50,75 50,35 80,60" fill="none" stroke="var(--ifm-color-primary)" strokeWidth="2" />
              <circle cx="25" cy="60" r="3.5" fill="#ffffff" />
              <circle cx="80" cy="60" r="3.5" fill="#ffffff" />
              <text x="52" y="27" fill="var(--ifm-color-primary)" fontSize="9" fontWeight="bold" textAnchor="middle">1st Generation</text>
              <text x="52" y="85" fill="rgba(255,255,255,0.5)" fontSize="8" textAnchor="middle">Electron / u-Quark</text>
              
              {/* Gen 2: Muon */}
              <rect x="110" y="10" width="85" height="90" fill="rgba(139,92,246,0.03)" stroke="rgba(139,92,246,0.2)" strokeWidth="1" rx="4" />
              <path d="M 125,60 C 140,80 140,30 152,60 C 165,80 165,30 180,60" fill="none" stroke="var(--qbd-spine-color)" strokeWidth="2" />
              <circle cx="125" cy="60" r="3.5" fill="#ffffff" />
              <circle cx="152" cy="60" r="3.5" fill="#ffffff" />
              <circle cx="180" cy="60" r="3.5" fill="#ffffff" />
              <text x="152" y="27" fill="var(--qbd-spine-color)" fontSize="9" fontWeight="bold" textAnchor="middle">2nd Generation</text>
              <text x="152" y="85" fill="rgba(255,255,255,0.5)" fontSize="8" textAnchor="middle">Muon / c-Quark</text>

              {/* Gen 3: Tau */}
              <rect x="210" y="10" width="85" height="90" fill="rgba(59,130,246,0.03)" stroke="rgba(59,130,246,0.2)" strokeWidth="1" rx="4" />
              <path d="M 225,60 C 235,80 235,30 245,60 C 255,80 255,30 265,60 C 275,80 275,30 280,60" fill="none" stroke="#3b82f6" strokeWidth="1.5" />
              <circle cx="225" cy="60" r="3.5" fill="#ffffff" />
              <circle cx="280" cy="60" r="3.5" fill="#ffffff" />
              <text x="252" y="27" fill="#3b82f6" fontSize="9" fontWeight="bold" textAnchor="middle">3rd Generation</text>
              <text x="252" y="85" fill="rgba(255,255,255,0.5)" fontSize="8" textAnchor="middle">Tau / t-Quark</text>
            </g>
            
            <text x="170" y="160" fill="rgba(255,255,255,0.4)" fontSize="8.5" textAnchor="middle">
              Matter generation families correspond strictly to three stable topological twist configurations.
            </text>
          </svg>
  );
};

export default Ch9_GenerationsAndDecay;

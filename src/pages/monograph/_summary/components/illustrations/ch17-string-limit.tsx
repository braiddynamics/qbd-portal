import React from 'react';

const Ch17_StringLimit: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Worldsheet ribbon band */}
            <path d="M 40,60 C 110,20 170,120 240,80 C 270,60 285,55 300,60" fill="none" stroke="var(--ifm-color-primary)" strokeWidth="4.5" />
            <path d="M 40,85 C 110,45 170,145 240,105 C 270,85 285,80 300,85" fill="none" stroke="var(--ifm-color-primary)" strokeWidth="1" />
            
            {/* Mesh grid inside ribbon representing worldsheet area */}
            <line x1="110" y1="36" x2="110" y2="61" stroke="rgba(255,255,255,0.2)" strokeWidth="1" />
            <line x1="170" y1="96" x2="170" y2="121" stroke="rgba(255,255,255,0.2)" strokeWidth="1" />
            <line x1="240" y1="80" x2="240" y2="105" stroke="rgba(255,255,255,0.2)" strokeWidth="1" />

            <text x="155" y="47" fill="var(--ifm-color-primary)" fontSize="10" fontWeight="bold" textAnchor="middle">2D Worldsheet Area</text>
            <text x="40" y="50" fill="var(--qbd-spine-color)" fontSize="8" textAnchor="middle">1D Braid String</text>
            <text x="300" y="50" fill="var(--qbd-spine-color)" fontSize="8" textAnchor="middle">Propagation</text>

            <text x="170" y="147" fill="rgba(255,255,255,0.4)" fontSize="8.5" textAnchor="middle">
              tripartite braids behave like relativistic strings sweeping out 2D areas.
            </text>
          </svg>
  );
};

export default Ch17_StringLimit;

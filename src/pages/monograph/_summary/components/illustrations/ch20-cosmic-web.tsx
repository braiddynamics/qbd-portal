import React from 'react';

const Ch20_CosmicWeb: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Cosmic filament webs and voids */}
            <path d="M 30,30 Q 170,120 310,30" fill="none" stroke="var(--ifm-color-primary)" strokeWidth="3" opacity="0.8" />
            <path d="M 30,150 Q 170,100 310,150" fill="none" stroke="var(--ifm-color-primary)" strokeWidth="2" opacity="0.6" />
            <path d="M 170,10 Q 170,90 170,170" fill="none" stroke="var(--qbd-spine-color)" strokeWidth="1.5" strokeDasharray="3,3" />

            {/* Dense cluster filaments */}
            <circle cx="100" cy="65" r="9" fill="var(--ifm-color-primary)" />
            <circle cx="240" cy="65" r="9" fill="var(--ifm-color-primary)" />
            <circle cx="170" cy="100" r="12" fill="var(--qbd-spine-color)" />

            <circle cx="100" cy="65" r="3" fill="#ffffff" />
            <circle cx="240" cy="65" r="3" fill="#ffffff" />
            <circle cx="170" cy="100" r="4" fill="#ffffff" />

            {/* Labeled annotations */}
            <text x="170" y="82" fill="var(--qbd-spine-color)" fontSize="9" fontWeight="bold" textAnchor="middle">Filament Cluster</text>
            <text x="60" y="110" fill="var(--ifm-color-primary-light)" fontSize="10" fontWeight="bold">EMPTY VOID</text>
            <text x="240" y="110" fill="var(--ifm-color-primary-light)" fontSize="10" fontWeight="bold">EMPTY VOID</text>
            
            <text x="170" y="157" fill="rgba(255,255,255,0.4)" fontSize="8.5" textAnchor="middle">
              Lattice stress clusters events into a vast cosmic web of filaments and voids.
            </text>
          </svg>
  );
};

export default Ch20_CosmicWeb;

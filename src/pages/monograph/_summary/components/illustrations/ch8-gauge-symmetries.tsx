import React from 'react';

const Ch8_GaugeSymmetries: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Relational ribbon swaps */}
            <g transform="translate(25, 30)">
              {/* Ribbon 1 */}
              <line x1="30" y1="20" x2="110" y2="100" stroke="var(--ifm-color-primary)" strokeWidth="2.5" />
              {/* Ribbon 2 */}
              <line x1="110" y1="20" x2="30" y2="100" stroke="var(--qbd-spine-color)" strokeWidth="2.5" />
              
              <circle cx="30" cy="20" r="5" fill="#ffffff" />
              <circle cx="110" cy="20" r="5" fill="#ffffff" />
              <circle cx="30" cy="100" r="5" fill="#ffffff" />
              <circle cx="110" cy="100" r="5" fill="#ffffff" />
              <text x="70" y="12" fill="var(--ifm-color-primary)" fontSize="9" fontWeight="bold" textAnchor="middle">Strand Swap Operator</text>
              <text x="70" y="117" fill="rgba(255,255,255,0.4)" fontSize="8" textAnchor="middle">Relational Generator</text>
            </g>

            {/* Standard Model Lie groups emergence */}
            <g transform="translate(180, 40)">
              <rect x="0" y="0" width="130" height="90" fill="rgba(255,255,255,0.01)" stroke="rgba(255,255,255,0.1)" strokeWidth="1" rx="6" />
              <text x="65" y="18" fill="var(--ifm-color-primary-light)" fontSize="9" fontWeight="bold" textAnchor="middle">Emergent Lie Symmetries</text>
              <line x1="15" y1="26" x2="115" y2="26" stroke="rgba(255,255,255,0.1)" strokeWidth="1" />
              
              <text x="65" y="44" fill="#ffffff" fontSize="10" textAnchor="middle">SU(3) Color (Gluons)</text>
              <text x="65" y="60" fill="#ffffff" fontSize="10" textAnchor="middle">SU(2) Weak (W/Z Bosons)</text>
              <text x="65" y="76" fill="#ffffff" fontSize="10" textAnchor="middle">U(1) EM (Photons)</text>
              
              <text x="-10" y="115" fill="rgba(255,255,255,0.5)" fontSize="8.5" textAnchor="middle">
                Gauge symmetries emerge from spatial coordinate-free ribbon swaps.
              </text>
            </g>
          </svg>
  );
};

export default Ch8_GaugeSymmetries;

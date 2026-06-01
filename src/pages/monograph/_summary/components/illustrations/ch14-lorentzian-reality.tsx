import React from 'react';

const Ch14_LorentzianReality: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Double lightcones representing Lorentzian causality */}
            <g transform="translate(170, 90)">
              {/* Future Lightcone */}
              <polygon points="-40,-50 0,0 40,-50" fill="rgba(37, 194, 160, 0.12)" stroke="var(--ifm-color-primary)" strokeWidth="1.5" />
              <text x="0" y="-35" fill="var(--ifm-color-primary)" fontSize="9" fontWeight="bold" textAnchor="middle">Future Lightcone</text>

              {/* Past Lightcone */}
              <polygon points="-40,50 0,0 40,50" fill="rgba(139, 92, 246, 0.12)" stroke="var(--qbd-spine-color)" strokeWidth="1.5" />
              <text x="0" y="42" fill="var(--qbd-spine-color)" fontSize="9" fontWeight="bold" textAnchor="middle">Past Lightcone</text>

              {/* Center observer node */}
              <circle cx="0" cy="0" r="5" fill="#ffffff" />
              <text x="8" y="3" fill="#ffffff" fontSize="8" textAnchor="start">Causal Event</text>
              
              {/* Spacetime signature label */}
              <text x="-90" y="5" fill="var(--ifm-color-primary-light)" fontSize="9" fontWeight="bold" textAnchor="middle">Lorentzian Signature</text>
              <text x="-90" y="20" fill="#ffffff" fontSize="13" fontWeight="bold" textAnchor="middle">(-, +, +, +)</text>

              {/* Maximum path label */}
              <text x="90" y="5" fill="var(--ifm-color-primary-light)" fontSize="9" fontWeight="bold" textAnchor="middle">Observer geodesics</text>
              <text x="90" y="20" fill="rgba(255,255,255,0.4)" fontSize="8.5" textAnchor="middle">Max logical-time paths</text>
            </g>
          </svg>
  );
};

export default Ch14_LorentzianReality;

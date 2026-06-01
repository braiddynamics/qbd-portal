import React from 'react';

const Ch15_EPRWormhole: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            {/* Background ER=EPR Wormhole illustration */}
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Distant spatial node clusters */}
            <g transform="translate(25, 45)">
              <circle cx="30" cy="45" r="25" fill="rgba(37,194,160,0.04)" stroke="var(--ifm-color-primary)" strokeWidth="1" strokeDasharray="3,3" />
              <circle cx="30" cy="45" r="5" fill="var(--ifm-color-primary)" />
              <circle cx="15" cy="35" r="3" fill="#ffffff" />
              <circle cx="45" cy="55" r="3" fill="#ffffff" />
              <text x="30" y="12" fill="var(--ifm-color-primary)" fontSize="9" fontWeight="bold" textAnchor="middle">Event Cluster A</text>
            </g>

            <g transform="translate(195, 45)">
              <circle cx="60" cy="45" r="25" fill="rgba(37,194,160,0.04)" stroke="var(--ifm-color-primary)" strokeWidth="1" strokeDasharray="3,3" />
              <circle cx="60" cy="45" r="5" fill="var(--ifm-color-primary)" />
              <circle cx="45" cy="35" r="3" fill="#ffffff" />
              <circle cx="75" cy="55" r="3" fill="#ffffff" />
              <text x="60" y="12" fill="var(--ifm-color-primary)" fontSize="9" fontWeight="bold" textAnchor="middle">Event Cluster B</text>
            </g>

            {/* Non-local Entanglement bridge (ER = EPR Wormhole) */}
            <path d="M 55,90 C 110,40 170,40 255,90" fill="none" stroke="var(--qbd-spine-color)" strokeWidth="3.5" />
            <path d="M 55,90 C 110,140 170,140 255,90" fill="none" stroke="var(--ifm-color-primary-light)" strokeWidth="1.5" strokeDasharray="3,3" />
            
            <text x="155" y="65" fill="var(--qbd-spine-color)" fontSize="10" fontWeight="bold" textAnchor="middle">ER = EPR Wormhole Bridge</text>
            <text x="155" y="120" fill="var(--ifm-color-primary-light)" fontSize="8.5" textAnchor="middle">Non-local Entanglement Edge</text>
            
            <text x="170" y="157" fill="rgba(255,255,255,0.5)" fontSize="8.5" textAnchor="middle">
              Spatial distance is emergent: quantum entanglement generates physical shortcuts.
            </text>
          </svg>
  );
};

export default Ch15_EPRWormhole;

import React from 'react';

const Ch10_QuantumUniversality: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Stabilizer grid circuit */}
            <g transform="translate(20, 20)">
              {/* Lines representing qubits */}
              <line x1="20" y1="30" x2="280" y2="30" stroke="rgba(255,255,255,0.15)" strokeWidth="2" />
              <line x1="20" y1="70" x2="280" y2="70" stroke="rgba(255,255,255,0.15)" strokeWidth="2" />
              <line x1="20" y1="110" x2="280" y2="110" stroke="rgba(255,255,255,0.15)" strokeWidth="2" />
              
              {/* Gate blocks */}
              <rect x="60" y="15" width="30" height="30" fill="rgba(37,194,160,0.2)" stroke="var(--ifm-color-primary)" strokeWidth="1.5" rx="4" />
              <text x="75" y="34" fill="var(--ifm-color-primary)" fontSize="11" fontWeight="bold" textAnchor="middle">X</text>
              
              <rect x="120" y="55" width="30" height="30" fill="rgba(139,92,246,0.2)" stroke="var(--qbd-spine-color)" strokeWidth="1.5" rx="4" />
              <text x="135" y="74" fill="var(--qbd-spine-color)" fontSize="11" fontWeight="bold" textAnchor="middle">H</text>
              
              {/* Entangling CZ gate */}
              <line x1="200" y1="30" x2="200" y2="110" stroke="#3b82f6" strokeWidth="1.5" />
              <circle cx="200" cy="30" r="5" fill="#3b82f6" />
              <circle cx="200" cy="110" r="5" fill="#3b82f6" />
              <text x="212" y="75" fill="#3b82f6" fontSize="9" fontWeight="bold">CZ</text>
              
              <rect x="230" y="95" width="30" height="30" fill="rgba(59,130,246,0.2)" stroke="#3b82f6" strokeWidth="1.5" rx="4" />
              <text x="245" y="114" fill="#3b82f6" fontSize="11" fontWeight="bold" textAnchor="middle">T</text>

              {/* Explanatory Annotations */}
              <text x="150" y="145" fill="rgba(255,255,255,0.5)" fontSize="9" textAnchor="middle">
                tripartite swap operations construct a universal fault-tolerant quantum computer.
              </text>
            </g>
          </svg>
  );
};

export default Ch10_QuantumUniversality;

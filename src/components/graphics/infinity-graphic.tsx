import React from 'react';
import './infinity-graphic.css';

export default function InfinityGraphic() {
  const primaryColor = 'var(--ifm-color-primary)';
  const secondaryColor = 'var(--ifm-color-emphasis-400)';

  return (
    <div style={{ width: '100%', height: '100%', display: 'flex', justifyContent: 'center', alignItems: 'center', padding: '1rem' }}>
      <svg viewBox="0 0 200 200" style={{ width: '100%', maxWidth: '180px', height: 'auto', overflow: 'visible' }}>
        
        {/* The Discrete Infinity Path (Floating, no background) */}
        <path 
          d="M 100 100 C 150 40, 210 60, 180 120 C 150 180, 120 120, 100 100 C 80 80, 50 20, 20 80 C -10 140, 50 160, 100 100 Z" 
          fill="none" 
          stroke={secondaryColor} 
          strokeWidth="4" 
          strokeLinecap="round"
          strokeDasharray="1 12"
          opacity="0.4"
          className="infinity-track" 
        />
        
        {/* Forward Traveling Data Packet */}
        <path 
          d="M 100 100 C 150 40, 210 60, 180 120 C 150 180, 120 120, 100 100 C 80 80, 50 20, 20 80 C -10 140, 50 160, 100 100 Z" 
          fill="none" 
          stroke={primaryColor} 
          strokeWidth="4" 
          strokeLinecap="round" 
          className="infinity-packet packet-forward" 
        />

        {/* Reverse Traveling Data Packet (Equilibrium) */}
        <path 
          d="M 100 100 C 150 40, 210 60, 180 120 C 150 180, 120 120, 100 100 C 80 80, 50 20, 20 80 C -10 140, 50 160, 100 100 Z" 
          fill="none" 
          stroke="#ffffff" 
          strokeWidth="3" 
          strokeLinecap="round" 
          className="infinity-packet packet-reverse" 
        />
        
        {/* The Central Crossing Node */}
        <circle cx="100" cy="100" r="6" fill={primaryColor} className="infinity-center-node" />
      </svg>
    </div>
  );
}
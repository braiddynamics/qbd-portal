import React from 'react';

const Ch1_Substrate: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            {/* Background grids */}
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            <line x1="20" y1="90" x2="320" y2="90" stroke="rgba(255,255,255,0.05)" strokeDasharray="3,3" />
            
            {/* Causal Paths */}
            <path d="M 40,90 L 110,40 L 180,90 L 250,40 L 300,90" fill="none" stroke="var(--ifm-color-primary)" strokeWidth="2.5" />
            <path d="M 40,90 L 110,140 L 180,90 L 250,140 L 300,90" fill="none" stroke="var(--qbd-spine-color)" strokeWidth="2" strokeDasharray="3,3" />
            <line x1="110" y1="40" x2="110" y2="140" stroke="var(--ifm-color-primary-light)" strokeWidth="1.5" strokeDasharray="2,2" />
            <line x1="250" y1="40" x2="250" y2="140" stroke="var(--ifm-color-primary-light)" strokeWidth="1.5" strokeDasharray="2,2" />

            {/* Event Nodes */}
            <circle cx="40" cy="90" r="7" fill="var(--ifm-color-primary)" />
            <circle cx="110" cy="40" r="7" fill="#3b82f6" />
            <circle cx="110" cy="140" r="7" fill="#3b82f6" />
            <circle cx="180" cy="90" r="7" fill="var(--ifm-color-primary)" />
            <circle cx="250" cy="40" r="7" fill="var(--qbd-spine-color)" />
            <circle cx="250" cy="140" r="7" fill="var(--qbd-spine-color)" />
            <circle cx="300" cy="90" r="7" fill="var(--ifm-color-primary)" />

            {/* Explanatory Annotations */}
            <text x="40" y="80" fill="#ffffff" fontSize="9" textAnchor="middle">Initial Event</text>
            <text x="110" y="27" fill="#3b82f6" fontSize="9" textAnchor="middle">Branch A</text>
            <text x="110" y="157" fill="#3b82f6" fontSize="9" textAnchor="middle">Branch B</text>
            <text x="180" y="80" fill="#ffffff" fontSize="9" textAnchor="middle">Reconvergence</text>
            <text x="250" y="27" fill="var(--qbd-spine-color)" fontSize="9" textAnchor="middle">Future A</text>
            <text x="250" y="157" fill="var(--qbd-spine-color)" fontSize="9" textAnchor="middle">Future B</text>
            
            {/* Timeline Arrow */}
            <line x1="30" y1="170" x2="310" y2="170" stroke="rgba(255,255,255,0.3)" strokeWidth="1" markerEnd="url(#arrow)" />
            <text x="170" y="167" fill="rgba(255,255,255,0.4)" fontSize="8" textAnchor="middle">Logical Clock Flow →</text>
            
            {/* Definitions marker definition */}
            <defs>
              <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 0 L 10 5 L 0 10 z" fill="rgba(255,255,255,0.4)" />
              </marker>
            </defs>
          </svg>
  );
};

export default Ch1_Substrate;

import React from 'react';

const Ch0_HistoricalRoots: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
      {/* Background container */}
      <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
      <line x1="20" y1="90" x2="320" y2="90" stroke="rgba(255,255,255,0.03)" strokeDasharray="3,3" />

      {/* Discrete Path (Greek & Indian Atomism) */}
      <path d="M 40,60 L 170,90" fill="none" stroke="var(--ifm-color-primary)" strokeWidth="2" strokeDasharray="2,2" />
      
      {/* Continuous Path (Chinese Qi Resonance & Plenum) */}
      <path d="M 40,120 L 170,90" fill="none" stroke="var(--qbd-spine-color)" strokeWidth="2" strokeDasharray="2,2" />
      
      {/* Impetus / Mayl to Modern QBD Path */}
      <path d="M 170,90 L 300,90" fill="none" stroke="var(--ifm-color-primary-light)" strokeWidth="2.5" />

      {/* Glow Backdrops */}
      <circle cx="40" cy="60" r="15" fill="rgba(37,194,160,0.06)" />
      <circle cx="40" cy="120" r="15" fill="rgba(139,92,246,0.06)" />
      <circle cx="170" cy="90" r="18" fill="rgba(59,130,246,0.08)" />
      <circle cx="300" cy="90" r="20" fill="rgba(37,194,160,0.12)" />

      {/* Node Circles */}
      <circle cx="40" cy="60" r="7" fill="var(--ifm-color-primary)" />
      <circle cx="40" cy="120" r="7" fill="var(--qbd-spine-color)" />
      <circle cx="170" cy="90" r="8" fill="#3b82f6" />
      <circle cx="300" cy="90" r="9" fill="var(--ifm-color-primary)" />

      {/* Main Historical Flow Labels */}
      <text x="40" y="40" fill="#ffffff" fontSize="9" fontWeight="bold" textAnchor="middle">THE DISCRETE</text>
      <text x="40" y="50" fill="var(--ifm-color-emphasis-500)" fontSize="7" textAnchor="middle">Atoms and Void (Greece / India)</text>

      <text x="40" y="140" fill="#ffffff" fontSize="9" fontWeight="bold" textAnchor="middle">THE CONTINUOUS</text>
      <text x="40" y="150" fill="var(--ifm-color-emphasis-500)" fontSize="7" textAnchor="middle">Qi Resonance and Plenum (China)</text>

      <text x="170" y="67" fill="#ffffff" fontSize="9" fontWeight="bold" textAnchor="middle">CONSERVED STATE</text>
      <text x="170" y="76" fill="var(--ifm-color-emphasis-500)" fontSize="7" textAnchor="middle">Mayl and Impetus (Middle Ages)</text>

      <text x="300" y="62" fill="var(--ifm-color-primary-light)" fontSize="10" fontWeight="bold" textAnchor="middle">QBD SYNTHESIS</text>
      <text x="300" y="71" fill="var(--ifm-color-emphasis-500)" fontSize="7" textAnchor="middle">Causal Informational Poset</text>

      {/* Small Detail Labels inside Node groups */}
      <text x="40" y="64" fill="#000000" fontSize="5" fontWeight="bold" textAnchor="middle">1</text>
      <text x="40" y="124" fill="#000000" fontSize="5" fontWeight="bold" textAnchor="middle">2</text>
      <text x="170" y="93" fill="#000000" fontSize="6" fontWeight="bold" textAnchor="middle">3</text>
      <text x="300" y="93" fill="#000000" fontSize="6" fontWeight="bold" textAnchor="middle">4</text>

      {/* Axis timeline arrow */}
      <line x1="20" y1="168" x2="310" y2="168" stroke="rgba(255,255,255,0.2)" strokeWidth="0.8" markerEnd="url(#arrow-hist)" />
      <text x="165" y="165" fill="rgba(255,255,255,0.3)" fontSize="7" textAnchor="middle">MILLISECONDS OF COGNITIVE CHRONOLOGY</text>

      {/* Arrow Marker Definitions */}
      <defs>
        <marker id="arrow-hist" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
          <path d="M 0 0 L 10 5 L 0 10 z" fill="rgba(255,255,255,0.2)" />
        </marker>
      </defs>
    </svg>
  );
};

export default Ch0_HistoricalRoots;

import React from 'react';
import './dag-graphic.css';

export default function DagGraphic() {
  const primaryColor = 'var(--ifm-color-primary)';
  const gridColor = 'var(--ifm-color-emphasis-200)';
  const secondaryEdgeColor = 'var(--ifm-color-emphasis-300)';

  return (
    <div style={{ width: '100%', height: '100%', display: 'flex', justifyContent: 'center', alignItems: 'center', padding: '1rem' }}>
      <svg viewBox="0 0 200 200" style={{ width: '100%', maxWidth: '200px', height: 'auto', overflow: 'visible' }}>
        <defs>
          {/* Hexagonal Grid Pattern for the Background */}
          <pattern id="hex-grid" width="40" height="34.64" patternUnits="userSpaceOnUse">
            <path
              d="M20 0 L40 11.55 L40 34.64 L20 46.19 L0 34.64 L0 11.55 Z"
              fill="none"
              stroke={gridColor}
              strokeWidth="0.5"
              opacity="0.5"
            />
          </pattern>

          {/* Arrowhead Markers */}
          <marker id="arrow-primary" viewBox="0 0 10 10" refX="24" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill={primaryColor} className="dag-arrow" />
          </marker>
          <marker id="arrow-secondary" viewBox="0 0 10 10" refX="24" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill={secondaryEdgeColor} />
          </marker>
        </defs>

        {/* Background Rect */}
        <rect x="-20" y="-20" width="240" height="240" fill="url(#hex-grid)" />

        {/* --- The True Geometric Quantum (Closed 3-Cycle) --- */}

        {/* Static Background Loop */}
        <g stroke={secondaryEdgeColor} strokeWidth="1.5" fill="none" markerEnd="url(#arrow-secondary)" opacity="0.5">
          {/* B -> A */}
          <line x1="50" y1="140" x2="100" y2="40" />
          {/* A -> C */}
          <line x1="100" y1="40" x2="150" y2="140" />
          {/* C -> B */}
          <line x1="150" y1="140" x2="50" y2="140" />
        </g>

        {/* Animating Data Flow (Chasing the loop) */}
        <g stroke={secondaryEdgeColor} strokeWidth="2.5" fill="none" markerEnd="url(#arrow-primary)">
          {/* B -> A */}
          <line x1="50" y1="140" x2="100" y2="40" className="dag-edge edge-1" />
          {/* A -> C */}
          <line x1="100" y1="40" x2="150" y2="140" className="dag-edge edge-2" />
          {/* C -> B */}
          <line x1="150" y1="140" x2="50" y2="140" className="dag-edge edge-3" />
        </g>

        {/* The 3 Nodes */}
        <g fill={primaryColor}>
          {/* Top Node (A) */}
          <circle cx="100" cy="40" r="12" className="dag-node node-top" />
          {/* Bottom Left Node (B) */}
          <circle cx="50" cy="140" r="12" className="dag-node node-mid-l" />
          {/* Bottom Right Node (C) */}
          <circle cx="150" cy="140" r="12" className="dag-node node-mid-r" />
        </g>
      </svg>
    </div>
  );
}
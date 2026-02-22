import React from 'react';
import './braid-graphic.css';

export default function BraidGraphic() {
  // The exact coordinates mapping to your diagram's timeline
  const t1 = 200;       // Bottom
  const t2_start = 160; 
  const t2_end = 120;   // First Crossing (Right over Mid)
  const t3_start = 100;
  const t3_end = 60;    // Second Crossing (Mid over Left)
  const t4 = 20;        // Top

  // SVG Paths mapped bottom-up
  // Ribbon 2 (Green) - Stays left, then crosses to middle
  const pathG = `M 50 ${t1} L 50 ${t3_start} C 50 80, 100 80, 100 ${t3_end} L 100 ${t4}`;
  
  // Ribbon 3 (Blue) - Starts middle, crosses to right, stays right
  const pathB = `M 100 ${t1} L 100 ${t2_start} C 100 140, 150 140, 150 ${t2_end} L 150 ${t4}`;
  
  // Ribbon 1 (Red) - The master crossing ribbon (Right -> Mid -> Left)
  const pathR = `M 150 ${t1} L 150 ${t2_start} C 150 140, 100 140, 100 ${t2_end} L 100 ${t3_start} C 100 80, 50 80, 50 ${t3_end} L 50 ${t4}`;

  return (
    <div style={{ width: '100%', height: '100%', display: 'flex', justifyContent: 'center', alignItems: 'center', padding: '1rem' }}>
      <svg viewBox="0 0 200 220" style={{ width: '100%', maxWidth: '160px', height: 'auto', overflow: 'visible' }}>
        
        {/* 1. Ribbon 3 (Blue) - Deepest background layer */}
        <path d={pathB} className="braid-ribbon braid-ribbon-b" />
        <path d={pathB} className="braid-packet" />

        {/* 2. Ribbon 2 (Green) - Middle layer */}
        <path d={pathG} className="braid-ribbon braid-ribbon-g" />
        <path d={pathG} className="braid-packet" />

        {/* 3. Ribbon 1 (Red) - Foreground layer. 
            We use a thick background-colored stroke first to 'cut' the lines beneath it, 
            creating the 3D over/under topological crossing. */}
        <path d={pathR} className="braid-eraser" />
        <path d={pathR} className="braid-ribbon braid-ribbon-r" />
        <path d={pathR} className="braid-packet" />

      </svg>
    </div>
  );
}
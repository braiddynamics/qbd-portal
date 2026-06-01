import React from 'react';

const Ch2_Constraints: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Unstable 4-Cycle Square */}
            <g transform="translate(0, 0)">
              <rect x="35" y="45" width="70" height="70" fill="none" stroke="#ef4444" strokeWidth="2" />
              <circle cx="35" cy="45" r="5" fill="#ffffff" />
              <circle cx="105" cy="45" r="5" fill="#ffffff" />
              <circle cx="105" cy="115" r="5" fill="#ffffff" />
              <circle cx="35" cy="115" r="5" fill="#ffffff" />
              <text x="70" y="32" fill="#ef4444" fontSize="10" fontWeight="bold" textAnchor="middle">Forbidden 4-Cycle</text>
              <text x="70" y="85" fill="#ef4444" fontSize="8" textAnchor="middle">Locality Defect</text>
            </g>

            {/* Transition Arrow */}
            <g transform="translate(130, 80)">
              <line x1="0" y1="0" x2="35" y2="0" stroke="var(--ifm-color-primary-light)" strokeWidth="2" />
              <path d="M 28,-4 L 36,0 L 28,4" fill="none" stroke="var(--ifm-color-primary-light)" strokeWidth="2" />
              <text x="17" y="-8" fill="var(--ifm-color-primary-light)" fontSize="8" textAnchor="middle">Triangulate</text>
            </g>

            {/* Stable Triangulated 3-Cycles */}
            <g transform="translate(155, 0)">
              <rect x="35" y="45" width="70" height="70" fill="none" stroke="var(--ifm-color-primary)" strokeWidth="2" />
              <line x1="35" y1="115" x2="105" y2="45" stroke="var(--qbd-spine-color)" strokeWidth="2.5" />
              <circle cx="35" cy="45" r="5" fill="#ffffff" />
              <circle cx="105" cy="45" r="5" fill="#ffffff" />
              <circle cx="105" cy="115" r="5" fill="#ffffff" />
              <circle cx="35" cy="115" r="5" fill="#ffffff" />
              <text x="70" y="32" fill="var(--ifm-color-primary)" fontSize="10" fontWeight="bold" textAnchor="middle">Simplicial Quanta</text>
              <text x="50" y="70" fill="var(--qbd-spine-color)" fontSize="8" textAnchor="middle">Chord</text>
              <text x="70" y="132" fill="var(--ifm-color-primary)" fontSize="8" textAnchor="middle">2 x Stable 3-Cycles</text>
            </g>
          </svg>
  );
};

export default Ch2_Constraints;

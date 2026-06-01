import React from 'react';

const Ch21_DarkRelics: React.FC = () => {
  return (
    <svg viewBox="0 0 340 180" width="100%" height="180">
            <rect width="340" height="180" fill="rgba(0,0,0,0.2)" rx="8" />
            
            {/* Relic vacancy defects (ash) */}
            <g transform="translate(170, 90)">
              {/* stable spatial background lattice */}
              <rect x="-80" y="-40" width="160" height="80" fill="none" stroke="rgba(255,255,255,0.06)" strokeWidth="1.5" />
              <line x1="-80" y1="0" x2="80" y2="0" stroke="rgba(255,255,255,0.06)" strokeWidth="1" />
              <line x1="0" y1="-40" x2="0" y2="40" stroke="rgba(255,255,255,0.06)" strokeWidth="1" />

              {/* Vacancy defect (missing node) */}
              <circle cx="0" cy="0" r="12" fill="none" stroke="#ef4444" strokeWidth="2.5" strokeDasharray="3,3" />
              <text x="0" y="4" fill="#ef4444" fontSize="13" fontWeight="bold" textAnchor="middle">Ø</text>
              <text x="0" y="-18" fill="#ef4444" fontSize="9" fontWeight="bold" textAnchor="middle">stable Relic Vacancy</text>

              {/* Surrounding metric warp lines */}
              <path d="M -40,-20 Q 0,0 -40,20" fill="none" stroke="var(--ifm-color-primary-light)" strokeWidth="1" />
              <path d="M 40,-20 Q 0,0 40,20" fill="none" stroke="var(--ifm-color-primary-light)" strokeWidth="1" />

              <text x="0" y="-55" fill="var(--ifm-color-primary)" fontSize="9.5" fontWeight="bold" textAnchor="middle">Dark Sector Relic pressure</text>
              <text x="0" y="55" fill="rgba(255,255,255,0.4)" fontSize="8.5" textAnchor="middle">
                relic vacancies ('ash') possess gravitational energy without matter.
              </text>
            </g>
          </svg>
  );
};

export default Ch21_DarkRelics;

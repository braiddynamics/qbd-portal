import React from 'react';
import Link from '@docusaurus/Link';
import FadeInView from './fade-in-view';

interface MonographCardProps {
  section: {
    part: string | number;
    title: string;
    subtitle: string;
    linkUrl: string;
  };
}

export default function MonographCard({ section }: MonographCardProps) {
  return (
    <FadeInView>
      <Link 
        to={section.linkUrl} 
        className="qbd-interactive-card section-row-margin" 
        style={{ display: 'block', textDecoration: 'none', color: 'inherit' }}
      >
        <div className="qbd-interactive-card-content section-grid-3col">
          
          {/* Column 1 */}
          <div className="section-text" style={{ textAlign: 'center' }}>
            {/* Reverted: Title is back on top */}
            <h3 style={{ fontSize: '1.75rem', marginBottom: '0.5rem', fontWeight: 'bold' }}>
              {section.title}
            </h3>
            {/* Reverted: Subtitle is back on the bottom */}
            <h4 style={{ marginBottom: '2rem', color: 'var(--ifm-color-primary)', fontSize: '1.25rem', fontWeight: 'normal', fontStyle: 'italic' }}>
              {section.subtitle}
            </h4>
            <span className="button button--secondary">
              Read Part {section.part} →
            </span>
          </div>

          {/* Column 2: Graphic Placeholder */}
          <div className="placeholder-box">
            <span>[ Graphic Placeholder ]</span>
          </div>

          {/* Column 3: Video Placeholder */}
          <div className="placeholder-box">
            <span>[ Video Placeholder ]</span>
          </div>

        </div>
      </Link>
    </FadeInView>
  );
}
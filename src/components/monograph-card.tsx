import React from 'react';
import Link from '@docusaurus/Link';
import FadeInView from './fade-in-view';
import DagGraphic from './graphics/dag-graphic';
import BraidGraphic from './graphics/braid-graphic';
import GeodesicGraphic from './graphics/geodesic-graphic';
import SCurveGraphic from './graphics/scurve-graphic';
import InfinityGraphic from './graphics/infinity-graphic';
import AppendixGraphic from './graphics/appendix-graphic';

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
                {/* Changed layout class to our new 2-column rule */}
                <div className="qbd-interactive-card-content section-grid-2col">

                    {/* Column 1: Core Text Content */}
                    <div className="section-text" style={{ textAlign: 'center' }}>
                        <h3 style={{ fontSize: '1.75rem', marginBottom: '0.5rem', fontWeight: 'bold' }}>
                            {section.title}
                        </h3>
                        <h4 style={{ marginBottom: '2rem', color: 'var(--ifm-color-primary)', fontSize: '1.25rem', fontWeight: 'normal', fontStyle: 'italic' }}>
                            {section.subtitle}
                        </h4>
                        <span className="button button--secondary">
                            Read Part {section.part} →
                        </span>
                    </div>

                    {/* Column 2: Interactive Graphic */}
                    <div className="placeholder-box" style={{ padding: 0, backgroundColor: 'transparent', border: 'none' }}>
                        {section.part === "1" ? <DagGraphic /> : 
                         section.part === "2" ? <BraidGraphic /> : 
                         section.part === "3" ? <GeodesicGraphic /> : 
                         section.part === "4" ? <SCurveGraphic /> : 
                         section.part === "5" ? <InfinityGraphic /> : 
                         section.part === "6" ? <AppendixGraphic /> : 
                         <span>[ Graphic Placeholder ]</span>}
                    </div>

                </div>
            </Link>
        </FadeInView>
    );
}
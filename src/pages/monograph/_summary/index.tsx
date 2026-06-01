import React, { useState } from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import Head from '@docusaurus/Head';

import { LightboxImageInfo } from './types';
import { chapters, timelineEvents, partsList } from './data';
import { MathInline } from './components/math';
import { ImportantDefinitionsBox, HistoricalCallout, ConceptualVisualBox } from './components/accessories';
import { LightConeSandbox, BraidAnimator, CurvatureWarp, TimelineSandbox, SelectionSandbox } from './components/sandboxes';
import { PartPreviewPanel } from './components/part-preview-panel';

// Helper to parse strings containing mixed plain text and inline LaTeX ($...$) and compile math cleanly
const renderMixedMathText = (text: string) => {
  if (!text.includes('$')) return <span>{text}</span>;
  
  // Split by matches of $...$ (capturing matching groups keeps the separators in the split array)
  const parts = text.split(/(\$.*?\$)/g);
  
  return (
    <span>
      {parts.map((part, index) => {
        if (part.startsWith('$') && part.endsWith('$')) {
          const mathExpr = part.slice(1, -1);
          return <MathInline key={index} math={mathExpr} />;
        }
        return part;
      })}
    </span>
  );
};

export default function MonographSummary() {
  // States for interactive SVG sandboxes
  const [timelineIndex, setTimelineIndex] = useState<number>(0);
  const [hoveredNode, setHoveredNode] = useState<number | null>(null);
  const [braidType, setBraidType] = useState<'electron' | 'quark' | 'neutrino'>('electron');
  const [warpStrength, setWarpStrength] = useState<number>(50);
  const [selectionStability, setSelectionStability] = useState<number>(75);

  // Lightbox Modal State
  const [lightbox, setLightbox] = useState<LightboxImageInfo | null>(null);

  // Enlarged Vector Diagram State
  const [activeDiagramNum, setActiveDiagramNum] = useState<number | null>(null);

  const renderChapterCard = (ch: typeof chapters[0]) => {
    const isIntro = ch.num === 0;
    return (
      <div className="qbd-dashboard-card" key={ch.num} id={`chapter-${ch.num}`}>
        
        {/* Chapter Header inside Card */}
        <div style={{ 
          display: 'flex', 
          justifyContent: 'space-between', 
          alignItems: 'flex-start', 
          borderBottom: '1px solid var(--ifm-color-emphasis-200)', 
          paddingBottom: '0.8rem', 
          marginBottom: '1.5rem' 
        }}>
          <div>
            <span style={{ 
              fontSize: '0.75rem', 
              fontWeight: '900', 
              color: 'var(--ifm-color-primary)', 
              textTransform: 'uppercase', 
              letterSpacing: '1.5px', 
              display: 'block' 
            }}>
              {isIntro ? 'INTRODUCTION' : `CHAPTER ${ch.num}`} • {ch.taxonomy.toUpperCase()}
            </span>
            <h2 style={{ 
              fontSize: '1.9rem', 
              fontWeight: '850', 
              margin: '0.2rem 0 0 0', 
              letterSpacing: '-0.5px', 
              color: 'var(--ifm-font-color-base)' 
            }}>
              {ch.title}
            </h2>
          </div>
          <div style={{ display: 'flex', gap: '0.4rem', alignItems: 'center' }}>
            {ch.leanProofs > 0 && (
              <span style={{
                fontSize: '0.7rem',
                fontWeight: '800',
                backgroundColor: 'rgba(16, 185, 129, 0.08)',
                color: 'var(--ifm-color-primary)',
                padding: '0.15rem 0.5rem',
                borderRadius: '6px',
                border: '1px solid currentColor'
              }}>
                Lean 4 Verified
              </span>
            )}
            {ch.pythonSims > 0 && (
              <span style={{
                fontSize: '0.7rem',
                fontWeight: '800',
                backgroundColor: 'rgba(59, 130, 246, 0.08)',
                color: '#3b82f6',
                padding: '0.15rem 0.5rem',
                borderRadius: '6px',
                border: '1px solid currentColor'
              }}>
                Python Sims
              </span>
            )}
          </div>
        </div>

        {/* Content Splitter Grid */}
        <div className="qbd-widescreen-splitter" style={{ display: 'flex', gap: '4%', width: '100%' }}>
          
          {/* LEFT COLUMN: text elements (57% width) */}
          <div className="qbd-col-left" style={{ flex: '0 0 57%', maxWidth: '57%', width: '57%', display: 'flex', flexDirection: 'column', gap: '1.5rem', boxSizing: 'border-box' }}>
            
            {/* Executive Critique (natural drop-cap wrap) */}
            <div>
              <p style={{ fontSize: '1.22rem', lineHeight: '1.85', color: 'var(--ifm-color-emphasis-800)', textAlign: 'justify', margin: 0 }}>
                <span style={{ 
                  fontSize: '3.6rem', 
                  fontWeight: '900', 
                  lineHeight: '1',
                  marginRight: '8px', 
                  color: 'var(--ifm-color-primary)', 
                  fontFamily: 'serif',
                  display: 'inline-block',
                  verticalAlign: 'baseline',
                  position: 'relative',
                  top: '3px'
                }}>
                  {ch.executiveEvaluation.charAt(0)}
                </span>
                {renderMixedMathText(ch.executiveEvaluation.slice(1))}
              </p>
            </div>

            {/* Deep-Dive Structural Breakdown */}
            <div>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '1.2rem' }}>
                {ch.breakdowns.map((b, bIdx) => (
                  <div key={bIdx}>
                    <strong style={{ display: 'block', fontSize: '1.08rem', color: 'var(--ifm-color-emphasis-950)', marginBottom: '0.2rem', letterSpacing: '-0.1px', lineHeight: '1.2' }}>
                      {isIntro ? b.title.replace(/^\d+\.\d+\s+/, '') : b.title}
                    </strong>
                    <p style={{ fontSize: '1.04rem', lineHeight: '1.65', color: 'var(--ifm-color-emphasis-700)', textAlign: 'justify', margin: 0 }}>
                      {renderMixedMathText(b.content)}
                    </p>
                  </div>
                ))}
              </div>
            </div>

            {/* Analogy & Read Link Box */}
            <div style={{ display: 'flex', gap: '1rem', justifyContent: 'space-between', alignItems: 'center', background: 'rgba(46, 133, 85, 0.03)', border: '1px solid var(--ifm-color-emphasis-300)', borderRadius: '8px', padding: '0.8rem 1rem' }}>
              <div style={{ flex: 1 }}>
                <span style={{ display: 'block', fontSize: '0.85rem', fontWeight: 'bold', color: 'var(--ifm-color-primary-light)', textTransform: 'uppercase', letterSpacing: '0.5px', marginBottom: '0.1rem' }}>
                  💡 Intuitive Analogy
                </span>
                <span style={{ display: 'block', fontSize: '1.02rem', color: 'var(--ifm-color-emphasis-700)', lineHeight: '1.5', textAlign: 'justify' }}>
                  {ch.analogy}
                </span>
              </div>
              <div style={{ display: 'flex', flexShrink: 0 }}>
                <Link to={ch.link} className="qbd-read-more-btn" style={{ fontSize: '0.95rem', padding: '0.4rem 0.9rem' }}>
                  {isIntro ? 'Read Intro' : 'Read Chapter'} &rarr;
                </Link>
              </div>
            </div>

          </div>

          {/* RIGHT COLUMN: visual interactive blocks (39% width) */}
          <div className="qbd-col-right" style={{ flex: '0 0 39%', maxWidth: '39%', width: '39%', display: 'flex', flexDirection: 'column', gap: '1.5rem', boxSizing: 'border-box' }}>
            
            {/* 1. Topological Schematic diagram (renders directly, no sub-header) */}
            <ConceptualVisualBox 
              num={ch.num} 
              onEnlarge={() => setActiveDiagramNum(ch.num)}
            />

            {/* 2. Physics Simulator Sandbox */}
            {ch.sandbox && (
              <div style={{
                backgroundColor: 'rgba(0, 0, 0, 0.25)',
                borderRadius: '16px',
                padding: '1.2rem',
                boxShadow: 'inset 0 4px 20px rgba(0,0,0,0.15)',
                border: '1px solid rgba(255, 255, 255, 0.02)',
                display: 'flex',
                flexDirection: 'column',
                gap: '0.8rem',
                overflow: 'hidden'
              }}>
                <div style={{ height: '180px', display: 'flex', alignItems: 'center', justifyContent: 'center', position: 'relative' }}>
                  {ch.sandbox === 'lightcone' && (
                    <LightConeSandbox hoveredNode={hoveredNode} setHoveredNode={setHoveredNode} />
                  )}
                  {ch.sandbox === 'braid' && (
                    <BraidAnimator braidType={braidType} setBraidType={setBraidType} />
                  )}
                  {ch.sandbox === 'curvature' && (
                    <CurvatureWarp warpStrength={warpStrength} setWarpStrength={setWarpStrength} />
                  )}
                  {ch.sandbox === 'timeline' && (
                    <TimelineSandbox timelineIndex={timelineIndex} setTimelineIndex={setTimelineIndex} timelineEvents={timelineEvents} />
                  )}
                  {ch.sandbox === 'selection' && (
                    <SelectionSandbox selectionStability={selectionStability} setSelectionStability={setSelectionStability} />
                  )}
                </div>
                <span style={{ display: 'block', fontSize: '0.76rem', color: 'rgba(255, 255, 255, 0.8)', fontStyle: 'italic', lineHeight: '1.4', textAlign: 'justify' }}>
                  <strong>Interactive Sandbox:</strong> Real-time physics engine simulation.
                </span>
              </div>
            )}

            {/* 3. Physics Graph */}
            {!ch.sandbox && ch.image && (
              <div 
                onClick={() => setLightbox(ch.image || null)}
                style={{
                  backgroundColor: 'rgba(0, 0, 0, 0.25)',
                  borderRadius: '16px',
                  padding: '1.2rem',
                  boxShadow: 'inset 0 4px 20px rgba(0,0,0,0.15)',
                  border: '1px solid rgba(255, 255, 255, 0.02)',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '0.8rem',
                  overflow: 'hidden',
                  cursor: 'zoom-in'
                }}
              >
                <div style={{ height: '140px', display: 'flex', alignItems: 'center', justifyContent: 'center', position: 'relative' }}>
                  <img 
                    src={ch.image.src} 
                    alt={ch.image.alt}
                    style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain', borderRadius: '4px' }}
                  />
                </div>
                <span style={{ display: 'block', fontSize: '0.76rem', color: 'rgba(255, 255, 255, 0.8)', fontStyle: 'italic', lineHeight: '1.4', textAlign: 'justify' }}>
                  <strong>Cosmological Graph:</strong> Observational projections.
                </span>
              </div>
            )}

            {/* 4. Important Definitions */}
            {ch.definitions && ch.definitions.length > 0 && (
              <ImportantDefinitionsBox definitions={ch.definitions} />
            )}

            {/* 5. Historical Connections Callout */}
            {ch.historicalCallout && (
              <HistoricalCallout title={ch.historicalCallout.title}>
                {ch.historicalCallout.text}
              </HistoricalCallout>
            )}

            {/* 6. Specialist Takeaways */}
            <div style={{ marginTop: '0.4rem', borderTop: '1px solid var(--ifm-color-emphasis-200)', paddingTop: '0.8rem' }}>
              <h3 style={{ fontSize: '1.1rem', fontWeight: 'bold', color: 'var(--ifm-color-primary)', textTransform: 'uppercase', letterSpacing: '0.8px', marginBottom: '0.6rem' }}>
                Takeaways for Specialists
              </h3>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '0.6rem' }}>
                {ch.specialists.map((s, sIdx) => (
                  <div key={sIdx} style={{ fontSize: '0.95rem', lineHeight: '1.5', color: 'var(--ifm-color-emphasis-700)' }}>
                    <strong style={{ color: 'var(--ifm-color-emphasis-950)' }}>• {s.area}: </strong>
                    <span>{s.text}</span>
                  </div>
                ))}
              </div>
            </div>

          </div>

        </div>

      </div>
    );
  };

  return (
<Layout
      title="QBD Summary Atlas: The Source Code of Cosmic Evolution"
      description="Mapping a Fault-Tolerant, Self-Compiling Universe. This interactive atlas decomposes the 25-chapter mechanics of a background-independent cosmos. Discover a framework where local network rewrites act as universal quantum gates, the vacuum executes a self-repairing stabilizer code, and gravity emerges naturally as the entropic drag of information processing.">
      
      <Head>
        <meta name="robots" content="index, follow" />
        <meta name="description" content="Mapping a Fault-Tolerant, Self-Compiling Universe. This interactive atlas decomposes the 25-chapter mechanics of a background-independent cosmos. Discover a framework where local network rewrites act as universal quantum gates, the vacuum executes a self-repairing stabilizer code, and gravity emerges naturally as the entropic drag of information processing." />
        <meta property="og:title" content="Quantum Braid Dynamics | The Source Code of Cosmic Evolution" />
        <meta property="og:description" content="Mapping a Fault-Tolerant, Self-Compiling Universe. This interactive atlas decomposes the 25-chapter mechanics of a background-independent cosmos. Discover a framework where local network rewrites act as universal quantum gates, the vacuum executes a self-repairing stabilizer code, and gravity emerges naturally as the entropic drag of information processing." />
        <meta name="twitter:title" content="Quantum Braid Dynamics | The Source Code of Cosmic Evolution" />
        <meta name="twitter:description" content="Mapping a Fault-Tolerant, Self-Compiling Universe. This interactive atlas decomposes the 25-chapter mechanics of a background-independent cosmos. Discover a framework where local network rewrites act as universal quantum gates, the vacuum executes a self-repairing stabilizer code, and gravity emerges naturally as the entropic drag of information processing." />
      </Head>

      <main style={{ padding: '2rem 0 6rem 0', position: 'relative', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
        
        {/* Ambient Glowing Radial Backdrops */}
        <div style={{
          position: 'absolute',
          top: '-10%',
          left: '5%',
          width: '600px',
          height: '600px',
          background: 'radial-gradient(circle, var(--qbd-glow-color) 0%, transparent 70%)',
          pointerEvents: 'none',
          zIndex: 0
        }} />
        <div style={{
          position: 'absolute',
          bottom: '5%',
          right: '5%',
          width: '600px',
          height: '600px',
          background: 'radial-gradient(circle, var(--qbd-glow-color) 0%, transparent 70%)',
          pointerEvents: 'none',
          zIndex: 0
        }} />

        <div className="container" style={{ position: 'relative', zIndex: 1, maxWidth: '1280px', display: 'flex', flexDirection: 'column', padding: '0 1rem' }}>
          
          <style dangerouslySetInnerHTML={{ __html: `
            :root {
              --qbd-sidebar-active-bg: rgba(46, 133, 85, 0.06);
              --qbd-sidebar-hover-bg: rgba(46, 133, 85, 0.03);
              --qbd-pulse-color: rgba(46, 133, 85, 0.5);
            }
            [data-theme='dark'] {
              --qbd-sidebar-active-bg: rgba(37, 194, 160, 0.08);
              --qbd-sidebar-hover-bg: rgba(37, 194, 160, 0.04);
              --qbd-pulse-color: rgba(37, 194, 160, 0.5);
            }

            /* Responsive Dashboard Flex Layout */
            .qbd-dashboard-container {
              display: flex;
              flex-direction: column;
              width: 100%;
              flex-grow: 1;
            }

            /* Premium Hover Zoomable Card classes */
            .qbd-zoomable-visual-card {
              background: rgba(255, 255, 255, 0.01);
              border: 1px solid var(--ifm-color-emphasis-300);
              border-radius: 12px;
              padding: 0.4rem;
              transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease, border-color 0.25s ease;
              overflow: hidden;
              cursor: zoom-in;
              display: flex;
              align-items: center;
              justify-content: center;
              width: 100%;
              height: 100%;
              box-sizing: border-box;
            }
            .qbd-zoomable-visual-card:hover {
              transform: scale(1.015) translateY(-1px);
              border-color: var(--ifm-color-primary);
              box-shadow: 0 6px 15px rgba(37, 194, 160, 0.06);
            }
            .qbd-zoomable-visual-card img, .qbd-zoomable-visual-card svg {
              transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
              max-width: 100%;
              max-height: 100%;
              object-fit: contain;
            }
            .qbd-zoomable-visual-card:hover img, .qbd-zoomable-visual-card:hover svg {
              transform: scale(1.025);
            }

            /* Widescreen Dashboard Card */
            .qbd-dashboard-card {
              background: rgba(255, 255, 255, 0.005);
              border: 1px solid var(--ifm-color-emphasis-300);
              border-radius: 16px;
              padding: 1.5rem;
              display: flex;
              flex-direction: column;
              box-shadow: 0 4px 20px rgba(0,0,0,0.02);
              box-sizing: border-box;
              margin-bottom: 3rem;
            }
            [data-theme='dark'] .qbd-dashboard-card {
              background: rgba(255, 255, 255, 0.015);
              border-color: rgba(255, 255, 255, 0.08);
            }

            /* Read more button */
            .qbd-read-more-btn {
              font-weight: 800;
              background-color: transparent !important;
              border: 1.5px solid var(--ifm-color-primary) !important;
              border-radius: 6px !important;
              color: var(--ifm-color-primary) !important;
              padding: 0.25rem 0.6rem !important;
              font-size: 0.74rem !important;
              text-decoration: none !important;
              transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.2s ease, background-color 0.2s ease, color 0.2s ease !important;
              display: inline-flex !important;
              align-items: center !important;
              gap: 0.3rem !important;
              cursor: pointer !important;
            }
            .qbd-read-more-btn:hover {
              background-color: var(--ifm-color-primary) !important;
              color: #ffffff !important;
              border-color: var(--ifm-color-primary) !important;
              transform: scale(1.03) translateY(-0.5px) !important;
            }

            @media screen and (max-width: 996px) {
              .qbd-widescreen-splitter {
                flex-direction: column !important;
                gap: 2rem !important;
              }
              .qbd-col-left, .qbd-col-right {
                width: 100% !important;
                max-width: 100% !important;
                flex: 1 1 auto !important;
              }
            }
          `}} />

          {/* MAIN PAGE HEADER */}
          <div style={{ textAlign: 'center', marginBottom: '4rem', zIndex: 10 }}>
            <h1 style={{ 
              fontSize: '3.4rem', 
              fontWeight: '900', 
              marginBottom: '1rem', 
              letterSpacing: '-1.5px',
              lineHeight: '1.1',
              color: 'var(--ifm-font-color-base)'
            }}>
              Quantum Braid Dynamics: <br />
              <span style={{ color: 'var(--ifm-color-primary)', fontStyle: 'italic', fontWeight: '400' }}>A Computational Process</span>
            </h1>
            <div style={{ width: '80px', height: '4px', backgroundColor: 'var(--ifm-color-primary)', margin: '1.5rem auto' }}></div>
            <p style={{ 
              fontSize: '1.25rem', 
              color: 'var(--ifm-color-emphasis-800)', 
              lineHeight: '1.7',
              textAlign: 'center',
              maxWidth: '850px',
              margin: '0 auto'
            }}>
              This interactive atlas introduces the mechanics of a background-independent cosmos. Discover a framework where local network rewrites act as universal quantum gates, the vacuum executes a self-repairing stabilizer code, and gravity emerges naturally as the entropic drag of information processing.
            </p>
          </div>

          {/* PARTS & CHAPTERS STREAM */}
          <div className="qbd-dashboard-container">
            
            {/* 1. INTRODUCTION (Chapter 0: Roots) rendered at the absolute top of the page */}
            {chapters.find(c => c.num === 0) && renderChapterCard(chapters.find(c => c.num === 0)!)}

            {/* 2. Parts stream starting with Part 1 Roadmap Panel */}
            {partsList.map((part, partIdx) => {
              // Filter out Chapter 0 from Part I chapters so it isn't rendered twice
              const partChapters = chapters.filter(
                c => c.num >= part.chStart && c.num <= part.chEnd && c.num !== 0
              );

              return (
                <div key={partIdx} style={{ marginBottom: '4rem' }}>
                  
                  {/* PART ROADMAP OVERVIEW HEADER CARD */}
                  <div style={{ marginBottom: '2.5rem' }}>
                    <PartPreviewPanel partIdx={partIdx} />
                  </div>

                  {/* CHAPTER CARDS UNDER THIS PART */}
                  {partChapters.map((ch) => renderChapterCard(ch))}

                </div>
              );
            })}
          </div>
        </div>
      </main>

      {/* UNIFIED MINIMALIST GLASSMORPHIC LIGHTBOX FOR IMAGES */}
      {lightbox && (
        <div 
          onClick={() => setLightbox(null)}
          style={{
            position: 'fixed',
            top: 0,
            left: 0,
            width: '100vw',
            height: '100vh',
            backgroundColor: 'rgba(4, 5, 6, 0.98)',
            backdropFilter: 'blur(30px)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            zIndex: 99999,
            cursor: 'zoom-out',
            animation: 'fadeIn 0.2s ease-out'
          }}
        >
          <button 
            onClick={() => setLightbox(null)}
            style={{
              position: 'absolute',
              top: '30px',
              right: '40px',
              backgroundColor: 'rgba(255, 255, 255, 0.08)',
              border: '1px solid rgba(255, 255, 255, 0.2)',
              borderRadius: '30px',
              padding: '0.6rem 1.5rem',
              color: '#ffffff',
              fontSize: '0.9rem',
              fontWeight: 'bold',
              cursor: 'pointer',
              boxShadow: '0 4px 20px rgba(0,0,0,0.5)',
              transition: 'all 0.2s',
              zIndex: 100000
            }}
          >
            ✕ Close Viewport
          </button>
          <div 
            onClick={() => setLightbox(null)}
            style={{
              width: '95vw',
              height: '90vh',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              position: 'relative',
              cursor: 'default'
            }}
          >
            <div 
              onClick={(e) => e.stopPropagation()} 
              style={{ 
                width: '100%', 
                height: '100%', 
                display: 'flex', 
                alignItems: 'center', 
                justifyContent: 'center' 
              }}
            >
              <img 
                src={lightbox.src} 
                alt={lightbox.alt} 
                style={{
                  maxHeight: '85%',
                  maxWidth: '90%',
                  objectFit: 'contain',
                  borderRadius: '12px',
                  border: '1px solid rgba(255, 255, 255, 0.1)',
                  boxShadow: '0 20px 50px rgba(0,0,0,0.6)'
                }}
              />
            </div>
          </div>
        </div>
      )}

      {/* MINIMALIST FULLSCREEN GLASSMORPHIC LIGHTBOX FOR VECTOR DIAGRAMS */}
      {activeDiagramNum !== null && (
        <div 
          onClick={() => setActiveDiagramNum(null)}
          style={{
            position: 'fixed',
            top: 0,
            left: 0,
            width: '100vw',
            height: '100vh',
            backgroundColor: 'rgba(4, 5, 6, 0.98)',
            backdropFilter: 'blur(30px)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            zIndex: 99999,
            cursor: 'zoom-out',
            animation: 'fadeIn 0.2s ease-out'
          }}
        >
          <button 
            onClick={() => setActiveDiagramNum(null)}
            style={{
              position: 'absolute',
              top: '30px',
              right: '40px',
              backgroundColor: 'rgba(255, 255, 255, 0.08)',
              border: '1px solid rgba(255, 255, 255, 0.2)',
              borderRadius: '30px',
              padding: '0.6rem 1.5rem',
              color: '#ffffff',
              fontSize: '0.9rem',
              fontWeight: 'bold',
              cursor: 'pointer',
              boxShadow: '0 4px 20px rgba(0,0,0,0.5)',
              transition: 'all 0.2s',
              zIndex: 100000
            }}
          >
            ✕ Close Viewport
          </button>
          <div 
            onClick={() => setActiveDiagramNum(null)}
            style={{
              width: '95vw',
              height: '90vh',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              position: 'relative',
              cursor: 'default'
            }}
          >
            <div 
              className="qbd-modal-svg-wrapper"
              onClick={(e) => e.stopPropagation()} 
              style={{ 
                width: '100%', 
                height: '100%', 
                display: 'flex', 
                alignItems: 'center', 
                justifyContent: 'center' 
              }}
            >
              <style dangerouslySetInnerHTML={{ __html: `
                .qbd-modal-svg-wrapper svg {
                  width: 95% !important;
                  height: auto !important;
                  max-height: 85% !important;
                  display: block;
                  margin: 0 auto;
                  max-width: 1000px;
                }
              `}} />
              <ConceptualVisualBox num={activeDiagramNum} hideChrome={true} />
            </div>
          </div>
        </div>
      )}
    </Layout>
  );
}

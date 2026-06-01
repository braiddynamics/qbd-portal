import React from 'react';
import { IllustrationRegistry } from './illustrations';

// Custom Important Definitions Box (Glossary for Non-Experts)
export const ImportantDefinitionsBox: React.FC<{
  definitions: { term: string; definition: string }[];
}> = ({ definitions }) => (
  <div style={{
    backgroundColor: 'rgba(255, 255, 255, 0.02)',
    border: '1px solid var(--ifm-color-emphasis-300)',
    borderRadius: '16px',
    padding: '1.2rem 1.4rem',
    fontSize: '0.88rem',
    lineHeight: '1.6',
    color: 'var(--ifm-color-emphasis-800)',
    boxShadow: '0 6px 20px rgba(0, 0, 0, 0.04)',
    margin: '0.4rem 0 0.8rem 0'
  }}>
    <h4 style={{ 
      margin: '0 0 0.8rem 0', 
      fontSize: '1.1rem', 
      fontWeight: '900', 
      textTransform: 'uppercase', 
      letterSpacing: '1.2px',
      color: 'var(--ifm-color-primary)',
      borderBottom: '1px solid var(--ifm-color-emphasis-300)',
      paddingBottom: '0.5rem',
      display: 'flex',
      alignItems: 'center',
      gap: '0.4rem'
    }}>
      <span>📖</span> Key Chapter Definitions
    </h4>
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      {definitions.map((d, idx) => (
        <div key={idx} style={{ borderBottom: idx < definitions.length - 1 ? '1px dashed rgba(255,255,255,0.04)' : 'none', paddingBottom: idx < definitions.length - 1 ? '0.8rem' : '0' }}>
          <strong style={{ 
            display: 'block', 
            fontSize: '1.08rem', 
            color: 'var(--ifm-color-emphasis-950)',
            marginBottom: '0.25rem'
          }}>
            {d.term}
          </strong>
          <span style={{ color: 'var(--ifm-color-emphasis-700)', fontSize: '1.02rem' }}>
            {d.definition}
          </span>
        </div>
      ))}
    </div>
  </div>
);

// Custom Historical Connections Callout (Zeno-like Callout)
export const HistoricalCallout: React.FC<{ title: string; children: React.ReactNode }> = ({ title, children }) => (
  <div style={{
    borderLeft: '4px solid var(--qbd-spine-color)',
    backgroundColor: 'rgba(139, 92, 246, 0.03)',
    padding: '1rem 1.2rem',
    borderRadius: '0 12px 12px 0',
    margin: '0.4rem 0 0.8rem 0',
    fontSize: '1.02rem',
    lineHeight: '1.6',
    color: 'var(--ifm-color-emphasis-700)',
    boxShadow: '0 2px 10px rgba(0,0,0,0.02)'
  }}>
    <strong style={{ display: 'block', marginBottom: '0.5rem', color: 'var(--ifm-color-emphasis-900)' }}>
      📜 {title}
    </strong>
    {children}
  </div>
);

// Conceptual Visual Box with highly detailed, explanatory SVG graphics for all 25 chapters
export const ConceptualVisualBox: React.FC<{ 
  num: number; 
  onEnlarge?: () => void; 
  hideChrome?: boolean; 
}> = ({ num, onEnlarge, hideChrome }) => {
  const Illustration = IllustrationRegistry[num];

  const renderVisualIllustration = () => {
    if (!Illustration) return null;
    return <Illustration />;
  };

  if (hideChrome) {
    return (
      <div style={{ width: '100%', height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        {renderVisualIllustration()}
      </div>
    );
  }

  return (
    <div style={{
      backgroundColor: 'rgba(255, 255, 255, 0.02)',
      border: '1px solid var(--ifm-color-emphasis-300)',
      borderRadius: '16px',
      padding: '1.2rem 1.4rem',
      marginBottom: '0.8rem',
      boxShadow: '0 6px 20px rgba(0, 0, 0, 0.04)',
      display: 'flex',
      flexDirection: 'column',
      gap: '0.8rem',
      overflow: 'hidden'
    }}>
      <div 
        onClick={onEnlarge}
        style={{ 
          backgroundColor: '#0f172a', 
          borderRadius: '12px', 
          padding: '0.6rem', 
          border: '1px solid rgba(255, 255, 255, 0.08)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          cursor: onEnlarge ? 'zoom-in' : 'default',
          position: 'relative',
          transition: 'all 0.2s',
          height: '180px',
          width: '100%',
          boxSizing: 'border-box'
        }}
        title={onEnlarge ? "Click to Enlarge Diagram" : undefined}
      >
        <div style={{ width: '100%', height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          {renderVisualIllustration()}
        </div>
        {onEnlarge && (
          <div style={{
            position: 'absolute',
            bottom: '8px',
            right: '8px',
            backgroundColor: 'rgba(0,0,0,0.6)',
            color: '#fff',
            borderRadius: '4px',
            padding: '2px 6px',
            fontSize: '0.68rem',
            fontWeight: 'bold',
            pointerEvents: 'none'
          }}>
            🔍 Click to Enlarge
          </div>
        )}
      </div>
      <span style={{ 
        display: 'block', 
        fontSize: '0.95rem', 
        color: 'var(--ifm-color-emphasis-700)', 
        fontStyle: 'italic', 
        lineHeight: '1.4',
        textAlign: 'justify'
      }}>
        <strong>Visual Schematic {num}.A:</strong> Labeled pre-geometric topological models and computational mechanisms of QBD.
      </span>
    </div>
  );
};

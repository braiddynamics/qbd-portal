import React, { useState } from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import Head from '@docusaurus/Head';
import downloadsInfo from '../../data/ai-downloads-info.json';

// Helper formatters
const formatSize = (bytes: number) => {
  if (!bytes) return '0 B';
  if (bytes < 1024) return `${bytes} B`;
  const kb = bytes / 1024;
  if (kb < 1024) return `${kb.toFixed(1)} KB`;
  const mb = kb / 1024;
  return `${mb.toFixed(2)} MB`;
};

const formatTokens = (tokens: number) => {
  if (!tokens) return '0';
  return tokens.toLocaleString();
};

export default function DownloadPage() {
  const [activeTab, setActiveTab] = useState<'chapters' | 'parts' | 'full' | 'codebase'>('chapters');

  return (
    <Layout
      title="Monograph Downloads"
      description="Download the Quantum Braid Dynamics Monograph in various formats: publication PDF, clean plain text Markdown, structured JSON database, or separate parts and chapters.">
      
      <Head>
        <meta name="robots" content="index, follow" />
        <meta property="og:title" content="Monograph Downloads | Quantum Braid Dynamics" />
        <meta name="twitter:title" content="Monograph Downloads | Quantum Braid Dynamics" />
      </Head>

      <main className="downloads-page">

        {/* Glow Backdrop */}
        <div style={{
          position: 'absolute',
          top: '-10%',
          left: '20%',
          width: '500px',
          height: '500px',
          background: 'radial-gradient(circle, var(--qbd-glow-color) 0%, transparent 70%)',
          pointerEvents: 'none',
          zIndex: 0
        }} />
        <div style={{
          position: 'absolute',
          bottom: '-10%',
          right: '20%',
          width: '500px',
          height: '500px',
          background: 'radial-gradient(circle, var(--qbd-glow-color) 0%, transparent 70%)',
          pointerEvents: 'none',
          zIndex: 0
        }} />

        <div className="container" style={{ position: 'relative', zIndex: 1, maxWidth: '1100px' }}>

          {/* Header */}
          <div style={{ textAlign: 'center', marginBottom: '3rem' }}>
            <span style={{
              fontSize: '0.88rem',
              fontWeight: 'bold',
              textTransform: 'uppercase',
              color: 'var(--ifm-color-primary)',
              letterSpacing: '2px',
              display: 'inline-block',
              marginBottom: '0.5rem'
            }}>
              Quantum Braid Dynamics Portal
            </span>
            <h1 className="downloads-header-title">
              Monograph Download Repository
            </h1>
            <p className="downloads-header-lead">
              Access the complete manuscript, theorem databases, and derivations. Available in copy-paste friendly Markdown, structured JSON, premium LaTeX-typeset PDF, or modular chapter slices.
            </p>
          </div>

          {/* Quick Selection Tab Bar */}
          <div className="downloads-tabs">
            {(
              [
                { id: 'chapters', label: 'Chapters' },
                { id: 'parts', label: 'Parts' },
                { id: 'full', label: 'Full Book' },
                { id: 'codebase', label: 'Codebase' },
              ] as const
            ).map((tab) => (
              <button
                type="button"
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`downloads-tab-btn ${activeTab === tab.id ? 'active' : ''}`}
              >
                {tab.label}
              </button>
            ))}
          </div>

          {/* TAB 1: BY CHAPTER FORMATS */}
          {activeTab === 'chapters' && (
            <div>
              <div className="downloads-grid-chapters">
                {downloadsInfo.chapters.map((ch, idx) => {
                  return (
                    <div key={idx} className="qbd-interactive-card" style={{ padding: '1.5rem' }}>
                      <div className="qbd-interactive-card-content" style={{ display: 'flex', flexDirection: 'column', height: '100%', justifyContent: 'space-between' }}>
                        <div>
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
                            <span style={{ fontSize: '0.8rem', fontWeight: 'bold', color: 'var(--ifm-color-emphasis-500)' }}>
                              Chapter {ch.chapter_number}
                            </span>
                          </div>
                          <h4 style={{ fontSize: '1.1rem', fontWeight: '800', margin: '0 0 1rem 0', lineHeight: '1.3' }}>
                            {ch.name.replace(/Chapter \d+:\s*/, '')}
                          </h4>
                        </div>

                        <div style={{ borderTop: '1px solid var(--ifm-color-emphasis-100)', paddingTop: '1rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: '0.75rem', flexWrap: 'wrap' }}>
                          <div style={{ fontSize: '0.8rem', color: 'var(--ifm-color-emphasis-600)' }}>
                            <div>{formatSize(ch.file_size_bytes)}</div>
                            <div>{formatTokens(ch.estimated_tokens)} tokens</div>
                          </div>
                          
                          <div style={{ display: 'flex', gap: '0.4rem', flexWrap: 'wrap' }}>
                            <a href={ch.url} download className="button button--sm btn-download-md" style={{ padding: '0.4rem 0.6rem', display: 'flex', alignItems: 'center', gap: '0.3rem' }}>
                              <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                              Get MD
                            </a>
                            {ch.json_url && (
                              <a href={ch.json_url} download className="button button--sm btn-download-json" style={{ padding: '0.4rem 0.6rem', display: 'flex', alignItems: 'center', gap: '0.3rem' }}>
                                <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                                Get JSON
                              </a>
                            )}
                            {ch.pdf_url && (
                              <a href={ch.pdf_url} download className="button button--sm btn-download-pdf" style={{ padding: '0.4rem 0.6rem', display: 'flex', alignItems: 'center', gap: '0.3rem' }}>
                                <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                                Get PDF
                              </a>
                            )}
                          </div>
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          )}


          {/* TAB 2: BY PART FORMATS */}
          {activeTab === 'parts' && (
            <div className="downloads-grid-parts">
              {downloadsInfo.parts.map((part, idx) => (
                <div key={idx} className="qbd-interactive-card" style={{ padding: '1.75rem' }}>
                  <div className="qbd-interactive-card-content" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: '1.5rem', flexWrap: 'wrap' }}>
                    <div style={{ flex: '1', minWidth: 'min(100%, 240px)' }}>
                      <span style={{ 
                        fontSize: '0.8rem', 
                        fontWeight: '800', 
                        color: 'var(--ifm-color-primary)', 
                        textTransform: 'uppercase',
                        letterSpacing: '0.5px' 
                      }}>
                        Part {part.part_number}
                      </span>
                      <h3 style={{ fontSize: '1.35rem', fontWeight: '800', margin: '0.2rem 0 0.5rem 0' }}>
                        {part.name.replace(/Part \d+:\s*/, '')}
                      </h3>
                      <p style={{ fontSize: '0.9rem', color: 'var(--ifm-color-emphasis-600)', lineHeight: '1.4', margin: '0 0 1rem 0' }}>
                        {part.part_number === 1 && "Chapters 1–5: Establishing spacetime substrates, topological causal axioms, and quantum equilibrium."}
                        {part.part_number === 2 && "Chapters 6–10: Formulating particle generations, gauge symmetries, and topological quantum computation."}
                        {part.part_number === 3 && "Chapters 11–17: Unifying continuous Einstein field equations, Lorentzian time, and holographic entanglements."}
                        {part.part_number === 4 && "Chapters 18–22: Numerical inflationary metrics, Big Bang nucleosynthesis, and dark sector lattice defects."}
                        {part.part_number === 5 && "Chapters 23–25: Exploring multiverse thermodynamics and cosmological selection criteria."}
                        {part.part_number === 6 && "Appendices: Citation libraries, simulation models, and the mathematical notation catalog."}
                      </p>
                      
                      <div style={{ display: 'flex', gap: '1.5rem', fontSize: '0.85rem' }}>
                        <div>
                          <span style={{ color: 'var(--ifm-color-emphasis-500)' }}>Size:</span>{' '}
                          <strong style={{ color: 'var(--ifm-color-emphasis-800)' }}>{formatSize(part.file_size_bytes)}</strong>
                        </div>
                        <div>
                          <span style={{ color: 'var(--ifm-color-emphasis-500)' }}>Tokens:</span>{' '}
                          <strong style={{ color: 'var(--ifm-color-emphasis-800)' }}>{formatTokens(part.estimated_tokens)}</strong>
                        </div>
                      </div>
                    </div>

                    <div className="downloads-part-actions">
                      <a href={part.url} download className="button button--sm btn-download-md" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.4rem', width: '100%' }}>
                        <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                        Get MD
                      </a>
                      {part.json_url && (
                        <a href={part.json_url} download className="button button--sm btn-download-json" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.4rem', width: '100%' }}>
                          <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                          Get JSON
                        </a>
                      )}
                      {part.pdf_url && (
                        <a href={part.pdf_url} download className="button button--sm btn-download-pdf" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.4rem', width: '100%' }}>
                          <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                          Get PDF
                        </a>
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}

          {/* TAB 3: FULL BOOK FORMATS */}
          {activeTab === 'full' && (
            <div className="downloads-grid-full">
              {downloadsInfo.full_book.map((file, idx) => (
                <div key={idx} className="qbd-interactive-card" style={{ padding: '2rem', display: 'flex', flexDirection: 'column', height: '100%' }}>
                  <div className="qbd-interactive-card-content" style={{ display: 'flex', flexDirection: 'column', height: '100%', justifyContent: 'space-between' }}>
                    <div>
                      {/* Format tag */}
                      <span style={{
                        fontSize: '0.75rem',
                        fontWeight: 'bold',
                        textTransform: 'uppercase',
                        backgroundColor: file.type === 'pdf' ? 'var(--qbd-badge-danger-bg)' : file.type === 'json' ? 'var(--qbd-badge-info-bg)' : 'var(--qbd-badge-success-bg)',
                        color: file.type === 'pdf' ? 'var(--qbd-badge-danger-text)' : file.type === 'json' ? 'var(--qbd-badge-info-text)' : 'var(--qbd-badge-success-text)',
                        border: file.type === 'pdf' ? '1px solid var(--qbd-badge-danger-border)' : file.type === 'json' ? '1px solid var(--qbd-badge-info-border)' : '1px solid var(--qbd-badge-success-border)',
                        padding: '0.25rem 0.6rem',
                        borderRadius: '6px',
                        display: 'inline-block',
                        marginBottom: '1rem'
                      }}>
                        {file.type}
                      </span>
                      <h3 style={{ fontSize: '1.5rem', fontWeight: '800', marginBottom: '0.75rem' }}>{file.name}</h3>
                      <p style={{ fontSize: '0.95rem', color: 'var(--ifm-color-emphasis-700)', lineHeight: '1.5', marginBottom: '1.5rem' }}>
                        {file.description}
                      </p>
                    </div>

                    <div style={{ borderTop: '1px solid var(--ifm-color-emphasis-200)', paddingTop: '1.5rem', marginTop: '1rem' }}>
                      {/* File specs */}
                      <div style={{ display: 'flex', gap: '2rem', marginBottom: '1.5rem' }}>
                        <div>
                          <div style={{ fontSize: '0.8rem', color: 'var(--ifm-color-emphasis-500)', textTransform: 'uppercase', fontWeight: 'bold' }}>File Size</div>
                          <div style={{ fontSize: '1.1rem', fontWeight: '800', color: 'var(--ifm-color-emphasis-900)' }}>{formatSize(file.file_size_bytes)}</div>
                        </div>
                        <div>
                          <div style={{ fontSize: '0.8rem', color: 'var(--ifm-color-emphasis-500)', textTransform: 'uppercase', fontWeight: 'bold' }}>Est. LLM Tokens</div>
                          <div style={{ fontSize: '1.1rem', fontWeight: '800', color: 'var(--ifm-color-emphasis-900)' }}>{formatTokens(file.estimated_tokens)}</div>
                        </div>
                      </div>
                      <a href={file.url} download className="button button--primary button--block button--lg" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}>
                        <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                        Download Source
                      </a>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}

          {/* TAB 4: CODEBASE MODULES */}
          {activeTab === 'codebase' && downloadsInfo.codebase && (
            <div>
              {/* Category 1: Python Physics Model */}
              <div style={{ marginBottom: '4rem' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '1.5rem', borderBottom: '1px solid var(--ifm-color-emphasis-200)', paddingBottom: '0.5rem' }}>
                  <span style={{ fontSize: '1.5rem' }}>⚡</span>
                  <h3 style={{ fontSize: '1.6rem', fontWeight: '800', margin: 0 }}>
                    Python Numerical Physics Engine
                  </h3>
                  <span style={{ fontSize: '0.8rem', fontWeight: 'bold', color: '#3b82f6', backgroundColor: 'rgba(59, 130, 246, 0.1)', padding: '0.2rem 0.5rem', borderRadius: '6px' }}>
                    {downloadsInfo.codebase.model.length} Modules
                  </span>
                </div>
                <p style={{ color: 'var(--ifm-color-emphasis-600)', fontSize: '1rem', marginBottom: '2rem', maxWidth: '800px' }}>
                  The core network simulation engine modeling topological braiding operations, causal set network setups, entanglement observables, and global error correcting codes.
                </p>
                <div className="downloads-grid-code">
                  {downloadsInfo.codebase.model.map((module, idx) => (
                    <div key={idx} className="qbd-interactive-card" style={{ padding: '1.5rem' }}>
                      <div className="qbd-interactive-card-content" style={{ display: 'flex', flexDirection: 'column', height: '100%', justifyContent: 'space-between' }}>
                        <div>
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
                            <span style={{ fontSize: '0.75rem', fontWeight: 'bold', color: '#3b82f6', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                              Python Class
                            </span>
                            <span style={{ fontSize: '0.8rem', color: 'var(--ifm-color-emphasis-500)' }}>
                              {formatSize(module.file_size_bytes)}
                            </span>
                          </div>
                          <h4 style={{ fontSize: '1.1rem', fontWeight: '800', margin: '0 0 0.75rem 0', fontFamily: 'monospace' }}>
                            {module.name}
                          </h4>
                          <p style={{ fontSize: '0.9rem', color: 'var(--ifm-color-emphasis-600)', lineHeight: '1.4', margin: '0 0 1rem 0' }}>
                            {module.description}
                          </p>
                        </div>
                        <div style={{ borderTop: '1px solid var(--ifm-color-emphasis-100)', paddingTop: '1rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: '0.5rem', flexWrap: 'wrap' }}>
                          <span style={{ fontSize: '0.8rem', color: 'var(--ifm-color-emphasis-550)' }}>
                            {formatTokens(module.estimated_tokens)} tokens
                          </span>
                          <div style={{ display: 'flex', gap: '0.4rem' }}>
                            <a href={module.url} download className="button button--sm btn-download-json" style={{ padding: '0.4rem 0.6rem', display: 'flex', alignItems: 'center', gap: '0.3rem', fontSize: '0.8rem' }}>
                              Get Code
                            </a>
                            <a href={`https://github.com/braiddynamics/qbd-portal/blob/main/code/model/${module.name}`} target="_blank" rel="noopener noreferrer" className="button button--sm button--secondary" style={{ padding: '0.4rem 0.6rem', display: 'flex', alignItems: 'center', gap: '0.3rem', fontSize: '0.8rem' }}>
                              GitHub
                            </a>
                          </div>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Category 2: Simulations & Solvers */}
              <div style={{ marginBottom: '4rem' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '1.5rem', borderBottom: '1px solid var(--ifm-color-emphasis-200)', paddingBottom: '0.5rem' }}>
                  <span style={{ fontSize: '1.5rem' }}>❄️</span>
                  <h3 style={{ fontSize: '1.6rem', fontWeight: '800', margin: 0 }}>
                    Solvers & Search Ensemble
                  </h3>
                  <span style={{ fontSize: '0.8rem', fontWeight: 'bold', color: '#ef4444', backgroundColor: 'rgba(239, 68, 68, 0.1)', padding: '0.2rem 0.5rem', borderRadius: '6px' }}>
                    {downloadsInfo.codebase.simulations.length} Modules
                  </span>
                </div>
                <p style={{ color: 'var(--ifm-color-emphasis-600)', fontSize: '1rem', marginBottom: '2rem', maxWidth: '800px' }}>
                  Simulated annealing path solvers searching for stable cosmological vacuum structures and multi-thread statistical ensemble coordinators.
                </p>
                <div className="downloads-grid-code">
                  {downloadsInfo.codebase.simulations.map((module, idx) => (
                    <div key={idx} className="qbd-interactive-card" style={{ padding: '1.5rem' }}>
                      <div className="qbd-interactive-card-content" style={{ display: 'flex', flexDirection: 'column', height: '100%', justifyContent: 'space-between' }}>
                        <div>
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
                            <span style={{ fontSize: '0.75rem', fontWeight: 'bold', color: '#ef4444', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                              Python Solver
                            </span>
                            <span style={{ fontSize: '0.8rem', color: 'var(--ifm-color-emphasis-500)' }}>
                              {formatSize(module.file_size_bytes)}
                            </span>
                          </div>
                          <h4 style={{ fontSize: '1.1rem', fontWeight: '800', margin: '0 0 0.75rem 0', fontFamily: 'monospace' }}>
                            {module.name}
                          </h4>
                          <p style={{ fontSize: '0.9rem', color: 'var(--ifm-color-emphasis-600)', lineHeight: '1.4', margin: '0 0 1rem 0' }}>
                            {module.description}
                          </p>
                        </div>
                        <div style={{ borderTop: '1px solid var(--ifm-color-emphasis-100)', paddingTop: '1rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: '0.5rem', flexWrap: 'wrap' }}>
                          <span style={{ fontSize: '0.8rem', color: 'var(--ifm-color-emphasis-550)' }}>
                            {formatTokens(module.estimated_tokens)} tokens
                          </span>
                          <div style={{ display: 'flex', gap: '0.4rem' }}>
                            <a href={module.url} download className="button button--sm btn-download-pdf" style={{ padding: '0.4rem 0.6rem', display: 'flex', alignItems: 'center', gap: '0.3rem', fontSize: '0.8rem' }}>
                              Get Code
                            </a>
                            <a href={`https://github.com/braiddynamics/qbd-portal/blob/main/code/simulations/${module.name}`} target="_blank" rel="noopener noreferrer" className="button button--sm button--secondary" style={{ padding: '0.4rem 0.6rem', display: 'flex', alignItems: 'center', gap: '0.3rem', fontSize: '0.8rem' }}>
                              GitHub
                            </a>
                          </div>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Category 3: Lean 4 Proof Suite */}
              <div style={{ marginBottom: '4rem' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '1.5rem', borderBottom: '1px solid var(--ifm-color-emphasis-200)', paddingBottom: '0.5rem' }}>
                  <span style={{ fontSize: '1.5rem' }}>💎</span>
                  <h3 style={{ fontSize: '1.6rem', fontWeight: '800', margin: 0 }}>
                    Lean 4 Formal Proof Suite
                  </h3>
                  <span style={{ fontSize: '0.8rem', fontWeight: 'bold', color: 'var(--ifm-color-primary)', backgroundColor: 'var(--qbd-accent-soft)', padding: '0.2rem 0.5rem', borderRadius: '6px' }}>
                    {downloadsInfo.codebase.lean.length} Modules
                  </span>
                </div>
                <p style={{ color: 'var(--ifm-color-emphasis-600)', fontSize: '1rem', marginBottom: '2rem', maxWidth: '800px' }}>
                  Mathematical sanity audits formalizing the core axioms of spacetime primitives, comonadic background independence, and stabilizer code isomorphisms under causal consistency.
                </p>
                <div className="downloads-grid-code">
                  {downloadsInfo.codebase.lean.map((module, idx) => (
                    <div key={idx} className="qbd-interactive-card" style={{ padding: '1.5rem' }}>
                      <div className="qbd-interactive-card-content" style={{ display: 'flex', flexDirection: 'column', height: '100%', justifyContent: 'space-between' }}>
                        <div>
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
                            <span style={{ fontSize: '0.75rem', fontWeight: 'bold', color: '#10b981', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                              Lean 4 Source
                            </span>
                            <span style={{ fontSize: '0.8rem', color: 'var(--ifm-color-emphasis-500)' }}>
                              {formatSize(module.file_size_bytes)}
                            </span>
                          </div>
                          <h4 style={{ fontSize: '1.1rem', fontWeight: '800', margin: '0 0 0.75rem 0', fontFamily: 'monospace' }}>
                            {module.name}
                          </h4>
                          <p style={{ fontSize: '0.9rem', color: 'var(--ifm-color-emphasis-600)', lineHeight: '1.4', margin: '0 0 1rem 0' }}>
                            {module.description}
                          </p>
                        </div>
                        <div style={{ borderTop: '1px solid var(--ifm-color-emphasis-100)', paddingTop: '1rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: '0.5rem', flexWrap: 'wrap' }}>
                          <span style={{ fontSize: '0.8rem', color: 'var(--ifm-color-emphasis-550)' }}>
                            {formatTokens(module.estimated_tokens)} tokens
                          </span>
                          <div style={{ display: 'flex', gap: '0.4rem' }}>
                            <a href={module.url} download className="button button--sm btn-download-md" style={{ padding: '0.4rem 0.6rem', display: 'flex', alignItems: 'center', gap: '0.3rem', fontSize: '0.8rem' }}>
                              Get Code
                            </a>
                            <a href={`https://github.com/braiddynamics/qbd-portal/blob/main/code/repo/lean/${module.name}`} target="_blank" rel="noopener noreferrer" className="button button--sm button--secondary" style={{ padding: '0.4rem 0.6rem', display: 'flex', alignItems: 'center', gap: '0.3rem', fontSize: '0.8rem' }}>
                              GitHub
                            </a>
                          </div>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Category 4: Python Simulations Repository */}
              <div style={{ marginBottom: '4rem' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '1.5rem', borderBottom: '1px solid var(--ifm-color-emphasis-200)', paddingBottom: '0.5rem' }}>
                  <span style={{ fontSize: '1.5rem' }}>📦</span>
                  <h3 style={{ fontSize: '1.6rem', fontWeight: '800', margin: 0 }}>
                    Python Simulations Repository (/repo/)
                  </h3>
                  <span style={{ fontSize: '0.8rem', fontWeight: 'bold', color: '#3b82f6', backgroundColor: 'rgba(59, 130, 246, 0.1)', padding: '0.2rem 0.5rem', borderRadius: '6px' }}>
                    {downloadsInfo.codebase.repo.length} Modules
                  </span>
                </div>
                <p style={{ color: 'var(--ifm-color-emphasis-600)', fontSize: '1rem', marginBottom: '2rem', maxWidth: '800px' }}>
                  An extensive database of {downloadsInfo.codebase?.repo?.length || 138} compact numerical simulation scripts. Each module corresponds to a specific theorem, equation, or derivation section from the monograph, allowing step-by-step mathematical audits.
                </p>

                {/* Featured ZIP Download Card & GitHub Row */}
                {downloadsInfo.codebase.repo_zip && (
                  <div className="qbd-interactive-card" style={{ padding: '2rem', marginBottom: '2rem' }}>
                    <div className="qbd-interactive-card-content" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: '2rem', flexWrap: 'wrap' }}>
                      <div style={{ flex: '1', minWidth: '280px' }}>
                        <span style={{ fontSize: '0.75rem', fontWeight: 'bold', color: '#10b981', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                          Simulations Archive
                        </span>
                        <h4 style={{ fontSize: '1.4rem', fontWeight: '800', margin: '0.2rem 0 0.5rem 0' }}>
                          Complete Simulations Repository Bundle (ZIP)
                        </h4>
                        <p style={{ fontSize: '0.95rem', color: 'var(--ifm-color-emphasis-600)', margin: '0 0 1rem 0' }}>
                          {downloadsInfo.codebase.repo_zip.description}
                        </p>
                        <div style={{ fontSize: '0.85rem' }}>
                          <span style={{ color: 'var(--ifm-color-emphasis-500)' }}>File Size:</span>{' '}
                          <strong style={{ color: 'var(--ifm-color-emphasis-800)' }}>{formatSize(downloadsInfo.codebase.repo_zip.file_size_bytes)}</strong>
                        </div>
                      </div>
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '0.6rem', minWidth: '160px' }}>
                        <a href={downloadsInfo.codebase.repo_zip.url} download className="button button--sm btn-download-md" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.4rem', width: '100%', padding: '0.5rem 1rem' }}>
                          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                          Download ZIP Archive
                        </a>
                        <a href="https://github.com/braiddynamics/qbd-portal/tree/main/code/repo/python" target="_blank" rel="noopener noreferrer" className="button button--sm button--secondary" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.4rem', width: '100%', padding: '0.5rem 1rem' }}>
                          View Folder on GitHub
                        </a>
                      </div>
                    </div>
                  </div>
                )}

                {/* Compact Scrollable File Explorer */}
                <div style={{ 
                  border: '1px solid var(--ifm-color-emphasis-200)', 
                  borderRadius: '12px', 
                  backgroundColor: 'var(--ifm-background-surface-color)', 
                  overflow: 'hidden' 
                }}>
                  <div style={{
                    backgroundColor: 'var(--qbd-surface-muted)',
                    padding: '0.75rem 1.25rem',
                    borderBottom: '1px solid var(--qbd-border-subtle)',
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center',
                    fontWeight: 'bold',
                    fontSize: '0.9rem',
                    color: 'var(--ifm-color-emphasis-700)'
                  }}>
                    <span>Numerical Derivation Module</span>
                    <span>Actions</span>
                  </div>

                  <div style={{ maxHeight: '380px', overflowY: 'auto', padding: '0.5rem 0' }}>
                    {downloadsInfo.codebase.repo.map((module, idx) => (
                      <div key={idx} className="downloads-repo-row" style={{
                        borderBottom: idx < downloadsInfo.codebase.repo.length - 1 ? '1px solid var(--qbd-border-subtle)' : 'none',
                      }}>
                        <div style={{ flex: 1, minWidth: 'min(100%, 220px)' }}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.2rem', flexWrap: 'wrap' }}>
                            <span style={{ color: 'var(--ifm-color-primary)', fontWeight: '800', fontFamily: 'monospace', fontSize: '0.95rem', wordBreak: 'break-all' }}>
                              {module.name}
                            </span>
                            <span style={{ fontSize: '0.75rem', color: 'var(--ifm-color-emphasis-450)' }}>
                              ({formatSize(module.file_size_bytes)} | {formatTokens(module.estimated_tokens)} tokens)
                            </span>
                          </div>
                          <div style={{ fontSize: '0.85rem', color: 'var(--ifm-color-emphasis-600)' }}>
                            {module.description}
                          </div>
                        </div>
                        <div style={{ display: 'flex', gap: '0.4rem' }}>
                          <a href={module.url} download className="button button--sm btn-download-json" style={{ padding: '0.3rem 0.6rem', fontSize: '0.8rem', display: 'flex', alignItems: 'center', gap: '0.3rem' }}>
                            Get Code
                          </a>
                          <a href={`https://github.com/braiddynamics/qbd-portal/blob/main/code/repo/python/${module.name}`} target="_blank" rel="noopener noreferrer" className="button button--sm button--secondary" style={{ padding: '0.3rem 0.6rem', fontSize: '0.8rem', display: 'flex', alignItems: 'center', gap: '0.3rem' }}>
                            GitHub
                          </a>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>

              {/* GitHub Contribution Panel */}
              <div className="qbd-interactive-card" style={{ padding: '3rem', marginTop: '5rem', textAlign: 'center' }}>
                <div className="qbd-interactive-card-content">
                  <h3 style={{ fontSize: '1.75rem', fontWeight: '800', marginBottom: '1rem' }}>
                    Explore & Contribute on GitHub
                  </h3>
                  <p style={{ color: 'var(--ifm-color-emphasis-700)', fontSize: '1.05rem', lineHeight: '1.6', maxWidth: '750px', margin: '0 auto 2rem auto' }}>
                    All Quantum Braid Dynamics (QBD) Lean proofs, numerical simulation algorithms, and theorem derivations are fully open-source. Help us audit Lean 4 proofs, expand simulations, or star our repository to support background-independent quantum gravity research.
                  </p>
                  <div style={{ display: 'flex', justifyContent: 'center', gap: '1rem', flexWrap: 'wrap' }}>
                    <a href="https://github.com/braiddynamics/qbd-portal" target="_blank" rel="noopener noreferrer" className="button button--lg btn-download-json" style={{ display: 'inline-flex', alignItems: 'center', gap: '0.5rem', padding: '0.75rem 2rem' }}>
                      <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
                      Browse Repository
                    </a>
                    <a href="https://github.com/braiddynamics/qbd-portal/issues" target="_blank" rel="noopener noreferrer" className="button button--lg btn-download-pdf" style={{ display: 'inline-flex', alignItems: 'center', gap: '0.5rem', padding: '0.75rem 2rem' }}>
                      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
                      Report Issues & Audits
                    </a>
                  </div>
                </div>
              </div>
            </div>
          )}

        </div>
      </main>
    </Layout>
  );
}

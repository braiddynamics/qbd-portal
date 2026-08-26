import React, { useState } from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import Head from '@docusaurus/Head';
import { papers } from '../../data/papers';

export default function PapersHub() {
  const [filter, setFilter] = useState<'all' | 'preprint' | 'working-paper' | 'comment'>('all');
  const [copiedId, setCopiedId] = useState<string | null>(null);
  const [activeBibtex, setActiveBibtex] = useState<string | null>(null);

  // Sort by publishing date descending (most recent at top)
  const sortedRecords = [...papers].sort(
    (a, b) => new Date(b.dateISO).getTime() - new Date(a.dateISO).getTime()
  );

  const filteredRecords = filter === 'all' 
    ? sortedRecords 
    : sortedRecords.filter(r => r.type === filter);

  const handleCopyBibtex = (id: string, bibtex: string) => {
    navigator.clipboard.writeText(bibtex);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2000);
  };

  const preprintCount = papers.filter(r => r.type === 'preprint').length;
  const workingPaperCount = papers.filter(r => r.type === 'working-paper').length;
  const commentCount = papers.filter(r => r.type === 'comment').length;

  return (
    <Layout
      title="Research Papers & Preprints Archive"
      description="Open science research repository for Quantum Braid Dynamics: machine-checked preprints, formal Lean 4 proofs, replication code, and datasets.">
      
      <Head>
        <meta name="robots" content="index, follow" />
        <meta property="og:title" content="Research Papers & Preprints Archive | Quantum Braid Dynamics" />
        <meta name="twitter:title" content="Research Papers & Preprints Archive | Quantum Braid Dynamics" />
      </Head>

      <main style={{ minHeight: '90vh', padding: '2.5rem 0 4rem 0', backgroundColor: 'var(--ifm-background-color)' }}>
        <div className="container" style={{ maxWidth: '1200px' }}>

          {/* Top Repository Header Banner */}
          <div style={{
            borderBottom: '1px solid var(--ifm-color-emphasis-200)',
            paddingBottom: '1.75rem',
            marginBottom: '2rem'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '1rem' }}>
              <div>
                <div style={{
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '0.4rem',
                  fontSize: '0.825rem',
                  color: '#6366f1',
                  fontWeight: 600,
                  textTransform: 'uppercase',
                  letterSpacing: '0.05em',
                  marginBottom: '0.35rem'
                }}>
                  <span>◈</span> Open Science Research Archive
                </div>
                <h1 style={{ fontSize: '2.2rem', fontWeight: 800, margin: '0 0 0.5rem 0', letterSpacing: '-0.02em' }}>
                  QBD Research Papers & Preprints
                </h1>
                <p style={{ fontSize: '1.05rem', color: 'var(--ifm-color-emphasis-700)', margin: 0, maxWidth: '800px' }}>
                  Preprints, research papers, critical commentaries, and computational replication archives by <strong>R. Fisher</strong> (Braid Dynamics).
                </p>
              </div>

              {/* Quick Filter Buttons */}
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.4rem', alignSelf: 'center' }}>
                {[
                  { key: 'all', label: `All Papers (${papers.length})` },
                  { key: 'preprint', label: `Preprints (${preprintCount})` },
                  { key: 'working-paper', label: `Working Papers (${workingPaperCount})` },
                  { key: 'comment', label: `Comments & Critiques (${commentCount})` },
                ].map(item => (
                  <button
                    key={item.key}
                    onClick={() => setFilter(item.key as any)}
                    style={{
                      padding: '0.4rem 0.85rem',
                      borderRadius: '6px',
                      fontSize: '0.825rem',
                      fontWeight: 600,
                      cursor: 'pointer',
                      border: filter === item.key ? '1px solid #6366f1' : '1px solid var(--ifm-color-emphasis-300)',
                      backgroundColor: filter === item.key ? '#6366f1' : 'var(--ifm-card-background-color)',
                      color: filter === item.key ? '#ffffff' : 'var(--ifm-color-emphasis-800)',
                      transition: 'all 0.15s ease'
                    }}>
                    {item.label}
                  </button>
                ))}
              </div>
            </div>
          </div>

          {/* Two-Column Zenodo-Style Layout */}
          <div style={{ display: 'grid', gridTemplateColumns: 'minmax(0, 1fr) 320px', gap: '2rem', alignItems: 'start' }}>
            
            {/* Left Column: Feed of Records */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
              
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingBottom: '0.5rem', borderBottom: '1px solid var(--ifm-color-emphasis-200)' }}>
                <span style={{ fontSize: '0.95rem', fontWeight: 700, color: 'var(--ifm-color-emphasis-800)' }}>
                  Indexed Manuscripts ({filteredRecords.length})
                </span>
                <span style={{ fontSize: '0.8rem', color: 'var(--ifm-color-emphasis-500)' }}>
                  Sorted by: Publication Date
                </span>
              </div>

              {filteredRecords.map(rec => {
                const pdfLink = rec.primaryLinks.find(l => l.label === 'PDF');
                
                return (
                  <div
                    key={rec.id}
                    style={{
                      backgroundColor: 'var(--ifm-card-background-color)',
                      border: '1px solid var(--ifm-color-emphasis-300)',
                      borderRadius: '10px',
                      padding: '1.5rem',
                      boxShadow: '0 2px 8px rgba(0,0,0,0.04)',
                      transition: 'border-color 0.15s ease, box-shadow 0.15s ease',
                      position: 'relative'
                    }}>
                    
                    {/* Top Metadata Badges Line */}
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '0.5rem', marginBottom: '0.75rem' }}>
                      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.4rem', alignItems: 'center' }}>
                        
                        {/* Date + Version Badge */}
                        <span style={{
                          backgroundColor: 'rgba(59, 130, 246, 0.12)',
                          color: '#2563eb',
                          border: '1px solid rgba(59, 130, 246, 0.25)',
                          padding: '0.15rem 0.55rem',
                          borderRadius: '4px',
                          fontSize: '0.75rem',
                          fontWeight: 600
                        }}>
                          {rec.date} ({rec.version})
                        </span>

                        {/* Type Badge */}
                        <span style={{
                          backgroundColor: rec.typeLabel.includes('WIP') ? 'rgba(245, 158, 11, 0.15)' : 'var(--ifm-color-emphasis-200)',
                          color: rec.typeLabel.includes('WIP') ? '#d97706' : 'var(--ifm-color-emphasis-800)',
                          border: rec.typeLabel.includes('WIP') ? '1px solid rgba(245, 158, 11, 0.35)' : 'none',
                          padding: '0.15rem 0.55rem',
                          borderRadius: '4px',
                          fontSize: '0.75rem',
                          fontWeight: 600
                        }}>
                          {rec.typeLabel.includes('WIP') ? '🚧 ' + rec.typeLabel : rec.typeLabel}
                        </span>

                        {/* Open Access Badge */}
                        {rec.isOpenAccess && (
                          <span style={{
                            backgroundColor: 'rgba(34, 197, 94, 0.12)',
                            color: '#16a34a',
                            border: '1px solid rgba(34, 197, 94, 0.25)',
                            padding: '0.15rem 0.55rem',
                            borderRadius: '4px',
                            fontSize: '0.75rem',
                            fontWeight: 600,
                            display: 'inline-flex',
                            alignItems: 'center',
                            gap: '0.25rem'
                          }}>
                            🔓 Open Access
                          </span>
                        )}

                        {/* License Pill */}
                        <span style={{
                          backgroundColor: 'var(--ifm-color-emphasis-100)',
                          color: 'var(--ifm-color-emphasis-700)',
                          border: '1px solid var(--ifm-color-emphasis-300)',
                          padding: '0.15rem 0.45rem',
                          borderRadius: '4px',
                          fontSize: '0.75rem'
                        }}>
                          {rec.licenseLabel}
                        </span>

                        {/* Verified Proof & Test Badges */}
                        {rec.verifiedBadges && rec.verifiedBadges.map((badge, idx) => (
                          <span key={idx} style={{
                            backgroundColor: 'rgba(147, 51, 234, 0.1)',
                            color: '#7e22ce',
                            border: '1px solid rgba(147, 51, 234, 0.25)',
                            padding: '0.15rem 0.55rem',
                            borderRadius: '4px',
                            fontSize: '0.75rem',
                            fontWeight: 600
                          }}>
                            ✓ {badge}
                          </span>
                        ))}

                      </div>
                    </div>

                    {/* Title */}
                    <h2 style={{ fontSize: '1.25rem', fontWeight: 700, margin: '0 0 0.5rem 0', lineHeight: 1.35 }}>
                      <Link to={rec.slug} style={{ color: '#2563eb', textDecoration: 'none' }}>
                        {rec.title}
                      </Link>
                    </h2>

                    {/* Author Line with ORCID */}
                    <div style={{ fontSize: '0.875rem', color: 'var(--ifm-color-emphasis-700)', marginBottom: '0.4rem', display: 'flex', alignItems: 'center', flexWrap: 'wrap' }}>
                      <span style={{ color: 'var(--ifm-color-emphasis-900)', fontWeight: 600 }}>{rec.authors}</span>
                      {rec.orcid && (
                        <a
                          href={`https://orcid.org/${rec.orcid}`}
                          target="_blank"
                          rel="noopener noreferrer"
                          title={`ORCID: ${rec.orcid}`}
                          style={{
                            display: 'inline-flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                            width: '16px',
                            height: '16px',
                            backgroundColor: '#a6ce39',
                            color: '#ffffff',
                            borderRadius: '50%',
                            fontSize: '9px',
                            fontWeight: 700,
                            textDecoration: 'none',
                            marginLeft: '6px',
                            lineHeight: 1,
                            boxShadow: '0 1px 2px rgba(0,0,0,0.1)'
                          }}>
                          iD
                        </a>
                      )}
                    </div>

                    {/* Subline Metadata */}
                    <div style={{ fontSize: '0.8rem', color: 'var(--ifm-color-emphasis-600)', marginBottom: '1.1rem' }}>
                      {rec.subMeta}
                    </div>

                    {/* Clean Action Links */}
                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.6rem', alignItems: 'center' }}>
                      <Link
                        to={rec.slug}
                        style={{
                          display: 'inline-flex',
                          alignItems: 'center',
                          gap: '0.35rem',
                          padding: '0.4rem 0.85rem',
                          borderRadius: '6px',
                          fontSize: '0.825rem',
                          fontWeight: 600,
                          backgroundColor: '#2563eb',
                          color: '#ffffff',
                          textDecoration: 'none'
                        }}>
                        📖 Read Manuscript &amp; Downloads →
                      </Link>

                      {pdfLink && (
                        <a
                          href={pdfLink.href}
                          download
                          style={{
                            display: 'inline-flex',
                            alignItems: 'center',
                            gap: '0.35rem',
                            padding: '0.4rem 0.85rem',
                            borderRadius: '6px',
                            fontSize: '0.825rem',
                            fontWeight: 600,
                            backgroundColor: 'var(--ifm-color-emphasis-100)',
                            color: 'var(--ifm-color-emphasis-900)',
                            textDecoration: 'none',
                            border: '1px solid var(--ifm-color-emphasis-300)'
                          }}>
                          <span>📄</span> PDF {pdfLink.size && `(${pdfLink.size})`}
                        </a>
                      )}

                      {/* BibTeX Citation toggle button */}
                      {rec.bibtex && (
                        <button
                          onClick={() => setActiveBibtex(activeBibtex === rec.id ? null : rec.id)}
                          style={{
                            display: 'inline-flex',
                            alignItems: 'center',
                            gap: '0.35rem',
                            padding: '0.4rem 0.85rem',
                            borderRadius: '6px',
                            fontSize: '0.825rem',
                            fontWeight: 600,
                            backgroundColor: 'transparent',
                            color: '#6366f1',
                            border: '1px solid rgba(99, 102, 241, 0.4)',
                            cursor: 'pointer'
                          }}>
                          📑 {activeBibtex === rec.id ? 'Hide Citation' : 'Cite'}
                        </button>
                      )}
                    </div>

                    {/* Expandable BibTeX Drawer */}
                    {activeBibtex === rec.id && rec.bibtex && (
                      <div style={{
                        marginTop: '0.85rem',
                        padding: '0.85rem',
                        backgroundColor: 'var(--ifm-code-background)',
                        borderRadius: '6px',
                        border: '1px solid var(--ifm-color-emphasis-300)',
                        position: 'relative'
                      }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.4rem' }}>
                          <span style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--ifm-color-emphasis-700)', textTransform: 'uppercase' }}>
                            BibTeX Citation Format
                          </span>
                          <button
                            onClick={() => handleCopyBibtex(rec.id, rec.bibtex!)}
                            style={{
                              padding: '0.2rem 0.5rem',
                              fontSize: '0.75rem',
                              fontWeight: 600,
                              borderRadius: '4px',
                              cursor: 'pointer',
                              backgroundColor: copiedId === rec.id ? '#16a34a' : 'var(--ifm-color-emphasis-200)',
                              color: copiedId === rec.id ? '#ffffff' : 'var(--ifm-color-emphasis-800)',
                              border: 'none'
                            }}>
                            {copiedId === rec.id ? '✓ Copied' : 'Copy BibTeX'}
                          </button>
                        </div>
                        <pre style={{ margin: 0, padding: 0, fontSize: '0.775rem', backgroundColor: 'transparent', border: 'none', lineHeight: 1.4 }}>
                          <code>{rec.bibtex}</code>
                        </pre>
                      </div>
                    )}

                  </div>
                );
              })}

            </div>

            {/* Right Column: Grounded Info Sidebar */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
              
              {/* "About This Archive" Card */}
              <div style={{
                backgroundColor: 'var(--ifm-card-background-color)',
                border: '1px solid var(--ifm-color-emphasis-300)',
                borderRadius: '10px',
                padding: '1.35rem',
                boxShadow: '0 2px 8px rgba(0,0,0,0.04)'
              }}>
                <h3 style={{ fontSize: '1.05rem', fontWeight: 700, marginBottom: '0.85rem', color: 'var(--ifm-color-emphasis-900)' }}>
                  About This Archive
                </h3>
                <ul style={{ margin: 0, paddingLeft: '1.1rem', fontSize: '0.85rem', color: 'var(--ifm-color-emphasis-800)', lineHeight: 1.6 }}>
                  <li style={{ marginBottom: '0.65rem' }}>
                    <strong>Research Papers & Critiques:</strong> Hosts preprints, formal analyses, and critical commentaries on discrete spacetime models, causal networks, and graph rewriting cosmologies.
                  </li>
                  <li style={{ marginBottom: '0.65rem' }}>
                    <strong>Computational Reproducibility:</strong> Articles provide standalone simulation engines, empirical datasets, or formal proof kernels where applicable.
                  </li>
                  <li>
                    <strong>Open Formats:</strong> Manuscripts are freely available in both compiled PDF and raw Markdown (<code>.md</code>) formats under permissive licenses.
                  </li>
                </ul>
              </div>

              {/* Author Attribution Card */}
              <div style={{
                backgroundColor: 'var(--ifm-card-background-color)',
                border: '1px solid var(--ifm-color-emphasis-300)',
                borderRadius: '10px',
                padding: '1.35rem',
                boxShadow: '0 2px 8px rgba(0,0,0,0.04)'
              }}>
                <h3 style={{ fontSize: '1.05rem', fontWeight: 700, marginBottom: '0.65rem', color: 'var(--ifm-color-emphasis-900)' }}>
                  Principal Investigator
                </h3>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', marginBottom: '0.25rem' }}>
                  <span style={{ fontSize: '0.9rem', fontWeight: 700 }}>R. Fisher</span>
                  <a
                    href="https://orcid.org/0009-0006-2441-3282"
                    target="_blank"
                    rel="noopener noreferrer"
                    title="ORCID: 0009-0006-2441-3282"
                    style={{
                      display: 'inline-flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      width: '16px',
                      height: '16px',
                      backgroundColor: '#a6ce39',
                      color: '#ffffff',
                      borderRadius: '50%',
                      fontSize: '9px',
                      fontWeight: 700,
                      textDecoration: 'none',
                      boxShadow: '0 1px 2px rgba(0,0,0,0.1)'
                    }}>
                    iD
                  </a>
                </div>
                <p style={{ fontSize: '0.8rem', color: 'var(--ifm-color-emphasis-600)', margin: 0 }}>
                  Braid Dynamics Research Group
                </p>
              </div>

              {/* Related Portal Resources Card */}
              <div style={{
                backgroundColor: 'var(--ifm-card-background-color)',
                border: '1px solid var(--ifm-color-emphasis-300)',
                borderRadius: '10px',
                padding: '1.35rem',
                boxShadow: '0 2px 8px rgba(0,0,0,0.04)'
              }}>
                <h3 style={{ fontSize: '1.05rem', fontWeight: 700, marginBottom: '0.85rem', color: 'var(--ifm-color-emphasis-900)' }}>
                  Related Portal Resources
                </h3>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem', fontSize: '0.85rem' }}>
                  <div>
                    <Link to="/monograph" style={{ fontWeight: 600, color: '#6366f1', textDecoration: 'none' }}>
                      📚 The Monograph →
                    </Link>
                    <div style={{ fontSize: '0.775rem', color: 'var(--ifm-color-emphasis-600)', marginTop: '0.15rem' }}>
                      Comprehensive 25-chapter treatise establishing the theoretical framework.
                    </div>
                  </div>
                  <div>
                    <Link to="/monograph/download" style={{ fontWeight: 600, color: '#6366f1', textDecoration: 'none' }}>
                      💾 Monograph Downloads Hub →
                    </Link>
                    <div style={{ fontSize: '0.775rem', color: 'var(--ifm-color-emphasis-600)', marginTop: '0.15rem' }}>
                      Monograph PDFs, structured JSON data, and treatise model archives.
                    </div>
                  </div>
                  <div>
                    <Link to="/spectrum" style={{ fontWeight: 600, color: '#6366f1', textDecoration: 'none' }}>
                      🔬 Braid Model Spectrum →
                    </Link>
                    <div style={{ fontSize: '0.775rem', color: 'var(--ifm-color-emphasis-600)', marginTop: '0.15rem' }}>
                      Interactive particle spectrum and topological braid configuration explorer.
                    </div>
                  </div>
                </div>
              </div>

            </div>

          </div>

        </div>
      </main>
    </Layout>
  );
}

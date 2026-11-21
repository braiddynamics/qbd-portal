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
      description="Open science research repository for Quantum Braid Dynamics: machine-checked preprints, formal Lean 4 proofs, replication code, and datasets."
    >
      <Head>
        <meta name="robots" content="index, follow" />
        <meta property="og:title" content="Research Papers & Preprints Archive | Quantum Braid Dynamics" />
        <meta name="twitter:title" content="Research Papers & Preprints Archive | Quantum Braid Dynamics" />
      </Head>

      <main className="papers-page">
        <div className="container" style={{ maxWidth: '1200px' }}>

          {/* Top Repository Header Banner */}
          <div className="papers-header">
            <div className="papers-header-inner">
              <div>
                <div className="papers-kicker">
                  <span>◈</span> Open Science Research Archive
                </div>
                <h1 className="papers-title">
                  QBD Research Papers &amp; Preprints
                </h1>
                <p style={{ fontSize: '1.05rem', color: 'var(--ifm-color-emphasis-700)', margin: 0, maxWidth: '800px' }}>
                  Preprints, research papers, critical commentaries, and computational replication archives by <strong>R. Fisher</strong> (Braid Dynamics).
                </p>
              </div>

              {/* Quick Filter Buttons */}
              <div className="papers-filters">
                {[
                  { key: 'all', label: `All Papers (${papers.length})` },
                  { key: 'preprint', label: `Preprints (${preprintCount})` },
                  { key: 'working-paper', label: `Working Papers (${workingPaperCount})` },
                  { key: 'comment', label: `Comments & Critiques (${commentCount})` },
                ].map(item => (
                  <button
                    type="button"
                    key={item.key}
                    onClick={() => setFilter(item.key as 'all' | 'preprint' | 'working-paper' | 'comment')}
                    className={`papers-filter-btn ${filter === item.key ? 'active' : ''}`}
                  >
                    {item.label}
                  </button>
                ))}
              </div>
            </div>
          </div>

          {/* Two-Column Zenodo-Style Layout (stacks cleanly on mobile) */}
          <div className="papers-layout">

            {/* Left Column: Feed of Records */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>

              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingBottom: '0.5rem', borderBottom: '1px solid var(--qbd-border-subtle)', flexWrap: 'wrap', gap: '0.5rem' }}>
                <span style={{ fontSize: '0.95rem', fontWeight: 700, color: 'var(--ifm-color-emphasis-800)' }}>
                  Indexed Manuscripts ({filteredRecords.length})
                </span>
                <span style={{ fontSize: '0.8rem', color: 'var(--ifm-color-emphasis-600)' }}>
                  Sorted by: Publication Date
                </span>
              </div>

              {filteredRecords.map(rec => {
                const pdfLink = rec.primaryLinks.find(l => l.label === 'PDF');
                const isWip = rec.typeLabel.includes('WIP');

                return (
                  <div key={rec.id} className="papers-card">

                    {/* Top Metadata Badges Line */}
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '0.5rem', marginBottom: '0.75rem' }}>
                      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.4rem', alignItems: 'center' }}>

                        {/* Date + Version Badge */}
                        <span className="papers-badge papers-badge--info">
                          {rec.date}{rec.version ? ` (${rec.version})` : ''}
                        </span>

                        {/* Type Badge */}
                        <span className={`papers-badge ${isWip ? 'papers-badge--warn' : 'papers-badge--neutral'}`}>
                          {isWip ? '🚧 ' + rec.typeLabel : rec.typeLabel}
                        </span>

                        {/* Open Access Badge */}
                        {rec.isOpenAccess && (
                          <span className="papers-badge papers-badge--success">
                            🔓 Open Access
                          </span>
                        )}

                        {/* License Pill */}
                        <span className="papers-badge papers-badge--neutral">
                          {rec.licenseLabel}
                        </span>

                        {/* Verified Proof & Test Badges */}
                        {rec.verifiedBadges && rec.verifiedBadges.map((badge, idx) => (
                          <span key={idx} className="papers-badge papers-badge--violet">
                            ✓ {badge}
                          </span>
                        ))}

                      </div>
                    </div>

                    {/* Title */}
                    <h2 className="papers-card-title">
                      <Link to={rec.slug}>
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
                          }}
                        >
                          iD
                        </a>
                      )}
                    </div>

                    {/* Subline Metadata */}
                    <div style={{ fontSize: '0.82rem', color: 'var(--ifm-color-emphasis-600)', marginBottom: '1.1rem' }}>
                      {rec.subMeta}
                    </div>

                    {/* Clean Action Links */}
                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.6rem', alignItems: 'center' }}>
                      <Link to={rec.slug} className="papers-action-primary">
                        📖 Read Manuscript &amp; Downloads →
                      </Link>

                      {pdfLink && (
                        <a
                          href={pdfLink.href.replace(/^pathname:\/\//, '')}
                          download
                          className="papers-action-secondary"
                        >
                          <span>📄</span> PDF {pdfLink.size && `(${pdfLink.size})`}
                        </a>
                      )}

                      {/* DOI record */}
                      {rec.doiUrl && (
                        <a
                          href={rec.doiUrl}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="papers-action-outline"
                        >
                          DOI / Zenodo ↗
                        </a>
                      )}

                      {/* BibTeX Citation toggle button */}
                      {rec.bibtex && (
                        <button
                          type="button"
                          onClick={() => setActiveBibtex(activeBibtex === rec.id ? null : rec.id)}
                          className="papers-action-outline"
                        >
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
                        borderRadius: '8px',
                        border: '1px solid var(--qbd-border-subtle)',
                        position: 'relative'
                      }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.4rem' }}>
                          <span style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--ifm-color-emphasis-700)', textTransform: 'uppercase' }}>
                            BibTeX Citation Format
                          </span>
                          <button
                            type="button"
                            onClick={() => handleCopyBibtex(rec.id, rec.bibtex!)}
                            style={{
                              padding: '0.2rem 0.55rem',
                              fontSize: '0.75rem',
                              fontWeight: 600,
                              borderRadius: '4px',
                              cursor: 'pointer',
                              backgroundColor: copiedId === rec.id ? 'var(--qbd-badge-success-text)' : 'var(--qbd-surface-muted)',
                              color: copiedId === rec.id ? '#ffffff' : 'var(--ifm-color-emphasis-800)',
                              border: '1px solid var(--qbd-border-subtle)'
                            }}
                          >
                            {copiedId === rec.id ? '✓ Copied' : 'Copy BibTeX'}
                          </button>
                        </div>
                        <pre className="papers-bibtex-pre">
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
              <div className="papers-sidebar-card">
                <h3 style={{ fontSize: '1.05rem', fontWeight: 700, marginBottom: '0.85rem', color: 'var(--ifm-color-emphasis-900)' }}>
                  About This Archive
                </h3>
                <ul style={{ margin: 0, paddingLeft: '1.1rem', fontSize: '0.85rem', color: 'var(--ifm-color-emphasis-800)', lineHeight: 1.6 }}>
                  <li style={{ marginBottom: '0.65rem' }}>
                    <strong>Research Papers &amp; Critiques:</strong> Hosts preprints, formal analyses, and critical commentaries on discrete spacetime models, causal networks, and graph rewriting cosmologies.
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
              <div className="papers-sidebar-card">
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
                    }}
                  >
                    iD
                  </a>
                </div>
                <p style={{ fontSize: '0.8rem', color: 'var(--ifm-color-emphasis-600)', margin: 0 }}>
                  Braid Dynamics Research Group
                </p>
              </div>

              {/* Related Portal Resources Card */}
              <div className="papers-sidebar-card">
                <h3 style={{ fontSize: '1.05rem', fontWeight: 700, marginBottom: '0.85rem', color: 'var(--ifm-color-emphasis-900)' }}>
                  Related Portal Resources
                </h3>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem', fontSize: '0.85rem' }}>
                  <div>
                    <Link to="/monograph" style={{ fontWeight: 600, color: 'var(--ifm-color-primary)', textDecoration: 'none' }}>
                      📚 The Monograph →
                    </Link>
                    <div style={{ fontSize: '0.775rem', color: 'var(--ifm-color-emphasis-600)', marginTop: '0.15rem' }}>
                      Comprehensive 25-chapter treatise establishing the theoretical framework.
                    </div>
                  </div>
                  <div>
                    <Link to="/monograph/download" style={{ fontWeight: 600, color: 'var(--ifm-color-primary)', textDecoration: 'none' }}>
                      💾 Monograph Downloads Hub →
                    </Link>
                    <div style={{ fontSize: '0.775rem', color: 'var(--ifm-color-emphasis-600)', marginTop: '0.15rem' }}>
                      Monograph PDFs, structured JSON data, and treatise model archives.
                    </div>
                  </div>
                  <div>
                    <Link to="/spectrum" style={{ fontWeight: 600, color: 'var(--ifm-color-primary)', textDecoration: 'none' }}>
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

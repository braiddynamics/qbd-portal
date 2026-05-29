import React, { useEffect, useState } from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import Head from '@docusaurus/Head';

interface ChapterProgress {
  title: string;
  subtitle: string;
  progress: number;
  status: string;
  tasks: { label: string; status: 'completed' | 'in-progress' | 'pending' }[];
}

const chaptersData: Record<string, ChapterProgress> = {
  '18': {
    title: "Chapter 18: Big Kindling (Inflation)",
    subtitle: "Phenomenological Consequences",
    progress: 85,
    status: "Numerical lattice computations executing...",
    tasks: [
      { label: "Analytical parity symmetry-breaking proofs", status: "completed" },
      { label: "Friedmann scaling constraint validation", status: "completed" },
      { label: "Exponential de Sitter growth modeling", status: "completed" },
      { label: "Primordial red-tilt spectral tilt verification (92% done)", status: "in-progress" },
      { label: "Causal network structural stabilization checks", status: "pending" }
    ]
  },
  '19': {
    title: "Chapter 19: Hot Universe (Nucleosynthesis)",
    subtitle: "Phenomenological Consequences",
    progress: 60,
    status: "Relic abundance modeling in progress...",
    tasks: [
      { label: "Nuclear reaction network matrices formulation", status: "completed" },
      { label: "Helium-4/Deuterium relic abundance calculations", status: "in-progress" },
      { label: "Thermodynamic expansion equilibrium solvers", status: "pending" },
      { label: "Phase transition temperature bounds integration", status: "pending" }
    ]
  },
  '20': {
    title: "Chapter 20: Structured Universe (Cosmic Web)",
    subtitle: "Phenomenological Consequences",
    progress: 45,
    status: "Filament cluster simulations active...",
    tasks: [
      { label: "Causal graph clustering definition rules", status: "completed" },
      { label: "Large-scale dark matter filament simulations", status: "in-progress" },
      { label: "Anisotropy power spectrum calculations", status: "pending" },
      { label: "N-body model isomorphism testing", status: "pending" }
    ]
  },
  '21': {
    title: "Chapter 21: Dark Sector (Relics)",
    subtitle: "Phenomenological Consequences",
    progress: 35,
    status: "Lattice defect analysis ongoing...",
    tasks: [
      { label: "ASH (defect) production thresholds definition", status: "completed" },
      { label: "Weakly interacting braid cross-section computations", status: "in-progress" },
      { label: "Cold dark matter density bounds correlation", status: "pending" }
    ]
  },
  '22': {
    title: "Chapter 22: Singularities & Condensates (Extremes)",
    subtitle: "Phenomenological Consequences",
    progress: 20,
    status: "Horizon geometry derivation active...",
    tasks: [
      { label: "Black hole horizons in causal graphs definition", status: "completed" },
      { label: "Singularity-free bounce transition mechanics", status: "in-progress" },
      { label: "Bose-Einstein braid condensate stability proofs", status: "pending" }
    ]
  },
  '23': {
    title: "Chapter 23: Holographic World (Universality)",
    subtitle: "Applications and Synthesis",
    progress: 15,
    status: "Mapping bulk-boundary operators...",
    tasks: [
      { label: "Boundary-to-bulk information mappings", status: "completed" },
      { label: "Holographic entropy bounds calculations", status: "in-progress" },
      { label: "Conformal field theory duality validation", status: "pending" }
    ]
  },
  '24': {
    title: "Chapter 24: Mathematical Universe (Derivations)",
    subtitle: "Applications and Synthesis",
    progress: 10,
    status: "Resolving consistency parameters...",
    tasks: [
      { label: "Axiom systems and graph rewriting theorems", status: "completed" },
      { label: "Consistency proofs under Gödel boundaries", status: "pending" },
      { label: "Derivations database index schema design", status: "pending" }
    ]
  },
  '25': {
    title: "Chapter 25: Cosmological Natural Selection (Synthesis)",
    subtitle: "Applications and Synthesis",
    progress: 5,
    status: "Establishing selection criteria...",
    tasks: [
      { label: "Selection pressure algorithm formalisms", status: "in-progress" },
      { label: "Multiverse path integral calculations", status: "pending" },
      { label: "Cosmological parameter stabilization bounds", status: "pending" }
    ]
  }
};

export default function WIPPage() {
  const [activeTab, setActiveTab] = useState<string>('18');
  const [email, setEmail] = useState('');
  const [subscribed, setSubscribed] = useState(false);

  // Safe client-side reading of URL query params
  useEffect(() => {
    if (typeof window !== 'undefined') {
      const params = new URLSearchParams(window.location.search);
      const ch = params.get('chapter');
      const pt = params.get('part');
      
      if (ch && chaptersData[ch]) {
        setActiveTab(ch);
      } else if (pt === '4') {
        setActiveTab('18');
      } else if (pt === '5') {
        setActiveTab('23');
      }
    }
  }, []);

  const handleSubscribe = (e: React.FormEvent) => {
    e.preventDefault();
    if (email.trim()) {
      setSubscribed(true);
      setEmail('');
    }
  };

  const currentChapter = chaptersData[activeTab];

  return (
    <Layout
      title="Monograph Expanding: Work In Progress"
      description="Active computational simulations and derivations are currently expanding Parts 4 and 5 of the Quantum Braid Dynamics Monograph.">
      
      <Head>
        <meta name="robots" content="noindex, follow" />
      </Head>

      <main style={{ minHeight: '85vh', padding: '4rem 0', display: 'flex', alignItems: 'center', justifyContent: 'center', position: 'relative', overflow: 'hidden' }}>
        
        {/* Glow Spheres Backdrop */}
        <div style={{
          position: 'absolute',
          top: '-10%',
          left: '10%',
          width: '400px',
          height: '400px',
          background: 'radial-gradient(circle, var(--qbd-glow-color) 0%, transparent 70%)',
          pointerEvents: 'none',
          zIndex: 0
        }} />
        <div style={{
          position: 'absolute',
          bottom: '-10%',
          right: '10%',
          width: '500px',
          height: '500px',
          background: 'radial-gradient(circle, var(--qbd-glow-color) 0%, transparent 70%)',
          pointerEvents: 'none',
          zIndex: 0
        }} />

        <div className="container" style={{ position: 'relative', zIndex: 1, maxWidth: '1000px' }}>
          
          {/* Header */}
          <div style={{ textAlign: 'center', marginBottom: '3.5rem' }}>
            <div style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '0.5rem',
              backgroundColor: 'rgba(245, 158, 11, 0.1)',
              border: '1px solid rgba(245, 158, 11, 0.3)',
              color: 'var(--ifm-color-warning)',
              padding: '0.4rem 1rem',
              borderRadius: '20px',
              fontSize: '0.9rem',
              fontWeight: '600',
              marginBottom: '1rem',
              boxShadow: '0 0 15px rgba(245, 158, 11, 0.05)'
            }}>
              <span className="wip-pulse-dot" style={{
                width: '8px',
                height: '8px',
                borderRadius: '50%',
                backgroundColor: 'rgba(245, 158, 11, 1)',
                display: 'inline-block',
                boxShadow: '0 0 8px rgba(245, 158, 11, 0.8)',
              }} />
              ACTIVE SIMULATION AUDITING
            </div>
            
            <h1 style={{ fontSize: '3rem', fontWeight: '800', marginBottom: '1rem', letterSpacing: '-0.5px' }}>
              Expanding the Horizon
            </h1>
            <p style={{ fontSize: '1.25rem', color: 'var(--ifm-color-emphasis-700)', maxWidth: '650px', margin: '0 auto', lineHeight: '1.6' }}>
              Parts 4 and 5 of the monograph are currently undergoing extensive numerical simulations and peer review audits to ensure strict mathematical consistency.
            </p>
          </div>

          {/* Chapters Quick Selector Tab Bar */}
          <div style={{ 
            display: 'flex', 
            justifyContent: 'center', 
            gap: '0.5rem', 
            flexWrap: 'wrap', 
            marginBottom: '2rem',
            backgroundColor: 'rgba(0, 0, 0, 0.03)',
            padding: '0.5rem',
            borderRadius: '12px',
            border: '1px solid var(--ifm-color-emphasis-200)'
          }}>
            {Object.keys(chaptersData).map((num) => (
              <button
                key={num}
                onClick={() => setActiveTab(num)}
                style={{
                  border: 'none',
                  backgroundColor: activeTab === num ? 'var(--ifm-color-primary)' : 'transparent',
                  color: activeTab === num ? '#ffffff' : 'var(--ifm-color-emphasis-700)',
                  padding: '0.5rem 1rem',
                  borderRadius: '8px',
                  fontWeight: '600',
                  fontSize: '0.9rem',
                  cursor: 'pointer',
                  transition: 'background-color 0.2s ease, color 0.2s ease'
                }}
              >
                Ch {num}
              </button>
            ))}
          </div>

          {/* Interactive Card */}
          <div className="qbd-interactive-card" style={{ padding: '3rem', marginBottom: '3rem' }}>
            <div className="qbd-interactive-card-content">
              
              {/* Card Header */}
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '1.5rem', marginBottom: '2rem' }}>
                <div>
                  <span style={{ fontSize: '0.9rem', fontWeight: 'bold', textTransform: 'uppercase', color: 'var(--ifm-color-primary)', letterSpacing: '0.5px' }}>
                    {currentChapter.subtitle}
                  </span>
                  <h2 style={{ fontSize: '2rem', fontWeight: '800', marginTop: '0.25rem', marginBottom: '0.5rem' }}>
                    {currentChapter.title}
                  </h2>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--ifm-color-emphasis-600)', fontSize: '0.95rem' }}>
                    <span style={{ display: 'inline-block', width: '6px', height: '6px', borderRadius: '50%', backgroundColor: 'var(--ifm-color-primary)' }} />
                    {currentChapter.status}
                  </div>
                </div>

                <div style={{ textAlign: 'right' }}>
                  <div style={{ fontSize: '2.5rem', fontWeight: '900', color: 'var(--ifm-color-primary)', lineHeight: '1' }}>
                    {currentChapter.progress}%
                  </div>
                  <span style={{ fontSize: '0.8rem', fontWeight: 'bold', color: 'var(--ifm-color-emphasis-500)', textTransform: 'uppercase' }}>
                    Calculated Integrity
                  </span>
                </div>
              </div>

              {/* Progress Bar */}
              <div style={{ width: '100%', height: '10px', backgroundColor: 'var(--ifm-color-emphasis-200)', borderRadius: '5px', overflow: 'hidden', marginBottom: '2.5rem' }}>
                <div style={{
                  width: `${currentChapter.progress}%`,
                  height: '100%',
                  backgroundColor: 'var(--ifm-color-primary)',
                  borderRadius: '5px',
                  boxShadow: '0 0 12px var(--qbd-glow-color)',
                  transition: 'width 0.6s cubic-bezier(0.16, 1, 0.3, 1)'
                }} />
              </div>

              {/* Checklists */}
              <div style={{ marginBottom: '2.5rem' }}>
                <h4 style={{ fontSize: '1.1rem', fontWeight: 'bold', marginBottom: '1.25rem', color: 'var(--ifm-color-emphasis-800)' }}>
                  Derivation & Simulation Checklist
                </h4>
                
                <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                  {currentChapter.tasks.map((task, idx) => (
                    <div key={idx} style={{ 
                      display: 'flex', 
                      alignItems: 'center', 
                      gap: '1rem', 
                      padding: '0.75rem 1rem', 
                      borderRadius: '8px', 
                      border: '1px solid var(--ifm-color-emphasis-200)', 
                      backgroundColor: task.status === 'completed' ? 'rgba(46, 133, 85, 0.03)' : 'transparent' 
                    }}>
                      {task.status === 'completed' && (
                        <div style={{
                          width: '20px',
                          height: '20px',
                          borderRadius: '50%',
                          backgroundColor: 'var(--ifm-color-primary)',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          color: '#ffffff',
                          fontWeight: 'bold',
                          fontSize: '0.75rem'
                        }}>✓</div>
                      )}

                      {task.status === 'in-progress' && (
                        <div style={{
                          width: '20px',
                          height: '20px',
                          borderRadius: '50%',
                          border: '2px solid var(--ifm-color-warning)',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          color: 'var(--ifm-color-warning)',
                          fontWeight: 'bold',
                          fontSize: '0.8rem',
                          animation: 'spin 2s linear infinite'
                        }}>◌</div>
                      )}

                      {task.status === 'pending' && (
                        <div style={{
                          width: '20px',
                          height: '20px',
                          borderRadius: '50%',
                          border: '2px solid var(--ifm-color-emphasis-400)',
                        }} />
                      )}

                      <span style={{ 
                        fontSize: '0.95rem', 
                        color: task.status === 'completed' ? 'var(--ifm-color-emphasis-600)' : 'var(--ifm-color-emphasis-900)',
                        textDecoration: task.status === 'completed' ? 'line-through' : 'none',
                        fontWeight: task.status === 'in-progress' ? '600' : 'normal'
                      }}>
                        {task.label}
                      </span>
                    </div>
                  ))}
                </div>
              </div>

              {/* Action Buttons */}
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '1rem', borderTop: '1px solid var(--ifm-color-emphasis-200)', paddingTop: '2rem' }}>
                <Link to="/monograph/stage/worldsheets/17.5" className="button button--secondary button--lg" style={{ display: 'inline-flex', alignItems: 'center', gap: '0.5rem' }}>
                  <span>←</span> Read Chapter 17
                </Link>
                <Link to="/monograph" className="button button--secondary button--lg">
                  Table of Contents
                </Link>
                <Link to="/" className="button button--primary button--lg">
                  Return to Homepage
                </Link>
              </div>

            </div>
          </div>

          {/* Email Subscription Widget */}
          <div style={{
            backgroundColor: 'var(--ifm-color-emphasis-100)',
            border: '1px solid var(--ifm-color-emphasis-200)',
            padding: '2.5rem 2rem',
            borderRadius: '16px',
            textAlign: 'center'
          }}>
            <h3 style={{ fontSize: '1.5rem', marginBottom: '0.5rem', fontWeight: 'bold' }}>
              Want to review early drafts?
            </h3>
            <p style={{ color: 'var(--ifm-color-emphasis-600)', maxWidth: '500px', margin: '0 auto 1.5rem auto', fontSize: '0.95rem', lineHeight: '1.5' }}>
              Submit your email to be included in our private beta review cycles. We dispatch simulation checkpoints and draft manuscripts directly to researchers.
            </p>

            {subscribed ? (
              <div style={{
                color: 'var(--ifm-color-success)',
                fontWeight: 'bold',
                padding: '0.75rem',
                backgroundColor: 'rgba(46, 133, 85, 0.1)',
                border: '1px solid rgba(46, 133, 85, 0.3)',
                borderRadius: '8px',
                display: 'inline-block'
              }}>
                ✓ Thank you! You have been added to the private review registry.
              </div>
            ) : (
              <form onSubmit={handleSubscribe} style={{ display: 'flex', justifyContent: 'center', gap: '0.5rem', maxWidth: '450px', margin: '0 auto', flexWrap: 'wrap' }}>
                <input
                  type="email"
                  placeholder="researcher@institute.edu"
                  required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  style={{
                    flex: '1',
                    minWidth: '220px',
                    padding: '0.75rem 1rem',
                    borderRadius: '8px',
                    border: '1px solid var(--ifm-color-emphasis-300)',
                    fontSize: '0.95rem',
                    backgroundColor: 'var(--ifm-background-color)',
                    color: 'var(--ifm-color-emphasis-900)'
                  }}
                />
                <button type="submit" className="button button--primary" style={{ padding: '0.75rem 1.5rem' }}>
                  Register for Drafts
                </button>
              </form>
            )}
          </div>

        </div>

        {/* CSS Keyframe Injection for the spinning icon */}
        <style dangerouslySetInnerHTML={{__html: `
          @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
          }
          .wip-pulse-dot {
            animation: pulse-amber 1.8s infinite ease-in-out;
          }
          @keyframes pulse-amber {
            0%, 100% { transform: scale(1); opacity: 1; }
            50% { transform: scale(1.3); opacity: 0.6; }
          }
        `}} />
      </main>
    </Layout>
  );
}

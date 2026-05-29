import React, { useRef } from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import Head from '@docusaurus/Head';

// Data & Components
import { monographSections } from '../data/sections';
import LazyYouTube from '../components/lazy-youtube';
import HomepageHeader from '../components/homepage-header';
import MonographCard from '../components/monograph-card';

export default function Home() {
  // Create a ref for smooth scrolling to the video section
  const videoRef = useRef<HTMLDivElement>(null);

  const scrollToVideo = (e: React.MouseEvent) => {
    e.preventDefault();
    videoRef.current?.scrollIntoView({ behavior: 'smooth', block: 'center' });
  };

  return (
    <Layout
      title="Quantum Braid Dynamics: A Computational Process"
      description="Unifying General Relativity and the Standard Model">

      <Head>
        <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large" />
        <meta property="og:title" content="Quantum Braid Dynamics: A Computational Process" />
        <meta name="twitter:title" content="Quantum Braid Dynamics: A Computational Process" />
      </Head>

      <HomepageHeader />

      <main style={{ padding: '4rem 0', maxWidth: '1200px', margin: '0 auto' }}>
        <div className="container">

          {/* Hero Content Split */}
          <div className="row" style={{ alignItems: 'center', marginBottom: '4rem' }}>
            <div className="col col--5">
              <h2 style={{ fontSize: '2.5rem', marginBottom: '1.5rem', fontWeight: 'bold', lineHeight: '1.2' }}>
                The universe is not a thing, it is relation.
              </h2>
              <p style={{ fontSize: '1.15rem', lineHeight: '1.6', color: 'var(--ifm-color-emphasis-800)', marginBottom: '2rem' }}>
                Our Aeon begins not with a bang but with a branch of structure, composed not of fundamental things but fundamental relations.
              </p>

              {/* Interactive Smooth-Scroll Anchor */}
              <a
                href="#overview-video"
                onClick={scrollToVideo}
                style={{
                  fontSize: '1.25rem',
                  fontWeight: 'bold',
                  color: 'var(--ifm-color-primary)',
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '0.5rem',
                  textDecoration: 'none',
                  cursor: 'pointer',
                  transition: 'transform 0.2s ease, color 0.2s ease'
                }}
                className="qbd-video-cta"
              >
                Watch QBD summed up in 90 seconds
                <span style={{ transition: 'transform 0.2s ease' }}>➔</span>
              </a>
            </div>

            <div className="col col--7" ref={videoRef} id="overview-video">
              <LazyYouTube
                videoId="vT3vW-tcad8"
                title="Quantum Braid Dynamics Overview"
              />
            </div>
          </div>

          {/* Elegant Section Divider */}
          <div style={{ padding: '4rem 0', display: 'flex', justifyContent: 'center' }}>
            <div style={{ width: '50%', height: '2px', background: 'linear-gradient(90deg, transparent, var(--ifm-color-emphasis-300), transparent)' }}></div>
          </div>

          {/* --- SPINE WRAPPER STARTS --- */}
          <div className="connecting-spine-wrapper">

{/* Introductory Framework Abstract */}
            <div className="qbd-interactive-card" style={{ maxWidth: '950px', margin: '0 auto 6rem auto' }}>
              <div className="qbd-interactive-card-content" style={{ textAlign: 'center', padding: '0 1rem' }}>
                <h2 style={{ fontSize: '2.5rem', fontWeight: '800', marginBottom: '1.5rem', lineHeight: '1.3' }}>
                  Quantum Braid Dynamics <br />
                  <span style={{ color: 'var(--ifm-color-primary)', fontStyle: 'italic', fontWeight: 'normal', fontSize: '1.75rem' }}>
                    A Computational Process
                  </span>
                </h2>

                <p style={{ fontSize: '1.2rem', color: 'var(--ifm-color-emphasis-800)', lineHeight: '1.7', marginBottom: '1.5rem', textAlign: 'justify' }}>
                  Quantum Braid Dynamics (QBD) is a background-independent formulation of quantum gravity that models the cosmos without free parameters. Using only discrete events and causal links, QBD bridges gaps between the Wolfram Physics Project, Causal Set Theory, and Causal Dynamical Triangulations.
                </p>

                <p style={{ fontSize: '1.2rem', color: 'var(--ifm-color-emphasis-800)', lineHeight: '1.7', margin: 0, textAlign: 'justify' }}>
                  By integrating formal mathematical proofs, Python simulations, and explicit Lean 4 validations directly in the text, QBD presents a mathematically modern theory of information constructed from first principles.
                </p>
              </div>
            </div>

            {/* Monograph Section Cards */}
            <div className="monograph-sections-container">
              {monographSections.map((section) => (
                <MonographCard key={section.part} section={section} />
              ))}
            </div>
          </div> {/* --- SPINE WRAPPER ENDS --- */}

          {/* Support Section */}
          <div style={{ marginTop: '8rem', backgroundColor: 'var(--ifm-color-emphasis-100)', padding: '3rem 2rem', borderRadius: '16px', textAlign: 'center', border: '1px solid var(--ifm-color-emphasis-200)' }}>
            <h3 style={{ fontSize: '2rem', marginBottom: '1rem' }}>Support the Project</h3>
            <p style={{ fontSize: '1.1rem', maxWidth: '600px', margin: '0 auto 2rem', color: 'var(--ifm-color-emphasis-700)' }}>
              Quantum Braid Dynamics is an independent research initiative. Your help directly enables computational validation and open-access publishing.
            </p>
            <div style={{ display: 'flex', justifyContent: 'center', gap: '1rem', flexWrap: 'wrap' }}>
              <Link to="/legal" className="button button--primary button--lg">Collaborate</Link>
              <a href="https://github.com/braiddynamics/qbd-portal" target="_blank" rel="noopener noreferrer" className="button button--secondary button--lg">GitHub Repository</a>
              <a href="https://x.com/BraidDynamics" target="_blank" rel="noopener noreferrer" className="button button--secondary button--lg">Follow on X</a>
            </div>
          </div>

        </div>
      </main>
    </Layout>
  );
}
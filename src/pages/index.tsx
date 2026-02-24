import React from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import Head from '@docusaurus/Head';

// Data & Components
import { monographSections } from '../data/sections';
import LazyYouTube from '../components/lazy-youtube';
import HomepageHeader from '../components/homepage-header';
import MonographCard from '../components/monograph-card';

export default function Home() {
  return (
    <Layout
      title="Quantum Braid Dynamics: A Computational Process"
      description="Unifying General Relativity and the Standard Model">

      <Head>
        <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large" />
      </Head>

      <HomepageHeader />

      <main style={{padding: '4rem 0', maxWidth: '1200px', margin: '0 auto'}}>
        <div className="container">
          
          <div className="row" style={{ alignItems: 'center' }}>
            <div className="col col--5">
              <h2 style={{ fontSize: '2.5rem', marginBottom: '1.5rem', fontWeight: 'bold', lineHeight: '1.2' }}>
                The universe is not a thing, it is relation.
              </h2>
              <p style={{ fontSize: '1.15rem', lineHeight: '1.6', color: 'var(--ifm-color-emphasis-800)', marginBottom: '2rem' }}>
                Our Aeon begins not with a bang but with a branch of structure, composed not of fundamental things but fundamental relations.
              </p>
              <p style={{ fontSize: '1.25rem', fontWeight: 'bold', color: 'var(--ifm-color-primary)' }}>
                Watch QBD summed up in 90 seconds ➔
              </p>
            </div>

            <div className="col col--7">
              <LazyYouTube 
                videoId="vT3vW-tcad8" 
                title="Quantum Braid Dynamics Overview" 
              />
            </div>
          </div>

          <div style={{ padding: '8rem 0', display: 'flex', justifyContent: 'center' }}>
            <div style={{ width: '50%', height: '2px', background: 'linear-gradient(90deg, transparent, var(--ifm-color-emphasis-300), transparent)' }}></div>
          </div>

          {/* --- SPINE WRAPPER STARTS --- */}
          <div className="connecting-spine-wrapper">
            
            {/* Introductory "Auditability" Box */}
            <div className="qbd-interactive-card" style={{ textAlign: 'center', marginBottom: '5rem', maxWidth: '850px', margin: '0 auto 6rem auto' }}>
              <div className="qbd-interactive-card-content">
                <h2 style={{ fontSize: '2.5rem', fontWeight: 'bold', marginBottom: '1rem', lineHeight: '1.3' }}>
                  Quantum Braid Dynamics <br />
                  <span style={{ color: 'var(--ifm-color-primary)', fontStyle: 'italic', fontWeight: 'normal' }}>A Computational Process</span>
                </h2>
                <p style={{ fontSize: '1.2rem', color: 'var(--ifm-color-emphasis-700)', lineHeight: '1.6', margin: 0 }}>
                  <strong>QBD</strong> is presented in a form explicitly engineered for <strong>auditability</strong>. This format ensures ideas become pure logic that can be parsed, producing a physical theory that is unambiguous and well defined, whose meaning is fully determined by its internal logic.
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

          <div style={{ marginTop: '8rem', backgroundColor: 'var(--ifm-color-emphasis-100)', padding: '3rem 2rem', borderRadius: '16px', textAlign: 'center', border: '1px solid var(--ifm-color-emphasis-200)' }}>
            <h3 style={{ fontSize: '2rem', marginBottom: '1rem' }}>Support the Project</h3>
            <p style={{ fontSize: '1.1rem', maxWidth: '600px', margin: '0 auto 2rem', color: 'var(--ifm-color-emphasis-700)' }}>
              Quantum Braid Dynamics is an independent research initiative. Your support directly funds computational validation and open-access publishing.
            </p>
            <div style={{ display: 'flex', justifyContent: 'center', gap: '1rem', flexWrap: 'wrap' }}>
              <Link to="/legal" className="button button--primary button--lg">Become a Sponsor</Link>
              <a href="https://github.com/braiddynamics/qbd-portal" target="_blank" rel="noopener noreferrer" className="button button--secondary button--lg">GitHub Repository</a>
              <a href="https://x.com/BraidDynamics" target="_blank" rel="noopener noreferrer" className="button button--secondary button--lg">Follow on X</a>
            </div>
          </div>

        </div>
      </main>
    </Layout>
  );
}
import React, { useEffect, useRef, useState, ReactNode } from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Head from '@docusaurus/Head';

// Import our decoupled data
import { monographSections } from '../data/sections';

// --- COMPONENTS ---

interface FadeInViewProps {
  children: ReactNode;
}

function FadeInView({ children }: FadeInViewProps) {
  const [isVisible, setIsVisible] = useState(false);
  const domRef = useRef<HTMLDivElement>(null); 

  useEffect(() => {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          setIsVisible(true);
          if (domRef.current) observer.unobserve(domRef.current);
        }
      });
    }, { threshold: 0.15 }); 
    
    const current = domRef.current;
    if (current) observer.observe(current);
    return () => { if (current) observer.unobserve(current); };
  }, []);

  return (
    <div ref={domRef} className={`timeline-fade-in ${isVisible ? 'is-visible' : ''}`}>
      {children}
    </div>
  );
}

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className="hero-rn-style">
      <div className="container" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center' }}>
        <h1 className="hero__title" style={{fontSize: '3.5rem', marginBottom: '1rem', fontWeight: '800'}}>
          {siteConfig.title}
        </h1>
        <p className="hero__subtitle" style={{fontSize: '1.5rem', fontWeight: '400', marginBottom: '2.5rem'}}>
          {siteConfig.tagline}
        </p>
        <div style={{display: 'flex', justifyContent: 'center', gap: '1rem'}}>
          <Link className="button button--primary button--lg" to="/monograph">
            Table of Contents
          </Link>
          <Link className="button hero-white-btn button--lg" to="/monograph/intro/intro-a"> 
            Introduction
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();

  return (
    <Layout
      title="Quantum Braid Dynamics: Axiomatic Unification of GR and the Standard Model"
      description="Rigorous mathematical monograph by R. Fisher deriving General Relativity and quantum phenomena from discrete causal graphs.">

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
              <div style={{ position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden', borderRadius: '12px', boxShadow: '0 12px 28px rgba(0,0,0,0.15)', backgroundColor: '#000' }}>
                <iframe 
                  style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%' }}
                  src="https://www.youtube.com/embed/vT3vW-tcad8" 
                  title="Quantum Braid Dynamics Overview" 
                  frameBorder="0" 
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                  allowFullScreen>
                </iframe>
              </div>
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

            {/* Monograph Section Cards - Width constraint removed */}
            <div className="monograph-sections-container">
              
              {monographSections.map((section) => (
                <FadeInView key={section.part}>
                  <Link 
                    to={section.linkUrl} 
                    className="qbd-interactive-card section-row-margin" 
                    style={{ display: 'block', textDecoration: 'none', color: 'inherit' }}
                  >
                    <div className="qbd-interactive-card-content section-grid-3col">
                      
                      {/* Column 1: Text styling matches header box */}
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
              ))}

            </div>
          </div> {/* --- SPINE WRAPPER ENDS --- */}

          <div style={{ marginTop: '8rem', backgroundColor: 'var(--ifm-color-emphasis-100)', padding: '3rem 2rem', borderRadius: '16px', textAlign: 'center', border: '1px solid var(--ifm-color-emphasis-200)' }}>
            <h3 style={{ fontSize: '2rem', marginBottom: '1rem' }}>Support the Project</h3>
            <p style={{ fontSize: '1.1rem', maxWidth: '600px', margin: '0 auto 2rem', color: 'var(--ifm-color-emphasis-700)' }}>
              Quantum Braid Dynamics is an independent research initiative. Your support directly funds computational validation and open-access publishing.
            </p>
            <div style={{ display: 'flex', justifyContent: 'center', gap: '1rem', flexWrap: 'wrap' }}>
              <Link to="/sponsor" className="button button--primary button--lg">Become a Sponsor</Link>
              <a href="https://github.com/braiddynamics/qbd-portal" target="_blank" rel="noopener noreferrer" className="button button--secondary button--lg">GitHub Repository</a>
              <a href="https://x.com/BraidDynamics" target="_blank" rel="noopener noreferrer" className="button button--secondary button--lg">Follow on X</a>
            </div>
          </div>

        </div>
      </main>
    </Layout>
  );
}
import React from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header style={{
      backgroundColor: '#1b1b1d', 
      color: '#fff', 
      padding: '4rem 0', 
      textAlign: 'center'
    }}>
      <div className="container">
        <h1 className="hero__title" style={{fontSize: '3.5rem', marginBottom: '1rem'}}>
          {siteConfig.title}
        </h1>
        <p className="hero__subtitle" style={{fontSize: '1.5rem', fontWeight: '300', marginBottom: '2rem'}}>
          <i>{siteConfig.tagline}</i>
        </p>
        <div style={{display: 'flex', justifyContent: 'center', gap: '1rem'}}>
          <Link
            className="button button--primary button--lg"
            to="/monograph">
            Read the Monograph
          </Link>
          <Link
            className="button button--secondary button--lg"
            to="/monograph/foundations/intro">
            Start at Introduction
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
      title={siteConfig.title}
      description="A background-independent framework unifying General Relativity and the Standard Model.">
      <HomepageHeader />
      <main style={{padding: '2rem 0', maxWidth: '800px', margin: '0 auto'}}>
        <div className="container">
          <div className="text--center">
            <h2>Abstract</h2>
            <p style={{textAlign: 'justify', fontSize: '1.1rem', lineHeight: '1.6'}}>
              We present <strong>Quantum Braid Dynamics (QBD)</strong>, a background-independent framework that unifies General Relativity and the Standard Model as emergent behaviors of a discrete, computational substrate. The theory posits that the fundamental ontology of the universe is not a continuous manifold but a dynamic Directed Acyclic Graph evolved by a stochastic, local rewrite rule.
            </p>
            <hr style={{margin: '2rem 0'}} />
            <div className="row">
              <div className="col col--4">
                <h3>Ontology</h3>
                {/* Fixed: Use HTML italics instead of LaTeX $G$ */}
                <p>A discrete causal graph (<i>G</i>) evolved by local rewrite rules.</p>
              </div>
              <div className="col col--4">
                <h3>Dynamics</h3>
                <p>Geometrogenesis via non-equilibrium thermodynamics.</p>
              </div>
              <div className="col col--4">
                <h3>Topology</h3>
                <p>Matter arises as braided topological defects.</p>
              </div>
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}
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
            Table of Contents
          </Link>
          <Link
            className="button button--secondary button--lg"
            to="/monograph/foundations/intro">
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
      title={siteConfig.title}
      description="A background-independent framework unifying General Relativity and the Standard Model.">
      <HomepageHeader />
      <main style={{padding: '2rem 0', maxWidth: '800px', margin: '0 auto'}}>
        <div className="container">
          <div className="text--center">
            <h2>The universe is not a thing, it is relation.</h2>
            <p style={{textAlign: 'justify', fontSize: '1.1rem', lineHeight: '1.6'}}>
              Our Aeon begins not with a bang but with a branch of structure, composed not of fundamental things but fundamental relations. At the Crossover, a smooth and featureless end gives way to the new; before ergo after. Maximally symmetric, pre-geometric. Only the latent rule of becoming exists. An irreducible statement: "A can affect B." From this primitive, information coiled into its first loop and a spark of geometrogenesis rushed forth. Organized by computational process, the most fundamental and stable complex motif that could crystallize did. Our topologically braided law takes form and the grand stage is set, only awaiting its actors. ♾️
            </p> 
            <hr style={{margin: '2rem 0'}} />
            <div className="row">
              <div className="col col--4">
                <h3>Time is Updates</h3>
                <p><a href="/monograph/category/part-1-the-rules">The Rules</a></p>
              </div>
              <div className="col col--4">
                <h3>Mass is Complexity</h3>
                <p><a href="/monograph/category/part-2-the-players">The Players</a></p>
              </div>
              <div className="col col--4">
                <h3>Gravity is Process</h3>
                <p><a href="/monograph/category/part-3-the-stage">The Stage</a></p>
              </div>
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}
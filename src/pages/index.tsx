import React from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Head from '@docusaurus/Head';

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
            to="/monograph/intro/intro-a"> 
            Introduction
          </Link>
        </div>
      </div>
    </header>
  );
}

const schema = {
  "@context": "https://schema.org",
  "@type": "ScholarlyArticle",
  "headline": "Quantum Braid Dynamics: Axiomatic Unification of General Relativity and the Standard Model",
  "name": "Quantum Braid Dynamics Monograph",
  "author": {
    "@type": "Person",
    "name": "R. Fisher",
    "sameAs": "https://orcid.org/0009-0006-2441-3282"
  },
  "description": "Background-independent axiomatic framework deriving spacetime, quantum probabilities, and the Standard Model from discrete braided causal graphs, category-theoretic dynamics (awareness comonad), and thermodynamic rewrite rules.",
  "keywords": "quantum gravity, emergent spacetime, relational physics, category theory physics, graph dynamics, born rule derivation, regular bethe fragment, pre-geometric unification",
  "about": [
    { "@type": "Thing", "name": "Quantum Gravity" },
    { "@type": "Thing", "name": "Emergent Spacetime" },
    { "@type": "Thing", "name": "Category Theory in Physics" },
    { "@type": "Thing", "name": "Digital Physics" },
    { "@type": "Thing", "name": "Pre-Geometric Physics" },
    { "@type": "Thing", "name": "Relational Quantum Mechanics" }
  ],
  "url": "https://braiddynamics.com/monograph",
  "license": "https://creativecommons.org/licenses/by-nc-sa/4.0/"
};

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title="Quantum Braid Dynamics: Axiomatic Unification of GR and the Standard Model"
      description="Rigorous mathematical monograph by R. Fisher deriving General Relativity and quantum phenomena from discrete causal graphs, category theory (comonads, functors), entropy maximization on Regular Bethe Fragments, and code-verified proofs.">

      <Head>
        <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large" />

        {/* Layered Keywords */}
        <meta name="keywords" content="quantum gravity, emergent spacetime, theory of everything, digital physics, relational quantum gravity, causal graph dynamics" />
        <meta name="keywords" content="category theory physics, graph theory physics, discrete differential geometry, comonad awareness, born rule derivation, ollivier-ricci curvature, thermodynamic arrow of time" />
        <meta name="keywords" content="quantum braid dynamics, regular bethe fragment, relational entropy maximization, braided causal graphs, geometrogenesis, awareness comonad" />

        {/* Academic signals */}
        <meta name="citation_title" content="Quantum Braid Dynamics: A Computational Process" />
        <meta name="citation_author" content="R. Fisher" />
        <meta name="citation_publication_date" content="2025" />
        <meta name="citation_keywords" content="Quantum Gravity; Relational Physics; Category Theory; Graph Dynamics; Emergent Quantum Mechanics; Pre-Geometric Unification" />
        <meta name="citation_abstract" content="Background-independent unification deriving GR and the Standard Model from relational primitives with formal proofs and computational validation." />

        {/* Open Graph */}
        <meta property="og:type" content="article" />
        <meta property="og:title" content="Quantum Braid Dynamics Monograph - R. Fisher" />
        <meta property="og:description" content="Deriving physics from braided relational topology and computational process." />

        <script type="application/ld+json">
          {JSON.stringify(schema)}
        </script>
      </Head>

      <HomepageHeader />

      {/* MAIN CONTENT */}
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
                <p><a href="/monograph/category/the-rules">The Rules</a></p>
              </div>
              <div className="col col--4">
                <h3>Mass is Complexity</h3>
                <p><a href="/monograph/category/the-players">The Players</a></p>
              </div>
              <div className="col col--4">
                <h3>Gravity is Process</h3>
                <p><a href="/monograph/category/the-stage">The Stage</a></p>
              </div>
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}
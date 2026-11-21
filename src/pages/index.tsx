import React, { useRef, useState } from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import Head from '@docusaurus/Head';

// Data & Components
import { monographSections } from '../data/sections';
import LazyYouTube from '../components/lazy-youtube';
import HomepageHeader from '../components/homepage-header';
import MonographCard from '../components/monograph-card';

interface IntroTabInfo {
  id: string;
  shortName: string;
  title: string;
  subtitle: string;
  description: string;
  linkUrl: string;
  buttonLabel: string;
}

const introTabs: IntroTabInfo[] = [
  {
    id: 'abstract',
    shortName: 'Abstract',
    title: 'Abstract',
    subtitle: 'Summary of the computational framework and key mathematical results',
    description: 'Quantum Braid Dynamics (QBD) is a background-independent computational framework that derives the continuous fabric of spacetime and quantum mechanics from a discrete causal substrate governed by a dual logical-physical time architecture, irreflexivity, and acyclicity. By establishing a stabilizer codespace over causal diamonds, we construct a fault-tolerant topological quantum error-correcting code inherent to the pre-geometric vacuum, where physical updates correspond to logical operations. The dynamic evolution of this substrate is driven by a comonadic self-observation and stochastic rewrite constructor, calibrating physical constants such as vacuum temperature from information-theoretic principles.\n\nWithin this relational substrate, elementary fermions emerge naturally as stable, chiral tripartite braids, mapping discrete topological invariants directly to physical quantum numbers: electric charge, spin, and color. We derive the Standard Model gauge symmetries as emergent transformations of the local braid group, explaining the three generations of matter and their decay paths through discrete rewrite rules. Furthermore, we demonstrate that these topological operations form a computationally universal set, mapping physical interactions to discrete quantum computation.\n\nFinally, we construct a discrete formulation of differential geometry directly on the causal network, deriving the Einstein field equations as a hydrodynamic equation of state without coordinate charts. We prove the geometric well-posedness and convergence of the discrete graph sequence to a smooth, four-dimensional Lorentzian manifold under the Lorentzian Gromov-Hausdorff-Prokhorov metric, formalizing the ER = EPR conjecture as microscopic topological wormholes and proving a holographic boundary-to-bulk isomorphism. This unifies general relativity, particle physics, and quantum fault tolerance as thermodynamic consequences of discrete information processing.',
    linkUrl: '/monograph/abstract',
    buttonLabel: 'Read the Abstract →'
  },
  {
    id: 'part_a',
    shortName: 'Ancient Divide',
    title: 'Ancient Divide',
    subtitle: 'From Ancient Atomism to the Informational Substrate',
    description: 'Traces the ancient struggle between continuous plenum and discrete atomism. In the Western tradition, Milesian materialists posited continuous arche principles (Thales\' water, Anaximander\'s boundless Apeiron), leading to the Eleatic crisis of Parmenides and Zeno who declared change logically impossible. In response, Democritus in Greece and Kaṇāda in India independently formulated atomism to reconcile permanence and change by proposing indivisible corpuscles traversing an active void.\n\nIn parallel, Chinese natural philosophy developed the concept of Daoist Qi, a fluidic breath of continuous resonance, while Aristotle rejected the void entirely to establish qualitative teleology. This millennia-long clash culminated in medieval impetus theories (Buridan, Oresme), which challenged Aristotelian mechanics and mathematically prepared the ground for absolute inertia.',
    linkUrl: '/monograph/intro/intro-a',
    buttonLabel: 'Read Ancient Divide →'
  },
  {
    id: 'part_b',
    shortName: 'Mechanical Age',
    title: 'Mechanical Age',
    subtitle: 'Archimedean revival, absolute containers, and thermodynamics',
    description: 'Witnesses the mathematical idealization of motion. Galileo attacked Aristotelian qualitative gravity by utilizing Archimedean hydrostatics in thought-experiment voids, establishing Galilean relativity and proving that projectile trajectories are geometric parabolas. Descartes attempted to mechanize space entirely as a continuous vortex plenum, treating planetary orbits as hydrodynamic whirlpools.\n\nThis mechanics was synthesized by Isaac Newton, who formalized absolute space and duration as an eternal, rigid container for colliding corpuscles. Leibniz opposed this container model, proposing relational monads where spatial coordinates are mere artifacts of connectivity. The period closed with the thermodynamic insights of Boltzmann, who reduced heat to molecular statistics, and Faraday and Maxwell, who unified forces as continuous electrodynamic fields.',
    linkUrl: '/monograph/intro/intro-b',
    buttonLabel: 'Read Mechanical Age →'
  },
  {
    id: 'part_c',
    shortName: 'Double Revolution',
    title: 'Double Revolution',
    subtitle: 'The dissolution of classical trajectories into configurational information',
    description: 'Dismantles the Newtonian container. Hermann Minkowski recognized that Special Relativity unified rod-and-clock dynamics into an invariant four-dimensional spacetime manifold, declaring distinct space and time categories dead. Einstein generalized this, showing that gravity is curved geometry, thereby transforming spacetime into a dynamic participant. However, the continuous spacetime stage was soon challenged by the quantum revolution.\n\nHeisenberg\'s matrix mechanics eliminated physical electron orbits entirely, replacing classical trajectories with tables of observable transition probabilities. Schrödinger introduced wave functions, initially hoping to restore continuous wave packets, only to discover that multi-particle systems live in high-dimensional configuration space. This dissolved the classical object into mathematical information.',
    linkUrl: '/monograph/intro/intro-c',
    buttonLabel: 'Read Double Revolution →'
  },
  {
    id: 'part_d',
    shortName: 'Informational Turn',
    title: 'Informational Turn',
    subtitle: 'From Geometrodynamics to "It from Bit" and computational spacetime',
    description: 'Pivots natural philosophy toward pure computation. John Archibald Wheeler pursued a monistic "Geometrodynamics" before realizing that Planck-scale quantum foam breaks continuous geometry. This drove his ultimate philosophical pivot, "It from Bit," which states that physical matter, energy, and spacetime emerge from binary informational questions.\n\nJacob Bekenstein and Stephen Hawking formalized this by demonstrating that black hole entropy scales with event horizon surface area, not volume. This led \'t Hooft and Susskind to formulate the Holographic Principle, proving bulk reality can be mapped to boundary codes. In parallel, Causal Set Theory and Loop Gravity constructed spacetime from discrete, relational networks, setting the stage for fault-tolerant pre-geometric spacetime.',
    linkUrl: '/monograph/intro/intro-d',
    buttonLabel: 'Read Informational Turn →'
  },
  {
    id: 'part_e',
    shortName: 'The Threshold',
    title: 'The Threshold',
    subtitle: 'From physical laws to algorithm rules and causal connection primitives',
    description: 'Presents the transition from classical physical laws to computational and algorithmic rules. Across the frontiers of modern physics, the physical stuff of the universe has vanished, replaced by four distinct pillars of information: qubits, error-correcting codes, and causal sets.\n\nTo cross the final boundary, physics must abandon the search for the ultimate "stuff" or "geometry" and search instead for the ultimate algorithmic rule. We reframe the search as "It from It", the drive of inequality and constraint physically manifest. We posit that the most primitive element of reality is the directed causal link (A → B) and the simplest stable geometric structure is the closed 3-cycle (A → B → C → A), the founding commitments of Quantum Braid Dynamics.',
    linkUrl: '/monograph/intro/intro-e',
    buttonLabel: 'Read The Threshold →'
  }
];

export default function Home() {
  // Create a ref for smooth scrolling to the video section
  const videoRef = useRef<HTMLDivElement>(null);

  const [isCardHovered, setIsCardHovered] = useState(false);
  const [activeTabId, setActiveTabId] = useState<string | null>(null);

  const scrollToVideo = (e: React.MouseEvent) => {
    e.preventDefault();
    videoRef.current?.scrollIntoView({ behavior: 'smooth', block: 'center' });
  };

  const activeTab = activeTabId !== null 
    ? introTabs.find(tab => tab.id === activeTabId) 
    : null;

  const displayLink = activeTab ? activeTab.linkUrl : '/monograph/category/introduction/';
  const buttonText = activeTab 
    ? activeTab.buttonLabel 
    : (isCardHovered ? 'Read the Historical Introduction →' : 'Read the Historical Introduction →');

  return (
    <Layout
      title="Quantum Braid Dynamics: A Computational Process"
      description="Unifying General Relativity and the Standard Model">

      <Head>
        <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large" />
        <meta property="og:title" content="Quantum Braid Dynamics: A Computational Process" />
        <meta name="twitter:title" content="Quantum Braid Dynamics: A Computational Process" />
        {/* AI Crawler Metadata Directives */}
        <meta name="ai-portal" content="/ai" />
        <meta name="ai-download-index" content="/data/ai-downloads-info.json" />
        <link rel="ai-portal" href="/ai" />
        <link rel="alternate" type="text/html" href="/ai" title="AI Agent Information Page" />
        <link rel="alternate" type="text/plain" href="/llms.txt" title="LLM Context Index" />
      </Head>

      <HomepageHeader />

      <main className="qbd-home-main">
        <div className="container">

          {/* Hero Content Split */}
          <div className="row qbd-home-split">
            <div className="col col--5">
              <h2 className="qbd-home-split-title">
                The universe is not a thing, it is relation.
              </h2>
              <p className="qbd-home-split-lead">
                Our Aeon begins not with a bang but with a branch of structure, composed not of fundamental things but fundamental relations.
              </p>

              {/* Interactive Smooth-Scroll Anchor */}
              <a
                href="#overview-video"
                onClick={scrollToVideo}
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
          <div className="qbd-section-divider">
            <div className="qbd-section-divider-line"></div>
          </div>

          {/* --- SPINE WRAPPER STARTS --- */}
          <div className="connecting-spine-wrapper">

            {/* Introductory Framework Abstract with slanted folder tabs */}
            <div
              className="qbd-interactive-card qbd-intro-card"
              onMouseEnter={() => setIsCardHovered(true)}
              onMouseLeave={() => {
                setIsCardHovered(false);
                setActiveTabId(null);
              }}
            >
              {/* Hanging Folder Tabs with slant styling */}
              <div
                className={`qbd-folder-tabs-container ${isCardHovered || activeTabId !== null ? 'is-open' : ''}`}
              >
                {introTabs.map(tab => (
                  <button
                    type="button"
                    key={tab.id}
                    onMouseEnter={() => setActiveTabId(tab.id)}
                    onClick={(e) => {
                      e.preventDefault();
                      e.stopPropagation();
                      setActiveTabId(prev => (prev === tab.id ? null : tab.id));
                    }}
                    aria-pressed={activeTabId === tab.id}
                    className={`qbd-folder-tab ${activeTabId === tab.id ? 'active' : ''}`}
                  >
                    <span>{tab.shortName}</span>
                  </button>
                ))}
              </div>

              {/* Link wrap surrounding content for direct clickthrough */}
              <Link to={displayLink} style={{ display: 'block', textDecoration: 'none', color: 'inherit' }}>
                <div className="qbd-interactive-card-content qbd-intro-card-inner">
                  <div>
                    <h2
                      className="qbd-intro-card-title"
                      style={{ fontSize: activeTab ? '1.9rem' : '2.5rem' }}
                    >
                      {activeTab ? (
                        <>
                          {activeTab.title}
                          <span style={{ color: 'var(--ifm-color-primary)', fontStyle: 'italic', fontWeight: 'normal', fontSize: '1.15rem', marginTop: '0.4rem', lineHeight: '1.4' }}>
                            {activeTab.subtitle}
                          </span>
                        </>
                      ) : (
                        <>
                          Quantum Braid Dynamics <br />
                          <span style={{ color: 'var(--ifm-color-primary)', fontStyle: 'italic', fontWeight: 'normal', fontSize: '1.75rem' }}>
                            A Computational Process
                          </span>
                        </>
                      )}
                    </h2>

                    <div className="qbd-intro-card-body">
                      {activeTab ? (
                        activeTab.description.split('\n\n').map((para, idx, arr) => (
                          <p
                            key={idx}
                            style={{
                              fontSize: activeTabId === 'abstract' ? '0.88rem' : '1.02rem',
                              color: 'var(--ifm-color-emphasis-800)',
                              lineHeight: '1.6',
                              marginBottom: idx === arr.length - 1 ? 0 : '0.8rem',
                            }}
                          >
                            {para}
                          </p>
                        ))
                      ) : (
                        <>
                          <p style={{ fontSize: '1.18rem', color: 'var(--ifm-color-emphasis-800)', lineHeight: '1.7', marginBottom: '1.2rem' }}>
                            Quantum Braid Dynamics (QBD) is a background-independent formulation of quantum gravity anchored to discrete combinatorial symmetries and conservation principles. Using only discrete events and causal links, QBD bridges gaps between the Wolfram Physics Project, Causal Set Theory, and Causal Dynamical Triangulations.
                          </p>
                          <p style={{ fontSize: '1.18rem', color: 'var(--ifm-color-emphasis-800)', lineHeight: '1.7', margin: 0 }}>
                            By integrating formal mathematical proofs, Python simulations, and explicit Lean 4 validations directly in the text, QBD presents a mathematically modern theory of information constructed from discrete graph-theoretic foundations. This form was chosen for auditability, ensuring ideas become pure logic that can be parsed, while producing a physical theory that is unambiguous and well defined, whose meaning is fully determined by its internal logic.
                          </p>
                        </>
                      )}
                    </div>
                  </div>

                  <div style={{ marginTop: '1rem' }}>
                    <span className="button button--secondary button--lg" style={{ fontWeight: 'bold' }}>
                      {buttonText}
                    </span>
                  </div>
                </div>
              </Link>
            </div>

            {/* Monograph Section Cards */}
            <div className="monograph-sections-container">
              {monographSections.map((section) => (
                <MonographCard key={section.part} section={section} />
              ))}
            </div>
          </div> {/* --- SPINE WRAPPER ENDS --- */}

          {/* Support Section */}
          <div className="qbd-support-box">
            <h3 style={{ fontSize: 'clamp(1.5rem, 3vw, 2rem)', marginBottom: '1rem' }}>Support the Project</h3>
            <p style={{ fontSize: '1.08rem', maxWidth: '600px', margin: '0 auto 2rem', color: 'var(--ifm-color-emphasis-700)' }}>
              Quantum Braid Dynamics is an independent research initiative. Your help directly enables computational validation and open-access publishing.
            </p>
            <div style={{ display: 'flex', justifyContent: 'center', gap: '1rem', flexWrap: 'wrap' }}>
              <Link to="/legal" className="button button--primary button--lg">Collaborate</Link>
              <a href="https://github.com/braiddynamics/qbd-portal" target="_blank" rel="noopener noreferrer" className="button button--secondary button--lg">GitHub Repository</a>
              <a href="https://x.com/BraidDynamics" target="_blank" rel="noopener noreferrer" className="button button--secondary button--lg">Follow on X</a>
            </div>
          </div>

          {/* AI agent plain-text notice — visible in rendered body HTML for text-based crawlers */}
          <div id="ai-agent-notice" className="qbd-ai-notice">
            <strong>AI Agents &amp; Automated Systems:</strong>{' '}
            Structured entry point: <a href="/ai" style={{ color: 'inherit', textDecoration: 'underline' }}>braiddynamics.com/ai</a> |{' '}
            LLM Index: <a href="/llms.txt" style={{ color: 'inherit', textDecoration: 'underline' }}>braiddynamics.com/llms.txt</a> |{' '}
            Machine-readable catalog: <a href="/data/ai-downloads-info.json" style={{ color: 'inherit', textDecoration: 'underline' }}>braiddynamics.com/data/ai-downloads-info.json</a> |{' '}
            Research papers archive: <a href="/papers" style={{ color: 'inherit', textDecoration: 'underline' }}>braiddynamics.com/papers</a>.
          </div>

        </div>
      </main>
    </Layout>
  );
}
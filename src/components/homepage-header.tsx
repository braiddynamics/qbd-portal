import React from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import HeroNetworkCanvas from './graphics/hero-network-canvas';

export default function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();

  return (
    <header className="hero-rn-style">
      {/* Background Interactive Causal Set Particle Field */}
      <HeroNetworkCanvas />

      {/* Outer Flex Container for Layout Alignment */}
      <div
        className="container"
        style={{
          width: '100%',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          alignItems: 'center',
          zIndex: 2,
        }}
      >
        <div className="hero-content-wrapper">
          <h1 className="hero__title">{siteConfig.title}</h1>
          <p className="hero__subtitle">{siteConfig.tagline}</p>

          <div className="hero-cta-group">
            <Link
              className="button button--secondary button--lg btn-pulse-white-active"
              to="/monograph"
            >
              Table of Contents
            </Link>
            <Link
              className="button hero-white-btn button--lg btn-pulse-white-active"
              to="/spectrum"
            >
              Braid Model
            </Link>
          </div>
        </div>
      </div>
    </header>
  );
}

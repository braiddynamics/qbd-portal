import React from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

export default function HomepageHeader() {
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
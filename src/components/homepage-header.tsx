import React, { useRef, useEffect } from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

// Embedded high-performance Canvas component inside the same file
// to prevent any Docusaurus path resolution failures and run the particles flawlessly.
function EmbeddedHeroNetworkCanvas() {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let width = 0;
    let height = 0;
    const particles: any[] = [];
    const particleCount = 140;

    class Particle {
      x!: number;
      y!: number;
      size!: number;
      speedX!: number;
      speedY!: number;
      opacity!: number;

      constructor() {
        this.reset();
      }

      reset() {
        this.x = Math.random() * width;
        this.y = Math.random() * height;
        this.size = Math.random() * 2.8 + 1.2;
        this.speedX = (Math.random() - 0.5) * 0.5;
        this.speedY = (Math.random() - 0.5) * 0.5;
        this.opacity = Math.random() * 0.7 + 0.3;
      }

      update() {
        this.x += this.speedX;
        this.y += this.speedY;

        if (this.x < 0) this.x = width;
        if (this.x > width) this.x = 0;
        if (this.y < 0) this.y = height;
        if (this.y > height) this.y = 0;
      }

      draw() {
        ctx!.save();
        ctx!.globalAlpha = this.opacity;
        ctx!.fillStyle = '#67e8f9'; // Cyan particle core
        ctx!.beginPath();
        ctx!.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx!.fill();
        ctx!.restore();
      }
    }

    const resize = () => {
      const parent = canvas.parentElement;
      if (parent) {
        width = canvas.width = parent.clientWidth;
        height = canvas.height = parent.clientHeight;
      } else {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
      }
    };

    window.addEventListener('resize', resize);
    resize();

    for (let i = 0; i < particleCount; i++) {
      particles.push(new Particle());
    }

    const animate = () => {
      ctx!.clearRect(0, 0, width, height);

      // Celestial void backdrop overlay
      ctx!.fillStyle = 'rgba(10, 15, 35, 0.55)';
      ctx!.fillRect(0, 0, width, height);

      particles.forEach((p) => {
        p.update();
        p.draw();
      });

      // Render Causal Connections
      ctx!.strokeStyle = 'rgba(103, 232, 249, 0.25)';
      ctx!.lineWidth = 1.1;

      for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
          const dx = particles[i].x - particles[j].x;
          const dy = particles[i].y - particles[j].y;
          const distance = Math.sqrt(dx * dx + dy * dy);

          if (distance < 180) {
            ctx!.globalAlpha = (1 - distance / 180) * 0.35;
            ctx!.beginPath();
            ctx!.moveTo(particles[i].x, particles[i].y);
            ctx!.lineTo(particles[j].x, particles[j].y);
            ctx!.stroke();
          }
        }
      }
      ctx!.globalAlpha = 1;

      requestAnimationFrame(animate);
    };

    animate();

    return () => window.removeEventListener('resize', resize);
  }, []);

  return (
    <canvas
      ref={canvasRef}
      style={{
        position: 'absolute',
        top: 0,
        left: 0,
        width: '100%',
        height: '100%',
        zIndex: 0,
        pointerEvents: 'none',
      }}
    />
  );
}

export default function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();

  return (
    <header className="hero-rn-style">
      {/* Background Interactive Causal Set Particle Field (Self-contained) */}
      <EmbeddedHeroNetworkCanvas />

      {/* Outer Flex Container for Layout Alignment */}
      <div 
        className="container" 
        style={{ 
          width: '100%', 
          display: 'flex', 
          flexDirection: 'column',
          justifyContent: 'center', 
          alignItems: 'center',
          zIndex: 2 
        }}
      >
        {/* Transparent Content Wrapper:
            Groups title, subtitle, and CTA buttons into a single structural unit
            without any background card or border, keeping the background braid 
            completely sharp and unobstructed.
        */}
        <div className="hero-content-wrapper">
          {/* Animated Chromodynamic Title */}
          <h1 className="hero__title">
            {siteConfig.title}
          </h1>
          
          {/* Tagline Subtitle */}
          <p className="hero__subtitle">
            {siteConfig.tagline}
          </p>

          {/* Call to Action Buttons */}
          <div style={{ display: 'flex', justifyContent: 'center', gap: '1.2rem', flexWrap: 'wrap' }}>
            <Link 
              className="button button--primary button--lg btn-pulse-white-active" 
              to="/monograph"
            >
              Table of Contents
            </Link>
            <Link 
              className="button hero-white-btn button--lg btn-pulse-white-active" 
              to="/monograph/intro/intro-a"
            >
              Introduction
            </Link>
          </div>
        </div>
      </div>
    </header>
  );
}
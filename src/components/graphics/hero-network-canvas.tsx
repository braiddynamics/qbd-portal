import React, { useRef, useEffect } from 'react';

export default function HeroNetworkCanvas() {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const prefersReducedMotion =
      typeof window !== 'undefined' &&
      window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;

    let width = 0;
    let height = 0;
    let animationFrameId = 0;
    let isCancelled = false;

    interface Particle {
      x: number;
      y: number;
      size: number;
      speedX: number;
      speedY: number;
      opacity: number;
    }

    const particles: Particle[] = [];

    const createParticle = (): Particle => ({
      x: Math.random() * width,
      y: Math.random() * height,
      size: Math.random() * 2.6 + 1.2,
      speedX: (Math.random() - 0.5) * 0.5,
      speedY: (Math.random() - 0.5) * 0.5,
      opacity: Math.random() * 0.7 + 0.3,
    });

    const syncParticleCount = () => {
      const targetCount = width < 640 ? 60 : width < 1024 ? 95 : 140;
      while (particles.length < targetCount) {
        particles.push(createParticle());
      }
      if (particles.length > targetCount) {
        particles.length = targetCount;
      }
    };

    const resize = () => {
      const parent = canvas.parentElement;
      if (parent) {
        width = canvas.width = parent.clientWidth;
        height = canvas.height = parent.clientHeight;
      } else {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
      }
      syncParticleCount();
    };

    window.addEventListener('resize', resize);
    resize();

    const drawFrame = (advance: boolean) => {
      ctx.clearRect(0, 0, width, height);

      // Deep celestial void base backdrop
      ctx.fillStyle = 'rgba(10, 15, 35, 0.55)';
      ctx.fillRect(0, 0, width, height);

      for (const p of particles) {
        if (advance) {
          p.x += p.speedX;
          p.y += p.speedY;
          if (p.x < 0) p.x = width;
          if (p.x > width) p.x = 0;
          if (p.y < 0) p.y = height;
          if (p.y > height) p.y = 0;
        }

        ctx.save();
        ctx.globalAlpha = p.opacity;
        ctx.fillStyle = '#67e8f9';
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      }

      // Render causal connection lines
      const maxDist = width < 640 ? 130 : 180;
      ctx.strokeStyle = 'rgba(103, 232, 249, 0.25)';
      ctx.lineWidth = 1.1;

      for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
          const dx = particles[i].x - particles[j].x;
          const dy = particles[i].y - particles[j].y;
          const distance = Math.sqrt(dx * dx + dy * dy);

          if (distance < maxDist) {
            ctx.globalAlpha = (1 - distance / maxDist) * 0.35;
            ctx.beginPath();
            ctx.moveTo(particles[i].x, particles[i].y);
            ctx.lineTo(particles[j].x, particles[j].y);
            ctx.stroke();
          }
        }
      }
      ctx.globalAlpha = 1;
    };

    const animate = () => {
      if (isCancelled) return;
      drawFrame(true);
      animationFrameId = requestAnimationFrame(animate);
    };

    if (prefersReducedMotion) {
      drawFrame(false);
    } else {
      animate();
    }

    return () => {
      isCancelled = true;
      cancelAnimationFrame(animationFrameId);
      window.removeEventListener('resize', resize);
    };
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

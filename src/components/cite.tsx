import React, { useState, useEffect, useRef } from 'react';
import { createPortal } from 'react-dom';
import referencesData from '../data/references.json';
import './cite.css';

interface CiteProps {
  id: string;
  label: string;
}

interface Reference {
  author: string;
  title: string;
  publication?: string;
  url: string;
  overview: string;
  relevance: string;
}

const references: Record<string, Reference> = referencesData as any;

export default function Cite({ id, label }: CiteProps) {
  const [isMounted, setIsMounted] = useState(false);
  const [isOpen, setIsOpen] = useState(false);
  const [coords, setCoords] = useState({ top: 0, left: 0 });
  const [placement, setPlacement] = useState<'top' | 'bottom'>('top');
  const triggerRef = useRef<HTMLAnchorElement>(null);
  const tooltipRef = useRef<HTMLDivElement>(null);
  const timeoutRef = useRef<NodeJS.Timeout | null>(null);

  const refData = references[id];

  useEffect(() => {
    setIsMounted(true);
  }, []);

  if (!refData) {
    return <span className="cite-broken">[Broken Citation: {id}]</span>;
  }

  const handleMouseEnter = () => {
    if (timeoutRef.current) clearTimeout(timeoutRef.current);
    timeoutRef.current = setTimeout(() => {
      setIsOpen(true);
    }, 150); // 150ms debounced hover trigger
  };

  const handleMouseLeave = () => {
    if (timeoutRef.current) clearTimeout(timeoutRef.current);
    timeoutRef.current = setTimeout(() => {
      setIsOpen(false);
    }, 200); // 200ms grace period before fading out
  };

  const handleTooltipMouseEnter = () => {
    if (timeoutRef.current) clearTimeout(timeoutRef.current);
  };

  const handleTooltipMouseLeave = () => {
    if (timeoutRef.current) clearTimeout(timeoutRef.current);
    timeoutRef.current = setTimeout(() => {
      setIsOpen(false);
    }, 200);
  };

  const updatePosition = () => {
    if (triggerRef.current && tooltipRef.current) {
      const triggerRect = triggerRef.current.getBoundingClientRect();
      const tooltipRect = tooltipRef.current.getBoundingClientRect();
      const viewportWidth = window.innerWidth;
      const viewportHeight = window.innerHeight;

      // Determine horizontal position (center aligned to trigger, with boundary clipping protection)
      let left = triggerRect.left + (triggerRect.width / 2) - (tooltipRect.width / 2);
      
      // Keep inside horizontal viewport boundaries
      const padding = 16;
      if (left < padding) {
        left = padding;
      } else if (left + tooltipRect.width > viewportWidth - padding) {
        left = viewportWidth - tooltipRect.width - padding;
      }

      // Determine vertical position (above or below, based on available space)
      let top = triggerRect.top - tooltipRect.height - 12; // 12px gap
      let currentPlacement: 'top' | 'bottom' = 'top';

      if (top < padding) {
        // Not enough space above, place below
        top = triggerRect.bottom + 12;
        currentPlacement = 'bottom';
      }

      // Using fixed positioning relative to viewport, so we don't add scrollY
      setCoords({
        top: top,
        left: left
      });
      setPlacement(currentPlacement);
    }
  };

  useEffect(() => {
    if (isOpen) {
      // Calculate position initially
      // Small timeout to allow the element to render and have dimensions
      const timer = setTimeout(updatePosition, 0);
      
      window.addEventListener('resize', updatePosition);
      window.addEventListener('scroll', updatePosition);

      return () => {
        clearTimeout(timer);
        window.removeEventListener('resize', updatePosition);
        window.removeEventListener('scroll', updatePosition);
      };
    }
  }, [isOpen]);

  useEffect(() => {
    return () => {
      if (timeoutRef.current) clearTimeout(timeoutRef.current);
    };
  }, []);

  const triggerElement = (
    <a
      ref={triggerRef}
      href={`/monograph/appendices/a-references#${id}`}
      className="cite-badge"
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
    >
      {label}
    </a>
  );

  // If not mounted or server-side render, just show the badge link
  if (!isMounted) {
    return triggerElement;
  }

  const tooltipElement = isOpen ? (
    <div
      ref={tooltipRef}
      className={`cite-tooltip cite-placement-${placement}`}
      style={{
        position: 'fixed',
        top: `${coords.top}px`,
        left: `${coords.left}px`,
        zIndex: 9999,
      }}
      onMouseEnter={handleTooltipMouseEnter}
      onMouseLeave={handleTooltipMouseLeave}
    >
      <div className="cite-tooltip-content">
        <div className="cite-tooltip-header">
          <span className="cite-author">{refData.author}</span>
          <span className="cite-title">"{refData.title}"</span>
        </div>
        
        <div className="cite-tooltip-body">
          <div className="cite-section">
            <span className="cite-section-title">OVERVIEW</span>
            <p className="cite-section-text">{refData.overview}</p>
          </div>
          
          <div className="cite-section">
            <span className="cite-section-title">RELEVANCE TO QBD</span>
            <p className="cite-section-text">{refData.relevance}</p>
          </div>
        </div>
        
        <div className="cite-tooltip-footer">
          <a 
            href={refData.url} 
            target="_blank" 
            rel="noopener noreferrer" 
            className="cite-footer-btn cite-btn-primary"
          >
            View Paper Website
          </a>
          <a 
            href={`/monograph/appendices/a-references#${id}`} 
            className="cite-footer-btn cite-btn-secondary"
          >
            Go to Appendix Page
          </a>
        </div>
      </div>
    </div>
  ) : null;

  return (
    <span className="cite-container">
      {triggerElement}
      {createPortal(tooltipElement, document.body)}
    </span>
  );
}

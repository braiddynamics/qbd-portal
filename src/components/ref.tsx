import React, { useState, useEffect, useRef } from 'react';
import { createPortal } from 'react-dom';
import katex from 'katex';
import definitionsData from '../data/definitions.json';
import './ref.css';

interface RefProps {
  id: string;
  label: string;
}

interface Definition {
  id: string;
  type: string;
  title: string;
  statement: string;
  plainEnglish: string;
  file: string;
}

const definitions: Record<string, Definition> = definitionsData as any;

// Helper to format link destination based on parsed relative file path
// E.g. "01-rules/01-ontology/1.2.md" -> "/monograph/rules/ontology/1.2"
const getChapterUrl = (file: string, anchor: string) => {
  const withoutExt = file.replace(/\.mdx?$/, '');
  // Clean up folder leading digits (e.g. "01-rules" -> "rules")
  const cleanPath = withoutExt
    .split('/')
    .map(part => part.replace(/^\d+-/, ''))
    .join('/');
  return `/monograph/${cleanPath}#${anchor}`;
};

// Parse simple inline Markdown: bold (**text**), italics (*text*), and links ([label](url)),
// and React components <Ref id="..." label="..." /> and <Cite id="..." label="..." />
const parseMarkdown = (text: string) => {
  if (!text) return null;

  // Split by bold (**), italics (*), links ([label](url)), <Ref /> and <Cite /> components
  const regex = /(\*\*.*?\*\*|\*.*?\*|\[.*?\]\(.*?\)|<Ref\s+id="[^"]+"\s+label="[^"]+"\s*(?:\/>|>.*?<\/Ref>)|<Cite\s+id="[^"]+"\s+label="[^"]+"\s*(?:\/>|>.*?<\/Cite>))/g;
  const parts = text.split(regex);

  return parts.map((part, index) => {
    if (part.startsWith('**') && part.endsWith('**')) {
      return <strong key={index}>{part.slice(2, -2)}</strong>;
    } else if (part.startsWith('*') && part.endsWith('*')) {
      return <em key={index}>{part.slice(1, -1)}</em>;
    } else if (part.startsWith('[') && part.includes('](')) {
      const match = part.match(/\[(.*?)\]\((.*?)\)/);
      if (match) {
        const [_, label, url] = match;
        return (
          <a key={index} href={url} className="ref-inline-link">
            {label}
          </a>
        );
      }
    } else if (part.startsWith('<Ref') && (part.endsWith('/>') || part.endsWith('Ref>'))) {
      const match = part.match(/<Ref\s+id="([^"]+)"\s+label="([^"]+)"\s*(?:\/>|>.*?<\/Ref>)/);
      if (match) {
        const [_, refId, refLabel] = match;
        const targetDef = definitions[refId];
        const destination = targetDef ? getChapterUrl(targetDef.file, refId) : `/monograph/appendices/b-definitions#${refId}`;
        return (
          <a key={index} href={destination} className="ref-badge">
            {refLabel}
          </a>
        );
      }
    } else if (part.startsWith('<Cite') && (part.endsWith('/>') || part.endsWith('Cite>'))) {
      const match = part.match(/<Cite\s+id="([^"]+)"\s+label="([^"]+)"\s*(?:\/>|>.*?<\/Cite>)/);
      if (match) {
        const [_, citeId, citeLabel] = match;
        return (
          <a key={index} href={`/monograph/appendices/a-references#${citeId}`} className="ref-inline-cite">
            {citeLabel}
          </a>
        );
      }
    }
    return part;
  });
};

// Render inline and display math blocks with KaTeX, cascading markdown parsing for the text
const renderLaTeX = (text: string) => {
  if (!text) return null;

  // Split by Display math ($$...$$) and Inline math ($...$)
  const regex = /(\$\$[\s\S]*?\$\$|\$[\s\S]*?\$)/g;
  const parts = text.split(regex);

  return parts.map((part, index) => {
    if (part.startsWith('$$') && part.endsWith('$$')) {
      const math = part.slice(2, -2);
      try {
        const html = katex.renderToString(math, { displayMode: true, throwOnError: false });
        return <div key={index} dangerouslySetInnerHTML={{ __html: html }} className="ref-math-display" />;
      } catch (err) {
        return <span key={index} className="ref-math-error">{part}</span>;
      }
    } else if (part.startsWith('$') && part.endsWith('$')) {
      const math = part.slice(1, -1);
      try {
        const html = katex.renderToString(math, { displayMode: false, throwOnError: false });
        return <span key={index} dangerouslySetInnerHTML={{ __html: html }} className="ref-math-inline" />;
      } catch (err) {
        return <span key={index} className="ref-math-error">{part}</span>;
      }
    }
    return <React.Fragment key={index}>{parseMarkdown(part)}</React.Fragment>;
  });
};

export default function Ref({ id, label }: RefProps) {
  const [isMounted, setIsMounted] = useState(false);
  const [isOpen, setIsOpen] = useState(false);
  const [coords, setCoords] = useState({ top: 0, left: 0 });
  const [placement, setPlacement] = useState<'top' | 'bottom'>('top');
  const [isPositioned, setIsPositioned] = useState(false);
  const triggerRef = useRef<HTMLAnchorElement>(null);
  const tooltipRef = useRef<HTMLDivElement>(null);
  const timeoutRef = useRef<NodeJS.Timeout | null>(null);

  const refData = definitions[id];

  useEffect(() => {
    setIsMounted(true);
  }, []);

  if (!refData) {
    return <span className="ref-broken">[Broken Reference: §{id}]</span>;
  }

  // Deduce if a formal proof exists (e.g. 1.3.6.1 is the proof for 1.3.6)
  const proofId = `${id}.1`;
  const hasProof = definitions[proofId] !== undefined;

  // Clean up MDX/HTML tags in parsed markdown statement for tooltips
  const cleanStatement = (text: string) => {
    // Strip :::info/:::tip wrapper markers cleanly
    let cleaned = text.replace(/:::[a-z]+(?:\[.*?\])?/g, '');
    cleaned = cleaned.replace(/:::/g, '');
    return cleaned.trim();
  };

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
      setIsPositioned(false);
    }, 200); // 200ms grace period before fading out
  };

  const handleTooltipMouseEnter = () => {
    if (timeoutRef.current) clearTimeout(timeoutRef.current);
  };

  const handleTooltipMouseLeave = () => {
    if (timeoutRef.current) clearTimeout(timeoutRef.current);
    timeoutRef.current = setTimeout(() => {
      setIsOpen(false);
      setIsPositioned(false);
    }, 200);
  };

  const updatePosition = () => {
    if (triggerRef.current && tooltipRef.current) {
      const triggerRect = triggerRef.current.getBoundingClientRect();
      const tooltipRect = tooltipRef.current.getBoundingClientRect();
      const viewportWidth = window.innerWidth;
      const viewportHeight = window.innerHeight;

      // If tooltip is newly mounted, width or height might measure as 0 initially
      if (tooltipRect.width === 0 || tooltipRect.height === 0) {
        requestAnimationFrame(updatePosition);
        return;
      }

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

      setCoords({
        top: top,
        left: left
      });
      setPlacement(currentPlacement);
      setIsPositioned(true);
    }
  };

  useEffect(() => {
    if (isOpen) {
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
      href={getChapterUrl(refData.file, id)}
      className="ref-badge"
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
    >
      {label}
    </a>
  );

  if (!isMounted) {
    return triggerElement;
  }

  const tooltipElement = isOpen ? (
    <div
      ref={tooltipRef}
      className={`ref-tooltip ref-placement-${placement} ${isPositioned ? 'ref-visible' : ''}`}
      style={{
        position: 'fixed',
        top: `${coords.top}px`,
        left: `${coords.left}px`,
        zIndex: 100000,
        visibility: isPositioned ? 'visible' : 'hidden',
      }}
      onMouseEnter={handleTooltipMouseEnter}
      onMouseLeave={handleTooltipMouseLeave}
    >
      <div className="ref-tooltip-content">
        <div className="ref-tooltip-header">
          <span className="ref-category">{refData.type} {refData.id}</span>
          <span className="ref-title">{refData.title}</span>
        </div>
        
        <div className="ref-tooltip-body">
          <div className="ref-section">
            <span className="ref-section-title">FORMAL STATEMENT</span>
            <div className="ref-section-text ref-math-block">
              {renderLaTeX(cleanStatement(refData.statement))}
            </div>
          </div>
          
          <div className="ref-section">
            <span className="ref-section-title">IN PLAIN ENGLISH</span>
            <div className="ref-section-text ref-plain-text">
              {renderLaTeX(refData.plainEnglish)}
            </div>
          </div>
        </div>
        
        <div className="ref-tooltip-footer">
          {hasProof ? (
            <a 
              href={getChapterUrl(refData.file, proofId)} 
              className="ref-footer-btn ref-btn-primary"
            >
              View Formal Proof
            </a>
          ) : (
            <a 
              href={getChapterUrl(refData.file, id)} 
              className="ref-footer-btn ref-btn-primary"
            >
              Go to Monograph Section
            </a>
          )}
        </div>
      </div>
    </div>
  ) : null;

  return (
    <span className="ref-container">
      {triggerElement}
      {createPortal(tooltipElement, document.body)}
    </span>
  );
}

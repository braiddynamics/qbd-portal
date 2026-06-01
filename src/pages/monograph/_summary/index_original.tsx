"import React, { useState, useRef, useEffect } from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import Head from '@docusaurus/Head';

import { LightboxImageInfo } from './types';
import { chapters, timelineEvents, partsList } from './data';
import { MathInline } from './components/math';
import { ImportantDefinitionsBox, HistoricalCallout, ConceptualVisualBox } from './components/accessories';
import { LightConeSandbox, BraidAnimator, CurvatureWarp, TimelineSandbox, SelectionSandbox } from './components/sandboxes';
import { PartPreviewPanel } from './components/part-preview-panel';

// Helper to parse strings containing mixed plain text and inline LaTeX ($...$) and compile math cleanly
const renderMixedMathText = (text: string) => {
  if (!text.includes('$')) return <span>{text}</span>;
  
  // Split by matches of $...$ (capturing matching groups keeps the separators in the split array)
  const parts = text.split(/(\$.*?\$)/g);
  
  return (
    <span>
      {parts.map((part, index) => {
        if (part.startsWith('$') && part.endsWith('$')) {
          const mathExpr = part.slice(1, -1);
          return <MathInline key={index} math={mathExpr} />;
        }
        return part;
      })}
    </span>
  );
};

const ROMAN_NUMERALS = ['I', 'II', 'III', 'IV', 'V'];

export default function MonographSummary() {
  const [activeChapterNum, setActiveChapterNum] = useState<number>(0);

  // States for interactive SVG sandboxes
  const [timelineIndex, setTimelineIndex] = useState<number>(0);
  const [hoveredNode, setHoveredNode] = useState<number | null>(null);
  const [braidType, setBraidType] = useState<'electron' | 'quark' | 'neutrino'>('electron');
  const [warpStrength, setWarpStrength] = useState<number>(50);
  const [selectionStability, setSelectionStability] = useState<number>(75);

  // Lightbox Modal State
  const [lightbox, setLightbox] = useState<LightboxImageInfo | null>(null);

  // Enlarged Vector Diagram State
  const 
<truncated 42929 bytes>
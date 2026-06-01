import React from 'react';
import katex from 'katex';

// QBD Specific LaTeX Macros from docusaurus.config.ts
export const qbdMacros = {
  "\\tL": "t_L",
  "\\tphys": "t_{phys}",
  "\\Gadel": "\\mathcal{G}_{adel}",
  "\\Con": "\\operatorname{Con}",
  "\\ket": "\\left| #1 \\right\\rangle",
  "\\bra": "\\left\\langle #1 \\right|",
  "\\braket": "\\langle #1 | #2 \\rangle",
  "\\Evol": "\\mathcal{U}",
  "\\Hamiltonian": "\\hat{H}",
  "\\Perm": "\\hat{P}",
  "\\Prob": "\\mathbb{P}",
  "\\Exp": "\\mathbb{E}",
  "\\card": "\\left| #1 \\right|",
  "\\Ent": "S(U_{\\tL})",
  "\\Graph": "G=(V, E)",
  "\\Hist": "\\mathbf{Hist}",
  "\\Caus": "\\mathbf{Caus}_t",
  "\\braid": "\\beta",
  "\\writhe": "w(\\beta)",
  "\\geom": "\\gamma",
  "\\syndrome": "\\sigma",
  "\\ash": "\\text{ash}",
};

// Math components utilizing raw KaTeX compilation for JSX safety
export const MathBlock: React.FC<{ math: string; displayMode?: boolean }> = ({ math, displayMode = true }) => {
  try {
    const html = katex.renderToString(math, { 
      displayMode, 
      throwOnError: false,
      macros: qbdMacros 
    });
    return (
      <div 
        dangerouslySetInnerHTML={{ __html: html }} 
        style={{ 
          overflowX: 'auto', 
          overflowY: 'hidden', 
          padding: '0.6rem 0',
          margin: '0.6rem 0',
          fontFamily: 'var(--ifm-font-family-monospace)',
          fontSize: '0.98rem'
        }} 
      />
    );
  } catch (err) {
    return <div style={{ fontFamily: 'monospace', fontSize: '0.9rem', margin: '0.5rem 0' }}>$${math}$$</div>;
  }
};

export const MathInline: React.FC<{ math: string }> = ({ math }) => {
  try {
    const html = katex.renderToString(math, { 
      displayMode: false, 
      throwOnError: false,
      macros: qbdMacros 
    });
    return <span dangerouslySetInnerHTML={{ __html: html }} />;
  } catch (err) {
    return <span>${math}$</span>;
  }
};

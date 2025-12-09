import type { Config } from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import { themes as prismThemes } from 'prism-react-renderer';

// QBD Specific LaTeX Macros from your Symbol Table
const qbdMacros = {
  // Logic & Time
  "\\tL": "t_L",                                   // Global Logical Time
  "\\tphys": "t_{phys}",                           // Physical Time
  "\\Gadel": "\\mathcal{G}_{adel}",                // Gödel sentence
  "\\Con": "\\operatorname{Con}",                  // Consistency
  
  // Operators & State
  "\\ket": "\\left| #1 \\right\\rangle",           // Dirac Ket
  "\\bra": "\\left\\langle #1 \\right|",           // Dirac Bra
  "\\braket": "\\langle #1 | #2 \rangle",          // Inner Product
  "\\Evol": "\\mathcal{U}",                        // Universal Evolution Operator
  "\\Hamiltonian": "\\hat{H}",
  "\\Perm": "\\hat{P}",                            // Permutation Operator
  
  // Probability & Thermodynamics
  "\\Prob": "\\mathbb{P}",                         // Probability measure
  "\\Exp": "\\mathbb{E}",                          // Expected value
  "\\card": "\\left| #1 \\right|",                 // Cardinality
  "\\Ent": "S(U_{\\tL})",                          // Universal Entropy
  
  // Graph & Topology
  "\\Graph": "G=(V, E)",
  "\\Hist": "\\mathbf{Hist}",                      // Global Historical Category
  "\\Caus": "\\mathbf{Caus}_t",                    // Internal Causal Category
  "\\braid": "\\beta",                             // Braid variable
  "\\writhe": "w(\\beta)",                         // Writhe
  
  // QBD Specifics
  "\\geom": "\\gamma",                             // Geometric Quantum (3-cycle)
  "\\syndrome": "\\sigma",                         // Syndrome
  "\\ash": "\\text{ash}",                          // Dark Matter defects
};

const config: Config = {
  title: 'Quantum Braid Dynamics',
  tagline: 'The universe is not a thing, it is relation.',
  url: 'https://braiddynamics.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  favicon: 'img/favicon.ico',

  // Enable Mermaid for Flowcharts (Appendix C)
  markdown: {
    mermaid: true,
  },
  themes: ['@docusaurus/theme-mermaid'],

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          routeBasePath: '/monograph', // Serves your book at /monograph instead of /docs
          remarkPlugins: [require('remark-math')],
          rehypePlugins: [[require('rehype-katex'), { 
            strict: false, 
            macros: qbdMacros 
          }]],
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  stylesheets: [
    {
      href: 'https://cdn.jsdelivr.net/npm/katex@0.13.24/dist/katex.min.css',
      type: 'text/css',
      integrity: 'sha384-odtC+0UGzzFL/6PNoE8rX/SPcQDXBJ+uRepguP4QkPCm2LBxH3FA3yAd8i6Qq0',
      crossorigin: 'anonymous',
    },
  ],

  themeConfig: {
    navbar: {
      title: 'QBD',
      // We temporarily comment out the logo until you add the file, to prevent build errors
      // logo: { alt: 'QBD Logo', src: 'img/logo.svg' }, 
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar', 
          position: 'left',
          label: 'The Monograph',
        },
        { to: '/monograph/notation', label: 'Notation', position: 'left' },
        { href: 'https://github.com/braiddynamics/qbd-portal', label: 'GitHub', position: 'right' },
      ],
    },
    footer: {
      style: 'dark',
      copyright: `Copyright © ${new Date().getFullYear()} Quantum Braid Dynamics.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
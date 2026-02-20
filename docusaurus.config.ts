import type { Config } from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import { themes as prismThemes } from 'prism-react-renderer';

// QBD Specific LaTeX Macros
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
  tagline: 'Unifying General Relativity and the Standard Model',
  url: 'https://braiddynamics.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  
  // Pointing the site icon to logo
  favicon: 'img/logo.png',

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
          routeBasePath: '/monograph',
          remarkPlugins: [require('remark-math')],
          rehypePlugins: [[require('rehype-katex'), { 
            strict: false, 
            macros: qbdMacros 
          }]],
        },
        theme: {
          customCss: './src/css/main.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    navbar: {
      style: 'dark',
      title: 'QBD',
      logo: { alt: 'QBD Logo', src: 'img/logo.png' }, 
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar', 
          position: 'left',
          label: 'The Monograph',
        },
        { to: '/monograph/appendices/notation', label: 'Notation', position: 'left' },
        { 
          href: 'https://github.com/braiddynamics/qbd-portal', 
          position: 'right', 
          className: 'header-github-link', 
          'aria-label': 'GitHub repository',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [], 
      copyright: `Copyright © ${new Date().getFullYear()} Braid Dynamics. <a href="/legal" style="color: inherit; text-decoration: underline; margin-left: 10px;">Legal & License</a>`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
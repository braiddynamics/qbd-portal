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

import path from 'path';
import fs from 'fs';

function papersAssetsPlugin() {
  return {
    name: 'papers-assets-plugin',
    async postBuild({ outDir }: { outDir: string }) {
      const srcDir = path.join(__dirname, 'papers');
      const destDir = path.join(outDir, 'papers');
      const paperDirs = [
        'vacuum-phase',
        'causal-invariance-hypergraphs',
        'maximal-entropy-random-walk',
        'comments/js-riverfield',
      ];
      const assetSubdirs = ['downloads', 'simulations', 'code', 'data', 'figures'];
      for (const p of paperDirs) {
        for (const a of assetSubdirs) {
          const src = path.join(srcDir, p, a);
          const dest = path.join(destDir, p, a);
          if (fs.existsSync(src)) {
            fs.cpSync(src, dest, { recursive: true });
          }
        }
        const pSrc = path.join(srcDir, p);
        const pDest = path.join(destDir, p);
        if (fs.existsSync(pSrc)) {
          const files = fs.readdirSync(pSrc);
          for (const f of files) {
            if (f.endsWith('.png') || f.endsWith('.jpg') || f.endsWith('.svg') || f.endsWith('.pdf')) {
              fs.cpSync(path.join(pSrc, f), path.join(pDest, f));
            }
          }
        }
      }
    },
    configureWebpack(): any {
      return {
        devServer: {
          static: [
            {
              directory: path.join(__dirname, 'papers'),
              publicPath: '/papers',
            },
          ],
        },
      };
    },
  };
}

const config: Config = {
  title: 'Quantum Braid Dynamics',
  tagline: 'A Computational Process of Discrete Gravity',
  url: 'https://braiddynamics.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',

  markdown: {
    mermaid: true,
  },
  themes: ['@docusaurus/theme-mermaid'],

  future: {
    faster: true,
    v4: {
      removeLegacyPostBuildHeadAttribute: true,
    },
  },

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

  plugins: [
    papersAssetsPlugin,
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'papers',
        path: 'papers',
        routeBasePath: 'papers',
        sidebarPath: false,
        exclude: [
          '**/downloads/**',
          '**/simulations/**',
          '**/code/**',
          '**/data/**',
        ],
        remarkPlugins: [require('remark-math')],
        rehypePlugins: [[require('rehype-katex'), {
          strict: false,
          macros: qbdMacros,
        }]],
      },
    ],
  ],

  themeConfig: {
    image: 'img/qbd-social-card.png',

    navbar: {
      hideOnScroll: true,
      style: 'dark',
      title: 'QBD',
      logo: { alt: 'QBD Logo', src: 'img/logo.png' },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Table of Contents',
        },
        { to: '/spectrum', label: 'Braid Model', position: 'left' },
        { to: '/papers', label: 'Papers', position: 'left' },
        { to: '/ai', label: 'AI Portal', position: 'left' },
        { to: '/monograph/download', label: 'Downloads', position: 'left' },
        {
          href: 'https://github.com/braiddynamics/qbd-portal',
          label: 'Github',
          position: 'left',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [],
      copyright: `Copyright © ${new Date().getFullYear()} Braid Dynamics. <a href="/legal" style="color: inherit; text-decoration: underline; margin-left: 10px;">Legal &amp; License</a>`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
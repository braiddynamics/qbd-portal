import React, { useState } from 'react';
import Link from '@docusaurus/Link';
import FadeInView from './fade-in-view';
import DagGraphic from './graphics/dag-graphic';
import BraidGraphic from './graphics/braid-graphic';
import GeodesicGraphic from './graphics/geodesic-graphic';
import SCurveGraphic from './graphics/scurve-graphic';
import InfinityGraphic from './graphics/infinity-graphic';
import AppendixGraphic from './graphics/appendix-graphic';

interface MonographCardProps {
    section: {
        part: string | number;
        title: string;
        subtitle: string;
        linkUrl: string;
    };
}

interface ChapterInfo {
    num: number | string;
    shortName: string;
    title: string;
    description: string;
    linkUrl: string;
}

const part1Chapters: ChapterInfo[] = [
    { num: 1, shortName: "Ontology", title: "Chapter 1: Substrate (Ontology)", description: "Defines the fundamental dual-time architecture and relational graph G=(V, E, H) as the minimal substrate of existence.", linkUrl: "/monograph/rules/ontology/1.1" },
    { num: 2, shortName: "Axioms", title: "Chapter 2: Constraints (Axioms)", description: "Formulates the strict axiomatic bounds, including irreflexivity, acyclicity, and no-cloning, that prevent causal paradoxes.", linkUrl: "/monograph/rules/axioms/2.1" },
    { num: 3, shortName: "Architecture", title: "Chapter 3: Object Model (Architecture)", description: "Constructs the initial Bethe vacuum tree: a symmetric pre-geometric state poised for symmetry-breaking.", linkUrl: "/monograph/rules/architecture/3.1" },
    { num: 4, shortName: "Dynamics", title: "Chapter 4: Operations (Dynamics)", description: "Animates the relational substrate with a universal constructor, driving local topological updates.", linkUrl: "/monograph/rules/dynamics/4.1" },
    { num: 5, shortName: "Equilibrium", title: "Chapter 5: Geometrogenesis (Equilibrium)", description: "Demonstrates how thermodynamic equilibrium drives the transition from graph dynamics to continuous spacetime.", linkUrl: "/monograph/rules/equilibrium/5.1" }
];

const part2Chapters: ChapterInfo[] = [
    { num: 6, shortName: "Fermions", title: "Chapter 6: Tripartite Braid (Fermions)", description: "Models elementary fermions as stable, chiral braids of three active strands, deriving physical structures from topological invariants.", linkUrl: "/monograph/players/fermions/6.1" },
    { num: 7, shortName: "Topology", title: "Chapter 7: Quantum Numbers (Topology)", description: "Maps the discrete topological invariants of braids to physical quantum numbers: electric charge, spin, and color.", linkUrl: "/monograph/players/topology/7.1" },
    { num: 8, shortName: "Symmetries", title: "Chapter 8: Gauge Symmetries (Braids)", description: "Derives standard model gauge symmetries as emergent topological transformations and transitions of the local braid group.", linkUrl: "/monograph/players/braids/8.1" },
    { num: 9, shortName: "Unification", title: "Chapter 9: Generations and Decay (Unification)", description: "Explains the three generations of matter and their decay paths through braid rewrites and topological transitions.", linkUrl: "/monograph/players/unification/9.1" },
    { num: 10, shortName: "Computation", title: "Chapter 10: Quantum Universality (Computation)", description: "Demonstrates that braid-group operations form a computationally universal set, mapping physics to discrete quantum computation.", linkUrl: "/monograph/players/computation/10.1" }
];

const part3Chapters: ChapterInfo[] = [
    { num: 11, shortName: "Discrete", title: "Chapter 11: Differential Geometry (Discrete)", description: "Defines a discrete formulation of differential geometry directly on the causal set network without coordinate charts.", linkUrl: "/monograph/stage/discrete/11.1" },
    { num: 12, shortName: "Convergence", title: "Chapter 12: Continuum Limit (Convergence)", description: "Mathematically proves the convergence of the discrete causal set graph to a smooth, continuous macroscopic manifold.", linkUrl: "/monograph/stage/reconstruction/12.1" },
    { num: 13, shortName: "Einstein", title: "Chapter 13: Discrete Field Equations (Einstein)", description: "Formulates discrete Einstein field equations, deriving gravity as the manifestation of causal curvature and flow.", linkUrl: "/monograph/stage/dynamics/13.1" },
    { num: 14, shortName: "Time", title: "Chapter 14: Lorentzian Reality (Time)", description: "Derives the Lorentzian metric signature and the directionality of time directly from discrete causal acyclicity.", linkUrl: "/monograph/stage/time/14.1" },
    { num: 15, shortName: "EPR", title: "Chapter 15: Geometry of Entanglement (ER = EPR)", description: "Formalizes the ER = EPR conjecture inside QBD, proving that quantum entanglement is isomorphic to microscopic topological wormholes.", linkUrl: "/monograph/stage/epr/15.1" },
    { num: 16, shortName: "Holography", title: "Chapter 16: Isomorphism Principle (Holography)", description: "Proves the holographic boundary-to-bulk isomorphism, mapping quantum events on the boundary to bulk causal set dynamics.", linkUrl: "/monograph/stage/holography/16.1" },
    { num: 17, shortName: "Worldsheets", title: "Chapter 17: String Limit (Worldsheets)", description: "Recovers standard string theory worldsheets as the 2D continuum limit of dense causal set braids.", linkUrl: "/monograph/stage/worldsheets/17.1" }
];

const part4Chapters: ChapterInfo[] = [
    { num: 18, shortName: "Inflation", title: "Chapter 18: Big Kindling (Inflation)", description: "Establishes exponential spatial expansion and scale-invariant fluctuations from autocatalytic ribbon network branching.", linkUrl: "/monograph/output/inflation/18.1" },
    { num: 19, shortName: "Nucleosynthesis", title: "Chapter 19: Hot Universe (Nucleosynthesis)", description: "Models primordial nuclear freeze-out and cosmological light element abundances from discrete trivalent fusion kinetics.", linkUrl: "/monograph/output/nucleosynthesis/19.1" },
    { num: 20, shortName: "Web", title: "Chapter 20: Structured Universe (Cosmic Web)", description: "Derives cosmic filamentation, void formation, and baryonic acoustic oscillation harmonics on expanding graph topologies.", linkUrl: "/monograph/output/web/20.1" },
    { num: 21, shortName: "Relics", title: "Chapter 21: Dark Sector (Relics)", description: "Identifies cold dark matter candidates and cosmic coincidences as uncharged topological ribbon knot invariants.", linkUrl: "/monograph/output/relics/21.1" },
    { num: 22, shortName: "Extremes", title: "Chapter 22: Singularities & Condensates (Extremes)", description: "Resolves black hole singularities into saturated graph condensates with unitary horizon evaporation and topological superconductivity.", linkUrl: "/monograph/output/extremes/22.1" }
];

const part5Chapters: ChapterInfo[] = [
    { num: 23, shortName: "Universality", title: "Chapter 23: Operational Verification (Universality)", description: "Formulates laboratory test protocols across Rydberg simulators, quantum processor benchmarks, and optomechanical bounds.", linkUrl: "/monograph/conclusion/universality/23.1" },
    { num: 24, shortName: "Derivations", title: "Chapter 24: Non-Perturbative Foundations & The Mass Gap (Derivations)", description: "Non-perturbative derivation of the Yang-Mills mass gap, dimensional transmutation, and tripartite color confinement.", linkUrl: "/monograph/conclusion/derivations/24.1" },
    { num: 25, shortName: "Synthesis", title: "Chapter 25: Architectural Synthesis (Synthesis)", description: "Architectural synthesis of the cosmos as a closed, self-correcting causal network with comonadic measurement and conformal renewal.", linkUrl: "/monograph/conclusion/synthesis/25.1" }
];

const part6Chapters: ChapterInfo[] = [
    { num: "A", shortName: "References", title: "Appendix A: External References Cited", description: "Comprehensive bibliography of peer-reviewed literature, historical foundations, and foundational mathematical citations.", linkUrl: "/monograph/appendices/a-references" },
    { num: "B", shortName: "Simulations", title: "Appendix B: Python Simulation Models", description: "Numerical simulation scripts, Monte Carlo algorithms, and empirical verification packages validating QBD theorems.", linkUrl: "/monograph/appendices/b-sim-models" },
    { num: "C", shortName: "Notation", title: "Appendix C: Notation & Symbol Table", description: "Global mathematical notation ledger, operators, topological invariants, and physical units across all chapters.", linkUrl: "/monograph/appendices/notation" }
];

const getChaptersForPart = (partNum: string | number): ChapterInfo[] => {
    const p = String(partNum);
    if (p === "1") return part1Chapters;
    if (p === "2") return part2Chapters;
    if (p === "3") return part3Chapters;
    if (p === "4") return part4Chapters;
    if (p === "5") return part5Chapters;
    if (p === "6") return part6Chapters;
    return [];
};

export default function MonographCard({ section }: MonographCardProps) {
    const chapters = getChaptersForPart(section.part);
    const hasTabs = chapters.length > 0;
    
    // Unified sticky state tracking for hovering/tapping
    const [isCardHovered, setIsCardHovered] = useState(false);
    const [activeChapterNum, setActiveChapterNum] = useState<number | string | null>(null);
    
    const activeChapter = activeChapterNum !== null 
        ? chapters.find(ch => ch.num === activeChapterNum) 
        : null;

    const displayTitle = activeChapter ? activeChapter.title : section.title;
    const displaySubtitle = activeChapter ? activeChapter.description : section.subtitle;
    const displayLink = activeChapter ? activeChapter.linkUrl : section.linkUrl;
    
    // Action button text updates based on active chapter
    const isAppendix = String(section.part) === "6";
    const buttonText = activeChapter 
        ? (isAppendix 
            ? `Read Appendix ${activeChapter.num} →` 
            : `Read Chapter ${activeChapter.num} →`)
        : (isAppendix 
            ? `Explore Appendices →` 
            : `Read Part ${section.part} →`);

    const cardContent = (
        <div className="qbd-interactive-card-content section-grid-2col" style={{ height: '100%' }}>
            {/* Column 1: Typography (Dynamic Title, Description, and Bottom Button) */}
            <div className="section-text" style={{ textAlign: 'center', display: 'flex', flexDirection: 'column', height: '100%', minHeight: '16.5rem', justifyContent: 'space-between', minWidth: 0, width: '100%' }}>
                <div>
                    <h3 style={{ fontSize: '1.9rem', marginBottom: '0.6rem', fontWeight: 'bold', lineHeight: '1.2', minHeight: '4.8rem', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                        {displayTitle}
                    </h3>
                    <h4 style={{ marginBottom: '1.5rem', color: 'var(--ifm-color-primary)', fontSize: '1.15rem', fontWeight: 'normal', fontStyle: 'italic', minHeight: '4.5rem', display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '0 0.5rem', lineHeight: '1.5' }}>
                        {displaySubtitle}
                    </h4>
                </div>
                <div>
                    <span className="button button--secondary button--lg" style={{ fontWeight: 'bold' }}>
                        {buttonText}
                    </span>
                </div>
            </div>

            {/* Column 2: Enhanced Graphic Layout Container */}
            <div 
                className="placeholder-box" 
                style={{ 
                    padding: 0, 
                    backgroundColor: 'transparent', 
                    border: 'none',
                    display: 'flex',
                    justifyContent: 'center',
                    alignItems: 'center',
                    transform: 'scale(1.15)',
                    transition: 'transform 0.3s ease',
                    minWidth: 0,
                    width: '100%'
                }}
            >
                {section.part === "1" ? <DagGraphic /> : 
                 section.part === "2" ? <BraidGraphic /> : 
                 section.part === "3" ? <GeodesicGraphic /> : 
                 section.part === "4" ? <SCurveGraphic /> : 
                 section.part === "5" ? <InfinityGraphic /> : 
                 section.part === "6" ? <AppendixGraphic /> : 
                 <span>[ Graphic Placeholder ]</span>}
            </div>
        </div>
    );

    if (hasTabs) {
        return (
            <FadeInView>
                <div 
                    className="qbd-interactive-card section-row-margin"
                    onMouseEnter={() => setIsCardHovered(true)}
                    onMouseLeave={() => {
                        setIsCardHovered(false);
                        setActiveChapterNum(null); // Resets selection back to Part view on mouse exit
                    }}
                    style={{ position: 'relative', display: 'block', padding: '3.5rem 2.5rem 2.5rem 2.5rem', maxWidth: '950px', width: '100%', marginLeft: 'auto', marginRight: 'auto' }}
                >
                    {/* Hanging Folder Tabs with slant styling */}
                    <div 
                        className="qbd-folder-tabs-container"
                        style={{
                            opacity: isCardHovered || activeChapterNum !== null ? 1 : 0,
                            pointerEvents: isCardHovered || activeChapterNum !== null ? 'auto' : 'none',
                            transform: isCardHovered || activeChapterNum !== null ? 'translateY(0)' : 'translateY(-6px)',
                            transition: 'opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1), transform 0.3s cubic-bezier(0.16, 1, 0.3, 1)'
                        }}
                    >
                        {chapters.map(ch => (
                            <div
                                key={ch.num}
                                onMouseEnter={() => setActiveChapterNum(ch.num)}
                                onClick={(e) => {
                                    e.preventDefault();
                                    e.stopPropagation();
                                    setActiveChapterNum(ch.num);
                                }}
                                className={`qbd-folder-tab ${activeChapterNum === ch.num ? 'active' : ''}`}
                            >
                                <span>{ch.shortName}</span>
                            </div>
                        ))}
                    </div>

                    {/* Make the card itself linkable to the active selection */}
                    <Link to={displayLink} style={{ display: 'block', textDecoration: 'none', color: 'inherit' }}>
                        {cardContent}
                    </Link>
                </div>
            </FadeInView>
        );
    }

    return (
        <FadeInView>
            <Link
                to={section.linkUrl}
                className="qbd-interactive-card section-row-margin"
                style={{ display: 'block', textDecoration: 'none', color: 'inherit', maxWidth: '950px', width: '100%', marginLeft: 'auto', marginRight: 'auto' }}
            >
                {cardContent}
            </Link>
        </FadeInView>
    );
}
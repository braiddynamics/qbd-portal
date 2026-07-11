# /model/braids.py
"""
Topological braid / fermion layer.

Provides data structures and mass hierarchy calculations for tripartite
braids, as well as helpers for defect injection and deletion barriers.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import networkx as nx

# Anchored mass scale: m_e / N_e with N_e = 3 for the electron.
KAPPA_M_DEFAULT = 0.511 / 3.0  # MeV per net complexity unit


@dataclass(frozen=True)
class WritheConfig:
    """
    Integer writhe triple (w0, w1, w2) for a tripartite braid.

    Conventions (mass hierarchy):
      - Lepton: (-w, -w, -w)
      - D-type: (-w, 0, 0)
      - U-type: (w, w, 0)
    """
    w0: int
    w1: int
    w2: int
    name: str = ""
    family: str = ""  # "lepton" | "d_type" | "u_type" | ""

    @property
    def triple(self) -> Tuple[int, int, int]:
        return (self.w0, self.w1, self.w2)


@dataclass(frozen=True)
class Ribbon:
    """Ordered path of one strand (optional graph embedding)."""
    path: Tuple[int, ...]
    writhe: int = 0


@dataclass(frozen=True)
class Braid:
    """Tripartite braid as three ribbons plus abstract writhe config."""
    config: WritheConfig
    ribbons: Optional[Tuple[Ribbon, Ribbon, Ribbon]] = None


# --- Complexity / mass (from hierarchy formulas) ---

def net_complexity(config: WritheConfig) -> float:
    """
    Net topological complexity N_net from writhe config.

    Lepton:  3 w^2
    D-type:  w^2
    U-type:  2 w^2 - w   (parallel sharing)
    Generic: fall back to sum of squares of absolute writhes.
    """
    family = (config.family or "").lower()
    w0, w1, w2 = config.triple

    if family == "lepton":
        w = abs(w0)
        return float(3 * w * w)
    if family == "d_type":
        w = max(abs(w0), abs(w1), abs(w2))
        return float(w * w)
    if family == "u_type":
        # (w, w, 0) → 2w^2 - w
        vals = sorted((abs(w0), abs(w1), abs(w2)), reverse=True)
        w = vals[0]
        return float(2 * w * w - w)

    # Generic fallback: sum of squared writhes (no sharing credit).
    return float(w0 * w0 + w1 * w1 + w2 * w2)


def topological_mass(config: WritheConfig, kappa_m: float = KAPPA_M_DEFAULT) -> float:
    """Rest mass estimate m = κ_m * N_net (MeV)."""
    return kappa_m * net_complexity(config)


def lepton_config(w: int, name: str = "") -> WritheConfig:
    return WritheConfig(-w, -w, -w, name=name or f"lepton_w{w}", family="lepton")


def d_type_config(w: int, name: str = "") -> WritheConfig:
    return WritheConfig(-w, 0, 0, name=name or f"d_type_w{w}", family="d_type")


def u_type_config(w: int, name: str = "") -> WritheConfig:
    return WritheConfig(w, w, 0, name=name or f"u_type_w{w}", family="u_type")


# SM best-fit integer writhe table (from hierarchy verification script).
STANDARD_MODEL_WRITHE: Dict[str, WritheConfig] = {
    "Electron": lepton_config(1, "Electron"),
    "Muon": lepton_config(14, "Muon"),
    "Tau": lepton_config(59, "Tau"),
    "Down": d_type_config(1, "Down"),
    "Strange": d_type_config(24, "Strange"),
    "Bottom": d_type_config(157, "Bottom"),
    "Up": u_type_config(1, "Up"),
    "Charm": u_type_config(62, "Charm"),
    "Top": u_type_config(712, "Top"),
}

SM_EMPIRICAL_MASS_MEV: Dict[str, float] = {
    "Electron": 0.511,
    "Muon": 105.66,
    "Tau": 1776.8,
    "Down": 4.7,
    "Strange": 95.0,
    "Bottom": 4180.0,
    "Up": 2.2,
    "Charm": 1275.0,
    "Top": 172900.0,
}


def mass_hierarchy_table(
    kappa_m: float = KAPPA_M_DEFAULT,
) -> List[Dict[str, float]]:
    """Compute topological masses for the standard writhe dictionary."""
    rows = []
    for name, cfg in STANDARD_MODEL_WRITHE.items():
        m_topo = topological_mass(cfg, kappa_m)
        m_emp = SM_EMPIRICAL_MASS_MEV[name]
        delta_pct = abs(m_topo - m_emp) / m_emp * 100.0 if m_emp else float("nan")
        rows.append({
            "name": name,
            "N_net": net_complexity(cfg),
            "mass_topo_MeV": m_topo,
            "mass_empirical_MeV": m_emp,
            "delta_pct": delta_pct,
        })
    return rows


# --- Graph embedding (opt-in; does not alter default dynamics) ---

def inject_tripartite_cycle(
    G: nx.DiGraph,
    nodes: Optional[Sequence[int]] = None,
    H: int = 1,
) -> Tuple[nx.DiGraph, Braid]:
    """
    Inject a minimal tripartite 3-cycle braid into G (in-place).

    If nodes is None, uses (0,1,2) if present, else the first three nodes.
    Returns (G, Braid) with electron ground-state writhe config.
    """
    if nodes is None:
        existing = list(G.nodes())
        if {0, 1, 2}.issubset(existing):
            a, b, c = 0, 1, 2
        elif len(existing) >= 3:
            a, b, c = existing[0], existing[1], existing[2]
        else:
            a, b, c = 0, 1, 2
            for n in (a, b, c):
                if n not in G:
                    G.add_node(n)
    else:
        a, b, c = nodes[0], nodes[1], nodes[2]
        for n in (a, b, c):
            if n not in G:
                G.add_node(n)

    # Ensure cycle a→b→c→a with timestamps.
    for u, v in ((a, b), (b, c), (c, a)):
        if G.has_edge(u, v):
            G.edges[u, v]["H"] = G.edges[u, v].get("H", H)
        else:
            G.add_edge(u, v, H=H)

    cfg = lepton_config(1, "injected_electron")
    ribbons = (
        Ribbon((a, b), writhe=-1),
        Ribbon((b, c), writhe=-1),
        Ribbon((c, a), writhe=-1),
    )
    return G, Braid(config=cfg, ribbons=ribbons)


def deletion_barrier_active(rho_local: float, rho_core: float = 0.082) -> bool:
    """
    Topological protection: below core density, prime-knot deletion freezes
    (cluster-decay model). Opt-in for extended sims only.
    """
    return rho_local <= rho_core


def flux_balance(rho: float, mu: float = 0.3989, lam: float = 1.7183,
                 lambda_vac: float = 0.0156) -> Tuple[float, float, float]:
    """
    Mean-field creation/deletion fluxes from the Master Equation.

    Returns (J_in, J_out, dρ/dt).
    """
    j_in = (lambda_vac + 9.0 * rho ** 2) * math_exp_neg_friction(mu, rho)
    j_out = 0.5 * rho + 3.0 * lam * rho ** 2
    return j_in, j_out, j_in - j_out


def math_exp_neg_friction(mu: float, rho: float) -> float:
    import math
    return math.exp(-6.0 * mu * rho)


def su2_local_dof_count() -> int:
    """
    SU(2) local channels on a 3-cycle: 3 edges × 2 flavor flips + 1 stabilizer = 7.
    """
    return 3 * 2 + 1

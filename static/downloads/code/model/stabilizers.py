# /model/stabilizers.py
"""
Classical stabilizer / syndrome layer.

Provides hard-constraint checks, triplet syndrome classification, and
stabilizer syndrome evaluations.
"""
from __future__ import annotations

from typing import Dict, Hashable, Iterable, List, Optional, Set, Tuple

import networkx as nx

from model.utils import find_all_3_cycles

# Syndrome eigenvalue conventions: +1 = edge absent, -1 = edge present
# for the geometric Z-checks on directed edges (classical bit embedding).


def edge_present(G: nx.DiGraph, u: Hashable, v: Hashable) -> bool:
    return G.has_edge(u, v)


def z_eigenvalue(G: nx.DiGraph, u: Hashable, v: Hashable) -> int:
    """
    Classical Z on edge qubit: |0> (absent) → +1, |1> (present) → -1.
    """
    return -1 if G.has_edge(u, v) else +1


def has_2_cycle(G: nx.DiGraph, u: Hashable, v: Hashable) -> bool:
    """True if both (u,v) and (v,u) exist (hard axiom violation)."""
    return G.has_edge(u, v) and G.has_edge(v, u)


def hard_2cycle_projectors_satisfied(G: nx.DiGraph) -> bool:
    """
    Π_cycle: no mutual 2-cycles on any undirected pair.
    """
    for u, v in G.edges():
        if G.has_edge(v, u):
            return False
    return True


def edge_has_length2_support(G: nx.DiGraph, u, v) -> bool:
    """True if u and v share an undirected common neighbor (triangle/2-path face)."""
    U = G.to_undirected()
    if not U.has_edge(u, v) and not G.has_edge(u, v):
        return False
    return bool(set(U.neighbors(u)) & set(U.neighbors(v)))


def count_unsupported_chords(G: nx.DiGraph) -> int:
    """
    Diagnostic: undirected edges that are neither bridges nor length-2 supported.

    After densification, original tree edges often gain long alternate paths
    without a common neighbor — they look like "chords" under a post-hoc
    check even if they were local at insertion. Treat as a metric, not a
    hard fail, unless you track support history.
    """
    if G.number_of_nodes() <= 2:
        return 0
    U = G.to_undirected()
    bad = 0
    for u, v in list(U.edges()):
        if set(U.neighbors(u)) & set(U.neighbors(v)):
            continue
        U.remove_edge(u, v)
        try:
            if nx.has_path(U, u, v):
                bad += 1  # non-bridge without length-2 support
        finally:
            if not U.has_edge(u, v):
                U.add_edge(u, v)
    return bad


def hard_locality_projectors_satisfied(
    G: nx.DiGraph,
    max_undirected_distance: int = 2,
) -> bool:
    """
    Strict post-hoc locality proxy (often fails on densified vacua).

    §3.5 Π_local constrains *proposal* sites (no long-range edge creation).
    The shared micro-rule already enforces that adds close 2-paths (local).
    A post-hoc scan of the residual graph is NOT equivalent: tree edges that
    later acquire long detours register as failures here.

    Prefer count_unsupported_chords as a diagnostic. This boolean is kept for
    explicit --require-locality experiments and is expected to be brittle.
    """
    if G.number_of_nodes() <= 2:
        return True
    # Strict: zero unsupported chords
    return count_unsupported_chords(G) == 0


def hard_projectors_satisfied(G: nx.DiGraph) -> bool:
    """Codespace proxy: hard 2-cycle and locality projectors all pass."""
    return hard_2cycle_projectors_satisfied(G) and hard_locality_projectors_satisfied(G)


def triplet_syndrome(
    G: nx.DiGraph,
    u: Hashable,
    v: Hashable,
    w: Hashable,
) -> Tuple[int, int, int]:
    """
    Geometric syndrome tuple (lambda_uv, lambda_vw, lambda_wu).
    """
    return (
        z_eigenvalue(G, u, v),
        z_eigenvalue(G, v, w),
        z_eigenvalue(G, w, u),
    )


def classify_triplet_syndrome(syndrome: Tuple[int, int, int]) -> str:
    """
    Coarse classification of triplet edge occupation patterns.
    """
    n_present = sum(1 for s in syndrome if s == -1)
    if n_present == 0:
        return "empty"
    if n_present == 1:
        return "single_edge"
    if n_present == 2:
        return "two_path"
    # three edges present: could be a directed 3-cycle or a tournament mess
    return "triangle"


def is_directed_3_cycle(G: nx.DiGraph, u: Hashable, v: Hashable, w: Hashable) -> bool:
    return G.has_edge(u, v) and G.has_edge(v, w) and G.has_edge(w, u)


def all_triplet_syndromes(
    G: nx.DiGraph,
    max_triplets: Optional[int] = 500,
) -> List[Dict]:
    """
    Enumerate syndromes for ordered triplets that have at least one edge.
    Caps enumeration for large graphs.
    """
    nodes = list(G.nodes())
    results = []
    count = 0
    n = len(nodes)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if k == i or k == j:
                    continue
                u, v, w = nodes[i], nodes[j], nodes[k]
                # Skip completely empty triplets for efficiency.
                if not (G.has_edge(u, v) or G.has_edge(v, w) or G.has_edge(w, u)):
                    continue
                syn = triplet_syndrome(G, u, v, w)
                results.append({
                    "triplet": (u, v, w),
                    "syndrome": syn,
                    "class": classify_triplet_syndrome(syn),
                    "is_3_cycle": is_directed_3_cycle(G, u, v, w),
                })
                count += 1
                if max_triplets is not None and count >= max_triplets:
                    return results
    return results


def parity_stabilizer_eigenvalue(bits: Iterable[int]) -> int:
    """
    Classical multi-qubit Z⊗…⊗Z eigenvalue on bit string (0/1 occupations).
    Even parity → +1, odd parity → -1.
    """
    parity = sum(int(b) % 2 for b in bits) % 2
    return +1 if parity == 0 else -1


def geometric_cycle_stabilizer(G: nx.DiGraph, cycle_edges: List[Tuple]) -> int:
    """
    Z-parity check on the three edges of a 3-cycle support.
    Present edges count as bit 1.
    """
    bits = []
    for e in cycle_edges:
        if isinstance(e, tuple) and len(e) == 2:
            u, v = e
        else:
            u, v = tuple(e)
        bits.append(1 if G.has_edge(u, v) else 0)
    return parity_stabilizer_eigenvalue(bits)


def codespace_summary(G: nx.DiGraph) -> Dict[str, object]:
    """
    Aggregate hard-projector status and 3-cycle stabilizer snapshot.
    """
    cycles = find_all_3_cycles(G)
    cycle_evals = [geometric_cycle_stabilizer(G, c) for c in cycles]
    return {
        "hard_ok": hard_projectors_satisfied(G),
        "two_cycle_ok": hard_2cycle_projectors_satisfied(G),
        "n_3_cycles": len(cycles),
        "cycle_stabilizer_evals": cycle_evals,
        "all_cycle_stabilizers_minus_one": all(e == -1 for e in cycle_evals) if cycle_evals else True,
    }


def stabilizers_commute_on_supports(
    support_a: Set[int],
    support_b: Set[int],
    pauli_a: str = "Z",
    pauli_b: str = "Z",
) -> bool:
    """
    Commutation of Pauli products on qubit index supports.

    Z-type with Z-type always commute. X with Z commute iff |overlap| even.
    """
    overlap = len(support_a & support_b)
    if pauli_a == pauli_b:
        return True
    # X and Z (or mixed): commute on even overlap
    return (overlap % 2) == 0

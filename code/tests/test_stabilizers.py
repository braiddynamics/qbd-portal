# tests/test_stabilizers.py
import os
import sys

import networkx as nx
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from model.graph_setup import generate_zpi_vacuum, inject_energic_event
from model.stabilizers import (
    z_eigenvalue,
    hard_2cycle_projectors_satisfied,
    hard_projectors_satisfied,
    count_unsupported_chords,
    triplet_syndrome,
    classify_triplet_syndrome,
    is_directed_3_cycle,
    parity_stabilizer_eigenvalue,
    codespace_summary,
    stabilizers_commute_on_supports,
)


def test_z_eigenvalue_absent_present():
    G = nx.DiGraph([(0, 1)])
    assert z_eigenvalue(G, 0, 1) == -1
    assert z_eigenvalue(G, 1, 0) == +1


def test_hard_2cycle_detects_violation():
    G = nx.DiGraph([(0, 1), (1, 0)])
    assert hard_2cycle_projectors_satisfied(G) is False


def test_zpi_vacuum_satisfies_hard_2cycle():
    G, _ = generate_zpi_vacuum(20)
    assert hard_2cycle_projectors_satisfied(G) is True
    # Pure Bethe fragment: all undirected edges are bridges ⇒ no unsupported chords
    assert count_unsupported_chords(G) == 0
    assert hard_projectors_satisfied(G) is True


def test_triplet_syndrome_two_path_and_cycle():
    G = nx.DiGraph([(0, 1), (1, 2)])
    syn = triplet_syndrome(G, 0, 1, 2)
    assert classify_triplet_syndrome(syn) == "two_path"
    assert is_directed_3_cycle(G, 0, 1, 2) is False

    G.add_edge(2, 0)
    syn2 = triplet_syndrome(G, 0, 1, 2)
    assert classify_triplet_syndrome(syn2) == "triangle"
    assert is_directed_3_cycle(G, 0, 1, 2) is True


def test_parity_stabilizer_even_odd():
    assert parity_stabilizer_eigenvalue([0, 0, 0, 0]) == +1
    assert parity_stabilizer_eigenvalue([1, 1, 0, 0]) == +1
    assert parity_stabilizer_eigenvalue([1, 0, 0, 0]) == -1


def test_codespace_summary_after_ignition():
    G, levels = generate_zpi_vacuum(20)
    G = inject_energic_event(G, levels)
    summary = codespace_summary(G)
    assert summary["hard_ok"] is True
    assert summary["n_3_cycles"] >= 1
    assert summary["all_cycle_stabilizers_minus_one"] is True


def test_stabilizer_commutation_rules():
    assert stabilizers_commute_on_supports({0, 1, 2}, {3, 4, 5}, "Z", "Z")
    assert stabilizers_commute_on_supports({0, 1}, {0, 1, 2, 3}, "X", "Z")  # overlap 2 even
    assert stabilizers_commute_on_supports({0, 1}, {0}, "X", "Z") is False  # overlap 1 odd

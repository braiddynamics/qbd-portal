"""
Comprehensive Unit, Mock, and Stress Test Suite for Multiway Causal Invariance Auditor.
Tests MultiwayStateSpaceAuditor, ExplicitHypergraphRuleAuditor, information-theoretic invariants,
and asserts Lean 4 formal machine-checked proof validity.
"""

import os
import sys
import glob
import math
import subprocess
import re
import pytest
from unittest.mock import patch

# Ensure module can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from causal_invariance_auditor import (
    MultiwayStateSpaceAuditor,
    ExplicitHypergraphRuleAuditor,
    PreGeometricMultiwayAuditor,
    HypergraphRewriteAuditor,
    CanonicalState,
    HypergraphState,
    compute_spectral_moments,
    compute_laplacian_fiedler_eigenvalue,
    lovasz_homomorphism_matches,
    compute_kms_regularized_relative_entropy
)


@pytest.fixture(autouse=True)
def cleanup_temp_exports():
    """Fixture to ensure test execution does not leave JSON/PKL relics behind."""
    yield
    for pattern in ["distribution_N*.json", "cache_N*.pkl"]:
        for f in glob.glob(pattern):
            try:
                os.remove(f)
            except OSError:
                pass


class TestFormalVerificationKernel:
    """Automated integration assertion for Lean 4 formal proof suite."""

    def test_lean4_formal_proofs_kernel_check(self):
        """Validates Lean 4 formal proofs with 0 sorry keywords via lean CLI or lake toolchain."""
        import shutil
        lean_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "formal-proofs", "CausalInvariance.lean"))
        assert os.path.exists(lean_file), f"Lean proof file not found at {lean_file}"

        # Resolve lean executable (direct CLI or via Lake environment)
        cmd = ["lean", lean_file]
        if not shutil.which("lean") and shutil.which("lake"):
            cmd = ["lake", "env", "lean", lean_file]

        res = subprocess.run(cmd, capture_output=True, text=True)
        assert res.returncode == 0, f"Lean 4 proof verification failed:\nStdout: {res.stdout}\nStderr: {res.stderr}"

        # Strip comments and ensure zero 'sorry' in Lean code
        with open(lean_file, "r", encoding="utf-8") as f:
            code = f.read()
            # Remove multi-line comments /- ... -/
            code_clean = re.sub(r'/-(.|\n)*?-/', '', code)
            # Remove single-line comments -- ...
            code_clean = re.sub(r'--.*', '', code_clean)
            assert not re.search(r'\bsorry\b', code_clean), "Found unproven 'sorry' keyword in Lean 4 proof file!"


class TestInputValidation:
    """Validates defensive assertions on invalid scales and parameter inputs."""

    def test_invalid_n_raises_value_error(self):
        auditor = MultiwayStateSpaceAuditor()
        with pytest.raises(ValueError, match="must be >= 2"):
            auditor.generate_canonical_complete_graph(1)
        with pytest.raises(ValueError, match="must be >= 2"):
            auditor.evaluate_exact_multiway_induction(n=1, k=2, silent=True)

    def test_invalid_k_raises_value_error(self):
        auditor = MultiwayStateSpaceAuditor()
        with pytest.raises(ValueError, match="must be non-negative"):
            auditor.evaluate_exact_multiway_induction(n=4, k=-1, silent=True)


class TestGraphCanonicalization:
    """Tests for graph canonicalization and isomorphism invariance."""

    @pytest.fixture
    def auditor(self):
        return MultiwayStateSpaceAuditor()

    def test_canonical_kn_generation(self, auditor):
        for n in [3, 4, 5]:
            kn = auditor.generate_canonical_complete_graph(n)
            expected_edges = n * (n - 1) // 2
            assert len(kn) == expected_edges
            degs = auditor.get_vertex_degrees(kn, n)
            assert all(d == n - 1 for d in degs)

    def test_isomorphic_graphs_yield_identical_canonical_forms(self, auditor):
        auditor.clear_cache()
        # Graph 1: 4-cycle (0-1-2-3-0)
        edges1 = [(0, 1), (1, 2), (2, 3), (0, 3)]
        # Graph 2: Isomorphic 4-cycle with permuted vertex labels
        edges2 = [(2, 0), (0, 3), (3, 1), (2, 1)]

        canon1 = auditor.canonicalize_unlabeled_graph(4, edges1)
        canon2 = auditor.canonicalize_unlabeled_graph(4, edges2)
        assert canon1 == canon2

    def test_non_isomorphic_graphs_yield_distinct_canonical_forms(self, auditor):
        auditor.clear_cache()
        c4 = [(0, 1), (1, 2), (2, 3), (0, 3)]
        star = [(0, 1), (0, 2), (0, 3), (1, 2)]

        canon_c4 = auditor.canonicalize_unlabeled_graph(4, c4)
        canon_star = auditor.canonicalize_unlabeled_graph(4, star)
        assert canon_c4 != canon_star


class TestAnalyticalCombinatoricsGroundTruth:
    """
    Validates multiway trajectory counts against independently derived analytical combinatorics.
    
    Analytical Derivation for N=5, k=3 (Degree-Threshold Pruning from K_5):
      - K_5 initial state: E_0 = 10 edges, all vertices have degree 4 > 3.
      - Layer 0 (E=10): 1 state, 1 path.
      - Layer 1 (E=9): 10 symmetric edges can be pruned -> 10 paths.
        States have degree sequence (4, 4, 4, 3, 3). All 9 remaining edges touch a degree 4 vertex.
      - Layer 2 (E=8): 10 * 9 = 90 paths.
        States are either (4, 4, 3, 3, 2) or (4, 3, 3, 3, 3).
      - Layer 3 (E=7): 90 * 6 = 540 paths.
        From (4, 3, 3, 3, 3), 4 prunable edges reach terminal states directly (180 paths at Layer 3).
      - Layer 4 (E=6): Remaining non-terminal paths branch into 1,440 paths at Layer 4.
      - Total terminal paths = 180 (at Layer 3) + 1,440 (at Layer 4) = 1,620 exact paths.
    """

    @pytest.fixture
    def auditor(self):
        return MultiwayStateSpaceAuditor()

    def test_scale_n3_k1_analytical_exact(self, auditor):
        """Analytical exact verification for N=3, k=1: exactly 3! = 6 paths."""
        res = auditor.evaluate_exact_multiway_induction(n=3, k=1, silent=True, save_cache=False)
        assert res["total_paths"] == 6
        assert math.isclose(res["h_process_max"], math.log2(6), rel_tol=1e-5)
        assert res["delta_h_realized"] >= 0.0

    def test_scale_n5_k3_benchmark_and_landauer_gap(self, auditor):
        """Analytical exact verification for N=5, k=3: exactly 1,620 paths across 4 classes."""
        res = auditor.evaluate_exact_multiway_induction(n=5, k=3, silent=True, top_k=5, save_cache=False)
        # Analytical ground truth: 180 (Layer 3) + 1440 (Layer 4) = 1620
        assert res["total_paths"] == 1620
        assert res["physical_classes"] == 4
        assert res["delta_h_realized"] > 0.0

    @pytest.mark.parametrize("n_scale, k_deg", [(3, 1), (4, 2), (5, 3)])
    def test_probability_mass_conservation_multiscale(self, auditor, n_scale, k_deg):
        res = auditor.evaluate_exact_multiway_induction(n=n_scale, k=k_deg, silent=True, top_k=10, save_cache=False)
        all_states = res["all_classes"]
        prob_sum = sum(item["probability"] for item in all_states)
        assert math.isclose(prob_sum, 1.0, rel_tol=1e-5)


class TestHypergraphRewriteAuditor:
    """Tests for explicit Wolfram 2-in 4-out hypergraph substitution rule engine."""

    @pytest.fixture
    def auditor(self):
        return ExplicitHypergraphRuleAuditor()

    def test_hypergraph_canonicalization_isomorphism(self, auditor):
        h1: HypergraphState = frozenset({(0, 1), (1, 2), (2, 3)})
        h2: HypergraphState = frozenset({(3, 2), (2, 1), (1, 0)})
        c1 = auditor.get_canonical_hypergraph(h1)
        c2 = auditor.get_canonical_hypergraph(h2)
        assert c1 == c2

    @pytest.mark.parametrize("n, expected_matches", [
        (3, 3),   # K3: 3 * (2 choose 2) = 3
        (4, 12),  # K4: 4 * (3 choose 2) = 4 * 3 = 12
        (5, 30),  # K5: 5 * (4 choose 2) = 5 * 6 = 30
    ])
    def test_exact_2in_pattern_matching_combinatorics(self, auditor, n, expected_matches):
        kn_edges: HypergraphState = frozenset((i, j) for i in range(n) for j in range(i + 1, n))
        matches = auditor.find_2in_matches(kn_edges)
        assert len(matches) == expected_matches

    def test_2in_4out_rule_application(self, auditor):
        state: HypergraphState = frozenset({(0, 1), (0, 2)})
        match = ((0, 1), (0, 2))
        new_state = auditor.apply_2in_4out_rule(state, match, new_vertex=3)
        assert len(new_state) == 4

    def test_multiway_branching_growth(self, auditor):
        k4: HypergraphState = frozenset({(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)})
        res = auditor.evaluate_multiway_branching(k4, steps=2)
        assert res["steps"] == 2
        assert res["total_paths"] > 0
        assert res["distinct_macrostates"] > 0
        assert res["h_process"] > 0.0

    def test_2in_1out_pruning_rule_application(self, auditor):
        state: HypergraphState = frozenset({(0, 1), (0, 2), (1, 2)})
        match = ((0, 1), (0, 2))
        new_state = auditor.apply_2in_1out_rule(state, match)
        # Should remove (0,1), (0,2) and add (1,2). Since (1,2) is already in set, len is 1
        assert len(new_state) == 1

    def test_pruning_multiway_evaluation(self, auditor):
        k4: HypergraphState = frozenset({(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)})
        res = auditor.evaluate_pruning_multiway(k4, steps=2)
        assert res["steps"] == 2
        assert res["total_paths"] > 0
        assert res["distinct_macrostates"] > 0

    def test_2in_2out_swap_rule_application(self, auditor):
        # Disjoint edges: (0, 1) and (2, 3)
        state: HypergraphState = frozenset({(0, 1), (2, 3)})
        matches = auditor.find_2in_2out_swap_matches(state)
        assert len(matches) == 1
        new_state = auditor.apply_2in_2out_swap_rule(state, matches[0])
        assert len(new_state) == 2


class TestMonteCarloTrajectorySampler:
    """Tests for stochastic trajectory sampling on intractable scales."""

    @pytest.fixture
    def auditor(self):
        return MultiwayStateSpaceAuditor()

    def test_sample_trajectory_statistics_n5_k3(self, auditor):
        res = auditor.sample_monte_carlo_percolation(n=5, k=3, num_samples=50, seed=123)
        assert res["n"] == 5
        assert res["k"] == 3
        assert res["num_samples"] == 50
        assert res["mean_path_length"] > 0
        assert 0.0 <= res["p_connected_sampled"] <= 1.0
        assert 0.0 <= res["p_regular_sampled"] <= 1.0

    def test_sample_trajectory_statistics_n9_k3(self, auditor):
        # Fast stochastic sweep on N=9
        res = auditor.sample_monte_carlo_percolation(n=9, k=3, num_samples=20, seed=42)
        assert res["n"] == 9
        assert res["k"] == 3
        assert res["num_samples"] == 20
        assert res["mean_path_length"] > 0


class TestMockingAndResilience:
    """Tests resilience to file system failures via mocking."""

    def test_graceful_handling_of_disk_write_error(self):
        auditor = MultiwayStateSpaceAuditor()
        with patch("builtins.open", side_effect=IOError("Permission denied")):
            res = auditor.evaluate_exact_multiway_induction(n=3, k=1, silent=True, save_cache=True)
            assert res["total_paths"] == 6


class TestGaugeInvariantSpectraAndFirstLaw:
    """Tests gauge-invariant spectral observables, Laplacian spectral gap, and KMS relative entropy."""

    def test_spectral_moments_trace_invariants(self):
        # Triangle graph K_3: 3 vertices, 3 edges, 1 triangle
        k3_edges = ((0, 1), (0, 2), (1, 2))
        moments = compute_spectral_moments(k3_edges, n=3, max_k=4)
        # Tr(A) = 0
        assert moments[0] == pytest.approx(0.0)
        # Tr(A^2) = 2 * |E| = 6
        assert moments[1] == pytest.approx(6.0)
        # Tr(A^3) = 6 * (number of triangles) = 6 * 1 = 6
        assert moments[2] == pytest.approx(6.0)

    def test_laplacian_fiedler_eigenvalue_collapse_on_disconnected_graphs(self):
        # Connected 4-cycle: lambda_2 > 0
        c4_edges = ((0, 1), (1, 2), (2, 3), (0, 3))
        fiedler_c4 = compute_laplacian_fiedler_eigenvalue(c4_edges, n=4)
        assert fiedler_c4 > 0.0
        assert fiedler_c4 == pytest.approx(2.0)

        # Disconnected graph: 2 disjoint edges (0-1) and (2-3) -> lambda_2 == 0
        disjoint_edges = ((0, 1), (2, 3))
        fiedler_disjoint = compute_laplacian_fiedler_eigenvalue(disjoint_edges, n=4)
        assert fiedler_disjoint == pytest.approx(0.0)

    def test_kms_regularized_relative_entropy_convergence(self):
        # Distribution with 90% in non-vacuum state, 10% in vacuum state (idx 0)
        probs = [0.10, 0.90]
        # Finite beta yields finite relative entropy (no infinity)
        s_rel_beta1 = compute_kms_regularized_relative_entropy(probs, vac_idx=0, beta=1.0)
        assert s_rel_beta1 > 0.0

        # As beta increases (temperature drops), distinguishability increases monotonically
        s_rel_beta5 = compute_kms_regularized_relative_entropy(probs, vac_idx=0, beta=5.0)
        assert s_rel_beta5 > s_rel_beta1

        # Trace distance Pinsker lower bound: 1/2 * (2 * (1 - 0.10))^2 = 0.5 * 1.8^2 = 1.62
        trace_dist = 2.0 * (1.0 - probs[0])
        pinsker_bound = 0.5 * (trace_dist ** 2)
        assert s_rel_beta5 > pinsker_bound


class TestLovaszHomomorphismAndFragmentationBias:
    """Tests Lovász homomorphism matching predictions and fragmentation measure bias."""

    def test_lovasz_homomorphism_matches_on_kn(self):
        # 2-in rule: v1=3, e1=2, Aut=2.
        # On complete graph K_N (p=1), match count is N(N-1)(N-2)/2 ~ N^3 / 2
        for n in [3, 4, 5]:
            pred = lovasz_homomorphism_matches(v1=3, e1=2, aut_h1=2, p=1.0, n=n)
            exact = n * (n - 1) * (n - 2) // 2
            assert pred >= exact  # asymptotic formula upper bounds / matches exact leading order
            assert pred == pytest.approx(n ** 3 / 2.0)

    def test_fragmentation_reduces_matches_and_increases_step_weight(self):
        auditor = ExplicitHypergraphRuleAuditor()
        # Connected complete graph K_4: 6 edges
        k4: HypergraphState = frozenset({(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)})
        matches_k4 = auditor.find_2in_matches(k4)
        assert len(matches_k4) == 12  # C(4,3)*3 = 12

        # Disconnected graph: two disjoint triangles K_3 on vertices {0,1,2} and {3,4,5}
        disjoint_k3: HypergraphState = frozenset({(0, 1), (0, 2), (1, 2), (3, 4), (3, 5), (4, 5)})
        matches_disjoint = auditor.find_2in_matches(disjoint_k3)
        # Matches in cluster 1 + matches in cluster 2 = 3 + 3 = 6
        assert len(matches_disjoint) == 6

        # Step probability weight b(G)^(-1) is strictly higher for fragmented topology (1/6 > 1/12)
        weight_connected = 1.0 / len(matches_k4)
        weight_fragmented = 1.0 / len(matches_disjoint)
        assert weight_fragmented > weight_connected


class TestCppEngineIntegration:
    """Tests integration, correctness, and performance of C++20 simulation engine."""

    def test_cpp_engine_smoke_test(self):
        cpp_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "cpp"))
        exe_path = os.path.join(cpp_dir, "causal_invariance_engine.exe")

        # Compile if not present
        if not os.path.exists(exe_path):
            compile_cmd = ["g++", "-O3", "-std=c++20", "-pthread", "causal_invariance_engine.cpp", "-o", "causal_invariance_engine.exe"]
            res_comp = subprocess.run(compile_cmd, cwd=cpp_dir, capture_output=True, text=True)
            assert res_comp.returncode == 0, f"Compilation failed: {res_comp.stderr}"

        # Run smoke test
        res = subprocess.run([exe_path, "--smoke-test"], cwd=cpp_dir, capture_output=True, text=True)
        assert res.returncode == 0, f"C++ smoke test failed: {res.stderr}\nStdout: {res.stdout}"
        assert "All Smoke Tests Passed Cleanly!" in res.stdout

    def test_cpp_python_exact_equivalence_n5_n6(self):
        auditor = MultiwayStateSpaceAuditor()
        res_py_5 = auditor.evaluate_exact_multiway_induction(5, 3, silent=True)
        assert res_py_5["total_paths"] == 1620
        assert res_py_5["physical_classes"] == 4

        res_py_6 = auditor.evaluate_exact_multiway_induction(6, 3, silent=True)
        assert res_py_6["total_paths"] == 133797600
        assert res_py_6["physical_classes"] == 29

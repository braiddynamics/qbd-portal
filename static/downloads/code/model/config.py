# /model/config.py
import math

DEFAULT_CONFIG = {
    # --- ANCHORED PHYSICAL CONSTANTS (Units: MeV) ---

    # (ALPHA): The fundamental energy cost (in MeV) for creating a single
    # quantum of geometric information (a 3-cycle, N_3).
    # This value is a foundational anchor, matching the electron's
    # rest mass (m_e ≈ 0.511 MeV) divided by its topological
    # ribbon-count (n=3).
    #
    # *** CRITICAL NOTE ***
    # This value is *NOT* used by the local rewrite rule R in dynamics.py.
    # The micro-rule is 'α'-agnostic.
    # ALPHA is an *emergent macroscopic* constant.
    "ALPHA": 0.173,

    # (T_VACUUM): The foundational temperature of the vacuum (in MeV).
    # It anchors the thermal scale to the fundamental
    # entropy scale (ΔS = ln(2) for one bit of geometric info.
    # This specific value is what yields the deletion
    # probability Q_del = 1/2, ensuring a stable, dynamic vacuum.
    "T_VACUUM": math.log(2),  # ~0.693 MeV

    # --- GEOMETRIC PARAMETERS (Dimensionless) ---

    # (MU): The dimensionless friction coefficient. This is the 'μ'
    # in the syndrome-response function f(σ) ≈ exp(-μ * <k>).
    # It models the PUC/saturation effect by suppressing creation
    # in dense, "crowded" regions (high local σ = -1 density).
    # This value (.40) is a *simulation choice*. The theory only
    # requires μ < 3/e (≈ 1.104) for a stable vacuum.
    "MU": .3989,

    # (LAMBDA): The dimensionless catalysis coefficient. This is the 'λ'
    # in the syndrome-response function f(σ).
    # It *boosts* the probability of rewrites that resolve local
    # geometric tension (e.g., flipping a syndrome from -1 to +1).
    "LAMBDA": 1.7183,

    # --- SIMULATION CONTROL ---

    # (N): The approximate number of nodes (vertices) in the causal graph.
    # This is the 'N' in all *macroscopic* thermodynamic and master equations.
    #
    # *** CRITICAL NOTE ***
    # This value is used to *build* the initial graph, but the local
    # rewrite rule R in dynamics.py *does not know* this value.
    # This separation is the "micro/macro" split.
    "NUM_NODES_APPROX": 100,

    # (t_max): The number of logical time steps ("ticks") to run
    # the simulation. (i.e., applications of the E operator).
    "SIMULATION_STEPS": 2000,

    # The number of independent simulation runs to perform
    # for ensemble averaging.
    "NUM_RUNS": 200,

    # The master seed for the random number generator (RNG)
    # to ensure reproducible results.
    "SEED": 42,

    # Directory to save simulation data (e.g., CSVs, plots).
    "OUTPUT_DIR": "./outputs",
}
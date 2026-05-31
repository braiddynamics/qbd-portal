#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# Title:     QBD Ensemble Simulation Runner
# Subject:   Statistical Ensemble Analysis
# -----------------------------------------------------------------------------

# --- Imports ---
import sys, os, time, csv, argparse
import numpy as np
from multiprocessing import Pool, TimeoutError, cpu_count
from tqdm import tqdm
from scipy.stats import skew, kurtosis

# Optional plots (uncomment if matplotlib available)
# import matplotlib.pyplot as plt

# Path fix
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# --- qbd Library Imports ---
from model.config import DEFAULT_CONFIG
from model.graph_setup import generate_zpi_vacuum, inject_energic_event
from model.dynamics import evolve_graph_to_equilibrium
from model.observables import get_n3_count, get_graph_density

# --- STATS HELPER (Direct skew/kurtosis) ---
def compute_full_stats(data_array):
    """
    Computes full statistics on an array (n3 or density).
    Returns dict with mean, std, median, skew, kurtosis.
    """
    if len(data_array) == 0 or np.all(np.isnan(data_array)):
        return {key: np.nan for key in ['Mean', 'Std_Dev', 'Median', 'Skewness', 'Kurtosis']}
    
    data = np.array(data_array)
    valid_data = data[~np.isnan(data)]
    if len(valid_data) == 0:
        return {key: np.nan for key in ['Mean', 'Std_Dev', 'Median', 'Skewness', 'Kurtosis']}
    
    return {
        'Mean': np.mean(valid_data),
        'Std_Dev': np.std(valid_data),
        'Median': np.median(valid_data),
        'Skewness': skew(valid_data),
        'Kurtosis': kurtosis(valid_data)
    }

# --- WORKER FUNCTION (FOR MULTIPROCESSING) ---

def run_simulation_worker(config):
    """
    A self-contained, isolated function that runs one full simulation.
    Returns a tuple of all key observables.
    """
    np.random.seed(None)  # Per-run random
    
    G_acyclic, levels = generate_zpi_vacuum(config["NUM_NODES_APPROX"])
    G_initial = inject_energic_event(G_acyclic, levels)
    G_final, steps_taken = evolve_graph_to_equilibrium(G_initial, config)
    
    final_n3 = get_n3_count(G_final)
    final_density = get_graph_density(G_final)
    
    return (final_n3, final_density, steps_taken)

# --- MAIN ENSEMBLE RUNNER ---

def run_ensemble():
    """
    Manages the entire ensemble experiment, including argument parsing.
    """
    parser = argparse.ArgumentParser(description="Run a robust ensemble of qbd simulations.")
    parser.add_argument('--runs', type=int, default=DEFAULT_CONFIG["NUM_RUNS"])
    parser.add_argument('--nodes', type=int, default=DEFAULT_CONFIG["NUM_NODES_APPROX"])
    parser.add_argument('--steps', type=int, default=DEFAULT_CONFIG["SIMULATION_STEPS"])
    parser.add_argument('--timeout', type=int, default=60)
    parser.add_argument('--cores', type=int, default=None, help="CPU cores (default: all-2)")
    parser.add_argument('--mu', type=float, default=DEFAULT_CONFIG["MU"])
    parser.add_argument('--lambda', type=float, default=DEFAULT_CONFIG["LAMBDA"], dest='lambda_')
    parser.add_argument('--alpha', type=float, default=DEFAULT_CONFIG["ALPHA"])
    parser.add_argument('--seed', type=int, default=DEFAULT_CONFIG["SEED"])
    parser.add_argument('--outdir', type=str, default=DEFAULT_CONFIG["OUTPUT_DIR"])
    args = parser.parse_args()

    config = DEFAULT_CONFIG.copy()
    config.update({
        "NUM_RUNS": args.runs,
        "NUM_NODES_APPROX": args.nodes,
        "SIMULATION_STEPS": args.steps,
        "TIMEOUT": args.timeout,
        "MU": args.mu,
        "LAMBDA": args.lambda_,
        "ALPHA": args.alpha,
        "SEED": args.seed,
        "OUTPUT_DIR": args.outdir,
    })

    # Cores default
    if args.cores is None:
        args.cores = max(1, cpu_count() - 2)

    np.random.seed(config["SEED"])
    os.makedirs(config["OUTPUT_DIR"], exist_ok=True)

    print("="*80)
    print(f"Running Ensemble Analysis")
    print(f"Configuration: N≈{config['NUM_NODES_APPROX']}, Runs={config['NUM_RUNS']}, Timeout={config['TIMEOUT']}s")
    print(f"Parameters: ALPHA={config['ALPHA']:.3f}, MU={config['MU']:.2f}, LAMBDA={config['LAMBDA']:.2f}")
    print(f"Cores: {args.cores}")
    print("="*80)

    all_results = []
    stalled_runs = 0

    with Pool(processes=args.cores) as pool:
        results_async = [pool.apply_async(run_simulation_worker, (config,)) for _ in range(config['NUM_RUNS'])]
        with tqdm(total=config['NUM_RUNS'], desc="Simulations", ncols=90) as pbar:
            for res in results_async:
                try:
                    all_results.append(res.get(timeout=config['TIMEOUT']))
                except TimeoutError:
                    stalled_runs += 1
                pbar.update(1)

    print("\nEnsemble complete. Analyzing and saving results...")

    # --- Analysis & Output ---
    successful_runs = len(all_results)
    n3_array = [r[0] for r in all_results]
    density_array = [r[1] for r in all_results]
    steps_array = [r[2] for r in all_results]

    n3_stats = compute_full_stats(n3_array)
    density_stats = compute_full_stats(density_array)
    steps_stats = compute_full_stats(steps_array)

    # Global metrics
    n3_stats["Successful_Runs"] = successful_runs
    n3_stats["Stalled_Runs"] = stalled_runs
    n3_stats["Stall_Rate_Percent"] = (stalled_runs / config['NUM_RUNS']) * 100
    n3_stats["Mean_Degree"] = np.mean(density_array) if successful_runs else np.nan
    n3_stats["Mean_Steps"] = np.mean(steps_array) if successful_runs else np.nan

    # --- Save files ---
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    csv_path = os.path.join(config["OUTPUT_DIR"], f"ensemble_N{config['NUM_NODES_APPROX']}_runs{config['NUM_RUNS']}_alpha{config['ALPHA']:.3f}_mu{config['MU']:.2f}.csv")
    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Run_ID", "Final_N3", "Final_Density", "Steps_Taken"])
        for i, (n3, density, steps) in enumerate(all_results):
            writer.writerow([i + 1, n3, density, steps])

    # Optional plots (uncomment if matplotlib available)
    # if len(n3_array) > 0:
    #     plt.figure(figsize=(10, 5))
    #     plt.subplot(1, 2, 1)
    #     plt.hist(n3_array, bins=20, alpha=0.7)
    #     plt.xlabel('Final N3')
    #     plt.ylabel('Frequency')
    #     plt.subplot(1, 2, 2)
    #     plt.hist(steps_array, bins=20, alpha=0.7)
    #     plt.xlabel('Steps Taken')
    #     plt.ylabel('Frequency')
    #     plt.tight_layout()
    #     plot_path = csv_path.replace('.csv', '_plots.png')
    #     plt.savefig(plot_path)
    #     print(f"Plots saved to: {plot_path}")

    print("\n" + "="*80)
    print("STATISTICAL ANALYSIS COMPLETE")
    print("="*80)
    print(f"{'Metric':<20} {'N3 Value':>15} {'Density Value':>15}")
    print("-"*60)
    for key in ['Mean', 'Std_Dev', 'Median', 'Skewness', 'Kurtosis']:
        n3_val = n3_stats.get(key, np.nan)
        den_val = density_stats.get(key, np.nan)
        print(f"{key:<20} {n3_val:>15.4f} {den_val:>15.4f}")
    print("-"*60)
    print(f"Successful Runs: {successful_runs}, Stalled: {stalled_runs} ({n3_stats['Stall_Rate_Percent']:.1f}%)")
    print(f"Mean Degree: {n3_stats['Mean_Degree']:.4f}, Mean Steps: {n3_stats['Mean_Steps']:.1f}")
    print(f"Raw data saved to: {csv_path}")
    print("="*80)

if __name__ == "__main__":
    run_ensemble()
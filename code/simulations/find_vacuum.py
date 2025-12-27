#!/usr/bin/env python
# -----------------------------------------------------------------------------
# Title:     QBD Vacuum Parameter Sweep
# Subject:   Finds the "Region of Physical Viability" (RPV) for the vacuum.
# Version:   1.0
# -----------------------------------------------------------------------------

import sys
import os
import time
import csv
import argparse
import numpy as np
from itertools import product
from multiprocessing import Pool, TimeoutError, cpu_count
from tqdm import tqdm
import random
import math
from scipy import stats

# Path fix
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# QBD Imports
from model.config import DEFAULT_CONFIG
from model.graph_setup import generate_zpi_vacuum, inject_energic_event
from model.dynamics import evolve_graph_to_equilibrium
from model.observables import get_n3_count

# --- WORKER ---
def run_vacuum_simulation_worker(config_tuple):
    """
    Worker function that takes a (config, seed) tuple.
    Returns a (n3_final, n_nodes_final) tuple.
    """
    config, seed = config_tuple
    random.seed(int(seed))
    
    try:
        G_acyclic, levels = generate_zpi_vacuum(config["NUM_NODES_APPROX"])
        G_initial = inject_energic_event(G_acyclic.copy(), levels) 
        G_final, steps = evolve_graph_to_equilibrium(G_initial.copy(), config)
        
        n_nodes_final = G_final.number_of_nodes()
        if n_nodes_final == 0:
            return (0, 0) # (n3, n_nodes)
            
        n3_final = get_n3_count(G_final)
        return (n3_final, n_nodes_final)
        
    except Exception as e:
        return (np.nan, np.nan) 

# --- HELPERS ---
def parse_range(range_str: str) -> np.ndarray:
    """
    Parses a 'start:end:step' string into a robust numpy array.
    """
    try:
        parts = list(map(float, range_str.split(':')))
        if len(parts) == 1:
            return np.array(parts)
        if len(parts) == 2:
            start, end = parts
            step = 1.0
            if end < start:
                step = -1.0
            return np.arange(start, end + step, step)
        if len(parts) == 3:
            start, end, step = parts
            if step == 0:
                return np.array([start])
            return np.arange(start, end + step*0.5, step)
        else:
            raise ValueError
    except (ValueError, TypeError):
        print(f"Error: Invalid range format '{range_str}'. Use 'val' or 'start:end' or 'start:end:step'.")
        sys.exit(1)

# --- MAIN ---
def run_sweep():
    parser = argparse.ArgumentParser(
        description="QBD Vacuum Parameter Sweep (Find RPV)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument('--nodes', type=int, default=100,
                        help='Approx nodes per graph (larger is better).')
    parser.add_argument('--runs', type=int, default=20,
                        help='Runs per parameter point for statistics.')
    parser.add_argument('--steps', type=int, default=2000,
                        help='Max steps per simulation run.')
    parser.add_argument('--timeout', type=int, default=120,
                        help="Timeout per single run (seconds).")
    parser.add_argument('--cores', type=int, default=max(1, cpu_count() - 2),
                        help="Number of CPU cores to use. (Default: all - 2, min 1)")
    
    parser.add_argument('--mu-range', type=str, default="0.1:3.0:0.3",
                        help='Mu (friction) range (start:end:step).')
    parser.add_argument('--lambda-range', type=str, default="0.1:3.0:0.3",
                        help='Lambda (catalysis) range (start:end:step).')
                        
    parser.add_argument('--seed', type=int, default=42,
                        help='Main random seed for sweep reproducibility.')
    parser.add_argument('--outdir', type=str, default="./outputs",
                        help='Output directory for CSV results.')

    args = parser.parse_args()

    np.random.seed(args.seed)
    random.seed(args.seed)

    os.makedirs(args.outdir, exist_ok=True)

    mu_values = parse_range(args.mu_range)
    lambda_values = parse_range(args.lambda_range)
    
    param_grid = list(product(mu_values, lambda_values))

    field_names = [
        "mu", "lambda", "Runs_Success", "Stall_Rate_pct",
        "Mean_N3", "Std_Dev_N3", "Median_N3", 
        "Mean_Rho3", "Std_Dev_Rho3", "Median_Rho3", "Skew_Rho3"
    ]

    all_results = []
    print("="*80)
    print(f"QBD Vacuum Parameter Sweep (Sweep 1: Find RPV)")
    print(f"Anchored Constants: ALPHA={DEFAULT_CONFIG['ALPHA']:.2f} MeV, T_VACUUM={DEFAULT_CONFIG['T_VACUUM']:.3f} MeV")
    print(f"Nodes: ~{args.nodes}, Runs/point: {args.runs}, Steps: {args.steps}")
    print(f"Cores: {args.cores}, Timeout: {args.timeout}s")
    print(f"Sweeping Mu range: {np.round(mu_values, 3)}")
    print(f"Sweeping Lambda range: {np.round(lambda_values, 3)}")
    print(f"Total parameter points to test: {len(param_grid)}")
    print("="*80)
    print("Running simulations...")

    master_seed_gen = np.random.RandomState(args.seed)
    safe_seed_max = 2**31 - 1
    
    with Pool(processes=args.cores) as pool:
        for point_index, (mu_val, lambda_val) in enumerate(param_grid):
            
            run_seeds = master_seed_gen.randint(0, safe_seed_max, args.runs).tolist()
            
            tasks = []
            for i in range(args.runs):
                point_config = DEFAULT_CONFIG.copy() 
                point_config.update({
                    "MU": mu_val,
                    "LAMBDA": lambda_val,
                    "NUM_NODES_APPROX": args.nodes,
                    "SIMULATION_STEPS": args.steps,
                })
                tasks.append((point_config, run_seeds[i]))

            results_async = [pool.apply_async(run_vacuum_simulation_worker, (task,)) for task in tasks]
            
            raw_n3_results = []
            raw_node_results = []
            stalled = 0
            
            desc = f"μ={mu_val:.2f}, λ={lambda_val:.2f}"
            for res in tqdm(results_async, desc=desc):
                try:
                    n3, n_nodes = res.get(timeout=args.timeout)
                    if not np.isnan(n3) and n_nodes > 0:
                        raw_n3_results.append(n3)
                        raw_node_results.append(n_nodes)
                except TimeoutError:
                    stalled += 1
                except Exception as e:
                    pass 

            stats_row = {
                "mu": mu_val, "lambda": lambda_val,
                "Runs_Success": len(raw_n3_results),
                "Stall_Rate_pct": (stalled / args.runs) * 100
            }

            if raw_n3_results:
                n3_array = np.array(raw_n3_results)
                nodes_array = np.array(raw_node_results)
                rho3_array = n3_array / nodes_array

                stats_row.update({
                    "Mean_N3": np.mean(n3_array),
                    "Std_Dev_N3": np.std(n3_array),
                    "Median_N3": np.median(n3_array),
                    "Mean_Rho3": np.mean(rho3_array),
                    "Std_Dev_Rho3": np.std(rho3_array),
                    "Median_Rho3": np.median(rho3_array),
                    "Skew_Rho3": stats.skew(rho3_array) if np.std(rho3_array) > 0 else 0
                })
            else:
                for key in field_names:
                    if key not in stats_row:
                        stats_row[key] = np.nan
            
            all_results.append(stats_row)
            
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    csv_path = os.path.join(args.outdir, f"vacuum_sweep_N{args.nodes}_{timestamp}.csv")
    
    if not all_results:
        print("No results to save. Exiting.")
        return

    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["# QBD Vacuum Parameter Sweep Results"])
        writer.writerow([f"# Timestamp: {timestamp}"])
        writer.writerow([f"# Anchored ALPHA: {DEFAULT_CONFIG['ALPHA']:.2f} MeV"])
        writer.writerow([f"# Anchored T_VACUUM: {DEFAULT_CONFIG['T_VACUUM']:.3f} MeV"])
        writer.writerow([f"# Nodes (approx): {args.nodes}"])
        writer.writerow([f"# Runs per point: {args.runs}"])
        writer.writerow([f"# Max Steps: {args.steps}"])
        writer.writerow([]) 
        
        dict_writer = csv.DictWriter(f, fieldnames=field_names)
        dict_writer.writeheader()
        dict_writer.writerows(all_results)
        
    print(f"\nSweep Complete. Results in: {csv_path}")
    
    # --- FINAL RPV ANALYSIS ---
    print("\n" + "="*80)
    print("Vacuum Search Analysis: Region of Physical Viability (RPV)")
    print("Target: 0.01 < Mean_Rho3 < 0.1")
    print("="*80)
    print(f"{'Mu':>6} {'Lambda':>6} {'Mean_Rho3':>11} {'Status':>12}")
    print("-" * 80)
    
    rpv_count = 0
    rpv_params = []
    
    for row in all_results:
        mean_rho = row.get("Mean_Rho3", np.nan)
        
        if (not np.isnan(mean_rho)):
            is_viable = 0.01 < mean_rho < 0.1
            
            if is_viable:
                rpv_count += 1
                rpv_params.append((row['mu'], row['lambda']))
                status = "<-- VIABLE"
            elif mean_rho <= 0.01:
                status = "(Frozen)"
            else:
                status = "(Saturated)"
                
            print(f"{row['mu']:>6.2f} {row['lambda']:>6.2f} {mean_rho:>11.4f} {status:>12}")
        else:
             print(f"{row['mu']:>6.2f} {row['lambda']:>6.2f} {'NaN':>11} {'(Failed)':>12}")

    print("-" * 80)
    if rpv_count > 0:
        print(f"SUCCESS: Found {rpv_count} viable parameter sets.")
    else:
        print("FAILURE: No parameter sets found in the RPV.")
        print("ADVICE: Widen the parameter sweep ranges and try again.")
    print("="*80)

if __name__ == "__main__":
    run_sweep()
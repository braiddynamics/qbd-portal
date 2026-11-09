from math import ceil, cosh, sinh

import numpy as np


def maximize_proper_time(layers):
    duration = 1.0
    dt = duration / layers
    dx = dt**2
    grid = dx * np.arange(-round(0.25 / dx), round(0.30 / dx) + 1)
    origin = int(np.argmin(abs(grid)))
    radius = 1.0 + grid

    # Exact squared Minkowski separation of consecutive Rindler events.
    factor = 4.0 * sinh(dt / 2.0)**2
    max_offset = ceil(radius.max() * np.sqrt(factor) / dx)
    edges = []
    for offset in range(-max_offset, max_offset + 1):
        first = slice(max(0, -offset), min(len(grid), len(grid) - offset))
        second = slice(max(0, offset), min(len(grid), len(grid) + offset))
        interval = factor * radius[first] * radius[second] - (offset * dx)**2
        edge_time = np.full(interval.shape, -np.inf)
        causal = interval >= 0
        edge_time[causal] = np.sqrt(interval[causal])
        edges.append((first, second, edge_time))

    best = np.full(len(grid), -np.inf)
    apex = np.zeros(len(grid))
    best[origin] = 0.0
    for _ in range(layers):
        next_best = np.full(len(grid), -np.inf)
        next_apex = np.zeros(len(grid))
        for first, second, edge_time in edges:
            candidate = best[first] + edge_time
            better = candidate > next_best[second]
            next_best[second][better] = candidate[better]
            next_apex[second][better] = np.maximum(apex[first], grid[second])[better]
        best, apex = next_best, next_apex

    return float(best[origin]), float(apex[origin])


if __name__ == "__main__":
    exact_time = 2.0 * sinh(0.5)
    exact_apex = cosh(0.5) - 1.0
    print("--- Proper-time maximization in a Rindler chart ---")
    print(f"Exact proper duration: {exact_time:.8f}")
    print(f"Exact spatial apex:    {exact_apex:.8f}")
    print("Layers | Proper duration | Error      | Apex")
    previous_error = float("inf")
    for layers in (16, 32, 64):
        duration, apex = maximize_proper_time(layers)
        error = exact_time - duration
        assert 0 <= error < previous_error
        previous_error = error
        print(f"{layers:6d} | {duration:.8f}      | {error:.8f} | {apex:.8f}")
    assert previous_error < 1e-3
    print("PASS: The finite path durations approach the analytic benchmark.")

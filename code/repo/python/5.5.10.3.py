from math import gamma, isclose


def calibration(dimension):
    return gamma(dimension + 1) * gamma(dimension / 2) / (4 * gamma(1.5 * dimension))


def invert(statistic):
    low, high = 1.0, 10.0
    for _ in range(60):
        middle = (low + high) / 2
        if calibration(middle) > statistic:
            low = middle
        else:
            high = middle
    return (low + high) / 2


for dimension in range(1, 7):
    print(f"d={dimension}: calibrated statistic {calibration(dimension):.6f}")
assert isclose(calibration(4), 1 / 20)
assert isclose(invert(1 / 20), 4)
print(f"Exact calibration 1/20: estimated dimension {invert(1 / 20):.4f}")
print(f"Synthetic statistic 0.0501: estimated dimension {invert(0.0501):.4f}")

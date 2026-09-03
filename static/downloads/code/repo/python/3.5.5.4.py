TRIAD_CONFIGS = [
    (0, 0, 0, "Vacuum", "Pre-geometric Void"),
    (1, 0, 0, "Tension A", "Single Edge 1 -> 2"),
    (0, 1, 0, "Tension B", "Single Edge 2 -> 3"),
    (0, 0, 1, "Tension C", "Single Edge 3 -> 1"),
    (1, 1, 0, "Precursor A", "Compliant 2-Path 1 -> 2 -> 3"),
    (0, 1, 1, "Precursor B", "Compliant 2-Path 2 -> 3 -> 1"),
    (1, 0, 1, "Precursor C", "Compliant 2-Path 3 -> 1 -> 2"),
    (1, 1, 1, "Geometric Quantum", "Closed 3-Cycle"),
]

def z_val(bit: int) -> int:
    return 1 if bit == 0 else -1

def evaluate_triad(q12: int, q23: int, q31: int):
    z12, z23, z31 = z_val(q12), z_val(q23), z_val(q31)
    s1, s2, s3 = z12 * z23, z23 * z31, z31 * z12
    v = z12 * z23 * z31
    proj_factor = ((1 - z12) * (1 - z23) * (1 - z31)) // 8
    pi_order = 1 - proj_factor
    return {"S1": s1, "S2": s2, "S3": s3, "V": v, "Pi_order": pi_order}

print("Triad Quantum Occupancy and Projector Evaluation")
print("=" * 80)
print(f"{'State':<10} | {'Classification':<18} | {'S1':<4} {'S2':<4} {'S3':<4} | {'V':<4} | {'Pi_order':<8} | {'Description'}")
print("-" * 80)
for q12, q23, q31, name, desc in TRIAD_CONFIGS:
    res = evaluate_triad(q12, q23, q31)
    print(f"|{q12}{q23}{q31}>     | {name:<18} | {res['S1']:>2}   {res['S2']:>2}   {res['S3']:>2}  | {res['V']:>2}   | {res['Pi_order']:>8} | {desc}")
print("=" * 80)

import pandas as pd

def commutes(p1: str, p2: str) -> bool:
    """Return True if two Pauli strings commute (even number of anti-commuting sites)."""
    anti_count = 0
    for a, b in zip(p1, p2):
        if a in 'IXYZ' and b in 'IXYZ' and a != b and {a, b} == {'X', 'Y'}:
            anti_count += 1
    return anti_count % 2 == 0

def syndrome(error: str, stabilizers: list[str]) -> str:
    """Compute syndrome bitstring for a given error under the stabilizer set."""
    return ''.join('0' if commutes(error, stab) else '1' for stab in stabilizers)

def generate_syndrome_table(n_qubits: int, stabilizers: list[str], code_name: str):
    """Generate and print syndrome table for a stabilizer code."""
    results = []
    
    # No error
    identity = 'I' * n_qubits
    results.append({'Error Type': 'None', 'Qubit': '-', 'Syndrome': syndrome(identity, stabilizers)})
    
    # Single-qubit errors
    for q in range(n_qubits):
        for pauli in ['X', 'Y', 'Z']:
            error_str = list(identity)
            error_str[q] = pauli
            error_str = ''.join(error_str)
            results.append({
                'Error Type': pauli,
                'Qubit': q,
                'Syndrome': syndrome(error_str, stabilizers)
            })
    
    df = pd.DataFrame(results)
    print(f"{code_name} Syndrome Table")
    print("=" * (len(code_name) + 14))
    print(df.to_markdown(index=False, tablefmt="github"))
    print()

# 5-qubit perfect code
stabilizers_5 = ['XZZXI', 'IXZZX', 'XIXZZ', 'ZXIXZ']
generate_syndrome_table(5, stabilizers_5, "5-Qubit Perfect Code")

# 7-qubit Steane code
stabilizers_7 = ['IIIXXXX', 'IXXIIXX', 'XIXIXIX', 'IIIZZZZ', 'IZZIIZZ', 'ZIZIZIZ']
generate_syndrome_table(7, stabilizers_7, "7-Qubit Steane Code")
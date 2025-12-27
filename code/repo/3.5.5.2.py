import pandas as pd
import os

def commutes(p1, p2):
    """
    Checks if two Pauli strings commute.
    """
    anti_count = 0
    for a, b in zip(p1, p2):
        if a == 'I' or b == 'I' or a == b:
            continue
        else:
            anti_count += 1
    return anti_count % 2 == 0

def get_algebraic_syndrome(error_str, stabilizers):
    """
    Calculates the syndrome by checking commutation with stabilizers.
    """
    syndrome = ""
    for stabilizer in stabilizers:
        comm = commutes(error_str, stabilizer)
        syndrome_bit = '0' if comm else '1'
        syndrome += syndrome_bit
    return syndrome

def main():
    """
    Main function to run the test and display results.
    """
    print("Running algebraic test of the 5-qubit perfect code...")

    # Define the four stabilizers as strings
    stabilizers = [
        'XZZXI',
        'IXZZX',
        'XIXZZ',
        'ZXIXZ'
    ]

    qubits = range(5)
    pauli_errors = ['X', 'Y', 'Z']
    results = []

    # Test no error
    identity = 'IIIII'
    results.append({'Error_Type': 'I', 'Qubit_Index': '-', 'Syndrome': get_algebraic_syndrome(identity, stabilizers)})

    # Loop through all single-qubit errors
    for q_idx in qubits:
        for pauli_char in pauli_errors:
            error_str = list('IIIII')
            error_str[q_idx] = pauli_char
            error_str = ''.join(error_str)
            syndrome = get_algebraic_syndrome(error_str, stabilizers)
            results.append({'Error_Type': pauli_char, 'Qubit_Index': q_idx, 'Syndrome': syndrome})

    df = pd.DataFrame(results)

    # Save to CSV
    output_dir = "./outputs"
    os.makedirs(output_dir, exist_ok=True)
    csv_path = os.path.join(output_dir, "qecc_5qubit_syndrome_table.csv")
    df.to_csv(csv_path, index=False)

    print("\n--- Syndrome Lookup Table ---")
    print(df.to_string())

    syndromes = df['Syndrome'].tolist()
    unique_syndromes = set(syndromes)
    no_error_syndrome = syndromes[0]

    print("\n--- Verification ---")
    print(f"Syndrome table saved to: {csv_path}")
    print(f"Total non-trivial errors tested: {len(syndromes) - 1}")
    print(f"Unique syndromes generated: {len(unique_syndromes)}")
    print(f"Syndrome for no error: '{no_error_syndrome}' (should be 0000)")

    is_successful = (
        len(unique_syndromes) == len(syndromes) and
        no_error_syndrome == '0000' and
        '0000' not in syndromes[1:]
    )

    if is_successful:
        print("\nSUCCESS: Each single-qubit Pauli error produces a unique, non-zero syndrome.")
    else:
        print("\nFAILURE: The code did not perform as expected. Check for duplicate or zero syndromes.")

main()
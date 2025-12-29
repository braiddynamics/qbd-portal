import sympy as sp

# Define SU(N) anomaly coefficients symbolically
N = sp.symbols('N', integer=True)
A_fund = 1  # Fundamental
A_antifund = -1  # Anti-fundamental
A_antisym = N - 4  # Antisymmetric 2-tensor

# For SU(5), N=5
N_val = 5
A_5bar = A_antifund  # \bar{5} is anti-fundamental
A_10 = A_antisym.subs(N, N_val)  # 10 is \wedge^2 5

# Total anomaly for one generation
total_anomaly = A_5bar + A_10

# Numerical evaluation
print(f"A(\bar{{5}}) = {A_5bar}")
print(f"A(10) = {A_10}")
print(f"Total anomaly = {total_anomaly}")
print(f"Symbolic: A(antisym) = {A_antisym}, eval at N={N_val}: {A_antisym.subs(N, N_val)}")
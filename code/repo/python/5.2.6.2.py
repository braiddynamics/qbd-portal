import math

mu = 1/math.sqrt(2*math.pi)
lam = math.e-1
a1 = 0.5
a2 = 3*(lam-mu)
a3 = 9*mu*mu-18*lam*mu
print(f'Damped quadratic coefficient: {a2:.9f}')
print(f'Baseline quadratic coefficient: {3*lam:.9f}')
print('rho       exact flux       cubic flux       abs error / rho^4')
for rho in (0.02,0.01,0.005):
    exact = 0.5*rho*(1+6*lam*rho)*math.exp(-6*mu*rho)
    cubic = a1*rho+a2*rho*rho+a3*rho**3
    scaled = abs(exact-cubic)/rho**4
    assert scaled < 20
    print(f'{rho:.5f}   {exact:.10f}   {cubic:.10f}   {scaled:.6f}')

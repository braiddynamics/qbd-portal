import math
from itertools import product

mu = 1/math.sqrt(2*math.pi)
lam = math.e-1
p = math.exp(-2*mu)
q = min(1.0,0.5*(1+2*lam)*math.exp(-2*mu))
event = 0.0
expected = 0.0
mass = 0.0
for a,b in product((0,1),repeat=2):
    additions = (p if a else 1-p)*(p if b else 1-p)
    # -1 = no deletion; 0 = seed return edge; 1,2 = other seed edges.
    for selected,probability in [(-1,1-q),(0,q/3),(1,q/3),(2,q/3)]:
        weight = additions*probability
        survivors = (a+b) if selected != 0 else 0
        mass += weight
        expected += weight*survivors
        event += weight*(survivors>0)
analytic = (1-(1-p)**2)*(1-q/3)
assert abs(mass-1)<1e-12
assert abs(event-analytic)<1e-12
assert abs(expected-2*p*(1-q/3))<1e-12
print(f'Cross-branch acceptance p: {p:.9f}')
print(f'Seed cycle deletion q: {q:.9f}')
print(f'Realization probability mass: {mass:.9f}')
print(f'At least one surviving descendant: {event:.9f}')
print(f'Expected surviving cross-branch descendants: {expected:.9f}')
print(f'Analytic/enumerated difference: {abs(event-analytic):.3e}')

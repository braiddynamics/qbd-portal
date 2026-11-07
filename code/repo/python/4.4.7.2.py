from decimal import Decimal as D, getcontext

getcontext().prec = 80
pi = D('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628')
mu = 1/(2*pi).sqrt()
q = (-2*pi*pi).exp()
direct = sum((-D(n*n)/2).exp() for n in range(-30,31))
delta = 2*sum(q**(n*n) for n in range(1,8))
poisson = (2*pi).sqrt()*(1+delta)
peak = 1/direct
relative = delta/(1+delta)
bound = 2*q/(1-q**3)
assert abs(direct-poisson) < D('1e-75')
assert abs((mu-peak)/mu-relative) < D('1e-75')
assert 0 < relative < bound
for label,value in [('Direct lattice partition',direct),('Poisson partition',poisson),('Continuum reference',mu),('Exact lattice peak',peak),('Relative correction',relative),('Theta-tail upper bound',bound)]:
    print(f'{label}: {value:.21g}')
print('Strict correction bound holds at 80-digit precision.')

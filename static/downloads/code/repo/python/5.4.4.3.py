import math

points = [0,0.25,0.5,0.75,1]
coefficients = [math.expm1(s) for s in points]
assert coefficients[0]==0
assert abs(coefficients[-1]-(math.e-1))<1e-14
assert all(0<=a<=b<3 for a,b in zip(coefficients,coefficients[1:]))
print('entropy   catalytic coefficient')
for s,c in zip(points,coefficients):
    print(f'{s:.2f}      {c:.9f}')
print('All coefficients lie in [0, e-1] and below 3.')

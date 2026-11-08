from itertools import product

vertices = range(3)
edges = [(u,v) for u in vertices for v in vertices if u!=v]
sites = list(product(vertices,repeat=3))
graphs = [{e:bit for e,bit in zip(edges,bits)} for bits in product((0,1),repeat=len(edges))]

def observe(E,p):
    v,w,u = p
    x,y,z = E.get((v,w),0), E.get((w,u),0), E.get((u,v),0)
    return (x^y,y^z,z^x)

checks = 0
for E in graphs:
    for F in graphs:
        difference = {e:E[e]^F[e] for e in edges}
        for p in sites:
            a,b,d = observe(E,p),observe(F,p),observe(difference,p)
            assert d==tuple(x^y for x,y in zip(a,b))
            assert sum(a)%2==0
            assert tuple(x^(x^y) for x,y in zip(a,b))==b
            checks += 1

for b,sE,sF,sG in product((0,1),repeat=4):
    assert (b^(sE^sF))^(sF^sG)==b^(sE^sG)
for a,b,u in product((0,1),repeat=3):
    k = lambda x:x^1
    lift = lambda pair:(k(pair[0]),pair[1]^u)
    duplicate = lambda pair:(pair,pair[1])
    lhs = duplicate(lift((a,b)))
    rhs = ((k(a),b^u),b^u)
    assert lhs==rhs
print('Adjacency patterns:',len(graphs))
print('Global site-pair observation checks:',checks)
print('Binary transport composition cases: 16')
print('Transported duplicate-context cases: 8')
print('Mismatches: 0')

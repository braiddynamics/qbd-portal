import math

def entropy(p):
    return -sum(x*math.log(x) for x in p if x > 0)

def push(p, K):
    return [sum(p[i]*K[i][j] for i in range(len(p))) for j in range(len(K[0]))]

def kl(p,q):
    return sum(a*math.log(a/b) for a,b in zip(p,q) if a>0)

K = [[0.9,0.1],[0.9,0.1]]
p = [0.5,0.5]
q = [0.8,0.2]
after = push(p,K)
conditional = sum(p[i]*entropy(K[i]) for i in range(2))
joint = entropy([p[i]*K[i][j] for i in range(2) for j in range(2)])
assert abs(joint-entropy(p)-conditional)<1e-12
assert entropy(after)<entropy(p)
assert joint>=entropy(p)
assert kl(push(p,K),push(q,K))<=kl(p,q)+1e-12
print(f'Snapshot entropy change: {entropy(after)-entropy(p):.9f} nats')
print(f'Full trajectory entropy increment: {joint-entropy(p):.9f} nats')
print(f'Conditional entropy: {conditional:.9f} nats')
print(f'KL input / output: {kl(p,q):.9f} / {kl(push(p,K),push(q,K)):.9f}')

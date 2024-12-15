from Crypto.Util.number import inverse
from hashlib import sha1

def sum(P, Q, E):
    O = (0, 0)
    if P == O: return Q
    elif Q == O: return P
    else:
        x1, y1 = P
        x2, y2 = Q
        if x1 == x2 and y1 == -y2: return O
        Ea, Ep = E['a'], E['p']
        if P != Q:
            k = ((y2 - y1) * inverse(x2 - x1, Ep)) % Ep
        else:
            k = ((3*x1**2 + Ea) * inverse(2 * y1, Ep)) % Ep

        x3 = (k**2 - x1 - x2) % Ep
        y3 = (k*(x1 - x3) - y1) % Ep
        return x3, y3

def mul(P, n, E):
    O = (0, 0)
    Q = P
    R = O
    while n>0:
        if n%2 == 1: R = sum(R, Q, E)
        Q = sum(Q, Q, E)
        n //=2
    return R

E = {'a': 497, 'b': 1768, 'p': 9739}
G = (1804, 5368)
Q_A = (815, 3190)
b = 1829
key = mul(Q_A, b, E)[0]
key = sha1(str(key).encode()).hexdigest()
flag = 'crypto{?}'.replace('?', key)
print(flag)


We just need to apply the aimless volume of the previous post

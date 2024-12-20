from Crypto.Util.number import inverse

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


Code for calculating aimlessly according to the accounted algorithm.Enter E and and P, n I found it. Q(9467; 2742)


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


First we need to code to calculate "total" two points.Then just count S(x; y) According to the request, the title is finished

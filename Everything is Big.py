from Crypto.Util.number import getPrime, bytes_to_long

FLAG = b"crypto{?????????????????????????}"

m = bytes_to_long(FLAG)

def get_huge_RSA():
    p = getPrime(1024)
    q = getPrime(1024)
    N = p*q
    phi = (p-1)*(q-1)
    while True:
        d = getPrime(256)
        e = pow(d,-1,phi)
        if e.bit_length() == N.bit_length():
            break
    return N,e


N, e = get_huge_RSA()
c = pow(m, e, N)

print(f'N = {hex(N)}')
print(f'e = {hex(e)}')
print(f'c = {hex(c)}')

from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes
from fractions import Fraction

def f2cf(nu, de):
    '''
    Fraction nu/de to continued fraction
    '''
    cf = []
    while de:
        qu = nu // de
        cf.append(qu)
        nu, de = de, nu - de*qu
    return cf

def cf2f(cf):
    '''
    Continued fraction to fraction
    '''
    f = Fraction(0, 1)
    for x in reversed(cf):
        try:
            f = 1 / (f+x)
        except ZeroDivisionError:
            return Fraction(0, 1)
    return 1/f

def cf2cvg(cf):
    '''
    Continued faction to convergents
    '''
    for i in range(1,len(cf)+1):
        yield cf2f(cf[:i])

def crack(e, n):
    for cvg in cf2cvg(f2cf(e, n)):
        k = cvg.numerator
        if k == 0:
            continue
        d = cvg.denominator
        phi = (e*d-1)//k
        nb = n - phi + 1
        squ = nb*nb-4*n
        if squ < 0:
            continue
        root = int(iroot(squ, 2)[0])
        if root*root == squ and not (nb+root)&1:
            p = (nb+root)>>1
            q = (nb-root)>>1
            d = d
            return p, q, d
    return "FAIL"

N, e, c = ... 
p, q, d = crack(e, N)

pt = long_to_bytes(pow(c, d, N))
print(pt)

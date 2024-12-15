from Crypto.Util.number import getPrime, bytes_to_long, inverse
from random import getrandbits
from math import gcd

FLAG = b"crypto{?????????????????????????????????????}"

m = bytes_to_long(FLAG)

def get_huge_RSA():
    p = getPrime(1024)
    q = getPrime(1024)
    N = p*q
    phi = (p-1)*(q-1)
    while True:
        d = getrandbits(512)
        if (3*d)**4 > N and gcd(d,phi) == 1:
            e = inverse(d, phi)
            break
    return N,e


N, e = get_huge_RSA()
c = pow(m, e, N)

print(f'N = {hex(N)}')
print(f'e = {hex(e)}')
print(f'c = {hex(c)}')





Posts for N We can’t have a factor, so we won’t mention that way here.
If you look at the source code of the post, it’s easy to see that Weiner’s attack can’t be used. However, according to the reading source: https://www.ams.org/notices/199902/boneh.pdfWe know in a different way of attacking the case. d relatively small (Copy code but not understanding the nature so I have not written here)

from Crypto.Util.number import bytes_to_long
from Crypto.Hash import SHA256

N, d = ...
e = 65537

pt = b'crypto{Immut4ble_m3ssag1ng}'


H = SHA256.new(pt)
S = pow(bytes_to_long(H.digest()), d, N)
print(S)

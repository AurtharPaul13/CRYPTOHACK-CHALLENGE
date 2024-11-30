p = 17
q = 23
N = p*q
e = 65537
pt = 12
ct = pow(pt, e, N)
print(ct)

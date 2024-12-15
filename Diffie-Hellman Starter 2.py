p = 28151

def check(g, p):
    for i in range(2, p):
        if pow(g, i, p) == g: return False
    return True

for g in range(p):
    if check(g, p):
        print(g)
        break


Speak long lines of writing as above, but actually the element of birth. g of FpSatisfied with the following properties:
g^1 != g^2 != g^3 != ... != g^(p-1) (mod p)
My main goal is to avoid the birth of a cyclic subgroup


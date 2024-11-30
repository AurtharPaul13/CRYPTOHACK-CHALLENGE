p = 28151

def check(g, p):
    for i in range(2, p):
        if pow(g, i, p) == g: return False
    return True

for g in range(p):
    if check(g, p):
        print(g)
        break

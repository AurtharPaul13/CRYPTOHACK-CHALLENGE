from Crypto.Util.number import inverse
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
import hashlib

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

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))

def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

g_x = 43190960452218023575787899214023014938926631792651638044680168600989609069200
g_y = 20971936269255296908588589778128791635639992476076894152303569022736123671173
G = (g_x, g_y)

Ax = 87360200456784002948566700858113190957688355783112995047798140117594305287669
Bx = 6082896373499126624029343293750138460137531774473450341235217699497602895121

A = (87360200456784002948566700858113190957688355783112995047798140117594305287669, 59593466123013446762504853712989655201116629740011953821167160210569255093793)
B = (6082896373499126624029343293750138460137531774473450341235217699497602895121, 69060127841060897625121175491407587143129740583487721612423810293908788323020)

p = 99061670249353652702595159229088680425828208953931838069069584252923270946291
E = {
    'a': 1,
    'b': 4,
    'p': p,
}

iv = 'ceb34a8c174d77136455971f08641cc5'
encrypted_flag = 'b503bf04df71cfbd3f464aec2083e9b79c825803a4d4a43697889ad29eb75453'
a = 15423694994465574149
assert mul(G, a, E) == A
ss = mul(B, a, E)[0]
flag = decrypt_flag(ss, iv, encrypted_flag)
print(flag)

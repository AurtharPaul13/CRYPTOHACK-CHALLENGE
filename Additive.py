from pwn import *
from json import *
from Crypto.Util.number import inverse
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

HOST = 'socket.cryptohack.org'
PORT = 13380

def cvrt(hex):
    return int(hex, 16)

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
    
r = remote(HOST, PORT)
r.recvuntil(b'Intercepted from Alice: ')
get = loads(r.recvuntil(b'}'))
p, g, A = get['p'], get['g'], get['A']

r.recvuntil(b'Intercepted from Bob: ')
get = loads(r.recvuntil(b'}'))
B = get['B']

r.recvuntil(b'Intercepted from Alice: ')
get = loads(r.recvuntil(b'}'))
iv, encrypted = get['iv'], get['encrypted']

p, g, A, B = cvrt(p), cvrt(g), cvrt(A), cvrt(B)
a = A * inverse(g, p)
b = B * inverse(g, p)
assert (g*a*b)%p == (B*a)%p == (A*b)%p # thêm assert cho ngầu
key = (g*a*b)%p

print(decrypt_flag(key, iv, encrypted))


    I know the DH protocol is in the multi-worker group. (G, *) Create power and obtain the following maths:

A = g^a (mod p)
B = g^b (mod p)
key = B^a = A^b = g^(a*b) (mod p)

    So if the DH protocol is implemented in the community group (G, +) then the power of power will be transformed into multiplication and the consequences:

A = g*a (mod p)
B = g*b (mod p)
key = A*b = B*a = g*a*b (mod p)

    I can easily calculate. a, b by looking for the reverse element inverse in the mod p field and from there. key thui :smile_cat:, the formula is as follows:

g*a = A (mod p) --> g = A*inverse(g) (mod p)
g*b = B (mod p) --> g = B*inverse(g) (mod p)

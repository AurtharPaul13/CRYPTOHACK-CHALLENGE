from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


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


shared_secret = ?
iv = ?
ciphertext = ?

print(decrypt_flag(shared_secret, iv, ciphertext))


    we need to find the degree. q_y correspond to q_x. But in school Fp Hey, instead q_x into the equation of (E) It only helps to find the balance of the balance. q_y according to modulo p. That’s why we need to code to calculate the quadratwo surplus, in other words, find it again. q_y: :

E = {'a': 497, 'b': 1768, 'p': 9739}
G = (1804, 5368)
q_x = 4726
b = 6534
p = E['p']
left = lambda x : (x**3 + 497*x + 1768) % p
assert p % 4 == 3
q_y1, q_y2 = 0, 0
if pow(left(q_x), (p-1)//2, p) == 1:
    q_y1 = pow(left(q_x), (p+1)//4, p)
    q_y2 = p - q_y1

assert (q_y1)**2 % p == left(q_x)
assert (q_y2)**2 % p == left(q_x)
print(q_y1, q_y2)

    Have two toss q_y1 and and q_y2 (Actualally, these two throws out to the same shared secret) We will restore the flag

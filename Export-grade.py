from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
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

p = 16007670376277647657
g = 2
A = 9989801226209336220
B = 14534189480232724354
iv = 38571510066310834468440389169008255603   
encrypted_flag = 56801805763315812000647527321092706170023633891652995062990491131977722679933
a = 3996205933053804434
assert A == pow(g, a, p)
shared_secret = pow(B, a, p)

s, i, e = shared_secret, hex(iv)[2:], hex(encrypted_flag)[2:]
print(decrypt_flag(s, i, e))



Alice and Bob will initially agree on the appropriate DH protocol, as DH64 is the protocol with key 64 bits of security so I will choose to attack. After a series of exchanges, I have the following parameters: {p, g, A, B, iv, encrypted_flag} and the task is to code. encrypted_flag equal to key 64 bit.
To find key, I need to know a or b For A = pow(g, a, p) and and B = pow(g, b, p). This is related to discrete logarithm so I will perform on the sage

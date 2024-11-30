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

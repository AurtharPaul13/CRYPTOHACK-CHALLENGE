from pwn import *
from json import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

HOST = 'socket.cryptohack.org'
PORT = 13373

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

def send(msg):
    return r.sendline(dumps(msg).encode())

r = remote(HOST, PORT)
r.recvuntil(b'Intercepted from Alice: ')
get = loads(r.recvuntil(b'}'))
p, g, A = get['p'], get['g'], get['A']

r.recvuntil(b'Intercepted from Alice: ')
get = loads(r.recvuntil(b'}'))
iv_A, encrypted_A = get['iv'], get['encrypted']

r.recvuntil(b'Bob connects to you, send him some parameters: ')
fake = {
    'p': p,
    'g': A,
    'A': '0x0'
}
send(fake)
r.recvuntil(b'Bob says to you: ')
fake_B = loads(r.recvuntil(b'}'))['B']
shared_secret = int(fake_B, 16)

print(decrypt_flag(shared_secret, iv_A, encrypted_A))

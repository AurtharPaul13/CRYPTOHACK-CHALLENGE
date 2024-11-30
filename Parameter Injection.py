from pwn import *
from json import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

HOST = 'socket.cryptohack.org' 
PORT = 13371

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
   
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]

    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

def send(msg):
    return r.sendline(dumps(msg))
r = remote(HOST, PORT)

r.recvuntil(b'Intercepted from Alice: ')
get = loads(r.recvuntil(b'}'))
r.recvuntil(b'Send to Bob: ')
send(get)

r.recvuntil(b'Send to Alice: ')
send({'B': hex(1)})

r.recvuntil(b'Intercepted from Alice: ')
get = loads(r.recvuntil(b'}'))

iv = get['iv']
encrypted_flag = get['encrypted_flag']
key = 1

print(decrypt_flag(key, iv, encrypted_flag))

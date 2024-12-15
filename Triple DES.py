import requests
from pwn import *
from json import loads
from Crypto.Util.Padding import unpad

def encrypt(key, pt):
    key, pt = bytes.hex(key), bytes.hex(pt)
    url = f"https://aes.cryptohack.org/triple_des/encrypt/{key}/{pt}/"
    r = requests.get(url)
    ct = (loads(r.text))['ciphertext']
    return bytes.fromhex(ct)

def encrypt_flag(key):
    key = bytes.hex(key)
    url = f"https://aes.cryptohack.org/triple_des/encrypt_flag/{key}/"
    r = requests.get(url)
    key = (loads(r.text))['ciphertext']
    return bytes.fromhex(key)

keys = [
    b'\x00'*8 + b'\xff'*8,
    b'\xff'*8 + b'\x00'*8,
    b'\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01',
    b'\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00'
]
for key in keys:
    try:
        enc = encrypt_flag(key)
        flag = unpad(encrypt(key, enc), 8).decode()
        print(flag)
        break
    except:
        print(f'{key}: Error!!!')


First we need to understand the 3DES.According to the diagram above, the function encrypt of DES3 will take the 32-byte key with key1 = key[:8], key2 = key[8:16], key3 = [16:24] (key2 != key1 != key3 otherwise will become DES). If the key is only 24-byte, key1 = key3.
One more knowledge we need to use in this article. lock weak. The weak lock is the satisfying locks E(E(weak_key, plaintext)) = plaintext. Combined with 3DES encoding diagram ct = E(D(E(key, pt))), if replaced key = weak_key, pt = FLAGWe can restore the flag

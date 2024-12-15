from pwn import *
import requests
from json import loads

def encrypt(pt):
    pt = bytes.hex(pt)
    url = f"http://aes.cryptohack.org/lazy_cbc/encrypt/{pt}/"
    r = requests.get(url)
    enc = (loads(r.text))['ciphertext']
    return enc

def receive(ct):
    url = f"http://aes.cryptohack.org/lazy_cbc/receive/{ct}/"
    r = requests.get(url)
    pt = loads(r.text)['error'].split(": ")[1]
    return pt

def get_flag(key):
    key = bytes.hex(key)
    url = f"http://aes.cryptohack.org/lazy_cbc/get_flag/{key}/"
    r = requests.get(url)
    flag = (loads(r.text))['plaintext']
    return flag

pt1 = b'\x00'*16
pt2 = b'\x00'*32
ct1, ct2 = encrypt(pt1), encrypt(pt2)
ct2 = ct2[len(ct1):]
temp = receive(ct2)
key = xor(bytes.fromhex(temp), bytes.fromhex(ct1))
flag = get_flag(key)
print(bytes.fromhex(flag).decode())


we need to know the coding diagram of the CBC mode.Our formula overview will be: C = E(key, xor(P, key)). So, if you choose P = b'\x00'*16, we can shorten the city C = E(key, key).
we need to adjust a little bit. Part ct2 Really is ct2[len(ct1):], part pt2 It's really pt2[len(pt1):]based on the coded diagram above. Here, we have transformations.Get the value of temp, I calculate key = xor(temp, ct1) And submit on the web to get the flag easily

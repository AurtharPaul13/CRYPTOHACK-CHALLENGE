import requests
from pwn import *
from json import loads

def encrypt(pt):
    pt = bytes.hex(pt)
    url = f"https://aes.cryptohack.org/ecb_oracle/encrypt/{pt}/"
    r = requests.get(url)
    ct = (loads(r.text))['ciphertext']
    return bytes.fromhex(ct)

LEN = 25
FLAG = 'crypto{'
chars = '0123456789abcdefghijklmnopqrstuvwxyz{_}'

for i in range(8, 26):
    num = 32 - i
    OFFSET = b'\x00' * num
    check1 = encrypt(OFFSET)[32-LEN:32]
    for char in chars:
        check2 = encrypt(OFFSET + (FLAG + char).encode())[32-LEN:32]
        if check1 == check2:
            FLAG += char
            print(FLAG)
            break 
assert len(FLAG) == LEN

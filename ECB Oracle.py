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


we need to understand the padding mechanism of the code above. The code will automatically buffer the bytes so that the block length is a multiple of 16, here we can determine the length of the flag.
    Running a simple code as above, we see with value i = 6 then len(get) = 32 , i = 7 then len(get) = 48. That's why, len(FLAG) Satisfiction 7 + len(FLAG) = 32 should len(FLAG) = 25. Fortunately, the mode was chosen as the ECB, so the job is much simpler. Besides, we can use it. len(FLAG) to assert later

    



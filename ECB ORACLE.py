import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

ciphertext = b"177d36396d029f19708cef8d1c861bfd1f227170511203bbb211a703905f9e5128ae38bc1312435b814108836328262a"

flag = b'crypto{'

def response(byte_string):
    url = "http://aes.cryptohack.org/ecb_oracle/encrypt/"
    url += byte_string.hex()
    url += '/'
    r = requests.get(url)
    js = r.json()
    return bytes.fromhex(js["ciphertext"])

for i in range(7, 26):
    byte_string = b""
    byte_string += b"\x00" * (31-i)
    print(byte_string)
    res = response(byte_string)[:32]
    byte_string += flag
    for j in range(33, 128):
        byte_string = byte_string[:31]
        byte_string += j.to_bytes(1, byteorder="big")
        print(j)
        
        res2 = response(byte_string)[:32]
        *if r*es == res2:
            flag += j.to_bytes(1, byteorder="big")
            print(flag)
            break


The input will be plus the flag at the back to the out put is the encoding of (input + flag).

The ECB will encode each block of 16 bytes.

We’ll start with a block with 31 bytes ending with “crypte{”

⇒ b’xxxxxxxcrypto{’ + 1 bytes

So we’ll brute force to find out the last bytes by comparing the encrypted version after transmitt. ‘…xxxxxxxcrypto{’ + 1bytes into the encoding board

After finding 1 character, we will use the same way to find the next character until the complete flag is obtained.

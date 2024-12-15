from requests import get
from json import loads
from hashlib import md5
from Crypto.Cipher import AES

def encrypt_flag():
    url = 'https://aes.cryptohack.org/passwords_as_keys/encrypt_flag/'
    r = get(url)
    ct = (loads(r.text))['ciphertext']
    return bytes.fromhex(ct)

gist = 'https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words'
keys = get(gist).text.split("\n")
ct = encrypt_flag()

for key in keys:
    key = md5(key.encode()).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    flag = cipher.decrypt(ct)
    if(b'crypto' in flag):
        print(flag.decode())
        break



The direction of the post is brute-force, the key is bluebell after running the loop.

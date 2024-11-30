from Crypto.Cipher import AES
from Crypto.Util import Counter
import zlib


KEY = ?
FLAG = ?


@chal.route('/ctrime/encrypt/<plaintext>/')
def encrypt(plaintext):
    plaintext = bytes.fromhex(plaintext)

    iv = int.from_bytes(os.urandom(16), 'big')
    cipher = AES.new(KEY, AES.MODE_CTR, counter=Counter.new(128, initial_value=iv))
    encrypted = cipher.encrypt(zlib.compress(plaintext + FLAG.encode()))

    return {"ciphertext": encrypted.hex()}


from json import loads
import requests

def encrypt(pt):
    pt = bytes.hex(pt)
    url = f'https://aes.cryptohack.org/ctrime/encrypt/{pt}/'
    r = requests.get(url)
    ct = (loads(r.text))['ciphertext']
    return ct

FLAG = b'crypto{'
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_abcdefghijklmnopqrstuvwxyz}'

while True:
    temp = (FLAG + b'.') * 2
    check = len(encrypt(temp))
    for char in chars:
        pt = (FLAG + char.encode()) * 2
        print(char)
        if len(encrypt(pt)) < check:
            FLAG += char.encode()
            print('-'*20)
            print(f'FOUND: {FLAG.decode()}')
            print('-'*20)
            if FLAG.endswith(b'}'): 
                exit()
            break


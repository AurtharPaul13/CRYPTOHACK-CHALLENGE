from Crypto.Util.Padding import pad

IV = os.urandom(8)
FLAG = ?

def xor(a, b):
    # xor 2 bytestrings, repeating the 2nd one if necessary
    return bytes(x ^ y for x,y in zip(a, b * (1 + len(a) // len(b))))

@chal.route('/triple_des/encrypt/<key>/<plaintext>/')
def encrypt(key, plaintext):
    try:
        key = bytes.fromhex(key)
        plaintext = bytes.fromhex(plaintext)
        plaintext = xor(plaintext, IV)

        cipher = DES3.new(key, DES3.MODE_ECB)
        ciphertext = cipher.encrypt(plaintext)
        ciphertext = xor(ciphertext, IV)

        return {"ciphertext": ciphertext.hex()}

    except ValueError as e:
        return {"error": str(e)}

@chal.route('/triple_des/encrypt_flag/<key>/')
def encrypt_flag(key):
    return encrypt(key, pad(FLAG.encode(), 8).hex())

import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long

def encrypt(key, plain):
    url = "http://aes.cryptohack.org/triple_des/encrypt/"
    url += key
    url += "/"
    url += plain.hex()
    url += "/"
    r = requests.get(url).json()
    return bytes.fromhex(r["ciphertext"])

def encrypt_flag(key):
    url = "http://aes.cryptohack.org/triple_des/encrypt_flag/"
    r = requests.get(url + key + '/').json()
    return bytes.fromhex(r["ciphertext"])

key = b'\x00'*8 + b'\xff'*8
flag = encrypt_flag(key.hex())
cipher = encrypt(key.hex(), flag)
print(cipher)

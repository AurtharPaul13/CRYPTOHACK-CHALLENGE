import requests
from json import loads

def encrypt(plaintext, iv):
    plaintext, iv = bytes.hex(plaintext), bytes.hex(iv)
    url = f'https://aes.cryptohack.org/symmetry/encrypt/{plaintext}/{iv}/'
    r = requests.get(url)
    ct = (loads(r.text))['ciphertext']
    return ct

def encrypt_flag():
    url = f'https://aes.cryptohack.org/symmetry/encrypt_flag'
    r = requests.get(url)
    enc = (loads(r.text))['ciphertext']
    enc = bytes.fromhex(enc)
    iv, ct = enc[:16], enc[16:]
    return iv, ct

iv, ct = encrypt_flag()
flag = bytes.fromhex(encrypt(ct, iv)).decode()
print(flag)



we need to understand the coding and Decoding diagram of the mode OFB.It can be seen that the encryption process will become an code if we change the position of the Pi and and Ci. Therefore, the simple problem becomes to receive and send data back to the web

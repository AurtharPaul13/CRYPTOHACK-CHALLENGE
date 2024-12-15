from requests import get
from json import loads

def decrypt(ct):
    url = f'https://aes.cryptohack.org/block_cipher_starter/decrypt/{ct}/'
    r = get(url)
    pt = (loads(r.text))['plaintext']
    return bytes.fromhex(pt).decode()

def encrypt_flag():
    url = 'https://aes.cryptohack.org/block_cipher_starter/encrypt_flag/'
    r = get(url)
    ct = (loads(r.text))['ciphertext']
    return ct

flag = decrypt(encrypt_flag())
print(flag)



We just need to give ciphertext in Encrypt_Flag into the function decrypt Available to receive plaintext. Translated through hex we get the flag. With this song, I don’t need to know. key to code because key reused in the function itself decrypt It's already

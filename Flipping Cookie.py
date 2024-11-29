from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timedelta


KEY = ?
FLAG = ?


@chal.route('/flipping_cookie/check_admin/<cookie>/<iv>/')
def check_admin(cookie, iv):
    cookie = bytes.fromhex(cookie)
    iv = bytes.fromhex(iv)

    try:
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(cookie)
        unpadded = unpad(decrypted, 16)
    except ValueError as e:
        return {"error": str(e)}

    if b"admin=True" in unpadded.split(b";"):
        return {"flag": FLAG}
    else:
        return {"error": "Only admin can read the flag"}


@chal.route('/flipping_cookie/get_cookie/')
def get_cookie():
    expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
    cookie = f"admin=False;expiry={expires_at}".encode()

    iv = os.urandom(16)
    padded = pad(cookie, 16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(padded)
    ciphertext = iv.hex() + encrypted.hex()

    return {"cookie": ciphertext}

import requests
from json import loads
from pwn import xor

def check_admin(cookie, iv):
    cookie, iv = bytes.hex(cookie), bytes.hex(iv)
    url = f"https://aes.cryptohack.org/flipping_cookie/check_admin/{cookie}/{iv}/"
    r = requests.get(url)
    flag = loads(r.text)
    return flag

def get_cookie():
    url = "https://aes.cryptohack.org/flipping_cookie/get_cookie"
    r = requests.get(url)
    cookie = (loads(r.text))['cookie']
    cookie = bytes.fromhex(cookie)
    return cookie

temp = get_cookie()
iv, cookie = temp[:16], temp[16:]

block = b'admin=False;expi'
fake_block = b'admin=True;expir'
fake_iv = xor(fake_block, block, iv)

flag = check_admin(cookie, fake_iv)['flag']
print(flag)

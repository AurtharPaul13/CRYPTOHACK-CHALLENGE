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


We will observe the function get_cookie() Before. Function used for encoding cookie after pad, with the value of iv Mounted at the top. We can get value. cookie It's easy.
We already know that CBC mode is clearly divided into 16 bytes, so here we have the first block: block = admin=False;expi,... Observe the function check_admin, the function will release the flag when satisfied b"admin=True" in unpadded.split(b";"). So, we just need to change. admin=False into admin=True It's over. However, in order to keep the length of the block and satisfy the conditions, we will use fake_block = b'admin=True;expir' (resight to one bytes b'r') to bypass padding conditions.
In addition, we also need to create a fake_iv to bypass function unpad. We need to: ct_block = ct_fake.When there are two values cookie and and fake_iv, we have the flag



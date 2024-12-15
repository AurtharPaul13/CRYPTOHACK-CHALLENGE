from requests import get
from PIL import Image
from json import loads
from pwn import xor

def encrypt():
    url = 'https://aes.cryptohack.org/bean_counter/encrypt'
    r = get(url)
    enc = loads(r.text)['encrypted']
    return bytes.fromhex(enc)

first = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'
ct = encrypt()

keystream = xor(first, ct[:16])
assert len(keystream) == 16
png_flag = xor(keystream, ct)

image = open('flag.png', 'wb').write(png_flag)
flag = Image.open('flag.png')
flag.show()


First, we need to analyze the source code of the article, you can see. step_up=False(=0) Leads to self.newIV = hex(int(self.value, 16) Or or iv does not change in the coding process, causing keystream become a 16 bytes series repeated several times and then xor with clear version.
We can find these 16 bytes. First we have keysream(16) ^ flag(??) = ct(??) should keystream(16) ^ flag(16) = ct(16)
We are interested in the first 16 bytes of the flag because the first 16 bytes of the PNG file is always b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'. I know the first 16 bytes. ct, then we found keystream. 

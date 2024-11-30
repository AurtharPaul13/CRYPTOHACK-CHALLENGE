from Crypto.Cipher import AES


KEY = ?


class StepUpCounter(object):
    def __init__(self, step_up=False):
        self.value = os.urandom(16).hex()
        self.step = 1
        self.stup = step_up

    def increment(self):
        if self.stup:
            self.newIV = hex(int(self.value, 16) + self.step)
        else:
            self.newIV = hex(int(self.value, 16) - self.stup)
        self.value = self.newIV[2:len(self.newIV)]
        return bytes.fromhex(self.value.zfill(32))

    def __repr__(self):
        self.increment()
        return self.value



@chal.route('/bean_counter/encrypt/')
def encrypt():
    cipher = AES.new(KEY, AES.MODE_ECB)
    ctr = StepUpCounter()

    out = []
    with open("challenge_files/bean_flag.png", 'rb') as f:
        block = f.read(16)
        while block:
            keystream = cipher.encrypt(ctr.increment())
            xored = [a^b for a, b in zip(block, keystream)]
            out.append(bytes(xored).hex())
            block = f.read(16)

    return {"encrypted": ''.join(out)}


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

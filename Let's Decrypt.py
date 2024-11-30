import re
from Crypto.Hash import SHA256
from Crypto.Util.number import bytes_to_long, long_to_bytes
from utils import listener
from pkcos1 import emsa_pkcs1_v15
# from params import N, E, D

FLAG = "crypto{?????????????????????????????????}"

MSG = 'We are hyperreality and Jack and we own CryptoHack.org'
DIGEST = emsa_pkcs1_v15.encode(MSG.encode(), 256)
SIGNATURE = pow(bytes_to_long(DIGEST), D, N)


class Challenge():
    def __init__(self):
        self.before_input = "This server validates domain ownership with RSA signatures. Present your message and public key, and if the signature matches ours, you must own the domain.\n"

    def challenge(self, your_input):
        if not 'option' in your_input:
            return {"error": "You must send an option to this server"}

        elif your_input['option'] == 'get_signature':
            return {
                "N": hex(N),
                "e": hex(E),
                "signature": hex(SIGNATURE)
            }

        elif your_input['option'] == 'verify':
            msg = your_input['msg']
            n = int(your_input['N'], 16)
            e = int(your_input['e'], 16)

            digest = emsa_pkcs1_v15.encode(msg.encode(), 256)
            calculated_digest = pow(SIGNATURE, e, n)

            if bytes_to_long(digest) == calculated_digest:
                r = re.match(r'^I am Mallory.*own CryptoHack.org$', msg)
                if r:
                    return {"msg": f"Congratulations, here's a secret: {FLAG}"}
                else:
                    return {"msg": f"Ownership verified."}
            else:
                return {"error": "Invalid signature"}

        else:
            return {"error": "Invalid option"}

from pwn import *
from json import *
from Crypto.Util.number import bytes_to_long
from pkcs1 import emsa_pkcs1_v15

def send(hsh):
    return r.sendline(dumps(hsh))

def convert(txt):
    return int(txt, 16)

r = remote('socket.cryptohack.org', 13391)
print(r.recv())

option = {
    'option': 'get_signature'
}
send(option)
get = loads(r.recv())
N, e, s = get["N"], get["e"], get["signature"]
N, e, s = convert(N), convert(e), convert(s)

msg = 'I am Mallory, I own CryptoHack.org'
left = emsa_pkcs1_v15.encode(msg.encode(), 256)
left = bytes_to_long(left)
e = 1
n = s - left
assert left%n == s%n

option = {
    'option': 'verify',
    'msg': msg,
    'N': hex(n),
    'e': hex(e),
}
send(option)
get = loads(r.recv())
flag = (get['msg'].split(':'))[1]
print(flag)
      

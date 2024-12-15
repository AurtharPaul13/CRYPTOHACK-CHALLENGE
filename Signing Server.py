from Crypto.Util.number import bytes_to_long, long_to_bytes
from utils import listener



class Challenge():
    def __init__(self):
        self.before_input = "Welcome to my signing server. You can get_pubkey, get_secret, or sign.\n"

    def challenge(self, your_input):
        if not 'option' in your_input:
            return {"error": "You must send an option to this server"}

        elif your_input['option'] == 'get_pubkey':
            return {"N": hex(N), "e": hex(E) }

        elif your_input['option'] == 'get_secret':
            secret = bytes_to_long(SECRET_MESSAGE)
            return {"secret": hex(pow(secret, E, N)) }

        elif your_input['option'] == 'sign':
            msg = int(your_input['msg'], 16)
            return {"signature": hex(pow(msg, D, N)) }

        else:
            return {"error": "Invalid option"}

      from pwn import *
from json import *

def send(hsh):
    return r.sendline(dumps(hsh))
r = remote('socket.cryptohack.org', 13374)
r.recv()

option =  {
    'option': 'get_secret'
}
send(option)
msg = loads(r.recv())["secret"]

option =  {
    'option': 'sign',
    'msg': msg
}
send(option)
get = loads(r.recv())
message = bytes.fromhex(get["signature"][2:])
print(message.decode())



After nc with the server, we can get it. N, e, secret, signature.
However, if you read the source code, we really don’t need to count anything because the server has a value in the server. d It's already. Then just send it back. secret It's me with the flag

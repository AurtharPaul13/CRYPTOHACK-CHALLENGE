from pwn import *
from json import *

HOST = 'socket.cryptohack.org'
PORT = 13399

def send(msg):
    return r.sendline(dumps(msg))

r = remote(HOST, PORT)
r.recv()
exploit = b'\x00' * 28

while True:
    option1 = {'option': 'reset_password', 'token': bytes.hex(exploit)}
    send(option1)
    print(r.recv())

    auth = ''
    option2 = {'option': 'authenticate', 'password': auth}
    send(option2)
    get = loads(r.recv())['msg']
    if 'Welcome admin, flag: ' in get:
        print(get)
        break

    option3 = {'option': 'reset_connection'}
    send(option3)
    print(r.recv())



After reading the source code, I tried osint about the CFB8 mode and how to attack, I got a document about. Zerologon Attack as After
Basically, the encoding process of CFB8 applying AEs to IV.I’ll analyze a little bit, the server gives us three functions. authenticate, reset_connection and and reset_password. In it, the function authenticate to verify admin, function 2 to change key and the last function to change password equal to token which I sent (this is where I can exploit the weakness). Token get in decrypt by CFB8 made password New. However, this mode has weaknesses that have been introduced in the above link.
If we send token is a repeating series of 28 characters, password It will also be a repeating series of 8 characters. Here the idea will obviously be the brute force these 8 characters until the server will release. flag Okay, I'll choose here. token = b'\x00' * 28 (but you can also choose another string) and password To check will be '' Help to repeat. :monkey:. It's a Brute Force

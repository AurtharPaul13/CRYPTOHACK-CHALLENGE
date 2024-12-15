from pwn import *
from json import *
from Crypto.Util.number import long_to_bytes, bytes_to_long

def send(hsh):
    return r.sendline(dumps(hsh))

ALICE_N = 22266616657574989868109324252160663470925207690694094953312891282341426880506924648525181014287214350136557941201445475540830225059514652125310445352175047408966028497316806142156338927162621004774769949534239479839334209147097793526879762417526445739552772039876568156469224491682030314994880247983332964121759307658270083947005466578077153185206199759569902810832114058818478518470715726064960617482910172035743003538122402440142861494899725720505181663738931151677884218457824676140190841393217857683627886497104915390385283364971133316672332846071665082777884028170668140862010444247560019193505999704028222347577
ALICE_E = 3

r = remote('socket.cryptohack.org', 13375)
print(r.recv())

vote = 855520592299350692515886317752220783
option = {
    'option': 'vote',
    'vote': hex(vote)
}
send(option)
get = loads(r.recv())
flag = get['flag']
print(flag)


The first thing when you solve the article is to guess when the server is to release the flag. For this article, the flag is released when satisfied:Go to the file alice.key I got it.Obviously, we need to choose vote.We need to change the value of prefix to find left is the third surplus of vote by modulo n. Conspicable, the bytes prefix will be ignored because of the function split should be and The reality is n Largeier 256**15 A lot and residual. mod n It is no longer important, so the equation becomes vote.

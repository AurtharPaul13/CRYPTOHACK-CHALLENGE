from json import loads
import requests

def encrypt(pt):
    pt = bytes.hex(pt)
    url = f'https://aes.cryptohack.org/ctrime/encrypt/{pt}/'
    r = requests.get(url)
    ct = (loads(r.text))['ciphertext']
    return ct

FLAG = b'crypto{'
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_abcdefghijklmnopqrstuvwxyz}'

while True:
    temp = (FLAG + b'.') * 2
    check = len(encrypt(temp))
    for char in chars:
        pt = (FLAG + char.encode()) * 2
        print(char)
        if len(encrypt(pt)) < check:
            FLAG += char.encode()
            print('-'*20)
            print(f'FOUND: {FLAG.decode()}')
            print('-'*20)
            if FLAG.endswith(b'}'): 
                exit()
            break



hen I finished the source code, I don’t know what to do. :penguin:. Analysis of code a little, first function encrypt will take plaintext which I sent in the form hex. After initialing a iv 16 bytes any and converted into int Then start coding with key hidden, counter 128 bits (16 bytes) and initial_value = iv. The encoding object here is zlib.compress(plaintext + FLAG.encode()) And we will get it. ciphertext.
The encryption setup step is quite secure, so I try to find out how it works. zlib.compress But there is no result.I tried to send two. pt (pt1 = bytes.hex(b'crypto') #63727970746f
pt2 = bytes.hex(b'crypto{) #63727970746f7b).And try to change 7b in pt2 into other characters, the result is length ciphertext received has been changed, more specifically From here I pull out, if the character I enter is right, len(ct) will fix it. Trying with a few other cases, I realized that there are a few characters when sent up will make len(ct) Changed, so send pt repeat will be more certain, for example instead of sending crypto{ Then I will send it. crypto{crypto{ and check it out if the case ct Return when I fill out the next character. pt A length that is smaller than a certain level, it is accepted as a valid character.
So this post code will be brute force, quite similar to the post. ECB Oracle

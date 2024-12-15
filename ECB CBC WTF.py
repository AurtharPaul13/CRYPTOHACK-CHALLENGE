from pwn import xor

ct = '46114097100b0e0fbdc0f0c3cb530ed403091e84ead0642081f1773557a176484bb32e1da722966127bc7f6868894dd6'
ct = bytes.fromhex(ct)
iv = ct[:16]
block1 = ct[16:32]
block2 = ct[32:]
print(bytes.hex(block1), bytes.hex(block2), sep='\n\n')

# Sau khi đem đi decrypt block1 và block2 trên web ta được pt1 và pt2
pt1 = '256339e76464753cdea2aff6be3065e1'
pt2 = '5c3d68b4dbb43b11b6ae561476805735'
pt1 = xor(bytes.fromhex(pt1), iv)
pt2 = xor(bytes.fromhex(pt2), block1)
print(pt1.decode(), pt2.decode(), sep='')


First, let’s take the value of ciphertext. First we need to transfer ciphertext It's a bytes. Notice ciphertext 48 in length, of which iv It’s the first 16 characters, so we’ll divide the following code into two. block1 and and block2.
The idea of crypt is quite simple if you look at the CBC code-derreding scheme above. With iv I already have, besides the web also provides an ECB-made function (this function helps us bypass the lack of key) Our code will be as follows (codes are indirect rather than directly with the web)

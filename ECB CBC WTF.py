from Crypto.Cipher import AES


KEY = ?
FLAG = ?


@chal.route('/ecbcbcwtf/decrypt/<ciphertext>/')
def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


@chal.route('/ecbcbcwtf/encrypt_flag/')
def encrypt_flag():
    iv = os.urandom(16)

    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(FLAG.encode())
    ciphertext = iv.hex() + encrypted.hex()

    return {"ciphertext": ciphertext}

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

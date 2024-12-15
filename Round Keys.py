from pwn import xor

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def add_round_key(s, k):
    state = bytes(sum(s, []))
    key = bytes(sum(k, []))
    pt = b''
    for i in range(len(state)):
        pt += xor(state[i], key[i])
    return pt

print(add_round_key(state, round_key).decode())



AddRoundKey is also performed at the end of each round. AddRoundKey is also the only stage of AES that the lock is mixed with the state, forming a special lock permutation.
The question: Writing Function add_round_key and use the function matrix2bytes to restore the flag.



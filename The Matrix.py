import random

P = 2
N = 50
E = 31337

FLAG = b'crypto{??????????????????????????}'

def bytes_to_binary(s):
    bin_str = ''.join(format(b, '08b') for b in s)
    bits = [int(c) for c in bin_str]
    return bits

def generate_mat():
    while True:
        msg = bytes_to_binary(FLAG)
        msg += [random.randint(0, 1) for _ in range(N*N - len(msg))]

        rows = [msg[i::N] for i in range(N)]
        mat = Matrix(GF(2), rows)

        if mat.determinant() != 0 and mat.multiplicative_order() > 10^12:
            return mat

def load_matrix(fname):
    data = open(fname, 'r').read().strip()
    rows = [list(map(int, row)) for row in data.splitlines()]
    return Matrix(GF(P), rows)

def save_matrix(M, fname):
    open(fname, 'w').write('\n'.join(''.join(str(x) for x in row) for row in M))

mat = generate_mat()

ciphertext = mat^E
save_matrix(ciphertext, 'flag.enc')



    I will first try to analyze the coding algorithm of the article. For

P = 2
N = 50
E = 31337

with N is the size of the matrix, in other words the matrix of the card is 50x50. The matrix will be placed in school. Fp with P = 2, almost identical to the results of XOR:

Trong F2 thì:
1 + 1 = 0
1 + 0 = 1
0 + 0 = 0
0 + 1 = 1

    The encryption process is as follows. The first flag will be converted into a binary matrix mat. If the length of flag Not larger than the 50x50. mat will be cushioned to add the number 0, 1 random at the end. Then with a mess code. mat become the matrix of its own transposition.

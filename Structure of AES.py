def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    ????

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes(matrix))







The encryption process begins with key extension, where a 128-bit keyword is used to initialize 11 different 128-bit ring locks. During key initialization, the AddRoundKey step is performed by XOR-ing the bytes of the first round with the state bytes. The algorithm then runs for 10 iterations: 9 main rounds and a final round. In each round, the SubBytes step replaces each byte of the state with one from the S-box, and the ShiftRows step shifts the rows of the state matrix by one, two, or three columns. The MixColumns step, applied only during the first 9 rounds, performs matrix multiplication on the state columns, combining 4 bytes per column. Finally, AddRoundKey is applied again by XOR-ing the state bytes with the round key bytes.

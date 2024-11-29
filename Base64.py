import base64

text ="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
result = bytes.fromhex(text)
print('Bytes representation: ',result)
print('Base64 represenattion:',end=' ')
print ('Flag: ',base64.b64encode(result).decode())

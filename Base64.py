import base64

text ="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
result = bytes.fromhex(text)
print('Bytes representation: ',result)
print('Base64 represenattion:',end=' ')
print ('Flag: ',base64.b64encode(result).decode())



we first have to turn the hex string back to byte.The initial result of the code bytes.fromhex(text) is b’r\xbc\xa9\xb6\x8f\xc1j\xc7\xbe\xeb\x8f\x84\x9d\xca\x1d\x8ax>\x8a\xcf\x96y\xbf\x92i\xf7\xbf’.

From that byte object, we will then encode it to base64 using the b64encode function

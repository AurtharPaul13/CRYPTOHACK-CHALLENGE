from Crypto.Util.number import *
text ="11515195063862318899931685488813747395775516287289682636499965282714637259206269"
print('FLAG: ',long_to_bytes(int(text)).decode())



For this one we have to install a python library called PyCryptodome in order to use the Crypto.Util.number module. You can install it using pip command pip3 install pycryptodome.
ou can technically be more specific and import just the long_to_bytes module like this from Crypto.Util.number import long_to_bytes but for the sake of future coding, might as well just import all from Crypto.Util.number.

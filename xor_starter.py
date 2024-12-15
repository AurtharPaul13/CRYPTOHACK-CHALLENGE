text='label'
result=""

for i in text:
    result += chr(ord(i)^13)

print('FLAG: ',f"crypto{{{result}}}")


In order to XOR a string to an integer, we need to convert the each of the letter to its Unicode representation, which is an int. Because normal XOR bitwise operator in Python won’t work for different characters, in this case one int and the other str.

If you want to XOR items with different formats, you can use the xor() function from the pwntools library.

However, for this example, we’ll stick with the basic XOR operation. So in order to do that, we need to convert the each character of the string “label” to its decimal value which can be achieved using the ord() function.

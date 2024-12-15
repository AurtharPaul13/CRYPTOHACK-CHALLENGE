ascii_int = [199, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

#print("Here is your flag:")
for char in ascii_int:
  print(chr(char), end="")




Solution - crypto{ASCII_pr1nt4bl3}



ASCII is an encoding scheme wherein each character has a designated integer value. This is especially useful for translating strings to other formats like hexadecimal, binary, or bytes.

You can solve this using online tools such as CyberChef, However, in order to hone our programming skills, which we would definitely need later on, we’re going to solve this using python
The code above uses the chr() function of Python. This converts the integer to its character value based on the ASCII matrix.

So basically, 199 = c, 114 = r, 121 = y, and so on. Important to remember that every character has its own unique integer value so lower and uppercase letters have different values

ciphertext = bytearray.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

flag = ""

for num in range(256): 
    results = [chr(n^num) for n in ciphertext]
    flag = "".join(results)
    
    if flag.startswith("crypto"):
        print('FLAG: ',flag)
        print(num)  

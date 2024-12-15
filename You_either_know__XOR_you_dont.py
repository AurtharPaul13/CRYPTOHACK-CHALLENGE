from pwn import xor	

message = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")


# The resulting XOR is "myXORke". It's safe to assume that the complete word is "myXORkey" thus the additional 'y'
partial_key = xor(message[:7], "crypto{").decode() + 'y'  

complete_key = (partial_key * (len(message)//len(partial_key)+1))[:len(message)]


flag = xor(message, complete_key)

print(flag.decode())



Let’s consider the given value 0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104 as the “message” and crypto{ as the flag. We’re looking for the secret key so the partial formula should look like this

message ^ secret key = “crypto{“

And in order to get to get the secret key, we should do this

message ^ “crypto{“ = partial secret key

As I said, XOR working by individual value comparison. Since we only have the first seven characters of the flag (“crypto{“), we have to XOR that to the first 7 values of the message in order to get the first 7 character of the secret key. We will do that by using the associative property of XOR

from pwn import xor	


key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key1_2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_key123 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"


key2 = xor(bytes.fromhex(key1_2), key1)
key3 = xor(bytes.fromhex(key2_3), key2)

key1_2_3 = xor(bytes.fromhex(key1_2), key3)


flag = xor(bytes.fromhex(flag_key123), key1_2_3)


print(flag.decode())




The main property you should think about in solving this challenge is the associative property.

Let me show you how to solve for key 2

key 2 = key 1 ^ (key 1 ^ key 2)

key 2 = key 1 ^ (“37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e”)

key 2 = “911404e13f94884eabbec925851240a52fa381ddb79700dd6d0d”

Same with key 3

key 3 = key 2 ^ ( key 2 ^ key 3)

key 3 = key 2 ^ (“c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1”)

key 3 = “504053b757eafd3d709d6339b140e03d98b9fe62b84add0332cc”

Now the we have the individual values of key 1, key 2, and key 3, we can now solve for the flag value using the same methods above

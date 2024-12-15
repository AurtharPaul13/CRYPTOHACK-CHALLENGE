from Crypto.Util.number import bytes_to_long, long_to_bytes

n = 95341235345618011251857577682324351171197688101180707030749869409235726634345899397258784261937590128088284421816891826202978052640992678267974129629670862991769812330793126662251062120518795878693122854189330426777286315442926939843468730196970939951374889986320771714519309125434348512571864406646232154103
e = 3
c = 63476139027102349822147098087901756023488558030079225358836870725611623045683759473454129221778690683914555720975250395929721681009556415292257804239149809875424000027362678341633901036035522299395660255954384685936351041718040558055860508481512479599089561391846007771856837130233678763953257086620228436828

for i in range(9, 93):
    PR.<x> = PolynomialRing(Zmod(n))
    flag = b'crypto{'
    m = flag + (b'\x00' * i) + b'}' + (b'\x00' * (100 - len(flag) - i - 1))
    m = bytes_to_long(m)
    f = (m + (256**(100 - len(flag) - i))*x)**e - c
    f = f.monic()
    temp = f.small_roots(epsilon=1/30)
    if temp != []:
        middle = long_to_bytes(int(temp[0]))
        flag = (flag + middle + b'}').decode()
        print(flag)
        break
    else:
        print('Not yet!!!')


With e = 3, it seems that the song applies to Coppersmith is real. However, we need to analyze the text, m = flag + b'\x00' * (100 - len(flag)), that is, there will be 100 bytes. But the song is quite banana when not to tell us the length of the flag, it is imperative that we guess

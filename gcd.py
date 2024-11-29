def gcd(x,y):
    while(y!=0):
        rem=x%y
        x=y
        y=rem
    return x
        
num1=66528
num2=52920
print(gcd(num1,num2))

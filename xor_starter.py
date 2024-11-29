text='label'
result=""

for i in text:
    result += chr(ord(i)^13)

print('FLAG: ',f"crypto{{{result}}}")

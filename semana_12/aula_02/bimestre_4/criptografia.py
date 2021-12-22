frase = input()
st = ""

for i in range(len(frase)):
    if (frase[i].upper() >= 'A') and (frase[i].upper() <= 'Y'):
        st += chr(ord(frase[i]) + 1)
    elif (frase[i] == 'z'):
        st += 'a'
    elif (frase[i] == 'Z'):
        st += 'A'
    else:
        st += frase[i]

print(frase)
print(st)

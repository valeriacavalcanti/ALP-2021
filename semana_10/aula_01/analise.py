# ler uma frase

# qtde símbolos numéricos
# qtdesímbolos alfabeto maiúsculo
# qtde símbolos alfabeto minúsculo
# qtde símbolos especiais

qtdeNum = qtdeMai = qtdeMin = qtdeEsp = 0

frase = input('Frase: ')

for i in range(len(frase)):
    if (ord(frase[i]) >= 48 and ord(frase[i]) <= 57):
        qtdeNum += 1
    elif (ord(frase[i]) >= 65 and ord(frase[i]) <= 90):
        qtdeMai += 1
    elif (ord(frase[i])>= 97 and ord(frase[i]) <= 122):
        qtdeMin += 1
    else:
        qtdeEsp += 1

print(len(frase))
print(qtdeNum)
print(qtdeMai)
print(qtdeMin)
print(qtdeEsp)

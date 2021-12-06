# ler uma frase

# qtde símbolos numéricos
# qtdesímbolos alfabeto maiúsculo
# qtde símbolos alfabeto minúsculo
# qtde símbolos especiais

qtdeNum = qtdeMai = qtdeMin = qtdeEsp = 0

frase = input('Frase: ')

for i in range(len(frase)):
    if (frase[i] >= '0' and frase[i] <= '9'):
        qtdeNum += 1
    elif (frase[i] >= 'A' and frase[i] <= 'Z'):
        qtdeMai += 1
    elif (frase[i]>= 'a' and frase[i] <= 'z'):
        qtdeMin += 1
    else:
        qtdeEsp += 1

print(len(frase))
print(qtdeNum)
print(qtdeMai)
print(qtdeMin)
print(qtdeEsp)

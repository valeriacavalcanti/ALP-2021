qtde = 0

frase = input()
vogais = "aeoiuAEIOU"

for i in range(len(frase)):
    existe = False
    for j in range(len(vogais)):
        if (frase[i] == vogais[j]):
            existe = True
            break
    if (existe == True):
        qtde += 1

print(qtde)

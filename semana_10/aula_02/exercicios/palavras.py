qtde = 0

frase = input()

for i in range(len(frase)):
    if (frase[i] == ' '):
        qtde += 1

print(qtde + 1)

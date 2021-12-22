vogais = "A E I O U".split()
qtde = [0] * len(vogais)

for i in range(10):
    frase = input().upper()

    for j in range(len(vogais)): # 0 1 2 3 4
        qtde[j] += frase.count(vogais[j])

maior = qtde[0]
for i in range(len(vogais)):
    if (qtde[i] > maior):
        maior = qtde[i]

for i in range(len(vogais)):
    if (qtde[i] == maior):
        print(vogais[i])


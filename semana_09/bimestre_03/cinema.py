qtde = 0
cinema = []
for i in range(10):
    cinema.append([False]*20)

for i in range(100):
    linha, coluna = input().split()
    linha, coluna = int(linha), int(coluna)
    if (cinema[linha][coluna] == False):
        cinema[linha][coluna] = True
        qtde += 1

print(qtde)

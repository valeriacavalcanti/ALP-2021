tela = []
for i in range(8):
    tela.append([0]*4)

for i in range(20):
    l, c = input().split()
    l, c = int(l), int(c)
    tela[l][c] += 1

maior = tela[0][0]

for i in range(8):
    for j in range(4):
        if (tela[i][j] > maior):
            maior = tela[i][j]

for i in range(8):
    for j in range(4):
        if (tela[i][j] == maior):
            print(i, j)

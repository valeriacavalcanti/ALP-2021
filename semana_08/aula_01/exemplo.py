# matriz 4 x 5

matriz = []
for i in range(4):
    matriz.append([0] * 5)

# imprimir
for i in range(4):
    print(matriz[i])

print('-'*10)

# nota 100 para o todos os alunos
for i in range(4): # 0 1 2 3
    for j in range(5): # 0 1 2 3 4
        matriz[i][j] = 100
        #print(i, j)

# imprimir
for i in range(4):
    print(matriz[i])

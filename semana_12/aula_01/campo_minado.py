import random

# montar o tabuleiro
tam = int(input('Tamanho: '))
bombas = int(input('Bombas: '))

# declarando a matriz
tabuleiro = []
for i in range(tam):
    tabuleiro.append([0] * tam)

# inserir as bombas
for i in range(bombas):
    l = random.randint(0, tam - 1)
    c = random.randint(0, tam - 1)
    while (tabuleiro[l][c] == -1):
        l = random.randint(0, tam - 1)
        c = random.randint(0, tam - 1)
    tabuleiro[l][c] = -1

# preencher as pistas

for l in range(tam):
    for c in range(tam):
        # na posição, não é bomba ==> inserir pista
        if (tabuleiro[l][c] != -1):
            # analisando as linhas
            # antes
            if (c - 1 >= 0) and (tabuleiro[l][c-1] == -1):
                tabuleiro[l][c] += 1
            # depois
            if (c + 1 < tam) and (tabuleiro[l][c+1] == -1):
                tabuleiro[l][c] += 1
            # analisando as colunas
            # antes
            if (l-1 >= 0) and (tabuleiro[l-1][c] == -1):
                tabuleiro[l][c] += 1
            # depois
            if (l+1<tam) and (tabuleiro[l+1][c] == -1):
                tabuleiro[l][c] += 1
            # analisando as diagonais
            # diagonais linha anterior
            if (l-1 >= 0) and (c-1 >= 0) and (tabuleiro[l-1][c-1] == -1):
                tabuleiro[l][c] += 1
            if (l-1 >= 0) and (c+1 < tam) and (tabuleiro[l-1][c+1] == -1):
                tabuleiro[l][c] += 1
            # diagonais linha depois
            if (l+1 < tam) and (c-1 >= 0) and (tabuleiro[l+1][c-1] == -1):
                tabuleiro[l][c] += 1
            if (l+1 < tam) and (c+1 < tam) and (tabuleiro[l+1][c+1] == -1):
                tabuleiro[l][c] += 1
# brincar
l, c = input('Posição: ').split()
l, c = int(l), int(c)
while (tabuleiro[l][c] != -1):
    print('Bombas nas adjacencias:', tabuleiro[l][c])
    l, c = input('Posição: ').split()
    l, c = int(l), int(c)

# exibir tabuleiro
for i in range(tam):
    print(tabuleiro[i])

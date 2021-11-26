import random

# montar o tabuleiro
tam = int(input('Tamanho: '))
bombas = int(input('Bombas: '))

# declarando a matriz
tabuleiro = []
for i in range(tam):
    tabuleiro.append([0] * tam)

# exibir tabuleiro
#for i in range(tam):
#    print(tabuleiro[i])

# inserir as bombas
for i in range(bombas):
    #l, c = input('Posição: ').split()
    #l, c = int(l), int(c)
    l = random.randint(0, tam - 1)
    c = random.randint(0, tam - 1)
    # verificar se é válida
    # enquanto não for válida
    while (tabuleiro[l][c] == -1):
        # gerar nova posição
        l = random.randint(0, tam - 1)
        c = random.randint(0, tam - 1)
    tabuleiro[l][c] = -1

# preencher as pistas

# brincar
l, c = input('Posição: ').split()
l, c = int(l), int(c)
while (tabuleiro[l][c] != -1):
    print('Não tem bomba!')
    l, c = input('Posição: ').split()
    l, c = int(l), int(c)

# exibir tabuleiro
for i in range(tam):
    print(tabuleiro[i])

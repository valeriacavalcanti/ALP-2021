imagem = []

for i in range(6):
    imagem.append([' '] * 6)

qtde = int(input())
for i in range(qtde):
    linha, coluna = input().split()
    linha, coluna = int(linha), int(coluna)
    imagem[linha][coluna] = '*'

for i in range(6):
    print(imagem[i])

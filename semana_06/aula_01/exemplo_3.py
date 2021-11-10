qtde = 0

nome = input('Nome: ')

# ler vários nomes, ENQUANTO for diferente de "fim" (minúsculo)
while (nome != 'fim'):
    print('entrou na repetição')
    qtde += 1
    nome = input('Nome: ')

print(qtde)

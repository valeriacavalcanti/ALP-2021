qtde = 0
soma = 0

num = int(input("Número: "))

while (num != 0):
    qtde += 1
    soma += num
    num = int(input("Número: "))

if (qtde > 0):
    media = soma/qtde
    print('Num:', num)
    print('Quantidade:', qtde)
    print('Soma:', soma)
    print('Media:', media)
else:
    print('Nenhum valor digitado')

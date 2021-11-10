qtde = 0

n = int(input('Número: '))

# perguntar vários numeros, ENQUANTO n [0,100]
while (n >= 0) and (n <= 100):
    qtde += 1
    n = int(input('Número: '))

print('terminou', qtde)

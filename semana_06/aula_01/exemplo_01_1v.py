qtde = 0

n = int(input('Número: '))

# perguntar outro número, SE n != 0
if (n != 0):
    qtde += 1
    n = int(input('Número: '))

print('terminou', qtde)

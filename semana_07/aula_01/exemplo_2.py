soma = 0
numeros = [0] * 4

for i in range(4):
    numeros[i] = int(input())
    soma += numeros[i]

media = soma/4

print('Memória')
print('i', i)
print('Números:', numeros)
print('Soma:', soma)
print('Media:', media)

# verificar se TODOS os números são > media
for i in range(4):
    if (numeros[i] > media):
        print(i, numeros[i])

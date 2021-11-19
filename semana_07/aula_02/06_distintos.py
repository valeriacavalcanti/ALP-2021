# Escreva um programa para ler vários números inteiros,
# o programa deverá encerrar quando for informado o valor 0 (zero).
# Descarte as repetições e exiba os valores que foram digitados.

numeros = []

num = int(input("Número: "))
while (num != 0):
    if (num not in numeros):
        numeros.append(num)
    num = int(input("Número: "))

print(numeros)

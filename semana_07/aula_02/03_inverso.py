# Escreva um programa para ler 06 (seis) números inteiros.
# Ao final, exiba todos os números lidos na ordem inversa.

numeros = [0]*6

for i in range(6):
    numeros[i] = int(input("Número: "))

for i in range(5, -1, -1):
    print(numeros[i])

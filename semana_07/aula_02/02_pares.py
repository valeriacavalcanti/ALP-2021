# Escreva um programa para ler 10 (dez) números inteiros.
# Ao final, exiba todos os números pares que foram lidos.

pares = []
for i in range(10):
    num = int(input("Número: "))
    if (num % 2 == 0):
        pares.append(num)

print(pares)

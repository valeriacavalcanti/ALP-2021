# Escreva um programa para ler 10 (dez) números.
# Ao final, exiba quantas vezes foram informados valores
# iguais ao último número lido.

numeros = [0]*10

for i in range(10):
    numeros[i] = int(input("Número: "))

print(numeros[9])
print(numeros.count(numeros[9]) - 1)

# deve ser o 8 ou o 9
print(numeros[:8].count(numeros[9]))
print(numeros[:9].count(numeros[9]))

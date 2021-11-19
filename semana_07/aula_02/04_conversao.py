# Escreva um programa para ler um número inteiro N (0<= N <= 100).
# Converta esse número para binário e exiba.

binario = []
num = int(input("Número: "))

while (num // 2 != 0):
    binario.append(num % 2)
    num = num // 2

binario.append(num)

for i in range(len(binario) - 1, -1, -1):
    print(binario[i], end="")

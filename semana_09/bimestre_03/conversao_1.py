valor = int(input())
binario = []
octal = []
hexa = []

# binario
divisor = valor
while (divisor // 2 != 0):
    binario.append(divisor % 2)
    divisor = divisor // 2
binario.append(divisor)

# octal
divisor = valor
while (divisor // 8 != 0):
    octal.append(divisor % 8)
    divisor = divisor // 8
octal.append(divisor)

# hexa
divisor = valor
while (divisor // 16 != 0):
    hexa.append(divisor % 16)
    divisor = divisor // 16
hexa.append(divisor)

# exibir
for i in range(len(binario) - 1, -1, -1):
    print(binario[i], end='')
print()

for i in range(len(octal) - 1, -1, -1):
    print(octal[i], end='')
print()

for i in range(len(hexa) - 1, -1, -1):
    if (hexa[i] == 10):
        print('A', end='')
    elif (hexa[i] == 11):
        print('B', end='')
    elif (hexa[i] == 12):
        print('C', end='')
    elif (hexa[i] == 13):
        print('D', end='')
    elif (hexa[i] == 14):
        print('E', end='')
    elif (hexa[i] == 15):
        print('F', end='')
    else:
        print(hexa[i], end='')
print()

numeros = []

num = int(input())
while (num not in numeros):
    numeros.append(num)
    num = int(input())

for i in range(len(numeros)):
    print(numeros[i])

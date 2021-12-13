from random import randint

# intervalo: [1,20]

lista = []
for i in range(10):
	lista.append(randint(-100,100))

maior = menor = lista[0]

for i in range(1, 10): # 1 2 3 4 ... 9
	if (lista[i] > maior):
		maior = lista[i]
	elif (lista[i] < menor):
		menor = lista[i]

print(lista)
print(menor)
print(maior)

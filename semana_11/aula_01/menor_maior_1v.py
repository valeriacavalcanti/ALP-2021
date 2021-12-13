from random import randint

# intervalo: -1 [1,20] 25

menor = 25
maior = -1

lista = []
for i in range(10):
	lista.append(randint(1,20))

for i in range(10):
	if (lista[i] > maior):
		maior = lista[i]
	elif (lista[i] < menor):
		menor = lista[i]

print(lista)
print(menor)
print(maior)

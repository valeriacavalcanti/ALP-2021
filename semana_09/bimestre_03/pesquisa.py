dezembro = soma = 0
qtde = int(input())
idades = []

for i in range(qtde):
    idade, mes = input().split()
    idade, mes = int(idade), int(mes)

    idades.append(idade)
    soma += idade

    if (mes == 12):
        dezembro += 1

# calcular a média
media = soma / qtde

# exibir a qtde dezembro
print(dezembro)

# exibir as idades acima da média (<-)
for i in range(len(idades) - 1, -1, -1):
    if (idades[i] > media):
        print(idades[i])

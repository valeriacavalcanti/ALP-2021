credito = 200
qtde = 0

valor = int(input('Valor: '))

# conceder o valor, ENQUANTO for menor ou igual ao crédito disponível
while (valor <= credito):
    qtde += 1
    credito -= valor
    valor = int(input('Valor: '))

print(qtde, credito)

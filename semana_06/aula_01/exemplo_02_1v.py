credito = 200
qtde = 0

valor = int(input('Valor: '))

# conceder o valor, SE for menor ou igual ao crédito disponível
if (valor <= credito):
    qtde += 1
    credito -= valor
    valor = int(input('Valor: '))

print(qtde, credito)

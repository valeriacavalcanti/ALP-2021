qtde = total = maior = 0

valor = float(input())
while (valor > 0):
    qtde += 1
    cupons = int(valor // 40)
    total += cupons
    if (valor > maior):
        maior = valor

    valor = float(input())

print(qtde)
print(total)
print("{:.1f}".format(maior))

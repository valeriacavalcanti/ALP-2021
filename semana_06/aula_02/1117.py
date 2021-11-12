qtde = 0
soma = 0

while (qtde < 2):
    nota = float(input())
    if (nota >= 0) and (nota <= 10):
        qtde += 1
        soma += nota
    else:
        print('nota invalida')

media = soma / 2

print('media = {:.2f}'.format(media))

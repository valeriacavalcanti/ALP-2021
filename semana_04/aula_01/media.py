nota1 = int(input('Nota 1: '))
nota2 = int(input('Nota 2: '))

media = (nota1 + nota2)/2

print('Média =', media)
print('Média = {:f}'.format(media))
print('Média = {:.3f}'.format(media))

print(media >= 70)

if (media >= 70):
    print('aprovado')
    print('que bom!')
else:
    print('reprovado')
    print('que pena')

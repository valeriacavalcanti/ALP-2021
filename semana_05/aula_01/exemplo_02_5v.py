soma = 0

qtde = int(input('Quantidade de números: '))

# quero repetir esseS comandoS 'qtde' vezes
for i in range(qtde):
    num = int(input('Número {}: '.format(i + 1)))
    soma = soma + num

print(soma)

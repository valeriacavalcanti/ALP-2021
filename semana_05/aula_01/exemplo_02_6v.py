soma = 0

qtde = int(input('Quantidade de números: '))

# quero repetir esseS comandoS 'qtde' vezes
for i in range(1, qtde + 1):
    num = int(input('Número {}: '.format(i)))
    soma = soma + num

print(soma)

soma = 0
for i in range(4):
    num = int(input("Número: "))
    soma += num

media = soma/4

print('Memória')
print('i', i)
print('Número:', num)
print('Soma:', soma)
print('Media:', media)

if (num > media):
    print('o ultimo é maior')
else:
    print('nao é maior')

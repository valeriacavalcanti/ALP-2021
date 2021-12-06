# senha
# - 4 letras maiúsculas
# - 2 letra minúsculas
# - 4 dígitos numéricos

from random import randint

senha = ''
print(len(senha))

for i in range(4):
    codigo = randint(ord('A'), ord('Z'))
    #senha += chr(codigo)
    senha = senha + chr(codigo)

for i in range(2):
    codigo = randint(ord('a'), ord('z'))
    senha += chr(codigo)

for i in range(4):
    codigo = randint(ord('0'), ord('9'))
    senha += chr(codigo)

print(senha)

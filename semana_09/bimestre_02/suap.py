qtde  = 0
nota = int(input())

while (nota < 0) or (nota > 100):
    qtde += 1
    nota = int(input())

print(nota, qtde)

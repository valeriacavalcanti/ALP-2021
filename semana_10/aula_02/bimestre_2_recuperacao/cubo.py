qtde = 0

a, l, p = input().split()
a, l, p = int(a), int(l), int(p)

while (a == l) and (a == p):
    qtde += 1

    a, l, p = input().split()
    a, l, p = int(a), int(l), int(p)

print(qtde)

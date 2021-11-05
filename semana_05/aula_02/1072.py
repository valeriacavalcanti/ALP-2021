qtde_in = 0
qtde_out = 0

qtde = int(input())
for i in range(qtde):
    num = int(input())
    if (num >= 10) and (num <= 20):
        qtde_in += 1
    else:
        qtde_out += 1

print(qtde_in, 'in')
print(qtde_out, 'out')

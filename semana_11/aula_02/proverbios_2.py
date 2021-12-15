A = E = I = O = U = 0

for i in range(10):
    st = input().upper()

    for j in range(len(st)):
        if (st[j] == 'A'):
            A += 1
        elif (st[j] == 'E'):
            E += 1
        elif (st[j] == 'I'):
            I += 1
        elif (st[j] == 'O'):
            O += 1
        elif (st[j] == 'U'):
            U += 1

print('A', A)
print('E', E)
print('I', I)
print('O', O)
print('U', U)

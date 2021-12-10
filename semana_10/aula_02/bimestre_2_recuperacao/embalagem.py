l, p, a = input().split()
l, p, a = int(l), int(p), int(a)

n = int(input())

if (l >= n) and (p >= n) and (a >= n):
    print('S')
else:
    print('N')

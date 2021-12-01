l, p, a = input().split()
l, p, a = float(l), float(p), float(a)
peso = float(input())

if (l <= 35) and (p <= 25) and (a <= 55) and (peso <= 10):
    print('S')
else:
    print('N')

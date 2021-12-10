n1, n2, n3, n4 = input().split()
n1, n2, n3, n4 = float(n1), float(n2), float(n3), float(n4)

v1 = n1 + n4
v2 = n2 - n3
v3 = (n3 + n4)/n1
v4 = (n1 + n2 + n3 + n4) * 2

print("{:.1f}".format(v1))
print("{:.1f}".format(v2))
print("{:.1f}".format(v3))
print("{:.1f}".format(v4))

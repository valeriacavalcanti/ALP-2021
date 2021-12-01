honesto = desonesto = 0

for i in range(10):
    a, d = input().split()
    a, d = float(a), float(d)

    if (d < a):
        honesto += 1
    else:
        desonesto += 1

# honestos: 6 (60.0%)
# desonestos: 4 (40.0%)

pHonesto = (honesto * 100)/10
pDesonesto = (desonesto * 100)/10

print("honestos: {} ({:.1f}%)".format(honesto, pHonesto))
print("desonestos: {} ({:.1f}%)".format(desonesto, pDesonesto))

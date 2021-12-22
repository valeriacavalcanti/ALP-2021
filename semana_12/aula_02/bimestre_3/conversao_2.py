binario = []

bit = int(input())
while (bit == 0) or (bit == 1):
    binario.append(bit)
    bit = int(input())

tam = len(binario)
decimal = 0

for i in range(tam):
    decimal += binario[i] * 2 ** (tam - i - 1)

st = str(binario)

#print(binario)
print(st.replace('[', '').replace(',', '').replace(' ', '').replace(']', ''))
print(decimal)

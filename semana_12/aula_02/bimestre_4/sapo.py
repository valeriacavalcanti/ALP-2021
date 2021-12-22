vogais = "AEIOU"

trecho = input().upper()

print(trecho)

for i in range(len(vogais)):
    for j in range(len(trecho)):
        if (trecho[j] in vogais):
            print(vogais[i], end='')
        else:
            print(trecho[j], end='')
    print()

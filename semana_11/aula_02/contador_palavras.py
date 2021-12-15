"""
Escreva um programa para ler um texto contendo várias linhas.
Ao final, o programa deverá exibir quantas palavras distintas esse texto possui
e a quantidade total de palavras.

O programa deverá encerrar quando for informada uma linha contendo XXXX.
"""

distintas = []
qtde = 0
st = input()

while (st != 'XXXX'):
    # separar as palavras. str -> list
    palavras = st.split()

    # totalizar a quantidade de palavras
    qtde += len(palavras)

    # identificar as novas palavras
    for i in range(len(palavras)):
        if (palavras[i] not in distintas):
            distintas.append(palavras[i])
    st = input()

print(len(distintas), qtde)

"""
Uma empresa de publicidade está analisando os principais provérbios populares no Brasil,
para isso, escreva um programa para ler os 10 provérbios mais comentados nas redes sociais.

Seu programa deverá exibir a quantidade de cada uma das vogais presentes nesses
provérbios lidos.
"""
A = E = I = O = U = 0

for i in range(10):
    st = input().upper()

    # Analisar a string
    A += st.count('A')
    E += st.count('E')
    I += st.count('I')
    O += st.count('O')
    U += st.count('U')

print('A', A)
print('E', E)
print('I', I)
print('O', O)
print('U', U)


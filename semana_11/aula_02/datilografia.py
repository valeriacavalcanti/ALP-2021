"""
Uma importante empresa de desenvolvimento de software realiza todos os anos uma competição 
entre seus desenvolvedores. Essa competição consiste em ler um texto impresso, digitar e 
enviar por e-mail, em 10 (dez) minutos. Historicamente provou-se que os competidores que 
possuem técnicas de datilografia possuem melhores resultados.

Escreva um programa para ler os textos enviados por 10 (dez) programadores. 
Seu programa deverá exibir o texto enviado com a maior quantidade de caracteres, ou seja,
o texto vencedor. Em seguida, essa respectiva quantidade.

Atenção! Em caso de empate, exibir os textos empatados.
"""

emails = []
maior = 0

for i in range(10):
    #email = input()
    emails.append(input())
    if (len(emails[i]) > maior):
        maior = len(emails[i])

print(maior)
for i in range(10):
    if (len(emails[i]) == maior):
        print(emails[i])

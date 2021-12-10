for i in range(38): # rodadas
    qtA = qtV = 0
    for j in range(20): # jogos da "i" jogada
        a, v = input().split()
        a, v = int(a), int(v)
        qtA += a
        qtV += v
    print(qtA, qtV)

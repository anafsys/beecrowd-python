inicial, final = map(int, input().split(" "))

if inicial < final:
    duracao = final - inicial
    print(f"O JOGO DUROU {duracao} HORA(S)")
elif inicial > final:
    duracao = 24 + (final - inicial)
    print(f"O JOGO DUROU {duracao} HORA(S)")
else:
    duracao = 24
    print(f"O JOGO DUROU {duracao} HORA(S)")
partida, viagem, fuso = map(int,input().split(" "))

res = (24+partida+viagem+fuso) % 24

print(res)
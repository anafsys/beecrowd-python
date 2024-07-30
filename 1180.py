n = int(input())
x = list(map(int,input().split()))

menor_valor = min(x)
posicao = x.index(menor_valor)

print("Menor valor: " + str(menor_valor))
print("Posicao: " + str(posicao))
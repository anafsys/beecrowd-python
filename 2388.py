n = int(input())

lista = []

for i in range(n):
    t,v = map(int,input().split(" "))
    distancia = t * v
    lista.append(distancia)

total = sum(lista)
print(total)
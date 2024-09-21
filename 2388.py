<<<<<<< HEAD
n = int(input())

lista = []

for i in range(n):
    t,v = map(int,input().split(" "))
    distancia = t * v
    lista.append(distancia)

total = sum(lista)
=======
n = int(input())

lista = []

for i in range(n):
    t,v = map(int,input().split(" "))
    distancia = t * v
    lista.append(distancia)

total = sum(lista)
>>>>>>> ee0007d29b8d1793a4c35c26777fa640729ec7fb
print(total)
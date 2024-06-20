t = int(input())

lista = []

for i in range(t):
    t1,t2 = map(int,input().split(" "))
    raio = t1 + t2
    lista.append(raio)

for total in lista:
    print(total)
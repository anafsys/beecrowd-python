<<<<<<< HEAD
t = int(input())

lista = []

for i in range(t):
    t1,t2 = map(int,input().split(" "))
    raio = t1 + t2
    lista.append(raio)

for total in lista:
=======
t = int(input())

lista = []

for i in range(t):
    t1,t2 = map(int,input().split(" "))
    raio = t1 + t2
    lista.append(raio)

for total in lista:
>>>>>>> ee0007d29b8d1793a4c35c26777fa640729ec7fb
    print(sum(total))
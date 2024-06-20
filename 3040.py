n = int(input())

lista = []

for i in range(n):
    a, d, g = map(int,input().split(" "))
    if a >= 200 and a <= 300 and d >= 50 and g >= 150:
        lista.append("Sim")
    else:
        lista.append("Nao")

for item in lista:
    print(item)
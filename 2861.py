c = int(input())

lista = []

for _ in range(c):
    c = input()
    if '?' in c:
        lista.append("gzuz")

for item in lista:
    print(item)
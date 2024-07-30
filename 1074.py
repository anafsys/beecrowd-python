n = int(input())

lista = []

for i in range(n):
    x = int(input())
    if x % 2 == 0 and x > 0:
        lista.append("EVEN POSITIVE")
    if x % 2 == 0 and x < 0:
        lista.append("EVEN NEGATIVE")
    if x % 2 != 0 and x > 0:
        lista.append("ODD POSITIVE")
    if x % 2 != 0 and x < 0:
        lista.append("ODD NEGATIVE")
    if x == 0:
        lista.append("NULL")

for item in lista:
    print(item)
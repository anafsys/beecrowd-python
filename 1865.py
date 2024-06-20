lista = []

c = int(input())
for _ in range(c):
    name, n = input().split(" ")
    n = int(n)
    if 'Thor' == name:
        lista.append("Y")
    else:
        lista.append("N")

for item in lista:
    print(item)        
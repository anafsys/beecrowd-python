lista = []

while True:
    l,r = map(int,input().split(" "))
    if l == r == 0:
        break
    soma = l + r
    lista.append(soma)

for item in lista:
    print(item)
n = int(input())

lista = []
count = 0

for i in range(n):
    x = int(input())
    
    if x == 1:
        count =+ 0
        lista.append(count)

    if x == 2 or x == 3:
        valor = 1
        lista.append(valor)

print(sum(lista))

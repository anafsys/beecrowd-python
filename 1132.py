x = int(input())
y = int(input())

if x > y:
    x, y = y, x

lista = []

for i in range(x,y + 1):
    if i % 13 != 0:
        lista.append(i)

print(sum(lista))
        



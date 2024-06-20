x = int(input())
y = int(input())

soma = 0
lista = []

menor = min(x,y)
maior = max(x,y)

for i in range(menor + 1,maior):
    if i % 2 != 0:
        lista.append(i)

soma = sum(lista)
print(soma)
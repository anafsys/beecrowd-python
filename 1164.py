lista = []
n = int(input())

for _ in range(n):
    x = int(input())
    soma = 0

    for i in range(1, x):  # Corrigido para incluir x como divisor
        if x % i == 0:
            soma += i

    if soma == x:
        lista.append(f'{x} eh perfeito')
    else:
        lista.append(f'{x} nao eh perfeito')

# Impressão dos resultados
for resultado in lista:
    print(resultado)







































'''
lista = []
soma = 0
n = int(input())

for i in range(1,n + 1):
    x = int(input())
    soma = 0  # Reinicializa a soma para cada número x
    for j in range(1, x):
        if x % j == 0:
            soma += j

if soma == i:
    lista.append(f'{x} eh perfeito')
else:
    lista.append(f'{x} nao eh perfeito')

for item in lista:
    print(item)
'''
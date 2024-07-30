
n = int(input())

resultados = []

for _ in range(n):
    x, y = map(int, input().split(" "))
    soma_impares = 0

    # Corrige a ordem dos valores se x for maior que y
    if x > y:
        x, y = y, x

    for i in range(x + 1, y):
        if i % 2 != 0:  # Verifica se i é ímpar
            soma_impares += i

    resultados.append(soma_impares)

# Imprimir os resultados
for resultado in resultados:
    print(resultado)

n = int(input())

resultados = []

for _ in range(n):
    x, y = map(int, input().split(" "))
    soma = 0

    # Garante que x seja ímpar
    if x % 2 == 0:
        x += 1

    for _ in range(y): # Executando esta linha 5 vezes
        soma += x # soma = soma + x
        x += 2  # Incrementa para o próximo número ímpar

    resultados.append(soma)

# Imprime os resultados no final
for resultado in resultados:
    print(resultado)
























'''
n = int(input())

lista = []

for _ in range(n):
    x,y = map(int,input().split(" "))
    soma = 0

    if x % 2 != 0:
        for i in range(x,y + 1):
            soma += i
            lista.append(soma)
    if x % 2 == 0:
        for i in range(x + 1, y + 1):
            soma += i
            lista.append(soma)

for elemento in lista:
    print(elemento)
''' 
def calcular_somatorio(n):
    if n % 2 == 0:
        return 0
    else:
        return 1

lista = []

# Entrada de casos de teste
quantidade_casos = int(input())

for _ in range(quantidade_casos):
    n = int(input())
    resultado = calcular_somatorio(n)
    lista.append(resultado)

for numero in lista:
    print(numero)
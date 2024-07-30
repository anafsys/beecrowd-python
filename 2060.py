
n = int(input())  # Lê o número de elementos na lista
lista = list(map(int, input().split()))  # Lê a lista de números e converte para inteiros
count2 = 0
count3 = 0
count4 = 0
count5 = 0

for x in lista:
    if x % 2 == 0:
        count2 += 1
    if x % 3 == 0:
        count3 += 1
    if x % 4 == 0:
        count4 += 1
    if x % 5 == 0:
        count5 += 1

# Imprime os resultados
print(f"{count2} Multiplo(s) de 2")
print(f"{count3} Multiplo(s) de 3")
print(f"{count4} Multiplo(s) de 4")
print(f"{count5} Multiplo(s) de 5")
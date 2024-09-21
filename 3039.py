lista = []
carrinhos = 0
bonecas = 0

n = int(input())
for i in range(n):
    nome,fem_masc = input().split(" ")
    if fem_masc == 'F':
        bonecas += 1
        
    if fem_masc == 'M':
        carrinhos += 1

lista.append(f"{carrinhos} carrinhos")
lista.append(f"{bonecas} bonecas")

for item in lista:
    print(item)
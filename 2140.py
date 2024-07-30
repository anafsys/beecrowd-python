notas = [2, 5, 10, 20, 50, 100]
lista = []

while True:
    n, m = map(int, input().split(" "))
    if n == 0 and m == 0:
        break
    
    troco = m - n
    possible = False

    for nota1 in notas:
        for nota2 in notas:
            if nota1 + nota2 == troco:
                possible = True
                break

    if possible:
        lista.append("possible")
    else:
        lista.append("impossible")

for item in lista:
    print(item)
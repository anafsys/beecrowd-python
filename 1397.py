lista = []

while True:
    n = input().strip()
    
    if n == '0':
        break

    try:
        n = int(n)
    except ValueError:
        continue

    pontos_a = 0
    pontos_b = 0

    for _ in range(n):
        a, b = map(int, input().strip().split())

        if a > b:
            pontos_a += 1
        elif b > a:
            pontos_b += 1

    lista.append((pontos_a, pontos_b))

for par in lista:
    print(f"{par[0]} {par[1]}")

resultados = []

while True:
    try:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        if a > b or b > a or a == b:
            c = 2 * a - b
            resultados.append(c)
    except EOFError:
        break

for resultado in resultados:
    print(resultado)

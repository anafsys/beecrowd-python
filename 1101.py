resultados = []

while True:
    m, n = map(int, input().split())

    if m > n:
        m, n = n, m
    if m <= 0 or n <= 0:
        break
    
    soma = 0
    linha_resultado = ""
    for i in range(m, n + 1):
        soma += i
        linha_resultado += f"{i} "

    linha_resultado += f"Sum={soma}"
    resultados.append(linha_resultado)

for resultado in resultados:
    print(resultado)
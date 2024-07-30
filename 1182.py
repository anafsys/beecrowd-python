c = int(input())
t = input()

tamanho = 12
matriz = []

for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0
for i in range(tamanho):
    soma += matriz[i][c]

resultado = soma
if t == "M":
    resultado = soma / tamanho

print(f"{resultado:.1f}")
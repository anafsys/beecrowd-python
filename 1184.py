operacao = input().strip()

tamanho = 12

matriz = []
for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append(float(input().strip()))
    matriz.append(linha)

soma = 0
contagem = 0

for i in range(tamanho):
    for j in range(i):
        soma += matriz[i][j]
        contagem += 1

if operacao == 'S':
    resultado = soma
elif operacao == 'M':
    resultado = soma / contagem

print(f"{resultado:.1f}")
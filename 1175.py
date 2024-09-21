# Recebe 20 valores inteiros
valores = [int(input()) for _ in range(20)]

# Cria a lista N invertendo a ordem dos valores
N = list(reversed(valores))

# Imprime a lista N com os índices correspondentes
for i, j in enumerate(N):
    print(f"N[{i}] = {j}")

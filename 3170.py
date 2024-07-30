# Recebe a quantidade de bolinhas que Amélia já possui
b = int(input())

# Recebe a quantidade de galhos da nova árvore de natal
g = int(input())

# Calcula a quantidade de bolinhas que Amélia precisa para decorar sua nova árvore
resultado = g // 2 if g % 2 == 0 else (g // 2)

# Verifica se Amélia tem todas as bolinhas necessárias
if resultado <= b:
    print("Amelia tem todas bolinhas!")
else:
    # Se não, imprime a quantidade de bolinhas que faltam para completar a árvore
    print(f"Faltam {resultado - b} bolinha(s)")

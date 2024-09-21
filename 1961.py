def jogo_pula_sapo(P, N, alturas):
    for i in range(1, N):
        diferenca_altura = abs(alturas[i] - alturas[i - 1])
        if diferenca_altura > P:
            return "GAME OVER"
    return "YOU WIN"

# Leitura da entrada
P, N = map(int, input().split())
alturas = list(map(int, input().split()))

# Verificação do resultado e impressão
resultado = jogo_pula_sapo(P, N, alturas)
print(resultado)
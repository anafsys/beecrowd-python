
lista = []        # Inicializa uma lista vazia para armazenar as estatísticas
grenal = 0        # Inicializa a variável para contar o número total de grenais
inter = 0         # Inicializa a variável para contar o número de vitórias do Inter
gremio = 0        # Inicializa a variável para contar o número de vitórias do Grêmio
empate = 0        # Inicializa a variável para contar o número de empates

while True:
    entrada_times = input()  # Lê a entrada, que representa os gols do Inter e do Grêmio
    i, g = map(int, entrada_times.split(" "))  # Divide a entrada nos valores de gols do Inter e do Grêmio
    grenal += 1  # Incrementa o número total de grenais

    novo_grenal = int(input())  # Lê a entrada para determinar se haverá um novo grenal
    
    if i > g:
        inter += 1
    elif i < g:
        gremio += 1
    else:
        empate += 1

    lista.append("Novo grenal (1-sim 2-nao)")  # Adiciona a mensagem de novo grenal à lista

    if novo_grenal == 2:
        lista.append(f"{grenal} grenais")  # Adiciona o número total de grenais à lista
        lista.append(f"Inter:{inter}")     # Adiciona o número de vitórias do Inter à lista
        lista.append(f"Gremio:{gremio}")   # Adiciona o número de vitórias do Grêmio à lista
        lista.append(f"Empates:{empate}")   # Adiciona o número de empates à lista

        # Determina qual time venceu mais grenais ou se houve empate
        if inter > gremio:
            lista.append("Inter venceu mais")
        elif inter < gremio:
            lista.append("Gremio venceu mais")
        else:
            lista.append("Nao houve vencedor")

        break  # Sai do loop

# Imprime a entrada e a saída
for elemento in lista:
    print(elemento)
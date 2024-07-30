lista_de_sequencias = []

while True:
    x = int(input())
    if x == 0:
        break

    sequencia = list(range(1, x + 1))
    lista_de_sequencias.append(sequencia)

for sequencia in lista_de_sequencias:
    print(" ".join(str(num) for num in sequencia))
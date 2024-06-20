lista = []

n = int(input())

for _ in range(n):
    x,y = map(float,input().split(" "))
    if y != 0:
        divisao = x / y
        lista.append(divisao)
    else:
        lista.append("divisao impossivel")

for result in lista:
    if isinstance(result, float):  #função isinstance verifica se cada elemento da lista (result) é uma instância do tipo float. Se for um número de ponto flutuante, ele é formatado e impresso com uma casa decimal. Se não for, é assumido que é uma string (possivelmente "divisao impossivel") e é impresso sem formatação.
        print(f"{(result):0.1f}")
    else:
        print(result)            
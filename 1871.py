resultados = []

while True:
    m,n = map(int,input().split(" "))
    if m == 0 and n == 0:
        break
    
    soma = m + n
    soma_sem_zeros = str(soma).replace('0', '')
    resultados.append(soma_sem_zeros)

for resultado in resultados:    
    print(resultado)
lista = []

qt = int(input())

for i in range(qt):
    nome1, escolha1, nome2, escolha2 = input().split(" ")
    j1, j2 = map(int, input().split(" ")) 
    
    soma = j1 + j2
        
    if soma % 2 == 0 and escolha1 == 'PAR':
        lista.append(nome1)
    elif soma % 2 == 0 and escolha2 == 'PAR':
        lista.append(nome2)
    elif soma % 2 != 0 and escolha1 == 'IMPAR':
        lista.append(nome1)
    elif soma % 2 != 0 and escolha2 == 'IMPAR':
        lista.append(nome2)  
    
for item in lista:
    print(item)
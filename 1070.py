
x = int(input())    # Solicita ao usuário um número inteiro e armazena em x
i = x               # Inicializa i com o valor de x
n = 1               # Inicializa n com 1

# Se x for par, pula para o próximo número ímpar
if i % 2 == 0:
    i += 1

while n <= 6:       # Continue até que 6 números ímpares sejam impressos
    print(i)         # Imprime o valor de i
    i += 2           # Incrementa i por 2 para obter o próximo número ímpar
    n += 1           # Incrementa n por 1
    



'''
x=int(input())
i = x
n = 1
while n <= x:
  if x % 2 != 0:
    print(i)
  i+=3
  n+=1
'''
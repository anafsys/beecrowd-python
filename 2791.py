
lista = []
copos = 0 
c1,c2,c3,c4 = map(int,input().split(" "))
copos = (c1,c2,c3,c4) 
lista.append(copos)
if 1 in copos:
    indice = copos.index(1) + 1 # adiciona 1 ao índice pra começar em 1 ao invés de 0
    print(indice)

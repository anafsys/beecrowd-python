
for i in range(int(input())):
    x=list(map(int,input().split()))
    z=x.pop(0) 
    print(sum(x)-z+1)

'''
z=x.pop(0)
Remove e atribui o primeiro elemento da lista x à variável z. Isso é feito para extrair o 
primeiro número da lista e garantir que ele não seja incluído na soma posterior.
'''
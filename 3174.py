b = 0
a = 0
m = 0
d = 0

for i in range(int(input())):
    e, g, h = input().split()
    h = int(h)
  
    if g == 'bonecos':
        b = b + h
    elif g == 'arquitetos':
        a = a + h
    elif g == 'musicos':
        m = m + h
    elif g == 'desenhistas':
        d = d + h

a = a // 4
b = b // 8
d = d // 12
m = m // 6

total = a + b + d + m

print(total)

''' 
n = int(input())

lista = []

for _ in range(n):
    e, g, h = input().split(" ")
    h = int(h)
   
    if g == 'bonecos':
       p = h // 8
       arred = round(p,1)
       lista.append(arred) 
    if g == 'arquitetos':
       p = h // 4
       arred = round(p,1)
       lista.append(arred)
    if g == 'musicos':
       p = h // 6
       arred = round(p,1)
       lista.append(arred)
    if g == 'desenhistas':
       p = h // 12
       arred = round(p,1)
       lista.append(arred)   

print(round(sum(lista)))
'''











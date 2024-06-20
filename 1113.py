lista = []
while True:
    x,y = map(int, input().split(" "))
    
    if x > y:
        lista.append("Decrescente")
    if x < y:
        lista.append("Crescente")
    if x == y:
        break

for elemento in lista:
    print(elemento)

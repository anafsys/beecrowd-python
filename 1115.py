lista = []

while True:
    x,y = map(int, input().split(" "))

    if x > 0 and y > 0: 
        lista.append("primeiro")

    if x < 0 and y > 0:           
        lista.append("segundo")

    if x < 0 and y < 0:   
        lista.append("terceiro")

    if x > 0 and y < 0:   
        lista.append("quarto")
    
    if x == 0 or y == 0:
        break

for elemento in lista:
    print(elemento)


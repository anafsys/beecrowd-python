t = 0
lista = []

c = int(input())

for i in range(c):
    t = input()
    char = list(t)
    t_final = (len(char) * 0.01)
    lista.append(t_final)

for item in lista:
    print(f"{(item):.2f}")
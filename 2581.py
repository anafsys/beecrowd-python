n = int(input())

lista = []

for i in range(n):
    pergunta = input()
    if '?' in pergunta:
        lista.append("I am Toorg!")
for resposta in lista:
    print(resposta)
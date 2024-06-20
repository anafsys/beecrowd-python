
lista = []
qtde_idades = 0

while True:
    idade = int(input())
    if idade < 0:
        break
    elif idade >= 1:
        lista.append(idade)
        qtde_idades += 1

if qtde_idades > 0:
    media = sum(lista) / qtde_idades
    print("%.2f" % media)










'''
lista = []
qtde_notas = 0

while True:
    nota = int(input())
    if nota <= 10:
        lista.append(nota)
        qtde_notas += 1
    if nota < 0:
        break

if qtde_notas > 0:
    media = sum(lista) / qtde_notas
    print(media)
'''
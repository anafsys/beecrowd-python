
count_nota = 0
soma_notas = 0
mensagens_invalidas = []

while count_nota < 2:
    nota = float(input())
    
    if nota < 0 or nota > 10:
        mensagens_invalidas.append("nota invalida")
    else:
        soma_notas += nota
        count_nota += 1

# Saída de mensagens de notas inválidas
for mensagem in mensagens_invalidas:
    print(mensagem)

# Saída no final, incluindo média se as duas notas foram válidas
if count_nota == 2:
    media = soma_notas / 2
    print(f"media = {media:.2f}")
























'''
count_nota = 0

while True:
    nota = float(input())
    
    if nota < 0 or nota > 10:
       print("nota invalida")
       continue
       count_nota += 1
    
    if count_nota == 2:
        media = nota / 2
        print(f"media = {(media):.2f}")
        break
'''

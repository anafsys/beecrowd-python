n = int(input())

lista = []

for i in range(n):
    h, m, o = map(int, input().split(" "))
    time_str = ''
    
    if 0 <= h <= 9:
        time_str += '0' + str(h) + ':'
    else:
        time_str += str(h) + ':'
    
    if 0 <= m <= 9:
        time_str += '0' + str(m)
    else:
        time_str += str(m)
    
    if o == 0:
        ocorrencia = 'A porta fechou!'
    else:
        ocorrencia = 'A porta abriu!'
    
    lista.append(time_str + ' - ' + ocorrencia)

for item in lista:
    print(item)

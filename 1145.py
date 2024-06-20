X, Y = map(int, input().split())

count = 0

for i in range(1, Y + 1):
    print(i, end='')
    count += 1
    
    if count == X:
        print()
        count = 0
    else:
        print(' ', end='')

# Certifica-se de imprimir uma nova linha se a última linha não estiver completa
if count > 0:
    print()
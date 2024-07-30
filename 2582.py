playlist = ['PROXYCITY','P.Y.N.G.','DNSUEY!','SERVERS','HOST!','CRIPTONIZE','OFFLINE DAY', 'SALT','ANSWER!','RAR?','WIFI ANTENNAS']
n = int(input())
while(n>0):
    n -= 1
    x, y = input().split()
    print(playlist[int(x)+int(y)])


'''
playlist = ['PROXYCITY','P.Y.N.G.','DNSUEY!','SERVERS','HOST!','CRIPTONIZE','OFFLINE DAY','SALT','ANSWER!','RAR?','WIFI ANTENNAS']
lista_final = []

c = int(input())

for i in range(c):
    try:
        x, y = map(int, input().split(" "))
        soma = x + y
        musica = playlist[soma]
        lista_final.append(musica)
    except ValueError:
        pass  

for item in lista_final:
    print(item)
'''
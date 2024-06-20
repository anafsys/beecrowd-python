n = int(input()) # valor inteiro N, que indica o número de casos de teste.

medias = [] # Lista para armazenar as médias

for _ in range(n):
    n1, n2, n3 = map(float, input().split(" ")) # Use map para converter cada valor p/float
    media = (n1 * 2 + n2 * 3 + n3 * 5) / 10
    medias.append(media) # Armazena a média na lista
    
# Imprime as médias no final
for media in medias:
    print(f"{media:.1f}")
    

'''
6.5 4.3 6.2
5.1 4.2 8.1
8.0 9.0 10.0  
'''
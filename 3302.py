testes = int(input())
cout = 0

lista = []

for i in range(testes):
    n = int(input())
    resposta = n
    cout += 1
    lista.append(f"resposta {cout}: {resposta}") # A resposta formatada é adicionada à lista usando o método append.

for resposta in lista: # Imprime as respostas em linhas separadas
    print(resposta)
    

for i in range(1,10,2):
    for j in range(6+i,3+i,-1):
        print(f"I={i} J={j}")

'''
Quando i é 1:

range(6 + 1, 3 + 1, -1) é equivalente a range(7, 4, -1).
Isso cria uma sequência decrescente de números de 7 até 5 (exclusivo), com um passo de -1.

Quando i é 3:

range(6 + 3, 3 + 3, -1) é equivalente a range(9, 6, -1).
Isso cria uma sequência decrescente de números de 9 até 7 (exclusivo), com um passo de -1.
Portanto, o loop for j in range(6 + i, 3 + i, -1) está iterando sobre uma sequência 
decrescente de valores de j, onde o ponto de partida é 6 + i, o ponto final é 3 + i (exclusivo), 
e o passo é -1.
'''
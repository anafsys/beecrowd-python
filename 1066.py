
x = [int(x) for x in input("").split()]
par = 0
imp = 0
pos = 0
neg = 0

for numero in x:
    if numero % 2 == 0:
        par = par +1
        
    else:
        imp = imp +1
        
    if numero > 0:
        pos = pos +1
        
    elif numero < 0:
        neg = neg +1
        
print("{} valor(es) par(es)".format(par))
print("{} valor(es) impar(es)".format(imp))
print("{} valor(es) positivo(s)".format(pos))
print("{} valor(es) negativo(s)".format(neg))













'''Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos 
valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores 
digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o 
final de linha após cada uma.'''
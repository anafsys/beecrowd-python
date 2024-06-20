import itertools #ferramentas eficientes em termos de memória para trabalhar com iteradores

t = int(input())

for i, x in zip(range(1000), itertools.cycle(range(t))): # Isso emparelha os elementos dos dois iteráveis. Isso para quando o mais curto dos dois for esgotado.
    print(f"N[{i}] = {x}")

'''
t = int(input())

for i,x in zip(range(0,1000), range(0,t)):
    print(f"N[{i}] = {x}")
'''    
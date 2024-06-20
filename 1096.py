
for _ in range(1): #loop externo
    for i in range(1, 10, 2): #itera pelos valores de i
        for j in range(7, 4, -1): #itera pelos valores de j
            print(f"I={i} J={j}")



'''
for i in range(1,10,2):
    for _ in range(3): # Loop para repetir cada número três vezes
        print(f"I={i:<1}")

for _ in range(3): # Loop externo para repetir a sequência três vezes
    for j in range(7,4,-1):
        print(f"J={j:<1}")
'''
'''for i, j in zip(range(1,10,2), range(7,-5,-1)):
    print(f"I={i:<1} J={j:<1}")
'''
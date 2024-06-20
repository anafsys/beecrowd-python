
n = int(input())

for i, j, k in zip(range(1,n + 1), range(1,n + 1), range(1,n + 1)):
    print(f"{i:<1} {j ** 2:<1} {k ** 3:<1}") #impressão em três colunas 



'''
for i in range(1,n + 1):
    print(i)

for j in range(1,n + 1):
    print(j ** 2)

for l in range(1,n + 1):
    print(l ** 3)
'''
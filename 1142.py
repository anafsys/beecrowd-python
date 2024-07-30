
n = int(input())

for i, j, k in zip(range(1,n * 4,4), range(2, n * 4,4), range(3, n * 4,4)):
    print(f"{i:<1} {j:<1} {k:<1} {'PUM'}") #impressão em quatro colunas

'''
for i in range(1,n * 4,4):
    print(i)

for i in range(2, n * 4,4):
    print(i)

for i in range(3, n * 4,4):
    print(i)
'''
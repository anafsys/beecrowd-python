t = 'A[{0}] = {1}' 
a = [] 

for i in range (100): 
    i = float(input())
    a.append(i)

for j in range (100): 
    if a[j] <= 10: 
        print(t.format(j, a[j]))
S = 0  

for i in range(1, 40, 2):
    S += i / (2 ** ((i-1)//2))

print(f"{S:.2f}")
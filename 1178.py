x = float(input())
x = round(x, 4)

for i, y in enumerate(range(100)):
    y = x / (2 ** i)
    print(f"N[{i}] = {y:.4f}")



'''
for i in range(1,100):
       print(f"N[{i}] = {(y):.4f}")
'''



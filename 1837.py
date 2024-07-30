a, b = map(int,input().split(" "))

if b != 0:
    r = a % b
    q = (a - r) / b
    print(q + r)
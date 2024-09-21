<<<<<<< HEAD
p1, c1, p2, c2 = map(int, input().split(" "))

esq = p1 * c1
dir = p2 * c2

if esq == dir:
    print("0")
elif esq > dir:
    print("-1")
else:
=======
p1, c1, p2, c2 = map(int, input().split(" "))

esq = p1 * c1
dir = p2 * c2

if esq == dir:
    print("0")
elif esq > dir:
    print("-1")
else:
>>>>>>> ee0007d29b8d1793a4c35c26777fa640729ec7fb
    print("1")
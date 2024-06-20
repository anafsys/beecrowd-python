a_1001 = 1.5
a_1002 = 2.5
a_1003 = 3.5
a_1004 = 4.5
a_1005 = 5.5

prod_val = [a_1001, a_1002, a_1003, a_1004, a_1005]

p = int(input())

total = 0

for _ in range(p):
    prod_cod, q = map(int,input().split(" "))
    if 1001 <= prod_cod <= 1005:
        prod_unit = prod_val[prod_cod - 1001]
        sub_total = prod_unit * q
        total += sub_total
print(f"{(total):.2f}")
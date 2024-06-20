n = int(input()) # valor inteiro N, que indica o número de casos de teste.
cout_in = 0
cout_out = 0

for i in range(n):
    x = int(input())
    if 10 <= x <= 20:
        cout_in += 1
    else:
        cout_out += 1

print("%i in" % cout_in)
print("%i out" % cout_out)
    
n = int(input())

if n % 2 != 0:
    brancas = (n * n + 1) / 2
    pretas = (n * n - 1) / 2

if n % 2 == 0:
    brancas = (n * n) / 2
    pretas = (n * n) / 2

print(f"{(brancas):.0f} casas brancas e {(pretas):.0f} casas pretas")




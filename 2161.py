n = int(input())
raiz_quad = 0

for i in range(n):
    raiz_quad = 1 / (6 + raiz_quad)

raiz_quad = 3 + raiz_quad

print(f"{raiz_quad:.10f}")
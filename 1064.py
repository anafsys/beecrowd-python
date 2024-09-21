
quantidade = 0
soma_positivos = 0

for i in range(6):
    valor = float(input())
    if valor > 0:
        quantidade += 1
        soma_positivos += valor #soma os valores do input

media = soma_positivos / quantidade if quantidade > 0 else 0

print(quantidade, "valores positivos")
print(f"{(media):.1f}")

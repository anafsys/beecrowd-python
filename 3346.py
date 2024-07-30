
entrada_valores = input()

f1,f2 = map(float,entrada_valores.split())  # Dividindo a entrada em dois valores

pib_flut = ((((1.0 + f1/100.00) * (1.0 + f2/100.00)) - 1.0) * 100.0)

print(f"{(pib_flut):.6f}")


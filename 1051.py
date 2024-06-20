salario = input()

salario = float(salario)

imposto = 0

if salario <= 2000:
    print("Isento")

if salario >= 2000.01 and salario <= 3000:
    imposto = (salario - 2000) * 0.08
    print(f"R$ {imposto:.2f}") 

if salario >= 3000.01 and salario <= 4500:
    imposto = (salario - 3000) * 0.18 + 80
    print(f"R$ {imposto:.2f}") 

if salario >= 4500.01:
    imposto = (salario - 4500) * 0.28 + 350
    print(f"R$ {imposto:.2f}") 
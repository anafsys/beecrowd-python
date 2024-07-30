
# Obtendo entrada do usuário para números separados por espaço
entrada_usuario = input()

# Convertendo a entrada em uma lista de inteiros
numeros = [int(numero) for numero in entrada_usuario.split()]

# Ordenando a lista de números
numeros.sort()

# Exibindo a lista resultante
print()

for numero in numeros:
    print(numero)

# espaço em branco
print()

# Exibindo a entrada original em linhas separadas
for entrada in entrada_usuario.split():
    print(entrada)





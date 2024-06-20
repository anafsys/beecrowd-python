 # Entrada de dados: recebe uma linha como uma string e a divide em uma lista de substrings
valores = input().split()

# Converte o primeiro elemento da lista para um número inteiro e atribui a variável 'a'
a = int(valores[0])

# Calcula o índice do último elemento na lista
ultimo_valor = len(valores) - 1

# Converte o último elemento da lista para um número inteiro e atribui a variável 'n'
n = int(valores[ultimo_valor])

# Inicializa a variável de soma
soma = 0

# Loop que itera de 0 até (n-1)
for i in range(0, n):
    # Adiciona à soma o valor de 'a + i' em cada iteração
    soma += a + i

# Exibe o resultado final da soma
print(soma)

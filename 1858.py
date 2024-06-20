n = int(input()) # numero de casos de teste
t = list(map(int, input().split())) # mesmo numero n de entradas

min_value = min(t)
min_index = t.index(min_value)

print(min_index + 1)
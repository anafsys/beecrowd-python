cod = int(input())

cidades = {"Brasilia":61, "Salvador":71, "Sao Paulo":11, "Rio de Janeiro":21, "Juiz de Fora":32, "Campinas":19, "Vitoria":27, "Belo Horizonte":31}

for cidade, codigo in cidades.items(): 
    if codigo == cod:
        print(f"{cidade}")
        break
else:
    print("DDD nao cadastrado")

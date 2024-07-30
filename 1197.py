while True:
    try: 
        v, t = (input().split(" "))

        v = int(v)
        t = int(t)

        distancia = v * (t * 2)
        print(distancia)
    except EOFError:
        break
    
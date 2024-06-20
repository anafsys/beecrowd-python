while True:
    try:
        v = float(input())
        d = float(input())
        
        altura = (4 * v) / (3.14 * (d ** 2))
        area = 3.14 * ((d/2) * (d/2))

        print(f"ALTURA = {altura:.2f}")
        print(f"AREA = {area:.2f}")
        
    except EOFError:
        break

turistas = 0
jipes_no_parque = 0

while True:
    try:
        entrada = input().strip()
        if entrada == 'ABEND':
            break
        sv, t = entrada.split(" ")
        t = int(t)
        
        if sv == 'SALIDA':
            turistas += t
            jipes_no_parque += 1
        elif sv == 'VUELTA':
            turistas -= t
            jipes_no_parque -= 1
    except ValueError:
        continue

print(turistas)
print(jipes_no_parque)
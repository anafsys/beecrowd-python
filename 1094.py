<<<<<<< HEAD
c = 0
r = 0
s = 0

n = int(input())
for i in range(n):
    quantia, tipo = input().split(" ")
    quantia = int(quantia)
    if tipo == 'C':
        c += quantia
    elif tipo == 'R':
        r += quantia
    elif tipo == 'S':
        s += quantia
    
total_cobaias = c + r + s

print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
print(f"Percentual de coelhos: {(c / total_cobaias * 100):.2f} %") 
print(f"Percentual de ratos: {(r / total_cobaias * 100):.2f} %")
=======
c = 0
r = 0
s = 0

n = int(input())
for i in range(n):
    quantia, tipo = input().split(" ")
    quantia = int(quantia)
    if tipo == 'C':
        c += quantia
    elif tipo == 'R':
        r += quantia
    elif tipo == 'S':
        s += quantia
    
total_cobaias = c + r + s

print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
print(f"Percentual de coelhos: {(c / total_cobaias * 100):.2f} %") 
print(f"Percentual de ratos: {(r / total_cobaias * 100):.2f} %")
>>>>>>> ee0007d29b8d1793a4c35c26777fa640729ec7fb
print(f"Percentual de sapos: {(s / total_cobaias * 100):.2f} %")
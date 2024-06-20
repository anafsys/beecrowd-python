H,Z,L=input().split()

# Os valores de H, Z e L são armazenados em uma lista chamada A. Em seguida, essa lista é 
# ordenada em ordem crescente, e o resultado é armazenado na variável a.

A = [H, Z, L]
a = sorted(A)

if(a[1]==H):
    print("huguinho")
elif(a[1]==Z):
    print("zezinho")
elif(a[1]==L):
    print("luisinho")
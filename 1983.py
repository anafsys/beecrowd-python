n = int(input())  

maior_nota = -1  
matricula_maior_nota = None

for _ in range(n):
    mat, nota = input().split()  
    mat = int(mat)  
    nota = float(nota)  
    
    if nota >= 8 and nota > maior_nota:
        maior_nota = nota
        matricula_maior_nota = mat

if matricula_maior_nota is not None:
    print(matricula_maior_nota)
else:
    print("Minimum note not reached")      
n, m = map(int,input().split(' '))

for i in range(m):
    acao = input()
    if acao == 'fechou':
        n = n - 1 + 2
    elif acao == 'clicou':
        n = n - 1

print(n)
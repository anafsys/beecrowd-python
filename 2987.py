l = input()

alphabet = ['0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

position = alphabet.index(l)

print(position)

'''
O método index em Python é sensível a maiúsculas e minúsculas, então se o usuário inserir 
uma letra maiúscula, o código não encontrará a letra na lista do alfabeto em minúsculas.
'''
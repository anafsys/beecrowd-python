import re #Importa o módulo re, que fornece suporte para expressões regulares em Python.

cpf = input()

digitos = re.split("[.-]",cpf) #Usa a função re.split para dividir a string do CPF em uma lista de substrings,

for digito in digitos:
    print(digito)








'''
lista = []

digitos1 = cpf.split('.')
digitos2 = digitos1.split('-')

lista.append(digitos1)
lista.append(digitos2)

for item in lista: 
    print(item)
'''

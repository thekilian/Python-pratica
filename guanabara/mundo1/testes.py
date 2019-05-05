'''
from random import randint
num = randint(1, 6)
res = num // 2
print(res)
'''

'''
num = 4.999
print(int(num))
'''

'''
res = 5 * 3 ** 2
print(res)
'''

'''
from random import choice
n = [2, 5, 1, 9, 4]
res = choice(n) % n[0]
print(res)
'''

'''
frase = 'Curso em Video de Python'
separado = frase.split()
palavra = separado[2]
letra = palavra[3]
print(letra.upper())
'''

'''
nome = 'Joao dos Anjos Moura'
print(nome[1:10:2].upper())
'''

'''
if a>b:
    print('X')
else:
    print('Y')
    print('W')
print('Z')
'''

'''
if condição: (ESTA)
if condição: bloco else: bloco (NAO)
if condição else bloco (NAO)
if condição
if: else:
'''

'''
valor = '153'
parte = "5"
valor += parte
print(valor.isnumeric())
'''

'''
n1 = 5
n2 = 2
res = n1 / n2 // 1
print(res)
'''

'''
texto = 'Tres Pratos de Trigo para Tigres Tristes'
total = texto.upper().count(texto[0])
print(total)
'''

'''
num = '7'
res = int(num) / 2
print(type(res))
'''

'''
from datetime import date
ano = date.today().year
print(ano)
'''

'''
preço = 1500
novo = preço + 50 if preço < 1000 else preço - 35
print(novo)
print('*' * 20)
if preço < 1000:
    novo = preço + 50
else:
    novo = preço - 35
(print(novo))
'''

'''
res =  3 + 2 * 4
print(res)
'''
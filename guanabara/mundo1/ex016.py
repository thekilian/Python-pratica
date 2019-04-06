# 016 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
'''
Ex.:
    Digite um número: 6.127
    O número 6.127 tem a parte inteira de 6.
'''
'''
from math import floor
num = float(input('Digite um número: '))
inteiro = floor(num)
print('O número {} tem a parte inteira de {}'.format(num, inteiro))
'''

'''
# outra maneira de resolver:
from math import trunc
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira de {}'.format(num, trunc(num)))
'''

# mais uma maneira de resolver, sem importar math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
# 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

'''
# maneira tradicional/matemática de resolver:
cat_oposto = float(input('Digite o comprimento do cateto oposto: '))
cat_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = (cat_oposto ** 2 + cat_adjacente ** 2) **(1/2)

print('Tendo {}cm de cateto oposto e {}cm de cateto adjacente, o comprimento da hipotenusa será {:.2f}cm.'.format(cat_oposto, cat_adjacente, hipotenusa))
'''

'''
# importando classe math:
import math
op = float(input('Digite o comprimento do cateto oposto: '))
ad = float(input('Digite o comprimento do cateto adjacente: '))
hip = math.hypot(op, ad)

print('A hipotenusa vai medir {:.2f}'.format(hip))
'''

# importando apenas o que será utilizado - hypot:
from math import hypot
op = float(input('Digite o comprimento do cateto oposto: '))
ad = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(op, ad)

print('A hipotenusa vai medir {:.2f}'.format(hip))
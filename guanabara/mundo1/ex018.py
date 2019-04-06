# 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

'''
from math import sin, cos, tan

ang = float(input('Digite um ângulo: '))
sen = sin(ang)
cos = cos(ang)
tan = tan(ang)

print('Ângulo de {}°: \n Seno = {:.2f} \n Cosseno = {:.2f} \n Tangente = {:.2f}'.format(ang, sen, cos, tan))
'''

'''
# apenas faltou conventer para radiano:
import math
ang = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan))
'''

# importando somente o que vamos utilizar: sin, cos, tan, radians

from math import sin, cos, tan, radians
ang = float(input('Digite um ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print('Ângulo de {}°: \n Seno = {:.2f} \n Cosseno = {:.2f} \n Tangente = {:.2f}'.format(ang, sen, cos, tan))
# -*- coding: utf-8 -*-

#006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
print('Você digitou {}: '.format(n))
print('O dobro de {} é {}'.format(n, n * 2))
print('O triplo de {} é {}'.format(n, n * 3))
print('A raíz quadrada de {} é {:.3f}'.format(n, n ** (1/2)))
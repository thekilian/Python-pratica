# -*- coding: utf-8 -*-

#008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

'''
m = float(input('Digite o valor (em metros): '))
c = m * 100
mm = m * 1000

print('O valor que você digitou é: {}m'.format(m))
print('O valor em centímetros é: {}cm'.format(c))
print('O valor em milímetros é: {}mm'.format(mm))
'''

'''
Complemento do exercício: fazer as outras escalas:

# km hm dam m dm cm mm
# Escala: quilômetro - hectômetro - decâmetro - metro - decímetro - centímetro - milímetro
'''

m = float(input('Digite o valor (em metros): '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
c = m * 100
mm = m * 1000

print('Escala de {}m:'.format(m))
print('-' * 12)
print('O valor em quilômetro é: {}km'.format(km))
print('O valor em hectômetro é: {}hm'.format(hm))
print('O valor em decâmetro é: {}dam'.format(dam))
print('O valor em decímetro é: {}dm'.format(dm))
print('O valor em centímetro é: {}cm'.format(c))
print('O valor em milímetro é: {}mm'.format(mm))
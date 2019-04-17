'''
032 - Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''

from datetime import date
ano = int(input('Qual ano você quer saber? \nDigite 0 para analisar o ano atual: '))
print('Você digitou {}'.format(ano))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é BISSEXTO!'.format(ano))
else:
    print('{} NÃO é bissexto.'.format(ano))

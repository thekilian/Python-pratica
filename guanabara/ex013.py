# -*- coding: utf-8 -*-

#013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual seu salário? R$'))

aumento = salario + (salario * 15 / 100)

print('Parabéns, você terá um aumento de 15%. Então, agora você ganha {:.2f}!'.format(aumento))
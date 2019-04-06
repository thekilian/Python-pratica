# -*- coding: utf-8 -*-

#010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,27

r = float(input('Hey, quanto dinheiro você tem na carteira agora? R$'))

d = r / 3.27

print('Sabia que com R${:.2f} você pode comprar US${:.2f}?'. format(r, d))
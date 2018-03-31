# -*- coding: utf-8 -*-

#011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

l = float(input('Digite a largura (em metros): '))
a = float(input('Digite a altura (em metros): '))

area = l * a
tinta = area / 2

print('Para uma parede de {}m de largura por {}m de altura, você tem uma área de {}m². Então, você precisa de {:.0f}l de tinta para pintá-la. Boa sorte e boa pintura!'.format(l, a, area, tinta))
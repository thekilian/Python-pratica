# -*- coding: utf-8 -*-

#007 - Desenvolva um progama que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

print('A média entre {} e {} é {:.1f}'.format(n1, n2, media))
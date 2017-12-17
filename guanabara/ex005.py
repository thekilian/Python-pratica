# -*- coding: utf-8 -*-

#005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número inteiro: '))

print('Você digitou: {}'.format(n))
print('O sucessor de {} é {}'.format(n, n + 1), end='. ')
print('O antecessor de {} é {}.'.format(n, n - 1))
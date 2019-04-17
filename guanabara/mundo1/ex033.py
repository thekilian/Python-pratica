'''
033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

print('Você digitou os números: {}, {} e {}.'.format(a, b, c))

'''
if n1 > n2 and n1 > n3:
    maior = n1

if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n2:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1

if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3
'''

# verificando qual é o maior valor:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

# verificando qual é o menor valor:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print('O maior número é {}. \nO menor número é {}.'.format(maior, menor))
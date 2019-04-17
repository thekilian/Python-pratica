'''
035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
a = float(input('Comprimento da 1° reta: '))
b = float(input('Comprimento da 2° reta: '))
c = float(input('Comprimento da 3° reta: '))

if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    print('É um triângulo!')
else:
    print('Não é um triângulo.')

'''
Um triângulo só pode existir se a soma de dois lados for maior que o terceiro lado
| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b
'''

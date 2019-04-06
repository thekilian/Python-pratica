'''
023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Exemplo:
Digite um número: 1834

unidade: 4
dezena: 3
centena: 8
milhar: 1

* fazer o exercício como string e matematicamente
'''

# string
'''
num = int(input('Digite um número: '))
n = str(num)
print('Analisando o número {}'.format(num))
print("Unidade: {}".format(n[3]))
print("Dezena: {}".format(n[2]))
print("Centena: {}".format(n[1]))
print("Milhar: {}".format(n[0]))
# obs.: vai dar erro se não digitar 4 números
'''

num = int(input('Informe um número: '))
u = num // 1 % 10 # divisão inteira e módulo de 10
d = num // 10 % 10
c = num // 100 % 10
m = num //1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

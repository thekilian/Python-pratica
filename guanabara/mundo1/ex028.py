'''
028 - Escreva um programa que faça o computador "pensar"  em um número inteiro de 0 a 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

'''
from random import randint
num = randint(0, 5)
palpite = int(input('O computador escolheu um número de 0 a 5. \nVocê consegue descobrir qual foi? \nDigite seu palpite: '))
print('O número escolhido pelo computer foi {}.'.format(num))
if num == palpite:
    print('Parabéns, você acertou!')
else:
    print("Sorry, not sorry! You're wrong!")
'''

# com firulas:
from random import randint
from time import sleep
num = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 a 5. Tente adivinhar...')
print('-=-' * 20)
palpite = int(input('Digite seu palpite: '))
print('PROCESSANDO...')
sleep(2)
print('O número escolhido pelo computer foi {}.'.format(num))
if num == palpite:
    print('Parabéns, você acertou!')
else:
    print("Sorry, not sorry! You're wrong!")

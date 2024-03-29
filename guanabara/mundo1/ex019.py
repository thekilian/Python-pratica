# 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

'''
from random import shuffle
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print('O aluno escolhido foi: {}'.format(alunos[0]))
'''

'''
# método choice da classe random:
import random
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(alunos)
print('O aluno escolhido foi: {}'.format(escolhido))
'''

# importando somente o que precisamos: choice
from random import choice
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(alunos)
print('O aluno escolhido foi: {}'.format(escolhido))
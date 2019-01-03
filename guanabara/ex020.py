# 020 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

'''
from random import shuffle
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print("Sorteio - aluno n°1: {}".format(alunos[0]))
print("Sorteio - aluno n°2: {}".format(alunos[1]))
print("Sorteio - aluno n°3: {}".format(alunos[2]))
print("Sorteio - aluno n°4: {}".format(alunos[3]))
'''

'''
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print("A ordem de apresentação será: ")
print(lista)
'''

# importando apenas o que será utilizado
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print("A ordem de apresentação será: ")
print(lista)

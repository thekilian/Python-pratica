'''
022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas.
- O nome com todas as letras minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''

'''
nome = input('Qual seu nome completo? ')
alta = nome.upper()
baixa = nome.lower()

space = nome.strip()
no_space = space.replace(" ", "")
tamanho = len(no_space)

separar = nome.split()
primeiro = len(separar[0])

print("Seu nome é: {} \n Seu nome em caixa alta fica assim: {} \n Seu nome em caixa baixa fica assim: {} \n Seu nome completo tem {} letras \n Seu primeiro nome tem {} letras".format(nome, alta, baixa, tamanho, primeiro))
'''

nome = str(input('Qual seu nome completo? ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
'''
031 - Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
'''
dist = int(input('Qual a distância da viagem em km? '))
print('Você digitou {}km'.format(dist))
if dist <= 200:
    print('O preço da passagem é de R${}.'.format(dist * 0.50))
else:
    print('O preço da passagem é de R${}'.format(dist * 0.45))

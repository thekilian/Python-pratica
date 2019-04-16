'''
031 - Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
'''

'''
# 1st try:
dist = float(input('Qual a distância da viagem em km? '))
print('Você digitou {:.0f}km'.format(dist))
if dist <= 200:
    print('O preço da passagem é de R${:.2f}.'.format(dist * 0.50))
else:
    print('O preço da passagem é de R${:.2f}'.format(dist * 0.45))
'''

'''
# Guanabara:
dist = float(input('Qual a distância da viagem? '))
print('Você vai viajar {:.0f}km.'.format(dist))
if dist <=200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print('O preço da passagem será de R${:.2f}.'. format(preco))
'''

'''
# simplificada (if inline / operador ternário em outras linguagens):
dist = float(input('Qual a distância da viagem? '))
print('Você vai viajar {:.0f}km.'.format(dist))

preco = dist * 0.50 if dist <= 200 else dist * 0.45

print('O preço da passagem será de R${:.2f}.'. format(preco))
'''

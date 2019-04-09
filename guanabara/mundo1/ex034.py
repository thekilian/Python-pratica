'''
034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input('Qual seu salário? R$'))
print('Seu salário é de R${:.2f}'.format(salario))
if salario > 1250:
    aumento = (salario * 10) / 100
    total = salario + aumento
    print('Você receberá R${:.2f} de aumento. \nSeu salário será de R${:.2f}.'.format(aumento, total))
else:
    aumento = (salario * 15) / 100
    total = salario + aumento
    print('Você receberá R${:.2f} de aumento. \nSeu salário será de R${:.2f}.'.format(aumento, total))
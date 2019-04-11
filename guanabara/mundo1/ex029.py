'''
029 - Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.
'''

speed = float(input('Qual a velocidade do carro? '))
print('A velocidade do carro é de {:.0f}km/h.'.format(speed))

if speed > 80:
    print('Você foi MULTADO! Você excedeu o limite de velocidade de 80km/h.')
    multa = (speed - 80) * 7
    print('A multa será de R${:.2f}'.format(multa))
print('Tenha um bom dia e dirija com segurança!!!')
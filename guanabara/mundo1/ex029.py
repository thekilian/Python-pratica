'''
029 - Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.
'''

speed = int(input('Qual a velocidade do carro? '))
print('A velocidade do carro é de {}km/h.'.format(speed))
max_speed = 80

if speed >= max_speed:
    test = speed - max_speed
    result = test * 7.00
    print('Você foi multado!')
    print('A multa será de R${}'.format(result))
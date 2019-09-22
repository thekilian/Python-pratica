'''
039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- se ele ainda vai se alistar ao serviço militar
- se é a hora de se alistar
- se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date

ano = int(input('Qual ano de nascimento? '))
ano_atual = date.today().year

print('Você nasceu em {}. Considerando que estamos em {}:'.format(ano, ano_atual))

idade = ano_atual - ano

if(idade < 18):
    print('Você não tem idade para se alistar.')
elif(idade == 18):
    print('Você deve se alistar este ano!')
elif(idade > 18 or idade < 45):
    print('Você já deveria ter se alistado!!!')
elif(idade > 50):
    print('Eita...')

# A obrigação para com o Serviço Militar, em tempo de paz, começa no dia 1º de janeiro do ano em que o cidadão completar 18 anos de idade e subsistirá até 31 de dezembro do ano em que completar 45 anos.
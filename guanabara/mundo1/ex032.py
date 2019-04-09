'''
032 - Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''

ano = int(input('Digite um ano: '))
print('Você digitou {}'.format(ano))

if (ano % 4 == 0):
    print('{} é BISSEXTO!'.format(ano))
else:
    print('{} não é bissexto.'.format(ano))


'''
Um ano é bissexto quando ele é divisível por 4. Porém, existe uma exceção. Os anos que terminam por dois zeros serão bissextos se forem divisíveis por 400.

Exemplo: 
2012 é um ano bissexto. Pois 2012 / 4 = 503, ou seja, uma divisão exata. 
1998 não é um ano bissexto, pois 1998 / 4 = 499,5, uma divisão inexata.
5000 não é um ano bissexto pois, apesar de ser divisível por 4, é um número terminado em 00 e não é divisível por 400.
'''
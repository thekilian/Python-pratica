'''
038 - Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior, os dois são iguais
'''
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
print('Você digitou: {} e {}. Analisando os números informados:'.format(n1, n2))

if(n1 > n2):
    print('O primeiro número é maior.')
elif(n2 > n1):
    print('O segundo número é maior.')
else:
    print('Não existe valor maior. Os dois são iguais.')
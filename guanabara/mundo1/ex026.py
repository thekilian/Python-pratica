'''
026 - Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.
'''

phrase = str(input('Digite uma frase: ')).upper().strip()
print("A frase que você digitou foi: {}".format(phrase))
print("A letra 'A' aparece {} vezes nesta frase.".format(phrase.count('A')))
print("A letra 'A' aparece pela primeira vez na posição {}.".format(phrase.find('A')+1))
print("A letra a aparece pela última vez na posição {}.".format(phrase.rfind('A')+1))
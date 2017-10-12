# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ela.

info = input("Digite algo: ")

print("O tipo primitivo desse valor é {}".format(type(info)))
print("Só tem espaços? {}".format(info.isspace()))
print("É um número? {}".format(info.isnumeric()))
print("É alfabético? {}".format(info.isalpha()))
print("É alfanumérico? {}".format(info.isalnum()))
print("Está em maiúsculas? {}".format(info.isupper()))
print("Está em minúsculas? {}".format(info.islower()))
print("Está em capitalizda? {}".format(info.istitle()))

'''
Faça um algoritmo que utilize o menu abaixo onde:
Na opção 1: voce deverá realizar o cadastro do nome, o salário e o sexo(m/f) de uma pessoa.
Na opção 2: você deverá apenas listar os dados cadastrados
Na opção 3: você deverá calcular a média dos salarios cadastrados e imprimir o nome das pessoas cujos salários estáo acima da média.
Na opção 4: você deverá imprimir o nome e o salário do homem que ganha mais e, o nome e o salário da mulher que ganha mais. Mostre também a diferença de salário entre eles.
Na opção 5: Você deverá ler um valor percentual e dar aumento para todos que ganham abaixo da média.
'''

menu = '''
====================
MENU
====================
0- Finaliza
1- Cadastro
2- Relatório Geral
3- Relatório Acima da Média
4- Maiores Salários
5- Aumento salarial
====================
Escolha: '''

while True:
    escolha = input(menu)
    if escolha == '0':
        break
    elif escolha == '1':
    elif escolha == '2':
    elif escolha == '3':
    elif escolha == '4':
    elif escolha == '5':
print("Fim.")
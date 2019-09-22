# MUNDO 2
# Estrutura de Controle - Condições e Laços

- Condições simples, compostas e aninhadas
- Iterações: estruturas de repetição com variável de controle com teste lógico no início; e as repetiçõs infinitas com interrupção no meio

## Fase 12: Condições aninhadas

- Condições aninhadas: estruturas condicionais dentro de estruturas condicionais

- Estruturas condicionais = verdadeiro ou falso (TRUE or FALSE)

***CONDIÇÕES SIMPLES:***

```
nome = str(input('Qual seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
print('Tenha um bom dia {}!'.format(nome))
```


***CONDIÇÃO COMPOSTA:***

```
nome = str(input('Qual seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome))
```

***ESTRUTURA CONDIONAL ANINHADA:***
- é aninhada pois está em formato de ninho - uma coisa dentro da outra
```
nome = str(input('Qual seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome =='Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome))
```

- outro exemplo:
```
nome = str(input('Qual seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome =='Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome))
```

- else é opcional:
```
nome = str(input('Qual seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome =='Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino.')

print('Tenha um bom dia {}!'.format(nome))
```


## Desafios:

***#036 -*** Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.


***#037 -*** Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
* (bases numéricas)

***#038 -*** Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior, os dois são iguais


***#039 -*** Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- se ele ainda vai see alistar ao serviço militar
- se é a hora de se alistar
- se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


***#040 -*** Crie um programa que leia dusa notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- média abaixo de 5.0: REPROVADO
- média entre 5.0 e 6.9: RECUPERAÇÃO
- média 7.0 ou superior: APROVADO


***#041 -*** A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- até 9 anos: MIRIM
- até 14 anos: INFANTIL
- até 19 anos: JUNIOR
- até 20 anos: SENIOR
- acima: MASTER


***#042 -*** Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes


***#043 -*** Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida

***#044 -*** Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro / cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros


***#045 -*** Crie um programa que faça o computador jogar Jokenpô com você.
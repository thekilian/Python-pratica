'''
#08 - Utilizando Módulos
- importar bibliotecas (recursos extras que adicionam funcionalidades)

import bebida = importa todas as bebidas
- importa todas as funcionalidades do módulo

from doce import pudim = importa um item da biblioteca apenas
- importa apenas as funcionalidades que forem escolhidas

Exemplo:
biblioteca math - funcionalidades:
    ceil - arredonda número para cima
    floor - arredonda número para baixo
    trunc (truncate) - eliminar da vírgula pra frente sem arredondar
    pow (power) - potência
    sqrt (square root) - calcular raíz quadrada
    factorial - cálculo de fatorial de um número

    import math - importa todas as funcionalidades
    from math import sqrt - importa só raíz quadrada (não poderei utilizar as outras funcionalidades)
    from math import sqrt, ceil - importa só raíz quadrada E ceil

# importar tudo
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))

# importar apenas sqrt
from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num) # não precisa digitar math.função
print('A raiz de {} é igual a {}'.format(num, raiz))

# importar apenas sqrt e floor
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num) # não precisa digitar math.função
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))

Para pesquisar as bibliotecas: python.org / docs / escolher versão Python - math

# importar números aleatórios
import random
num = random.random() // computador dizer n° aleatório entre 0 e 1
print(num)

import random
num = random.randint(1, 10) // randomizar n° inteiro de 1 a 10
print(num)

python.org
PyPI - Python package index (índice de pacotes extras) - lista enorme de pacotes que podemos importar. Tb podemos criar nossas pps bibliotecas, módulos e disponibilizar para a comunidade

import emoji
print(emoji.emojize("Olá, Mundo :earth_americas: !", use_aliases=True))
'''

'''
Desafios:
***Dica: procurar utilizar as bibliotecas corretas!***

# 016 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. (Ex.:
    Digite um número: 6.127
    O número 6.127 tem a parte inteira de 6.)

# 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

# 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

# 020 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# 021 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

'''
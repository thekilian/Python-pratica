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
'''

'''
# importar tudo
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
'''

'''
# importar apenas sqrt
from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num) # não precisa digitar math.função
print('A raiz de {} é igual a {}'.format(num, raiz))
'''

'''
# importar apenas sqrt
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num) # não precisa digitar math.função
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))
'''

'''
Para pesquisar as bibliotecas: python.org / docs / escolher versão Python - math
'''

'''
import random
num = random.random()
print(num)
'''

import random
num = random.randint(1, 10)
print(num)
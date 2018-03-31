'''
Operadores Aritméticos

+ Adição
- Subtração
* Multiplicação
/ Divisão
** Potência
// Divisão inteira ( divisão sem vírgula)
% Resto da divisão (módulo)

5 + 2 == 7
5 - 2 == 3
5 * 2 == 10
5 / 2 == 2.5
5 ** 2 == 25
5 // 2 == 2
5 % 2 == 1
'''

'''
print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 ** 2)
print(5 // 2)
print(5 % 2)
'''

'''
Ordem de precedência:
1. ()
2. **
3. * / // % (quem aparecer primeiro)
4. + -
'''

'''
print(5 + 3 * 2) # 11, não 16! Primeiro resolve *
print(3 * 5 + 4 ** 2) # 31, não 361!
print(3 * (5 + 4) ** 2) # 243
'''

'''
Potência pode ser feita com operador aritmético de potência ** e também pode ser feita com função interna de potência pow(). Quando usamos a função pow(), perdemos a ordem de precedência
'''

'''
print(4 ** 3)
print(pow(4,3))
'''

'''
Raíz Quadrada de 81 é 9
(9 vezes 9, 81. No tempo do burro seu pai era um hahahaha #guanabararules)
81**(1/2)
Forçando primeiro a calcular 1/2 que vai dar meio (0.5)
Calcular raiz quadrada de um número é a mesma coisa que criar a potência dele por meio
'''

'''
print(81**(1/2))
print(25**(1/2))
print(127**(1/3)) # raíz cúbica
'''

'''
Alguns operadores aritméticos podem ser utilizados com strings - deixam de ser operadores aritméticos, mas tb funcionam para strings
'''

'''
print('Oi' + 'Olá') # + não está somando, está concatenando
print('Oi' * 5)
print('=' * 20)
'''

'''
Replicar informações

nome = input('Qual seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))
'''

'''
# dar 20 espaços
nome = input('Qual seu nome? ')
print('Prazer em te conhecer, {:20}!'.format(nome))
'''

'''
# alinhar à direita
nome = input('Qual seu nome? ')
print('Prazer em te conhecer, {:>20}!'.format(nome))
'''

'''
# alinhar à esquerda
nome = input('Qual seu nome? ')
print('Prazer em te conhecer, {:<20}!'.format(nome))
'''

'''
# centralizar
nome = input('Qual seu nome? ')
print('Prazer em te conhecer, {:^20}!'.format(nome))
'''

'''
# adicionar sinal nos espaços
nome = input('Qual seu nome? ')
print('Prazer em te conhecer, {:=^20}!'.format(nome))
'''

'''
# se quiser ser mais explícito em relação ao tipo 
nome = str(input('Qual seu nome? '))
'''

'''
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}'.format(n1+n2))
# se eu quiser usar o resultado de n1+n2 depois, colacar em uma variável, ex s = n1 + n2 e no print, colocar .format(s)

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
print('A soma vale {}'.format(s))
'''

'''
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2 
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))
print('A divisão inteira é {} e a potência é {}'.format(di, e))
'''

# 14/12
'''
observer o print onde mostra a divisão. O formato para colcoar o números de casas é parecido com o %1.3f. Então fica {:.3f}
'''

'''
não quebrar a linha de um print para outro: end=''
'''

'''
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2 
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('A divisão inteira é {} e a potência é {}'.format(di, e))
'''

'''
tb posso quebrar a linha no meio do print: \n
'''

'''
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2 
print('A soma é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end=' ')
print('A divisão inteira é {} e a potência é {}'.format(di, e))
'''

'''
Desafios:

# 005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

# 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# 007 - Desenvolva um progama que leia as duas notas de um aluno, calcule e mostre a sua média.

# 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# 009 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

# 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere US$1,00 = R$3,27

# 011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

# 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# 014 - Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
 
# 015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.

'''
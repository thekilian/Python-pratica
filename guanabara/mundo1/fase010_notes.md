# 10 - Condições simples e compostas (parte 1)
- estrutura simples: ***if***
- estrutura composta: ***if + else***

Se a condição for verdadeira, executa o bloco de código identado do if; senão, executa o bloco de código identado do else. Apenas um dos blocos é executado.

Sintaxe:


```
# sintaxe:
if carro.esquerda():
    bloco True
else:
    bloco False
```

Exemplo de código:
```buildoutcfg
# exemplo:
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('carro novo :)')
else:
    print('carro velho :(')
print('---FIM---')

```

## Condição simplificada:

Outra maneira de fazer o mesmo código de maneira simplificada, utilizando apenas 3 linhas:


```
# condição simplificada:
tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <= 3 else 'carro velho')
print('---FIM---')
```

Embora Python não tenha, esta estrutura se assemelha ao operador ternário.

## Snippets:

```buildoutcfg
# snippet 1:
nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem! :)')
else:
    print('Seu nome é tão normal...')
print('Bom dia {}!'. format(nome))
```

```buildoutcfg
# snippet 2:
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))

if m >= 6.0:
    print('Sua média foi boa. Parabéns!')
else:
    print('Sua média foi ruim. ESTUDE MAIS!')
```

```buildoutcfg
# snippet 3 - simplificada:
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS!' if m >= 6 else 'ESTUDE MAIS!')
```

## Desafios:

***#028 -***
Escreva um programa que faça o computador "pensar"  em um número inteiro de 0 a 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.

***#029 -***
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.

***#030 -***
Crie um programa que leia um número inteiro e mostre na tela s ele é PAR ou ÍMPAR.

***#031 -***
Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

***#032 -***
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

***#033 -***
Faça um programa que leia três números e mostre qual é o ***maior*** e qual é o ***menor***.

***#034 -***
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.

***#035 -***
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
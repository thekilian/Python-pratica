# 09 - Manipulando Texto
- tratar/manipular cadeias de caracteres/texto = string
- aspas simples ou duplas (pode até ter aspas triplas)


```
frase = 'Curso em Vídeo Python'
```
(21 caracteres/micro espaços)

## Funcionalidades com strings:

***- FATIAMENTO:***
- no fatiamento, o último valor sempre é ignorado pelo Python


```
frase[9:13]
```
- pega os caracteres destas posições: inicia no 9 e termina no 13, mas não inclui o 13 (inclui o 9 e remove o 13)


```
frase[9:21:2]
 ```
- início no 9, paro no 21, mas vou pulando de 2 em 2


```
frase[:5]
```
- começa do caractere 0. É como se fosse ```frase[0:5]```


```
frase[15:]
```
- indiquei o início, mas não sei o final, então Python pega o final


```
frase[9::3]
```
- começa no 9, não sei onde é o final - pega pra mim Python heeh, e o :3 pula de 3 em 3

***- ANÁLISE:***
```
len(frase)
```
- comprimento da string


```
frase.count('o')
```
- conta quantas vezes a letras 'o' aparece


```
frase.count('o', 0, 13)
```
- contagem com fatiamento: considera do zero ao 13 (sem incluir o 13)


```
frase.find('deo')
```
- conta quantas encontra 'deo' -> retorna  11 pq é onde começa


```
frase.find('Android')
```
- retorna -1 pq esta string não existe na string de frase


```
'Curso' in frase
```
- existe a palavra 'Curso' em frase? Dentro de frase, existe a palavra? True, False (é um operador)


***- TRANSFORMAÇÃO:***

Via de regra, uma lista de string é imutável. Mas consigo mudá-la através de métodos. Não consigo mexer direto nos elementos, mas consigo através de métodos.


```
frase.replace('Python', 'Android')
```
- replace é substituir - vai buscar a palavra 'Python' e substituí-la por 'Android'


```
frase.upper()
```
- tudo maiúsculo (uppercase). upper() é método, precisa de () no final


```
frase.lower()
```
- tudo minúsculo (lowercase)


```
frase.capitalize()
```
- apenas primeira maiúscula de toda a frase


```
frase.title()
```
- analisa cada palavra baseado nos espaços e transforma as primeiras de cada palavra em maiúscula


* substituimos a string frase para '   Aprenda Python  ':

```
frase = '   Aprenda Python  '
```

```
frase.strip()
```
- remove todos os espaços inúteis no início e no final da string. O do meio será mantido


```
frase.rstrip()
```
- r = right (muitas funções que tratam strings dentro do Python tem a variação r) - só aplica na direita, removendo os espaços da direita e mantendo os da esquerda


```
frase.lstrip()
```
- l = left - só aplica na esquerda, removendo os espaços da esquerda e mantendo os da direita


***- DIVISÃO:***
* voltamos à string inicial:
```
frase = 'Curso em Vídeo Python'
```


```
frase.split()
```
- divisão da string, considerando os espaços, em uma lista
- podem ter parâmetros na função com outros separadores/caracteres
```
[str.split(sep=None, maxsplit=-1)]
```

[str.split(sep=None, maxsplit=-1)](https://docs.python.org/3/library/stdtypes.html?highlight=split#str.split)



***- JUNÇÃO:***
- análogo ao split()
- junta nomes que estão separados por listas de acordo com o separador indicado

```
'-'.join(frase)
```


## Desafios:

***#022 -*** Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas.
- O nome com todas as letras minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.


***#023 -*** Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Exemplo:
Digite um número: 1834

unidade: 4

dezena: 3

centena: 8

milhar: 1

* fazer o exercício como string e matematicamente


***#024 -*** Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".


***#025 -***
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.


***#026 -*** Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.


***#027 -*** Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

Exemplo: Ana Maria de Souza

primeiro = Ana

último = Souza
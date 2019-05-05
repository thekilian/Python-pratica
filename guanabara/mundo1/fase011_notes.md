# 11 - Cores no Terminal

(Existem vários módulo para isto, como o colorised. Veremos um padrão mais simples.)

***Padrão ANSI*** - padrão de normalização internacional.

Tem "escape sequence" que funciona em vários ambientes.

Comandos começam com contrabarra.

A que funciona melhor para o Python é o 033.

Sempre que você quiser representar uma cor em Python, use:
```buildoutcfg
\033[m
```

Entre o colchete e a letra "m", você deve adicionar o código da cor.

Três códigos podem ser inseridos entre eles:
- style
- text
- background

Eles devems er separados por ";":
```buildoutcfg
\033[0;33;44m
```

## Códigos para estilo:
***0***: sem estilo

***1***: negrito
 
***4***: sublinhado
 
***7***: inverte as configurações 

## Códigos para texto:
***30***: branco

***31***: vermelho

***32***: verde

***33***: amarelo

***34***: azul

***35***: magenta

***36***: ciano

***37***: cinza

## Códigos para background:
***40***: branco

***41***: vermelho

***42***: verde

***43***: amarelo

***44***: azul

***45***: magenta

***46***: ciano

***47***: cinza 

Existem vários outros códigos, mas os que funcionam melhor para o terminal Python são estes.

## Testes
1. letra branca, fundo vermelho
2. letra amarela sublinhada, fundo ciano
3. letra magenta, fundo amarelo
4. letra branca, fundo verde
5. letra cinza, fundo preto
6. letra preta, fundo branco

## Códigos:
1. \033[0;30;41m
2. \033[4;33;44m
3. \033[1;35;43m
4. \033[30;42m
5. \033[m
6. \033[7;30m

Obs.: 5 é a configuração padrão do terminal. 7 inverte.
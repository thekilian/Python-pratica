'''
- ler 3 palavras (uma em cada linha, com todas as letras minúsculas)

| Input Sample | Output Samples |
| ------------ | -------------- |
| vertebrado   | homem          |
| mamifero     |
| onivoro      |

| ------------ | ------ |
| vertebrado   | aguia  |
| ave          |
| carnivoro    |

| ------------ | ------- |
| invertebrado | minhoca |
| anelideo     |
| onivoro      |
'''

'''

1. vertebrado

    1.1. ave
        1.1.1. carnivoro
            1.1.1.1 aguia

        1.1.2. onivoro
            1.1.2.1. pomba

    1.2 mamifero
        1.2.1. onivoro
            1.2.1.1. homem

        1.2.2. herbivoro
            1.2.2.1. vaca

2. invertebrado

    2.1. inseto
        2.1.1. hematofago
            2.1.1.1 pulga

        2.1.2. herbivoro
            2.1.2.1. lagarta

    2.2 anelideo
        2.2.1. hematofago
            2.2.1.1. sanguessuga

        2.2.2. onivoro
            2.2.2.1. minhoca

'''

ossos = input()
classe = input()
alimentacao = input()

if ossos == 'vertebrado':
    if classe == 'ave':
        if alimentacao == 'carnivoro':
            print('aguia')
        elif alimentacao == 'onivoro':
            print('pomba')
    elif classe == 'mamifero':
        if alimentacao == 'onivoro':
            print('homem')
        elif alimentacao == 'herbivoro':
            print('vaca')

if ossos == 'invertebrado':
    if classe == 'inseto':
        if alimentacao == 'hematofago':
            print('pulga')
        elif alimentacao == 'herbivoro':
            print('lagarta')
    elif classe == 'anelideo':
        if alimentacao == 'hematofago':
            print('sanguessuga')
        elif alimentacao == 'onivoro':
            print('minhoca')
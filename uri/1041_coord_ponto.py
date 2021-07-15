'''
- determine qual o quadrante ao qual pertence o ponto

- ou se está sobre um dos eixos cartesianos: escreva “Eixo X” ou “Eixo Y”

- se o ponto estiver na origem (x = y = 0), escreva a mensagem “Origem”

| Input Sample | Output Samples |
| ------------ | -------------- |
| 4.5 -2.2     | Q4             |

| 0.1 0.1      | Q1             |

| 0.0 0.0      | Origem         |
'''

x, y = input().split()
x = float(x)
y = float(y)

if x > 0.0 and y > 0.0:
    print("Q1")
elif x < 0.0 and y > 0.0:
    print("Q2")
elif x < 0.0 and y < 0.0:
    print("Q3")
elif x > 0.0 and y < 0.0:
    print("Q4")
elif x == 0.0 and y == 0.0:
    print("Origem")
elif x == 0.0 and y != 0.0:
    print("Eixo Y")
elif x != 0.0 and y == 0.0:
    print("Eixo X")
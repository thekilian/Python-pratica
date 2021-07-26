'''
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
- se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
- se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
- se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
- se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
- se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
- se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

**Input**

A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

**Output**

Imprima todas as classificações do triângulo especificado na entrada.

| Input Sample | Output Samples         |
| ------------ | ---------------------- |
| 7.0 5.0 7.0  | TRIANGULO ACUTANGULO   |
|              | TRIANGULO ISOSCELES    | 
| ------------ | ---------------------- |
| 6.0 6.0 10.0 | TRIANGULO OBTUSANGULO  |
|              | TRIANGULO ISOSCELES    |
| ------------ | ---------------------- |
| 6.0 6.0 6.0  | TRIANGULO ACUTANGULO   |
|              | TRIANGULO EQUILATERO   |
| ------------ | ---------------------- |
| 5.0 7.0 2.0  | NAO FORMA TRIANGULO    |
| ------------ | ---------------------- |
| 6.0 8.0 10.0 | TRIANGULO RETANGULO    |
'''

triang = input().split()

n1 = float(triang[0])
n2 = float(triang[1])
n3 = float(triang[2])

result = n1, n2, n3
ordem = sorted(result, reverse=True)

a = ordem[0]
b = ordem[1]
c = ordem[2]

'''
#debug
print("n1 = {}".format(n1))
print("n2 = {}".format(n2))
print("n3 = {}".format(n3))
print("result = {}".format(result))
print("ordem = {}".format(ordem))
print("A = {}".format(a))
print("B = {}".format(b))
print("C = {}".format(c))
'''

tag = True

if a >= (b + c):
    tag = False
    print("NAO FORMA TRIANGULO")

if (a ** 2) == (b ** 2) + (c ** 2) and tag == True:
    print("TRIANGULO RETANGULO")

if (a ** 2) > (b ** 2) + (c ** 2) and tag == True:
    print("TRIANGULO OBTUSANGULO")

if (a ** 2) < (b ** 2) + (c ** 2) and tag == True:
    print("TRIANGULO ACUTANGULO")

if a == b and a == c and b == a and b == c and c == a and c == b and tag == True:
    print("TRIANGULO EQUILATERO")

if a == b and a != c or a == c and a != b or b == a and b!= c or b == c and b != a or c == b and c != a or c == a and c != b and tag == True:
    print("TRIANGULO ISOSCELES")
'''
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem: Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem: Area = XX.X

| Input Sample | Output Samples   |
| ------------ | ---------------- |
| 6.0 4.0 2.0  | Area = 10.0      |
| ------------ | ---------------- |
| 6.0 4.0 2.1  | Perimetro = 12.1 |

***

a, b, c = input().split()

if triangulo
    print(perimetro)
else
    print(area)

***

Só irá existir um triângulo se, e somente se, os seus lados obedeceram à seguinte regra: um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados:

| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b

***

perímetro do triângulo = soma de todos os lados

***

área do trapézio = ((a + b) * c) / 2

'''

a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    perimetro = a + b + c
    print("Perimetro = {:.1f}".format(perimetro))
else:
    area = ((a + b) * c) / 2
    print("Area = {:.1f}".format(area))
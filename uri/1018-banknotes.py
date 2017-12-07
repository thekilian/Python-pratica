nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0

n = int(input())
print(n)

while(n >= 100):
    nota100 += 1
    n -= 100

while(n >= 50):
    nota50 += 1
    n -= 50

while(n >= 20):
    nota20 += 1
    n -= 20

while(n >= 10):
    nota10 += 1
    n -= 10

while(n >= 5):
    nota5 += 1
    n -= 5

while(n >= 2):
    nota2 += 1
    n -= 2

while(n >= 1):
    nota1 += 1
    n -= 1

print("{} nota(s) de R$ 100,00".format(nota100))
print("{} nota(s) de R$ 50,00".format(nota50))
print("{} nota(s) de R$ 20,00".format(nota20))
print("{} nota(s) de R$ 10,00".format(nota10))
print("{} nota(s) de R$ 5,00".format(nota5))
print("{} nota(s) de R$ 2,00".format(nota2))
print("{} nota(s) de R$ 1,00".format(nota1))

'''
576
               | 5 nota(s) de R$ 100,00 |
               | 1 nota(s) de R$ 50,00  |
               | 1 nota(s) de R$ 20,00  |
               | 0 nota(s) de R$ 10,00  |
               | 1 nota(s) de R$ 5,00   |
               | 0 nota(s) de R$ 2,00   |
               | 1 nota(s) de R$ 1,00   |
'''
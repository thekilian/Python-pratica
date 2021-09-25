'''
Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

| Input Sample | Output Samples |
| ------------ | -------------- |
| 4            | April          |
'''

mes = int(input())

if mes == 1:
    print("January")
elif mes == 2:
    print("February")
elif mes == 3:
    print("March")
elif mes == 4:
    print("April")
elif mes == 5:
    print("May")
elif mes == 6:
    print("June")
elif mes == 7:
    print("July")
elif mes == 8:
    print("August")
elif mes == 9:
    print("September")
elif mes == 10:
    print("October")
elif mes == 11:
    print("November")
elif mes == 12:
    print("December")
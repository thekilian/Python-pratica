'''
# Lanche

Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

| CODE | SPECIFICATION   | PRICE  |
| 1    | Cachorro Quente | R$4.00 |
| 2    | X-Salada        | R$4.50 |
| 3    | X-Bacon         | R$5.00 |
| 4    | Torrada simples | R$2.00 |
| 5    | Refrigerante    | R$1.50 |

**Input**

O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

**Output**

O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

| Input Sample | Output Samples  |
| ------------ | --------------- |
| 3 2          | Total: R$ 10.00 |
| 4 3          | Total: R$ 6.00  |
| 2 3          | Total: R$ 13.50 |
'''

pedido = input().split(" ")
cod = pedido[0]
qtt = pedido[1]

cod1 = 4.00
cod2 = 4.50
cod3 = 5.00
cod4 = 2.00
cod5 = 1.50

if cod == "1":
    result = float(qtt) * cod1
    print("Total: R${:.2f}".format(result))
elif cod == "2":
    result = float(qtt) * cod2
    print("Total: R${:.2f}".format(result))
elif cod == "3":
    result = float(qtt) * cod3
    print("Total: R${:.2f}".format(result))
elif cod == "4":
    result = float(qtt) * cod4
    print("Total: R${:.2f}".format(result))
elif cod == "5":
    result = float(qtt) * cod5
    print("Total: R${:.2f}".format(result))
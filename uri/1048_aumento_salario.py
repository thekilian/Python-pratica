'''
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

| Salário           | Percentual de reajuste |
| ----------------- | ---------------------- |
| 0 - 400.00        | 15%                    | 
| 400.01 - 800.00   | 12%                    |
| 800.01 - 1200.00  | 10%                    |  
| 1200.01 - 2000.00 | 7%                     |
| Acima de 2000.00  | 4%                     |

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.


| Input Sample | Output Samples         |
| ------------ | ---------------------- |
| 400.00       | Novo salario: 460.00   |
|              | Reajuste ganho: 60.00  |
|              | Em percentual: 15 %    |
| ------------ | ---------------------- |
| 800.01       | Novo salario: 880.01   | 
|              | Reajuste ganho: 80.00  | 
|              | Em percentual: 10 %    |
| ------------ | ---------------------- |
| 2000.00      | Novo salario: 2140.00  |
|              | Reajuste ganho: 140.00 | 
|              | Em percentual: 7 %     |
'''
# Aplicar um desconto de 20% nada mais é que multiplicar o valor por 0,2 

salario = float(input())

if salario > 0 and salario <= 400.00:
    reaj = salario * 0.15
    perc = 15
elif salario >= 400.01 and salario <= 800.00:
    reaj = salario * 0.12
    perc = 12
elif salario >= 800.01 and salario <= 1200.00:
    reaj = salario * 0.1
    perc = 10
elif salario >= 1200.01 and salario <= 2000.00:
    reaj = salario * 0.07
    perc = 7
elif salario > 2000.00:
    reaj = salario * 0.04
    perc = 4

novo = salario + reaj

print("Novo salario: {:.2f}".format(novo))
print("Reajuste ganho: {:.2f}".format(reaj))
print("Em percentual: {} %".format(perc))
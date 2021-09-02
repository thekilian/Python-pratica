'''
Leia um valor com duas casas decimais, equivalente ao salário e calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda

| Renda  | Imposto de renda |

| de 0.0 a R$ 2000.00          | Isento |
| de R$ 2000.01 até R$ 3000.00 | 8 %    |
| de R$ 3000.01 até R$ 4500.00 | 18 %   |
| acima de R$ 4500.00          | 28 %   |

Lembre que, se o salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre R$ 1000.00, pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda. No exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, o que resulta em R$ 80.36 no total. O valor deve ser impresso com duas casas decimais.

| Input Sample | Output Samples |
| ------------ | -------------- |
| 3002.00      | R$ 80.36       |
| 1701.12      | Isento         |
| 4520.00      | R$ 355.60      |
'''

salario = float(input())
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

if salario >= 0.0 and salario <= 2000.00:
    print("Isento")
elif salario >= 2000.01 and salario <= 3000.00:
    imposto = salario - (salario * 92 / 100)
    print("R$ {}".format(imposto)) # 8%
elif salario >= 3000.01 and salario <= 4500.00:
    imposto = salario - (salario * 82 / 100)
    print("R$ {}".format(imposto)) # 18%
elif salario >= 4500.01:
    imposto = salario - (salario * 72 / 100)
    print("R$ {}".format(imposto)) # 28%

# resposta internet
r = float(input())

if r <= 2000.00:
    i = 0
    print('Isento')
    
if 2000.00 < r <= 3000.00:
    r8 = r - 2000.00
    i = r8 * (8 / 100)
    
if 3000.00 < r <= 4500.00:
    i8 = (8 / 100) * (1000.00)
    r18 = r - 3000.00
    i = r18 * (18 / 100) + i8
    
if r > 4500.00:
    i8 = (8 / 100) * (1000.00)
    i18 = (18 / 100) * (1500.00)
    r28 = r - 4500.00
    i = i18 + i8 + r28 * (28 / 100)

if r > 2000.00:
    i = float(i)
    print('R$ {:.2f}'.format(i))


# ota
a=float(input())
if(0<a<=2000):
    print("Isento")
elif(2000<a<=3000):
    t= (a-2000)
    tx= (t*8)/100
    print("R$ %.2f"%tx)
elif(3000<a<=4500):
    t= (a-2000)
    t1=t-1000
    tx1=(1000*8)/100
    tx2= (t1*18)/100
    print("R$ %.2f"%(tx1+tx2))
else:
    t= (a-2000)
    t1= t-1000
    tx1= (1000*8)/100
    t2=t1-1500
    tx2=(1500*18)/100
    tx= (t2*28)/100
    print("R$ %.2f" %(tx+tx1+tx2))
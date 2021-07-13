'''
# Teste de Seleção 1

Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

**Input**
Quatro números inteiros A, B, C e D.

**Output**
Mostre a respectiva mensagem após a validação dos valores.

| Input Sample | Output Samples      |
| ------------ | ------------------- |
| 5 6 7 8      | Valores nao aceitos |
| 2 3 2 6      | Valores aceitos     |
'''

valores = input().split(" ")

a = int(valores[0])
b = int(valores[1])
c = int(valores[2])
d = int(valores[3])

if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")